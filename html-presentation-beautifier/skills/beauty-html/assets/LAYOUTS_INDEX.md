# HTML布局索引 / HTML Layout Index

**版本 / Version**: v1.1.0
**更新日期 / Update Date**: 2026-01-29
**用途 / Purpose**: 页面布局索引，供步骤3.4（布局选择）使用

---

## ⭐ 标准模版 / Standard Template

**参考文件**: `layouts/layout-template.html`

创建新布局时，请参考标准模版，确保代码结构和样式一致。

### 模版包含内容
- **单列布局**: 适用于纯文本内容
- **双列布局**: 适用于图表+文本对比
- **三列布局**: 适用于三个并列内容
- **卡片网格布局**: 适用于4个并列观点

### 模版特性
- 响应式设计（桌面/平板/移动）
- 统一的CSS类名命名规范
- 完整的Chart.js集成示例
- 关键洞察样式

### 使用方法
1. 复制 `layout-template.html`
2. 根据内容类型选择合适的布局结构
3. 将 `[layout-type]` 替换为实际布局类型
4. 修改标题、内容和数据

### 重要设计规范
- ✅ 图表页面必须使用两列或三列布局
- ✅ 图表宽度100%（在容器内）
- ✅ 每页内容不超过8个要点

---

## 📐 布局类型总览 / Layout Type Overview

本索引包含两大类布局：

1. **NEW系列（推荐）/ NEW Series (Recommended)** ⭐
   - 100%符合McKinsey设计规范
   - 基于STANDARD_TEMPLATE.html标准模板
   - 包含完整的设计规范检查清单

2. **传统系列 / Traditional Series**
   - 原有布局示例
   - 部分符合McKinsey设计规范

---

## 🏠 封面页布局 / Cover Page Layouts

### L1. 单列封面布局 / Single Column Cover

**文件**: `layouts/01-cover-page.html`
**NEW系列**: `layouts/NEW_01-cover-page.html` ⭐
**增强版**: `layouts/NEW_06-cover-page-with-bg.html` ⭐ 新增

**增强版布局结构**:
```html
<div class="slide cover-slide" id="slide-1">
  <div class="cover-content">
    <h1 class="main-title">主标题</h1>
    <div class="decorative-line"></div>
    <p class="subtitle">副标题</p>
    <div class="meta-info">
      <span>作者</span> | <span>日期</span>
    </div>
  </div>
</div>
```

**新增CSS类名**:
- `.decorative-line`

**增强功能** ⭐ 新增:
- 支持动态背景颜色（从McKinsey标准色系随机选择）
- 支持深色/浅色背景自动切换文字颜色
- 确保对比度≥4.5:1

**背景颜色选择** ⭐ 新增:
```javascript
const backgroundColors = [
    { bg: '#F8F9FA', text: '#000000' },
    { bg: '#E9ECEF', text: '#000000' },
    { bg: '#DEE2E6', text: '#000000' },
    { bg: '#FFFFFF', text: '#000000' },
    { bg: '#003366', text: '#FFFFFF' },
    { bg: '#1A365D', text: '#FFFFFF' },
    { bg: '#2C5282', text: '#FFFFFF' },
    { bg: '#F85d42', text: '#FFFFFF' },
    { bg: '#38A169', text: '#FFFFFF' }
];
```

**CSS类名**:
- `.cover-slide`
- `.cover-content`
- `.main-title`
- `.subtitle`
- `.meta-info`

**适用内容**:
- 演示文稿封面
- 报告封面
- 标题页

**设计规范**:
- ✅ 64px粗体黑色主标题
- ✅ 36px粗体McKinsey红色副标题
- ✅ 垂直居中布局
- ✅ 充足白空间

---

### L14. 章节封面布局 / Chapter Cover

**文件**: `layouts/NEW_05-chapter-cover.html` ⭐
**增强版**: `layouts/NEW_07-chapter-cover-with-overview.html` ⭐ 新增

**增强版布局结构**:
```html
<div class="slide section-slide" id="slide-2">
  <div class="section-header">
    <span class="section-number">一</span>
    <h1 class="section-title">章节标题</h1>
  </div>
  <div class="section-description">
    <p>章节描述文字</p>
  </div>
  <div class="section-overview">
    <h3 class="overview-title">本章内容</h3>
    <ul class="overview-list">
      <li class="overview-item">
        <span class="overview-page-num">03</span>
        <span class="overview-title-text">子标题1</span>
      </li>
      <li class="overview-item">
        <span class="overview-page-num">04</span>
        <span class="overview-title-text">子标题2</span>
      </li>
    </ul>
  </div>
</div>
```

