---
name: pyspider-order
description: "Manage PySpider web scraping tasks via Feishu API. Use when users request: (1) Social media scraping (Reddit, Instagram, TikTok, Twitter, Facebook), (2) E-commerce data (Amazon, 卖家精灵), (3) SEO data (SEMrush). Maps natural language to PySpider projects with validation, status checks, and notifications."
---

# PySpider Task Management

**Tool Operation Skill** - Low freedom, precise steps for external system integration.

## Purpose

Enable analysts to order PySpider web scraping tasks through natural language. Integrates Feishu API and PySpider dispatcher with validation and error handling.

## Trigger

Use when user requests:
- "抓取 Reddit/Instagram/TikTok/Twitter/Facebook 数据"
- "Amazon 评论/卖家精灵数据"
- "SEMrush 外链数据"
- Any web scraping from social media, e-commerce, or SEO tools

## Workflow

**MANDATORY**: Always follow this exact sequence:

1. **Parse Request** → Extract platform + keywords from natural language
2. **Get Config** → `from scripts.crawlers import get_crawler_info`
3. **Validate** → Check Facebook URL format if applicable
4. **Check Status** → `from scripts.check_project_status import check_project_status`
5. **Create Record** → `from scripts.feishu_client import FeishuClient`
6. **Send Task** → `from scripts.pyspider_dispatcher import PySpiderDispatcher`
7. **Update & Notify** → Update status to "抓取中", send Feishu notification

## Supported Platforms

**Social Media** (field type):
- Reddit 关键词下的帖子 (keyword)
- Instagram 标签下的帖子 (tags)
- TikTok 标签下的帖子 (keyword)
- Twitter 关键词下的帖子 (keyword)
- Facebook Ads 主页下的广告 (url, must start with https://www.facebook.com/)
- Youtube 关键词下的视频 (keyword)
- Pinterest 关键词的所有帖子 (keyword)

**E-commerce**:
- Amazon列表所有产品及评论 (keywords)
- 卖家精灵的品牌销售额数据 (brand)
- 卖家精灵的卖家销售额数据 (seller)
- 卖家精灵的关键词销售额数据 (keyword)

**SEO Tools**:
- semrush中的外链数据抓取 (keyword)

## NEVER

- ❌ Skip parameter validation
- ❌ Execute without checking PySpider project status (must be RUNNING or DEBUG)
- ❌ Use command line interface (`python run.py...`) - Use Python imports instead
- ❌ Create orders for incomplete crawlers (check crawler info exists first)

## Error Handling

- **Validation errors** → Show specific error with format requirements
- **Project not found** → Notify via Feishu, mark as "等待手动处理"
- **Project status error** (not RUNNING/DEBUG) → Notify via Feishu, mark as "等待手动处理"
- **API failures** → Notify via Feishu, mark as "等待手动处理"

## Example Interactions

**User**: "帮我抓取Reddit上关于AI的帖子"
**AI**: 
1. Parse: platform="Reddit 关键词下的帖子", keywords=["AI"]
2. Get config: project="ScrapingRedditByKeyword_api", field="keyword"
3. Validate: ✓ (no special validation for Reddit)
4. Check status: ✓ RUNNING
5. Execute: `create_order("Reddit 关键词下的帖子", ["AI"], task_user="ou_xxx")`

**User**: "抓取Facebook广告，https://example.com/ads"
**AI**: 
1. Parse: platform="Facebook Ads 主页下的广告", keywords=["https://example.com/ads"]
2. Get config: field="url", validation="must start with https://www.facebook.com/"
3. Validate: ✗ URL format error
4. Response: "❌ Facebook URL格式错误: https://example.com/ads\n必须以 https://www.facebook.com/ 开头"

## Environment Variables Required

```bash
MONGODB_URL              # MongoDB connection
FEISHU_API_URL          # Feishu API server
FEISHU_TABLE_TOKEN       # Feishu table token
FEISHU_TABLE_ID          # Feishu table ID
FEISHU_WEBHOOK           # Feishu webhook URL
PYSPIDER_BASE_URL        # PySpider server URL
PYSPIDER_SESSION_COOKIE   # PySpider session cookie
```

## Implementation Notes

- All scripts in `scripts/` directory
- Main function: `scripts.order.create_order(media_type, keywords, task_user)`
- Crawler config: `scripts.crawlers.get_crawler_info(name)`
- No CLI commands needed - Minto calls Python functions directly
