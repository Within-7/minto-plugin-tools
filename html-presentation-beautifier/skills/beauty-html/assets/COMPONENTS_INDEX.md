# HTML组件索引 / HTML Component Index

**版本 / Version**: v1.1.0
**更新日期 / Update Date**: 2026-01-29
**用途 / Purpose**: 元素组件索引，供步骤3.2（内容元素识别）和步骤3.3（组件匹配）使用

---

## ⭐ 标准模版 / Standard Template

**参考文件**: `components/component-template.html`

创建新组件时，请参考标准模版，确保代码结构和样式一致。

### 模版包含内容
- HTML结构（容器、头部、内容、底部）
- CSS样式（容器、标题、内容、列表）
- JavaScript（Chart.js配置示例）

### 使用方法
1. 复制 `component-template.html`
2. 将 `[component-name]` 替换为实际组件名称
3. 将 `[canvas-id]` 替换为唯一的Canvas ID
4. 将 `[chart-type]` 替换为实际的图表类型
5. 修改数据和标签内容

---

## 📊 图表组件 / Chart Components

### C1. 柱状图系列 / Bar Chart Series

#### C1.1 **chart-examples.html**
基础柱状图示例 - 多类型柱状图展示

**组件类型**: bar
**Chart.js配置**:
```javascript
{
  type: 'bar',
  data: datasets[],
  options: {
    responsive: true,
    maintainAspectRatio: false
  }
}
```

**CSS类名**:
- `.chart-container`
- `.bar-chart`
- `.legend`

**用途**: 单系列柱状图、多系列分组柱状图、堆叠柱状图

---

#### C1.2 **mckinsey-label-bar-example.html**
麦肯锡标签柱状图 - 带数据标签的柱状图

**组件类型**: bar (with labels)
**Chart.js配置**:
```javascript
{
  type: 'bar',
  data: {
    labels: ['A', 'B', 'C', 'D', 'E'],
    datasets: [{
      data: [120, 190, 80, 250, 170],
      label: '数据系列'
    }]
  },
  options: {
    plugins: {
      datalabels: {
        anchor: 'end',
        align: 'top'
      }
    }
  }
}
```

**CSS类名**:
- `.chart-container`
- `.label-bar-chart`
- `.data-label`

**用途**: 需要在柱子上显示具体数值的场景

---

#### C1.3 **pareto-chart-example.html**
帕累托图 - 柱状图+折线图组合

**组件类型**: mixed (bar + line)
**Chart.js配置**:
```javascript
{
  type: 'bar',
  data: {
    labels: ['问题A', '问题B', '问题C', '问题D', '问题E'],
    datasets: [
      {
        type: 'bar',
        data: [45, 28, 15, 8, 4],
        label: '频次'
      },
      {
        type: 'line',
        data: [45, 73, 88, 96, 100],
: '累计百分比        label',
        yAxisID: 'y1'
      }
    ]
  },
  options: {
    scales: {
      y: { beginAtZero: true },
      y1: { position: 'right', max: 100 }
    }
  }
}
```

**CSS类名**:
- `.chart-container`
- `.pareto-chart`
- `.cumulative-line`

**用途**: 二八法则分析、问题优先级排序

---

## 📝 图文列表组件 / Graphic List Components ⭐ 新增

### G1. 图标+文字列表 / Icon + Text List

#### 文件: `graphic-list-components.html` ⭐

**组件类型**: graphic-list (icon-text)
**实现方式**: HTML + CSS Flexbox
**HTML结构**:
```html
<div class="icon-text-list">
  <div class="icon-text-item">
    <div class="graphic-icon">
      <svg>...</svg>
    </div>
    <div class="graphic-content">
      <h4 class="graphic-title">标题</h4>
      <p class="graphic-description">描述文字</p>
    </div>
  </div>
  ...
</div>
```

**CSS类名**:
- `.icon-text-list`
- `.icon-text-item`
- `.graphic-icon`
- `.graphic-content`
- `.graphic-title`
- `.graphic-description`

**用途**: 要点列表、优势展示、特性说明