**CSS类名**:
- `.section-slide`
- `.section-header`
- `.section-number`
- `.section-title`
- `.section-description`
- `.section-overview` ⭐ 新增
- `.overview-title` ⭐ 新增
- `.overview-list` ⭐ 新增
- `.overview-item` ⭐ 新增
- `.overview-page-num` ⭐ 新增
- `.overview-title-text` ⭐ 新增

**增强功能** ⭐ 新增:
- 支持动态背景颜色
- 章节概览列表（列出本章所有子标题）
- 2列网格布局的章节概览
- 页码信息显示

**章节概览规范** ⭐ 新增:
- 每个章节首页必须包含章节概览列表
- 章节概览必须列出当前章节的所有子标题
- 章节概览必须包含每个子标题对应的页码
- 章节概览必须使用2列网格布局

**适用内容**:
- 章节分隔页
- 主题转换页
- 章节首页

**设计规范**:
- ✅ 120px粗体McKinsey蓝色章节编号
- ✅ 48px粗体黑色章节标题
- ✅ 20px常规灰色章节描述
- ✅ 居中对齐，垂直居中

---

## 📝 内容页布局 / Content Page Layouts

### L2. 双列对比布局 / Two Column Comparison

**文件**: `layouts/02-two-column-comparison.html`

**布局结构**:
```html
<div class="slide content-slide">
  <div class="two-column-layout">
    <div class="column column-left">
      <h2 class="column-title">左侧标题</h2>
      <div class="column-content">左侧内容</div>
    </div>
    <div class="column column-right">
      <h2 class="column-title">右侧标题</h2>
      <div class="column-content">右侧内容</div>
    </div>
  </div>
</div>
```

**CSS类名**:
- `.content-slide`
- `.two-column-layout`
- `.column`
- `.column-left`
- `.column-right`
- `.column-title`
- `.column-content`

**列宽配置**:
- 默认: `grid-template-columns: 1fr 1fr`
- 可选: `grid-template-columns: 60% 40%`
- 可选: `grid-template-columns: 40% 60%`

**适用内容**:
- 左右对比分析
- 方案对比
- 优缺点并排

**设计规范**:
- ✅ 两列等宽或按需比例
- ✅ 列间距 40px
- ✅ 相同类型内容对齐

---

### L3. 三列布局 / Three Column Layout

**文件**: `layouts/03-three-column.html`

**布局结构**:
```html
<div class="slide content-slide">
  <div class="three-column-layout">
    <div class="column column-1">
      <h3>列1标题</h3>
      <p>列1内容</p>
    </div>
    <div class="column column-2">
      <h3>列2标题</h3>
      <p>列2内容</p>
    </div>
    <div class="column column-3">
      <h3>列3标题</h3>
      <p>列3内容</p>
    </div>
  </div>
</div>
```

**CSS类名**:
- `.three-column-layout`
- `.column` (×3)
- `.column-1`, `.column-2`, `.column-3`

**列宽配置**:
- 默认: `grid-template-columns: 1fr 1fr 1fr`
- 可选: `grid-template-columns: 33.33% 33.33% 33.33%`

**适用内容**:
- 三个并列观点
- 三方对比
- 分类展示

**设计规范**:
- ✅ 三列等宽
- ✅ 列间距 30px
- ✅ 每列内容类型一致

---

### L13. 三列图表对比布局 / Three Chart Comparison

**文件**: `layouts/NEW_04-content-page-three-charts.html` ⭐

**布局结构**:
```html
<div class="slide content-slide">
  <div class="three-chart-layout">
    <div class="chart-column">
      <div class="chart-container">
        <canvas id="chart-1"></canvas>
      </div>
      <p class="chart-caption">图表1说明</p>
    </div>
    <div class="chart-column">
      <div class="chart-container">
        <canvas id="chart-2"></canvas>
      </div>
      <p class="chart-caption">图表2说明</p>
    </div>
    <div class="chart-column">
      <div class="chart-container">
        <canvas id="chart-3"></canvas>
      </div>
      <p class="chart-caption">图表3说明</p>
    </div>
  </div>
</div>
```

