---
name: "beauty-step3"
description: "HTML样式布局代码生成。将步骤2的页面清单转换为HTML文件。采用内容→组件→布局→代码流程。用于处理：内容元素识别、HTML组件匹配、布局选择、代码生成。严格根据beauty-html skill选择布局。使用beauty-html-reference.md中指定的颜色规范。"
---

# Beauty 步骤3：HTML样式布局代码生成

## 目标

将步骤2生成的幻灯片页面清单转换为完整的、可运行的HTML文件。

采用**内容→组件→布局→代码**的优化流程。

## 核心原则 [CRITICAL]

**幻灯片格式 [强制 - 新增]**：
- 每个页面必须是独立的幻灯片，使用 `.slide` 类
- 幻灯片必须使用 `position: absolute` 定位，实现全屏切换
- 必须使用 `.active` 类控制当前显示的幻灯片
- 必须实现页面导航功能（点击按钮、键盘方向键、触摸滑动）
- 禁止使用网页形式（上下滚动查看所有内容）
- 禁止将所有内容放在一个长页面中

**图表使用 [强制 - 新增]**：
- 数据相关内容必须使用图表组件可视化
- 数值对比数据必须使用柱状图
- 趋势变化数据必须使用折线图
- 占比/比例数据必须使用饼图或环形图
- 多维评估数据必须使用雷达图
- 流程转化数据必须使用漏斗图
- 每个图表必须配合洞察面板（图表概述、数据解读、洞察分析）
- 禁止只有数据文本而没有图表可视化
- 禁止用简单列表代替图表

**颜色规范 [强制]**：
- 必须使用 beauty-html-reference.md 中定义的配色方案
- 禁止使用其他颜色系统
- 主背景色：#FFFFFF
- 标题栏背景：#000000
- 主要强调色：#F85d42

**必读资源**：
- [beauty-html-reference.md](./beauty-html-reference.md) - 简化版CSS样式库和HTML模板（包含颜色规范）
- [beauty-component-guide.md](./beauty-component-guide.md) - 简化版组件选择指南

**重要：布局选择必须严格遵循beauty-html skill规则**：
- 必须读取 `beauty-html/LAYOUTS_INDEX.md` 获取完整布局索引
- 必须读取 `beauty-html/COMPONENTS_INDEX.md` 获取组件索引
- 必须参考 `beauty-html/assets/layouts/*.html` 布局示例文件
- 必须参考 `beauty-html/assets/components/*.html` 组件示例文件

**项目特定资源优先级**（如果存在）：
- `.ppt_assets/INDEX.md` - 项目特定的布局和图表示例（优先级最高）

**Token限制处理**：
- 遇到token限制时使用"继续"机制
- 禁止压缩或省略资源读取
- 禁止跳过必读资源

## 执行流程

```
步骤3.1：读取必读资源 → 步骤3.2：识别内容元素 → 步骤3.3：匹配组件 → 步骤3.4：选择布局 → 步骤3.5：生成HTML
```

---

## 步骤 3.1：读取必读资源

### 目标

完整读取所有必读资源，为后续代码生成提供参考。

### 必读资源清单

#### 核心资源（必须按顺序读取）

```
阶段1：读取 beauty-html/LAYOUTS_INDEX.md
├─ 布局类型索引（L1-L17）
├─ 布局结构示例
├─ 布局配置参数
└─ 布局选择决策树

阶段2：读取 beauty-html/COMPONENTS_INDEX.md
├─ 图表组件索引（C1-C3）
├─ 图示组件索引（D1-D3）
├─ 表格组件索引（T1）
├─ 组件CSS类名和配置
└─ 组件选择决策树

阶段3：读取 beauty-html-reference.md
├─ 配色方案（必须严格遵循）
├─ CSS变量定义
├─ 布局结构
└─ 组件模板

阶段4：读取 beauty-component-guide.md
├─ 图表组件选择决策树
├─ 图示组件说明
└─ 表格组件配置
```

#### 项目特定资源（如果存在）

```
阶段5：检查并读取 .ppt_assets/INDEX.md（如果存在）
├─ 项目特定的布局示例
├─ 项目特定的图表示例
├─ 项目特定的样式和组件
└─ ⚠️ 优先级规则：如果某个布局、图表或图文展示在 beauty-html 和 .ppt_assets 中都存在，
   必须优先使用 .ppt_assets/INDEX.md 中的版本
```

### 资源读取优先级规则 [CRITICAL]

```
优先级顺序（从高到低）：
1. .ppt_assets/INDEX.md（如果存在）
2. beauty-html/INDEX.md
3. beauty-html/LAYOUTS_INDEX.md
4. beauty-html/COMPONENTS_INDEX.md
5. beauty-html/assets/layouts/*.html
6. beauty-html/assets/components/*.html

示例：
├─ 如果 .ppt_assets/INDEX.md 存在且包含"漏斗图"示例 → 使用项目版本
├─ 如果 .ppt_assets/INDEX.md 不存在 → 使用 beauty-html 版本
└─ 如果两者都存在相同组件 → 优先使用 .ppt_assets 版本
```

### 验证标准

- [ ] 已读取beauty-html/LAYOUTS_INDEX.md并理解布局选择规则
- [ ] 已读取beauty-html/COMPONENTS_INDEX.md并理解组件选择规则
- [ ] 已理解颜色规范（beauty-html-reference.md）
- [ ] 已了解所有可用的布局类型和组件
- [ ] 已检查项目是否存在.ppt_assets/INDEX.md（如存在则已读取）

