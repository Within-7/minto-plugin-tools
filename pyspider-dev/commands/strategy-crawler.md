---
description: Create a new PySpider crawler with production strategy templates (A-E)
args:
  - name: name
    description: Crawler class name (e.g., TikTokCrawler)
    required: true
  - name: strategy
    description: Strategy type: A (BD V3), B (Cookie), C (SSR), D (API), E (Dispatcher)
    required: true
  - name: output
    description: Output file path (e.g., ./projects/tiktok_crawler.py)
    required: true
---

# Strategy Crawler

Create a new PySpider crawler with production-grade anti-scraping strategies.

## Process

1. **Select Strategy**: Choose based on target website characteristics

2. **Generate Strategy Template**: Use `init_strategy_crawler.py` script

3. **Configure Proxies/Cookies**: Set up required resources

4. **Customize for Target**: Update URLs, endpoints, data extraction

5. **Register to Database**: Use `register_business.py` script

6. **Sync to Repository**: Use `sync-spider` skill

## Strategy Selection

| Strategy | Name | Use Case | Target Sites |
|----------|-------|-----------|--------------|
| A | BrightData V3 | Top-tier anti-scraping | TikTok, Amazon, heavy protection |
| B | Cookie Pool | Strong account binding | Facebook, Reddit, Mjjl |
| C | SSR | Proxy breakthrough + regex | Youtube, Amazon, Twitter |
| D | API Forward | Pure APIs + task status | Dify, internal APIs |
| E | Dispatcher | Scheduling + distribution | Task routing, fanout |

## Examples

```bash
# Strategy A - BrightData V3 (TikTok keyword scraping)
/strategy-crawler TikTokByKeywords A ./tiktok_crawler.py

# Strategy B - Cookie Pool (Facebook ads scraping)
/strategy-crawler FacebookAds B ./facebook_crawler.py

# Strategy C - SSR (Youtube video details)
/strategy-crawler YoutubeVideo C ./youtube_crawler.py

# Strategy D - API Forward (Dify integration)
/strategy-crawler BackLinkToDify D ./dify_crawler.py

# Strategy E - Dispatcher (Main dispatch)
/strategy-crawler MainDispatch E ./main_dispatch.py
```

## Strategy Details

### Strategy A (BrightData V3)
**Features**:
- Three-step state machine (trigger → snapshot → result)
- Pure request protocol
- BD_EMPTY_DATA validation

**Requirements**:
- BrightData API credentials
- Target site URL
- Data extraction logic

### Strategy B (Cookie Pool)
**Features**:
- Forced cookies inheritance
- Cookie pool randomization
- Login wall detection

**Requirements**:
- Cookie pool configuration
- ISP proxy (ispProxy_us_)
- Account credentials

### Strategy C (SSR)
**Features**:
- Residential proxy
- Regex extraction for embedded JSON
- DOM + JSON mixed parsing

**Requirements**:
- Residential proxy (serProxy_us_)
- Regex patterns for data extraction
- Target site structure analysis

### Strategy D (API Forward)
**Features**:
- UUID taskid bypass
- API status polling
- MongoDB task status bits

**Requirements**:
- Datacenter proxy
- API endpoints
- Task status management

### Strategy E (Dispatcher)
**Features**:
- on_message fanout
- send_message task routing
- Multi-project distribution

**Requirements**:
- Target project list
- Task source (database, file, API)
- Routing rules

## After Creation

1. **Configure Resources**:
   - Set up proxy pools (strategies B, C, D)
   - Configure cookie pool (strategy B)
   - Set up API credentials (strategies A, D)

2. **Customize Logic**:
   - Update target URLs/endpoints
   - Implement data extraction
   - Adjust timeout values
   - Add custom error handling

3. **Test Locally**:
   - Test with small data sets
   - Verify proxy connections
   - Check cookie validity (strategy B)
   - Validate API responses (strategies A, D)

4. **Register to Database**:
   ```bash
   python3 skills/production-sop/scripts/register_business.py '<JSON_CONFIG>'
   ```

5. **Sync to Repository**:
   - Use `sync-spider` skill
   - Git commit and push
   - Pyspider webui auto-loads

## See Also

- `/new-crawler` - Create crawler with standard templates
- `production-sop` skill - Complete strategy documentation
- `assets/examples/strategy_examples.md` - Detailed examples