**CSS类名**:
- `.three-chart-layout`
- `.chart-column`
- `.chart-container`
- `.chart-caption`

**列宽配置**:
- `grid-template-columns: 1fr 1fr 1fr` (每列33.33%)

**适用内容**:
- 三个图表并排对比
- 区域对比分析
- 产品线对比

**设计规范**:
- ✅ 每个图表占33%宽度
- ✅ 图表容器 min-height: 350px
- ✅ 每个图表下方有简短说明

---

### L4. 卡片网格布局 / Card Grid Layout

**文件**: `layouts/04-card-grid.html`

**布局结构**:
```html
<div class="slide content-slide">
  <div class="card-grid">
    <div class="highlight-card">
      <h3>卡片1标题</h3>
      <p>卡片1内容</p>
    </div>
    <div class="highlight-card">
      <h3>卡片2标题</h3>
      <p>卡片2内容</p>
    </div>
    <div class="highlight-card">
      <h3>卡片3标题</h3>
      <p>卡片3内容</p>
    </div>
    <div class="highlight-card">
      <h3>卡片4标题</h3>
      <p>卡片4内容</p>
    </div>
  </div>
</div>
```

**CSS类名**:
- `.card-grid`
- `.highlight-card`
- `.card-title`
- `.card-content`

**网格配置**:
- 默认: `grid-template-columns: repeat(2, 1fr)` (2×2)
- 可选: `grid-template-columns: repeat(3, 1fr)` (3列)
- 可选: `grid-template-columns: repeat(4, 1fr)` (4列)

**卡片样式**:
- 白色背景
- 左边框 4px solid #F85d42
- 内边距 30px

**适用内容**:
- 4-6个并列观点
- 关键发现展示
- 特性/优势卡片

**设计规范**:
- ✅ 卡片内容≤3要点
- ✅ 相同类型卡片风格一致
- ✅ 卡片间距 20px

---

### L5. 图表+文本布局 / Chart + Text Layout ⚠️ 重要

**文件**: `layouts/05-chart-text.html`
**NEW系列**: `layouts/NEW_02-content-page-chart-insights.html` ⭐

**布局结构**:
```html
<div class="slide content-slide">
  <div class="chart-text-layout">
    <div class="chart-area">
      <div class="chart-container">
        <canvas id="main-chart"></canvas>
      </div>
    </div>
    <div class="text-area">
      <div class="key-insights">
        <h3>关键洞察</h3>
        <ul>
          <li>洞察1：...</li>
          <li>洞察2：...</li>
          <li>洞察3：...</li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

**CSS类名**:
- `.chart-text-layout`
- `.chart-area`
- `.text-area`
- `.chart-container`
- `.key-insights`

**布局模式**:

**模式1（推荐）: 图表左 + 洞察右**
```
grid-template-columns: 55% 45%
图表占55%，洞察占45%
```

**模式2: 图表左 + 数据摘要右**
```
grid-template-columns: 50% 50%
图表占50%，数据框占50%
```

**模式3: 三列并排图表**
```
grid-template-columns: 33.33% 33.33% 33.33%
每个图表占33.33%（见L13）
```

**⚠️ CRITICAL设计规范**:
- ✅ 图表使用两列或三列布局
- ✅ **禁止单列布局**
- ✅ 图表宽度100%（在容器内）
- ✅ Chart.js: responsive: true, maintainAspectRatio: false
- ✅ 图表容器 min-height: 400px
- ✅ 每页洞察≤8个要点

**适用内容**:
- 数据展示+分析
- 图表+关键洞察
- 市场数据可视化

---

### L6. 雷达图+卡片布局 / Radar + Cards Layout

**文件**: `layouts/07-radar-card-layout.html`

**布局结构**:
```html
<div class="slide content-slide">
  <div class="radar-card-layout">
    <div class="radar-area">
      <div class="chart-container">
        <canvas id="radar-chart"></canvas>
      </div>
    </div>
    <div class="cards-area">
      <div class="analysis-card">
        <h4>能力A</h4>
        <p>评分: 8/10</p>
      </div>
      <div class="analysis-card">
        <h4>能力B</h4>
        <p>评分: 6/10</p>
      </div>
    </div>
  </div>
