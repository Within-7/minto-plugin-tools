# PySpider API Reference

Complete API reference for PySpider framework with standard patterns.

## BaseHandler

The base class for all PySpider crawlers.

### crawl_config

Global configuration that applies to all requests.

```python
crawl_config = {
    # Request settings
    'user_agent': 'Mozilla/5.0...',     # Default User-Agent
    'headers': {},                       # Global request headers
    'timeout': 30,                       # Request timeout (seconds)
    'connect_timeout': 10,               # Connection timeout (seconds)
    
    # Retry and caching
    'retries': 5,                        # Retry attempts
    'age': 0,                           # Cache age (0 = no cache)
    'itag': 'v1',                       # Version tag (changes trigger re-crawl)
    
    # Proxy and SSL
    'proxy': 'http://user:pass@ip:port', # Global proxy
    'validate_cert': True,               # SSL certificate validation
    
    # JavaScript rendering
    'fetch_type': 'html',                # 'html' or 'js' (requires PhantomJS)
    'js_run_at': 'document-end',         # JS execution timing
    'js_script': '',                     # Custom JS to execute
}
```

### Decorators

#### @every

Schedule periodic execution.

```python
@every(minutes=60)              # Every hour
@every(hours=2)                 # Every 2 hours
@every(days=1)                  # Daily
def on_start(self):
    pass
```

**Note**: If using with `@config(age=...)`, when age is shorter than @every interval, requests may be skipped as "unchanged".

#### @config

Configure default parameters for all requests from a callback.

```python
@config(age=10*24*60*60)        # Cache for 10 days
@config(priority=2)             # Priority level (0-9)
@config(retries=3)              # Override retry count
def callback(self, response):
    pass
```

All `self.crawl()` calls within this callback inherit these defaults.

#### @catch_status_code_error

By default, non-200 status codes are treated as failures and callbacks are NOT called. Use this decorator to receive non-200 responses in callbacks.

```python
@catch_status_code_error
def callback(self, response):
    # Even if status_code is 404, 500, etc., this will be called
    if response.status_code == 404:
        print(f"Not found: {response.url}")
    elif response.status_code == 500:
        print(f"Server error: {response.url}")
```

## Core Methods

### on_start(self)

Required entry point - called when crawler starts.

```python
def on_start(self):
    self.crawl('https://example.com', callback=self.parse)
```

### on_result(self, result)

⚠️ **DEPRECATED / NOT SUPPORTED** - This method is not supported in PySpider. Use `on_message` instead for data storage and inter-project communication.

**Correct approach** - Use `on_message`:
```python
def on_message(self, project, message):
    if project == self.project_name:
        return message
    # Save to database
    # self.RESULTDB.save(self.DB_NAME, message)
```

### on_error(self, exception, response)

Optional - handles errors with retry logic.

```python
def on_error(self, exception, response):
    error_info = {
        'url': response.url if response else 'N/A',
        'error': str(exception),
        'timestamp': time.time()
    }
    # Implement retry logic
    if hasattr(response, 'save') and response.save.get('retry_count', 0) < 3:
        self.crawl(response.url, save={**response.save, 'retry_count': 1})
```

### on_message(self, project, message)

Handle inter-project messages.

```python
def on_message(self, project, message):
    if project == self.project_name:
        return message
    if 'url' in message:
        self.crawl(message['url'], callback=self.process)
```

### crawl(url, **kwargs)

Initiate HTTP request.