**设计规范**:
- ✅ 左侧图标48×48px，背景#F8F9FA
- ✅ 右侧内容包含标题+描述
- ✅ 左侧边框4px强调色（#F85d42）
- ✅ 卡片式布局，圆角4px

---

### G2. 数字+文字列表 / Number + Text List

#### 文件: `graphic-list-components.html` ⭐

**组件类型**: graphic-list (number-text)
**实现方式**: HTML + CSS Flexbox
**HTML结构**:
```html
<div class="number-text-list">
  <div class="number-text-item">
    <div class="graphic-number">01</div>
    <div class="graphic-content">
      <h4 class="graphic-title">标题</h4>
      <p class="graphic-description">描述文字</p>
    </div>
  </div>
  ...
</div>
```

**CSS类名**:
- `.number-text-list`
- `.number-text-item`
- `.graphic-number`
- `.graphic-content`
- `.graphic-title`
- `.graphic-description`

**用途**: 步骤列表、排名展示、编号要点

**设计规范**:
- ✅ 左侧圆形数字徽章，40×40px
- ✅ 数字样式：蓝色背景（#556EE6），白色文字
- ✅ 底部边框分隔线
- ✅ 垂直列表布局

---

### G3. 卡片式列表 / Card List

#### 文件: `graphic-list-components.html` ⭐

**组件类型**: graphic-list (card)
**实现方式**: HTML + CSS Grid
**HTML结构**:
```html
<div class="card-list">
  <div class="graphic-card">
    <div class="card-header">
      <span class="card-badge">标签</span>
      <h4 class="card-title">标题</h4>
    </div>
    <div class="card-body">
      <p class="card-description">描述文字</p>
    </div>
    <div class="card-footer">
      <span class="card-meta">元信息</span>
    </div>
  </div>
  ...
</div>
```

**CSS类名**:
- `.card-list`
- `.graphic-card`
- `.card-header`
- `.card-badge`
- `.card-title`
- `.card-body`
- `.card-description`
- `.card-footer`
- `.card-meta`

**用途**: 特性展示、优势对比、项目列表

**设计规范**:
- ✅ 2列网格布局
- ✅ 卡片圆角8px，悬停阴影效果
- ✅ 顶部标签（#F85d42背景）
- ✅ 底部元信息区域（#F8F9FA背景）

---

### 图文列表转换规则 ⭐ 新增

```
原始列表 → 转换后格式
├─ 无序列表 (<ul><li>...)</ul>)
│   → 图标+文字列表 或 数字+文字列表
│
├─ 编号列表 (<ol><li>...)</ol>)
│   → 数字+文字列表
│
├─ 要点列表 (.key-insights)
│   → 图标+文字列表
│
├─ 洞察列表 (.bullet-list)
│   → 卡片式列表 或 图标+文字列表
│
└─ 目录列表 (.toc-list)
    → 卡片式列表（2列网格）
```

### 列表转换验证 ⭐ 新增

- [ ] 所有文字列表都已转换为图文格式
- [ ] 图文列表使用卡片或媒体对象样式
- [ ] 无传统的HTML list格式（<ul><li>）
- [ ] 图文列表布局合理（2列或垂直列表）
- [ ] 图文列表样式与整体设计一致

---

### C2. 饼图/环形图系列 / Pie/Doughnut Chart Series

#### C2.1 **polar-chart-example.html**
极坐标图（饼图变体）

**组件类型**: polarArea
**Chart.js配置**:
```javascript
{
  type: 'polarArea',
  data: {
    labels: ['维度A', '维度B', '维度C', '维度D', '维度E'],
    datasets: [{
      data: [65, 59, 80, 81, 56],
      backgroundColor: ['#003366', '#0066cc', '#4d94ff', '#80b3ff', '#b3d1ff']
    }]
  }
}
```

**CSS类名**:
- `.chart-container`
- `.polar-chart`

**用途**: 多维度评估、能力分析、竞争力雷达

---

#### C2.2 **gauge-chart-example.html**
仪表盘图 - 目标达成率/进度展示