</div>
```

**CSS类名**:
- `.radar-card-layout`
- `.radar-area`
- `.cards-area`
- `.analysis-card`

**布局配置**:
- 默认: `grid-template-columns: 60% 40%`

**适用内容**:
- 能力评估+分析
- 竞争力雷达
- 多维对比

---

### L7. 目录列表布局 / Table of Contents List

**文件**: `layouts/08-table-of-contents.html`

**布局结构**:
```html
<div class="slide toc-slide">
  <div class="toc-header">
    <h2>目录</h2>
  </div>
  <div class="toc-list">
    <div class="toc-item">
      <span class="toc-number">一</span>
      <span class="toc-title">章节标题</span>
    </div>
    <div class="toc-item">
      <span class="toc-number">二</span>
      <span class="toc-title">章节标题</span>
    </div>
  </div>
</div>
```

**CSS类名**:
- `.toc-slide`
- `.toc-header`
- `.toc-list`
- `.toc-item`
- `.toc-number`
- `.toc-title`

**适用内容**:
- 目录页（列表式）
- 议程页
- 导航页

---

### L8. 品牌介绍布局 / Brand Introduction

**文件**: `layouts/09-brand-intro-page.html`

**布局结构**:
```html
<div class="slide brand-slide">
  <div class="brand-container">
    <div class="brand-logo">
      <img src="logo.png" alt="品牌Logo">
    </div>
    <div class="brand-info">
      <h1>品牌名称</h1>
      <p>品牌定位描述</p>
    </div>
  </div>
</div>
```

**CSS类名**:
- `.brand-slide`
- `.brand-container`
- `.brand-logo`
- `.brand-info`

**适用内容**:
- 品牌介绍
- 公司介绍
- 产品介绍

---

### L9. 网格式目录布局 / Grid TOC Layout

**文件**: `layouts/10-toc-grid-cards.html`

**布局结构**:
```html
<div class="slide toc-grid-slide">
  <div class="toc-grid">
    <div class="toc-card">
      <span class="toc-card-number">一</span>
      <span class="toc-card-title">章节1</span>
    </div>
    <div class="toc-card">
      <span class="toc-card-number">二</span>
      <span class="toc-card-title">章节2</span>
    </div>
    <div class="toc-card">
      <span class="toc-card-number">三</span>
      <span class="toc-card-title">章节3</span>
    </div>
    <div class="toc-card">
      <span class="toc-card-number">四</span>
      <span class="toc-card-title">章节4</span>
    </div>
  </div>
</div>
```

**CSS类名**:
- `.toc-grid-slide`
- `.toc-grid`
- `.toc-card`
- `.toc-card-number`
- `.toc-card-title`

**网格配置**:
- `grid-template-columns: repeat(2, 1fr)` (2×2)
- `grid-template-columns: repeat(3, 1fr)` (3列)

**适用内容**:
- 网格式目录（4-6章节）
- 导航卡片
- 章节索引

---

### L10. 章节概览布局 / Chapter Overview

**文件**: `layouts/11-chapter-overview.html`

**布局结构**:
```html
<div class="slide overview-slide">
  <div class="chapter-overview">
    <div class="overview-header">
      <h2>章节概览</h2>
    </div>
    <div class="sub-chapter-list">
      <div class="sub-chapter">
        <span class="sub-chapter-number">1.1</span>
        <span class="sub-chapter-title">小节标题</span>
      </div>
    </div>
  </div>
</div>
```

**CSS类名**:
- `.overview-slide`
- `.chapter-overview`
- `.sub-chapter-list`
- `.sub-chapter`

**适用内容**:
- 章节概览
- 小节列表
- 内容导航

---

### L11. 流量分析布局 / Traffic Analysis

**文件**: `layouts/12-traffic-analysis.html`

**布局结构**:
```html
<div class="slide traffic-slide">
  <div class="traffic-analysis-layout">
    <div class="traffic-chart">
      <div class="chart-container">
        <canvas id="traffic-chart"></canvas>
      </div>
    </div>
    <div class="traffic-insights">
      <div class="insight-card">
        <h4>流量来源</h4>
        <ul>
          <li>直接访问: 40%</li>
          <li>搜索引擎: 35%</li>
          <li>社交媒体: 25%</li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

