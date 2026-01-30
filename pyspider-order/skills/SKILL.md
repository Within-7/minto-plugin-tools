---
name: pyspider-order
description: "Manage PySpider web scraping tasks through natural language. Use when analysts request: (1) Scraping social media data (Reddit, Instagram, TikTok, Twitter, Facebook), (2) Keyword-based content collection, (3) E-commerce data scraping (Amazon, SellerSprite), (4) SEO data extraction (SEMrush). Maps natural language requests to PySpider projects via Feishu API integration."
---

# PySpider Order

Enable analysts to order web scraping tasks through natural language.

## Core Philosophy

**This is a Tool Operation skill** - Low freedom, precise steps.

The plugin manages complex external systems (Feishu, PySpider). Every decision matters.
Goal: Transform natural language → structured API calls with 100% reliability.

## Mental Model: How to Approach User Requests

### Decision Tree

```
用户请求
    ↓
能否直接解析出"平台+关键词"？
    ↓ Yes
    直接校验参数 → 确认 → 执行
    ↓ No
    用户需求模糊？
    ↓ Yes
    展示分类选项 → 询问平台和关键词
    ↓ No
    用户说了平台但没说关键词？
    ↓ Yes
    确认平台 → 询问关键词
```

### Key Decision Principles

**1. Parse First, Ask Second**
- Always try to extract info from user's initial request
- Don't ask unless necessary
- Example: "抓Reddit上关于AI的帖子" → 直接提取，不要问"哪个平台？"

**2. Guide, Don't Overwhelm**
- If unclear, show categorized options (社交媒体/电商/SEO工具)
- Don't show all 20+ crawlers at once
- Let user drive the conversation

**3. Validate Before Confirming**
- Never skip validation
- Show all collected info before executing
- One final confirmation with all details

**4. Multi-Keyword Awareness**
- Support natural separators: 逗号、顿号、换行
- "AI、machine learning、crypto" → 3 keywords
- "AI, machine learning" → 2 keywords
- Parse automatically, don't ask user to format

## NEVER Do These (Anti-Patterns)

**Interaction Anti-Patterns:**
- ❌ Don't use "其他" (Other) option in AskUserQuestion - causes deadlock
- ❌ Don't ask all questions at once - one question at a time
- ❌ Don't force users to pick from dropdowns - let them type freely
- ❌ Don't treat comma-separated keywords as single keyword

**Technical Anti-Patterns:**
- ❌ NEVER write custom test scripts - always use `scripts/`
- ❌ NEVER skip validation - always use `run.py validate`
- ❌ NEVER access MongoDB directly - only through scripts
- ❌ NEVER execute without user confirmation

## Interaction Examples

### 1. List Available Crawlers

When user request is unclear or wants to see options:

**Use:** `run.py list`

```bash
python run.py list
```

This displays all 20+ crawlers organized by category.

### 2. Order Crawl Task

Parse natural language requests and create scraping tasks:

**MANDATORY Workflow:**
1. Parse user's natural language request → Extract media type + keywords
2. If unclear, use `run.py list` to show options
3. Intelligently parse multi-keywords (support: 逗号、顿号、换行)
4. Validate parameters using `run.py validate`
5. Show confirmation with all collected info
6. Only after user confirms, use `run.py order` to execute

**Execute order:**
```bash
python run.py order "Reddit 关键词下的帖子" "AI, machine learning" "ou_xxx"
```

## Pre-built Scripts (NEVER rewrite these)

**Query & Display:**
- `scripts/list_all_crawlers.py` - List all available crawlers with examples

**Validation:**
- `scripts/validate_params.py` - Strict parameter validation (URL, keywords, multi-keyword parsing)

**Execution:**
- `scripts/create_crawl_order.py` - Complete order workflow (validation → status check → create → dispatch)
- `scripts/check_project_status.py` - Check PySpider project status (internal use)
- `scripts/feishu_client.py` - Feishu API client
- `scripts/pyspider_dispatcher.py` - PySpider dispatcher client

## Parameter Validation

**Always use `run.py validate`:**

```bash
python run.py validate "Reddit 关键词下的帖子" "AI, machine learning"
```

