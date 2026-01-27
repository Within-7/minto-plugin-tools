"""列出所有可用的爬虫类型供用户选择"""
import csv
import os

def list_all_crawlers(csv_path=None):
    """
    列出所有配置的爬虫类型，按分类展示
    
    Returns:
        dict: {
            '社交媒体': [{name, project, field, complete, example}],
            '电商平台': [...],
            'SEO工具': [...]
        }
    """
    if csv_path is None:
        # CSV在项目根目录（用户安装skill后的工作目录）
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # skill目录: project_root/.minto/skills/pyspider-order/skills/
        # 项目根目录: 向上4级
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))))
        csv_path = os.path.join(project_root, 'feishudb.ScrapingMongoQuery.csv')
    
    categories = {
        "社交媒体": [],
        "电商平台": [],
        "SEO工具": [],
        "咨询任务": []
    }
    
    # 关键词示例映射
    examples = {
        "Reddit": ("AI", "machine learning"),
        "Instagram": ("fashion", "travel"),
        "TikTok": ("crypto", "dance"),
        "Twitter": ("tech", "news"),
        "Facebook": ("https://www.facebook.com/example",),
        "Youtube": ("music", "gaming"),
        "Pinterest": ("food", "DIY"),
        "Amazon": ("iPhone", "laptop"),
        "卖家精灵": ("Nike", "Apple"),
        "SEMrush": ("example.com",)
    }
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            name = row.get('name', '')
            scrap_key = row.get('scrap_key', '')
            table = row.get('table', '')
            has_mongo = bool(row.get('mongo_list[0]', ''))
            
            # 获取示例
            example_keywords = []
            for key, vals in examples.items():
                if key in name:
                    example_keywords = vals
                    break
            
            crawler_info = {
                "name": name,
                "project": table,
                "field": scrap_key,
                "complete": has_mongo,
                "examples": example_keywords
            }
            
            # 分类
            if any(k in name for k in ['Reddit', 'Instagram', 'TikTok', 'Twitter', 'Facebook', 'Youtube', 'Pinterest']):
                categories["社交媒体"].append(crawler_info)
            elif any(k in name for k in ['Amazon', '卖家精灵']):
                categories["电商平台"].append(crawler_info)
            elif any(k in name for k in ['semrush', 'SEMrush', 'Google']):
                categories["SEO工具"].append(crawler_info)
            elif '全案咨询' in name:
                categories["咨询任务"].append(crawler_info)
    
    return categories


def format_crawlers_for_display(categories):
    """
    格式化爬虫列表用于显示给用户
    
    Returns:
        str: 格式化的文本
    """
    lines = []
    lines.append("=" * 100)
    lines.append("🚀 可用的爬虫任务类型")
    lines.append("=" * 100)
    
    for category, crawlers in categories.items():
        if crawlers:
            lines.append(f"\n📌 {category}")
            lines.append("-" * 100)
            for i, c in enumerate(crawlers, 1):
                status = "✅" if c['complete'] else "⚠️ "
                lines.append(f"{status} {i}. {c['name']}")
                lines.append(f"   └─ 项目: {c['project']}")
                lines.append(f"   └─ 字段类型: {c['field']}")
                
                # 显示示例
                if c['examples']:
                    examples_str = "、".join(c['examples'][:3])
                    lines.append(f"   └─ 示例: {examples_str}")
                
                if not c['complete']:
                    lines.append(f"   └─ ⚠️  配置不完整，暂未自动化")
    
    lines.append("\n" + "=" * 100)
    lines.append("💡 提示：请告诉我你想抓哪个平台的数据，以及关键词")
    lines.append("   例如：\"抓Reddit上关于AI的帖子\" 或 \"查Amazon上iPhone的评论\"")
    lines.append("=" * 100)
    
    return "\n".join(lines)


if __name__ == "__main__":
    # 测试
    categories = list_all_crawlers()
    print(format_crawlers_for_display(categories))
