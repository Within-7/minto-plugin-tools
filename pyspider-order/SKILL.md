---
name: pyspider-order
description: "Manage PySpider web scraping tasks through natural language. Use when analysts request: (1) Scraping social media data (Reddit, Instagram, TikTok, Twitter, Facebook), (2) Keyword-based content collection, (3) E-commerce data scraping (Amazon, SellerSprite), (4) SEO data extraction (SEMrush). Maps natural language requests to PySpider projects via Feishu API integration."
---

# PySpider Order

Enable analysts to order web scraping tasks through natural language conversation.

## ⚠️ CRITICAL: Interaction Rules

**MUST follow these constraints:**

1. **NEVER write test scripts automatically** - Always use pre-built scripts from scripts/
2. **NEVER execute without confirmation** - Must show confirmation dialog before any API calls
3. **ALWAYS parse natural language first** - Extract media type and keywords from user request
4. **CHECK message field type** - Different crawlers use different message fields (keyword/keywords/tags/url/brand/seller)
5. **VALIDATE parameters strictly** - Use scripts/validate_params.py for all user inputs
6. **NEVER access MongoDB directly** - Only through scripts/check_project_status.py (internal use)

## 🚨 CRITICAL: Debugging Rules (NEW!)

**当用户报告问题或要求修复bug时，必须严格遵守以下流程：**

### 禁止行为（DO NOT DO）：
- ❌ **不要盲目执行测试代码** - 问题分析和代码审查应该在大脑中完成
- ❌ **不要反复bash运行** - 每次运行可能触发实际业务操作（如发送爬虫任务）
- ❌ **不要边试边改** - 这是低效的，容易产生副作用
- ❌ **不要忽视用户指令** - 如果用户说"别执行"、"先分析"，必须立即停止执行

### 必须遵守的流程（MUST FOLLOW）：

**阶段1：理解问题（只读，不执行）**
1. 仔细阅读相关代码文件
2. 理解现有的业务流程和数据流
3. 找出问题可能的原因
4. 列出所有可能的解决方案

**阶段2：方案确认（与用户沟通）**
1. 向用户解释你的分析结果
2. 提出多个解决方案（如果有）
3. 说明每个方案的优缺点
4. **等待用户确认后再执行**

**阶段3：实施修改（一次性完成）**
1. 基于确认的方案，直接修改代码
2. 一次性完成所有相关修改
3. 向用户说明改了什么、为什么这样改

### 具体案例 - 飞书记录创建问题：

**错误做法（已犯）：**
```
用户：飞书记录没创建
我：bash测试 → 发现字段不存在 → 改字段 → bash测试 → 又失败 → 改字段 → ...
后果：发送了多次重复的爬虫任务
```

**正确做法（应该）：**
```
用户：飞书记录没创建
我：
1. 阅读 feishu.py 第962-1010行，理解创建流程
2. 阅读 pyspider_crawl.py，理解业务流程
3. 分析：现有流程是"先创建记录，后发爬虫"
4. 发现问题：飞书字段ID和显示名不一致
5. 向用户说明问题和解决方案
6. 等待用户确认后，一次性修改代码
```

### 自检清单：
在执行任何bash命令前，问自己：
- [ ] 这个命令会触发实际业务操作吗？（发消息、写数据库、调用API）
- [ ] 用户已经明确要求我执行了吗？
- [ ] 我有没有充分分析问题的根源？
- [ ] 有没有更安全的分析方法（只读文件、查看日志）？

**如果答案都是"是"，才能执行。否则，先分析，再沟通，最后执行。**

## Core Capabilities

### 1. List Available Crawlers

When user request is unclear or wants to see options:

**Use:** `scripts/list_all_crawlers.py`

```python
from scripts.list_all_crawlers import list_all_crawlers, format_crawlers_for_display

categories = list_all_crawlers()
print(format_crawlers_for_display(categories))
```

This displays all 20+ crawlers organized by category with examples.

### 2. Order Crawl Task

Parse natural language requests and create scraping tasks:

**MANDATORY Workflow:**
1. Parse user's natural language request → Extract media type + keywords
2. If unclear, use `list_all_crawlers.py` to show options
3. Ask for user's Feishu open_id (optional but recommended for proper attribution)
4. Validate parameters using `scripts/validate_params.py`
5. Show confirmation dialog using AskUserQuestion
6. Only after user confirms, use `scripts/create_crawl_order.py` to execute

**Execute order:**
```python
from scripts.create_crawl_order import create_crawl_order, format_order_result

result = create_crawl_order(
    media_type="Reddit 关键词下的帖子",
    keywords="AI",
    task_user="ou_xxxxxxxxxxxxx"  # Optional: User's Feishu open_id
)
print(format_order_result(result))
```

**⚠️ IMPORTANT: Feishu Field Mapping**
The plugin uses Chinese field names (not English) for Feishu Bitable:
- `任务类型` ← media_type (e.g., "Reddit 关键词下的帖子")
- `关键词1`, `关键词2`, ... ← keywords array
- `数据抓取状态` ← Fixed value: "等待处理"
- `紧急程度` ← Fixed value: "一般（今天）"
- `工单发起人` ← Optional: user object {id, name}
- `charge任务` ← Optional: user ID array

**User Attribution:**
- If `task_user` is provided: sets 工单发起人 and charge任务
- If not provided: Feishu system uses default values (may show as "任务分发")
- Recommended: Always ask user for their Feishu open_id for proper tracking

### 3. Check Task Progress

Query Feishu API for task status:

**Use:** `scripts/query_task_progress.py`

```python
from scripts.query_task_progress import query_all_tasks, format_tasks_for_display

tasks = query_all_tasks()
print(format_tasks_for_display(tasks, show_all=False))
```

