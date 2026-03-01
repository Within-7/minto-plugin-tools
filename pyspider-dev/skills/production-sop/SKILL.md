---
name: production-sop
description: "Production-grade Pyspider SOP with dual-mode workflows (new project vs refactor), strategy patterns A-E, strict engineering redlines, and best practices. Use when: (1) Creating new Pyspider crawlers with anti-scraping strategies, (2) Refactoring existing production crawlers, (3) Managing database operations for scraping projects, (4) Implementing BrightData V3, Cookie pools, SSR parsing, API forwarding, or dispatchers. Provides strict redlines, zero-field-loss principles, and automation scripts."
---

# Production Pyspider SOP

Comprehensive production-grade SOP for Pyspider crawler development with dual-mode workflows and strategy patterns.

## Dual-Mode Workflows

### Mode 1: New Project Development

Use when creating crawlers from scratch:

1. **Select Strategy Template**: Choose from Strategy A-E based on target website characteristics
2. **Generate Code**: Use strategy template generator to create crawler skeleton
3. **Define Contract**: Check `ScrapingMongoQuery` for preset `name` and `scrap_key`
4. **Assemble**: Use `Functions.get_dict_by_dot` and `raise Exception` for error handling

**Generate Strategy Templates**:
```bash
# Strategy A (BrightData V3)
python scripts/init_strategy_crawler.py TikTokCrawler A ./tiktok_crawler.py

# Strategy B (Cookie Pool)
python scripts/init_strategy_crawler.py FacebookCrawler B ./facebook_crawler.py

# Strategy C (SSR)
python scripts/init_strategy_crawler.py YoutubeCrawler C ./youtube_crawler.py

# Strategy D (API Forward)
python scripts/init_strategy_crawler.py DifyCrawler D ./dify_crawler.py

# Strategy E (Dispatcher)
python scripts/init_strategy_crawler.py MainDispatch E ./main_dispatch.py
```

See [`STRATEGY_DEEP_DIVE.md`](references/STRATEGY_DEEP_DIVE.md) for strategy details and [`strategy_examples.md`](assets/examples/strategy_examples.md) for example implementations.

### Mode 2: Refactor & Debug (CORE REDLINES)

Use when optimizing existing production crawlers:

**1. Contract Lock (Pre-Audit)**
- Extract full Headers from old code via `read_file` (including Sec-* fields)
- Extract all output key names (Result Keys)

**2. Shadow Preservation Principle**
- **NEVER remove browser fingerprint Headers** for code simplicity
- **Field 1:1 Alignment**: Optimized `result` field names must be pixel-perfect with old version
- **Proxy Inheritance**: Never change verified proxy types (e.g., MX residential proxy)

**3. Transparent Auditing**
- If line count decreases significantly, explain what redundant logic was simplified
- Never silently delete core logic

See [`MASTER_SOP.md`](references/MASTER_SOP.md) for complete refactoring guidelines.

## Global Engineering Redlines

### Critical Rules

1. **Exception Must Be Red**: Never use `logger.error` + silent `return`. Always `raise Exception` to trigger FAILED status
2. **Three-in-One Sync**: `Script (on_message)` + `Git (Pure .py)` + `DB (register_business.py)` must be synchronized
3. **Never Modify Name**: Never change `name` field when updating database config (breaks scheduling mapping)
4. **Repository Hygiene**: Git commits only `.py` files. Never commit `./skills`, `.md`, `.json`

See [`PROJECT_GUIDE.md`](references/PROJECT_GUIDE.md) for complete architecture rules.

## Strategy Patterns (A-E)

### Strategy A (BrightData V3)
For top-tier anti-scraping:
- **Pure Request Protocol**: No extra params in URL, exact payload alignment with official CURL examples
- **Hard Redline**: Must validate `records` field. If `status` is `ready/done` but `records == 0`, throw `BD_EMPTY_DATA`

### Strategy B (Cookie Pool)
For strong account binding (Facebook/Reddit/Mjjl):
- Force use `ispProxy_us_`
- Pass `forced_cookies` via `save` parameter

### Strategy C (SSR)
For proxy breakthrough (Youtube/Amazon/Twitter):
- Residential proxy with regex extraction

### Strategy D (API Forward)
For pure APIs and internal AI forwarding:
- Datacenter proxy with MongoDB task status bits

### Strategy E (Dispatcher)
For scheduling and distribution:
- Use `on_message` for fanout and task routing

See [`STRATEGY_DEEP_DIVE.md`](references/STRATEGY_DEEP_DIVE.md) for complete strategy details.

## Database Operations

### Business Registration

Register new crawler mappings in `ScrapingMongoQuery`:

