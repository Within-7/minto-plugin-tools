---
name: minto-slides
description: 演示文稿页面生成器。支持生成消费者洞察散点图(第24页)、用户画像(第25-29页)、品牌目录(第30页)、品牌详情(第31页)、品牌分析(第32页)、社媒营销(第33页)、行业结论卡片(第49-50页)。关键词：演示文稿、幻灯片、散点图、用户画像、品牌目录、品牌详情、品牌分析、社媒营销、行业结论、消费者洞察。
---

# Minto Slides Skill

演示文稿页面生成器，支持生成第24-29页（消费者洞察）、第30页（品牌目录）、第31-33页（品牌案例深度分析）和第49-50页（行业结论）。


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
│   ├── profiles/                    # 25-29页用户画像截图
│   │   ├── 水上活动.png
│   │   ├── 自然探索.png
│   │   ├── 极端探险.png
│   │   ├── 长途旅行.png
│   │   └── 家庭旅行.png
│   ├── brands/                      # 30页品牌目录图片
│   │   ├── spot.png
│   │   ├── biolite.png
│   │   ├── helinox.png
│   │   ├── big_agnes.png
│   │   ├── front_runner.png
│   │   └── rumpl.png
│   ├── brand_details/               # 31页品牌详情图片
│   │   ├── spot_product.png         # 产品图 450×300px
│   │   ├── spot_logo.png            # 品牌Logo 510×350px
│   │   └── ...
│   ├── brand_analysis/              # 32页品牌分析图片（新增）
│   │   ├── spot_persona_1.png       # 用户画像1 ~400×300px
│   │   ├── spot_persona_2.png       # 用户画像2 ~400×300px
│   │   ├── spot_seo_table.png       # SEO表格 ~500×200px
│   │   └── ...
│   └── brand_social/                # 33页社媒营销图片（新增）
│       ├── spot_style_1.png         # 社媒风格1 ~300×250px
│       ├── spot_style_2.png         # 社媒风格2 ~300×250px
│       ├── spot_style_3.png         # 社媒风格3 ~300×250px
│       ├── spot_ambassador.png      # 品牌大使 ~400×350px
│       └── ...
├── data/                            # 数据文件
│   ├── brand_01_detail.json         # 品牌1-第31页数据
│   ├── brand_01_analysis.json       # 品牌1-第32页数据（新增）
│   ├── brand_01_social.json         # 品牌1-第33页数据（新增）
│   ├── brand_02_detail.json         # 品牌2...
│   └── ...
├── slides/                          # 生成的HTML文件
│   ├── 24_user_attention.html
│   ├── 25_user_profile_1.html
│   ├── ...
│   ├── 30_brand_catalog.html
│   ├── 31_brand_detail_01.html
│   ├── 32_brand_analysis_01.html    # 新增
│   ├── 33_brand_social_01.html      # 新增
│   ├── 34_brand_detail_02.html
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
| 品牌案例 | 30 | 品牌目录 | 6个品牌索引（图片宫格 + 列表） |
| 品牌案例 | 31 | 品牌详情 | 单品牌深度拆解（背景+产品+数据+KPI） |
| 品牌案例 | 32 | 品牌分析 | 用户定位+需求+画像+流量模型+SEO+外链（新增） |
| 品牌案例 | 33 | 社媒营销 | KOL合作+社媒数据+风格展示+营销活动（新增） |
| 行业结论 | 49-50 | 卡片布局 | 12个行业结论卡片，每页6个 |

---

## 执行机制

