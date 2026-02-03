"""爬虫配置 - 支持的爬虫列表和元数据

从CSV迁移而来，精简为Python字典，提高可读性和性能。
"""

CRAWLERS = {
    # ========== 社交媒体 ==========
    "Reddit 关键词下的帖子": {
        "project": "ScrapingRedditByKeyword_api",
        "field": "keyword",
        "category": "社交媒体",
        "examples": ["AI", "machine learning"]
    },
    "Reddit某群组的所有帖子": {
        "project": "ScrapingRedditAllPostByKeyword_api",
        "field": "keyword",
        "category": "社交媒体",
        "examples": ["python", "javascript"]
    },
    "Instagram 标签下的帖子": {
        "project": "ScrapingInstagramPostsFromTagsSearch",
        "field": "tags",
        "category": "社交媒体",
        "examples": ["fashion", "travel"]
    },
    "Instagram 标签下的帖子_补充": {
        "project": "ScrapingInstagramPostsFromTagsSearchByAccount",
        "field": "tags",
        "category": "社交媒体",
        "examples": ["food", "art"]
    },
    "TikTok 标签下的帖子": {
        "project": "ScrapingTiktokByKeywordsFromBD",
        "field": "keyword",
        "category": "社交媒体",
        "examples": ["crypto", "dance"]
    },
    "TikTok 用户发布的视频": {
        "project": "ScrapingTikTokUserProfileProject",
        "field": "url",
        "category": "社交媒体",
        "examples": ["https://www.tiktok.com/@username"]
    },
    "Twitter 关键词下的帖子": {
        "project": "ScrapingTwitterPostsByTags",
        "field": "keyword",
        "category": "社交媒体",
        "examples": ["tech", "news"]
    },
    "Youtube 关键词下的视频": {
        "project": "ScrapingYoutubeVideosByKeywordsV001",
        "field": "keyword",
        "category": "社交媒体",
        "examples": ["music", "gaming"]
    },
    "Pinterest 关键词的所有帖子": {
        "project": "ScrapingPinterestPostByKeywords",
        "field": "keyword",
        "category": "社交媒体",
        "examples": ["food", "DIY"]
    },
    "Pinterest 博主的所有帖子": {
        "project": "ScrapingPinterestProfilePosts",
        "field": "keyword",
        "category": "社交媒体",
        "examples": ["travel", "photography"]
    },
    
    # ========== 电商 ==========
    "Amazon列表所有产品及评论": {
        "project": "ScrapingAmazonListByKeywords",
        "field": "keywords",
        "category": "电商",
        "examples": ["iPhone", "laptop"]
    },
    "卖家精灵的品牌销售额数据": {
        "project": "ScrapingMjjlDispatcherByBrand",
        "field": "brand",
        "category": "电商",
        "examples": ["Nike", "Apple"]
    },
    "卖家精灵的卖家销售额数据": {
        "project": "ScrapingMjjlDispatcherBySeller",
        "field": "seller",
        "category": "电商",
        "examples": ["seller123"]
    },
    "卖家精灵的关键词销售额数据": {
        "project": "ScrapingMjjlDispatcherByKeyword",
        "field": "keyword",
        "category": "电商",
        "examples": ["wireless headphones"]
    },
    "卖家精灵的类目销售额数据": {
        "project": "ScrapingMjjlDispatcherBynodeIdPath",
        "field": "nodeIdPath",
        "category": "电商",
        "examples": ["category_path"]
    },
    "卖家精灵的全站品牌销售额数据": {
        "project": "ScrapingMjjlDispatcherByBrandAllStation",
        "field": "brand",
        "category": "电商",
        "examples": ["Samsung"]
    },
    "卖家精灵的全站关键词销售额数据": {
        "project": "ScrapingMjjlDispatcherByKeywordAllStation",
        "field": "keyword",
        "category": "电商",
        "examples": ["smartphone"]
    },
    
    # ========== Facebook ==========
    "Facebook Ads 主页下的广告": {
        "project": "ScrapingFacebookUserDetailByBright",
        "field": "url",
        "category": "社交媒体",
        "examples": ["https://www.facebook.com/example"],
        "validation": "must start with https://www.facebook.com/"
    },
    "[手动]fb群组人群帖子活跃度": {
        "project": "ScrapingFacebookGroupsByGoogleUrl",
        "field": "keywords",
        "category": "社交媒体",
        "examples": ["group_name"]
    },
    
    # ========== SEO工具 ==========
    "semrush中的外链数据抓取": {
        "project": "BackLink",
        "field": "keyword",
        "category": "SEO工具",
        "examples": ["example.com"]
    },
    
    # ========== 咨询任务 ==========
    "【全案咨询】分词任务": {
        "project": "ScrapingHandlerArticlesUrl",
        "field": "keyword",
        "category": "咨询任务",
        "examples": ["article_url"]
    },
}

# 字段类型说明
FIELD_TYPES = {
    "keyword": "单个关键词（Reddit/TikTok/Youtube/Pinterest）",
    "keywords": "多个关键词（Amazon/Facebook Group）",
    "tags": "标签/话题（Instagram）",
    "brand": "品牌名称（卖家精灵）",
    "seller": "卖家ID（卖家精灵）",
    "url": "URL地址（Facebook Ads/TikTok User）",
    "nodeIdPath": "类目路径（卖家精灵分类）"
}


def get_crawler_info(name: str) -> dict:
    """获取爬虫配置信息"""
    return CRAWLERS.get(name)


def get_crawler_project(name: str) -> str:
    """获取爬虫对应的PySpider项目名"""
    info = CRAWLERS.get(name)
    return info["project"] if info else None


def get_crawler_field(name: str) -> str:
    """获取爬虫的字段类型"""
    info = CRAWLERS.get(name)
    return info["field"] if info else None


def list_crawlers(category: str = None) -> list:
    """列出爬虫，可按分类筛选
    
    Args:
        category: 分类筛选（可选）
    
    Returns:
        爬虫名称列表
    """
    if category:
        return [k for k, v in CRAWLERS.items() if v.get("category") == category]
    return list(CRAWLERS.keys())


def list_categories() -> list:
    """列出所有分类"""
    categories = set()
    for info in CRAWLERS.values():
        if "category" in info:
            categories.add(info["category"])
    return sorted(categories)


def format_crawlers_for_display(category: str = None) -> str:
    """格式化爬虫列表用于显示
    
    Args:
        category: 分类筛选（可选）
    
    Returns:
        格式化的文本
    """
    lines = []
    lines.append("=" * 80)
    lines.append("🚀 可用的爬虫任务类型")
    lines.append("=" * 80)
    
    # 按分类组织
    by_category = {}
    for name, info in CRAWLERS.items():
        cat = info.get("category", "其他")
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append((name, info))
    
    # 显示每个分类
    for cat in sorted(by_category.keys()):
        crawlers = by_category[cat]
        lines.append(f"\n📌 {cat}")
        lines.append("-" * 80)
        for i, (name, info) in enumerate(crawlers, 1):
            project = info["project"]
            field = info["field"]
            examples = info.get("examples", [])
            
            lines.append(f"  {i}. {name}")
            lines.append(f"     └─ 项目: {project}")
            lines.append(f"     └─ 字段: {field}")
            if examples:
                examples_str = "、".join(examples[:3])
                lines.append(f"     └─ 示例: {examples_str}")
    
    lines.append("\n" + "=" * 80)
    return "\n".join(lines)


if __name__ == "__main__":
    # 测试
    print(format_crawlers_for_display())