**组件类型**: doughnut (simulated gauge)
**Chart.js配置**:
```javascript
{
  type: 'doughnut',
  data: {
    labels: ['已完成', '剩余'],
    datasets: [{
      data: [75, 25],
      backgroundColor: ['#F85d42', '#e0e0e0'],
      circumference: 180,
      rotation: 270
    }]
  },
  options: {
    circumference: 180,
    rotation: 270,
    plugins: {
      centerText: '75%'
    }
  }
}
```

**CSS类名**:
- `.chart-container`
- `.gauge-chart`
- `.gauge-center-text`

**用途**: KPI展示、目标达成率、进度跟踪

---

### C3. 特殊图表系列 / Special Chart Series

#### C3.1 **pyramid-chart-example.html**
金字塔图 - 层级结构/漏斗分析

**组件类型**: horizontalBar (simulated pyramid)
**Chart.js配置**:
```javascript
{
  type: 'bar',
  data: {
    labels: ['战略层', '范围层', '结构层', '框架层', '表现层'],
    datasets: [{
      data: [100, 80, 60, 40, 20],
      backgroundColor: [
        '#003366', '#1a4d8c', '#3366b3', '#4d80cc', '#6699cc'
      ]
    }]
  },
  options: {
    indexAxis: 'y'
  }
}
```

**CSS类名**:
- `.chart-container`
- `.pyramid-chart`
- `.pyramid-level`

**用途**: 战略层级、用户需求层次、转化漏斗

---

#### C3.2 **funnel-chart-example.html**
漏斗图 - 转化率分析

**组件类型**: custom (funnel visualization)
**实现方式**: HTML + CSS (非Chart.js原生)
**HTML结构**:
```html
<div class="funnel-container">
  <div class="funnel-level" style="--width: 100%">阶段1: 1000用户</div>
  <div class="funnel-level" style="--width: 80%">阶段2: 800用户</div>
  <div class="funnel-level" style="--width: 60%">阶段3: 600用户</div>
  <div class="funnel-level" style="--width: 40%">阶段4: 400用户</div>
  <div class="funnel-level" style="--width: 20%">阶段5: 200用户</div>
</div>
```

**CSS类名**:
- `.funnel-container`
- `.funnel-level`
- `.funnel-conversion-rate`

**用途**: 销售漏斗、用户转化分析、流程优化

---

#### C3.3 **slider-chart-example.html**
滑块图 - 区间选择/范围展示

**组件类型**: bar (with range slider)
**实现方式**: Chart.js + 自定义插件
**CSS类名**:
- `.chart-container`
- `.slider-chart`
- `.range-slider`

**用途**: 预算范围、目标区间、时间范围选择

---

## 📈 图示组件 / Diagram Components

### D1. 矩阵/框架图系列 / Matrix/Framework Diagrams

#### D1.1 **competitive-4box-example.html**
四象限矩阵 - 竞争分析

**实现方式**: HTML + CSS Grid
**HTML结构**:
```html
<div class="matrix-4box">
  <div class="quadrant q1">第一象限（高重要性/高紧急）</div>
  <div class="quadrant q2">第二象限（高重要性/低紧急）</div>
  <div class="quadrant q3">第三象限（低重要性/高紧急）</div>
  <div class="quadrant q4">第四象限（低重要性/低紧急）</div>
</div>
```

**CSS类名**:
- `.matrix-4box`
- `.quadrant`
- `.matrix-axis`

**用途**: 优先级矩阵、竞争定位、时间管理

---

#### D1.2 **kano-model-example.html**
KANO模型 - 需求分类

**实现方式**: HTML + CSS Grid
**HTML结构**:
```html
<div class="kano-model">
  <div class="kano-quadrant performance">绩效需求</div>
  <div class="kano-quadrant basic">基本需求</div>
  <div class="kano-quadrant excitement">兴奋需求</div>
  <div class="kano-quadrant indifferent">无差异需求</div>
</div>
```

**CSS类名**:
- `.kano-model`
- `.kano-quadrant`
- `.kano-curve`

**用途**: 需求分析、用户满意度研究、产品规划

---

