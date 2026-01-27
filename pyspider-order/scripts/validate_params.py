"""参数校验脚本 - 严格校验用户输入的爬虫参数"""
import re
import csv
import os


class ValidationError(Exception):
    """参数校验失败异常"""
    pass


def load_crawler_config(csv_path=None):
    """加载爬虫配置"""
    if csv_path is None:
        # CSV在项目根目录（用户安装skill后的工作目录）
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # skill目录: project_root/.minto/skills/pyspider-order/skills/
        # 项目根目录: 向上4级
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))))
        csv_path = os.path.join(project_root, 'feishudb.ScrapingMongoQuery.csv')
    
    config = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get('name', '')
            config[name] = {
                'project': row.get('table', ''),
                'field': row.get('scrap_key', ''),
                'complete': bool(row.get('mongo_list[0]', ''))
            }
    return config


def validate_media_type(media_type, config=None):
    """
    校验媒体类型是否有效
    
    Args:
        media_type: 媒体类型名称
        config: 爬虫配置字典
        
    Returns:
        dict: 爬虫配置信息
        
    Raises:
        ValidationError: 媒体类型无效或未配置完成
    """
    if config is None:
        config = load_crawler_config()
    
    if media_type not in config:
        available = [k for k, v in config.items() if v['complete']]
        raise ValidationError(
            f"❌ 不支持的媒体类型: {media_type}\n\n"
            f"支持的媒体类型:\n" + "\n".join([f"  - {m}" for m in available])
        )
    
    crawler_info = config[media_type]
    
    if not crawler_info['complete']:
        raise ValidationError(
            f"⚠️  {media_type} 配置不完整，暂未自动化\n"
            f"请联系爬虫工程师配置"
        )
    
    return crawler_info


def validate_keyword(keyword, field_type='keyword'):
    """
    校验关键词参数
    
    Args:
        keyword: 关键词
        field_type: 字段类型 (keyword/keywords/tags/brand/seller/url/nodeIdPath)
        
    Returns:
        str: 校验后的关键词
        
    Raises:
        ValidationError: 关键词无效
    """
    if not keyword or not isinstance(keyword, str):
        raise ValidationError("❌ 关键词不能为空")
    
    keyword = keyword.strip()
    
    if not keyword:
        raise ValidationError("❌ 关键词不能为空")
    
    # 长度限制
    if len(keyword) > 500:
        raise ValidationError("❌ 关键词长度不能超过500字符")
    
    # 根据字段类型特殊校验
    if field_type == 'url':
        # URL格式校验
        # Facebook Ads 必须以 https://www.facebook.com/ 开头
        if 'facebook' in keyword.lower() and not keyword.startswith('https://www.facebook.com/'):
            raise ValidationError(
                f"❌ Facebook Ads URL格式错误\n"
                f"   必须以 https://www.facebook.com/ 开头\n"
                f"   当前: {keyword}"
            )
        
        # TikTok User URL 校验
        if 'tiktok.com' in keyword.lower():
            if not keyword.startswith(('http://', 'https://')):
                raise ValidationError(
                    f"❌ TikTok URL格式错误\n"
                    f"   必须以 http:// 或 https:// 开头"
                )
        
        # 通用URL格式校验
        url_pattern = re.compile(
            r'^https?://'  # http or https
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
            r'localhost|'  # localhost
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE
        )
        
        if not url_pattern.match(keyword):
            raise ValidationError(f"❌ URL格式无效: {keyword}")
    
    elif field_type == 'brand' or field_type == 'seller':
        # 品牌/卖家名称 - 只允许字母、数字、中文、常见符号
        if not re.match(r'^[\w\u4e00-\u9fa5\s\-\.]+$', keyword):
            raise ValidationError(
                f"❌ {field_type}格式无效\n"
                f"   只允许字母、数字、中文、空格、横线、点号"
            )
    
    elif field_type == 'keyword' or field_type == 'keywords' or field_type == 'tags':
        # 关键词 - 过滤特殊字符
        dangerous_chars = ['<', '>', '"', "'", '\\', ';', '$', '%', '&']
        found = [c for c in keyword if c in dangerous_chars]
        if found:
            raise ValidationError(
                f"❌ 关键词包含非法字符: {', '.join(found)}\n"
                f"   关键词: {keyword}"
            )
    
    return keyword


def validate_keywords_list(keywords, field_type='keyword'):
    """
    校验关键词列表
    
    Args:
        keywords: 关键词或关键词列表
        field_type: 字段类型
        
    Returns:
        list: 校验后的关键词列表
        
    Raises:
        ValidationError: 关键词列表无效
    """
    if isinstance(keywords, str):
        keywords = [keywords]
    
    if not isinstance(keywords, list):
        raise ValidationError("❌ 关键词必须是字符串或字符串列表")
    
    if len(keywords) == 0:
        raise ValidationError("❌ 关键词列表不能为空")
    
    if len(keywords) > 100:
        raise ValidationError("❌ 关键词数量不能超过100个")
    
    validated = []
    for kw in keywords:
        validated_kw = validate_keyword(kw, field_type)
        validated.append(validated_kw)
    
    # 去重
    seen = set()
    unique = []
    for kw in validated:
        if kw.lower() not in seen:
            seen.add(kw.lower())
            unique.append(kw)
    
    return unique


def validate_crawl_params(media_type, keywords, config=None):
    """
    完整的爬虫参数校验
    
    Args:
        media_type: 媒体类型
        keywords: 关键词或关键词列表
        config: 爬虫配置
        
    Returns:
        dict: {
            'media_type': str,
            'project': str,
            'field': str,
            'keywords': list,
            'validated': True
        }
        
    Raises:
        ValidationError: 校验失败
    """
    # 加载配置
    if config is None:
        config = load_crawler_config()
    
    # 校验媒体类型
    crawler_info = validate_media_type(media_type, config)
    field_type = crawler_info['field']
    
    # 校验关键词
    validated_keywords = validate_keywords_list(keywords, field_type)
    
    return {
        'media_type': media_type,
        'project': crawler_info['project'],
        'field': field_type,
        'keywords': validated_keywords,
        'validated': True
    }


if __name__ == "__main__":
    # 测试
    try:
        # 测试1: 正常关键词
        result = validate_crawl_params("Reddit 关键词下的帖子", "AI")
        print("✅ 测试1通过:", result)
        
        # 测试2: URL校验
        result = validate_crawl_params(
            "Facebook Ads 主页下的广告",
            "https://www.facebook.com/example"
        )
        print("✅ 测试2通过:", result)
        
        # 测试3: 无效URL
        # validate_crawl_params("Facebook Ads 主页下的广告", "invalid-url")
        
        # 测试4: 不支持的媒体类型
        # validate_crawl_params("不存在的媒体", "test")
        
    except ValidationError as e:
        print(f"❌ 校验失败: {e}")
