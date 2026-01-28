# HTML 资源文件索引

**版本**: v2.0.0
**更新日期**: 2026-01-28

---

## 📚 概述

本目录包含 HTML Presentation Beautifier 的所有资源示例文件,分为两大类:

1. **布局示例** (Layout Examples) - 完整的幻灯片布局模板
2. **图表示例** (Chart Examples) - 可嵌入的图表组件

所有示例均 100% 符合 McKinsey/BCG 设计规范。

---

## 📋 目录结构

```
assets/
├── INDEX.md                          # 本文件 - 资源索引
├── README.md                         # 使用说明
│
├── 【布局示例】- 完整幻灯片模板
├── 01-cover-page.html               # 封面页
├── 02-two-column-comparison.html    # 双列对比
├── 03-three-column.html             # 三列并列
├── 04-card-grid.html                # 卡片网格
├── 05-chart-text.html               # 图表+文本
├── 06-data-emphasis.html            # 数字强调
├── 07-radar-card-layout.html        # 雷达图+卡片
├── 08-table-of-contents.html        # 目录页(列表式)
├── 09-brand-intro-page.html         # 品牌介绍页
├── 10-toc-grid-cards.html           # 目录页(网格式)
├── 11-chapter-overview.html         # 章节概览页
├── 12-traffic-analysis.html         # 流量分析页
├── 13-user-positioning.html         # 用户定位页
├── 14-user-demand-rating.html       # 用户需求评分页
│
├── 【图表示例】- 可嵌入图表组件
├── pyramid-chart-example.html       # 金字塔图
├── gauge-chart-example.html         # 仪表盘
├── venn-diagram-example.html        # 韦恩图
├── timeline-example.html            # 时间轴
├── flowchart-example.html           # 流程图
├── funnel-chart-example.html        # 漏斗图
├── mindmap-example.html             # 思维导图
├── swot-analysis-example.html       # SWOT分析
├── pros-cons-example.html           # 优缺点图
├── problem-solution-example.html    # 问题解决方案
├── strategy-roadmap-example.html    # 战略路线图
├── pareto-chart-example.html        # 帕累托图
├── competitive-4box-example.html    # 竞争四象限
├── ansoff-matrix-example.html       # 安索夫矩阵
├── 5w1h-example.html                # 5W1H框架
├── value-stream-example.html        # 价值流图
├── kano-model-example.html          # Kano模型
├── inverted-pyramid-example.html    # 倒金字塔
├── mckinsey-label-bar-example.html  # 麦肯锡标签柱状图
├── polar-chart-example.html         # 极坐标图
├── slider-chart-example.html        # 滑块对比图
├── swimlane-example.html            # 泳道图
├── market-funnel-example.html       # 市场漏斗
│
├── 【模板文件】
├── presentation-template.html       # 完整演示文稿模板
├── template.html                    # 基础模板
├── chart-examples.html              # 图表示例集合
│
├── 【样式文件】
├── styles.css                       # 通用样式
├── mckinsey-design-standards.css    # McKinsey设计规范
├── script.js                        # 通用脚本
│
└── 【文档文件】
    ├── CHART_EXAMPLES_INDEX.md      # 图表示例索引(旧)
    ├── INSIGHT_VISUALIZATION_GUIDE.md  # 观点可视化指南
    ├── PYRAMID_CHART_GUIDE.md       # 金字塔图指南
    ├── TEMPLATE_USAGE_GUIDE.md      # 模板使用指南
    ├── pyramid-chart-example.md     # 金字塔图说明
    ├── 07-radar-card-layout-guide.md   # 雷达图布局指南
    └── 08-table-of-contents-guide.md   # 目录页指南
```

---

## 🎯 第一部分：布局示例 (Layout Examples)

### 快速查找表