#### D1.3 **ansoff-matrix-example.html**
安索夫矩阵 - 增长策略

**实现方式**: HTML + CSS Grid
**HTML结构**:
```html
<div class="ansoff-matrix">
  <div class="ansoff-cell market-penetration">市场渗透</div>
  <div class="ansoff-cell market-development">市场开发</div>
  <div class="ansoff-cell product-development">产品开发</div>
  <div class="ansoff-cell diversification">多元化</div>
</div>
```

**CSS类名**:
- `.ansoff-matrix`
- `.ansoff-cell`
- `.ansoff-label`

**用途**: 战略规划、业务增长分析

---

#### D1.4 **swot-analysis-example.html**
SWOT分析 - 战略规划

**实现方式**: HTML + CSS Grid
**HTML结构**:
```html
<div class="swot-container">
  <div class="swot-quadrant strengths">优势 S</div>
  <div class="swot-quadrant weaknesses">劣势 W</div>
  <div class="swot-quadrant opportunities">机会 O</div>
  <div class="swot-quadrant threats">威胁 T</div>
</div>
```

**CSS类名**:
- `.swot-container`
- `.swot-quadrant`
- `.swot-title`

**用途**: 战略分析、风险评估、商业规划

---

#### D1.5 **5w1h-example.html**
5W1H分析 - 问题分析

**实现方式**: HTML + CSS Flexbox
**HTML结构**:
```html
<div class="five-w-one-h">
  <div class="wh-item what">What（什么）</div>
  <div class="wh-item why">Why（为什么）</div>
  <div class="wh-item who">Who（谁）</div>
  <div class="wh-item when">When（何时）</div>
  <div class="wh-item where">Where（何地）</div>
  <div class="wh-item how">How（如何）</div>
</div>
```

**CSS类名**:
- `.five-w-one-h`
- `.wh-item`

**用途**: 问题分析、流程优化、决策制定

---

#### D1.6 **inverted-pyramid-example.html**
倒金字塔 - 内容优先级

**实现方式**: HTML + CSS
**HTML结构**:
```html
<div class="inverted-pyramid">
  <div class="pyramid-level level-1">核心信息（最重要）</div>
  <div class="pyramid-level level-2">支持信息</div>
  <div class="pyramid-level level-3">背景信息</div>
  <div class="pyramid-level level-4">详细信息（最不重要）</div>
</div>
```

**CSS类名**:
- `.inverted-pyramid`
- `.pyramid-level`

**用途**: 新闻写作、内容优先级、信息架构

---

### D2. 流程图系列 / Flowchart Components

#### D2.1 **flowchart-example.html**
流程图 - 业务流程

**实现方式**: HTML + CSS
**HTML结构**:
```html
<div class="flowchart">
  <div class="flow-node start">开始</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-node process">处理步骤</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-node decision">判断</div>
  <div class="flow-arrow">↓</div>
  <div class="flow-node end">结束</div>
</div>
```

**CSS类名**:
- `.flowchart`
- `.flow-node`
- `.flow-arrow`
- `.flow-connector`

**用途**: 业务流程、工作流程、决策流程

---

#### D2.2 **mindmap-example.html**
思维导图 - 创意发散

**实现方式**: HTML + CSS
**HTML结构**:
```html
<div class="mindmap">
  <div class="mindmap-center">中心主题</div>
  <div class="mindmap-branch">
    <div class="mindmap-node">分支1</div>
    <div class="mindmap-subnode">子节点1.1</div>
    <div class="mindmap-subnode">子节点1.2</div>
  </div>
</div>
```

**CSS类名**:
- `.mindmap`
- `.mindmap-center`
- `.mindmap-branch`
- `.mindmap-node`

**用途**: 头脑风暴、创意规划、项目分解

---

#### D2.3 **timeline-example.html**
时间线 - 时间序列

**实现方式**: HTML + CSS
**HTML结构**:
```html
<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-marker"></div>
    <div class="timeline-content">2024 Q1 - 阶段1</div>
  </div>
  <div class="timeline-item">
    <div class="timeline-marker"></div>
    <div class="timeline-content">2024 Q2 - 阶段2</div>
  </div>
</div>
```

