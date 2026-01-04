#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Initialize a new PySpider crawler with standard template code.
Based on production-ready patterns with best practices.

Usage: python init_crawler.py <CrawlerName> <output_path>
       python init_crawler.py <CrawlerName> <output_path> --template=advanced
       python init_crawler.py <CrawlerName> <output_path> --template=enterprise
"""

import sys
import os
import argparse
from datetime import datetime


# Standard template with basic GET requests
STANDARD_TEMPLATE = '''#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on {date}
# Project: {name}

from pyspider.libs.base_handler import *

class Handler(BaseHandler):
    """Standard PySpider crawler for {name}"""
    
    # Global crawl config - applies to all requests
    crawl_config = {{
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'headers': {{
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }},
        'timeout': 60,
        'connect_timeout': 10,
        'validate_cert': True,
        'itag': 'v1',  # Version tag - changes trigger re-crawl
    }}
    
    def on_start(self):
        """Entry point - initiate crawling tasks (REQUIRED)"""
        start_url = 'https://example.com'
        self.crawl(start_url, callback=self.parse_page)
    
    def on_message(self, project, message):
        """Handle inter-project messages and data storage (REQUIRED)"""
        if project == self.project_name:
            return message
        # Process message from other projects
        return message
    
    @config(age=10 * 24 * 60 * 60)  # Cache 10 days (remove if no caching needed)
    def parse_page(self, response):
        """Parse page callback - receives Response object"""
        if not response.ok:
            print(f"Failed to fetch: {{response.url}} - Status: {{response.status_code}}")
            return
        
        # Extract page title
        title = response.doc('title').text()
        print(f"Processing: {{response.url}} - Title: {{title}}")
        
        # Extract and crawl discovered links
        for each in response.doc('a[href^="http"]').items():
            url = each.attr.href
            self.crawl(url, callback=self.parse_page)
        
        # Return structured data
        return {{
            'url': response.url,
            'title': title,
            'status_code': response.status_code,
            'timestamp': {timestamp},
        }}
'''


# Advanced template with POST requests and proxy
ADVANCED_TEMPLATE = '''#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on {date}
# Project: {name}

from pyspider.libs.base_handler import *
import json
import time

class Handler(BaseHandler):
    """Advanced PySpider crawler with POST and proxy support for {name}"""
    
    crawl_config = {{
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'headers': {{
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }},
        'timeout': 30,
        'proxy': 'http://username:password@proxy_ip:port',  # Configure proxy
    }}
    
    # Proxy pool (optional)
    proxy_pool = [
        'http://proxy1:port',
        'http://proxy2:port',
        'http://proxy3:port',
    ]
    
    def on_start(self):
        """Entry point - initiate crawling tasks"""
        # GET request with parameters
        self.crawl(
            'https://api.example.com/data',
            params={{'page': 1, 'size': 20}},  # GET parameters
            callback=self.parse_get_data,
            proxy=self.proxy_pool[0] if self.proxy_pool else None
        )
        
        # POST JSON request
        post_data = {{'username': 'test_user', 'action': 'login'}}
        self.crawl(
            'https://api.example.com/login',
            method='POST',
            data=json.dumps(post_data),  # String for JSON
            headers={{'Content-Type': 'application/json'}},
            callback=self.parse_login_response
        )
        
        # POST Form request
        form_data = {{'search': 'keyword', 'page': 1}}
        self.crawl(
            'https://example.com/search',
            method='POST',
            data=form_data,  # Dict for form data (auto converts to x-www-form-urlencoded)
            callback=self.parse_search_results
        )
    
    def parse_get_data(self, response):
        """Handle GET request response"""
        try:
            data = response.json  # Auto-parse JSON
            print(f"Got {{len(data.get('items', []))}} items")
            
            # Pagination with save state
            current_page = response.save.get('page', 1)
            if current_page < 10:  # Max 10 pages
                self.crawl(
                    'https://api.example.com/data',
                    params={{'page': current_page + 1, 'size': 20}},
                    callback=self.parse_get_data,
                    save={{'page': current_page + 1}}
                )
            
            return data
        except Exception as e:
            print(f"Parse error: {{e}}")
            return {{'error': str(e)}}
    
    def on_message(self, project, message):
        """Handle inter-project messages and data storage (REQUIRED)"""
        if project == self.project_name:
            return message
        # Process message from other projects
        return message
    
    def parse_login_response(self, response):
        """Handle login response"""
        login_result = response.json
        if login_result.get('success'):
            token = login_result.get('token')
            # Use token in subsequent requests
            self.crawl(
                'https://api.example.com/user/profile',
                headers={{'Authorization': f'Bearer {{token}}'}},
                callback=self.parse_profile
            )
        return login_result
    
    def parse_search_results(self, response):
        """Handle search results"""
        results = []
        for item in response.doc('.search-result-item').items():
            results.append({{
                'title': item.find('.title').text(),
                'url': item.find('.title a').attr('href'),
                'summary': item.find('.summary').text()
            }})
        return {{'results': results, 'total': len(results)}}
    
    def parse_profile(self, response):
        """Handle profile data"""
        profile_data = response.json
        return {{
            'user_id': profile_data.get('id'),
            'username': profile_data.get('username'),
            'email': profile_data.get('email')
        }}
    
    def on_error(self, exception, response):
        """Error handler with retry logic"""
        error_info = {{
            'url': response.url if response else 'N/A',
            'error': str(exception),
            'timestamp': time.time()
        }}
        print(f"Error: {{error_info}}")
        
        # Retry logic (max 3 retries)
        if hasattr(response, 'save') and response.save.get('retry_count', 0) < 3:
            retry_count = response.save.get('retry_count', 0) + 1
            print(f"Retrying {{retry_count}}...")
            self.crawl(
                response.url,
                callback=self.parse_get_data,
                save={{**response.save, 'retry_count': retry_count}},
                proxy=self.proxy_pool[retry_count % len(self.proxy_pool)] if self.proxy_pool else None
            )
'''


# Enterprise template with proxy rotation and header rotation
ENTERPRISE_TEMPLATE = '''#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on {date}
# Project: {name}

from pyspider.libs.base_handler import *
import random
import time
import json

class Handler(BaseHandler):
    """Enterprise-grade PySpider crawler with proxy and header rotation for {name}"""
    
    # Proxy IP pool
    PROXY_POOL = [
        'http://user1:pass1@192.168.1.100:8080',
        'http://user2:pass2@192.168.1.101:8080',
        'http://user3:pass3@192.168.1.102:8080',
    ]
    
    # User-Agent pool for different browsers
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
    ]
    
    crawl_config = {{
        'timeout': 45,
        'connect_timeout': 15,
        'validate_cert': True,
        'fetch_type': 'js',  # Enable JS rendering (requires PhantomJS)
        'js_run_at': 'document-end',
    }}
    
    def get_random_proxy(self):
        """Get random proxy from pool"""
        return random.choice(self.PROXY_POOL)
    
    def get_random_user_agent(self):
        """Get random User-Agent"""
        return random.choice(self.USER_AGENTS)
    
    def get_headers(self):
        """Get randomized headers"""
        return {{
            'User-Agent': self.get_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }}
    
    def on_start(self):
        """Entry point - initiate crawling tasks with randomized config"""
        urls = [
            'https://httpbin.org/get',
            'https://httpbin.org/headers',
            'https://httpbin.org/ip',
        ]
        
        for url in urls:
            self.crawl(
                url,
                headers=self.get_headers(),
                proxy=self.get_random_proxy(),
                callback=self.parse_response,
                save={{'original_url': url, 'request_type': 'GET'}}
            )
    
    def parse_response(self, response):
        """Universal response parser"""
        print(f"Processing: {{response.url}} - Status: {{response.status_code}}")
        
        result = {{
            'url': response.save.get('original_url', response.url),
            'request_type': response.save.get('request_type', 'GET'),
            'status_code': response.status_code,
            'response_time': response.time,
        }}
        
        try:
            # Try JSON parsing
            json_data = response.json
            result['data'] = json_data
            print(f"JSON response: {{json_data}}")
        except:
            # Fallback to HTML parsing
            title = response.doc('title').text()
            result['title'] = title
            result['content_length'] = len(response.text)
            print(f"HTML: {{title}}, Length: {{len(response.text)}}")
        
        return result
    
    def on_message(self, project, message):
        """Handle inter-project messages and data storage (REQUIRED)"""
        if project == self.project_name:
            return message
        
        if not message:
            return
        
        print(f"Message from {{project}}: {{message.get('url', 'N/A')}}")
        
        # Add your data storage logic here
        # Example: save to database
        # self.save_to_database(message)
        
        # Example: save to file
        # with open('results.json', 'a', encoding='utf-8') as f:
        #     f.write(json.dumps(message, ensure_ascii=False) + '\\n')
        
        return message
    
    def on_error(self, exception, response):
        """Error handler with intelligent retry"""
        error_info = {{
            'url': response.url if response else 'N/A',
            'error_type': type(exception).__name__,
            'error_message': str(exception),
            'timestamp': time.time()
        }}
        print(f"Error: {{error_info}}")
        
        # Retry logic with proxy rotation
        if hasattr(response, 'save') and response.save.get('retry_count', 0) < 3:
            retry_count = response.save.get('retry_count', 0) + 1
            print(f"Retrying {{retry_count}}/3...")
            self.crawl(
                response.url,
                callback=self.parse_response,
                save={{**response.save, 'retry_count': retry_count}},
                headers=self.get_headers(),
                proxy=self.get_random_proxy()  # Use different proxy
            )
'''


def create_crawler_template(name, output_path, template_type='standard'):
    """Create a new PySpider crawler file with selected template"""
    
    timestamp = int(datetime.now().timestamp())
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Select template
    if template_type == 'advanced':
        template = ADVANCED_TEMPLATE
    elif template_type == 'enterprise':
        template = ENTERPRISE_TEMPLATE
    else:
        template = STANDARD_TEMPLATE
    
    # Format template
    content = template.format(
        name=name,
        date=date_str,
        timestamp=timestamp
    )
    
    # Create output file
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Created crawler: {output_path}")
    print(f"   Project: {name}")
    print(f"   Template: {template_type}")
    return True


def main():
    parser = argparse.ArgumentParser(
        description='Initialize a new PySpider crawler with standard template',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Templates:
  standard    Basic GET request crawler with standard patterns
  advanced    POST requests with proxy support
  enterprise  Dynamic proxy + header rotation for production

Examples:
  python init_crawler.py MyCrawler ./projects/my_crawler.py
  python init_crawler.py MyCrawler ./projects/my_crawler.py --template=advanced
  python init_crawler.py ApiCrawler ./projects/api.py --template=enterprise
        '''
    )
    parser.add_argument('name', help='Crawler class name')
    parser.add_argument('output', help='Output file path')
    parser.add_argument('--template', choices=['standard', 'advanced', 'enterprise'],
                        default='standard', help='Template type (default: standard)')
    
    args = parser.parse_args()
    
    create_crawler_template(args.name, args.output, args.template)


if __name__ == '__main__':
    main()
