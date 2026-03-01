# Strategy Examples Reference

This directory contains example scripts demonstrating each strategy pattern (A-E).

## Quick Reference

| Strategy | Example File | Use Case |
|----------|--------------|----------|
| A (BD V3) | `tiktok_bd_v3.py` | TikTok keyword scraping with BrightData V3 |
| B (Cookie) | `facebook_ads.py` | Facebook ads scraping with cookie pool |
| C (SSR) | `youtube_video.py` | YouTube video details with SSR regex |
| D (API) | `dify_forward.py` | Dify API forwarding with task polling |
| E (Dispatcher) | `main_dispatch.py` | Task distribution and routing |

## Strategy A Examples

### TikTok Keyword Scraping (BD V3)
```bash
python init_strategy_crawler.py TikTokByKeywords A ./tiktok_bd_v3.py
```

Key features:
- Three-step state machine (trigger → snapshot → result)
- Pure request protocol
- BD_EMPTY_DATA validation

### Amazon Store Reviews (BD V3)
```bash
python init_strategy_crawler.py AmazonStoreReviews A ./amazon_bd_v3.py
```

Key features:
- MarketplaceID support
- Exception-driven FAILED status

## Strategy B Examples

### Mjjl List Scraping (Cookie Pool)
```bash
python init_strategy_crawler.py MjjlList B ./mjjl_list.py
```

Key features:
- Forced cookies inheritance
- Cookie pool randomization
- Login wall check

### Facebook Ads by Page ID (Cookie Pool)
```bash
python init_strategy_crawler.py FacebookAds B ./facebook_ads.py
```

Key features:
- Cookie pool management
- Account binding

## Strategy C Examples

### YouTube Video Details (SSR)
```bash
python init_strategy_crawler.py YoutubeVideo C ./youtube_video.py
```

Key features:
- `re.search('ytInitialData')` pattern
- Residential proxy (serProxy_us_)
- Regex extraction for embedded JSON

### Twitter Posts by Tags (SSR)
```bash
python init_strategy_crawler.py TwitterPosts C ./twitter_posts.py
```

Key features:
- SSR regex extraction
- Residential proxy

## Strategy D Examples

### BackLink to Dify (API Forward)
```bash
python init_strategy_crawler.py BackLinkToDify D ./dify_forward.py
```

Key features:
- UUID taskid bypass
- Dify status polling
- MongoDB integration

### Mjjl Dispatcher by Brand (API Forward)
```bash
python init_strategy_crawler.py MjjlDispatcher D ./mjjl_dispatcher.py
```

Key features:
- API forwarding
- Task status management

## Strategy E Examples

### Job Trigger (Dispatcher)
```bash
python init_strategy_crawler.py JobTrigger E ./job_trigger.py
```

Key features:
- on_message fanout
- send_message task routing

### Main Dispatch (Dispatcher)
```bash
python init_strategy_crawler.py MainDispatch E ./main_dispatch.py
```

Key features:
- Task distribution
- Multi-project routing

## Generating Strategy Templates

Use the strategy template generator:

```bash
# Strategy A (BrightData V3)
python skills/production-sop/scripts/init_strategy_crawler.py MyCrawler A ./my_crawler.py

# Strategy B (Cookie Pool)
python skills/production-sop/scripts/init_strategy_crawler.py MyCrawler B ./my_crawler.py

# Strategy C (SSR)
python skills/production-sop/scripts/init_strategy_crawler.py MyCrawler C ./my_crawler.py

# Strategy D (API Forward)
python skills/production-sop/scripts/init_strategy_crawler.py MyCrawler D ./my_crawler.py

# Strategy E (Dispatcher)
python skills/production-sop/scripts/init_strategy_crawler.py MyCrawler E ./my_crawler.py
```

## Customizing Templates

After generating a template, customize it for your specific use case:

1. **Update URLs**: Replace example URLs with actual target URLs
2. **Configure Proxies**: Set up proxy pools for strategies B, C, D
3. **Set Up Cookies**: Configure cookie pools for strategy B
4. **Adjust Timeouts**: Modify timeout values based on target site response times
5. **Add Custom Logic**: Implement specific data extraction logic in callback functions

## Testing Strategy Templates

Before deploying to production:

1. Test with small data sets
2. Verify proxy connections
3. Check cookie validity (for strategy B)
4. Validate API responses (for strategies A, D)
5. Test error handling and retry logic
6. Monitor FAILED status generation

## Production Deployment Checklist

- [ ] Strategy template generated correctly
- [ ] Proxies configured and tested
- [ ] Cookies configured (for strategy B)
- [ ] API endpoints verified (for strategies A, D)
- [ ] Error handling tested
- [ ] Database registration completed
- [ ] Git commit and push completed
- [ ] Pyspider webui loaded successfully

For detailed strategy patterns and rules, see [`STRATEGY_DEEP_DIVE.md`](../references/STRATEGY_DEEP_DIVE.md).
