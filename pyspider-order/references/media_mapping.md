# Media Type Mapping

Complete mapping between natural language, Feishu media types, PySpider projects, and message fields.

## Social Media Platforms

| Feishu Media Type | PySpider Project | Message Field | User ID |
|-------------------|------------------|---------------|---------|
| Reddit 关键词下的帖子 | ScrapingRedditByKeyword_api | keyword | ou_a45583a7f2843869b71ff4cc9692cf3d |
| Reddit某群组的所有帖子 | ScrapingRedditAllPostByKeyword_api | keyword | ou_a45583a7f2843869b71ff4cc9692cf3d |
| Instagram 标签下的帖子 | ScrapingInstagramPostsFromTagsSearch | tags | ou_a45583a7f2843869b71ff4cc9692cf3d |
| Instagram 标签下的帖子_补充 | ScrapingInstagramPostsFromTagsSearchByAccount | tags | ou_a45583a7f2843869b71ff4cc9692cf3d |
| TikTok 标签下的帖子 | ScrapingTiktokByKeywordsFromBD | keyword | ou_a45583a7f2843869b71ff4cc9692cf3d |
| TikTok 用户发布的视频数据 | ScrapingTikTokUserProfileProject | url | ou_a45583a7f2843869b71ff4cc9692cf3d |
| Twitter 关键词下的帖子 | ScrapingTwitterPostsByTags | keyword | ou_a45583a7f2843869b71ff4cc9692cf3d |
| Facebook Ads 主页下的广告 | ScrapingFacebookUserDetailByBright | url | ou_a45583a7f2843869b71ff4cc9692cf3d |
| [手动]fb群组人群帖子活跃度 | ScrapingFacebookGroupsByGoogleUrl | keywords | ou_a45583a7f2843869b71ff4cc9692cf3d |
| Youtube 关键词下的视频 | ScrapingYoutubeVideosByKeywordsV001 | keyword | ou_a45583a7f2843869b71ff4cc9692cf3d |

## E-commerce Platforms

| Feishu Media Type | PySpider Project | Message Field | User ID |
|-------------------|------------------|---------------|---------|
| Amazon列表所有产品及评论 | ScrapingAmazonListByKeywords | keywords | ou_a45583a7f2843869b71ff4cc9692cf3d |

## SellerSprite (卖家精灵)

| Feishu Media Type | PySpider Project | Message Field | User ID |
|-------------------|------------------|---------------|---------|
| 卖家精灵的品牌销售额数据 | ScrapingMjjlDispatcherByBrand | brand | ou_a45583a7f2843869b71ff4cc9692cf3d |
| 卖家精灵的卖家销售额数据 | ScrapingMjjlDispatcherBySeller | seller | ou_a45583a7f2843869b71ff4cc9692cf3d |
| 卖家精灵的关键词销售额数据 | ScrapingMjjlDispatcherByKeyword | keyword | ou_a45583a7f2843869b71ff4cc9692cf3d |
| 卖家精灵的全站品牌销售额数据 | ScrapingMjjlDispatcherByBrandAllStation | brand | ou_a45583a7f2843869b71ff4cc9692cf3d |
| 卖家精灵的全站关键词销售额数据 | ScrapingMjjlDispatcherByKeywordAllStation | keyword | ou_a45583a7f2843869b71ff4cc9692cf3d |
| 卖家精灵的类目销售额数据 | ScrapingMjjlDispatcherBynodeIdPath | nodeIdPath | ou_a45583a7f2843869b71ff4cc9692cf3d |

## SEO Tools

| Feishu Media Type | PySpider Project | Message Field | User ID |
|-------------------|------------------|---------------|---------|
| semrush中的外链数据抓取 | BackLink | keyword | ou_a45583a7f2843869b71ff4cc9692cf3d |
| [手动]网站论坛人群帖子活跃度 | ScrapingGoogleIndexTemp | keywords | ou_a45583a7f2843869b71ff4cc9692cf3d |

## Pinterest

| Feishu Media Type | PySpider Project | Message Field | User ID |
|-------------------|------------------|---------------|---------|
| Pinterest 关键词的所有帖子 | ScrapingPinterestPostByKeywords | keyword | ou_a45583a7f2843869b71ff4cc9692cf3d |
| Pinterest 博主的所有帖子 | ScrapingPinterestProfilePosts | keyword | ou_a45583a7f2843869b71ff4cc9692cf3d |

## Consulting Tasks

| Feishu Media Type | PySpider Project | Message Field | User ID |
|-------------------|------------------|---------------|---------|
| 【全案咨询】分词任务 | ScrapingHandlerArticlesUrl | keyword | ou_a45583a7f2843869b71ff4cc9692cf3d |

## Message Field Types

- **keyword** - Single keyword search
- **keywords** - Multiple keywords search  
- **tags** - Hashtag/tag search
- **brand** - Brand name search
- **seller** - Seller ID search
- **url** - URL-based scraping
- **nodeIdPath** - Category path search

## Natural Language Parsing

**Common patterns:**
- "抓[媒体]" → Map to primary media type
- "查[媒体]关键词" → Map to keyword-based task
- "[媒体]标签" → Map to hashtag/tag scraping
- "[媒体]用户" → Map to user-based scraping

**Examples:**
- "抓Reddit" → Reddit 关键词下的帖子 (keyword)
- "Instagram的fashion标签" → Instagram 标签下的帖子 (tags)
- "查Amazon评论" → Amazon列表所有产品及评论 (keywords)
- "卖家精灵品牌数据" → 卖家精灵的品牌销售额数据 (brand)
