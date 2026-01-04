#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Initialize a new PySpider crawler with template code.
Usage: python init_crawler.py <CrawlerName> <output_path>
"""

import sys
import os
from datetime import datetime


def create_crawler_template(name, output_path):
    """Create a new PySpider crawler file with template code."""
    
    template = f'''#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
# Project: {name}

from pyspider.libs.base_handler import *
from pyspider import database
import re
import urllib.parse
import logging
import time

myLogger = logging.getLogger('handler_screen')

class {name}(BaseHandler):
    """PySpider crawler for {name}"""
    
    crawl_config = {{
        'connect_timeout': 2,
        'timeout': 30,
        'retries': 5,
        'age': 0
    }}
    
    retry_delay = {{'': 10}}
    
    # Database connection (uncomment and configure as needed)
    # __RESULTDB = database.connect_database({{
    #     'host': 'localhost',
    #     'port': 27017,
    #     'database': 'results'
    # }})
    # __DB_NAME = '{name}'
    
    # Proxy configuration (uncomment and configure as needed)
    # __PROXY = 'auto'
    # __PROXY = 'http://proxy.example.com:8080'
    
    def on_start(self):
        """Entry point - initiate crawling tasks"""
        start_url = 'https://example.com'
        self.crawl(
            start_url,
            callback=self.index_page,
            save={{}}
        )
    
    def on_message(self, project, message):
        """Handle inter-project messages"""
        if project == self.project_name:
            return message
        
        if 'url' in message:
            self.crawl(
                message['url'],
                callback=self.process_page,
                save=message.get('data', {{}}
            )
    
    def index_page(self, response):
        """Process index page and extract links"""
        if not response.ok:
            myLogger.error(f"Failed to fetch: {{response.url}}")
            return
        
        # Extract links
        for each in response.doc('a[href^="http"]').items():
            url = each.attr.href
            self.crawl(
                url,
                callback=self.detail_page,
                save={{'source': response.url}}
            )
    
    def detail_page(self, response):
        """Process detail page and extract data"""
        if not response.ok:
            myLogger.error(f"Failed to fetch: {{response.url}}")
            return
        
        data = {{
            'url': response.url,
            'title': response.doc('title').text(),
            'content': response.doc('body').text()[:500],
            'timestamp': time.time()
        }}
        
        # Save to database (uncomment to use)
        # self.__RESULTDB.save(self.__DB_NAME, data)
        
        # Send message (uncomment to use)
        # self.send_message(
        #     self.project_name,
        #     data,
        #     url=f'data:,on_message?url={{response.url}}'
        # )
        
        myLogger.info(f"Processed: {{response.url}}")
        return data
'''
    
    # Create output file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"✅ Created crawler: {output_path}")
    print(f"   Project: {name}")
    return True


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python init_crawler.py <CrawlerName> <output_path>")
        print("Example: python init_crawler.py MyCrawler ./projects/my_crawler.py")
        sys.exit(1)
    
    crawler_name = sys.argv[1]
    output_path = sys.argv[2]
    
    create_crawler_template(crawler_name, output_path)
