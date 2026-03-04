---
name: minto-slides
description: 演示文稿页面生成器。支持生成消费者洞察散点图(第24页)、用户画像(第25-29页)、行业结论卡片(第49-50页)。关键词：演示文稿、幻灯片、散点图、用户画像、行业结论、消费者洞察。
---

# Minto Slides Skill

演示文稿页面生成器，支持生成第24-29页（消费者洞察）和第49-50页（行业结论）。

## 依赖安装

```bash
pip install playwright pillow
python -m playwright install chromium
```

## 输出目录

默认输出到当前工作目录下的 `output/` 文件夹，用户可自定义。

---

## 功能模块

| 模块 | 页码 | 类型 | 说明 |
|------|------|------|------|
| 消费者洞察 | 24 | 散点图 | 用户关注度分析（市场分 vs 需求分） |
| 消费者洞察 | 25-29 | 用户画像 | 优选用户展示（文字 + Instagram截图） |
| 行业结论 | 49-50 | 卡片布局 | 12个行业结论卡片，每页6个 |

---

## 执行机制

**重要：每次调用只生成一页，需要再次调用才继续下一页**

```
# 消费者洞察模块
第1次调用 → 生成第24页（散点图）
第2次调用 → 生成第25页（用户画像1）
...
第6次调用 → 生成第29页（用户画像5）

# 行业结论模块
第1次调用 → 生成第49页（卡片1-6）
第2次调用 → 生成第50页（卡片7-12）
```

---

## SOP - 第24页：散点图生成

### 输入数据格式

**格式1：CSV/TSV**
```
人群特征,市场得分,需求得分
摄影师,75,88
tennis,10,3.3
licensed cosmetologist,1.33,10
```

**格式2：JSON**
```json
[
  {"name": "摄影师", "marketScore": 75, "demandScore": 88},
  {"name": "tennis", "marketScore": 10, "demandScore": 3.3}
]
```

### 处理流程

**Step 1: 数据解析**
- 读取人群数据
- 验证必需字段：人群名称、市场得分、需求得分
- 归一化分数到0-100范围

**Step 2: 维度自动识别**

根据人群名称自动分类：

| 维度 | 识别规则 | 颜色 |
|------|---------|------|
| 职业 | job, 职业, 师, 家, 员, technician, cosmetologist, writer | #e74c3c |
| 爱好/运动 | sport, 运动, 球, 舞, 爬, yoga, tennis, hiking, swimming, climbing | #3498db |
| 身体状况 | 疾病, 症状, disease, onycholysis, paronychia, cancer | #9b59b6 |
| 身份特征 | mother, parent, children, kids, single, working | #f39c12 |
| 生活方式 | vegetarian, vegan, smoker, meditation, fitness | #1abc9c |
| 其他 | 未匹配到的 | #95a5a6 |

**Step 3: 数据分析**
- 高市场得分人群（TOP 5-10）
- 高需求得分人群（TOP 5-10）
- 各维度分布统计
- 生成数据总结

**Step 4: 模板渲染**
使用 `templates/scatter_chart.html` 模板

**Step 5: 输出**
- 文件：`output/24_user_attention.html`
- 同时生成数据状态文件供后续页面使用

---

## SOP - 第25-29页：用户画像生成

### 前置条件
- 第24页已生成
- 存在高得分人群数据

### 处理流程

**Step 1: 选择目标人群**
从第24页数据中选择高得分人群，记录当前进度

**Step 2: 生成文字分析**

使用大模型生成三类内容，**要求文字充实撑满左侧区域**：

| 模块 | 内容要求 | 字数要求 |
|------|---------|---------|
| 人群规模 | 全球人数、占比、细分群体、地区分布、增长率、预测 | 400-600字 |
| 人群年龄水平 | 年龄分层、各年龄段占比、性别特征、不同活动差异 | 400-600字 |
| 人群消费水平和习惯 | 年均消费、购买渠道占比、决策因素、消费特征、趋势 | 400-600字 |

**Step 3: Instagram截图**

调用截图脚本：
```bash
python3 scripts/instagram_screenshot.py "人群名称"
```

**Step 4: 模板渲染**
使用 `templates/user_profile.html` 模板

**Step 5: 输出**
- HTML：`output/25_user_profile_1.html`
- 截图：`output/instagram_人群名称.png`

---

## SOP - 第49-50页：行业结论生成

### 输入格式

**自由文本格式**（AI自动解析和扩展）

用户可提供：
- 行业描述段落
- 关键点列表
- 部分主题 + 部分内容
- 甚至只是几个关键词

示例：
```
户外露营装备行业是一个专注于露营相关装备的研发、制造和销售的行业。
核心产品包括帐篷、睡袋、照明设备、炊具等。
行业发展从军用转民用开始，经历了专业化、大众化和智能化三个阶段。
2024年全球市场规模约为968亿美元...
```

### 处理流程

**Step 1: 文本分析**
- 读取用户提供的自由文本
- 识别关键主题和内容要点
- 分析内容结构和逻辑关系

**Step 2: 主题提取/生成**

根据文本内容，AI自动提取或生成12个主题卡片：