**Validation rules:**
- Multi-keyword support: "AI, machine learning" → ["AI", "machine learning"]
- URL format (Facebook Ads must start with https://www.facebook.com/)
- Keyword length (max 500 chars each)
- Dangerous characters filtered (<, >, ", ', \, ;, $, %, &)
- Max 100 keywords per order
- Media type must exist and be configured

## Error Handling

**Strict policy:**
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

Different PySpider crawlers expect different message fields:

- **keyword** - Single keyword (Reddit, TikTok, Youtube, Pinterest)
- **keywords** - Multiple keywords (Amazon, Facebook Group)
- **tags** - Hashtag/tag (Instagram)
- **brand** - Brand name (SellerSprite)
- **seller** - Seller ID (SellerSprite)
- **url** - URL-based (Facebook Ads, TikTok User)
- **nodeIdPath** - Category path (SellerSprite Category)

The `create_crawl_order.py` script automatically handles this based on CSV config.

## Interaction Examples

**Example 1: User request unclear**
```
User: "帮我抓数据"
Agent: "我可以帮你抓取以下平台的数据：
       
       📱 社交媒体：
       • Reddit - 关键词下的帖子
       • Instagram - 标签下的帖子
       • TikTok - 标签下的帖子
       • Twitter - 关键词下的帖子
       • Facebook - 广告/群组
       
       🛒 电商：
       • Amazon - 产品评论
       • 卖家精灵 - 品牌/卖家/关键词销售额
       
       🔍 SEO工具：
       • SEMrush - 外链数据
       
       告诉我你想抓哪个平台，关键词是什么？"

User: "抓Reddit，关键词是AI"
Agent: [Parse → Validate → Confirm → Execute]
       "确认抓取任务：
        • 媒体: Reddit 关键词下的帖子
        • 关键词: AI
        • 项目: ScrapingRedditByKeyword_api
        确认执行吗？"
```

**Example 2: Clear request with keyword**
```
User: "抓Reddit上关于AI的帖子"
Agent: [Parse → Validate → Confirm → Execute]
       "确认抓取任务：
        • 媒体: Reddit 关键词下的帖子
        • 关键词: AI
        • 项目: ScrapingRedditByKeyword_api
        确认执行吗？"
```

**Example 3: Request without keyword**
```
User: "抓SEMrush外链数据"
Agent: "好的，SEMrush外链数据。请输入要查询的域名："

User: "example.com"
Agent: [Validate → Confirm → Execute]
       "确认抓取任务：
        • 媒体: SEMrush外链数据
        • 域名: example.com
        确认执行吗？"
```

**Example 4: User wants custom platform not in list**
```
User: "我要抓Pinterest数据"
Agent: "好的，Pinterest数据。关键词是什么？"

User: "travel"
Agent: [Validate → Confirm → Execute]
       "确认抓取任务：
        • 媒体: Pinterest
        • 关键词: travel
        确认执行吗？"
```

## IMPORTANT: Interaction Pattern

**✅ DO - 逐步询问，自然对话**：
1. 展示选项帮助用户理解（不要一次性展示太多，分类展示）
2. 每次只问一个问题
3. 等待用户回复后，再问下一个问题
4. 允许用户用自然语言描述，不要强制选择选项
5. 智能解析多关键词：支持空格、逗号、顿号、换行等分隔符
6. 最后一次性确认所有信息

**❌ DON'T - 避免这些错误做法**：
1. 不要用"其他"选项 - 会导致死锁，用户无法输入
2. 不要一次性问所有问题 - 给用户压力
3. 不要用 AskUserQuestion 提供选项后，无法继续输入
4. 不要强制用户按照格式输入 - 先尝试理解自然语言
5. 不要把逗号分隔的关键词当作单个关键词

**Pattern**:
- 如果用户在初始请求中提供了关键词 → 智能解析（支持多关键词）→ 直接校验并确认
- 如果用户没提供关键词 → 先展示选项，然后询问"告诉我你想抓哪个平台，关键词是什么？"
- 支持用户说"AI、machine learning、crypto"或"AI, machine learning, crypto"
- 自动解析成列表：`["AI", "machine learning", "crypto"]`
- 保持对话连续性，像真人对话一样

**After Order Success Response:**
```
✅ 下单成功！

任务ID: xxx
飞书记录ID: xxx
项目: xxx

📤 已通知飞书群：@你 @爬虫工程师

正在抓取中，请耐心等待，完成后会通过飞书通知你结果📬
```

## Workflow Summary

1. **Understand** - Parse user request (extract media type + keywords if provided)
2. **Guide** - If unclear, show categorized crawler options (社交媒体/电商/SEO工具)
3. **Ask** - One question at a time, wait for user response
4. **Validate** - Use `run.py validate` strictly
5. **Confirm** - Show all collected info and ask for final confirmation
6. **Execute** - Use `run.py order` (handles all steps)
7. **Notify** - Success/failure notifications via Feishu

**NEVER skip steps or write custom scripts. Always use run.py for all operations.**
