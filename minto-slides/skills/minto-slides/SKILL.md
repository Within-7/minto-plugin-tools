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

**注意**：如果不需要自动截图功能，可以跳过 playwright 安装。

---

## 项目目录结构

**重要**：在当前项目目录下创建以下结构：

```
当前项目目录/
├── assets/
│   ├── logo.png                     # Logo文件（必需）
│   └── profiles/                    # 25-29页用户画像截图
│       ├── 水上活动.png
│       ├── 自然探索.png
│       ├── 极端探险.png
│       ├── 长途旅行.png
│       └── 家庭旅行.png
├── slides/                          # 生成的HTML文件
│   ├── 24_user_attention.html
│   ├── 25_user_profile_1.html
│   ├── ...
│   ├── 49_industry_conclusion_1.html
│   └── 50_industry_conclusion_2.html
└── .minto-state.json                # 状态文件（自动生成）
```

---

## 功能模块

| 模块 | 页码 | 类型 | 说明 |
|------|------|------|------|
| 消费者洞察 | 24 | 散点图 | 用户关注度分析（市场分 vs 需求分） |
| 消费者洞察 | 25-29 | 用户画像 | 优选用户展示（文字 + 截图） |
| 行业结论 | 49-50 | 卡片布局 | 12个行业结论卡片，每页6个 |

---

## 执行机制

```
# 消费者洞察模块
第24页：单次调用生成
第25-29页：单次调用批量生成5页（需提前准备截图）

# 行业结论模块
第49-50页：单次调用批量生成2页
```

---

## 通用步骤：Logo处理

**每次生成HTML前必须执行**：

1. 检查当前项目目录是否存在 `assets/logo.png`
2. 如果不存在：
   - 从插件目录复制默认logo：`/Users/mac/Desktop/minto-plugin-tools/minto-slides/assets/logo.png`
   - 复制到：`{当前项目目录}/assets/logo.png`
3. HTML中的logo路径统一使用：`assets/logo.png`

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

**Step 1: Logo检查与复制**
- 检查 `assets/logo.png` 是否存在
- 不存在则从插件目录复制

**Step 2: 数据解析**
- 读取人群数据
- 验证必需字段：人群名称、市场得分、需求得分
- 归一化分数到0-100范围

**Step 3: 维度自动识别**

根据人群名称自动分类：

| 维度 | 识别规则 | 颜色 |
|------|---------|------|
| 职业 | job, 职业, 师, 家, 员, technician, cosmetologist, writer | #e74c3c |
| 爱好/运动 | sport, 运动, 球, 舞, 爬, yoga, tennis, hiking, swimming, climbing | #3498db |
| 身体状况 | 疾病, 症状, disease, onycholysis, paronychia, cancer | #9b59b6 |
| 身份特征 | mother, parent, children, kids, single, working | #f39c12 |
| 生活方式 | vegetarian, vegan, smoker, meditation, fitness | #1abc9c |
| 其他 | 未匹配到的 | #95a5a6 |

**Step 4: 数据分析**
- 高市场得分人群（TOP 5-10）
- 高需求得分人群（TOP 5-10）
- 各维度分布统计
- 生成数据总结

**Step 5: 模板渲染**
- 使用 `templates/scatter_chart.html` 模板
- Logo路径：`assets/logo.png`

**Step 6: 输出**
- 文件：`slides/24_user_attention.html`
- 状态文件：`.minto-state.json`（记录人群数据供后续使用）

---

## SOP - 第25-29页：用户画像批量生成

### 前置条件检查

**Step 1: 检查图片文件**

生成前必须检查 `assets/profiles/` 目录：

```
需要检查的图片（根据24页数据选取的人群）：
- assets/profiles/水上活动.png
- assets/profiles/自然探索.png
- assets/profiles/极端探险.png
- assets/profiles/长途旅行.png
- assets/profiles/家庭旅行.png
```

**如果图片缺失**：

1. 输出提示信息：
```
⚠️ 检测到以下图片缺失：
- assets/profiles/xxx.png
- assets/profiles/xxx.png

请先上传图片，格式要求：
- 尺寸：480px × 850-900px（推荐）
- 格式：PNG 或 JPG
- 存放位置：assets/profiles/
- 文件命名：{人群名称}.png

上传完成后回复"继续"。
```

2. 等待用户确认后再继续

### 图片格式要求

| 项目 | 要求 |
|------|------|
| 宽度 | 480px（固定） |
| 高度 | 850-900px（推荐） |
| 格式 | PNG 或 JPG |
| 命名 | `{人群名称}.png`（如：水上活动.png） |
| 位置 | `assets/profiles/` |

### 处理流程

**Step 2: Logo检查与复制**
- 确保 `assets/logo.png` 存在

**Step 3: 选择目标人群**
- 从第24页数据（`.minto-state.json`）中选取5个高得分人群
- 优先选择高市场得分人群

**Step 4: 批量生成文字分析**

为每个选中的5个人群生成三类内容：

