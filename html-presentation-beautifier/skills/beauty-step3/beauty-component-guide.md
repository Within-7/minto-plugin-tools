# 组件选择指南

本文档提供幻灯片演示中HTML组件的选择指导，包括图表组件、图示组件和表格组件的详细说明及选择决策树。

**重要参考**：
- 本文档是beauty-html skill的简化版参考
- 完整组件索引和配置请参考 `beauty-html/COMPONENTS_INDEX.md`
- 详细组件示例请参考 `beauty-html/assets/components/*.html`
- 布局配置请参考 `beauty-html/LAYOUTS_INDEX.md`
- 如果项目存在 `.ppt_assets/INDEX.md`，必须优先使用其中的组件示例

---

## 1 图表组件

### 1.1 图表类型概览

| 组件 | 代码类名 | 适用场景 | 数据特征 |
|-----|---------|---------|---------|
| 柱状图 | bar-chart | 类别比较、数量对比 | 离散类别数据 |
| 折线图 | line-chart | 趋势变化、时间序列 | 连续数据 |
| 饼图 | pie-chart | 占比分析、比例展示 | 部分与整体 |
| 雷达图 | radar-chart | 多维评估、能力分析 | 多维度数据 |
| 漏斗图 | funnel-chart | 流程转化、筛选过程 | 逐步递减 |
| 仪表盘 | gauge-chart | KPI达成、目标进度 | 单值进度 |

### 1.2 柱状图（bar-chart）

**适用场景**：类别比较、数量对比、排名展示。

**数据特征**：
- 离散类别数据（产品类型、地区、年份等）
- 需要比较不同类别的数值大小
- 数据点数量在3-10个之间

**子类型**：
- 单系列柱状图：单一类别数据
- 分组柱状图：多系列并排对比
- 堆叠柱状图：部分与整体关系

**HTML结构**：

```html
<div class="chart-container bar-chart">
    <div class="chart-title">图表标题</div>
    <div class="bar-chart-body">
        <div class="bar-item">
            <div class="bar" style="height: 80%; background-color: var(--color-primary);">
                <span class="bar-value">80%</span>
            </div>
            <div class="bar-label">类别A</div>
        </div>
        <div class="bar-item">
            <div class="bar" style="height: 65%; background-color: var(--color-accent-primary);">
                <span class="bar-value">65%</span>
            </div>
            <div class="bar-label">类别B</div>
        </div>
        <div class="bar-item">
            <div class="bar" style="height: 90%; background-color: var(--color-success);">
                <span class="bar-value">90%</span>
            </div>
            <div class="bar-label">类别C</div>
        </div>
    </div>
</div>
```

**CSS样式**：

```css
.bar-chart {
    background: var(--color-bg-secondary);
    border-radius: 8px;
    padding: var(--spacing-lg);
}

.bar-chart-body {
    display: flex;
    align-items: flex-end;
    justify-content: space-around;
    height: 250px;
    padding-top: var(--spacing-lg);
    border-bottom: 2px solid var(--color-border);
}

.bar-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    flex: 1;
    max-width: 80px;
}

.bar {
    width: 48px;
    border-radius: 4px 4px 0 0;
    position: relative;
    min-height: 20px;
}

.bar-value {
    position: absolute;
    top: -28px;
    left: 50%;
    transform: translateX(-50%);
    font-size: var(--font-size-body-secondary);
    font-weight: var(--font-weight-semibold);
}

.bar-label {
    margin-top: var(--spacing-sm);
    font-size: var(--font-size-caption);
    color: var(--color-text-secondary);
    text-align: center;
}
```

### 1.3 折线图（line-chart）

**适用场景**：趋势变化、时间序列、增长率展示。

**数据特征**：
- 连续数据（时间序列、进度百分比等）
- 需要展示数据的变化趋势
- 数据点数量在3-12个之间

**子类型**：
- 单线图：单一数据序列
- 多线对比图：多条曲线对比

**HTML结构**：