| 卡片编号 | 建议主题方向 |
|---------|-------------|
| 01-02 | 行业定义、发展历程 |
| 03-04 | 市场规模、区域分布 |
| 05-06 | 产品分布、重点产品 |
| 07-08 | 驱动因素、限制因素 |
| 09-10 | 热点趋势、竞争格局 |
| 11-12 | 品牌关注、用户关注 |

**Step 3: 内容扩展**

如果用户提供的内容不足12个卡片，LLM自动扩展：
- 根据行业知识补充缺失内容
- 确保每个卡片有100-150字的内容
- 关键数据用 `<strong>` 标签加粗

**Step 4: 颜色分配**

6种颜色主题循环分配：

| 主题色 | HEX值 | 卡片编号 |
|--------|-------|---------|
| blue | #1E88E5 | 01, 07 |
| orange | #FF7043 | 02, 08 |
| yellow | #FBC02D | 03, 09 |
| gold | #F9A825 | 04, 10 |
| red | #FF5252 | 05, 11 |
| cyan | #03A9F4 | 06, 12 |

**Step 5: 模板渲染**
使用 `templates/industry_conclusion.html` 模板

模板变量：
| 变量 | 说明 |
|------|------|
| `{{sectionTitle}}` | 部分标题，如"第九部分：行业结论" |
| `{{logoPath}}` | logo文件路径 |
| `{{card1.number}}` | 卡片编号（01-06 或 07-12） |
| `{{card1.title}}` | 卡片标题 |
| `{{card1.content}}` | 卡片内容（可含HTML标签） |
| `{{card1.theme}}` | 颜色主题（blue/orange/yellow/gold/red/cyan） |

**Step 6: 输出**
- 第49页：`output/49_industry_conclusion_1.html`（卡片1-6）
- 第50页：`output/50_industry_conclusion_2.html`（卡片7-12）

### 调用示例

```
用户：/minto-slides 生成行业结论页面，主题是户外露营装备，内容如下：
[自由文本...]

→ AI分析文本 → 提取/生成12个主题 → 扩展内容 → 分配颜色
→ 输出：output/49_industry_conclusion_1.html

用户：/minto-slides 继续生成第50页

→ 使用已生成的卡片7-12数据 → 渲染模板
→ 输出：output/50_industry_conclusion_2.html
```

---

## 中文→英文Hashtag完整映射

```python
KEYWORD_MAPPING = {
    # 水上活动
    "水上活动": "watersports",
    "水上/水边活动爱好者": "watersports",
    "潜水": "diving",
    "冲浪": "surfing",
    "钓鱼": "fishing",
    "皮划艇": "kayaking",
    "游泳": "swimming",

    # 自然探索
    "自然探索": "naturelover",
    "自然探索爱好者": "naturelover",
    "徒步": "hiking",
    "露营": "camping",
    "登山": "mountaineering",
    "野生动物观察": "wildlife",

    # 极端探险
    "极端探险": "extremesports",
    "极端探险爱好者": "extremesports",
    "攀岩": "rockclimbing",
    "溪降": "canyoning",

    # 旅行
    "长途旅行": "traveler",
    "长途/四季旅行爱好者": "traveler",
    "冬季露营": "wintercamping",
    "滑雪": "skiing",

    # 家庭
    "家庭旅行": "familytravel",
    "团体/家庭旅行爱好者": "familytravel",
    "带宠人士": "petfriendly",

    # 美妆
    "美甲": "nailart",
    "婚庆美甲": "bridalnails",
}
```

---

## 文件结构

```
minto-slides/
├── .claude-plugin/
│   └── plugin.json                # 插件清单
├── skills/
│   └── minto-slides/
│       └── SKILL.md               # 本文件
├── templates/
│   ├── scatter_chart.html         # 第24页模板（散点图）
│   ├── user_profile.html          # 第25-29页模板（用户画像）
│   └── industry_conclusion.html   # 第49-50页模板（行业结论）
├── assets/
│   └── logo.png                   # 默认Logo
├── scripts/
│   └── instagram_screenshot.py    # Instagram截图脚本
├── examples/
│   ├── example_scatter.json       # 散点图示例数据
│   └── example_conclusion.txt     # 行业结论文本示例
├── requirements.txt               # Python依赖
└── README.md                      # 使用说明
```

---

## Logo配置

默认使用 `assets/logo.png`

调用时可指定其他logo：
```
用户：生成第24页，logo用 /path/to/my-logo.png
```

---

## 注意事项

1. **分页执行**：每次只生成一页，避免一次性生成过多
2. **手动配合**：截图需要用户手动点击Instagram用户和选择截图窗口
3. **数据一致性**：25-29页的人群需从24页数据中选取
4. **文字充实**：用户画像页面的文字要足够详细，撑满左侧区域
5. **进度记录**：记录当前生成到第几页，下次继续
6. **AI扩展**：行业结论页面支持AI自动扩展内容到12个卡片

---

## 版本

- v2.0.0 - 重命名为 minto-slides，新增第49-50页行业结论生成
- v1.0.0 - 初始版本，支持第24-29页生成