| Parameter | Type | Description |
|-----------|------|-------------|
| `url` | str/list | Target URL (or list of URLs) |
| `callback` | method | Response handler |
| `method` | str | HTTP method: 'GET', 'POST', 'PUT', 'DELETE' |
| `params` | dict | GET parameters → URL query string |
| `data` | dict/str | POST data: dict=form, str=JSON |
| `headers` | dict | Request headers |
| `cookies` | dict | Request cookies |
| `proxy` | str | 'http://user:pass@ip:port' |
| `timeout` | int | Request timeout (seconds, default: 120) |
| `connect_timeout` | int | Connection timeout (seconds, default: 20) |
| `save` | dict | State passed to callback |
| `priority` | int | Task priority (0-9, higher first) |
| `taskid` | str | Unique task ID (default: URL MD5) |
| `age` | int | Cache time in seconds (default: -1) |
| `retries` | int | Retry attempts (default: 3) |
| `exetime` | int | Schedule execution time (unix timestamp) |
| `itag` | str | Version tag (changes trigger re-crawl) |
| `auto_recrawl` | bool | Auto re-crawl after age expires |
| `force_update` | bool | Force update even if ACTIVE |
| `cancel` | bool | Cancel task |
| `validate_cert` | bool | SSL verification (default: True) |
| `allow_redirects` | bool | Follow 30x redirects (default: True) |
| `fetch_type` | str | 'html' or 'js' (requires PhantomJS) |
| `js_script` | str | JavaScript to execute |
| `js_run_at` | str | JS timing: 'document-start' or 'document-end' |
| `js_viewport_width` | int | JS viewport width |
| `js_viewport_height` | int | JS viewport height |
| `load_images` | bool | Load images in JS mode (default: False) |
| `files` | dict | Upload files: {field: {filename: 'content'}} |
| `etag` | bool | Enable ETag mechanism (default: True) |
| `last_modified` | bool | Enable Last-Modified (default: True) |

```python
# GET with parameters
self.crawl(
    'https://api.example.com/data',
    params={'page': 1, 'size': 20},
    callback=self.parse_data
)

# POST JSON
self.crawl(
    'https://api.example.com/login',
    method='POST',
    data=json.dumps({'user': 'test'}),
    headers={'Content-Type': 'application/json'},
    callback=self.parse_login
)

# POST Form
self.crawl(
    'https://example.com/search',
    method='POST',
    data={'search': 'keyword'},  # Dict for form
    callback=self.parse_search
)

# With proxy and headers
self.crawl(
    'https://example.com',
    headers={'User-Agent': 'Mozilla/5.0'},
    proxy='http://proxy:8080',
    callback=self.parse_page
)

# With state (pagination)
self.crawl(
    'https://example.com/page/2',
    save={'page': 2},
    callback=self.parse_page
)

# JavaScript rendering (requires PhantomJS)
self.crawl(
    'https://example.com',
    fetch_type='js',
    js_script='''
    function() {
        window.scrollTo(0, document.body.scrollHeight);
        return document.title;
    }
    ''',
    js_run_at='document-end',
    callback=self.parse_js_page
)

# Schedule delayed execution (30 minutes later)
import time
self.crawl(
    'https://example.com',
    exetime=time.time() + 30*60,
    callback=self.parse_page
)
```

### cURL Command Support

PySpider can parse cURL commands directly. Copy "Copy as cURL" from Chrome DevTools and pass to `self.crawl()`.

```python
# Chrome DevTools → Network → Right click request → Copy as cURL
curl_command = '''curl 'https://example.com/api' \
  -H 'Authorization: Bearer token123' \
  -H 'Content-Type: application/json' \
  --data-raw '{"key":"value"}' '''

# Pass directly to self.crawl
self.crawl(curl_command, callback=self.parse_response)
```

PySpider automatically extracts: URL, method, headers, data, cookies from the cURL string.

### send_message(project, message, url=None)

Send message to another project.

```python
# Send with URL for unique taskid
self.send_message(
    self.project_name,
    {'data': 'value'},
    url=f'data:,on_message?key=value'
)

# Send multiple items from array
def detail_page(self, response):
    for i, item in enumerate(response.json['products']):
        self.send_message(
            'other_project',
            {'name': item['name'], 'price': item['price']},
            url=f"{response.url}#{i}"
        )
```

**Command line alternative**:
```bash
pyspider send_message project_name '{"key": "value"}'
```

## Response Object

Passed to callback functions.

### Properties

```python
response.url              # Actual URL (after redirects)
response.text             # Response body as text (auto-detected encoding)
response.content          # Response body as bytes
response.json             # Parsed JSON (auto-parsed if Content-Type is JSON)
response.ok               # Boolean: status_code == 200 and no error
response.status_code      # HTTP status code
response.headers          # Response headers (case-insensitive dict)
response.cookies          # Response cookies
response.time             # Request duration (seconds)
response.save             # Data passed via `save` parameter
response.orig_url         # Original URL before redirects
response.error            # Error message if failed
response.encoding         # Response encoding (can be set manually)
```