```html
<div class="chart-container line-chart">
    <div class="chart-title">图表标题</div>
    <div class="line-chart-body">
        <svg viewBox="0 0 600 300" class="line-chart-svg">
            <!-- X轴 -->
            <line x1="50" y1="250" x2="550" y2="250" stroke="#E2E8F0" stroke-width="2"/>
            <!-- Y轴 -->
            <line x1="50" y1="250" x2="50" y2="30" stroke="#E2E8F0" stroke-width="2"/>
            <!-- 数据线 -->
            <polyline 
                fill="none" 
                stroke="#003366" 
                stroke-width="3"
                points="50,200 150,180 250,150 350,100 450,80 550,50"/>
            <!-- 数据点 -->
            <circle cx="50" cy="200" r="6" fill="#003366"/>
            <circle cx="150" cy="180" r="6" fill="#003366"/>
            <circle cx="250" cy="150" r="6" fill="#003366"/>
            <circle cx="350" cy="100" r="6" fill="#003366"/>
            <circle cx="450" cy="80" r="6" fill="#003366"/>
            <circle cx="550" cy="50" r="6" fill="#003366"/>
        </svg>
        <div class="chart-legend">
            <span class="legend-item"><span class="legend-color" style="background: #003366;"></span>2024年</span>
        </div>
    </div>
</div>
```

### 1.4 饼图/环形图（pie-chart）

**适用场景**：占比分析、比例展示、部分与整体。

**数据特征**：
- 部分与整体的关系
- 分类数量在2-6个之间
- 各部分占比之和为100%

**HTML结构**：

```html
<div class="chart-container pie-chart">
    <div class="chart-title">图表标题</div>
    <div class="pie-chart-body">
        <div class="pie-wrapper">
            <svg viewBox="0 0 200 200" class="pie-chart-svg">
                <circle cx="100" cy="100" r="80" fill="transparent" stroke="#003366" stroke-width="40" stroke-dasharray="125.6 502.6" transform="rotate(-90 100 100)"/>
                <circle cx="100" cy="100" r="80" fill="transparent" stroke="#F85d42" stroke-width="40" stroke-dasharray="100.5 502.6" stroke-dashoffset="-125.6" transform="rotate(-90 100 100)"/>
                <circle cx="100" cy="100" r="80" fill="transparent" stroke="#38A169" stroke-width="40" stroke-dasharray="75.4 502.6" stroke-dashoffset="-226.1" transform="rotate(-90 100 100)"/>
                <circle cx="100" cy="100" r="60" fill="white"/>
            </svg>
            <div class="pie-center-text">100%</div>
        </div>
        <div class="pie-legend">
            <div class="legend-row">
                <span class="legend-dot" style="background: #003366;"></span>
                <span class="legend-label">类别A</span>
                <span class="legend-value">25%</span>
            </div>
            <div class="legend-row">
                <span class="legend-dot" style="background: #F85d42;"></span>
                <span class="legend-label">类别B</span>
                <span class="legend-value">20%</span>
            </div>
            <div class="legend-row">
                <span class="legend-dot" style="background: #38A169;"></span>
                <span class="legend-label">类别C</span>
                <span class="legend-value">15%</span>
            </div>
        </div>
    </div>
</div>
```

### 1.5 雷达图（radar-chart）

**适用场景**：多维评估、能力分析、对比展示。

**数据特征**：
- 多维度数据（3-6个维度）
- 需要评估各维度的相对表现
- 适合展示均衡性或偏向性

### 1.6 漏斗图（funnel-chart）

**适用场景**：流程转化、筛选过程、阶段展示。

**数据特征**：
- 逐步递减的数据
- 明确的阶段划分
- 需要展示转化率

---

## 2 图示组件

### 2.1 图示类型概览

| 组件 | 代码类名 | 适用场景 |
|-----|---------|---------|
| 流程图 | flow-chart | 步骤流程、过程展示 |
| -chart | 循环图 | cycle循环过程、持续改进 |
| 金字塔图 | pyramid-chart | 层次结构、递进关系 |
| 对比图 | comparison-chart | 并列对比、A/B选择 |
| 时间线 | timeline | 时间序列、历史回顾 |

### 2.2 流程图（flow-chart）