```
# 消费者洞察模块
第24页：单次调用生成
第25-29页：单次调用批量生成5页（需提前准备截图）

# 品牌案例模块（每个品牌生成3页）
第30页：单次调用生成（需提前准备品牌目录图片）

品牌1 (No.01): 31 + 32 + 33 页
品牌2 (No.02): 34 + 35 + 36 页
品牌3 (No.03): 37 + 38 + 39 页
品牌4 (No.04): 40 + 41 + 42 页
品牌5 (No.05): 43 + 44 + 45 页
品牌6 (No.06): 46 + 47 + 48 页

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
3. HTML中的logo路径统一使用：`../assets/logo.png`（因为HTML文件在 slides/ 目录下）

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
- Logo路径：`../assets/logo.png`（HTML在 slides/ 目录，需返回上级）

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
| `slides/25_user_profile_1.html` | 第1个人群 | `../assets/profiles/{人群名}.png` |
| `slides/26_user_profile_2.html` | 第2个人群 | `../assets/profiles/{人群名}.png` |
| `slides/27_user_profile_3.html` | 第3个人群 | `../assets/profiles/{人群名}.png` |
| `slides/28_user_profile_4.html` | 第4个人群 | `../assets/profiles/{人群名}.png` |
| `slides/29_user_profile_5.html` | 第5个人群 | `../assets/profiles/{人群名}.png` |

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
| `{{logoPath}}` | logo路径：`../assets/logo.png` |
| `{{profileImagePath}}` | 截图路径：`../assets/profiles/{人群名}.png` |

---

## SOP - 第30页：品牌目录生成

### 前置条件检查

**Step 1: 检查图片文件**

生成前必须检查 `assets/brands/` 目录：

```
需要6张品牌图片，按文件名字母顺序排序后分配序号01-06
```

**如果图片缺失**：

1. 输出提示信息：
```
⚠️ 检测到以下图片缺失：
- assets/brands/xxx.png

请先上传图片，格式要求：
- 尺寸：448px × 224px（固定）
- 格式：PNG 或 JPG
- 存放位置：assets/brands/
- 文件命名：{品牌名}.png（如：spot.png, big_agnes.png）
- 命名规则：小写字母，单词间用下划线分隔

上传完成后回复"继续"。
```

2. 等待用户确认后再继续

### 图片格式要求

| 项目 | 要求 |
|------|------|
| 宽度 | 448px（固定） |
| 高度 | 224px（固定） |
| 格式 | PNG 或 JPG |
| 命名 | `{品牌名}.png`（如：spot.png, big_agnes.png） |
| 命名规则 | 小写字母，单词间用下划线分隔 |
| 位置 | `assets/brands/` |

### 处理流程

**Step 2: Logo检查与复制**
- 确保 `assets/logo.png` 存在

**Step 3: 扫描并排序图片**

- 扫描 `assets/brands/` 目录下所有图片
- 按文件名字母顺序排序
- 取前6张图片（如不足6张则报错）

**Step 4: 文字处理**

从文件名提取品牌名：
1. 去掉扩展名（`.png`, `.jpg` 等）
2. 下划线转空格（`big_agnes` → `big agnes`）
3. 转为大写（`big agnes` → `BIG AGNES`）

**示例**：
| 文件名 | 提取结果 |
|--------|---------|
| `spot.png` | `SPOT` |
| `big_agnes.png` | `BIG AGNES` |
| `front_runner.png` | `FRONT RUNNER` |

**Step 5: 中文介绍生成与确认**

为每个品牌生成简短中文介绍：

1. AI根据品牌名称自动生成中文介绍（5-10字，基于猜测）
2. 输出给用户确认：
```
品牌中文介绍预览：
01 - FRONT RUNNER：南非越野装备品牌
02 - SPOT：户外运动装备
03 - BIG AGNES：露营装备专家
...

