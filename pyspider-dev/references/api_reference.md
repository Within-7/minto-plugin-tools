# PySpider API Reference

## BaseHandler

The base class for all PySpider crawlers.

### Configuration

```python
crawl_config = {
    'connect_timeout': 2,  # Connection timeout in seconds
    'timeout': 30,         # Request timeout in seconds
    'retries': 5,          # Number of retry attempts
    'age': 0              # Cache age (0 = no cache)
}
```

### Core Methods

#### `on_start()`

Entry point for the crawler. Called when the crawler starts.

```python
def on_start(self):
    self.crawl('https://example.com', callback=self.process)
```

#### `on_message(project, message)`

Handle messages from other projects.

```python
def on_message(self, project, message):
    if project == self.project_name:
        return message
    # Process message
```

#### `crawl(url, **kwargs)`

Initiate an HTTP request.

**Parameters:**
- `url` (str): Target URL
- `callback` (method): Function to handle response
- `method` (str): HTTP method (GET, POST, etc.)
- `headers` (dict): Request headers
- `data` (dict): POST data
- `proxy` (str): Proxy configuration
- `save` (dict): Data to pass to callback
- `priority` (int): Task priority (higher = earlier)
- `taskid` (str): Unique task identifier
- `force_update` (bool): Force update ignoring cache
- `validate_cert` (bool): Validate SSL certificate

```python
self.crawl(
    'https://example.com',
    method='GET',
    headers={'User-Agent': 'Mozilla/5.0'},
    proxy='auto',
    save={'key': 'value'},
    priority=10,
    taskid=f"{url}|{time.time()}",
    callback=self.process_response
)
```

#### `send_message(project, message, url=None)`

Send a message to another project.

```python
self.send_message(
    self.project_name,
    {'data': 'value'},
    url=f'data:,on_message?key=value'
)
```

## Response Object

Passed to callback functions.

### Properties

- `response.url` - The actual URL (after redirects)
- `response.text` - Response body as text
- `response.content` - Response body as bytes
- `response.json` - Parsed JSON response
- `response.ok` - Boolean indicating success
- `response.status_code` - HTTP status code
- `response.headers` - Response headers
- `response.save` - Data passed via `save` parameter
- `response.cookies` - Response cookies
- `response.time` - Request duration in seconds

### Methods

#### `response.doc`

PyQuery object for HTML parsing (jQuery-like syntax).

```python
# Select elements
response.doc('h1.title').text()
response.doc('a.link').attr.href

# Iterate
for item in response.doc('.item').items():
    print(item.text())

# Nested queries
response.doc('.container .content').text()

# Attributes
response.doc('img').attr.src
response.doc('a').attr.href
```

#### `response.json`

Access parsed JSON response.

```python
data = response.json
for item in data['results']:
    print(item['title'])
```

## Database

### `database.connect_database(config)`

Connect to MongoDB for result storage.

```python
from pyspider import database

RESULTDB = database.connect_database({
    'host': 'localhost',
    'port': 27017,
    'database': 'results'
})
```

### `RESULTDB.save(project, data)`

Save data to database.

```python
RESULTDB.save('MyProject', {
    'url': 'https://example.com',
    'title': 'Example'
})
```

### `RESULTDB.select(project, **kwargs)`

Query data from database.

```python
# Simple query
results = RESULTDB.select('MyProject')

# With filter
results = RESULTDB.select('MyProject', 
    filter={'url': 'https://example.com'}
)

# With limit
results = RESULTDB.select('MyProject', limit=10)
```

## Proxy Management

### Built-in Proxy Types

```python
# Auto proxy (built-in pool)
__PROXY = 'auto'

# Static proxy
__PROXY = 'http://proxy.example.com:8080'

# SOCKS proxy
__PROXY = 'socks5://127.0.0.1:1080'

# No proxy
__PROXY = None
```

### Custom Proxy Pool

```python
class ProxyPool:
    def get_proxy(self):
        # Return proxy string
        return 'http://proxy.example.com:8080'

__PROXY = ProxyPool()
```

## Logging

```python
import logging

myLogger = logging.getLogger('handler_screen')

myLogger.info('Info message')
myLogger.warning('Warning message')
myLogger.error('Error message')
```

## Helper Modules

### `urllib.parse`

URL manipulation.

```python
import urllib.parse

# Encode query parameters
query = urllib.parse.urlencode({'q': 'search term', 'page': 1})
url = f'https://example.com/search?{query}'

# Parse URL
parsed = urllib.parse.urlparse('https://example.com/path?param=value')
```

### `re`

Regex operations.

```python
import re

# Find all matches
matches = re.findall(r'<div>(.*?)</div>', text, re.DOTALL)

# Search with groups
match = re.search(r'(\d+) results', text)
if match:
    count = match.group(1)

# Replace
text = re.sub(r'\s+', ' ', text)
```

### `time`

Time utilities.

```python
import time

# Current timestamp
timestamp = time.time()

# Sleep
time.sleep(1)

# Format time
formatted = time.strftime('%Y-%m-%d %H:%M:%S')
```

## Common Patterns

### Retry Logic

```python
def fetch_with_retry(self, url, retry=0):
    self.crawl(
        url,
        save={'retry': retry},
        callback=self.handle_response
    )

def handle_response(self, response):
    retry = response.save.get('retry', 0)
    
    if not response.ok and retry < 3:
        time.sleep(2 ** retry)
        self.fetch_with_retry(response.url, retry + 1)
```

### Pagination

```python
def crawl_page(self, page=1):
    url = f'https://example.com/list?page={page}'
    self.crawl(url, save={'page': page}, callback=self.process_page)

def process_page(self, response):
    page = response.save['page']
    # Extract data...
    if page < self.MAX_PAGES:
        self.crawl_page(page + 1)
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