**适用场景**：步骤流程、过程展示、任务分解。

**HTML结构**：

```html
<div class="diagram-container flow-chart">
    <div class="flow-step">
        <div class="step-number">1</div>
        <div class="step-content">
            <h4>步骤一</h4>
            <p>步骤描述内容</p>
        </div>
    </div>
    <div class="flow-connector">→</div>
    <div class="flow-step">
        <div class="step-number">2</div>
        <div class="step-content">
            <h4>步骤二</h4>
            <p>步骤描述内容</p>
        </div>
    </div>
    <div class="flow-connector">→</div>
    <div class="flow-step">
        <div class="step-number">3</div>
        <div class="step-content">
            <h4>步骤三</h4>
            <p>步骤描述内容</p>
        </div>
    </div>
</div>
```

### 2.3 对比图（comparison-chart）

**适用场景**：方案对比、优劣势分析、A/B选择。

**HTML结构**：

```html
<div class="diagram-container comparison-chart">
    <div class="comparison-column pros">
        <h4 class="comparison-title">方案A</h4>
        <ul class="comparison-list">
            <li class="pro">优势点1</li>
            <li class="pro">优势点2</li>
            <li class="pro">优势点3</li>
        </ul>
    </div>
    <div class="comparison-column cons">
        <h4 class="comparison-title">方案B</h4>
        <ul class="comparison-list">
            <li class="con">劣势点1</li>
            <li class="con">劣势点2</li>
            <li class="con">劣势点3</li>
        </ul>
    </div>
</div>
```

---

## 3 表格组件

### 3.1 表格类型概览

| 组件 | 代码类名 | 适用场景 | 列数 |
|-----|---------|---------|------|
| 简单表格 | simple-table | 基础数据展示 | ≤5列 |
| 对比表格 | comparison-table | 多维度对比 | ≥3列 |
| 复杂表格 | complex-table | 详细数据展示 | >5列 |

### 3.2 简单表格（simple-table）

**HTML结构**：

```html
<div class="table-container simple-table">
    <table>
        <thead>
            <tr>
                <th>列标题1</th>
                <th>列标题2</th>
                <th>列标题3</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>数据1-1</td>
                <td>数据1-2</td>
                <td>数据1-3</td>
            </tr>
            <tr>
                <td>数据2-1</td>
                <td>数据2-2</td>
                <td>数据2-3</td>
            </tr>
        </tbody>
    </table>
</div>
```

**CSS样式**：

```css
.simple-table table {
    width: 100%;
    border-collapse: collapse;
    background: var(--color-bg);
}

.simple-table th,
.simple-table td {
    padding: var(--spacing-md);
    text-align: left;
    border-bottom: 1px solid var(--color-border);
}

.simple-table th {
    background: var(--color-bg-secondary);
    font-weight: var(--font-weight-semibold);
    color: var(--color-text-primary);
}

.simple-table tr:hover {
    background: var(--color-bg-secondary);
}
```

### 3.3 对比表格（comparison-table）

**适用场景**：特性对比、方案对比、多维度评估。

**HTML结构**：

```html
<div class="table-container comparison-table">
    <table>
        <thead>
            <tr>
                <th>特性</th>
                <th>方案A</th>
                <th>方案B</th>
                <th>方案C</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>特性1</td>
                <td class="highlight">✓ 支持</td>
                <td>✗ 不支持</td>
                <td>◐ 部分</td>
            </tr>
            <tr>
                <td>特性2</td>
                <td>◐ 部分</td>
                <td class="highlight">✓ 支持</td>
                <td>✓ 支持</td>
            </tr>
        </tbody>
    </table>
</div>
```

---

## 4 组件选择决策树

### 4.1 图表选择决策树

```
需要展示数据可视化？
├─ 否 → 使用文本或列表组件
└─ 是 ↓
    
    数据类型是？
    ├─ 类别比较（产品、地区、年份）→ 柱状图
    ├─ 时间趋势（增长、下降、波动）→ 折线图
    ├─ 占比比例（市场份额、分配）→ 饼图
    ├─ 多维评估（能力、均衡性）→ 雷达图
    └─ 流程转化（步骤、阶段）→ 漏斗图
```

