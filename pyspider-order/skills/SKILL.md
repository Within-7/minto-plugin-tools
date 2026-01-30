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

**CRITICAL**: Execute step-by-step. NEVER skip steps or combine them. Each step MUST complete successfully before proceeding.

### Step 1: Parse Request (DO NOT SKIP)

Extract from user's natural language:
- Platform (媒体类型) - e.g., "Reddit 关键词下的帖子"
- Keywords (关键词) - e.g., ["AI", "machine learning"]

**If unclear**: Show available platforms:
```python
from scripts.crawlers import format_crawlers_for_display
available = format_crawlers_for_display()
print(available)
```

**Ask user**: "请选择平台：\n1. Reddit (关键词)\n2. Instagram (标签)\n3. TikTok (关键词)\n4. ..."

**STOP HERE until user provides platform + keywords**

### Step 2: Get Crawler Config (CRITICAL - DO NOT SKIP)

```python
from scripts.crawlers import get_crawler_info

info = get_crawler_info(media_type)
if not info:
    available = format_crawlers_for_display()
    return f"❌ 不支持的平台: {media_type}\n\n{available}"

project = info["project"]
field = info["field"]
validation = info.get("validation")  # e.g., "must start with https://www.facebook.com/"
```

**DO NOT PROCEED if config not found**

### Step 3: Validate Parameters (CRITICAL - DO NOT SKIP)

**Facebook Ads**: URL must start with `https://www.facebook.com/`
- Check: `keyword.startswith('https://www.facebook.com/')`
- If invalid: Return error with format requirement

**Other platforms**: Basic validation (not empty, length < 500)

**DO NOT PROCEED if validation fails**

### Step 4: Check PySpider Project Status (CRITICAL - DO NOT SKIP)

```python
from scripts.check_project_status import check_project_status

status = check_project_status(project)
if not status['exists']:
    return f"❌ PySpider项目不存在: {project}\n请联系爬虫工程师确认项目配置"

if not status['can_run']:
    return f"❌ PySpider项目状态异常: {status['status']}\n项目必须处于 RUNNING 或 DEBUG 状态才能执行\n请联系爬虫工程师处理"
```

**DO NOT PROCEED if project not RUNNING or DEBUG**

### Step 5: Create Feishu Record (DO NOT PROCEED if environment variables not set)

**First check environment variables**:
```python
import os
if not os.getenv('MONGODB_URL'):
    return "❌ 环境变量 MONGODB_URL 未配置\n请设置: export MONGODB_URL=\"mongodb://user:pass@host:port\""

if not os.getenv('FEISHU_API_URL'):
    return "❌ 王试飞书API连接失败: $FEISHU_API_URL 未配置\n请参考 README.md 配置环境变量"
```

**Then create record**:
```python
from scripts.feishu_client import FeishuClient
from scripts.order import create_order

result = create_order(media_type, keywords, task_user='minto')

if not result['success']:
    return f"❌ 下单失败: {result['message']}"

return f"✅ 下单成功！\n{result['message']}"
```

**DO NOT PROCEED if Feishu API fails**

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

### Example 1: Successful Request

**User**: "帮我抓取Reddit上关于AI的帖子"

**AI Execution**:
```
Step 1: Parse → platform="Reddit 关键词下的帖子", keywords=["AI"]
Step 2: Get config → project="ScrapingRedditByKeyword_api", field="keyword"
Step 3: Validate → ✓ (no special validation needed)
Step 4: Check status → ✓ RUNNING
Step 5: Create record → record_id="rec123"
Step 6: Send task → ✓ 1/1 keywords sent
Step 7: Update & notify → ✓
```

**Response**: "✅ 下单成功！\n任务ID: xxx-xxx-xxx\n飞书记录ID: rec123\n项目: ScrapingRedditByKeyword_api\n成功发送 1/1 个关键词"

---

### Example 2: Validation Failure

**User**: "抓取Facebook广告，https://example.com/ads"

**AI Execution**:
```
Step 1: Parse → platform="Facebook Ads 主页下的广告", keywords=["https://example.com/ads"]
Step 2: Get config → field="url", validation="must start with https://www.facebook.com/"
Step 3: Validate → ✗ URL format error (doesn't start with https://www.facebook.com/)
```

**Response**: "❌ Facebook URL格式错误: https://example.com/ads\n\n格式要求：必须以 https://www.facebook.com/ 开头\n\n请提供正确的Facebook Ads URL"

---

### Example 3: Platform Not Supported

**User**: "帮我抓取LinkedIn数据"

**AI Execution**:
```
Step 1: Parse → platform="LinkedIn", keywords=unknown
Step 2: Get config → get_crawler_info("LinkedIn") = None
```

**Response**: "❌ 不支持的平台: LinkedIn\n\n支持的平台：\n📱 社交媒体：\n- Reddit 关键词下的帖子 (keyword)\n- Instagram 标签下的帖子 (tags)\n- TikTok 标签下的帖子 (keyword)\n- ..."

---

### Example 4: Project Status Error

**User**: "抓取SEMrush外链数据，baidu.com"

**AI Execution**:
```
Step 1: Parse → platform="semrush中的外链数据抓取", keywords=["baidu.com"]
Step 2: Get config → project="BackLink", field="keyword"
Step 3: Validate → ✓
Step 4: Check status → ✗ status="STOP" (not RUNNING/DEBUG)
```

**Response**: "❌ PySpider项目状态异常: STOP\n\n项目: BackLink\n当前状态: STOP\n要求状态: RUNNING 或 DEBUG\n\n请联系爬虫工程师处理"

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

## Troubleshooting

### If execution fails, check in order:

**1. Environment Variables (CRITICAL)**
```bash
# Check all required variables are set
echo $MONGODB_URL
echo $FEISHU_API_URL
echo $FEISHU_TABLE_TOKEN
echo $FEISHU_TABLE_ID
echo $FEISHU_WEBHOOK
echo $PYSPIDER_BASE_URL
echo $PYSPIDER_SESSION_COOKIE
```

If any are empty → "❌ 环境变量未配置，请设置后重试"

**2. Feishu API Connection**
```bash
# Test Feishu API
curl -s "$FEISHU_API_URL/api/query_scraping_form_data" | jq .
```

If connection fails → "❌ 无法连接飞书API: $FEISHU_API_URL\n请检查网络和API地址"

**3. PySpider Project Status**
```python
from scripts.check_project_status import check_project_status
status = check_project_status('BackLink')
print(f"Exists: {status['exists']}, Status: {status['status']}, Can Run: {status['can_run']}")
```

**4. MongoDB Connection**
```python
from pymongo import MongoClient
import os
client = MongoClient(os.getenv('MONGODB_URL'))
print('✓ MongoDB connected' if client else '❌ MongoDB connection failed')
```

### Common Issues

| Error | Cause | Solution |
|------|-------|----------|
| ModuleNotFoundError: No module named 'scripts' | Wrong working directory | cd to project root containing scripts/ directory |
| ❌ 环境变量未配置 | .env not loaded | Set environment variables from README.md |
| ❌ 无法连接飞书API | Wrong API URL or network | Check $FEISHU_API_URL and network connection |
| ❌ PySpider项目不存在 | Project not in MongoDB | Contact 爬虫工程师 to add project |
| ❌ PySpider项目状态异常 | Project stopped/error | Contact 爬虫工程师 to start project |