### response.doc

PyQuery object for HTML parsing (jQuery-like syntax, links auto-converted to absolute).

```python
# Text content
title = response.doc('title').text()
content = response.doc('.content').text()

# Attributes
link = response.doc('a.link').attr('href')
src = response.doc('img').attr('src')

# Iterate
for item in response.doc('.item').items():
    title = item.find('.title').text()
    link = item.find('a').attr('href')

# Nested selectors
response.doc('.container .content .title').text()

# Filters
response.doc('a[href^="http"]').items()     # Starts with
response.doc('a[href$=".pdf"]').items()     # Ends with
response.doc('a[href*="example"]').items()  # Contains

# Index
response.doc('.item').eq(0).text()          # First item
response.doc('.item').eq(-1).text()         # Last item
```

### response.etree

lxml element tree for XPath parsing.

```python
# XPath queries
title = response.etree.xpath('//title/text()')[0]
links = response.etree.xpath('//a/@href')

# With namespaces
namespaces = {'ns': 'http://www.w3.org/1999/xhtml'}
items = response.etree.xpath('//ns:div/ns:p', namespaces=namespaces)

# Get element text
element = response.etree.xpath('//h1[@class="title"]')[0]
title_text = element.text
```

### response.json

Access parsed JSON response.

```python
# Direct access (auto-parsed if Content-Type is JSON)
data = response.json
results = data.get('results', [])
for item in results:
    print(item['title'])

# Manual parsing (if auto-parse fails)
import json
try:
    data = json.loads(response.text)
except:
    data = {}

# Check if JSON is available
if hasattr(response, 'json'):
    print(response.json)
```

### response.js_script_result

When using `fetch_type='js'` with `js_script` that returns a value.

```python
# In crawl request
self.crawl(
    'https://example.com',
    fetch_type='js',
    js_script='''
    function() {
        window.scrollTo(0, document.body.scrollHeight);
        return {
            title: document.title,
            height: document.body.scrollHeight
        };
    }
    ''',
    callback=self.parse
)

# In callback
def parse(self, response):
    result = response.js_script_result
    print(result['title'])   # JS return value
    print(result['height'])  # JS return value
```

### Methods

#### response.raise_for_status()

Raise HTTPError if status_code != 200 or error exists.

```python
def parse(self, response):
    response.raise_for_status()  # Raises if not 200 or has error
    # Continue processing...
```

**Alternative: Manual check**
```python
def parse(self, response):
    if not response.ok:
        print(f"Error: {response.status_code} - {response.error}")
        return
    # Continue...


## Database

### Connect to MongoDB

```python
from pyspider import database

RESULTDB = database.connect_database({
    'host': 'localhost',
    'port': 27017,
    'database': 'results'
})

DB_NAME = 'MyCrawler'
```

### RESULTDB.save(project, data)

Save data to database.

```python
RESULTDB.save(DB_NAME, {
    'url': 'https://example.com',
    'title': 'Example',
    'timestamp': time.time()
})
```

### RESULTDB.select(project, **kwargs)

Query data from database.

```python
# All results
results = list(RESULTDB.select(DB_NAME))

# With filter
results = list(RESULTDB.select(
    DB_NAME,
    filter={'url': 'https://example.com'}
))

# With limit
results = list(RESULTDB.select(DB_NAME, limit=10))

# Count
count = RESULTDB.select(DB_NAME).count()
```

## Proxy Management

### Proxy Types

```python
# Auto proxy (built-in pool)
proxy = 'auto'

# Static proxy
proxy = 'http://proxy.example.com:8080'
proxy = 'http://username:password@proxy.example.com:8080'

# SOCKS proxy
proxy = 'socks5://127.0.0.1:1080'

# No proxy
proxy = None
```

### Proxy Pool Pattern

```python
class Handler(BaseHandler):
    PROXY_POOL = [
        'http://user1:pass1@192.168.1.100:8080',
        'http://user2:pass2@192.168.1.101:8080',
    ]
    
    def get_random_proxy(self):
        return random.choice(self.PROXY_POOL)
    
    def on_start(self):
        self.crawl(
            'https://example.com',
            proxy=self.get_random_proxy(),
            callback=self.parse
        )
