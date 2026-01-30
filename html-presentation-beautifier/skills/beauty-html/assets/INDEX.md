# HTML演示资源索引 / HTML Presentation Resource Index

**版本 / Version**: v2.0.0
**更新日期 / Update Date**: 2026-01-29
**说明 / Description**: HTML演示资源的完整索引，包含组件、布局、模板和指南

---

## 📁 目录结构 / Directory Structure

```
assets/
├── components/                    # 图表和图示组件（24个文件）
│   ├── component-template.html    # 组件标准模版 ⭐
│   ├── chart-examples.html        # 柱状图系列
│   ├── mckinsey-label-bar-example.html  # 麦肯锡标签柱状图
│   ├── pareto-chart-example.html  # 帕累托图
│   ├── polar-chart-example.html   # 极坐标图
│   ├── gauge-chart-example.html   # 仪表盘图
│   ├── pyramid-chart-example.html # 金字塔图
│   ├── funnel-chart-example.html  # 漏斗图
│   ├── slider-chart-example.html  # 滑块图
│   ├── json-html-example.html     # JSON数据表格
│   ├── ansoff-matrix-example.html # 安索夫矩阵
│   ├── competitive-4box-example.html   # 四象限矩阵
│   ├── kano-model-example.html    # KANO模型
│   ├── swot-analysis-example.html # SWOT分析
│   ├── 5w1h-example.html          # 5W1H分析
│   ├── inverted-pyramid-example.html   # 倒金字塔
│   ├── flowchart-example.html     # 流程图
│   ├── mindmap-example.html       # 思维导图
│   ├── timeline-example.html      # 时间线
│   ├── swimlane-example.html      # 泳道图
│   ├── value-stream-example.html  # 价值流图
│   ├── venn-diagram-example.html  # 韦恩图
│   ├── problem-solution-example.html   # 问题-解决方案
│   ├── pros-cons-example.html     # 优缺点对比
│   ├── strategy-roadmap-example.html   # 战略路线图
│   └── market-funnel-example.html # 市场漏斗
│
├── layouts/                       # 页面布局（18个文件）
│   ├── layout-template.html       # 布局标准模版 ⭐
│   ├── presentation-template.html # 完整演示模板
│   ├── template.html              # 基础模板
│   ├── 01-cover-page.html         # 单列封面布局
│   ├── 02-two-column-comparison.html  # 双列对比布局
│   ├── 03-three-column.html       # 三列布局
│   ├── 04-card-grid.html          # 卡片网格布局
│   ├── 05-chart-text.html         # 图表+文本布局
│   ├── 06-data-emphasis.html      # 数据强调布局
│   ├── 07-radar-card-layout.html  # 雷达图+卡片布局
│   ├── 08-table-of-contents.html  # 目录列表布局
│   ├── 09-brand-intro-page.html   # 品牌介绍布局
│   ├── 10-toc-grid-cards.html     # 网格式目录布局
│   ├── 11-chapter-overview.html   # 章节概览布局
│   ├── 12-traffic-analysis.html   # 流量分析布局
│   ├── 13-user-positioning.html   # 用户定位布局
│   ├── 14-user-demand-rating.html # 用户需求评分布局
│   ├── NEW_01-cover-page.html     # 新版封面布局 ⭐
│   ├── NEW_02-content-page-chart-insights.html   # 新版图表+洞察布局 ⭐
│   ├── NEW_03-content-page-text-only.html        # 新版纯文本布局 ⭐
│   ├── NEW_04-content-page-three-charts.html     # 新版三图表布局 ⭐
│   └── NEW_05-chapter-cover.html   # 新版章节封面布局 ⭐
│
├── templates/                     # 模板文件
│   ├── STANDARD_TEMPLATE.html     # 标准模板（完整版）
│   └── template.html              # 基础模板
│
├── guides/                        # 指南和文档
│   ├── README.md                  # 自述文件
│   ├── TEMPLATE_USAGE_GUIDE.md    # 模板使用指南
│   ├── OPTIMIZATION_REPORT.md     # 优化报告
│   ├── CHART_EXAMPLES_INDEX.md    # 图表示例索引
│   ├── HTML_OPTIMIZATION_GUIDE.md # HTML优化指南
│   ├── INSIGHT_VISUALIZATION_GUIDE.md   # 洞察可视化指南
│   ├── JSON_HTML_TEMPLATE_GUIDE.md  # JSON HTML模板指南
│   ├── PYRAMID_CHART_GUIDE.md     # 金字塔图指南
│   ├── 07-radar-card-layout-guide.md   # 雷达图布局指南
│   ├── 08-table-of-contents-guide.md   # 目录布局指南
│   └── pyramid-chart-example.md   # 金字塔图示例
│
├── COMPONENTS_INDEX.md            # 组件索引 ⭐ 重要
├── LAYOUTS_INDEX.md               # 布局索引 ⭐ 重要
├── INDEX.md                       # 本索引文件
├── mckinsey-design-standards.css  # McKinsey设计标准CSS
├── script.js                      # 通用脚本
└── styles.css                     # 通用样式
```

---

## 🚀 快速开始 / Quick Start

### 步骤1：识别内容元素
读取 `COMPONENTS_INDEX.md` 识别所需的组件类型

### 步骤2：匹配HTML组件
根据内容元素匹配对应的HTML组件

### 步骤3：选择页面布局
读取 `LAYOUTS_INDEX.md` 选择合适的页面布局

### 步骤4：生成HTML代码
使用 `layout-template.html` 或 `component-template.html` 生成代码

---

## 📊 组件分类 / Component Categories

### 图表组件 (Charts)
- **C1**: 柱状图系列 (Bar Charts)
- **C2**: 饼图/环形图系列 (Pie/Doughnut Charts)
- **C3**: 特殊图表 (Special Charts)

详情请参考: `COMPONENTS_INDEX.md`

### 图示组件 (Diagrams)
- **D1**: 矩阵/框架图 (Matrix/Framework Diagrams)
- **D2**: 流程图 (Flowcharts)
- **D3**: 对比图 (Comparison Diagrams)

详情请参考: `COMPONENTS_INDEX.md`

---

## 📐 布局分类 / Layout Categories

### 页面布局 (Page Layouts)
- **L1**: 封面页布局 (Cover Page Layouts)
- **L2-L5**: 内容页布局 (Content Page Layouts)
- **L6-L10**: 特殊页面布局 (Special Page Layouts)
- **L11-L17**: 数据展示布局 (Data Display Layouts)
- **NEW系列**: 推荐的新版布局 (Recommended New Layouts)

详情请参考: `LAYOUTS_INDEX.md`

---

## 🎨 设计标准 / Design Standards

### 配色方案
- **主色**: #003366 (McKinsey Blue)
- **强调色**: #F85d42 (McKinsey Red)
- **背景色**: #FFFFFF (White)
- **文本色**: #000000 (Black)

### 字体规范
- **标题**: Arial Bold, 42px/36px/28px
- **正文**: Arial, 20px/18px/16px
- **注释**: Arial, 14px/12px

### 间距标准
- **幻灯片内边距**: 60px
- **列间距**: 40px
- **卡片间距**: 20px

详情请参考: `mckinsey-design-standards.css`

---

## 📝 版本历史 / Version History

| 版本 | 日期 | 更新内容 |
|------|------|---------|
| v2.0.0 | 2026-01-29 | 重构目录结构，分为components/layouts/guides/templates |
| v1.0.0 | 2026-01-28 | 初始版本，混合存放所有文件 |