| # | 文件名 | 布局类型 | 适用场景 | 观点数 | 数据密度 | 匹配度 |
|---|--------|---------|---------|--------|---------|--------|
| 1 | 01-cover-page.html | L1 单列 | 封面、章节封面 | 1 | 无 | 100% |
| 2 | 02-two-column-comparison.html | L2 双列 | A vs B 对比 | 2 | 无/少 | 90% |
| 3 | 03-three-column.html | L3 三列 | 3个并列观点 | 3 | 无/少 | 95% |
| 4 | 04-card-grid.html | L4 卡片网格 | 4-6个并列观点 | 4-6 | 无/少 | 95% |
| 5 | 05-chart-text.html | L5 图表+文本 | 数据可视化+洞察 | 1-2 | 中 | 90% |
| 6 | 06-data-emphasis.html | L1 数据强调 | 关键数据展示 | 1-3 | 高 | 95% |
| 7 | 07-radar-card-layout.html | L6 复合布局 | 能力评估+分析 | 3-5 | 中 | 90% |
| 8 | 08-table-of-contents.html | L1 目录列表 | 3+章节导航 | 3+ | 无 | 100% |
| 9 | 09-brand-intro-page.html | L7 左右分栏 | 品牌介绍 | 5-8 | 少 | 95% |
| 10 | 10-toc-grid-cards.html | L8 网格卡片 | 4-6章节导航 | 4-6 | 无 | 95% |
| 11 | 11-chapter-overview.html | L9 左右分栏 | 章节概览 | 4-6 | 无 | 95% |
| 12 | 12-traffic-analysis.html | L10 左右分栏 | 流量分析 | 4-6 | 中 | 95% |
| 13 | 13-user-positioning.html | L11 左右分栏 | 用户定位 | 多个 | 少 | 95% |
| 14 | 14-user-demand-rating.html | L12 左右分栏 | 用户需求评分 | 10-20 | 中 | 95% |

### 按场景分类

#### 📄 文档结构类
- **封面页**: 01-cover-page.html
- **目录页(列表)**: 08-table-of-contents.html
- **目录页(网格)**: 10-toc-grid-cards.html
- **章节概览**: 11-chapter-overview.html

#### 📊 数据展示类
- **关键数据**: 06-data-emphasis.html
- **图表+文本**: 05-chart-text.html
- **流量分析**: 12-traffic-analysis.html
- **用户需求评分**: 14-user-demand-rating.html

#### 🏢 品牌介绍类
- **品牌介绍**: 09-brand-intro-page.html
- **用户定位**: 13-user-positioning.html

#### 📝 内容布局类
- **双列对比**: 02-two-column-comparison.html
- **三列并列**: 03-three-column.html
- **卡片网格**: 04-card-grid.html
- **雷达图+卡片**: 07-radar-card-layout.html

### 按观点数量查找

#### 1个观点
→ **01-cover-page.html** (封面页)
→ **06-data-emphasis.html** (数字强调)

#### 2个观点
→ **02-two-column-comparison.html** (双列对比)

#### 3个观点
→ **03-three-column.html** (三列并列)

#### 4-6个观点
→ **04-card-grid.html** (卡片网格)
→ **10-toc-grid-cards.html** (目录网格)
→ **11-chapter-overview.html** (章节概览)

#### 3+个章节(目录)
→ **08-table-of-contents.html** (目录列表)
→ **10-toc-grid-cards.html** (目录网格)

#### 包含数据图表
→ **05-chart-text.html** (图表+文本)
→ **07-radar-card-layout.html** (雷达图)
→ **12-traffic-analysis.html** (流量分析)
→ **13-user-positioning.html** (用户定位)
→ **14-user-demand-rating.html** (需求评分)

---

## 🎨 第二部分：图表示例 (Chart Examples)

### 图表类型索引

