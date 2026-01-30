"""Feishu API client for PySpider order management."""
import os
import requests
import json
from typing import List, Dict, Optional


class FeishuClient:
    """Client for interacting with Feishu API."""

    def __init__(self, base_url: str = None, table_token: str = None, table_id: str = None, hook_url: str = None):
        # 支持环境变量配置，提供默认值用于内部测试
        # ⚠️  生产环境必须通过环境变量覆盖这些默认值
        self.base_url = base_url or os.getenv("FEISHU_API_URL", "http://3.144.97.122")
        self.table_token = table_token or os.getenv("FEISHU_TABLE_TOKEN", "bascn92h2DxjIZom4hsB1U9irLc")
        self.table_id = table_id or os.getenv("FEISHU_TABLE_ID", "tblBBtyYcEtpS7h2")
        self.hook_url = hook_url or os.getenv("FEISHU_WEBHOOK", "https://open.feishu.cn/open-apis/bot/v2/hook/9117978b-7907-42de-9ab2-cf6995175573")
    
    def create_record(self, task: str, data: List[str], task_user: str, task_id: str, charge_user: Optional[str] = None, user_token: Optional[str] = None) -> Optional[str]:
        """Create a new scraping task record in Feishu.

        Args:
            task: Feishu media type name (e.g., "Reddit 关键词下的帖子")
            data: List of keywords/targets
            task_user: User open ID who created the task
            task_id: Unique task identifier
            charge_user: Optional user ID for the person in charge
            user_token: Optional Feishu user token (will fetch if not provided)

        Returns:
            record_id if successful, None otherwise
        """
        # 参考 pyspider_crawl.py 的接口调用
        url = f"{self.base_url}/api/form_keywords_crawl_to_feishu"

        # 根据MongoDB里保存的实际字段名创建记录
        # 正确的字段名（从MongoDB查询结果获取）：
        # - 任务类型（不是task）
        # - 关键词1, 关键词2...（不是data）
        # - 数据抓取状态（不是task_status）
        # - 紧急程度
        # - charge任务

        # 构建基础字段
        fields_data = {
            "任务类型": task,
            "数据抓取状态": "等待分发",
            "紧急程度": "一般（今天）"
        }

        # 设置工单发起人和charge任务（必须提供task_user）
        if not task_user:
            print("⚠️ 未提供task_user，使用系统默认值")
            # 不设置工单发起人，让飞书系统自动处理
        else:
            fields_data["工单发起人"] = {
                "id": task_user,
                "name": "用户"  # 飞书会根据ID自动获取名字
            }
            fields_data["charge任务"] = [task_user]

        # 添加关键词字段（关键词1, 关键词2, ...）
        for i, keyword in enumerate(data):
            fields_data[f"关键词{i+1}"] = keyword

        payload = {
            "user_token": user_token,
            "fieldsList": [fields_data]
        }

        try:
            response = requests.post(url, json=payload, timeout=30)
            result = response.json()

            print(f"Feishu API Response: {result}")

            # 检查响应 - 参考 feishu.py 992-1006
            if result.get("code") == 0:
                # 从响应中提取record_id
                resp_data = result.get("data", {})
                if isinstance(resp_data, dict):
                    records = resp_data.get("records", [])
                    if len(records) > 0:
                        return records[0].get("record_id")
            else:
                print(f"Feishu API Error: {result.get('msg', 'Unknown error')}")
            return None
        except requests.ConnectionError:
            print("❌ 无法连接飞书服务器，请检查网络和 FEISHU_API_URL 配置")
            return None
        except requests.Timeout:
            print("❌ 飞书 API 请求超时")
            return None
        except Exception as e:
            print(f"❌ 创建飞书记录失败: {e}")
            return None
    
    def update_status(self, record_id: str, status: str) -> bool:
        """Update task status.

        Args:
            record_id: Feishu record ID
            status: New status (等待分发/抓取中/已完成/等待手动处理/已取消)

        Returns:
            True if successful, False otherwise
        """
        url = f"{self.base_url}/api/set_feishu_wiki_record"
        payload = {
            "record_id": record_id,
            "table_token": self.table_token,
            "table_id": self.table_id,
            "fields": {
                "数据抓取状态": status  # // 等待处理 抓取中、完成、等待手动处理
            }
        }
        
        try:
            response = requests.post(url, json=payload)
            result = response.json()
            return result.get("code") == 0
        except Exception as e:
            print(f"Error updating status: {e}")
            return False
    
    def query_tasks(self) -> Optional[Dict]:
        """Query all scraping tasks.

        Returns:
            Dict with task data, or None if failed
        """
        url = f"{self.base_url}/api/query_scraping_form_data"
        
        try:
            response = requests.get(url)
            result = response.json()
            if result.get("code") == 0:
                return {
                    "data": result.get("data", {}),
                    "list_dict": result.get("list_dict", {})
                }
            return None
        except Exception as e:
            print(f"Error querying tasks: {e}")
            return None
    
    def send_notification(self, title: str, text: str, at_user: Optional[List[str]] = None) -> bool:
        """Send notification to Feishu group.

        Args:
            title: Message title
            text: Message content
            at_user: List of user IDs to @mention (default: ['all'])

        Returns:
            True if successful, False otherwise
        """
        url = f"{self.base_url}/api/send_msg_to_feishu"
        # 默认@all，确保消息可见
        at_users = at_user if at_user else ['all']
        payload = {
            "hook_url": self.hook_url,
            "title": title,
            "text": text,
            "at_user": at_users
        }

        try:
            response = requests.post(url, json=payload)
            result = response.json()
            # 添加调试输出，和 pyspider_data.py 保持一致
            print(f"📤 飞书通知响应: status={response.status_code}, body={result}")
            return result.get("code") == 0
        except Exception as e:
            print(f"❌ 发送通知失败: {e}")
            return False