## Pre-built Scripts (NEVER rewrite these)

**Query & Display:**
- `scripts/list_all_crawlers.py` - List all available crawlers with examples
- `scripts/query_task_progress.py` - Query Feishu task status

**Validation:**
- `scripts/validate_params.py` - Strict parameter validation (URL, keywords, etc.)

**Execution:**
- `scripts/create_crawl_order.py` - Complete order workflow (validation → status check → create → dispatch)
- `scripts/check_project_status.py` - Check PySpider project status (internal use)
- `scripts/feishu_client.py` - Feishu API client
- `scripts/pyspider_dispatcher.py` - PySpider dispatcher client

## Parameter Validation

**Always use `scripts/validate_params.py`:**

```python
from scripts.validate_params import validate_crawl_params, ValidationError

try:
    validated = validate_crawl_params(media_type, keywords)
    # validated contains:
    # - media_type, project, field, keywords, validated
except ValidationError as e:
    # Show error to user, guide them to fix
    print(str(e))
```

**Validation rules:**
- URL format (Facebook Ads must start with https://www.facebook.com/)
- Keyword length (max 500 chars)
- Dangerous characters filtered (<, >, ", ', \, ;, $, %, &)
- Max 100 keywords per order
- Media type must exist and be configured

## Error Handling

**Strict security policy:**
- For validation errors → Show specific error, guide user to fix
- For project status errors → Notify 爬虫工程师 via Feishu
- For API failures → Notify 爬虫工程师 via Feishu
- NEVER attempt to fix technical issues automatically

**Error notification:**
```python
from scripts.feishu_client import FeishuClient

feishu = FeishuClient()
feishu.send_notification(
    title="🆘🆘🆘爬虫任务失败🆘🆘🆘",
    text=f"任务执行失败，请联系爬虫工程师\n错误: {error_message}",
    at_user=["ou_a45583a7f2843869b71ff4cc9692cf3d"]
)
```

## Message Field Types (CRITICAL)

Different PySpider crawlers expect different message fields in `on_message()`:

- **keyword** - Single keyword (Reddit, TikTok, Youtube, Pinterest)
- **keywords** - Multiple keywords (Amazon, Facebook Group)
- **tags** - Hashtag/tag (Instagram)
- **brand** - Brand name (SellerSprite)
- **seller** - Seller ID (SellerSprite)
- **url** - URL-based (Facebook Ads, TikTok User)
- **nodeIdPath** - Category path (SellerSprite Category)

The `create_crawl_order.py` script automatically handles this based on CSV config.

## Media Type Mapping

See [references/media_mapping.md](references/media_mapping.md) for complete mapping.

**Quick reference:**

| Natural Language | Feishu Media Type | PySpider Project | Message Field |
|-----------------|-------------------|------------------|---------------|
| Reddit | Reddit 关键词下的帖子 | ScrapingRedditByKeyword_api | keyword |
| Instagram | Instagram 标签下的帖子 | ScrapingInstagramPostsFromTagsSearch | tags |
| TikTok | TikTok 标签下的帖子 | ScrapingTiktokByKeywordsFromBD | keyword |
| Twitter | Twitter 关键词下的帖子 | ScrapingTwitterPostsByTags | keyword |
| Amazon | Amazon列表所有产品及评论 | ScrapingAmazonListByKeywords | keywords |
| 卖家精灵品牌 | 卖家精灵的品牌销售额数据 | ScrapingMjjlDispatcherByBrand | brand |

## Supported Crawlers (20+)

**Social Media:** Reddit, Instagram, TikTok, Twitter, Facebook Ads/Group, Youtube, Pinterest

**E-commerce:** Amazon, SellerSprite (brand/seller/keyword/category)

**SEO Tools:** SEMrush BackLink

**Other:** Google Index tasks, Pinterest profiles

See [references/media_mapping.md](references/media_mapping.md) for complete list.

## Interaction Examples

**Example 1: User request unclear**
```
User: "帮我抓数据"
Agent: [Use list_all_crawlers.py] 
       "我可以帮你抓取以下平台的数据...
       请告诉我你想抓哪个平台？"
```

**Example 2: Clear request with keyword**
```
User: "抓Reddit上关于AI的帖子"
Agent: [Parse → Validate → Confirm → Execute]
       "确认抓取任务
        媒体: Reddit 关键词下的帖子
        关键词: AI
        项目: ScrapingRedditByKeyword_api
        [确认执行] [取消]"
```

**Example 3: Request without keyword**
```
User: "抓SEMrush外链数据"
Agent: "请输入要查询的关键词（域名）："
User: "example.com"
Agent: [Confirm and execute]
```

**Example 4: Check progress**
```
User: "查一下任务进度"
Agent: [Use query_task_progress.py]
       Shows tasks grouped by status
```

**IMPORTANT: Keyword Input Pattern**
- If user provides keyword in initial request → Validate directly
- If user selects "其他" (other) or doesn't provide keyword → Ask for keyword input
- Never use AskUserQuestion with "其他关键词" option that doesn't allow input
- Instead: Ask directly "请输入关键词" or use multi-step conversation

## Workflow Summary

1. **Understand** - Parse user request (extract media type + keywords if provided)
2. **Guide** - If unclear, show crawler options using list_all_crawlers.py
3. **Ask** - If keyword missing, ask user directly (no dropdowns for "other")
4. **Validate** - Use validate_params.py strictly
5. **Confirm** - Always show confirmation dialog with AskUserQuestion
6. **Execute** - Use create_crawl_order.py (handles all steps)
7. **Notify** - Success/failure notifications via Feishu

**NEVER skip steps or write custom scripts. Always use pre-built scripts from scripts/ directory.**
