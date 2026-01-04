---
name: pyspider-dev
description: Guide for developing PySpider web crawlers. Use when creating, modifying, or debugging PySpider projects. Covers crawler architecture, BaseHandler patterns, database integration, proxy management, and common workflows for scraping web content with Python. Includes templates and best practices for production-ready crawlers.
---

# PySpider Development

## Overview

PySpider is a powerful web crawling framework built on Python. This skill provides workflows, patterns, and templates for developing production-ready crawlers.

## Core Architecture

Every PySpider crawler inherits from `BaseHandler` and implements key lifecycle methods:

```python
from pyspider.libs.base_handler import *
from pyspider import database

class MyCrawler(BaseHandler):
    crawl_config = {
        'connect_timeout': 2,
        'timeout': 30,
        'retries': 5,
        'age': 0
    }
    
    def on_start(self):
        """Entry point - initiate crawling tasks"""
        pass
    
    def on_message(self, project, message):
        """Handle inter-project messages"""
        pass
    
    def some_callback(self, response):
        """Process HTTP response"""
        pass
```

## Quick Start

### 1. Basic Crawler Structure

Create a new crawler file:

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2025-01-04
# Project: MyCrawler

from pyspider.libs.base_handler import *
from pyspider import database
import re
import urllib.parse
import logging

myLogger = logging.getLogger('handler_screen')

class MyCrawler(BaseHandler):
    crawl_config = {
        'connect_timeout': 2,
        'timeout': 30,
        'retries': 5,
        'age': 0
    }
    
    def on_start(self):
        """Initiate crawling"""
        url = 'https://example.com'
        self.crawl(url, callback=self.index_page)
    
    def index_page(self, response):
        """Process index page"""
        for each in response.doc('a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page)
    
    def detail_page(self, response):
        """Process detail page"""
        data = {
            'url': response.url,
            'title': response.doc('title').text(),
        }
        self.save_to_database(data)
```

### 2. Database Integration

Connect to result database:

```python
from pyspider import database

class MyCrawler(BaseHandler):
    __RESULTDB = database.connect_database({
        'host': 'localhost',
        'port': 27017,
        'database': 'results'
    })
    __DB_NAME = 'MyCrawler'
    
    def save_data(self, data):
        self.__RESULTDB.save(self.__DB_NAME, data)
    
    def query_existing(self, filter_dict):
        results = list(self.__RESULTDB.select(self.__DB_NAME, filter=filter_dict))
        return results
```

### 3. Proxy Management

Configure proxy pools:

```python
class MyCrawler(BaseHandler):
    # Static proxy
    __PROXY = 'http://proxy.example.com:8080'
    
    # Auto proxy pool
    __PROXY = 'auto'
    
    # Residential proxy
    __PROXY = 'residential_proxy_config'
    
    def crawl_with_proxy(self, url):
        self.crawl(
            url,
            proxy=self.__PROXY,
            headers={'User-Agent': 'Mozilla/5.0...'},
            callback=self.process_response
        )
```

### 4. Inter-Project Messaging

Send messages between projects:

```python
class MyCrawler(BaseHandler):
    def on_message(self, project, message):
        """Handle incoming messages"""
        if project == self.project_name:
            return message
        
        if 'url' in message:
            self.crawl(message['url'], callback=self.process_url)
    
    def send_result(self, data):
        """Send result to self or other projects"""
        self.send_message(
            self.project_name,
            {'keywords': data['keyword'], 'count': data['count']},
            url=f'data:,on_message?keywords={data["keyword"]}'
        )
```

## Common Patterns

### Pagination Pattern

```python
class PaginatedCrawler(BaseHandler):
    __PAGE_SIZE = 20
    __MAX_PAGES = 10
    
    def crawl_page(self, page=1):
        url = f'https://example.com/list?page={page}'
        self.crawl(
            url,
            save={'page': page},
            callback=self.process_page
        )
    
    def process_page(self, response):
        page = response.save['page']
        
        # Extract data
        for item in response.doc('.item').items():
            yield {'title': item.text()}
        
        # Next page
        if page < self.__MAX_PAGES:
            self.crawl_page(page + 1)
```

### Retry Pattern

```python
class RobustCrawler(BaseHandler):
    retry_delay = {'': 10}
    
    def fetch_with_retry(self, url, retry=0):
        self.crawl(
            url,
            save={'retry': retry},
            callback=self.handle_response
        )
    
    def handle_response(self, response):
        retry = response.save.get('retry', 0)
        
        if not response.ok:
            if retry < 3:
                time.sleep(2 ** retry)  # Exponential backoff
                self.fetch_with_retry(response.url, retry + 1)
            else:
                self.log_error(response.url)
```

### Keyword Batch Processing

```python
class KeywordCrawler(BaseHandler):
    __KEYWORDS = ['keyword1', 'keyword2', 'keyword3']
    
    def on_start(self):
        for keyword in self.__KEYWORDS:
            self.crawl_keyword(keyword)
    
    def crawl_keyword(self, keyword, priority=1):
        url = f'https://example.com/search?q={keyword}'
        self.crawl(
            url,
            save={'keyword': keyword},
            priority=priority,
            taskid=f"{url}|{time.time()}",
            callback=self.process_search_result
        )
```

## Response Processing

### HTML Parsing with CSS Selectors

```python
def process_html(self, response):
    # Extract elements
    titles = response.doc('h1.title').text()
    links = [a.attr.href for a in response.doc('a.link').items()]
    
    # Extract attributes
    images = [img.attr.src for img in response.doc('img').items()]
    
    # Nested queries
    content = response.doc('.container .content').text()
```

### Regex Extraction

```python
def extract_data(self, text):
    # Find all matches
    pattern = r'<div class="data">(.*?)</div>'
    matches = re.findall(pattern, text, re.DOTALL)
    
    # Search with groups
    result = re.search(r'(\d+) results', text)
    if result:
        count = int(result.group(1))
    
    return matches
```

### JSON Response Handling

```python
def process_json(self, response):
    data = response.json
    if 'results' in data:
        for item in data['results']:
            self.save_item(item)
```

## Error Handling

```python
class SafeCrawler(BaseHandler):
    def safe_process(self, response):
        try:
            if not response.ok:
                myLogger.error(f"HTTP {response.status_code}: {response.url}")
                return
            
            if response.text.count('Error') > 0:
                myLogger.warning(f"Error page detected: {response.url}")
                return
            
            # Process normally
            self.extract_data(response)
            
        except Exception as e:
            myLogger.error(f"Processing failed: {str(e)}")
```

## Best Practices

1. **Task ID uniqueness**: Use timestamp in taskid to prevent caching
   ```python
   taskid=f"{url}|{time.time()}"
   ```

2. **Priority management**: Set higher priority for important tasks
   ```python
   self.crawl(url, priority=10, callback=...)
   ```

3. **Rate limiting**: Use delays between requests
   ```python
   crawl_config = {'connect_timeout': 2, 'timeout': 30}
   ```

4. **Logging**: Use structured logging
   ```python
   myLogger.info(f"Processing: {keyword}")
   ```

5. **Data deduplication**: Check database before processing
   ```python
   existing = list(self.__RESULTDB.select(__DB_NAME, 
           filter={'url': url}))
   if not existing:
       self.process_new_url(url)
   ```

## Resources

### scripts/
- `init_crawler.py` - Generate new crawler template
- `validate_crawler.py` - Validate crawler syntax

### references/
- `API_REFERENCE.md` - Complete PySpider API documentation
- `PATTERNS.md` - Advanced crawling patterns and workflows

### assets/
- `templates/` - Crawler template files
