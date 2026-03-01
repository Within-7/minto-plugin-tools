---
description: Create a new PySpider crawler with standard/advanced/enterprise templates
args:
  - name: name
    description: Crawler class name (e.g., MyCrawler)
    required: true
  - name: output
    description: Output file path (e.g., ./projects/my_crawler.py)
    required: true
  - name: template
    description: Template type: standard, advanced, or enterprise
    required: false
---

# New Crawler

Create a new PySpider crawler with production-ready templates.

## Process

1. **Select Template Type**: Choose based on complexity
   - `standard`: Basic GET requests, simple HTML parsing
   - `advanced`: POST requests, proxy support, pagination
   - `enterprise`: Dynamic proxy + header rotation, production-grade

2. **Generate Crawler Code**: Use `init_crawler.py` script

3. **Customize for Target Site**: Update URLs, headers, data extraction logic

4. **Sync to Repository**: Use `sync-spider` skill to persist code

## Examples

```bash
# Create standard crawler (basic GET)
/new-crawler MyCrawler ./projects/my_crawler.py

# Create advanced crawler (POST + proxy)
/new-crawler ApiCrawler ./projects/api.py --template=advanced

# Create enterprise crawler (production-grade)
/new-crawler EnterpriseSpider ./projects/enterprise.py --template=enterprise
```

## Template Features

### Standard Template
- Basic GET requests
- Simple HTML parsing with PyQuery
- Pagination support
- Error handling with `@catch_status_code_error`

### Advanced Template
- POST requests (JSON + Form)
- Proxy pool support
- Pagination with state management
- Token-based authentication
- Retry logic with exponential backoff

### Enterprise Template
- Dynamic proxy rotation
- User-Agent pool
- Randomized headers
- JS rendering support (PhantomJS)
- Intelligent retry with proxy switching

## After Creation

1. Update `start_url` in `on_start()`
2. Configure proxy pools (for advanced/enterprise)
3. Implement data extraction in callback functions
4. Test with small data set
5. Sync to repository using `sync-spider` skill
6. Register to database if needed

## See Also

- `/strategy-crawler` - Create crawler with A-E production strategies
- `production-sop` skill - Production-grade guidelines and redlines