**CSS类名**:
- `.traffic-slide`
- `.traffic-analysis-layout`
- `.traffic-chart`
- `.traffic-insights`
- `.insight-card`

**布局配置**:
- 默认: `grid-template-columns: 65% 35%`

**适用内容**:
- 流量分析
- 用户来源分析
- 渠道效果

---

### L12. 用户定位布局 / User Positioning

**文件**: `layouts/13-user-positioning.html`

**布局结构**:
```html
<div class="slide positioning-slide">
  <div class="user-positioning-layout">
    <div class="positioning-matrix">
      <div class="matrix-quadrant q1">高价值/高活跃</div>
      <div class="matrix-quadrant q2">高价值/低活跃</div>
      <div class="matrix-quadrant q3">低价值/高活跃</div>
      <div class="matrix-quadrant q4">低价值/低活跃</div>
    </div>
    <div class="user-segments">
      <div class="segment-card">用户群1</div>
      <div class="segment-card">用户群2</div>
    </div>
  </div>
</div>
```

**CSS类名**:
- `.positioning-slide`
- `.user-positioning-layout`
- `.positioning-matrix`
- `.matrix-quadrant`
- `.user-segments`
- `.segment-card`

**适用内容**:
- 用户定位
- 用户分群
- 市场细分

---

### L15. 用户需求评分布局 / User Demand Rating

**文件**: `layouts/14-user-demand-rating.html`

**布局结构**:
```html
<div class="slide demand-rating-slide">
  <div class="demand-rating-layout">
    <div class="rating-header">
      <h2>用户需求评分</h2>
    </div>
    <div class="rating-bars">
      <div class="rating-bar">
        <span class="rating-label">需求A</span>
        <div class="rating-bar-container">
          <div class="rating-bar-fill" style="width: 80%"></div>
        </div>
        <span class="rating-value">8.0</span>
      </div>
    </div>
  </div>
</div>
```

**CSS类名**:
- `.demand-rating-slide`
- `.demand-rating-layout`
- `.rating-bars`
- `.rating-bar`
- `.rating-bar-container`
- `.rating-bar-fill`

**适用内容**:
- 用户需求评分
- 需求优先级
- 评分可视化（10-20个维度）

---

### L16. 纯文本单列布局 / Text Only Single Column

**文件**: `layouts/NEW_03-content-page-text-only.html` ⭐

**布局结构**:
```html
<div class="slide content-slide">
  <div class="text-only-layout">
    <div class="text-content">
      <div class="key-point">
        <strong>要点1标题：</strong>要点1描述文字
      </div>
      <div class="key-point">
        <strong>要点2标题：</strong>要点2描述文字
      </div>
      <div class="key-point">
        <strong>要点3标题：</strong>要点3描述文字
      </div>
    </div>
  </div>
</div>
```

**CSS类名**:
- `.text-only-layout`
- `.text-content`
- `.key-point`

**⚠️ CRITICAL设计规范**:
- ✅ 每页最多8个要点（本示例6个）
- ✅ 如果内容>8个要点，必须分页
- ✅ 使用序号标题（一、二、三...）
- ✅ 要点格式：<strong>标题</strong>: 描述（最多150字）

**适用内容**:
- 战略要点展示
- 行动计划列表
- 建议总结

---

### L17. 数据强调布局 / Data Emphasis

**文件**: `layouts/06-data-emphasis.html`

**布局结构**:
```html
<div class="slide content-slide">
  <div class="data-emphasis-layout">
    <div class="data-card">
      <div class="data-value">85%</div>
      <div class="data-label">关键指标</div>
    </div>
    <div class="data-card">
      <div class="data-value">$1.2M</div>
      <div class="data-label">收入</div>
    </div>
  </div>
</div>
```

**CSS类名**:
- `.data-emphasis-layout`
- `.data-card`
- `.data-value`
- `.data-label`

**卡片样式**:
- 白色背景
- 左边框 4px solid #F85d42
- 内边距 30px

**适用内容**:
- KPI展示
- 关键数据强调
- 数字指标

---

## 📐 布局选择决策树 / Layout Selection Decision Tree