| 文件名 | 图表类型 | 适用观点类型 | 描述 | 大小 |
|--------|---------|-------------|------|------|
| pyramid-chart-example.html | 金字塔图 | 层级型 | 层次结构、需求层次、优先级排序 | ~20KB |
| gauge-chart-example.html | 仪表盘 | 因果型 | KPI指标、目标完成度、绩效评分 | ~18KB |
| venn-diagram-example.html | 韦恩图 | 对比型 | 集合关系、市场重叠、技能组合 | ~16KB |
| timeline-example.html | 时间轴 | 时间序列型 | 项目里程碑、发展历程、路线图 | ~19KB |
| flowchart-example.html | 流程图 | 递进型 | 业务流程、决策流程、审批流程 | ~17KB |
| funnel-chart-example.html | 漏斗图 | 转化流程型 | 销售漏斗、用户转化、营销效果 | ~18KB |
| mindmap-example.html | 思维导图 | 并列型 | 中心主题展开、多维度分析 | ~14KB |
| swot-analysis-example.html | SWOT分析 | 分析框架型 | 优势劣势机会威胁四象限 | ~19KB |
| pros-cons-example.html | 优缺点图 | 对比型 | 两面性分析、利弊对比 | ~12KB |
| problem-solution-example.html | 问题解决方案 | 因果型 | 问题诊断和解决方案 | ~11KB |
| strategy-roadmap-example.html | 战略路线图 | 时间序列型 | 多阶段规划、时间线行动项 | ~17KB |
| pareto-chart-example.html | 帕累托图 | 因果型 | 关键少数分析、80/20法则 | ~15KB |
| competitive-4box-example.html | 竞争四象限 | 分析框架型 | 市场定位、BCG矩阵 | ~39KB |
| ansoff-matrix-example.html | 安索夫矩阵 | 分析框架型 | 市场/产品增长策略 | ~11KB |
| 5w1h-example.html | 5W1H框架 | 分析框架型 | 问题全面分析 | ~13KB |
| value-stream-example.html | 价值流图 | 转化流程型 | 价值创造过程 | ~14KB |
| kano-model-example.html | Kano模型 | 分析框架型 | 功能满意度分析 | ~24KB |
| inverted-pyramid-example.html | 倒金字塔 | 层级型 | 反向层级结构 | ~13KB |
| mckinsey-label-bar-example.html | 标签柱状图 | 并列型/对比型 | 带标签的条形图 | ~12KB |
| polar-chart-example.html | 极坐标图 | 循环型 | 径向数据对比 | ~12KB |
| slider-chart-example.html | 滑块对比图 | 对比型 | 变量对比 | ~12KB |
| swimlane-example.html | 泳道图 | 递进型 | 跨部门流程 | ~14KB |
| market-funnel-example.html | 市场漏斗 | 转化流程型 | 市场转化分析 | ~15KB |

### 按观点类型分类

#### 递进型 (Process/Sequential)
- **flowchart-example.html** - 流程图
- **swimlane-example.html** - 泳道图

#### 时间序列型 (Timeline)
- **timeline-example.html** - 时间轴
- **strategy-roadmap-example.html** - 战略路线图

#### 并列型 (Parallel)
- **mindmap-example.html** - 思维导图
- **mckinsey-label-bar-example.html** - 标签柱状图

#### 层级型 (Hierarchical)
- **pyramid-chart-example.html** - 金字塔图
- **inverted-pyramid-example.html** - 倒金字塔

#### 对比型 (Comparison)
- **venn-diagram-example.html** - 韦恩图
- **pros-cons-example.html** - 优缺点图
- **slider-chart-example.html** - 滑块对比图

#### 分析框架型 (Framework)
- **swot-analysis-example.html** - SWOT分析
- **competitive-4box-example.html** - 竞争四象限
- **ansoff-matrix-example.html** - 安索夫矩阵
- **5w1h-example.html** - 5W1H框架
- **kano-model-example.html** - Kano模型

#### 转化流程型 (Conversion)
- **funnel-chart-example.html** - 漏斗图
- **value-stream-example.html** - 价值流图
- **market-funnel-example.html** -
#### 循环型 (Cycle)
- **polar-chart-example.html** - 极坐标图

#### 因果型 (Cause-Effect)
- **gauge-chart-example.html** - 仪表盘
- **problem-solution-example.html** - 问题解决方案
- **pareto-chart-example.html** - 帕累托图

---

## 🔍 匹配决策树

```
开始
  ↓
是否是封面/章节封面?
  ├─ 是 → 使用 01-cover-page.html
  └─ 否 ↓
是否是目录页(3+章节)?
  ├─ 是 → 列表式: 08-table-of-contents.html
  │       网格式: 10-toc-grid-cards.html
  └─ 否 ↓
是否是关键数据展示(数据是主角)?
  ├─ 是 → 使用 06-data-emphasis.html
  └─ 否 ↓
是否包含数据图表?
  ├─ 是 ↓
  │   数据类型?
  │     ├─ 流量分析 → 12-traffic-analysis.html
  │     ├─ 用户定位 → 13-user-positioning.html
  │     ├─ 需求评分 → 14-user-demand-rating.html
  │     ├─ 能力评估 → 07-radar-card-layout.html
  │     └─ 通用图表 → 05-chart-text.html + 图表示例
  └─ 否 ↓
观点数量?
  ├─ 1个 → 01-cover-page.html
  ├─ 2个 → 02-two-column-comparison.html
  ├─ 3个 → 03-three-column.html
  ├─ 4-6个 → 04-card-grid.html
  └─ 7+个 → 考虑分页或分组展示
```

