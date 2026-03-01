# PySpider Development Toolkit

Production-ready PySpider web crawler development toolkit with enterprise-grade patterns and SOPs.

## Features

- **Dual-Mode Workflows**: New project development and refactoring/debug modes
- **Strategy Patterns (A-E)**: BrightData V3, Cookie pools, SSR parsing, API forwarding, Dispatchers
- **Strict Engineering Redlines**: Zero-field-loss principles, exception management, repository hygiene
- **Automation Scripts**: Database registration, project cleanup, crawler generation
- **Production SOPs**: Comprehensive guidelines for enterprise-grade crawler development

## Installation

Copy this plugin to your Claude plugins directory:

```bash
cp -r pyspider-dev ~/.claude/plugins/
```

## Usage

### Skills

#### pyspider-dev
Basic PySpider crawler development with templates and patterns.

**When to use**:
- Creating new PySpider crawlers
- Implementing web scraping tasks
- Handling complex crawling scenarios with proxies and retries

**Key features**:
- Decision tree for template selection
- Core architecture patterns
- Quick reference for essential parameters
- Anti-patterns and common mistakes

#### production-sop
Production-grade SOP with strict engineering redlines and strategy patterns.

**When to use**:
- Creating new crawlers with anti-scraping strategies
- Refactoring existing production crawlers
- Managing database operations for scraping projects
- Implementing BrightData V3, Cookie pools, SSR parsing, API forwarding, or dispatchers

**Key features**:
- Dual-mode workflows (New Project vs Refactor)
- Strategy patterns A-E with detailed examples
- Global engineering redlines
- Database operations guide
- Exception management principles

### Commands

#### /new-crawler
Create a new PySpider crawler with standard/advanced/enterprise templates.

**Usage**:
```bash
/new-crawler MyCrawler ./projects/my_crawler.py
/new-crawler ApiCrawler ./projects/api.py --template=advanced
/new-crawler EnterpriseSpider ./projects/enterprise.py --template=enterprise
```

#### /strategy-crawler
Create a new PySpider crawler with production strategy templates (A-E).

**Usage**:
```bash
/strategy-crawler TikTokCrawler A ./tiktok_crawler.py
/strategy-crawler FacebookCrawler B ./facebook_crawler.py
/strategy-crawler YoutubeCrawler C ./youtube_crawler.py
```

#### /register-db
Register crawler configuration to MongoDB ScrapingMongoQuery collection.

**Usage**:
```bash
/register-db '{"name":"TikTokCrawler","table":"tiktok","mapping":{"标题":"$title","链接":"$url"}}'
```

#### /delete-project
Delete crawler from MongoDB projectdb and clean up files.

**Usage**:
```bash
/delete-project TikTokCrawler
```

## Quick Start

### Create a New Crawler

**Option 1: Basic Templates (Standard/Advanced/Enterprise)**
1. Load `pyspider-dev` skill
2. Use the decision tree to select appropriate template
3. Generate code using `scripts/init_crawler.py`
4. Sync to repository using `sync-spider` skill

**Option 2: Production Strategy Templates (A-E)**
1. Load `production-sop` skill
2. Select strategy based on target website (A-E)
3. Generate code using `scripts/init_strategy_crawler.py`
4. Customize and test
5. Register to database and sync to repository

### Refactor Existing Crawler

1. Load the `production-sop` skill
2. Follow the Refactor & Debug mode guidelines
3. Observe Shadow Preservation Principle (zero field loss)
4. Maintain contract lock (headers, result keys)

## Directory Structure

```
pyspider-dev/
├── plugin.json              # Plugin manifest
├── README.md               # This file
├── agents/
│   └── spider-generator.md # Agent for generating spiders
├── skills/
│   ├── pyspider-dev/       # Basic development skill
│   ├── production-sop/     # Production SOP skill
│   │   ├── SKILL.md        # Main SOP documentation
│   │   ├── references/     # Detailed guides and examples
│   │   ├── scripts/        # Automation tools
│   │   │   ├── init_strategy_crawler.py  # Strategy template generator
│   │   │   ├── register_business.py      # Database registration
│   │   │   └── delete_project.py        # Project cleanup
│   │   └── assets/
│   │       └── examples/   # Strategy examples and guides
│   └── sync-spider/        # Spider synchronization skill
├── scripts/
│   └── init_crawler.py     # Crawler initialization script
└── references/
    └── api_reference.md    # Detailed API reference
```

## Scripts

### init_crawler.py
Generate new PySpider crawler templates:

```bash
python scripts/init_crawler.py MyCrawler ./projects/my_crawler.py --template=standard
python scripts/init_crawler.py ApiCrawler ./projects/api.py --template=advanced
python scripts/init_crawler.py EnterpriseSpider ./projects/enterprise.py --template=enterprise
```

### Database Operations

**Register business config**:
```bash
# Set environment variables (optional)
export MONGO_URI='mongodb://user:pass@host:port/?tls=false'
export MONGO_DB='feishudb'
export MONGO_COLLECTION='ScrapingMongoQuery'

# Register business config
python3 skills/production-sop/scripts/register_business.py '<JSON_CONFIG>'
```

**Delete project from database**:
```bash
python3 skills/production-sop/scripts/delete_project.py [project_name]
```

### Strategy Template Generator

Generate production-ready strategy templates:
```bash
# Strategy A (BrightData V3)
python skills/production-sop/scripts/init_strategy_crawler.py TikTokCrawler A ./tiktok_crawler.py

# Strategy B (Cookie Pool)
python skills/production-sop/scripts/init_strategy_crawler.py FacebookCrawler B ./facebook_crawler.py

# Strategy C (SSR)
python skills/production-sop/scripts/init_strategy_crawler.py YoutubeCrawler C ./youtube_crawler.py

# Strategy D (API Forward)
python skills/production-sop/scripts/init_strategy_crawler.py DifyCrawler D ./dify_crawler.py

# Strategy E (Dispatcher)
python skills/production-sop/scripts/init_strategy_crawler.py MainDispatch E ./main_dispatch.py
```

## Strategy Patterns

| Strategy | Description | Use Case |
|----------|-------------|----------|
| A (BrightData V3) | Top-tier anti-scraping with pure request protocol | Heavy anti-scraping sites |
| B (Cookie Pool) | Strong account binding with cookie pools | Facebook, Reddit, Mjjl |
| C (SSR) | Proxy breakthrough with regex extraction | Youtube, Amazon, Twitter |
| D (API Forward) | Pure APIs with task status management | Internal APIs, AI forwarding |
| E (Dispatcher) | Scheduling and distribution | Task routing, fanout |

## Engineering Redlines

### Critical Rules
- Exception must be red (use `raise Exception`, not silent returns)
- Three-in-one sync: Script + Git + Database
- Never modify `name` field in database config
- Repository hygiene: Git commits only `.py` files

### Refactoring Redlines
- Zero field loss principle
- Shadow preservation (never remove browser fingerprints)
- Transparent auditing (explain simplifications)

## License

MIT

## Contributing

Follow the [skill-creator](https://github.com/Within-7/minto-plugin-tools) guidelines for contributing to this plugin.
