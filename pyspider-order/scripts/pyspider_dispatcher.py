"""PySpider dispatcher client for sending crawl tasks."""
import os
import requests


class PySpiderDispatcher:
    """Client for sending tasks to PySpider dispatcher."""

    def __init__(self, base_url: str = None, session_cookie: str = None):
        # 支持环境变量配置，提供默认值用于内部测试
        # ⚠️  生产环境必须通过环境变量覆盖
        self.base_url = base_url or os.getenv("PYSPIDER_BASE_URL", "https://pyspider-dev.within-7.com")
        session_cookie = session_cookie or os.getenv("PYSPIDER_SESSION_COOKIE", "eyJfaWQiOiIyNGZmYTllMGI0MTI3OTI1MmY3NTk3MTc1ZGZlODMxYSJ9.ZK_V8A.1zmA_Fxinqi0VHcQRYH_FAKdzIY")
        
        self.headers = {
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': f'session={session_cookie}',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        
        self.headers = {
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': f'session={session_cookie}',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
    
    def send_task(self, project: str, key: str, keyword: str) -> bool:
        """Send a crawl task to PySpider.
        
        Args:
            project: PySpider project name
            key: Scraping key/task type
            keyword: Target keyword or URL
            
        Returns:
            True if successful, False otherwise
        """
        if not project or not keyword:
            print("Error: project and keyword cannot be empty")
            return False
        
        url = f"{self.base_url}/dispatcher"
        payload = f"project={project}&key={key}&keyword={keyword}&url=data%3A%2Con_message%3Fkeywords%3Ddispatcher%26task%3D{project}"
        
        try:
            response = requests.post(url, headers=self.headers, data=payload, timeout=30)
            print(f"Dispatcher response: {response.text}")
            return response.status_code == 200
        except requests.ConnectionError:
            print("❌ 无法连接PySpider服务器，请检查网络和 PYSPIDER_BASE_URL 配置")
            return False
        except requests.Timeout:
            print("❌ PySpider请求超时")
            return False
        except Exception as e:
            print(f"❌ 发送任务到PySpider失败: {e}")
            return False