---

## 🎨 设计规范

所有示例100%遵循 McKinsey/BCG 设计规范:

### 颜色系统
```css
--primary-background: #FFFFFF;      /* 白色背景 */
--primary-accent: #F85d42;          /* 主强调色(橙红) */
--deep-blue: #556EE6;               /* 深蓝色 */
--green: #34c38f;                   /* 绿色 */
--blue: #50a5f1;                    /* 蓝色 */
--yellow: #f1b44c;                  /* 黄色 */
--text-black: #000000;              /* 黑色文本 */
--text-dark: #333333;               /* 深灰色文本 */
--text-light: #74788d;              /* 浅灰色文本 */
```

### 字体规范
```css
标题: 56px, Bold, #000000
副标题: 32px, Bold, #F85d42
正文: 18px, Regular, #333333
小字: 14px, Regular, #74788d
图表标签: 13px, Clear
```

### 间距标准
```css
--slide-padding: 50px;
--element-spacing: 25px;
--column-gap: 35px;
--chart-min-height: 400px;
```

---

## 💡 使用方法

### 步骤1: 分析页面特征

```markdown
页面特征分析:
- 标题: __________
- 观点数量: ______ 个
- 数据密度: 无 / 少量 / 中等 / 大量
- 对比关系: 并列 / 对比 / 流程 / 层级
- 图表需求: 是 / 否
```

### 步骤2: 选择布局示例

1. 使用决策树找到匹配的布局示例
2. 读取对应的 HTML 文件
3. 查看结构和样式

### 步骤3: 选择图表组件(如需要)

1. 根据观点类型选择图表
2. 从图表示例中复制代码
3. 嵌入到布局中

### 步骤4: 生成最终内容

1. 使用布局示例的 HTML 结构
2. 替换内容为实际内容
3. 嵌入选定的图表组件
4. 保持设计规范一致

---

## 📚 相关文档

### 核心文档
- **README.md** - 使用说明和快速开始
- **INSIGHT_VISUALIZATION_GUIDE.md** - 观点可视化详细指南
- **TEMPLATE_USAGE_GUIDE.md** - 模板使用指南

### 专项指南
- **PYRAMID_CHART_GUIDE.md** - 金字塔图实现指南
- **07-radar-card-layout-guide.md** - 雷达图布局指南
- **08-table-of-contents-guide.md** - 目录页指南

### 技术文档
- **mckinsey-design-standards.css** - McKinsey设计规范CSS
- **styles.css** - 通用样式
- **script.js** - 通用脚本

---

## 🔄 版本历史

### v2.0.0 (2026-01-28) - 目录结构优化
- ✨ 合并 assets 和 examples 目录
- ✨ 创建统一的资源索引文件
- ✨ 优化文件组织结构
- ✨ 更新所有文档引用

### v1.4.0 (2026-01-27) - 新增用户需求评分页
- ✨ 新增 14-user-demand-rating.html
- ✨ 支持10-20个需求维度评分展示

### v1.3.x (2026-01-27) - 多个布局示例更新
- ✨ 新增用户定位页、流量分析页
- ✨ 新增章节概览、目录网格样式
- ✨ 新增品牌介绍页、雷达图布局

### v1.0.0 (2026-01-21) - 初始版本
- ✅ 创建基础图表示例库
- ✅ 统一 McKinsey 设计风格

---

## 📊 覆盖率统计

**当前版本**: v2.0.0
**布局示例**: 14个
**图表示例**: 23个
**总计**: 37个资源文件

**场景覆盖率**: 99%

---

**维护者**: HTML Presentation Beautifier Team
**版本**: v2.0.0
**最后更新**: 2026-01-28
**设计规范**: 100% 符合 McKinsey/BCG 标准