---

## 步骤 3.2：识别内容元素

### 目标

识别每页幻灯片的内容元素类型，为组件匹配做准备。

### 元素类型

| 类别 | 类型 | 说明 |
|-----|------|------|
| 文本 | 主标题、要点列表、编号列表 | 文字内容 |
| 数据 | 数字、百分比、货币 | 量化信息 |
| 图表 | 柱状图、折线图、饼图、雷达图 | 可视化 |
| 表格 | 简单表格、对比表格 | 结构化数据 |
| 布局 | 卡片、对比框、强调框 | 容器组件 |

### 执行要求

为每页生成元素识别清单：

```markdown
页面X：[页面标题]
- 文本元素：标题1个，要点列表N项
- 数据元素：数字N个，百分比N个
- 图表元素：柱状图1个（5数据点）
- 表格元素：无
- 布局元素：卡片N个
```

### 验证标准

- [ ] 所有页面已完成元素识别
- [ ] 元素分类准确
- [ ] 无遗漏内容元素

---

## 步骤 3.3：匹配HTML组件

### 目标

根据识别的元素类型，从资源文件中读取并匹配对应的HTML组件。

### 组件资源读取流程

**步骤3.3.1：读取beauty-html组件索引**

```
执行操作：
├─ 读取 beauty-html/assets/COMPONENTS_INDEX.md
│   ├─ 图表组件索引（C1-C3）
│   ├─ 图示组件索引（D1-D3）
│   ├─ 表格组件索引（T1）
│   └─ 组件选择决策树
├─ 遍历 beauty-html/assets/components/*.html
│   ├─ 图表组件示例（bar-chart, line-chart, pie-chart等）
│   ├─ 图示组件示例（swot, timeline, flowchart等）
│   └─ 特殊组件示例（funnel, pyramid, gauge等）
└─ 记录可用组件及其CSS类名和配置参数
```

**步骤3.3.2：读取.ppt_assets组件资源（如存在）**

```
执行操作：
├─ 检查 .ppt_assets/COMPONENTS_INDEX.md（如存在）
├─ 遍历 .ppt_assets/components/*.html（如存在）
├─ 遍历 .ppt_assets/assets/components/*.html（如存在）
└─ 记录项目特定的组件配置（优先级高于beauty-html）
```

**组件资源读取优先级**：

```
优先级顺序（从高到低）：
1. .ppt_assets/assets/components/*.html（如存在）
2. .ppt_assets/components/*.html（如存在）
3. .ppt_assets/COMPONENTS_INDEX.md（如存在）
4. beauty-html/assets/components/*.html
5. beauty-html/assets/COMPONENTS_INDEX.md

示例：
├─ 需求：漏斗图组件
├─ 检查.ppt_assets/assets/components/funnel-chart.html → 存在则使用
├─ 检查.ppt_assets/components/funnel-chart.html → 存在则使用
├─ 检查.beauty-html/assets/components/funnel-chart-example.html → 使用此版本
└─ → 根据实际找到的文件路径读取组件代码
```

### 组件选择决策树

根据识别的元素类型，从已读取的资源中选择匹配组件：

```
数据内容必须使用图表组件，数据可视化优先级规则：

【必须使用图表的情况】
├─ 数值对比（如：市场规模、增长率、占比）→ 柱状图或饼图
├─ 时间趋势（如：历年数据变化、季度趋势）→ 折线图
├─ 多维评估（如：SWOT分析、竞争力评估）→ 雷达图
├─ 流程转化（如：销售漏斗、用户转化）→ 漏斗图
└─ 分类占比（如：市场份额、预算分配）→ 饼图或环形图

【图表类型选择规则】
├─ 柱状图：适用离散类别数据比较，3-10个数据点
├─ 折线图：适用连续时间序列数据，3-12个时间点
├─ 饼图：适用部分与整体占比，2-6个分类
├─ 雷达图：适用多维度能力评估，4-8个维度
└─ 漏斗图：适用流程转化分析，3-6个阶段

【布局规则】
├─ 单图表页：必须使用两列布局（图表55% + 洞察45%）
├─ 多图表页：必须使用三列布局（并排对比）
└─ 禁止单列布局放置图表

内容元素 → 推荐组件（从已读取的组件资源中选择）
├─ 要点列表 → ul.bullet-list / ul.numbered-list
├─ 数字强调 → .big-number
├─ 柱状图 → div.bar-chart（多列布局，必须）
├─ 折线图 → div.line-chart（多列布局，必须）
├─ 饼图 → div.pie-chart（多列布局，必须）
├─ 雷达图 → div.radar-chart（多列布局，必须）
├─ 漏斗图 → div.funnel-chart（多列布局，必须）
├─ 金字塔图 → div.pyramid-chart
├─ 对比分析 → div.comparison-chart
├─ SWOT分析 → div.swot-analysis
├─ 时间线 → div.timeline
├─ 流程图 → div.flowchart
├─ 表格 → table.comparison-table
└─ 图表解释说明 → div.chart-insights / div.insight-panel
```

**图表组件使用验证清单 [强制检查]**：