| 模块 | 内容要求 | 字数要求 |
|------|---------|---------|
| 人群规模 | 全球人数、占比、细分群体、地区分布、增长率、预测 | 200-300字 |
| 人群年龄水平 | 年龄分层、各年龄段占比、性别特征、不同活动差异 | 200-300字 |
| 人群消费水平和习惯 | 年均消费、购买渠道占比、决策因素、消费特征、趋势 | 200-300字 |

**文字要求**：
- 数据要具体，包含百分比、金额等
- 关键数据用 `<strong>` 标签加粗
- 内容要详实，不能过于简略

**Step 5: 批量渲染模板**

使用 `templates/user_profile.html` 模板，一次性生成5页：

| 输出文件 | 人群 | 图片路径 |
|---------|------|---------|
| `slides/25_user_profile_1.html` | 第1个人群 | `assets/profiles/{人群名}.png` |
| `slides/26_user_profile_2.html` | 第2个人群 | `assets/profiles/{人群名}.png` |
| `slides/27_user_profile_3.html` | 第3个人群 | `assets/profiles/{人群名}.png` |
| `slides/28_user_profile_4.html` | 第4个人群 | `assets/profiles/{人群名}.png` |
| `slides/29_user_profile_5.html` | 第5个人群 | `assets/profiles/{人群名}.png` |

**Step 6: 输出确认**

```
✅ slides/25_user_profile_1.html（水上活动）
✅ slides/26_user_profile_2.html（自然探索）
✅ slides/27_user_profile_3.html（极端探险）
✅ slides/28_user_profile_4.html（长途旅行）
✅ slides/29_user_profile_5.html（家庭旅行）

批量生成完成！
```

### 模板变量

| 变量 | 说明 |
|------|------|
| `{{section}}` | 部分标题 |
| `{{subsection}}` | 小节标题，如"7.2 优选用户展示（1）" |
| `{{userTypeTitle}}` | 人群类型标题 |
| `{{populationContent}}` | 人群规模内容 |
| `{{ageContent}}` | 年龄水平内容 |
| `{{consumptionContent}}` | 消费习惯内容 |
| `{{logoPath}}` | logo路径：`assets/logo.png` |
| `{{profileImagePath}}` | 截图路径：`assets/profiles/{人群名}.png` |

---

## SOP - 第49-50页：行业结论批量生成

### 输入格式

**自由文本格式**（AI自动解析和扩展）

用户可提供：
- 行业描述段落
- 关键点列表
- 部分主题 + 部分内容
- 甚至只是几个关键词

### 处理流程

**Step 1: Logo检查与复制**
- 确保 `assets/logo.png` 存在

**Step 2: 文本分析**
- 读取用户提供的自由文本
- 识别关键主题和内容要点

**Step 3: 主题提取/生成**

AI自动提取或生成12个主题卡片：

| 卡片编号 | 建议主题方向 |
|---------|-------------|
| 01-02 | 行业定义、发展历程 |
| 03-04 | 市场规模、区域分布 |
| 05-06 | 产品分布、重点产品 |
| 07-08 | 驱动因素、限制因素 |
| 09-10 | 热点趋势、竞争格局 |
| 11-12 | 品牌关注、用户关注 |

**Step 4: 内容扩展**

- 确保每个卡片有100-150字的内容
- 关键数据用 `<strong>` 标签加粗

**Step 5: 颜色分配**

6种颜色主题循环分配：

| 主题色 | 卡片编号 |
|--------|---------|
| blue | 01, 07 |
| orange | 02, 08 |
| yellow | 03, 09 |
| gold | 04, 10 |
| red | 05, 11 |
| cyan | 06, 12 |

**Step 6: 批量输出**
- `slides/49_industry_conclusion_1.html`（卡片1-6）
- `slides/50_industry_conclusion_2.html`（卡片7-12）

---

## 中文→英文Hashtag映射（可选工具）

**注意**：`scripts/instagram_screenshot.py` 为可选工具，如需自动截图可使用。

```python
KEYWORD_MAPPING = {
    "水上活动": "watersports",
    "自然探索": "naturelover",
    "极端探险": "extremesports",
    "长途旅行": "traveler",
    "家庭旅行": "familytravel",
    # ...完整映射见脚本
}
```

---

## 插件目录结构

```
minto-slides/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── minto-slides/
│       └── SKILL.md
├── templates/
│   ├── scatter_chart.html
│   ├── user_profile.html
│   └── industry_conclusion.html
├── assets/
│   └── logo.png              # 默认Logo
├── scripts/
│   └── instagram_screenshot.py  # 可选工具
├── examples/
│   ├── example_scatter.json
│   └── example_conclusion.txt
├── requirements.txt
└── README.md
```

---

## 注意事项

1. **Logo必须存在**：每次生成前检查并复制logo到项目目录
2. **图片前置检查**：25-29页生成前必须检查截图是否存在
3. **批量生成**：25-29页一次生成5页，49-50页一次生成2页
4. **数据一致性**：25-29页的人群从24页数据中选取
5. **文字充实**：用户画像页面的文字要足够详细
6. **路径规范**：HTML中的路径统一使用相对路径

---

## 版本

- v2.1.0 - 优化目录结构，支持批量生成，添加前置检查
- v2.0.0 - 重命名为 minto-slides，新增第49-50页行业结论生成
- v1.0.0 - 初始版本