```
开始
  ↓
页面类型？
  ├─ 封面页 → L1 单列封面布局
  │
  ├─ 章节封面 → L14 章节封面布局
  │
  ├─ 目录页
  │   ├─ 列表式 → L7 目录列表布局
  │   └─ 网格式 → L9 网格式目录布局
  │
  ├─ 内容页 - 纯文本
  │   └─ L16 纯文本单列布局 (≤8要点)
  │
  ├─ 内容页 - 数据展示
  │   ├─ 1个图表 + 洞察 → L5 图表+文本布局 (2列)
  │   ├─ 2-3个图表并排 → L13 三列图表对比
  │   ├─ 雷达图 + 分析 → L6 雷达图+卡片布局
  │   └─ 强调数据/KPI → L17 数据强调布局
  │
  ├─ 内容页 - 观点并列
  │   ├─ 2个观点 → L2 双列对比布局
  │   ├─ 3个观点 → L3 三列布局
  │   └─ 4-6个观点 → L4 卡片网格布局
  │
  └─ 特殊页面
      ├─ 品牌介绍 → L8 品牌介绍布局
      ├─ 章节概览 → L10 章节概览布局
      ├─ 流量分析 → L11 流量分析布局
      ├─ 用户定位 → L12 用户定位布局
      └─ 需求评分 → L15 用户需求评分布局
```

---

## 📐 布局配置速查表 / Layout Configuration Quick Reference

| 布局 | 文件 | 列数 | 列宽比例 | 适用场景 |
|------|------|------|---------|----------|
| L1 | 01-cover-page.html | 1 | 100% | 封面页 |
| L2 | 02-two-column-comparison.html | 2 | 1:1, 60:40, 40:60 | 左右对比 |
| L3 | 03-three-column.html | 3 | 1:1:1 | 三方并列 |
| L4 | 04-card-grid.html | 2-4 | 等宽 | 卡片网格 |
| L5 | 05-chart-text.html | 2 | 55:45, 50:50 | 图表+洞察 |
| L6 | 07-radar-card-layout.html | 2 | 60:40 | 雷达图+分析 |
| L7 | 08-table-of-contents.html | 1 | 100% | 目录列表 |
| L9 | 10-toc-grid-cards.html | 2-3 | 等宽 | 网格式目录 |
| L13 | NEW_04-*.html | 3 | 33.33%×3 | 三图表对比 |
| L14 | NEW_05-*.html | 1 | 100% | 章节封面 |
| L16 | NEW_03-*.html | 1 | 100% | 纯文本内容 |
| L17 | 06-data-emphasis.html | 2-4 | 等宽 | 数据强调 |

---

## ⚠️ 重要设计规范 / Critical Design Standards

### 图表页面布局规则

**✅ 必须使用两列或三列布局**
- 图表页面（L5, L6, L11, L13）**禁止使用单列布局**
- 图表占50-60%，配套内容占40-50%

**✅ 图表宽度100%**
- 所有图表在容器内宽度100%
- Chart.js配置: `responsive: true, maintainAspectRatio: false`

**✅ 要点数量限制**
- 每页内容页**最多8个要点**（L16）
- 如果内容>8个要点，必须分页

### 响应式设计规则

- 默认桌面端布局
- 平板端：自动调整为单列
- 移动端：自动调整为单列

---

## 📖 使用说明 / Usage Instructions

### 步骤3.4：布局选择
在选择布局时，参考本索引中的布局类型：

```
页面 X：[页面标题]

#### 布局选择分析
- 组件需求：1个柱状图 + 3个洞察要点
- 决策路径：图表页面 → 1图表+洞察 → L5 图表+文本布局

#### 布局选择
- **布局类型**: L5 图表+文本布局（2列）
- **参考文件**: `layouts/NEW_02-content-page-chart-insights.html`
- **布局模式**: 模式1（图表55% + 洞察45%）
```

### 优先级规则
如果项目存在 `.ppt_assets/layouts/` 目录：
1. 先检查 `.ppt_assets/layouts/` 中是否有匹配的布局文件
2. 如果存在，使用项目本地的布局文件
3. 如果不存在，使用 `beauty-html/assets/layouts/` 中的标准布局

---

## 📁 文件位置 / File Locations

**标准布局库**: `beauty-html/assets/layouts/`
**项目布局库**: `.ppt_assets/layouts/` (如果存在)
