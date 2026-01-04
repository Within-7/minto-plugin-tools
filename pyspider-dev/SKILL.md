---
name: pyspider-dev
description: Guide for developing PySpider web crawlers. Covers GET/POST requests, proxy management, header rotation, error handling, pagination, and enterprise-grade crawling patterns. Includes standard templates with detailed explanations.
---

# PySpider Development

## Overview

PySpider is a powerful web crawling framework. This skill provides production-ready patterns covering GET/POST requests, proxy pools, dynamic headers, error handling, and enterprise-level crawling strategies.

## Core Architecture

Every PySpider crawler inherits from `BaseHandler`:

**Required Methods**:
- `on_start()`: Entry point - initiate crawling tasks
- `callback functions`: Process HTTP responses

**Optional Methods**:
- `on_message(project, message)`: Handle inter-project messages and data storage
- `on_error(exception, response)`: Handle errors with retry logic

## ⚠️ 重要警告

**PySpider 中没有 `on_result` 方法！**

- ❌ **错误**: `def on_result(self, result):`
- ✅ **正确**: `def on_message(self, project, message):`

所有代码必须使用 `on_message` 方法来处理跨项目消息和数据存储。**严禁使用 `on_result`**，因为 PySpider 框架根本不支持这个方法。

**Optional Decorators**:
- `@every(minutes=60)`: Only add when scheduled execution is explicitly required
- `@config(priority=2)`: Only add when priority is specifically specified
- `@config(age=...)`: Cache time in seconds (commonly used)

```python
from pyspider.libs.base_handler import *

class Handler(BaseHandler):
    crawl_config = {
        'user_agent': 'Mozilla/5.0...',
        'timeout': 60,
        'connect_timeout': 10,
    }
    
    def on_start(self):
        self.crawl('https://example.com', callback=self.parse)
    
    def parse(self, response):
        return {'url': response.url, 'title': response.doc('title').text()}
```

## Quick Start Templates

### 1. Standard GET Request Crawler (Basic)

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2024-01-04
# Project: standard_spider

from pyspider.libs.base_handler import *