```
每个包含数据的页面 图表类型选择必须验证：

□正确
   ├─ □ 数值对比使用柱状图
   ├─ □ 时间趋势使用折线图
   ├─ □ 占比分析使用饼图
   ├─ □ 多维评估使用雷达图
   └─ □ 流程转化使用漏斗图

□ 图表布局正确
   ├─ □ 使用两列布局（图表+洞察）
   └─ □ 禁止单列布局

□ 图表数据完整
   ├─ □ 所有数据点已可视化
   ├─ □ 数据标签完整显示
   └─ □ 图表标题准确描述

□ 洞察面板完整
   ├─ □ 图表概述完整
   ├─ □ 数据解读逐项展开
   ├─ □ 洞察分析提炼到位
   └─ □ 行动建议（推荐）

□ 禁止行为
   ├─ □ 没有用文本列表代替图表
   ├─ □ 没有省略图表数据标签
   ├─ □ 没有删除图表数值
   └─ □ 没有简化图表说明
```

### 图表解释说明组件

**必须为每个图表配置解释说明组件**：

```
图表页组件结构：
├─ 图表容器（左侧55%）
│   └─ 图表HTML（柱状图/折线图/饼图等）
└─ 洞察面板（右侧45%）
    ├─ 图表概述
    ├─ 数据解读
    ├─ 洞察分析
    └─ 行动建议（推荐）
```

**洞察面板组件资源读取**：

```
读取流程：
1. 检查 .ppt_assets/assets/components/*insight*.html（如存在）
2. 检查 .ppt_assets/components/*insight*.html（如存在）
3. 检查 beauty-html/assets/components/*insight*.html
4. 检查 beauty-html/assets/guides/INSIGHT_VISUALIZATION_GUIDE.md
5. 复制洞察面板的HTML结构和CSS样式
6. 根据步骤2.3.2生成的洞察内容填充数据

组件结构参考：
├─ .insight-panel（洞察面板容器）
│   ├─ .insight-section.chart-overview（图表概述）
│   ├─ .insight-section.data-interpretation（数据解读）
│   ├─ .insight-section.insight-analysis（洞察分析）
│   └─ .insight-section.action-recommendations（行动建议）
```

### 禁止行为 [CRITICAL]

**❌ 绝对禁止**：
- ❌ 图表页没有洞察面板或解释说明
- ❌ 洞察面板只有简单的一两句话
- ❌ 省略图表中的关键数据解读
- ❌ 只保留图表，没有文字说明

**✅ 正确做法**：
- ✅ 每个图表必须配合完整的洞察面板
- ✅ 洞察面板必须包含：图表概述、数据解读、洞察分析
- ✅ 行动建议推荐添加
- ✅ 洞察面板内容必须与步骤2.3.2的输出一致

### 组件示例参考规则

```
选择组件时，必须按优先级读取以下资源：
1. .ppt_assets/assets/components/[component-name]-example.html（如存在）
2. .ppt_assets/components/[component-name]-example.html（如存在）
3. .ppt_assets/INDEX.md 中的组件示例（如存在）
4. beauty-html/assets/components/[component-name]-example.html
5. beauty-html/assets/COMPONENTS_INDEX.md 中的组件配置

示例参考步骤：
1. 确定组件类型（如：漏斗图）
2. 按优先级检查资源文件是否存在
3. 读取找到的资源文件，获取HTML结构和CSS样式
4. 复制组件代码到当前页面
5. 根据实际内容调整数据和标签
```

### 图表布局规则 [CRITICAL]

