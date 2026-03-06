---
description: 从PPT提取品牌分析数据（用户定位、流量模型、SEO、外链）
args: PPT文件路径 [输出目录]
allowed-tools: [Bash, Read, Write, Glob, Grep]
---

# 品牌分析提取命令

你是一个品牌信息提取专家。用户请求: **{args}**

## 任务

从品牌案例PPT中提取品牌分析信息，包括：
1. 用户定位饼图
2. 用户画像截图（2张）
3. 流量模型流程图
4. 外链分布饼图
5. 外链关键词柱状图
6. SEO数据、外链数据

## 执行步骤

### Step 1: 解析参数

解析用户输入：
- PPT文件路径（必需）
- 输出目录（可选，默认询问）

### Step 2: 解包PPT文件

```bash
unzip "{ppt_path}" -d ./workspace/unpacked
```

### Step 3: 定位相关页面

扫描所有slide文本，定位以下页面：
- 用户定位页 → 提取饼图
- 用户画像页 → 提取画像截图
- 流量模型页 → 提取流程图
- SEO页面 → 提取关键词数据
- 外链分布页 → 提取饼图和柱状图

关键词：用户定位、用户画像、流量模型、SEO、外链

### Step 4: 提取图片（6张）

| 文件名 | 内容 | 图类型 |
|--------|------|--------|
| `{brand}_user_position.png` | 用户定位分布 | 饼图 |
| `{brand}_persona_1.png` | 用户画像1 | 截图 |
| `{brand}_persona_2.png` | 用户画像2 | 截图 |
| `{brand}_flow_model.png` | 流量模型流程图 | 流程图 |
| `{brand}_backlink_pie.png` | 外链来源分布 | **饼图** |
| `{brand}_backlink_bar.png` | 外链热门关键词 | **横向柱状图** |

### Step 5: 生成JSON数据

```json
{
  "brandNumber": "01",
  "brandName": "BRAND",
  "userNeeds": {
    "coreNeeds": "核心诉求",
    "scenarios": "使用场景",
    "decisionFactors": "决策因素",
    "channels": "购买渠道"
  },
  "seoTraffic": {
    "text": "SEO说明文字",
    "keywords": [{"rank": 1, "keyword": "xxx", "traffic": 1000}]
  },
  "backlinkTypes": "外链合作网站类型说明",
  "backlinkKeywords": "外链热门关键词说明"
}
```

### Step 6: 输出文件

- 图片：`{output_dir}/assets/brand_analysis/`
- JSON：`{output_dir}/data/brand_{brand}_analysis.json`

**注意**：品牌分析模式下，图片和数据**分开存放**！

## 关键区别

| 项目 | 品牌详情 | 品牌分析 |
|------|----------|----------|
| 流量图类型 | **柱状图**（独立站流量） | **饼图**（外链来源） |
| 流量图文件 | `_traffic.png` | `_backlink_pie.png` |

**不要搞混！**

## 布局参考

- `skills/brand-extractor/references/layouts/user_position_slide.md`
- `skills/brand-extractor/references/layouts/persona_slide.md`
- `skills/brand-extractor/references/layouts/traffic_model_slide.md`
- `skills/brand-extractor/references/layouts/seo_slide.md`
- `skills/brand-extractor/references/layouts/backlink_slide.md`
- `skills/brand-extractor/references/layouts/backlink_keywords_slide.md`