class Handler(BaseHandler):
    # Global config - applies to all requests
    crawl_config = {
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'headers': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        },
        'timeout': 60,
        'connect_timeout': 10,
        'validate_cert': True,
        'itag': 'v1',  # Version tag - changes trigger re-crawl
    }
    
    def on_start(self):
        """Entry point - initiate crawling tasks (REQUIRED)"""
        self.crawl('https://httpbin.org/get', callback=self.parse_page)
    
    def on_message(self, project, message):
        """Handle inter-project messages and data storage (REQUIRED)"""
        if project == self.project_name:
            return message
        # Process message from other projects
        return message
    
    @config(age=10 * 24 * 60 * 60)  # Cache 10 days
    def parse_page(self, response):
        """Parse page callback - receives Response object"""
        title = response.doc('title').text()
        
        # Extract and crawl links
        for each in response.doc('a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.parse_page)
        
        return {
            'url': response.url,
            'title': title,
            'status_code': response.status_code,
        }
```

### 2. POST Request with Proxy (Advanced)

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2024-01-04
# Project: post_spider_with_proxy

from pyspider.libs.base_handler import *
import json

class Handler(BaseHandler):
    crawl_config = {
        'user_agent': 'Mozilla/5.0...',
        'headers': {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        },
        'timeout': 30,
        'proxy': 'http://username:password@proxy_ip:port',  # Global proxy
    }
    
    proxy_pool = [
        'http://proxy1:port',
        'http://proxy2:port',
    ]
    
    def on_start(self):
        # GET with params
        self.crawl(
            'https://api.example.com/data',
            params={'page': 1, 'size': 20},  # GET parameters
            callback=self.parse_get_data,
            proxy=self.proxy_pool[0]
        )
        
        # POST JSON
        self.crawl(
            'https://api.example.com/login',
            method='POST',  # HTTP method (default: GET)
            data=json.dumps({'user': 'test'}),  # String for JSON
            headers={'Content-Type': 'application/json'},
            callback=self.parse_login
        )
        
        # POST Form
        self.crawl(
            'https://example.com/search',
            method='POST',
            data={'search': 'python'},  # Dict for form data
            callback=self.parse_search
        )
    
    def parse_get_data(self, response):
        data = response.json  # Auto-parse JSON
        # Pagination with save state
        current_page = response.save.get('page', 1)
        if current_page < 10:
            self.crawl(
                'https://api.example.com/data',
                params={'page': current_page + 1, 'size': 20},
                callback=self.parse_get_data,
                save={'page': current_page + 1}
            )
        return data
    
    def parse_login(self, response):
        login_result = response.json
        if login_result.get('success'):
            token = login_result.get('token')
            # Use token in subsequent requests
            self.crawl(
                'https://api.example.com/profile',
                headers={'Authorization': f'Bearer {token}'},
                callback=self.parse_profile
            )
        return login_result
```

### 3. Dynamic Proxy + Header Rotation (Enterprise)

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2024-01-04
# Project: enterprise_spider

from pyspider.libs.base_handler import *
import random
import time

class Handler(BaseHandler):
    PROXY_POOL = [
        'http://user1:pass1@192.168.1.100:8080',
        'http://user2:pass2@192.168.1.101:8080',
    ]
    
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91...',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/91...',
    ]
    
    crawl_config = {
        'timeout': 45,
        'fetch_type': 'js',  # Enable JS rendering (requires PhantomJS)
        'js_run_at': 'document-end',
    }
    
    def get_random_proxy(self):
        return random.choice(self.PROXY_POOL)
    
    def get_random_user_agent(self):
        return random.choice(self.USER_AGENTS)
    
    def get_headers(self):
        return {
            'User-Agent': self.get_random_user_agent(),
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
    
    def on_start(self):
        self.crawl(
            'https://httpbin.org/get',
            headers=self.get_headers(),
            proxy=self.get_random_proxy(),
            callback=self.parse_response
        )
    
    def parse_response(self, response):
        return {
            'url': response.url,
            'status': response.status_code,
            'data': response.json if hasattr(response, 'json') else {},
        }
    
    def on_error(self, exception, response):
        """Error handler with retry logic"""
        if hasattr(response, 'save') and response.save.get('retry_count', 0) < 3:
            self.crawl(
                response.url,
                save={**response.save, 'retry_count': response.save.get('retry_count', 0) + 1},
                proxy=self.get_random_proxy()
            )
```

## Key Parameters Reference

### `self.crawl()` Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `url` | str | Target URL |
| `callback` | function | Response handler |
| `method` | str | 'GET', 'POST', 'PUT', 'DELETE' (default: GET) |
| `params` | dict | GET parameters → URL query string |
| `data` | dict/str | POST data: dict=form, str=JSON |
| `headers` | dict | HTTP request headers |
| `proxy` | str | 'http://user:pass@ip:port' |
| `timeout` | int | Timeout in seconds |
| `save` | dict | State passed to callback |
| `priority` | int | Task priority (higher = priority) |

### `crawl_config` Options

| Option | Description |
|--------|-------------|
| `user_agent` | Default User-Agent |
| `headers` | Global request headers |
| `timeout` | Request timeout |
| `connect_timeout` | Connection timeout |
| `proxy` | Global proxy |
| `fetch_type` | 'js' or 'html' |
| `itag` | Version tag |
| `validate_cert` | SSL verification |

### Response Object Attributes

```python
response.url          # Request URL
response.text         # Response text
response.content      # Binary content
response.json         # Auto-parsed JSON
response.doc          # PyQuery for HTML
response.status_code  # HTTP status
response.headers      # Response headers
response.cookies      # Cookies
response.time         # Request duration
response.save         # Saved state
```

## Common Patterns

### Pagination Pattern

```python
def crawl_page(self, page=1):
    self.crawl(
        f'https://example.com/list?page={page}',
        save={'page': page},
        callback=self.process_page
    )

def process_page(self, response):
    page = response.save['page']
    for item in response.doc('.item').items():
        yield {'title': item.text()}
    
    if page < 10:
        self.crawl_page(page + 1)
```

### Retry Pattern

```python
def on_error(self, exception, response):
    if hasattr(response, 'save') and response.save.get('retry_count', 0) < 3:
        retry_count = response.save.get('retry_count', 0) + 1
        self.crawl(
            response.url,
            save={**response.save, 'retry_count': retry_count},
            proxy=self.get_random_proxy()
        )
```

### HTML Parsing

```python
def parse_html(self, response):
    # Extract text
    title = response.doc('h1.title').text()
    
    # Extract links
    links = [a.attr.href for a in response.doc('a.link').items()]
    
    # Extract attributes
    images = [img.attr.src for img in response.doc('img').items()]
    
    # Nested queries
    content = response.doc('.container .content').text()
```

### JSON Response Handling

```python
def parse_json(self, response):
    data = response.json
    if 'results' in data:
        for item in data['results']:
            self.save_item(item)
```

## Best Practices

1. **Decorators**:
   - `@every`: Only add when scheduled execution is explicitly required
   - `@config(priority=N)`: Only add when priority is specifically specified
   - `@config(age=...)`: Commonly used for caching

2. **Methods**:
   - `on_start()`: REQUIRED - entry point
   - `on_message(project, message)`: REQUIRED for inter-project communication and data storage
   - `on_error()`: Optional - for error handling with retry

**⚠️ 重要提醒**：
   - 永远使用 `on_message`，**不要使用 `on_result`**（PySpider 不支持此方法）
   - `on_message` 的第一个参数是 `project`（项目名），第二个参数是 `message`（消息数据）

3. **Error handling**: Implement `on_error` with retry
4. **Proxy rotation**: Use proxy pools to avoid blocking
5. **State management**: Use `save` for pagination
6. **Task uniqueness**: Use timestamp in taskid
   ```python
   taskid=f"{url}|{time.time()}"
   ```
7. **Data validation**: Verify response integrity
8. **Logging**: Log key steps and errors
9. **Request intervals**: Set reasonable delays

## Resources

### scripts/
- `init_crawler.py` - Generate new crawler template

### references/
- `api_reference.md` - Complete PySpider API documentation