- ❌ 禁止单列布局放置图表
- ✅ 必须使用2列布局（图表+洞察）
- ✅ 或使用3列布局（多图表并排）
- ✅ 布局配置参考 beauty-html/LAYOUTS_INDEX.md 和 beauty-html/assets/layouts/*.html

### 验证标准

- [ ] 已读取beauty-html/assets/COMPONENTS_INDEX.md
- [ ] 已读取beauty-html/assets/components/*.html中的组件示例
- [ ] 如.ppt_assets存在，已优先读取项目特定组件
- [ ] 每个元素都有匹配的组件
- [ ] 组件选择参考了已读取的资源文件
- [ ] 图表使用多列布局
- [ ] 组件选择符合内容特征

---

## 步骤 3.4：选择布局

### 目标

根据页面类型和组件需求，从资源文件中读取并选择合适的布局。

### 布局资源读取流程

**步骤3.4.1：读取beauty-html布局索引**

```
执行操作：
├─ 读取 beauty-html/assets/LAYOUTS_INDEX.md
│   ├─ 布局类型索引（L1-L17）
│   ├─ 布局结构示例
│   ├─ 布局配置参数
│   └─ 布局选择决策树
├─ 遍历 beauty-html/assets/layouts/*.html
│   ├─ 封面页布局（cover-page, NEW_01-cover-page.html等）
│   ├─ 内容页布局（two-column, three-column, card-grid等）
│   ├─ 章节页布局（chapter-overview, NEW_05-chapter-cover等）
│   └─ 特殊布局（toc-grid, traffic-analysis等）
└─ 记录可用布局及其CSS类名和配置参数
```

**步骤3.4.2：读取.ppt_assets布局资源（如存在）**

```
执行操作：
├─ 检查 .ppt_assets/LAYOUTS_INDEX.md（如存在）
├─ 遍历 .ppt_assets/layouts/*.html（如存在）
├─ 遍历 .ppt_assets/assets/layouts/*.html（如存在）
└─ 记录项目特定的布局配置（优先级高于beauty-html）
```

**布局资源读取优先级**：

```
优先级顺序（从高到低）：
1. .ppt_assets/assets/layouts/*.html（如存在）
2. .ppt_assets/layouts/*.html（如存在）
3. .ppt_assets/LAYOUTS_INDEX.md（如存在）
4. beauty-html/assets/layouts/*.html
5. beauty-html/assets/LAYOUTS_INDEX.md

示例：
├─ 需求：封面页布局
├─ 检查.ppt_assets/assets/layouts/cover-page.html → 存在则使用
├─ 检查.ppt_assets/layouts/cover-page.html → 存在则使用
├─ 检查.ppt_assets/INDEX.md是否有封面页布局 → 存在则使用
├─ 检查.beauty-html/assets/layouts/01-cover-page.html → 使用此版本
└─ → 根据实际找到的文件路径读取布局代码
```

### 布局选择决策树

根据页面类型和组件需求，从已读取的资源中选择匹配布局：

```
根据页面内容特征选择布局：
1. 页面包含图表？
   ├─ 是 → 图表数量？
   │   ├─ 1个 → 两列布局（图表+洞察）
   │   ├─ 2个 → 三列布局（并排对比）
   │   └─ ≥3个 → 卡片网格或分多页
   └─ 否 → 内容类型？
       ├─ 纯文本 ≤8要点 → 单列布局
       ├─ 步骤/流程 → 流程布局
       ├─ 时间序列 → 时间线布局
       ├─ 多主题并列 → 卡片网格布局
       └─ 章节过渡 → 章节首页布局

布局类型 → 推荐布局（从已读取的布局资源中选择）
├─ 封面页 → .cover-slide / .slide.cover
├─ 目录页 → .toc-slide / .slide.toc
├─ 章节首页 → .chapter-slide / .slide.chapter
├─ 内容页-纯文本 → .single-column / .content-text
├─ 内容页-图表+洞察 → .two-column / .chart-insights
├─ 内容页-多图表 → .three-column / .multi-chart
├─ 内容页-卡片网格 → .card-grid / .grid-cards
└─ 结束页 → .ending-slide / .slide.ending
```

### 项目特定布局优先级 [CRITICAL]

如果.ppt_assets布局资源存在，必须优先使用：

```
检查流程：
1. 确定所需布局类型（如：封面页布局、图表+洞察布局）
2. 按优先级检查.ppt_assets资源文件是否存在
3. 如果有 → 读取并使用.ppt_assets版本
4. 如果没有 → 读取并使用beauty-html版本

示例：
├─ 需求：封面页布局
├─ 检查.ppt_assets/assets/layouts/cover-page.html → 存在
└─ → 使用.ppt_assets中的封面页布局和样式

├─ 需求：漏斗图布局（.ppt_assets中不存在）
├─ 检查.ppt_assets/assets/layouts/funnel-chart.html → 不存在
├─ 检查.beauty-html/assets/layouts/funnel-chart.html → 不存在
├─ 检查.beauty-html/assets/layouts/05-chart-text.html → 存在
└─ → 使用beauty-html中的两列布局（图表+洞察）适配漏斗图
```

### 布局配置参考

选择布局后，从已读取的资源中获取配置参数：

```
布局配置参数来源（从已读取的资源中选择）：
├─ 布局CSS类名（来自LAYOUTS_INDEX.md或布局HTML文件）
├─ 容器宽度和间距（来自布局HTML文件的CSS样式）
├─ 列配置（grid-template-columns）
├─ 响应式断点
└─ 动画和过渡效果

配置参考步骤：
1. 从已读取的LAYOUTS_INDEX.md获取布局类型和配置参数
2. 从已读取的布局HTML文件获取实际CSS样式
3. 从已读取的mckinsey-design-standards.css获取CSS变量
4. 根据实际内容需求调整布局参数
```

### 背景颜色规则 [CRITICAL]

**必须严格使用beauty-html-reference.md中定义的颜色规范**：

```
主背景色：#FFFFFF（配黑字：#1A202C）
标题栏背景：#000000（配白字）
主要强调色：#F85d42（用于重点突出）
辅助色：#74788d, #556EE6, #34c38f, #50a5f1, #f1b44c

对比度要求：≥ 4.5:1
```

**颜色规范资源读取**：

```
读取流程：
1. 检查 .ppt_assets/INDEX.md 中的颜色规范（如存在）
2. 检查 .ppt_assets/assets/colors.md（如存在）
3. 检查 beauty-html-reference.md 中的颜色规范
4. 读取并应用指定的CSS变量

颜色变量参考：
├─ --color-bg: #FFFFFF
├─ --color-header: #000000
├─ --color-accent: #F85d42
├─ --color-gray: #74788d
└─ --color-primary: #556EE6
```

### 验证标准

- [ ] 已读取beauty-html/assets/LAYOUTS_INDEX.md
- [ ] 已读取beauty-html/assets/layouts/*.html中的布局示例
- [ ] 如.ppt_assets存在，已优先读取项目特定布局
- [ ] 布局选择符合页面类型
- [ ] 布局选择参考了已读取的资源文件
- [ ] 背景颜色有足够对比度
- [ ] 符合beauty-html-reference.md中定义的颜色规范

---

## 步骤 3.5：生成HTML

### 目标

根据规划的布局和组件，分阶段生成完整的HTML文件到本地。

### 分阶段写入流程

由于HTML文件可能较大，必须分阶段写入本地文件：

```
阶段1：创建HTML框架和CSS样式
  ├─ 写入DOCTYPE和head部分
  ├─ 写入CSS变量和全局样式
  └─ 写入导航栏结构

阶段2：按章节生成幻灯片
  ├─ 写入封面页
  ├─ 写入目录页
  ├─ 逐个写入章节首页
  ├─ 逐个写入内容页
  └─ 写入结束页

阶段3：生成JavaScript和结束标签
  ├─ 写入导航功能JavaScript
  ├─ 写入键盘和触摸事件
  └─ 写入body结束标签
```

### 阶段1：HTML框架和CSS样式

**步骤3.5.1：写入HTML头部**

```
执行操作：
├─ 使用Write工具创建或覆盖输出HTML文件
├─ 写入<!DOCTYPE html>声明
├─ 写入<html lang="zh-CN">标签
├─ 写入<head>部分，包含meta标签和title
├─ 写入CSS样式（beauty-html-reference.md定义的颜色规范）
│   └─ :root变量定义
│       ├─ --color-bg: #FFFFFF
│       ├─ --color-header: #000000
│       ├─ --color-accent: #F85d42
│       ├─ --color-gray: #74788d
│       ├─ --color-blue: #556EE6
│       ├─ --color-green: #34c38f
│       ├─ --color-light-blue: #50a5f1
│       ├─ --color-yellow: #f1b44c
│       └─ 字体和间距变量
├─ 写入布局基础样式
└─ 写入导航栏样式
```

**步骤3.5.2：写入幻灯片容器和导航控件 [强制更新]**

```
执行操作：
├─ 写入.presentation-container容器（width: 100%, height: 100vh, overflow: hidden）
├─ 写入.slide基础样式：
│   ├─ position: absolute
│   ├─ top: 0, left: 0
│   ├─ width: 100%, height: 100%
│   ├─ opacity: 0, visibility: hidden
│   ├─ transition: opacity 0.4s ease, visibility 0.4s ease
│   └─ overflow-y: auto（每页内容可滚动）
├─ 写入.slide.active状态（opacity: 1, visibility: visible, z-index: 1）
├─ 写入.slide-header固定导航栏：
│   ├─ position: fixed, top: 0
│   ├─ height: 60px, background: #000000
│   ├─ color: white, z-index: 100
│   └─ 封面页/章节首页/结束页隐藏：.cover-slide .slide-header { display: none; }
├─ 写入导航按钮（.nav-button）：
│   ├─ .nav-prev（上一页按钮，左侧）
│   ├─ .nav-next（下一页按钮，右侧）
│   └─ 必须显示：display: flex
├─ 写入页码计数器（.slide-counter）：
│   ├─ position: fixed, bottom: 20px
│   ├─ 显示格式："{当前页} / {总页数}"
│   └─ 必须显示：display: block
├─ 写入全屏按钮（.fullscreen-button）：
│   ├─ position: fixed, top: 20px, right: 20px
│   └─ 必须显示：display: flex
└─ 禁止行为：
    ├─ 禁止删除或隐藏导航按钮
    ├─ 禁止删除或隐藏页码计数器
    ├─ 禁止使用长页面滚动格式
    └─ 禁止省略JavaScript导航功能
```

**幻灯片CSS样式模板 [强制使用]**：

```css
.presentation-container {
    width: 100%;
    height: 100vh;
    position: relative;
    overflow: hidden;
    background: var(--color-bg, #FFFFFF);
}

.slide {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: var(--color-bg, #FFFFFF);
    padding: var(--page-padding, 80px 60px 60px 60px);
    box-sizing: border-box;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.4s ease, visibility 0.4s ease;
    overflow-y: auto;
}

.slide.active {
    opacity: 1;
    visibility: visible;
    z-index: 1;
}

.slide-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 60px;
    background: var(--color-primary, #000000);
    color: white;
    display: flex;
    align-items: center;
    padding: 0 60px;
    z-index: 100;
}

.cover-slide .slide-header,
.chapter-slide .slide-header,
.ending-slide .slide-header {
    display: none;
}
```

**导航功能JavaScript模板 [强制包含]**：

```javascript
// 幻灯片导航功能
document.addEventListener('DOMContentLoaded', function() {
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;
    let currentSlide = 1;
    
    // 显示第一页
    showSlide(1);
    
    // 显示指定幻灯片
    function showSlide(n) {
        if (n < 1) n = 1;
        if (n > totalSlides) n = totalSlides;
        
        slides.forEach(slide => {
            slide.classList.remove('active');
        });
        
        const targetSlide = document.getElementById('slide-' + n);
        if (targetSlide) {
            targetSlide.classList.add('active');
        }
        
        // 更新页码计数器
        const counter = document.querySelector('.slide-counter');
        if (counter) {
            counter.textContent = n + ' / ' + totalSlides;
        }
        
        // 更新导航按钮状态
        const prevBtn = document.querySelector('.nav-prev');
        const nextBtn = document.querySelector('.nav-next');
        if (prevBtn) prevBtn.disabled = (n === 1);
        if (nextBtn) nextBtn.disabled = (n === totalSlides);
        
        currentSlide = n;
    }
    
    // 上一页
    document.querySelector('.nav-prev').addEventListener('click', function() {
        showSlide(currentSlide - 1);
    });
    
    // 下一页
    document.querySelector('.nav-next').addEventListener('click', function() {
        showSlide(currentSlide + 1);
    });
    
    // 键盘导航
    document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
            showSlide(currentSlide - 1);
        } else if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') {
            showSlide(currentSlide + 1);
        } else if (e.key === 'Home') {
            showSlide(1);
        } else if (e.key === 'End') {
            showSlide(totalSlides);
        }
    });
    
    // 触摸滑动支持
    let touchStartX = 0;
    let touchEndX = 0;
    
    document.addEventListener('touchstart', function(e) {
        touchStartX = e.changedTouches[0].screenX;
    });
    
    document.addEventListener('touchend', function(e) {
        touchEndX = e.changedTouches[0].screenX;
        if (touchStartX - touchEndX > 50) {
            showSlide(currentSlide + 1);
        } else if (touchEndX - touchStartX > 50) {
            showSlide(currentSlide - 1);
        }
    });
    
    // 全屏功能
    document.querySelector('.fullscreen-button').addEventListener('click', function() {
        if (document.fullscreenElement) {
            document.exitFullscreen();
        } else {
            document.documentElement.requestFullscreen();
        }
    });
});
```

### 阶段2：按章节生成幻灯片

**步骤3.5.3：写入封面页**

```
执行操作：
├─ 写入<div class="slide cover-slide active" id="slide-1">
├─ 写入纯色背景样式（从以下颜色随机选取：#556EE6、#F85d42、#34c38f、#50a5f1、#f1b44c、#000000）
├─ 写入标题<h1>和副标题
├─ 写入品牌标识
└─ 封面页必须隐藏导航栏
```

**步骤3.5.4：写入目录页**

```
执行操作：
├─ 写入<div class="slide" id="slide-2">
├─ 使用.toc-grid网格布局
├─ 写入所有章节入口
├─ 添加点击跳转功能
└─ 恢复导航栏显示
```

**步骤3.5.5：逐个写入章节首页**

```
执行操作（每个章节）：
├─ 写入<div class="slide chapter-slide" id="slide-N">
├─ 写入纯色背景样式（从以下颜色随机选取：#556EE6、#F85d42、#34c38f、#50a5f1、#f1b44c、#000000）
├─ 写入章节编号（01、02...）
├─ 写入章节标题
├─ 写入章节描述
├─ 写入章节概览列表（包含所有子标题和页码）
└─ 章节首页必须隐藏导航栏
```

**步骤3.5.6：逐个写入内容页**

```
执行操作（每个内容页）：
├─ 写入<div class="slide" id="slide-N">
├─ 写入导航栏（显示当前标题）
├─ 根据布局类型选择结构：
│   ├─ 单列布局 → .single-column
│   ├─ 双列布局 → .two-column
│   └─ 三列布局 → .three-column
├─ 写入页面标题<h2>
├─ 写入页面导语（从步骤2.3.1获取）
├─ 写入详细内容（每个要点的完整描述）
├─ 写入关联说明（如果适用）
├─ 如果页面包含图表：
│   ├─ 使用两列布局（图表+洞察）
│   ├─ 左侧写入图表HTML
│   └─ 右侧写入洞察面板：
│       ├─ 图表概述（从步骤2.3.2获取）
│       ├─ 数据解读（从步骤2.3.2获取）
│       ├─ 洞察分析（从步骤2.3.2获取）
│       └─ 行动建议（从步骤2.3.2获取，推荐）
├─ 应用颜色规范
│   ├─ 强调色：#F85d42
│   ├─ 辅助色：#74788d
│   └─ 图表颜色：#556EE6、#34c38f、#50a5f1、#f1b44c
└─ 确保每页内容≤8个要点
```

**内容页HTML结构模板 [NEW]**：

```html
<!-- 内容页 -->
<div class="slide" id="slide-N" data-title="[页面标题]">
    <div class="slide-header">
        <span class="slide-title">[页面标题]</span>
    </div>
    <div class="slide-content [布局类型]">
        <h2 class="page-title">[页面标题]</h2>
        
        <!-- 页面导语 -->
        <div class="page-intro">
            <p>[从步骤2.3.1获取的页面导语内容]</p>
        </div>
        
        <!-- 详细内容 -->
        <div class="content-body">
            <!-- 要点1 -->
            <div class="content-point">
                <h3 class="point-title">[要点标题]</h3>
                <div class="point-content">
                    <p class="background-description"><strong>背景描述：</strong>[背景信息]</p>
                    <p class="main-description"><strong>具体内容：</strong>[完整描述]</p>
                    <p class="data-support"><strong>数据支撑：</strong>[相关数据]</p>
                    <p class="impact-analysis"><strong>影响分析：</strong>[影响说明]</p>
                    <p class="conclusion"><strong>结论说明：</strong>[结论]</p>
                </div>
            </div>
            
            <!-- 要点2... -->
        </div>
        
        <!-- 关联说明 -->
        <div class="content-connections">
            <h4>要点关联说明</h4>
            <p>[多个要点之间的逻辑关系说明]</p>
        </div>
        
        <!-- 图表页专用：图表+洞察 -->
        <div class="chart-insight-layout" style="display: none;">
            <div class="chart-container">
                <!-- 图表HTML -->
            </div>
            <div class="insight-panel">
                <div class="insight-section chart-overview">
                    <h4>图表概述</h4>
                    <p>[从步骤2.3.2获取]</p>
                </div>
                <div class="insight-section data-interpretation">
                    <h4>数据解读</h4>
                    <p>[从步骤2.3.2获取]</p>
                </div>
                <div class="insight-section insight-analysis">
                    <h4>洞察分析</h4>
                    <p>[从步骤2.3.2获取]</p>
                </div>
                <div class="insight-section action-recommendations">
                    <h4>行动建议</h4>
                    <p>[从步骤2.3.2获取，推荐]</p>
                </div>
            </div>
        </div>
    </div>
</div>
```

**内容页CSS样式 [NEW]**：

```css
.page-intro {
    background: var(--color-bg-secondary, #F5F7FA);
    padding: var(--spacing-lg);
    border-left: 4px solid var(--color-accent, #F85d42);
    margin-bottom: var(--spacing-xl);
    border-radius: 0 var(--radius-md, 4px) var(--radius-md, 4px) 0;
}

.page-intro p {
    font-size: var(--font-size-body, 14px);
    line-height: var(--line-height-relaxed, 1.6);
    color: var(--color-text, #1A202C);
    margin: 0;
}

.content-point {
    margin-bottom: var(--spacing-xl);
    padding-bottom: var(--spacing-lg);
    border-bottom: 1px solid var(--color-border, #E2E8F0);
}

.content-point:last-child {
    border-bottom: none;
    margin-bottom: 0;
}

.point-title {
    font-size: var(--font-size-h4, 18px);
    font-weight: var(--font-weight-semibold, 600);
    color: var(--color-blue, #556EE6);
    margin-bottom: var(--spacing-md);
}

.point-content p {
    font-size: var(--font-size-body, 14px);
    line-height: var(--line-height-relaxed, 1.6);
    color: var(--color-text, #1A202C);
    margin-bottom: var(--spacing-sm);
}

.point-content strong {
    color: var(--color-accent, #F85d42);
}

.content-connections {
    background: var(--color-bg-secondary, #F5F7FA);
    padding: var(--spacing-lg);
    border-radius: var(--radius-md, 4px);
    margin-top: var(--spacing-xl);
}

.content-connections h4 {
    font-size: var(--font-size-h5, 16px);
    font-weight: var(--font-weight-semibold, 600);
    color: var(--color-gray, #74788d);
    margin-bottom: var(--spacing-md);
}

.content-connections p {
    font-size: var(--font-size-body, 14px);
    line-height: var(--line-height-relaxed, 1.6);
    color: var(--color-text, #1A202C);
}

.chart-insight-layout {
    display: grid;
    grid-template-columns: 55% 45%;
    gap: var(--spacing-xl);
    margin-top: var(--spacing-xl);
}

.chart-insight-layout .chart-container {
    background: var(--color-bg-secondary, #F5F7FA);
    padding: var(--spacing-lg);
    border-radius: var(--radius-lg, 8px);
}
```

**内容丰富化验证清单 [NEW]**：

```
每个内容页生成时，必须验证以下要素：

□ 页面导语
   ├─ □ 包含1-2段核心观点概括
   ├─ □ 说明内容对整体报告的意义
   └─ □ 建立读者阅读预期

□ 要点详细展开
   ├─ □ 每个要点有独立标题
   ├─ □ 每个要点包含背景描述
   ├─ □ 每个要点包含具体内容
   ├─ □ 每个要点包含数据支撑
   ├─ □ 每个要点包含影响分析
   └─ □ 每个要点包含结论说明

□ 图表解释说明（如果页面包含图表）
   ├─ □ 图表概述完整
   ├─ □ 数据解读逐项展开
   ├─ □ 洞察分析提炼到位
   └─ □ 行动建议（推荐）

□ 关联说明
   ├─ □ 揭示要点之间的逻辑关系
   └─ □ 说明内容如何相互支撑

□ 禁止行为检查
   ├─ □ 没有只列出要点标题
   ├─ □ 没有省略解释说明
   ├─ □ 没有删除数据单位
   ├─ □ 没有简化专业术语
   └─ □ 没有压缩完整描述
```

**步骤3.5.7：写入结束页**

```
执行操作：
├─ 写入<div class="slide ending-slide" id="slide-last">
├─ 写入纯色背景样式（从以下颜色随机选取：#556EE6、#F85d42、#34c38f、#50a5f1、#f1b44c、#000000）
├─ 写入"谢谢"标题
├─ 写入品牌标识
└─ 结束页必须隐藏导航栏
```

### 阶段3：JavaScript和结束标签

**步骤3.5.8：写入导航功能JavaScript**

```
执行操作：
├─ 写入导航状态变量
├─ 写入showSlide(n)函数
├─ 写入changeSlide(direction)函数
├─ 写入goToSlide(n)函数
├─ 写入键盘事件监听（←、→、空格、Home、End）
├─ 写入触摸滑动支持
└─ 写入全屏切换功能
```

**步骤3.5.9：写入结束标签**

```
执行操作：
├─ 写入导航按钮（上一页、下一页）
├─ 写入页码计数器
├─ 写入全屏按钮
├─ 写入</div>（关闭presentation-container）
├─ 写入</body>
└─ 写入</html>
```

### HTML代码生成规则

```
生成HTML时，必须遵循以下规则：

1. 布局代码来源：
   ├─ 首选：.ppt_assets/INDEX.md中的布局代码（如存在）
   ├─ 次选：beauty-html/assets/layouts/*.html中的对应布局
   └─ 参考：beauty-html/LAYOUTS_INDEX.md中的布局配置

2. 组件代码来源：
   ├─ 首选：.ppt_assets/INDEX.md中的组件代码（如存在）
   ├─ 次选：beauty-html/assets/components/*.html中的对应组件
   └─ 参考：beauty-html/COMPONENTS_INDEX.md中的组件配置

3. CSS样式来源：
   ├─ beauty-html/mckinsey-design-standards.css
   ├─ beauty-html/assets/styles.css
   └─ beauty-html-reference.md中的样式定义

4. 代码整合步骤：
   a. 分阶段写入本地文件（每个Write操作≤500行）
   b. 复制基础HTML结构
   c. 插入布局容器
   d. 填充组件内容
   e. 应用颜色规范（beauty-html-reference.md）
   f. 添加交互逻辑
```

### 关键要求

1. **分阶段写入**：每个Write操作≤500行，避免过长导致错误
2. 每个内容页必须包含导航栏（封面页除外）
3. 导航栏标题必须与页面标题同步更新
4. 图表必须使用多列布局
5. 必须使用beauty-html-reference.md中定义的配色方案
6. 代码必须参考beauty-html中的示例文件
7. 封面页、章节首页、结束页使用纯色背景（从以下颜色随机选取：#556EE6、#F85d42、#34c38f、#50a5f1、#f1b44c、#000000），白色文字
8. 内容页使用白色背景，黑色文字

### 验证标准

**阶段验证**：
- [ ] 阶段1完成：HTML框架和CSS样式已写入（≤500行）
- [ ] 阶段2完成：所有幻灯片已逐个写入（封面页、目录页、章节首页、内容页、结束页）
- [ ] 阶段3完成：JavaScript和结束标签已写入

**HTML结构验证**：
- [ ] HTML结构完整
- [ ] 布局代码参考了beauty-html示例
- [ ] 组件代码参考了beauty-html示例
- [ ] 如.ppt_assets/INDEX.md存在，已优先使用项目资源

**功能验证**：
- [ ] 导航功能正常
- [ ] 页面切换动画正确
- [ ] 键盘导航正常
- [ ] 触摸滑动支持正常

**规范验证**：
- [ ] 符合best-practices.md规范
- [ ] 配色方案符合beauty-html-reference.md定义
- [ ] 背景颜色规则正确（封面页、章节首页、结束页使用纯色背景，从指定颜色随机选取）
- [ ] 导航栏实时更新功能正常

**内容丰富化验证 [NEW]**：
- [ ] 每个内容页包含页面导语
- [ ] 每个要点包含完整描述（背景、具体内容、数据支撑、影响分析、结论）
- [ ] 每个图表页包含洞察面板
- [ ] 洞察面板包含：图表概述、数据解读、洞察分析
- [ ] 洞察面板包含行动建议（推荐）
- [ ] 内容页包含关联说明（如果适用）
- [ ] 没有省略或压缩关键内容
- [ ] 所有数据点完整保留

---

## 反模式 [NEVER]

1. **NEVER单列布局放图表**
   - 图表必须配合文字解读
   - 使用两列或三列布局

2. **NEVER省略组件匹配步骤**
   - 每个内容元素必须有对应组件
   - 组件选择基于内容特征

3. **NEVER跳过资源读取**
   - 必须读取所有必读资源
   - 禁止用经验替代规范
   - 必须读取beauty-html/LAYOUTS_INDEX.md
   - 必须读取beauty-html/COMPONENTS_INDEX.md

4. **NEVER忽略项目特定资源优先级**
   - 如果.ppt_assets/INDEX.md存在，必须优先使用
   - 禁止跳过项目特定资源直接使用beauty-html版本

5. **NEVER使用AI生成色板**
   - 必须使用beauty-html-reference.md中定义的配色方案
   - 禁止紫色渐变

6. **NEVER页面无导航栏**
   - 内容页必须显示导航栏
   - 导航栏标题实时更新

7. **NEVER直接编写布局代码而不参考示例**
   - 必须参考beauty-html/assets/layouts/*.html
   - 必须参考beauty-html/LAYOUTS_INDEX.md的配置参数

---

## 自由度校准

### 高自由度

- 背景颜色的具体选择（从色系中随机）
- 图表数据标签的格式
- 页面内容的具体措辞（保持原意）

### 中等自由度

- 具体分页位置
- 列表样式的微调
- 组件细节的调整（保持整体结构）

### 低自由度

- 页面结构（必须包含导航栏）
- 布局选择（基于页面类型和beauty-html规则）
- 配色方案（beauty-html-reference.md定义的颜色规范）
- 组件来源（必须参考beauty-html示例）
- 资源优先级（.ppt_assets优先于beauty-html）

---

## 引用系统

- [beauty-html/LAYOUTS_INDEX.md] - 布局索引和配置参数
- [beauty-html/COMPONENTS_INDEX.md] - 组件索引和配置
- [beauty-html-reference.md] - CSS样式和HTML模板
- [beauty-component-guide.md] - 组件选择和图表配置
- [.ppt_assets/INDEX.md] - 项目特定资源（如存在，优先级最高）
- [beauty-step2] - 页面内容清单输入
- [beauty-step4] - 代码审核输出

---

## 步骤 3 完成确认

✅ 步骤3.1：必读资源已读取（包括beauty-html/LAYOUTS_INDEX.md和COMPONENTS_INDEX.md）
✅ 步骤3.2：内容元素已识别
✅ 步骤3.3：HTML组件已匹配（参考beauty-html示例）
✅ 步骤3.4：布局已选择（严格遵循beauty-html规则，优先使用.ppt_assets）
✅ 步骤3.5：HTML已生成（代码参考beauty-html示例文件）

**准备进入步骤4**：请输入"继续"或"next"