如需修改请告知，确认后回复"继续"。
```
3. 用户可修改任意品牌的中文介绍
4. 确认后再进入下一步

**注意事项**：
- 中文介绍控制在5-10字，过长会超出overlay条
- 对于知名品牌AI可准确描述，小众品牌可能需要用户修正
- 中文介绍在overlay条中右对齐显示

**Step 6: 颜色分配**

6种颜色按顺序固定分配：

| 序号 | 颜色类 | HEX值 | 用途 |
|------|--------|-------|------|
| 01 | bg-01 | #2196F3 | 第1个品牌 |
| 02 | bg-02 | #FF5722 | 第2个品牌 |
| 03 | bg-03 | #FFC107 | 第3个品牌 |
| 04 | bg-04 | #0D47A1 | 第4个品牌 |
| 05 | bg-05 | #607D8B | 第5个品牌 |
| 06 | bg-06 | #E91E63 | 第6个品牌 |

**Step 7: 模板渲染**

使用 `templates/brand_catalog.html` 模板：

| 变量 | 说明 |
|------|------|
| `{{sectionTitle}}` | 部分标题（如：第八部分：品牌案例拆解与学习） |
| `{{subtitle}}` | 副标题（如：品牌案例拆解目录） |
| `{{logoPath}}` | logo路径：`../assets/logo.png` |
| `{{brand1.imagePath}}` | 图片路径：`../assets/brands/xxx.png` |
| `{{brand1.name}}` | 品牌名：`SPOT` |
| `{{brand1.number}}` | 序号：`01` |
| `{{brand1.cnDesc}}` | 中文介绍：`户外运动装备`（5-10字，右对齐显示） |

**Step 8: 输出**

```
✅ slides/30_brand_catalog.html

品牌顺序（按文件名排序）：
01 - SPOT
02 - BIG AGNES
03 - BIOLITE
04 - FRONT RUNNER
05 - HELINOX
06 - RUMPL
```

---

## SOP - 第31页：品牌详情生成

### 前置条件检查

**Step 1: 检查图片文件**

生成前必须检查 `assets/brand_details/` 目录：

```
需要2张品牌图片：
- {品牌名}_product.png  # 产品图 450×300px
- {品牌名}_logo.png     # 品牌Logo 510×350px
```

**如果图片缺失**：

1. 输出提示信息：
```
⚠️ 检测到以下图片缺失：
- assets/brand_details/{品牌名}_product.png
- assets/brand_details/{品牌名}_logo.png

请先上传图片，格式要求：
- 产品图：450px × 300px（宽×高），PNG格式，透明底
- 品牌Logo：510px × 350px（宽×高），PNG格式，透明底
- 存放位置：assets/brand_details/
- 文件命名：{品牌名}_product.png、{品牌名}_logo.png（如：spot_product.png, spot_logo.png）
- 命名规则：小写字母，单词间用下划线分隔

上传完成后回复"继续"。
```

2. 等待用户确认后再继续

### 图片格式要求

| 图片类型 | 宽度 | 高度 | 格式 | 命名规则 |
|---------|------|------|------|---------|
| 产品图 | 450px | 300px | PNG（透明底） | `{品牌名}_product.png` |
| 品牌Logo | 510px | 350px | PNG（透明底） | `{品牌名}_logo.png` |
| 存放位置 | `assets/brand_details/` |

### 数据输入方式

**方式一：Markdown 文件（推荐）**

用户上传 Markdown 文件到 `data/` 目录，格式如下：

**方式二：对话中直接提供**

用户在对话中直接提供品牌信息数据。

### Markdown 文件格式示例

```markdown
# 品牌详情：SPOT
品牌序号：01

## 品牌背景与定位
- 基本信息：创立于2007年，美国路易斯安那州，母公司 Globalstar（2023年营收 1.24亿美元）
- 用户画像：核心用户：重度户外运动玩家、极地探险者、野外科研工作者
- 品牌使命："无论身处何处，卫星通信技术始终保障您的生命安全"
- 竞争优势：全球卫星网络覆盖、专业级SOS救援服务、军工级产品品质

## 爆款产品
- 产品名称：SPOT X 卫星通讯仪
- 产品价格：$249.99 USD
- 产品特点（7条，每条40-60字）：
  1. 内置 QWERTY 全键盘，支持独立发送短信和邮件，无需依赖手机即可完成通讯
  2. 24/7 全球 SOS 求救响应服务，一键触发紧急救援，覆盖全球无盲区
  3. IP67 级军工标准防尘防水，可在极端天气和恶劣环境下稳定工作
  4. 蓝牙连接智能手机 App，实现位置追踪、消息同步和设备远程控制
  5. 超长续航设计，单次充电可连续使用长达 10 天，适合长途户外探险
  6. 支持 GPS/GLONASS 双模定位，定位精度可达 2.5 米，实时轨迹记录
  7. 轻量化机身设计，整机仅重 198g，便于携带，不增加户外负重负担

