"""查询飞书任务进度"""
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from feishu_client import FeishuClient


def query_all_tasks():
    """
    查询所有飞书任务
    
    Returns:
        dict: {
            'data': {record_id: task_info},
            'list_dict': {media_type: keywords}
        }
    """
    client = FeishuClient()
    return client.query_tasks()


def filter_tasks_by_status(tasks, status_filter=None):
    """
    按状态过滤任务
    
    Args:
        tasks: 任务字典
        status_filter: 状态筛选 (等待处理/抓取中/完成/等待手动处理)
        
    Returns:
        dict: 过滤后的任务
    """
    if not tasks:
        return {}
    
    data = tasks.get('data', {})
    filtered = {}
    
    for record_id, task in data.items():
        task_status = task.get('task_status', '')
        
        if status_filter is None or task_status == status_filter:
            filtered[record_id] = task
    
    return {'data': filtered, 'list_dict': tasks.get('list_dict', {})}


def format_tasks_for_display(tasks, show_all=False):
    """
    格式化任务列表用于显示
    
    Args:
        tasks: 任务字典
        show_all: 是否显示所有状态的任务
        
    Returns:
        str: 格式化的文本
    """
    if not tasks or not tasks.get('data'):
        return "📭 当前没有任务"
    
    lines = []
    lines.append("=" * 100)
    
    if show_all:
        lines.append("📋 所有飞书任务")
    else:
        lines.append("📋 进行中的任务")
    
    lines.append("=" * 100)
    
    data = tasks.get('data', {})
    
    # 按状态分组
    by_status = {
        '等待处理': [],
        '抓取中': [],
        '完成': [],
        '等待手动处理': [],
        '其他': []
    }
    
    for record_id, task in data.items():
        status = task.get('task_status', '未知')
        task_name = task.get('task', '未知任务')
        task_data = task.get('data', [])
        keywords = ', '.join(task_data) if task_data else '-'
        
        task_info = {
            'record_id': record_id,
            'name': task_name,
            'keywords': keywords,
            'status': status
        }
        
        if status in by_status:
            by_status[status].append(task_info)
        else:
            by_status['其他'].append(task_info)
    
    # 显示各状态任务
    for status in ['等待处理', '抓取中', '完成', '等待手动处理', '其他']:
        tasks_list = by_status[status]
        if tasks_list:
            lines.append(f"\n📌 {status} ({len(tasks_list)})")
            lines.append("-" * 100)
            for i, t in enumerate(tasks_list[:10], 1):  # 最多显示10个
                lines.append(f"{i}. {t['name']}")
                lines.append(f"   └─ 关键词: {t['keywords']}")
                lines.append(f"   └─ 记录ID: {t['record_id']}")
            
            if len(tasks_list) > 10:
                lines.append(f"   ... 还有 {len(tasks_list) - 10} 个任务")
    
    lines.append("\n" + "=" * 100)
    return "\n".join(lines)


def query_tasks_by_media_type(media_type):
    """
    按媒体类型查询任务
    
    Args:
        media_type: 媒体类型名称
        
    Returns:
        dict: 该媒体类型的任务
    """
    all_tasks = query_all_tasks()
    
    if not all_tasks:
        return {}
    
    data = all_tasks.get('data', {})
    filtered = {}
    
    for record_id, task in data.items():
        task_name = task.get('task', '')
        if media_type in task_name:
            filtered[record_id] = task
    
    return {'data': filtered, 'list_dict': all_tasks.get('list_dict', {})}


if __name__ == "__main__":
    # 测试
    print("查询所有任务:")
    tasks = query_all_tasks()
    if tasks:
        print(format_tasks_for_display(tasks, show_all=True))
    else:
        print("无法查询任务，请检查飞书API服务")
