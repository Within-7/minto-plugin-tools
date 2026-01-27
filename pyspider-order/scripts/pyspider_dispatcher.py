"""PySpider dispatcher client for sending crawl tasks."""
import requests


class PySpiderDispatcher:
    """Client for sending tasks to PySpider dispatcher."""
    
    def __init__(self, base_url: str = "https://pyspider-dev.within-7.com"):
        self.base_url = base_url
        self.headers = {
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': 'session=eyJfaWQiOiIyNGZmYTllMGI0MTI3OTI1MmY3NTk3MTc1ZGZlODMxYSJ9.ZK_V8A.1zmA_Fxinqi0VHcQRYH_FAKdzIY',
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
            response = requests.post(url, headers=self.headers, data=payload)
            print(f"Dispatcher response: {response.text}")
            return response.status_code == 200
        except Exception as e:
            print(f"Error sending task to dispatcher: {e}")
            return False