**CSS类名**:
- `.timeline`
- `.timeline-item`
- `.timeline-marker`
- `.timeline-content`

**用途**: 项目时间线、历史回顾、里程碑规划

---

#### D2.4 **swimlane-example.html**
泳道图 - 角色分工

**实现方式**: HTML + CSS Grid
**HTML结构**:
```html
<div class="swimlane-container">
  <div class="swimlane-header">
    <div class="swimlane-role">角色A</div>
    <div class="swimlane-role">角色B</div>
    <div class="swimlane-role">角色C</div>
  </div>
  <div class="swimlane-body">
    <div class="swimlane-cell">任务A1</div>
    <div class="swimlane-cell">任务B1</div>
    <div class="swimlane-cell">任务C1</div>
  </div>
</div>
```

**CSS类名**:
- `.swimlane-container`
- `.swimlane-header`
- `.swimlane-cell`

**用途**: 跨部门协作、业务流程、角色职责

---

#### D2.5 **value-stream-example.html**
价值流图 - 流程优化

**实现方式**: HTML + CSS
**HTML结构**:
```html
<div class="value-stream">
  <div class="vs-node process">加工</div>
  <div class="vs-node inspection">检验</div>
  <div class="vs-node delay">等待</div>
  <div class="vs-node transport">运输</div>
</div>
```

**CSS类名**:
- `.value-stream`
- `.vs-node`
- `.vs-takt-time`

**用途**: 精益生产、流程优化、效率分析

---

### D3. 对比图系列 / Comparison Diagrams

#### D3.1 **pros-cons-example.html**
优缺点对比

**实现方式**: HTML + CSS Flexbox
**HTML结构**:
```html
<div class="pros-cons">
  <div class="pros-column">
    <h3>优点</h3>
    <ul>
      <li>优点1</li>
      <li>优点2</li>
    </ul>
  </div>
  <div class="cons-column">
    <h3>缺点</h3>
    <ul>
      <li>缺点1</li>
      <li>缺点2</li>
    </ul>
  </div>
</div>
```

**CSS类名**:
- `.pros-cons`
- `.pros-column`
- `.cons-column`

**用途**: 方案对比、决策分析、利弊评估

---

#### D3.2 **problem-solution-example.html**
问题-解决方案

**实现方式**: HTML + CSS
**HTML结构**:
```html
<div class="problem-solution">
  <div class="problem-box">
    <h3>问题</h3>
    <p>问题描述</p>
  </div>
  <div class="solution-box">
    <h3>方案</h3>
    <p>方案描述</p>
  </div>
</div>
```

**CSS类名**:
- `.problem-solution`
- `.problem-box`
- `.solution-box`

**用途**: 商业提案、咨询汇报、解决方案展示

---

#### D3.3 **venn-diagram-example.html**
韦恩图 - 交集分析

**实现方式**: HTML + CSS (SVG-based)
**HTML结构**:
```html
<div class="venn-diagram">
  <svg>
    <circle class="venn-set set-a" cx="100" cy="100" r="80"/>
    <circle class="venn-set set-b" cx="180" cy="100" r="80"/>
    <circle class="venn-set set-c" cx="140" cy="170" r="80"/>
  </svg>
</div>
```

**CSS类名**:
- `.venn-diagram`
- `.venn-set`
- `.venn-intersection`

**用途**: 交集分析、共性分析、分类整理

---

#### D3.4 **strategy-roadmap-example.html**
战略路线图

**实现方式**: HTML + CSS
**HTML结构**:
```html
<div class="strategy-roadmap">
  <div class="roadmap-phase phase-1">
    <h3>第一阶段</h3>
    <p>短期目标</p>
  </div>
  <div class="roadmap-phase phase-2">
    <h3>第二阶段</h3>
    <p>中期目标</p>
  </div>
  <div class="roadmap-phase phase-3">
    <h3>第三阶段</h3>
    <p>长期目标</p>
  </div>
</div>
```