```

### Proxy Rotation on Retry

```python
def on_error(self, exception, response):
    retry_count = response.save.get('retry_count', 0)
    if retry_count < 3:
        self.crawl(
            response.url,
            save={**response.save, 'retry_count': retry_count + 1},
            proxy=self.PROXY_POOL[retry_count % len(self.PROXY_POOL)]
        )
```

## Header Management

### User-Agent Pool

```python
class Handler(BaseHandler):
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91...',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/91...',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6) Mobile/15E148...',
    ]
    
    def get_random_user_agent(self):
        return random.choice(self.USER_AGENTS)
    
    def get_headers(self):
        return {
            'User-Agent': self.get_random_user_agent(),
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
        }
```

### Bearer Token Pattern

```python
def parse_login(self, response):
    token = response.json.get('token')
    # Use in subsequent requests
    self.crawl(
        'https://api.example.com/profile',
        headers={'Authorization': f'Bearer {token}'},
        callback=self.parse_profile
    )
```

## Common Patterns

### Pagination

```python
def crawl_page(self, page=1):
    self.crawl(
        f'https://example.com/list?page={page}',
        save={'page': page},
        callback=self.process_page
    )

def process_page(self, response):
    page = response.save['page']
    # Extract data...
    
    # Next page
    if page < 10:
        self.crawl_page(page + 1)
```

### Retry with Exponential Backoff

```python
def on_error(self, exception, response):
    retry_count = response.save.get('retry_count', 0)
    if retry_count < 3:
        time.sleep(2 ** retry_count)  # 1, 2, 4 seconds
        self.crawl(
            response.url,
            save={**response.save, 'retry_count': retry_count + 1}
        )
```

### Data Deduplication

```python
def process_url(self, url):
    existing = list(self.RESULTDB.select(
        self.DB_NAME,
        filter={'url': url}
    ))
    
    if not existing:
        self.crawl(url, callback=self.extract_data)
```

### Task ID Uniqueness

```python
# Use timestamp to prevent cache hits
self.crawl(
    url,
    taskid=f"{url}|{time.time()}",
    callback=self.parse
)
```

### Link Extraction

```python
def extract_links(self, response):
    # All HTTP links
    for link in response.doc('a[href^="http"]').items():
        url = link.attr('href')
        self.crawl(url, callback=self.parse_page)
    
    # Relative links
    for link in response.doc('a[href]').items():
        href = link.attr('href')
        full_url = urllib.parse.urljoin(response.url, href)
        self.crawl(full_url, callback=self.parse_page)
```

### Form Handling

```python
def submit_form(self, response):
    # Extract form action
    action = response.doc('form').attr('action')
    
    # Extract form data
    data = {}
    for input_field in response.doc('form input').items():
        name = input_field.attr('name')
        value = input_field.attr('value') or ''
        data[name] = value
    
    # Submit
    self.crawl(
        action,
        method='POST',
        data=data,
        callback=self.parse_form_result
    )
```

## Helper Modules

### urllib.parse

```python
import urllib.parse

# Build URL with parameters
params = {'q': 'search', 'page': 1}
query = urllib.parse.urlencode(params)
url = f'https://example.com/search?{query}'

# Join URLs
full_url = urllib.parse.urljoin(base_url, relative_path)

# Parse URL
parsed = urllib.parse.urlparse(url)
domain = parsed.netloc
path = parsed.path
```

### re

```python
import re

# Find all
matches = re.findall(r'<div>(.*?)</div>', text, re.DOTALL)

# Search with groups
match = re.search(r'(\d+) results', text)
if match:
    count = int(match.group(1))

# Extract email
emails = re.findall(r'[\w.]+@[\w.]+', text)

# Clean text
text = re.sub(r'\s+', ' ', text)
```

### time

```python
import time

# Timestamp
timestamp = time.time()

# Sleep
time.sleep(1)

# Format
formatted = time.strftime('%Y-%m-%d %H:%M:%S')
```

### json

```python
import json

# Parse
data = json.loads(response.text)

# Dump
json_string = json.dumps(data, ensure_ascii=False)
```

## Logging

```python
import logging

myLogger = logging.getLogger('handler_screen')

myLogger.debug('Debug message')
myLogger.info('Info message')
myLogger.warning('Warning message')
myLogger.error('Error message')
```