### 4.2 布局选择决策树

```
图表数量？
├─ 0个 → 单列布局（纯文本）
├─ 1个 → 两列布局（图表+洞察）
├─ 2个 → 三列布局（并排对比）
└─ ≥3个 → 卡片网格或分页展示
```

### 4.3 表格选择决策树

```
数据是结构化的？
├─ 否 → 使用列表或图表
└─ 是 ↓
    
    目的？
    ├─ 基础数据展示 → 简单表格
    ├─ 多方案对比 → 对比表格
    └─ 复杂数据 → 考虑拆分为多个简单表格
```

---

## 5 组件配置参数

### 5.1 图表通用配置

```javascript
const chartConfig = {
    // 颜色配置 - 使用beauty-html-reference.md中定义的配色方案
    colors: [
        '#F85d42',  // 主要强调色
        '#556EE6',  // 深蓝色
        '#34c38f',  // 绿色
        '#50a5f1',  // 蓝色
        '#f1b44c',  // 黄色
        '#74788d',  // 辅助色
    ],
    
    // 尺寸配置
    sizes: {
        small: { width: 200, height: 200 },
        medium: { width: 300, height: 250 },
        large: { width: 400, height: 300 },
    },
    
    // 动画配置
    animation: {
        duration: 500,
        easing: 'ease-in-out',
    },
};
```

### 5.2 表格配置

```javascript
const tableConfig = {
    // 列配置
    columns: [
        { key: 'col1', title: '列1', width: '25%' },
        { key: 'col2', title: '列2', width: '25%' },
        { key: 'col3', title: '列3', width: '50%' },
    ],
    
    // 样式配置
    styles: {
        striped: true,
        hoverable: true,
        bordered: false,
    },
};
```

---

## 6 常见问题

### Q1：何时使用柱状图而非折线图？

当数据是离散的类别（如产品类型、地区）时使用柱状图；当数据是连续的序列（如时间）时使用折线图。

### Q2：饼图可以超过6部分吗？

不建议。饼图的最佳实践是展示2-6个部分，超过6个部分会使图表难以阅读。建议将小部分合并为"其他"类别。

### Q3：图表必须使用多列布局吗？

是的。图表必须配合文字解读，使用两列布局（图表+洞察）或三列布局（多图表并排）。禁止在单列布局中单独放置图表。

### Q4：表格数据太多怎么办？

考虑以下方案：
- 拆分多个表格，每页一个
- 使用摘要表格+详细附录
- 使用图表替代部分数据展示
- 保留关键数据，详细数据放入附录

### Q5：如何选择合适的颜色？

必须使用beauty-html-reference.md中定义的配色方案。颜色选择应基于：
- 数据的重要程度（重要数据用深色）
- 数据的类别区分（不同类别用不同颜色）
- 整体的视觉平衡（避免颜色过于集中）

---

## 7 布局与组件组合示例

### 示例1：业绩趋势分析

```
布局：两列布局
├─ 左列：折线图（展示12个月销售趋势）
└─ 右列：要点列表（关键洞察）
    ├─ 洞察1：Q4销售额增长30%
    ├─ 洞察2：华南地区表现最佳
    └─ 洞察3：电子产品增速最快
```

### 示例2：市场份额对比

```
布局：三列布局
├─ 左列：饼图A公司（25%）
├─ 中列：饼图B公司（20%）
└─ 右列：其他品牌合计（55%）
```

### 示例3：产品功能对比

```
布局：表格布局
├─ 行1：特性A - ✓ / ✗ / ◐
├─ 行2：特性B - ✓ / ✓ / ✗
├─ 行3：特性C - ✗ / ✓ / ✓
└─ 行4：特性D - ✓ / ✓ / ◐
```

### 示例4：项目流程展示

```
布局：流程图布局
├─ 步骤1：需求分析（卡片）
├─ 箭头 →
├─ 步骤2：方案设计（卡片）
├─ 箭头 →
└─ 步骤3：实施执行（卡片）
```