**CSS类名**:
- `.strategy-roadmap`
- `.roadmap-phase`

**用途**: 战略规划、路线图、目标分解

---

#### D3.5 **market-funnel-example.html**
市场漏斗 - 营销分析

**实现方式**: HTML + CSS
**HTML结构**:
```html
<div class="market-funnel">
  <div class="funnel-stage awareness">认知阶段</div>
  <div class="funnel-stage interest">兴趣阶段</div>
  <div class="funnel-stage consideration">考虑阶段</div>
  <div class="funnel-stage conversion">转化阶段</div>
</div>
```

**CSS类名**:
- `.market-funnel`
- `.funnel-stage`

**用途**: 营销漏斗、用户旅程、销售预测

---

## 📋 表格组件 / Table Components

### T1. 数据表格 / Data Tables

#### T1.1 **json-html-example.html**
JSON驱动数据表格

**实现方式**: JavaScript渲染HTML
**CSS类名**:
- `.data-table`
- `.table-header`
- `.table-row`
- `.table-cell`

**用途**: 动态数据展示、API数据渲染

---

## 🔧 组件选择决策树 / Component Selection Decision Tree

```
开始
  ↓
需要什么类型的可视化？
  ├─ 图表（数据展示）
  │   ├─ 比较数据 → 柱状图 (C1)
  │   ├─ 占比数据 → 饼图/环形图 (C2)
  │   ├─ 趋势数据 → 折线图 (C1)
  │   ├─ 层级结构 → 金字塔图 (C3.1)
  │   ├─ 转化分析 → 漏斗图 (C3.2)
  │   ├─ 进度展示 → 仪表盘 (C2.2)
  │   └─ 多维评估 → 极坐标图 (C2.1)
  │
  ├─ 矩阵/框架
  │   ├─ 优先级排序 → 四象限 (D1.1)
  │   ├─ 需求分析 → KANO模型 (D1.2)
  │   ├─ 增长策略 → 安索夫矩阵 (D1.3)
  │   ├─ 战略分析 → SWOT (D1.4)
  │   └─ 问题分析 → 5W1H (D1.5)
  │
  ├─ 流程图
  │   ├─ 业务流程 → 流程图 (D2.1)
  │   ├─ 创意发散 → 思维导图 (D2.2)
  │   ├─ 时间序列 → 时间线 (D2.3)
  │   ├─ 角色分工 → 泳道图 (D2.4)
  │   └─ 流程优化 → 价值流图 (D2.5)
  │
  └─ 对比图
      ├─ 优缺点 → 优缺点对比 (D3.1)
      ├─ 问题方案 → 问题-解决方案 (D3.2)
      ├─ 交集分析 → 韦恩图 (D3.3)
      ├─ 战略规划 → 战略路线图 (D3.4)
      └─ 营销分析 → 市场漏斗 (D3.5)
```

---

## 📖 使用说明 / Usage Instructions

### 步骤3.2：内容元素识别
在识别图表元素时，参考本索引中的组件类型：

```
页面 X：[页面标题]

#### 图表元素
- [x] 柱状图：1个
  → 参考组件：C1.1 chart-examples.html (基础柱状图)
  
- [x] 漏斗图：1个
  → 参考组件：C3.2 funnel-chart-example.html (漏斗图)
```

### 步骤3.3：组件匹配
在匹配HTML组件时，参考本索引中的CSS类名和配置：

```
#### 图表组件
5. **柱状图** → `.chart-container` + Chart.js
   - 参考文件: `components/chart-examples.html`
   - Chart.js类型: 'bar'
   - 数据点: 5个
   - CSS类名: .chart-container, .bar-chart
```

### 优先级规则
如果项目存在 `.ppt_assets/components/` 目录：
1. 先检查 `.ppt_assets/components/` 中是否有匹配的组件文件
2. 如果存在，使用项目本地的组件文件
3. 如果不存在，使用 `beauty-html/assets/components/` 中的标准组件

---

## 📁 文件位置 / File Locations

**标准组件库**: `beauty-html/assets/components/`
**项目组件库**: `.ppt_assets/components/` (如果存在)