**Pipeline Rules**:
- Use `$match` to match `scrap_key`
- Use `$project` to map fields
- Use Chinese field names for Excel display

**Tool Usage**:
```bash
# Set environment variables (optional, defaults available)
export MONGO_URI='mongodb://user:pass@host:port/?tls=false'
export MONGO_DB='feishudb'
export MONGO_COLLECTION='ScrapingMongoQuery'

# Register business config
python3 scripts/register_business.py '<JSON_CONFIG>'
```

**Environment Variables**:
- `MONGO_URI` - MongoDB connection URI (default: production URI)
- `MONGO_DB` - Database name (default: feishudb)
- `MONGO_COLLECTION` - Collection name (default: ScrapingMongoQuery)

See [`DATABASE_OPS_GUIDE.md`](references/DATABASE_OPS_GUIDE.md) for details.

### Project Destruction

Delete crawler with proper cleanup:

1. **Physical Delete**: `rm [Script].py`
2. **Git Sync**: `git add .` → `git commit`
3. **DB Cleanup**: `python3 scripts/delete_project.py [project_name]`

**Environment Variables** (same as registration):
- `MONGO_URI` - MongoDB connection URI (default: production URI)
- `MONGO_DB` - Database name (default: projectdb)
- `MONGO_COLLECTION` - Collection name (default: projectdb)

## Communication Protocol

- **Non-Read Must Sync**: Any modification or database write operation must sync logic changes and get confirmation first

## Exception Management

### General Redlines

- **Forbidden**: `except Exception as e: pass`
- **Allowed**: For network fluctuations (e.g., 599), use `@catch_status_code_error` for Pyspider handling
- **Monitoring Alignment**: Core resource depletion (Cookie/Proxy exhaustion) must NOT throw error in `on_message` or `on_start`. Must pass error marker via `save`, throw exception in `callback` phase

**Purpose**: Ensure exceptions occur within Pyspider task lifecycle, generating red `FAILED` status and triggering n8n Webhook.

### Refactoring Redline: Zero Field Loss

**Principle**: When optimizing production scripts, data structure (Payload/Result) priority > code elegance

**Action**: Never delete any "useless" API parameters (e.g., `nodeIdPaths`) unless confirmed as dirty data

## Universal Interface: on_message Driven

All scripts must implement:

```python
def on_message(self, project, message):
    if project == self.project_name: return message
    # Parse message from Dispatcher
    url = message.get('url')
    if url:
        self.crawl(url, callback=self.index_page)
```

## Reference Examples

### Strategy Template Generator

Generate production-ready strategy templates:

```bash
python scripts/init_strategy_crawler.py <CrawlerName> <StrategyType> <output_path>
```

Available strategies:
- **A** - BrightData V3 (Top-tier anti-scraping)
- **B** - Cookie Pool (Strong account binding)
- **C** - SSR (Proxy breakthrough with regex)
- **D** - API Forward (Pure APIs with task status)
- **E** - Dispatcher (Scheduling and distribution)

### Example Implementations

See [`strategy_examples.md`](assets/examples/strategy_examples.md) for:
- Detailed example scripts for each strategy
- Customization guidelines
- Production deployment checklist

### Reference Index

See [`REFERENCE_INDEX.json`](references/REFERENCE_INDEX.json) for example scripts organized by strategy:
- **A_V3_Dataset**: BrightData V3 examples
- **B_Cookie_Pool**: Cookie pool examples
- **C_SSR_Regex**: SSR regex examples
- **D_API_Forward**: API forwarding examples
- **E_Dispatcher**: Dispatcher examples

See [`reference_map.json`](references/reference_map.json) for detailed strategy breakdown with features.

## Loading Triggers

### Conditional Loading

| Task Type | Must Load | Do NOT Load |
|-----------|-----------|-------------|
| New crawler development | All references | None |
| Refactoring existing crawler | MASTER_SOP.md, STRATEGY_DEEP_DIVE.md | PROJECT_GUIDE.md |
| Database operations | DATABASE_OPS_GUIDE.md | Strategy deep dives |
| Strategy selection | STRATEGY_DEEP_DIVE.md, REFERENCE_INDEX.json | Refactoring SOPs |

### When to Load References

**Load all references when**:
- Starting new crawler project
- Implementing specific anti-scraping strategy
- Refactoring production crawler

**Load specific references when**:
- Database registration: `DATABASE_OPS_GUIDE.md`
- Refactoring: `MASTER_SOP.md`, `STRATEGY_DEEP_DIVE.md`
- Strategy selection: `STRATEGY_DEEP_DIVE.md`, `REFERENCE_INDEX.json`