## 流量来源分布
| 来源 | 占比 |
|-----|-----|
| Direct | 65 |
| Search | 48 |
| Social | 15 |
| Referrals | 12 |
| Mail | 8 |

## 核心运营指标
| 指标 | 数值 |
|-----|-----|
| 日均活跃用户 | 10.6K |
| 平均停留时长 | 02:45 |
| 人均访问页面 | 3.54 |
| 用户跳出率 | 45% |

## 图片文件
- 产品图：spot_product.png
- 品牌Logo：spot_logo.png
```

### 处理流程

**Step 2: Logo检查与复制**
- 确保 `assets/logo.png` 存在

**Step 3: 读取数据**
- 如果用户上传了 Markdown 文件，读取并解析
- 如果用户在对话中提供，直接使用

**Step 4: 数据验证**

必需字段：
- `品牌名称` `品牌序号`
- `基本信息` `用户画像` `品牌使命` `竞争优势`
- `产品名称` `产品价格` `产品特点（7条）`
- `流量来源`（5个）
- `KPI指标`（4个）

**Step 5: 模板渲染**

使用 `templates/brand_detail.html` 模板：

| 变量 | 说明 |
|------|------|
| `{{brandNumber}}` | 品牌序号：`01` |
| `{{brandName}}` | 品牌名称：`SPOT` |
| `{{logoPath}}` | 页面Logo：`../assets/logo.png` |
| `{{basicInfo}}` | 基本信息 |
| `{{userProfile}}` | 用户画像 |
| `{{brandMission}}` | 品牌使命 |
| `{{competitiveAdvantage}}` | 竞争优势 |
| `{{productImagePath}}` | 产品图路径：`../assets/brand_details/{品牌名}_product.png` |
| `{{brandLogoPath}}` | 品牌Logo路径：`../assets/brand_details/{品牌名}_logo.png` |
| `{{productName}}` | 产品名称 |
| `{{productPrice}}` | 产品价格 |
| `{{feature1}}` ~ `{{feature7}}` | 产品特点（7条） |
| `{{traffic.direct}}` | Direct流量占比 |
| `{{traffic.search}}` | Search流量占比 |
| `{{traffic.social}}` | Social流量占比 |
| `{{traffic.referrals}}` | Referrals流量占比 |
| `{{traffic.mail}}` | Mail流量占比 |
| `{{kpi.dau}}` | 日均活跃用户 |
| `{{kpi.duration}}` | 平均停留时长 |
| `{{kpi.pages}}` | 人均访问页面 |
| `{{kpi.bounceRate}}` | 用户跳出率 |

**Step 6: 输出**

```
✅ slides/31_brand_detail.html

品牌：SPOT（No.01）
产品：SPOT X 卫星通讯仪
```

---

## SOP - 第32页：品牌分析生成

### 前置条件检查

**Step 1: 检查图片文件**

生成前必须检查 `assets/brand_analysis/` 目录：

```
需要3张图片：
- {品牌名}_persona_1.png   # 用户画像1 ~400×300px
- {品牌名}_persona_2.png   # 用户画像2 ~400×300px
- {品牌名}_seo_table.png   # SEO关键词表格 ~500×200px
```

**如果图片缺失**：

1. 输出提示信息：
```
⚠️ 检测到以下图片缺失：
- assets/brand_analysis/{品牌名}_persona_1.png
- assets/brand_analysis/{品牌名}_persona_2.png
- assets/brand_analysis/{品牌名}_seo_table.png

请先上传图片，格式要求：
- 用户画像图：约400px × 300px（宽×高）
- SEO表格图：约500px × 200px（宽×高）
- 格式：PNG 或 JPG
- 存放位置：assets/brand_analysis/
- 文件命名：{品牌名}_{类型}.png（如：spot_persona_1.png）

