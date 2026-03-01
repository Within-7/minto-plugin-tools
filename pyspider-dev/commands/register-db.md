---
description: Register crawler configuration to MongoDB ScrapingMongoQuery collection
args:
  - name: config
    description: JSON configuration string (enclosed in quotes)
    required: true
---

# Register Database

Register crawler configuration to MongoDB ScrapingMongoQuery collection.

## Process

1. **Prepare Configuration**: Create JSON config with required fields

2. **Register to Database**: Use `register_business.py` script

3. **Verify Registration**: Check database for new entry

## Configuration Format

```json
{
  "name": "CrawlerName",
  "table": "scrap_key",
  "mapping": {
    "field1": "$field1",
    "field2": "$field2"
  }
}
```

**Required Fields**:
- `name`: Crawler project name (matches script name)
- `table`: ScrapingMongoQuery match key (scrap_key)
- `mapping`: Field mapping for MongoDB aggregation pipeline

**Optional Fields**:
- `description`: Crawler description
- `strategy`: Strategy type (A-E)
- `created_at`: Creation timestamp

## Examples

```bash
# Simple registration
/register-db '{"name":"TikTokCrawler","table":"tiktok_keywords","mapping":{"title":"$title","url":"$url","likes":"$likes"}}'

# Full configuration
/register-db '{
  "name": "TikTokByKeywords",
  "table": "tiktok_keywords",
  "description": "TikTok keyword scraping with BD V3",
  "strategy": "A",
  "mapping": {
    "标题": "$title",
    "链接": "$url",
    "点赞数": "$likes",
    "评论数": "$comments",
    "发布时间": "$publish_time"
  }
}'
```

## Environment Variables

Optional environment variables for database connection:

```bash
export MONGO_URI='mongodb://user:pass@host:port/?tls=false'
export MONGO_DB='feishudb'
export MONGO_COLLECTION='ScrapingMongoQuery'
```

**Defaults**:
- `MONGO_URI`: Production database URI
- `MONGO_DB`: feishudb
- `MONGO_COLLECTION`: ScrapingMongoQuery

## Pipeline Rules

1. **Match**: Use `$match` to filter by `scrap_key`
   ```json
   {"table": "scrap_key"}
   ```

2. **Project**: Use `$project` to map fields
   ```json
   {"$project": {"标题": "$title", "链接": "$url"}}
   ```

3. **Field Naming**: Use Chinese field names for Excel display

## After Registration

1. **Verify in Database**:
   ```bash
   # Check if entry exists
   mongo feishudb --eval 'db.ScrapingMongoQuery.findOne({name: "CrawlerName"})'
   ```

2. **Test Crawler**: Run crawler to verify data flow

3. **Sync to Repository**: Ensure script is committed and pushed

## Update Existing Configuration

Running `/register-db` with same `table` value will update existing configuration:

```bash
# Update mapping for existing crawler
/register-db '{"name":"TikTokCrawler","table":"tiktok_keywords","mapping":{"标题":"$title","链接":"$url","点赞数":"$likes","收藏数":"$favorites"}}'
```

## Common Issues

**Issue**: Registration fails with connection error
- **Solution**: Check `MONGO_URI` environment variable
- **Solution**: Verify database accessibility

**Issue**: Fields not appearing in Excel
- **Solution**: Ensure field names in `mapping` are in Chinese
- **Solution**: Verify MongoDB aggregation pipeline syntax

**Issue**: Data not flowing to database
- **Solution**: Check crawler `on_message` implementation
- **Solution**: Verify `table` matches crawler's `scrap_key`

## See Also

- `/delete-project` - Remove crawler from database
- `production-sop` skill - Database operations guide
- `DATABASE_OPS_GUIDE.md` - Complete database documentation
