"""检查PySpider项目运行状态（内部使用，不暴露给用户）"""
import os
from pymongo import MongoClient
from typing import Dict, List, Optional


def get_mongo_client():
    """获取MongoDB客户端"""
    # 从环境变量获取MongoDB连接字符串
    # 生产环境必须设置 MONGODB_URL 环境变量
    # 参考 .env.example 文件配置
    mongo_url = os.getenv("MONGODB_URL")
    
    if not mongo_url:
        raise ValueError(
            "❌ MongoDB连接字符串未配置\n"
            "请设置环境变量 MONGODB_URL\n"
            "参考 .env.example 文件进行配置"
        )
    
    return MongoClient(mongo_url)


def check_project_status(project_name: str) -> Dict[str, Optional[str]]:
    """
    检查PySpider项目状态
    
    Args:
        project_name: 项目名称
        
    Returns:
        Dict[str, Optional[str]]: {
            'exists': bool,
            'status': Optional[str],  # RUNNING/DEBUG/STOP/CHECKING
            'name': str,
            'can_run': bool
        }
    """
    client = get_mongo_client()
    
    try:
        project = client['projectdb']['projectdb'].find_one({'name': project_name})
        
        if not project:
            return {
                'exists': False,
                'status': None,
                'name': project_name,
                'can_run': False
            }
        
        status = project.get('status', 'UNKNOWN')
        can_run = status in ['RUNNING', 'DEBUG']
        
        return {
            'exists': True,
            'status': status,
            'name': project_name,
            'can_run': can_run
        }
    finally:
        client.close()


def check_multiple_projects(project_names: List[str]) -> Dict[str, Dict]:
    """
    批量检查多个项目状态
    
    Args:
        project_names: 项目名称列表
        
    Returns:
        Dict[str, Dict]: {project_name: status_info}
    """
    client = get_mongo_client()
    
    try:
        projects = client['projectdb']['projectdb'].find(
            {'name': {'$in': project_names}},
            {'name': 1, 'status': 1}
        )
        
        result = {}
        for p in projects:
            name = p['name']
            status = p.get('status', 'UNKNOWN')
            result[name] = {
                'exists': True,
                'status': status,
                'can_run': status in ['RUNNING', 'DEBUG']
            }
        
        # 补充不存在的项目
        for name in project_names:
            if name not in result:
                result[name] = {
                    'exists': False,
                    'status': None,
                    'can_run': False
                }
        
        return result
    finally:
        client.close()


def get_running_projects() -> List[str]:
    """
    获取所有运行中的项目
    
    Returns:
        List[str]: 项目名称列表
    """
    client = get_mongo_client()
    
    try:
        projects = client['projectdb']['projectdb'].find(
            {'status': {'$in': ['RUNNING', 'DEBUG']}},
            {'name': 1}
        )
        
        return [p['name'] for p in projects]
    finally:
        client.close()


if __name__ == "__main__":
    # 测试
    print("检查单个项目:")
    result = check_project_status("ScrapingRedditByKeyword_api")
    print(result)
    
    print("\n检查多个项目:")
    results = check_multiple_projects([
        "ScrapingRedditByKeyword_api",
        "ScrapingInstagramPostsFromTagsSearch"
    ])
    for name, info in results.items():
        print(f"{name}: {info}")
