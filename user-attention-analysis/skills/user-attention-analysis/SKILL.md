---
name: user-attention-analysis
description: 消费者洞察页面生成器。当用户需要生成用户关注度分析、人群画像、散点图、消费者洞察页面时使用。支持生成第24页（散点图）和第25-29页（用户画像）。关键词：散点图、用户画像、市场得分、需求得分、Instagram截图、消费者洞察。
---

# User Attention Analysis Skill

消费者洞察页面生成器，支持生成第24-29页内容。

## 依赖安装

```bash
pip install playwright pillow
python -m playwright install chromium
```

## 输出目录

默认输出到当前工作目录下的 `output/` 文件夹，用户可自定义。

---

## 执行机制

**重要：每次调用只生成一页，需要再次调用才继续下一页**

```
第1次调用 → 生成第24页（散点图）
第2次调用 → 生成第25页（用户画像1）
第3次调用 → 生成第26页（用户画像2）
第4次调用 → 生成第27页（用户画像3）
第5次调用 → 生成第28页（用户画像4）
第6次调用 → 生成第29页（用户画像5）
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

模板变量：
| 变量 | 说明 |
|------|------|
| `{{section}}` | 部分标题，如"第七部分：消费者洞察" |
| `{{subsection}}` | 小节标题，如"7.1 用户关注度" |
| `{{topic}}` | 主题名称，如"户外露营装备" |
| `{{chartConfigJson}}` | 图表配置JSON对象 |
| `{{logoPath}}` | logo文件路径 |
| `{{highMarketGroups}}` | 高市场得分人群列表 |
| `{{highDemandGroups}}` | 高需求得分人群列表 |
| `{{summaryDescription}}` | 数据总结描述 |
| `{{dataSource}}` | 数据来源 |

**Step 5: 输出**
- 文件：`output/24_user_attention.html`
- 同时生成数据状态文件供后续页面使用

### 图表配置JSON示例

```javascript
var chartConfig = {
    title: {
        section: "第七部分：消费者洞察",
        subsection: "7.1 用户关注度"
    },
    topic: "户外露营装备",
    dataSource: "任小姐出海战略咨询自研心智洞察引擎系统",
    dimensions: {
        "职业": {
            color: "#e74c3c",
            data: [
                {name: "摄影师", demandScore: 75, marketScore: 88, symbolSize: 28},
                {name: "记者", demandScore: 68, marketScore: 85, symbolSize: 26}
            ]
        },
        "爱好/运动": {
            color: "#3498db",
            data: [
                {name: "tennis", demandScore: 3.3, marketScore: 10, symbolSize: 32}
            ]
        }
    },
    summary: {
        highMarket: ["tennis", "yoga", "travel"],
        highDemand: ["licensed cosmetologist", "fashion writer"],
        description: "该图展示户外露营装备市场中关注度较高的用户画像"
    }
};
```

---

## SOP - 第25-29页：用户画像生成

### 前置条件
- 第24页已生成
- 存在高得分人群数据

### 处理流程

**Step 1: 选择目标人群**
从第24页数据中选择高得分人群：
- 优先选择高市场得分人群
- 其次选择高需求得分人群
- 确保每页展示不同人群
- 记录当前进度，下次继续

**Step 2: 生成文字分析**

使用大模型生成三类内容，**要求文字充实撑满左侧区域**：

| 模块 | 内容要求 | 字数要求 |
|------|---------|---------|
| 人群规模 | 全球人数、占比、细分群体、地区分布、增长率、预测 | 400-600字 |
| 人群年龄水平 | 年龄分层、各年龄段占比、性别特征、不同活动差异 | 400-600字 |
| 人群消费水平和习惯 | 年均消费、购买渠道占比、决策因素、消费特征、趋势 | 400-600字 |

**文字要求：**
- 数据要具体，包含百分比、金额等
- 关键数据用 `<strong>` 标签加粗
- 内容要详实，不能过于简略

**Step 3: Instagram截图**

调用截图脚本：
```bash
python3 scripts/instagram_screenshot.py "人群名称"
```

脚本流程：
1. 转换中文→英文hashtag
2. 打开Instagram搜索该tag
3. 等待9秒让用户点击一个KOL用户
4. 弹出截图工具，用户点击窗口完成截图

**Step 4: 模板渲染**
使用 `templates/user_profile.html` 模板

模板变量：
| 变量 | 说明 |
|------|------|
| `{{section}}` | 部分标题 |
| `{{subsection}}` | 小节标题，如"7.2 优选用户展示（1）" |
| `{{userTypeTitle}}` | 人群类型标题 |
| `{{populationContent}}` | 人群规模内容 |
| `{{ageContent}}` | 年龄水平内容 |
| `{{consumptionContent}}` | 消费习惯内容 |
| `{{logoPath}}` | logo路径 |

**Step 5: 输出**
- HTML：`output/25_user_profile_1.html`
- 截图：`output/instagram_人群名称.png`

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
user-attention-analysis/
├── .claude-plugin/
│   └── plugin.json                # 插件清单
├── skills/
│   └── user-attention-analysis/
│       └── SKILL.md               # 本文件
├── templates/
│   ├── scatter_chart.html         # 第24页模板
│   └── user_profile.html          # 第25-29页模板
├── assets/
│   └── logo.png                   # 默认Logo
├── scripts/
│   └── instagram_screenshot.py    # Instagram截图脚本
├── examples/
│   └── example_data.json          # 示例数据
├── requirements.txt               # Python依赖
└── README.md                      # 使用说明
```

---

## 调用示例

```
用户：/user-attention-analysis 生成第24页，主题是户外露营装备，数据如下：
人群特征,市场得分,需求得分
摄影师,75,88
tennis,10,3.3
...

→ 解析数据 → 识别维度 → 生成散点图
→ 输出：output/24_user_attention.html

用户：/user-attention-analysis 继续生成第25页

→ 从24页数据选高得分人群（如：水上活动）
→ 生成文字分析
→ 调用截图脚本（等待用户手动操作）
→ 输出：output/25_user_profile_1.html + instagram_水上活动.png

用户：/user-attention-analysis 继续生成第26页

→ 选下一个高得分人群 → ...
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

---

## 版本

- v1.0.0 - 初始版本，支持第24-29页生成