上传完成后回复"继续"。
```

2. 等待用户确认后再继续

### 图片格式要求

| 图片类型 | 宽度 | 高度 | 格式 | 命名规则 |
|---------|------|------|------|---------|
| 用户画像1 | ~400px | ~300px | PNG/JPG | `{品牌名}_persona_1.png` |
| 用户画像2 | ~400px | ~300px | PNG/JPG | `{品牌名}_persona_2.png` |
| SEO表格 | ~500px | ~200px | PNG/JPG | `{品牌名}_seo_table.png` |
| 存放位置 | `assets/brand_analysis/` |

### 数据输入方式

**JSON 文件格式**

用户上传 JSON 文件到 `data/` 目录，格式参考 `examples/example_brand_analysis.json`

### 处理流程

**Step 2: Logo检查与复制**
- 确保 `assets/logo.png` 存在

**Step 3: 读取数据**
- 读取 `data/{品牌名}_analysis.json` 文件
- 或用户在对话中直接提供数据

**Step 4: 数据验证**

必需字段：
- `brandNumber` `brandName` `logoPath`
- `userPosition` - 用户定位（圆环图数据）
- `userNeeds` - 用户需求（4个文本块）
- `flowModel` - 流量模型（流程节点）
- `seoTraffic` - 基石流量（文字+表格图片）
- `backlinkAnalysis` - 外链分析（饼图+条形图）

**Step 5: 模板渲染**

使用 `templates/brand_analysis.html` 模板，页面包含6个卡片：

| 卡片 | 内容类型 | 说明 |
|-----|---------|-----|
| 用户定位 | 圆环图 | 展示用户群体分布 |
| 用户需求 | 文字 | 核心诉求、使用场景、决策因素、购买渠道 |
| 用户画像 | 双图 | INS截图展示 |
| 流量模型 | 流程图 | 搜索→落地页→转化→购买 |
| 基石流量 | 文字+图 | SEO关键词分析 |
| 外链分析 | 饼图+条形图 | 外链来源+热门关键词 |

**Step 6: 输出**

```
✅ slides/32_brand_analysis_01.html（品牌1）
✅ slides/35_brand_analysis_02.html（品牌2）
...
```

---

## SOP - 第33页：社媒营销生成

### 前置条件检查

**Step 1: 检查图片文件**

生成前必须检查 `assets/brand_social/` 目录：

```
需要4张图片：
- {品牌名}_style_1.png      # 社媒风格展示1 ~300×250px
- {品牌名}_style_2.png      # 社媒风格展示2 ~300×250px
- {品牌名}_style_3.png      # 社媒风格展示3 ~300×250px
- {品牌名}_ambassador.png   # 品牌大使图片 ~400×350px
```

**如果图片缺失**：

1. 输出提示信息：
```
⚠️ 检测到以下图片缺失：
- assets/brand_social/{品牌名}_style_1.png
- assets/brand_social/{品牌名}_style_2.png
- assets/brand_social/{品牌名}_style_3.png
- assets/brand_social/{品牌名}_ambassador.png

请先上传图片，格式要求：
- 社媒风格图：约300px × 250px（宽×高）
- 品牌大使图：约400px × 350px（宽×高）
- 格式：PNG 或 JPG
- 存放位置：assets/brand_social/
- 文件命名：{品牌名}_{类型}.png

