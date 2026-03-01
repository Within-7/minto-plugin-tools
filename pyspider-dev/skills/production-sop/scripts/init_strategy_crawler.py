#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Initialize a new PySpider crawler with production strategy templates (A-E).
Based on production-ready SOP with anti-scraping strategies.

Usage: python init_strategy_crawler.py <CrawlerName> <strategy_type> <output_path>
       python init_strategy_crawler.py TikTokCrawler A ./projects/tiktok_crawler.py
       python init_strategy_crawler.py FacebookCrawler B ./projects/facebook_crawler.py
"""

import sys
import os
import argparse
from datetime import datetime


# Strategy A: BrightData V3 (Top-tier anti-scraping)
STRATEGY_A_TEMPLATE = '''#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on {date}
# Project: {name}
# Strategy: A - BrightData V3 (Top-tier anti-scraping)

from pyspider.libs.base_handler import *
import json

class Handler(BaseHandler):
    """BrightData V3 Strategy Crawler for {name}
    
    Pure Request Protocol:
    - No extra params in URL
    - Exact payload alignment with official CURL
    - Use separators=(',', ':') for JSON
    """

    crawl_config = {{
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'timeout': 120,
        'connect_timeout': 30,
        'validate_cert': True,
    }}

    def on_start(self):
        """Entry point - initiate BD V3 three-step state machine"""
        # Step 1: Trigger BD job
        trigger_url = 'https://api.brightdata.com/v3/trigger'
        trigger_payload = {{
            'url': 'https://target-site.com/data',
            'method': 'GET',
        }}

        self.crawl(
            trigger_url,
            method='POST',
            data=json.dumps(trigger_payload, separators=(',', ':')),
            headers={{'Content-Type': 'application/json'}},
            callback=self.handle_trigger_response,
            save={{'step': 1}}
        )

    def handle_trigger_response(self, response):
        """Handle BD trigger response (Step 1 -> Step 2)"""
        if not response.ok:
            raise Exception(f"BD trigger failed: {{response.status_code}}")

        trigger_result = response.json
        job_id = trigger_result.get('job_id')

        if not job_id:
            raise Exception("BD_EMPTY_DATA: No job_id returned")

        # Step 2: Poll for snapshot status
        snapshot_url = f'https://api.brightdata.com/v3/snapshot/{{job_id}}'
        self.crawl(
            snapshot_url,
            callback=self.handle_snapshot_response,
            save={{'step': 2, 'job_id': job_id}},
            age=5  # Short cache for polling
        )

    def handle_snapshot_response(self, response):
        """Handle BD snapshot response (Step 2 -> Step 3)"""
        if not response.ok:
            raise Exception(f"BD snapshot failed: {{response.status_code}}")

        snapshot_result = response.json

        # Check status
        status = snapshot_result.get('status')
        if status not in ['ready', 'done']:
            # Still processing, retry after delay
            if response.save.get('retry_count', 0) < 60:  # Max 5 minutes
                retry_count = response.save.get('retry_count', 0) + 1
                snapshot_url = f'https://api.brightdata.com/v3/snapshot/{{response.save.get("job_id")}}'
                self.crawl(
                    snapshot_url,
                    callback=self.handle_snapshot_response,
                    save={{**response.save, 'retry_count': retry_count}},
                    age=5
                )
                return

        # Step 3: Get final result
        if status in ['ready', 'done']:
            records = snapshot_result.get('records', 0)
            if records == 0:
                raise Exception("BD_EMPTY_DATA: Status ready/done but records == 0")

            result_url = snapshot_result.get('result_url')
            self.crawl(
                result_url,
                callback=self.parse_final_result,
                save={{'step': 3}}
            )

    def parse_final_result(self, response):
        """Parse final BD result data"""
        data = response.json

        return {{
            'url': response.url,
            'records': len(data.get('items', [])),
            'data': data,
            'timestamp': {timestamp},
        }}

    def on_message(self, project, message):
        """Handle inter-project messages (REQUIRED)"""
        if project == self.project_name:
            return message
        return message

    @catch_status_code_error
    def on_error(self, exception, response):
        """Error handler - raise to trigger FAILED status"""
        raise Exception(f"Strategy A error: {{str(exception)}}")
'''


# Strategy B: Cookie Pool (Strong account binding)
STRATEGY_B_TEMPLATE = '''#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on {date}
# Project: {name}
# Strategy: B - Cookie Pool (Strong account binding)

from pyspider.libs.base_handler import *
import random

class Handler(BaseHandler):
    """Cookie Pool Strategy Crawler for {name}
    
    Features:
    - Force use ispProxy_us_
    - Pass forced_cookies via save parameter
    - Random cookie selection from pool
    """

    # Cookie pool configuration
    COOKIE_POOL = [
        'cookie1=value1; cookie2=value2',
        'cookie1=value3; cookie2=value4',
        # Add more cookies here
    ]

    # Proxy configuration (must use ispProxy_us_)
    PROXY_POOL = [
        'http://username:password@proxy1:port',
        'http://username:password@proxy2:port',
    ]

    crawl_config = {{
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'timeout': 60,
        'connect_timeout': 20,
        'validate_cert': True,
    }}

    def get_random_cookie(self):
        """Get random cookie from pool"""
        return random.choice(self.COOKIE_POOL)

    def get_random_proxy(self):
        """Get random proxy from pool"""
        return random.choice(self.PROXY_POOL)

    def on_start(self):
        """Entry point - initiate crawling with cookie and proxy"""
        target_url = 'https://target-site.com/data'

        self.crawl(
            target_url,
            proxy=self.get_random_proxy(),
            headers={{
                'Cookie': self.get_random_cookie(),
                'Accept': 'text/html,application/xhtml+xml',
                'Accept-Language': 'en-US,en;q=0.9',
            }},
            callback=self.parse_page,
            save={{'forced_cookies': self.get_random_cookie()}}
        )

    def parse_page(self, response):
        """Parse page with cookie authentication"""
        if not response.ok:
            raise Exception(f"Request failed: {{response.status_code}}")

        # Check for login wall
        if 'login' in response.text.lower() or 'sign in' in response.text.lower():
            raise Exception("Cookie expired or invalid - login wall detected")

        # Extract data
        items = response.doc('.data-item').items()
        results = []

        for item in items:
            results.append({{
                'title': item.find('.title').text(),
                'url': item.find('a').attr('href'),
                'description': item.find('.desc').text(),
            }})

        return {{
            'url': response.url,
            'items': results,
            'count': len(results),
            'timestamp': {timestamp},
        }}

    def on_message(self, project, message):
        """Handle inter-project messages (REQUIRED)"""
        if project == self.project_name:
            return message
        return message

    @catch_status_code_error
    def on_error(self, exception, response):
        """Error handler - raise to trigger FAILED status"""
        raise Exception(f"Strategy B error: {{str(exception)}}")
'''


# Strategy C: SSR (Proxy breakthrough with regex)
STRATEGY_C_TEMPLATE = '''#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on {date}
# Project: {name}
# Strategy: C - SSR (Proxy breakthrough with regex extraction)

from pyspider.libs.base_handler import *
import re

class Handler(BaseHandler):
    """SSR Strategy Crawler for {name}
    
    Features:
    - Residential proxy (serProxy_us_)
    - Regex extraction for embedded data
    - DOM + JSON mixed parsing
    """

    # Residential proxy configuration
    RESIDENTIAL_PROXY = 'http://username:password@residential-proxy:port'

    crawl_config = {{
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'timeout': 90,
        'connect_timeout': 30,
        'validate_cert': True,
    }}

    def on_start(self):
        """Entry point - initiate SSR crawling"""
        target_url = 'https://target-site.com/video/details'

        self.crawl(
            target_url,
            proxy=self.RESIDENTIAL_PROXY,
            callback=self.parse_ssr_page,
        )

    def parse_ssr_page(self, response):
        """Parse SSR page with regex extraction"""
        if not response.ok:
            raise Exception(f"Request failed: {{response.status_code}}")

        # Method 1: Regex extraction for embedded JSON data
        # Common patterns: ytInitialData, __INITIAL_STATE__, window.__DATA__
        json_pattern = r'var\\s+(\\w+)\\s*=\\s*(\\{{.*?\\}});'
        matches = re.findall(json_pattern, response.text, re.DOTALL)

        data = {{}}
        for var_name, json_str in matches:
            try:
                data[var_name] = json.loads(json_str)
            except:
                pass

        # Method 2: Extract specific data using regex
        title_pattern = r'<title>(.*?)</title>'
        title = re.search(title_pattern, response.text)
        if title:
            data['title'] = title.group(1)

        # Method 3: DOM parsing as fallback
        if not data:
            data['title'] = response.doc('title').text()
            data['description'] = response.doc('meta[name="description"]').attr('content')

        return {{
            'url': response.url,
            'extracted_data': data,
            'timestamp': {timestamp},
        }}

    def on_message(self, project, message):
        """Handle inter-project messages (REQUIRED)"""
        if project == self.project_name:
            return message
        return message

    @catch_status_code_error
    def on_error(self, exception, response):
        """Error handler - raise to trigger FAILED status"""
        raise Exception(f"Strategy C error: {{str(exception)}}")
'''


# Strategy D: API Forward (Pure APIs with task status)
STRATEGY_D_TEMPLATE = '''#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on {date}
# Project: {name}
# Strategy: D - API Forward (Pure APIs with task status)

from pyspider.libs.base_handler import *
import json
import uuid
import time

class Handler(BaseHandler):
    """API Forward Strategy Crawler for {name}
    
    Features:
    - Datacenter proxy
    - UUID taskid bypass
    - MongoDB task status bits
    - API status polling
    """

    # Datacenter proxy
    DATACENTER_PROXY = 'http://username:password@datacenter-proxy:port'

    crawl_config = {{
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'timeout': 60,
        'connect_timeout': 20,
        'validate_cert': True,
        'headers': {{
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }},
    }}

    def on_start(self):
        """Entry point - initiate API request with UUID taskid"""
        api_url = 'https://api.example.com/process'

        # Generate unique taskid for bypass
        taskid = str(uuid.uuid4())

        payload = {{
            'taskid': taskid,
            'action': 'process_data',
            'params': {{'key': 'value'}},
        }}

        self.crawl(
            api_url,
            method='POST',
            data=json.dumps(payload, separators=(',', ':')),
            proxy=self.DATACENTER_PROXY,
            callback=self.handle_api_response,
            save={{'taskid': taskid, 'step': 1}}
        )

    def handle_api_response(self, response):
        """Handle API response - check task status"""
        if not response.ok:
            raise Exception(f"API request failed: {{response.status_code}}")

        result = response.json

        # Check if task is complete
        status = result.get('status')
        taskid = response.save.get('taskid')

        if status == 'completed':
            # Task complete, return data
            return {{
                'taskid': taskid,
                'status': 'completed',
                'data': result.get('data'),
                'timestamp': {timestamp},
            }}
        elif status == 'processing':
            # Task still processing, poll status
            if response.save.get('poll_count', 0) < 30:  # Max 5 minutes
                poll_count = response.save.get('poll_count', 0) + 1
                status_url = f'https://api.example.com/status/{{taskid}}'

                self.crawl(
                    status_url,
                    proxy=self.DATACENTER_PROXY,
                    callback=self.handle_api_response,
                    save={{**response.save, 'poll_count': poll_count}},
                    age=10  # Poll every 10 seconds
                )
                return
        else:
            raise Exception(f"API task failed with status: {{status}}")

    def on_message(self, project, message):
        """Handle inter-project messages (REQUIRED)"""
        if project == self.project_name:
            return message
        return message

    @catch_status_code_error
    def on_error(self, exception, response):
        """Error handler - raise to trigger FAILED status"""
        raise Exception(f"Strategy D error: {{str(exception)}}")
'''


# Strategy E: Dispatcher (Scheduling and distribution)
STRATEGY_E_TEMPLATE = '''#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on {date}
# Project: {name}
# Strategy: E - Dispatcher (Scheduling and distribution)

from pyspider.libs.base_handler import *
import json

class Handler(BaseHandler):
    """Dispatcher Strategy Crawler for {name}
    
    Features:
    - on_message fanout
    - send_message task routing
    - Task distribution to multiple crawlers
    """

    # Target projects for task routing
    TARGET_PROJECTS = [
        'CrawlerA',
        'CrawlerB',
        'CrawlerC',
    ]

    crawl_config = {{
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'timeout': 30,
        'connect_timeout': 10,
    }}

    def on_start(self):
        """Entry point - initiate dispatcher"""
        # Load task list from database or file
        tasks = self.load_tasks()

        for task in tasks:
            self.crawl(
                task.get('url'),
                callback=self.index_task,
                save={{'task_data': task}}
            )

    def load_tasks(self):
        """Load tasks from source (database, file, API, etc.)"""
        # Example: Load from list
        return [
            {{'url': 'https://site1.com/page1', 'priority': 1}},
            {{'url': 'https://site2.com/page2', 'priority': 2}},
            # Add more tasks
        ]

    def index_task(self, response):
        """Index task and route to target crawlers"""
        if not response.ok:
            raise Exception(f"Task indexing failed: {{response.status_code}}")

        task_data = response.save.get('task_data', {{}})

        # Route task to appropriate crawler based on rules
        for target_project in self.TARGET_PROJECTS:
            message = {{
                'url': response.url,
                'task_id': task_data.get('id'),
                'priority': task_data.get('priority', 1),
                'metadata': task_data,
            }}

            # Send message to target project
            self.send_message(
                project=target_project,
                message=message
            )

        return {{
            'url': response.url,
            'routed_to': self.TARGET_PROJECTS,
            'task_count': len(self.TARGET_PROJECTS),
            'timestamp': {timestamp},
        }}

    def on_message(self, project, message):
        """Handle inter-project messages (REQUIRED)"""
        if project == self.project_name:
            return message

        # Process messages from other projects
        print(f"Message from {{project}}: {{message}}")

        # Example: Update task status in database
        # self.update_task_status(message.get('task_id'), message.get('status'))

        return message

    @catch_status_code_error
    def on_error(self, exception, response):
        """Error handler - raise to trigger FAILED status"""
        raise Exception(f"Strategy E error: {{str(exception)}}")
'''


STRATEGY_TEMPLATES = {
    'A': STRATEGY_A_TEMPLATE,
    'B': STRATEGY_B_TEMPLATE,
    'C': STRATEGY_C_TEMPLATE,
    'D': STRATEGY_D_TEMPLATE,
    'E': STRATEGY_E_TEMPLATE,
}

STRATEGY_DESCRIPTIONS = {
    'A': 'BrightData V3 - Top-tier anti-scraping with three-step state machine',
    'B': 'Cookie Pool - Strong account binding with forced cookies',
    'C': 'SSR - Proxy breakthrough with regex extraction',
    'D': 'API Forward - Pure APIs with UUID taskid and status polling',
    'E': 'Dispatcher - Scheduling and distribution with task routing',
}


def create_strategy_crawler(name, strategy_type, output_path):
    """Create a new PySpider crawler with selected strategy template"""

    if strategy_type not in STRATEGY_TEMPLATES:
        raise ValueError(f"Invalid strategy type: {{strategy_type}}. Must be one of: {{', '.join(STRATEGY_TEMPLATES.keys())}}")

    timestamp = int(datetime.now().timestamp())
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Select template
    template = STRATEGY_TEMPLATES[strategy_type]

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

    print(f"✅ Created crawler: {{output_path}}")
    print(f"   Project: {{name}}")
    print(f"   Strategy: {{strategy_type}} - {{STRATEGY_DESCRIPTIONS[strategy_type]}}")
    return True


def main():
    parser = argparse.ArgumentParser(
        description='Initialize a new PySpider crawler with production strategy templates',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Strategies:
  A  BrightData V3 (Top-tier anti-scraping)
  B  Cookie Pool (Strong account binding)
  C  SSR (Proxy breakthrough with regex)
  D  API Forward (Pure APIs with task status)
  E  Dispatcher (Scheduling and distribution)

Examples:
  python init_strategy_crawler.py TikTokCrawler A ./projects/tiktok_crawler.py
  python init_strategy_crawler.py FacebookCrawler B ./projects/facebook_crawler.py
  python init_strategy_crawler.py YoutubeCrawler C ./projects/youtube_crawler.py
        '''
    )
    parser.add_argument('name', help='Crawler class name')
    parser.add_argument('strategy', choices=list(STRATEGY_TEMPLATES.keys()),
                        help='Strategy type (A-E)')
    parser.add_argument('output', help='Output file path')

    args = parser.parse_args()

    try:
        create_strategy_crawler(args.name, args.strategy, args.output)
    except Exception as e:
        print(f"❌ Error: {{e}}")
        sys.exit(1)


if __name__ == '__main__':
    main()