上传完成后回复"继续"。
```

2. 等待用户确认后再继续

### 图片格式要求

| 图片类型 | 宽度 | 高度 | 格式 | 命名规则 |
|---------|------|------|------|---------|
| 社媒风格1 | ~300px | ~250px | PNG/JPG | `{品牌名}_style_1.png` |
| 社媒风格2 | ~300px | ~250px | PNG/JPG | `{品牌名}_style_2.png` |
| 社媒风格3 | ~300px | ~250px | PNG/JPG | `{品牌名}_style_3.png` |
| 品牌大使 | ~400px | ~350px | PNG/JPG | `{品牌名}_ambassador.png` |
| 存放位置 | `assets/brand_social/` |

### 数据输入方式

**JSON 文件格式**

用户上传 JSON 文件到 `data/` 目录，格式参考 `examples/example_brand_social.json`

### 处理流程

**Step 2: Logo检查与复制**
- 确保 `assets/logo.png` 存在

**Step 3: 读取数据**
- 读取 `data/{品牌名}_social.json` 文件
- 或用户在对话中直接提供数据

**Step 4: 数据验证**

必需字段：
- `brandNumber` `brandName` `logoPath`
- `kolStats` - KOL合作数量（统计+柱状图）
- `socialMediaData` - 官方社媒数据（IG/FB/YT表格）
- `socialStyle` - 社媒风格展示（3张图片）
- `activity1` - 活动一（救援活动）
- `activity2` - 活动二（合作赞助）
- `ambassador` - 品牌大使（列表+图片）

**Step 5: 模板渲染**

使用 `templates/brand_social.html` 模板，页面包含6个卡片：

| 卡片 | 内容类型 | 说明 |
|-----|---------|-----|
| KOL合作数量 | 统计+柱状图 | KOL分层统计 |
| 官方社媒数据 | 表格 | IG/FB/YT数据 |
| 社媒风格展示 | 三图 | 产品推荐/应用场景/救援活动 |
| 活动一 | 文字+统计 | 救援活动营销 |
| 活动二 | 文字+统计 | 合作赞助活动 |
| 品牌大使 | 列表+图 | 大使介绍+合影 |

**Step 6: 输出**

```
✅ slides/33_brand_social_01.html（品牌1）
✅ slides/36_brand_social_02.html（品牌2）
...
```

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
│   ├── brand_catalog.html       # 第30页品牌目录模板
│   ├── brand_detail.html        # 第31页品牌详情模板
│   ├── brand_analysis.html      # 第32页品牌分析模板（新增）
│   ├── brand_social.html        # 第33页社媒营销模板（新增）
│   └── industry_conclusion.html
├── assets/
│   └── logo.png              # 默认Logo
├── scripts/
│   └── instagram_screenshot.py  # 可选工具
├── examples/
│   ├── example_scatter.json
│   ├── example_conclusion.txt
│   ├── example_brand_detail.md     # 第31页示例数据
│   ├── example_brand_analysis.json # 第32页示例数据（新增）
│   └── example_brand_social.json   # 第33页示例数据（新增）
├── requirements.txt
└── README.md
```

---

## 注意事项

1. **Logo必须存在**：每次生成前检查并复制logo到项目目录
2. **图片前置检查**：25-29页、30页、31-33页生成前必须检查图片是否存在
3. **批量生成**：25-29页一次生成5页，49-50页一次生成2页
4. **品牌案例循环**：31-33页为一个品牌，共6个品牌循环生成（31-48页）
5. **数据一致性**：25-29页的人群从24页数据中选取
6. **文字充实**：用户画像页面、品牌详情页面的文字要足够详细
7. **路径规范**：HTML文件存放在 slides/ 目录，图片路径需使用 `../assets/` 相对路径
8. **品牌图片命名**：30页品牌图片需按规则命名（小写+下划线），文件名决定显示顺序和文字
9. **数据格式**：31页使用Markdown，32-33页使用JSON格式

---

## 版本

- v2.5.0 - 新增第32页品牌分析、第33页社媒营销生成功能（模板+示例+JSON数据格式）
- v2.4.0 - 新增第31页品牌详情生成功能（模板+示例+图片规格）
- v2.3.0 - 第30页品牌目录新增中文介绍功能（右对齐显示，用户可确认修改）
- v2.2.0 - 新增第30页品牌目录生成功能
- v2.1.0 - 优化目录结构，支持批量生成，添加前置检查
- v2.0.0 - 重命名为 minto-slides，新增第49-50页行业结论生成
- v1.0.0 - 初始版本
