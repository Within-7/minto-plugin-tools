# 图表选择指南

**目的**：为麦肯锡风格演示文稿提供图表和可视化选择的决策树和策略。

**设计规范引用**：本指南遵循《麦肯锡设计系统》规范，核心配色方案如下：

| 颜色类型 | 十六进制值 | 英文名称 | 用途 |
|---------|-----------|----------|------|
| 主背景色 | #FFFFFF | White | 幻灯片背景 |
| 标题栏背景 | #000000 | Black | 顶部标题栏 |
| 主要强调色 | #F85d42 | Orange | 关键高亮、强调数据 |
| 辅助色 | #74788d | Gray | 次要文本、说明文字 |
| 深蓝色 | #556EE6 | Deep Blue | 图表、主要数据 |
| 绿色 | #34c38f | Green | 成功指标、正向数据 |
| 蓝色 | #50a5f1 | Blue | 中性强调、次要数据 |
| 黄色 | #f1b44c | Yellow | 警告、注意事项、对比数据 |

**图表配色优先级**：深蓝色（#556EE6）→ 橙色（#F85d42）→ 绿色（#34c38f）→ 蓝色（#50a5f1）→ 黄色（#f1b44c）

---

## 关键规则（必须遵守）

**布局要求**：所有图表必须使用两列或三列布局，严禁单列布局。

| 布局类型 | 比例分配 | 适用场景 |
|---------|---------|---------|
| 两列布局（图表+洞察） | 左列50%-60%图表，右列40%-50%洞察 | 单图表展示配合数据分析 |
| 三列布局（多图表对比） | 三列等宽各33% | 多图表并排对比分析 |
| 混合布局 | 根据内容动态调整 | 复杂数据展示 |

**核心原则**：

- **图表+洞察模式**：左列放置图表（50%-60%），右列放置关键洞察、数据总结或结论
- **多图表模式**：三列并排展示对比图表，每列33%宽度
- **内容完整性**：100%保留所有数据点，不得简化
- **布局优先原则**：先确定布局，再分配内容
- **禁止行为**：单列布局展示图表、图表无上下文居中显示

**令牌限制处理**：

- 数据过大或达到令牌限制时，自动使用延续机制
- 通过分段加载确保100%内容保留
- **严格禁止**：跳过内容或使用摘要来节省令牌

---

## 快速决策树

```
开始：分析内容类型
│
├─ 数值型数据 ──→ 进入数据图表选择流程
│   │ 提示：必须使用两列布局（图表+洞察）
│   │
│   ├─ 需要展示趋势 ──→ 折线图
│   ├─ 需要展示类别对比 ──→ 柱状图（堆叠/分组）
│   ├─ 需要展示部分与整体关系 ──→ 饼图/环形图
│   ├─ 需要展示多维度对比 ──→ 雷达图
│   ├─ 需要展示排名 ──→ 水平条形图
│   ├─ 需要展示相关性 ──→ 散点图/气泡图
│   ├─ 需要展示循环/极坐标数据 ──→ 极坐标图
│   └─ 需要多系列组合 ──→ 组合图表
│
└─ 概念型内容 ──→ 进入概念可视化选择流程
    │ 提示：检查是否可使用两列/三列布局进行对比
    │
    ├─ 递进/序列型 ──→ 流程图、时间线、战略路线图
    ├─ 时间序列型 ──→ 时间线、战略路线图、折线图
    ├─ 并列/坐标型 ──→ 强调框、思维导图、矩阵
    ├─ 层级/金字塔型 ──→ 金字塔、倒金字塔、树形图
    ├─ 对比/双列型 ──→ 对比图、优劣势分析、文氏图
    ├─ 分析框架型 ──→ SWOT分析、安索夫矩阵、5W1H
    ├─ 转化/漏斗型 ──→ 漏斗图、价值流图、瀑布图
    ├─ 循环/迭代型 ──→ 循环图、极坐标图
    └─ 因果/问题解决型 ──→ 问题解决方案、帕累托图、鱼骨图
```

---

## 数据图表选择（Chart.js）

### 决策矩阵（扩展版）

| 数据特征 | 推荐图表 | Chart.js类型 | 布局建议 | 优先级 |
|---------|---------|-------------|---------|--------|
| 类别对比（单系列） | 柱状图 | bar | 两列（图表+洞察） | ★★★★★ |
| 时间趋势 | 折线图 | line | 两列（图表+洞察） | ★★★★★ |
| 部分与整体（≤5项） | 环形图 | doughnut | 两列（图表+洞察） | ★★★★☆ |
| 部分与整体（≤8项） | 饼图 | pie | 两列（图表+洞察） | ★★★★☆ |
| 多维度对比 | 雷达图 | radar | 两列（图表+洞察） | ★★★★☆ |
| 排名/循环数据 | 极坐标图 | polarArea | 两列（图表+洞察） | ★★★☆☆ |
| 三维数据（x,y,大小） | 气泡图 | bubble | 两列（图表+洞察） | ★★★☆☆ |
| 相关性分析 | 散点图 | scatter | 两列（图表+洞察） | ★★★☆☆ |
| 多类别堆叠对比 | 堆叠柱状图 | bar（堆叠） | 两列（图表+洞察） | ★★★★★ |
| 水平类别展示 | 水平条形图 | bar（水平） | 两列（图表+洞察） | ★★★★☆ |
| 进度/完成率 | 进度环 | doughnut | 两列（图表+洞察） | ★★★★☆ |
| 多指标组合 | 组合图表 | mixed | 两列或三列 | ★★★★★ |
| 双向对比 | 双向条形图 | bar | 两列（图表+洞察） | ★★★★☆ |
| 阶段转化 | 漏斗图 | funnel | 两列（图表+洞察） | ★★★☆☆ |
| 瀑布增减 | 瀑布图 | waterfall | 两列（图表+洞察） | ★★★☆☆ |
| 目标达成 | 仪表盘 | gauge | 两列（图表+洞察） | ★★★☆☆ |
| 地区分布 | 地图热力图 | choropleth | 两列（图表+洞察） | ★★☆☆☆ |

### 智能选择算法（详细版）

```
步骤1：分析数据维度

IF 数据包含时间维度：
    ├─ 时间序列连续数据 ──→ 使用'折线图'（line）
    │   布局：两列（左侧图表展示趋势，右侧分析洞察）
    │   示例：年度收入趋势、季度增长率、月份销量
    │
    ├─ 时间节点里程碑 ──→ 使用'时间线'（HTML/CSS）
    │   布局：单列或两列（根据内容调整）
    │   示例：项目里程碑、公司发展历程
    │
    └─ 时间段对比 ──→ 使用'分组柱状图'（bar）
        布局：两列（图表+洞察）
        示例：2023 vs 2024对比、各季度对比

步骤2：分析数据关系

IF 数据展示部分与整体关系：
    ├─ 5项及以下 ──→ 使用'环形图'（doughnut）
    │   优势：比饼图更现代，中央可放置总计
    │   布局：两列（左侧图表，右侧百分比明细）
    │   示例：市场份额、产品组合
    │
    ├─ 6-8项 ──→ 使用'饼图'（pie）
    │   布局：两列（左侧图表，右侧分类明细）
    │   警告：超过8项考虑使用柱状图
    │
    └─ 超过8项 ──→ 使用'柱状图'（bar）
        布局：两列（展示前10项，其余归为"其他"）
        示例：多项分类统计

步骤3：分析比较类型

IF 数据进行类别比较：
    ├─ 多指标多类别 ──→ 使用'堆叠柱状图'（bar，stacked=true）
    │   布局：两列（展示堆叠效果，右侧说明各部分构成）
    │   示例：各地区季度销售额构成
    │
    ├─ 单一指标排名 ──→ 使用'水平条形图'（bar，indexAxis='y'）
    │   布局：两列（左侧图表，右侧排名说明）
    │   示例：销售冠军排名、产品满意度排名
    │
    ├─ 双向对比 ──→ 使用'双向条形图'
    │   布局：两列（图表居中左右对比，右侧结论）
    │   示例：预算vs实际、去年vs今年
    │
    └─ 多维度指标 ──→ 使用'雷达图'（radar）
        布局：两列（展示雷达形状，右侧维度分析）
        示例：竞品多维度对比、绩效评估

步骤4：分析分布与相关性

IF 数据展示分布或相关性：
    ├─ 简单相关 ──→ 使用'散点图'（scatter）
    │   布局：两列（展示分布模式，右侧相关性分析）
    │   示例：广告投入vs销售额、客户年龄vs购买力
    │
    ├─ 三维数据（x,y,大小） ──→ 使用'气泡图'（bubble）
    │   布局：两列（展示气泡分布，右侧三个维度解读）
    │   示例：市场规模vs增长率vs利润
    │
    └─ 循环/周期性数据 ──→ 使用'极坐标图'（polarArea）
        布局：两列（展示极坐标分布，右侧循环分析）
        示例：月度销售周期、季节性波动

步骤5：分析组合需求

IF 需要多图表组合展示：
    ├─ 不同类型图表 ──→ 使用'组合图表'（mixed）
    │   布局：两列（左侧主图表组合，右侧各系列说明）
    │   示例：柱状图+折线图展示趋势与总量
    │
    ├─ 同类型多图表 ──→ 使用'三列布局'
    │   布局：三列等宽（每列一个图表，便于对比）
    │   示例：各地区销售对比、各产品线对比
    │
    └─ 父子层级数据 ──→ 使用'树形图'（treemap）
        布局：两列（展示树形结构，右侧层级说明）
        示例：组织架构、产品分类

步骤6：分析流程与转化

IF 数据涉及流程转化：
    ├─ 阶段过滤递减 ──→ 使用'漏斗图'
    │   布局：两列（展示漏斗形状，右侧各阶段转化率）
    │   示例：销售漏斗、用户转化漏斗
    │
    ├─ 增减变动分解 ──→ 使用'瀑布图'
    │   布局：两列（展示增减过程，右侧变动说明）
    │   示例：收入变动分析、预算执行情况
    │
    └─ 目标达成展示 ──→ 使用'仪表盘'（gauge）
        布局：两列（展示仪表盘，右侧目标分析）
        示例：KPI完成率、绩效评分

步骤7：默认处理

ELSE：
    → 默认使用'柱状图'（bar）- 最通用
    → 布局：两列（图表+洞察）
    → 说明：柱状图适用于大多数数据展示场景
```

### 图表类型详细说明

#### 1. 柱状图（Bar Chart）

**适用场景**：类别对比、数量比较、排名展示

**子类型**：

| 子类型 | 特点 | 适用场景 |
|-------|------|---------|
| 垂直柱状图 | 传统样式，x轴为类别 | 常规类别对比 |
| 水平条形图 | y轴为类别，便于阅读长标签 | 排名、长标签 |
| 分组柱状图 | 多系列并排对比 | 多期间/多条件对比 |
| 堆叠柱状图 | 多系列堆叠展示总量与构成 | 总量+构成分析 |
| 百分比堆叠柱状图 | 各列归一化为100% | 构成比例对比 |

**配置示例**：

```javascript
// 基础柱状图配置
const barChartConfig = {
  type: 'bar',
  data: {
    labels: ['类别A', '类别B', '类别C', '类别D', '类别E'],
    datasets: [{
      label: '2024年数据',
      data: [65, 59, 80, 81, 56],
      backgroundColor: [
        '#556EE6', // 深蓝色 - 主要数据
        '#F85d42', // 橙色 - 重点数据
        '#34c38f', // 绿色 - 正向数据
        '#50a5f1', // 蓝色 - 次要数据
        '#f1b44c'  // 黄色 - 对比数据
      ],
      borderColor: '#ffffff',
      borderWidth: 2,
      borderRadius: 0
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: {
        display: true,
        position: 'top',
        labels: {
          font: { family: 'Microsoft YaHei', size: 14 },
          color: '#333333'
        }
      },
      tooltip: {
        backgroundColor: 'rgba(0, 0, 0, 0.8)',
        titleFont: { family: 'Microsoft YaHei', size: 14 },
        bodyFont: { family: 'Microsoft YaHei', size: 12 },
        padding: 12,
        cornerRadius: 0
      }
    },
    scales: {
      x: {
        grid: { display: false },
        ticks: {
          font: { family: 'Microsoft YaHei', size: 12 },
          color: '#74788d'
        }
      },
      y: {
        beginAtZero: true,
        grid: { color: '#e0e0e0' },
        ticks: {
          font: { family: 'Microsoft YaHei', size: 12 },
          color: '#74788d'
        }
      }
    }
  }
};

// 堆叠柱状图配置
const stackedBarConfig = {
  type: 'bar',
  data: {
    labels: ['Q1', 'Q2', 'Q3', 'Q4'],
    datasets: [
      {
        label: '产品A',
        data: [30, 35, 40, 45],
        backgroundColor: '#556EE6' // 深蓝色
      },
      {
        label: '产品B',
        data: [20, 25, 30, 35],
        backgroundColor: '#F85d42' // 橙色
      },
      {
        label: '产品C',
        data: [15, 18, 22, 25],
        backgroundColor: '#34c38f' // 绿色
      }
    ]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    scales: {
      x: { stacked: true },
      y: { stacked: true }
    }
  }
};

// 水平条形图配置
const horizontalBarConfig = {
  type: 'bar',
  data: {
    labels: ['产品A', '产品B', '产品C', '产品D', '产品E'],
    datasets: [{
      label: '销售额（百万元）',
      data: [120, 95, 80, 65, 45],
      backgroundColor: '#556EE6',
      borderRadius: 0
    }]
  },
  options: {
    indexAxis: 'y',
    responsive: true,
    maintainAspectRatio: true
  }
};
```

**布局示例（两列）**：

```html
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">区域销售对比分析</h2>
  </div>
  <div class="slide-content">
    <div class="two-column">
      <div class="column" style="flex: 3;">
        <div class="chart-container">
          <canvas id="regionalSalesChart"></canvas>
        </div>
        <p class="chart-caption">数据来源：2024年度销售报表</p>
      </div>
      <div class="column" style="flex: 2;">
        <h3 class="section-heading">关键洞察</h3>
        <ul class="bullet-list">
          <li><strong>华东地区领先</strong>：销售额达1.2亿元，占比35%</li>
          <li><strong>华南增长最快</strong>：同比增长45%，潜力巨大</li>
          <li><strong>华北区稳定</strong>：保持20%市场份额</li>
          <li><strong>西部地区</strong>：占比最小但增速明显</li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

#### 2. 折线图（Line Chart）

**适用场景**：时间趋势、连续数据变化、预测分析

**子类型**：

| 子类型 | 特点 | 适用场景 |
|-------|------|---------|
| 单线图 | 单一数据系列 | 单指标趋势 |
| 多线图 | 多数据系列对比 | 多指标同期对比 |
| 平滑曲线 | 使用贝塞尔曲线 | 强调整体趋势 |
| 折线 | 锐利转折点 | 精确数据展示 |
| 阶梯图 | 阶梯式变化 | 状态变化、时间点触发 |
| 填充面积图 | 线下填充 | 强调累积量或范围 |

**配置示例**：

```javascript
// 多线趋势图配置
const lineChartConfig = {
  type: 'line',
  data: {
    labels: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
    datasets: [
      {
        label: '2024年实际',
        data: [65, 72, 86, 89, 95, 102, 118, 125, 138, 145, 152, 168],
        borderColor: '#556EE6', // 深蓝色
        backgroundColor: 'rgba(85, 110, 230, 0.1)',
        borderWidth: 3,
        tension: 0.3,
        fill: false,
        pointRadius: 4,
        pointHoverRadius: 6,
        pointBackgroundColor: '#ffffff',
        pointBorderColor: '#556EE6',
        pointBorderWidth: 2
      },
      {
        label: '2023年实际',
        data: [55, 58, 62, 68, 72, 78, 85, 88, 92, 98, 105, 112],
        borderColor: '#F85d42', // 橙色
        backgroundColor: 'rgba(248, 93, 66, 0.1)',
        borderWidth: 3,
        tension: 0.3,
        fill: false,
        pointRadius: 4,
        pointHoverRadius: 6,
        pointBackgroundColor: '#ffffff',
        pointBorderColor: '#F85d42',
        pointBorderWidth: 2
      },
      {
        label: '2024年目标',
        data: [60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115],
        borderColor: '#34c38f', // 绿色
        borderWidth: 2,
        borderDash: [5, 5],
        tension: 0.3,
        fill: false,
        pointRadius: 0,
        pointHoverRadius: 4
      }
    ]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    interaction: {
      mode: 'index',
      intersect: false
    },
    plugins: {
      legend: {
        display: true,
        position: 'top',
        labels: {
          font: { family: 'Microsoft YaHei', size: 13 },
          color: '#333333',
          usePointStyle: true,
          padding: 20
        }
      },
      tooltip: {
        backgroundColor: 'rgba(0, 0, 0, 0.8)',
        titleFont: { family: 'Microsoft YaHei', size: 14 },
        bodyFont: { family: 'Microsoft YaHei', size: 12 },
        padding: 12,
        cornerRadius: 0
      }
    },
    scales: {
      x: {
        grid: { display: false },
        ticks: {
          font: { family: 'Microsoft YaHei', size: 11 },
          color: '#74788d'
        }
      },
      y: {
        beginAtZero: false,
        min: 40,
        grid: { color: '#e0e0e0' },
        ticks: {
          font: { family: 'Microsoft YaHei', size: 11 },
          color: '#74788d'
        }
      }
    }
  }
};
```

**布局示例（两列）**：

```html
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">月度销售趋势分析</h2>
  </div>
  <div class="slide-content">
    <div class="two-column">
      <div class="column" style="flex: 3;">
        <div class="chart-container">
          <canvas id="monthlyTrendChart"></canvas>
        </div>
        <p class="chart-caption">数据来源：销售管理系统 | 2024年1月-12月</p>
      </div>
      <div class="column" style="flex: 2;">
        <h3 class="section-heading">趋势洞察</h3>
        <ul class="numbered-list">
          <li><strong>持续增长</strong>：全年保持正增长，月均增速8.5%</li>
          <li><strong>Q3加速</strong>：7月起增速明显加快，得益于新品上市</li>
          <li><strong>同比优势</strong>：全年同比提升32%，超额完成目标</li>
          <li><strong>Q4冲刺</strong>：11-12月增长最为显著</li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

#### 3. 饼图与环形图（Pie & Doughnut Chart）

**适用场景**：部分与整体关系、占比分析、分布构成

**子类型**：

| 子类型 | 特点 | 适用场景 |
|-------|------|---------|
| 饼图 | 传统圆形切割 | 5项及以下的占比 |
| 环形图 | 中央空心，更现代 | 强调中间数据（如总计） |
| 嵌套环形图 | 多层嵌套 | 多层级占比分析 |
| 旭日图 | 多层环形嵌套 | 层级结构占比 |

**配置示例**：

```javascript
// 饼图配置
const pieChartConfig = {
  type: 'pie',
  data: {
    labels: ['华东', '华南', '华北', '西部', '其他'],
    datasets: [{
      data: [35, 25, 20, 12, 8],
      backgroundColor: [
        '#556EE6', // 深蓝色 - 主要
        '#F85d42', // 橙色 - 重点
        '#34c38f', // 绿色 - 正向
        '#50a5f1', // 蓝色 - 次要
        '#f1b44c'  // 黄色 - 对比
      ],
      borderColor: '#ffffff',
      borderWidth: 3
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: {
        display: true,
        position: 'right',
        labels: {
          font: { family: 'Microsoft YaHei', size: 13 },
          color: '#333333',
          padding: 15,
          generateLabels: function(chart) {
            const data = chart.data;
            const total = data.datasets[0].data.reduce((sum, val) => sum + val, 0);
            return data.labels.map((label, i) => {
              const value = data.datasets[0].data[i];
              const percentage = ((value / total) * 100).toFixed(1);
              return {
                text: `${label}: ${percentage}%`,
                fillStyle: data.datasets[0].backgroundColor[i],
                index: i
              };
            });
          }
        }
      },
      tooltip: {
        backgroundColor: 'rgba(0, 0, 0, 0.8)',
        callbacks: {
          label: function(context) {
            const label = context.label || '';
            const value = context.raw || 0;
            const total = context.dataset.data.reduce((sum, val) => sum + val, 0);
            const percentage = ((value / total) * 100).toFixed(1);
            return `${label}: ${value} (${percentage}%)`;
          }
        }
      }
    }
  }
};

// 环形图配置（推荐用于现代风格）
const doughnutChartConfig = {
  type: 'doughnut',
  data: {
    labels: ['已完成', '进行中', '待开始'],
    datasets: [{
      data: [68, 22, 10],
      backgroundColor: [
        '#34c38f', // 绿色 - 已完成
        '#F85d42', // 橙色 - 进行中
        '#e0e0e0'  // 灰色 - 待开始
      ],
      borderColor: '#ffffff',
      borderWidth: 4,
      hoverOffset: 8
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    cutout: '65%',
    plugins: {
      legend: {
        display: true,
        position: 'bottom',
        labels: {
          font: { family: 'Microsoft YaHei', size: 13 },
          color: '#333333',
          padding: 20
        }
      },
      tooltip: {
        backgroundColor: 'rgba(0, 0, 0, 0.8)',
        callbacks: {
          label: function(context) {
            const label = context.label || '';
            const value = context.raw || 0;
            return `${label}: ${value}%`;
          }
        }
      }
    }
  }
};
```

**布局示例（两列）**：

```html
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">市场份额分布</h2>
  </div>
  <div class="slide-content">
    <div class="two-column">
      <div class="column" style="flex: 3;">
        <div class="chart-container">
          <canvas id="marketShareChart"></canvas>
        </div>
        <p class="chart-caption">数据来源：行业研究报告 | 2024年Q4</p>
      </div>
      <div class="column" style="flex: 2;">
        <h3 class="section-heading">市场分析</h3>
        <ul class="bullet-list">
          <li><strong>我方领先地位</strong>：占据35%市场份额，领先第二名10个百分点</li>
          <li><strong>主要竞争对手</strong>：B公司25%，C公司15%</li>
          <li><strong>市场集中度</strong>：前三大企业占比75%</li>
          <li><strong>增长机会</strong>：西部地区仍有较大提升空间</li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

#### 4. 雷达图（Radar Chart）

**适用场景**：多维度对比、绩效评估、竞品分析、能力分布

**配置示例**：

```javascript
const radarChartConfig = {
  type: 'radar',
  data: {
    labels: ['产品质量', '价格竞争力', '品牌认知', '渠道覆盖', '售后服务', '技术创新'],
    datasets: [
      {
        label: '我方',
        data: [90, 75, 85, 80, 88, 82],
        borderColor: '#556EE6',
        backgroundColor: 'rgba(85, 110, 230, 0.2)',
        borderWidth: 2,
        pointBackgroundColor: '#556EE6',
        pointBorderColor: '#ffffff',
        pointHoverBackgroundColor: '#ffffff',
        pointHoverBorderColor: '#556EE6'
      },
      {
        label: '竞品A',
        data: [80, 85, 75, 70, 72, 78],
        borderColor: '#F85d42',
        backgroundColor: 'rgba(248, 93, 66, 0.2)',
        borderWidth: 2,
        pointBackgroundColor: '#F85d42',
        pointBorderColor: '#ffffff',
        pointHoverBackgroundColor: '#ffffff',
        pointHoverBorderColor: '#F85d42'
      },
      {
        label: '竞品B',
        data: [72, 70, 80, 85, 75, 68],
        borderColor: '#34c38f',
        backgroundColor: 'rgba(52, 195, 143, 0.2)',
        borderWidth: 2,
        pointBackgroundColor: '#34c38f',
        pointBorderColor: '#ffffff',
        pointHoverBackgroundColor: '#ffffff',
        pointHoverBorderColor: '#34c38f'
      }
    ]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    elements: {
      line: { tension: 0 }
    },
    scales: {
      r: {
        angleLines: {
          color: '#e0e0e0'
        },
        grid: {
          color: '#e0e0e0'
        },
        pointLabels: {
          font: {
            family: 'Microsoft YaHei',
            size: 12
          },
          color: '#333333'
        },
        suggestedMin: 0,
        suggestedMax: 100,
        ticks: {
          stepSize: 20,
          display: false
        }
      }
    },
    plugins: {
      legend: {
        display: true,
        position: 'top',
        labels: {
          font: { family: 'Microsoft YaHei', size: 13 },
          color: '#333333',
          padding: 15
        }
      }
    }
  }
};
```

**布局示例（两列）**：

```html
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">竞品多维度能力对比</h2>
  </div>
  <div class="slide-content">
    <div class="two-column">
      <div class="column" style="flex: 3;">
        <div class="chart-container">
          <canvas id="competitorRadarChart"></canvas>
        </div>
        <p class="chart-caption">评分标准：0-100分 | 数据来源：市场调研</p>
      </div>
      <div class="column" style="flex: 2;">
        <h3 class="section-heading">竞争优势分析</h3>
        <ul class="card-list">
          <li><strong>产品质量领先</strong>：我方得分90，高于竞品10-18分</li>
          <li><strong>价格竞争力待提升</strong>：竞品A得分85，我方需加强</li>
          <li><strong>品牌认知优势</strong>：与竞品B持平，保持投入</li>
          <li><strong>技术创新持续</strong>：高于行业平均，差距缩小</li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

#### 5. 散点图与气泡图（Scatter & Bubble Chart）

**适用场景**：相关性分析、分布研究、多维度数据

**配置示例**：

```javascript
// 散点图配置
const scatterChartConfig = {
  type: 'scatter',
  data: {
    datasets: [{
      label: '产品组合',
      data: [
        { x: 10, y: 20 },
        { x: 15, y: 35 },
        { x: 20, y: 45 },
        { x: 25, y: 55 },
        { x: 30, y: 60 },
        { x: 35, y: 75 },
        { x: 40, y: 80 },
        { x: 45, y: 70 },
        { x: 50, y: 85 },
        { x: 55, y: 90 }
      ],
      backgroundColor: 'rgba(85, 110, 230, 0.6)',
      borderColor: '#556EE6',
      borderWidth: 1,
      pointRadius: 8,
      pointHoverRadius: 10
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: { display: false },
      tooltip: {
        callbacks: {
          label: function(context) {
            return `市场份额: ${context.raw.x}% | 增长率: ${context.raw.y}%`;
          }
        }
      }
    },
    scales: {
      x: {
        title: {
          display: true,
          text: '市场份额 (%)',
          font: { family: 'Microsoft YaHei', size: 13 },
          color: '#74788d'
        },
        min: 0,
        max: 60,
        grid: { color: '#e0e0e0' }
      },
      y: {
        title: {
          display: true,
          text: '增长率 (%)',
          font: { family: 'Microsoft YaHei', size: 13 },
          color: '#74788d'
        },
        min: 0,
        max: 100,
        grid: { color: '#e0e0e0' }
      }
    }
  }
};

// 气泡图配置（三维数据）
const bubbleChartConfig = {
  type: 'bubble',
  data: {
    datasets: [
      {
        label: '华东区域',
        data: [
          { x: 35, y: 45, r: 25 }
        ],
        backgroundColor: 'rgba(85, 110, 230, 0.6)',
        borderColor: '#556EE6'
      },
      {
        label: '华南区域',
        data: [
          { x: 25, y: 55, r: 18 }
        ],
        backgroundColor: 'rgba(248, 93, 66, 0.6)',
        borderColor: '#F85d42'
      },
      {
        label: '华北区域',
        data: [
          { x: 20, y: 35, r: 22 }
        ],
        backgroundColor: 'rgba(52, 195, 143, 0.6)',
        borderColor: '#34c38f'
      }
    ]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: {
        display: true,
        position: 'top',
        labels: {
          font: { family: 'Microsoft YaHei', size: 13 },
          color: '#333333'
        }
      }
    },
    scales: {
      x: {
        title: {
          display: true,
          text: '市场份额 (%)',
          font: { family: 'Microsoft YaHei', size: 13 },
          color: '#74788d'
        }
      },
      y: {
        title: {
          display: true,
          text: '增长率 (%)',
          font: { family: 'Microsoft YaHei', size: 13 },
          color: '#74788d'
        }
      }
    }
  }
};
```

#### 6. 极坐标图（Polar Area Chart）

**适用场景**：循环数据、周期性分析、排名展示

**配置示例**：

```javascript
const polarChartConfig = {
  type: 'polarArea',
  data: {
    labels: ['产品A', '产品B', '产品C', '产品D', '产品E', '产品F'],
    datasets: [{
      data: [45, 38, 32, 28, 22, 18],
      backgroundColor: [
        'rgba(85, 110, 230, 0.7)',
        'rgba(248, 93, 66, 0.7)',
        'rgba(52, 195, 143, 0.7)',
        'rgba(80, 165, 241, 0.7)',
        'rgba(241, 180, 76, 0.7)',
        'rgba(116, 120, 141, 0.7)'
      ],
      borderColor: '#ffffff',
      borderWidth: 2
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    scales: {
      r: {
        ticks: { display: false },
        grid: { color: '#e0e0e0' }
      }
    },
    plugins: {
      legend: {
        display: true,
        position: 'right',
        labels: {
          font: { family: 'Microsoft YaHei', size: 12 },
          color: '#333333',
          padding: 10
        }
      }
    }
  }
};
```

#### 7. 组合图表（Mixed Chart）

**适用场景**：多类型数据整合展示、趋势与构成结合

**配置示例**：

```javascript
// 柱状图+折线图组合
const mixedChartConfig = {
  type: 'bar',
  data: {
    labels: ['1月', '2月', '3月', '4月', '5月', '6月'],
    datasets: [
      {
        type: 'bar',
        label: '月度销售额（百万元）',
        data: [120, 150, 180, 165, 200, 230],
        backgroundColor: 'rgba(85, 110, 230, 0.8)',
        borderColor: '#556EE6',
        borderWidth: 1,
        order: 2
      },
      {
        type: 'line',
        label: '累计增长率（%）',
        data: [5, 12, 18, 22, 28, 35],
        borderColor: '#F85d42',
        backgroundColor: 'rgba(248, 93, 66, 0.1)',
        borderWidth: 3,
        tension: 0.3,
        fill: true,
        yAxisID: 'y1',
        order: 1
      }
    ]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: {
        display: true,
        position: 'top',
        labels: {
          font: { family: 'Microsoft YaHei', size: 13 },
          color: '#333333'
        }
      }
    },
    scales: {
      y: {
        type: 'linear',
        display: true,
        position: 'left',
        title: {
          display: true,
          text: '销售额（百万元）',
          font: { family: 'Microsoft YaHei', size: 12 },
          color: '#556EE6'
        },
        grid: { color: '#e0e0e0' }
      },
      y1: {
        type: 'linear',
        display: true,
        position: 'right',
        title: {
          display: true,
          text: '增长率（%）',
          font: { family: 'Microsoft YaHei', size: 12 },
          color: '#F85d42'
        },
        grid: { drawOnChartArea: false },
        min: 0,
        max: 50
      }
    }
  }
};
```

**布局示例（三列）**：

```html
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">各区域业绩对比</h2>
  </div>
  <div class="slide-content">
    <div class="three-column">
      <div class="column">
        <h4 class="chart-title">华东区域</h4>
        <div class="chart-container-sm">
          <canvas id="eastChinaChart"></canvas>
        </div>
        <p class="chart-caption">同比增长 32%</p>
      </div>
      <div class="column">
        <h4 class="chart-title">华南区域</h4>
        <div class="chart-container-sm">
          <canvas id="southChinaChart"></canvas>
        </div>
        <p class="chart-caption">同比增长 28%</p>
      </div>
      <div class="column">
        <h4 class="chart-title">华北区域</h4>
        <div class="chart-container-sm">
          <canvas id="northChinaChart"></canvas>
        </div>
        <p class="chart-caption">同比增长 25%</p>
      </div>
    </div>
  </div>
</div>
```

### 图表颜色应用规范

#### 配色优先级表

| 数据系列顺序 | 颜色代码 | 颜色名称 | 使用场景 |
|------------|---------|---------|---------|
| 第1系列 | #556EE6 | Deep Blue | 主要数据、基准线、首要对比 |
| 第2系列 | #F85d42 | Orange | 重点强调、次要对比、突出数据 |
| 第3系列 | #34c38f | Green | 正向数据、成功指标、增长趋势 |
| 第4系列 | #50a5f1 | Blue | 中性数据、次要系列 |
| 第5系列 | #f1b44c | Yellow | 警告数据、对比基准、参考线 |

#### 配色应用示例

```javascript
// 单系列数据 - 使用深蓝色
const singleSeriesColors = ['#556EE6'];

// 双系列数据 - 深蓝 + 橙色
const dualSeriesColors = ['#556EE6', '#F85d42'];

// 三系列数据 - 深蓝 + 橙色 + 绿色
const tripleSeriesColors = ['#556EE6', '#F85d42', '#34c38f'];

// 多系列数据 (4-5个) - 按优先级
const multiSeriesColors = ['#556EE6', '#F85d42', '#34c38f', '#50a5f1', '#f1b44c'];

// 特殊场景配色
const specialColors = {
  positive: '#34c38f',      // 正向/增长 - 绿色
  negative: '#F85d42',      // 负向/下降 - 橙色
  neutral: '#50a5f1',       // 中性 - 蓝色
  warning: '#f1b44c',       // 警告 - 黄色
  disabled: '#e0e0e0'       // 禁用/背景 - 浅灰
};

// 状态指示配色
const statusColors = {
  completed: '#34c38f',     // 已完成 - 绿色
  inProgress: '#F85d42',    // 进行中 - 橙色
  pending: '#e0e0e0',       // 待开始 - 灰色
  delayed: '#f1b44c'        // 延迟 - 黄色
};
```

---

## 概念可视化选择

### 9种内容结构类型

#### 1. 递进型（Progressive/Sequential）

**识别关键词**：首先、其次、最后、第一步、第二步、第三步、阶段、步骤、流程

**决策树**：

```
IF 3-5个顺序步骤无分支：
    → 使用'递进箭头'（简单箭头流程）
    
ELIF 包含时间标签（日期、年份）：
    → 使用'时间线'（水平时间轴）
    
ELIF 包含决策点或分支：
    → 使用'流程图'（含决策菱形）
    
ELIF 多阶段并行活动：
    → 使用'战略路线图'（泳道时间线）
    
ELSE：
    → 默认使用'递进箭头'
```

**示例文件**：

- `assets/flowchart-example.html`
- `assets/timeline-example.html`
- `assets/strategy-roadmap-example.html`

**布局示例**：

```html
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">项目实施三阶段</h2>
  </div>
  <div class="slide-content">
    <div class="two-column">
      <div class="column" style="flex: 3;">
        <div class="progression-container">
          <div class="progression-item">
            <div class="progression-number">01</div>
            <div class="progression-content">
              <h4>需求分析阶段</h4>
              <p>深入了解客户需求，明确项目目标与范围</p>
            </div>
          </div>
          <div class="progression-arrow">→</div>
          <div class="progression-item">
            <div class="progression-number">02</div>
            <div class="progression-content">
              <h4>方案设计阶段</h4>
              <p>制定详细实施方案，确定技术路线</p>
            </div>
          </div>
          <div class="progression-arrow">→</div>
          <div class="progression-item">
            <div class="progression-number">03</div>
            <div class="progression-content">
              <h4>落地执行阶段</h4>
              <p>按计划推进项目，定期汇报进展</p>
            </div>
          </div>
        </div>
      </div>
      <div class="column" style="flex: 2;">
        <h3 class="section-heading">关键要点</h3>
        <ul class="timeline-list">
          <li><strong>阶段一</strong>：周期2周，产出需求文档</li>
          <li><strong>阶段二</strong>：周期3周，产出设计方案</li>
          <li><strong>阶段三</strong>：周期8周，分迭代交付</li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

#### 2. 时间序列型（Temporal/Time-series）

**识别关键词**：年份（2024）、季度（Q1）、月份、过去、现在、未来、趋势、预测、预计

**决策树**：

```
IF 明确的时间顺序：
    → 使用'时间线'（含里程碑水平轴）
    
ELIF 含阶段战略规划：
    → 使用'战略路线图'（多轨道时间线）
    
ELIF 数值趋势数据：
    → 使用 Chart.js '折线图'
    
ELSE：
    → 默认使用'时间线'
```

**示例文件**：

- `assets/timeline-example.html`
- `assets/strategy-roadmap-example.html`

**布局示例**：

```html
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">公司发展历程</h2>
  </div>
  <div class="slide-content">
    <div class="timeline-container">
      <div class="timeline-item">
        <div class="timeline-date">2018</div>
        <div class="timeline-marker"></div>
        <div class="timeline-content">
          <h4>公司成立</h4>
          <p>完成首轮融资，启动产品研发</p>
        </div>
      </div>
      <div class="timeline-item">
        <div class="timeline-date">2020</div>
        <div class="timeline-marker"></div>
        <div class="timeline-content">
          <h4>产品上线</h4>
          <p>首款产品上线，用户突破100万</p>
        </div>
      </div>
      <div class="timeline-item">
        <div class="timeline-date">2022</div>
        <div class="timeline-marker"></div>
        <div class="timeline-content">
          <h4>市场扩张</h4>
          <p>扩展至全国市场，营收破亿</p>
        </div>
      </div>
      <div class="timeline-item">
        <div class="timeline-date">2024</div>
        <div class="timeline-marker"></div>
        <div class="timeline-content">
          <h4>战略升级</h4>
          <p>启动国际化战略，进入新阶段</p>
        </div>
      </div>
    </div>
  </div>
</div>
```

#### 3. 并列型（Parallel/Coordinate）

**识别关键词**：同时、以及、另外、此外、包括、并且、一方面、另一方面

**决策树**：

```
IF 2-4个等权重要点：
    → 使用'强调框'（网格盒子布局）
    
ELIF 5+要点从中心主题分支：
    → 使用'思维导图'（辐射布局）
    
ELIF 2x2或3x3框架：
    → 使用'矩阵'（网格布局）
    
ELIF 含标签的水平对比：
    → 使用'麦肯锡标签条形图'
    
ELSE：
    → 默认使用'强调框'
```

**示例文件**：

- `assets/mindmap-example.html`
- `assets/mckinsey-label-bar-example.html`
- `assets/emphasis-box-example.html`

**布局示例**：

```html
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">核心竞争优势</h2>
  </div>
  <div class="slide-content">
    <div class="two-column">
      <div class="column" style="flex: 1;">
        <div class="emphasis-box-grid">
          <div class="emphasis-box">
            <div class="emphasis-icon">🎯</div>
            <h4>精准定位</h4>
            <p>深耕细分市场，满足用户核心需求</p>
          </div>
          <div class="emphasis-box">
            <div class="emphasis-icon">⚡</div>
            <h4>高效运营</h4>
            <p>自动化流程，降低运营成本30%</p>
          </div>
          <div class="emphasis-box">
            <div class="emphasis-icon">🔬</div>
            <h4>技术创新</h4>
            <p>持续研发投入，专利数量行业领先</p>
          </div>
          <div class="emphasis-box">
            <div class="emphasis-icon">🤝</div>
            <h4>生态合作</h4>
            <p>构建合作伙伴网络，实现共赢发展</p>
          </div>
        </div>
      </div>
      <div class="column" style="flex: 1;">
        <h3 class="section-heading">综合评价</h3>
        <ul class="comparison-list">
          <li><strong>市场地位</strong>：行业前三，客户满意度95%</li>
          <li><strong>增长潜力</strong>：年均增长率45%，远高于行业</li>
          <li><strong>护城河</strong>：技术壁垒+品牌认知双重保障</li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

#### 4. 层级型（Hierarchical）

**识别关键词**：基础、中级、高级、核心、外围、层次、级别、顶层、底层

**决策树**：

```
IF 自底向上的层级（基础→顶层）：
    → 使用'金字塔'（三角形指向上）
    
ELIF 自顶向下的层级（重要→详细）：
    → 使用'倒金字塔'（三角形指向下）
    
ELIF 组织结构：
    → 使用'树形图'（层级盒子）
    
ELSE：
    → 默认使用'金字塔'
```

**示例文件**：

- `assets/pyramid-chart-example.html`
- `assets/inverted-pyramid-example.html`
- `assets/tree-example.html`

**布局示例**：

```html
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">需求层次金字塔</h2>
  </div>
  <div class="slide-content">
    <div class="two-column">
      <div class="column" style="flex: 3;">
        <div class="pyramid-container">
          <div class="pyramid-level level-1">
            <span>自我实现</span>
          </div>
          <div class="pyramid-level level-2">
            <span>尊重需求</span>
          </div>
          <div class="pyramid-level level-3">
            <span>社交需求</span>
          </div>
          <div class="pyramid-level level-4">
            <span>安全需求</span>
          </div>
          <div class="pyramid-level level-5">
            <span>生理需求</span>
          </div>
        </div>
      </div>
      <div class="column" style="flex: 2;">
        <h3 class="section-heading">层次解析</h3>
        <ul class="card-list">
          <li><strong>顶层</strong>：自我实现，追求成长与成就</li>
          <li><strong>中层</strong>：尊重与归属，被认可的需要</li>
          <li><strong>底层</strong>：基本需求，维持生活必需</li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

#### 5. 对比型（Comparative/Dual）

**识别关键词**：对比、差异、优劣、vs、相比、两者、A方案、B方案、现状、目标

**决策树**：

```
IF 两种状态并排（之前/之后、当前/目标）：
    → 使用'对比图'（左右布局）
    
ELIF 优点与缺点：
    → 使用'优劣势分析'（双列+/--）
    
ELIF 重叠集合或共享属性：
    → 使用'文氏图'（圆圈）
    
ELIF 变量对比含滑块：
    → 使用'滑块图表'（交互对比）
    
ELSE：
    → 默认使用'对比图'
```

**示例文件**：

- `assets/pros-cons-example.html`
- `assets/venn-diagram-example.html`
- `assets/slider-chart-example.html`

**布局示例**：

```html
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">方案A与方案B对比</h2>
  </div>
  <div class="slide-content">
    <div class="two-column">
      <div class="column">
        <div class="comparison-header" style="background: #556EE6;">
          <h3>方案A</h3>
        </div>
        <div class="comparison-body">
          <h4 class="pros">✓ 优势</h4>
          <ul class="bullet-list">
            <li>实施周期短，6个月可完成</li>
            <li>初始投入较低</li>
            <li>技术风险可控</li>
          </ul>
          <h4 class="cons">✗ 劣势</h4>
          <ul class="bullet-list">
            <li>扩展性有限</li>
            <li>长期维护成本高</li>
          </ul>
        </div>
      </div>
      <div class="column">
        <div class="comparison-header" style="background: #F85d42;">
          <h3>方案B</h3>
        </div>
        <div class="comparison-body">
          <h4 class="pros">✓ 优势</h4>
          <ul class="bullet-list">
            <li>架构先进，扩展性强</li>
            <li>长期成本更优</li>
            <li>符合未来发展趋势</li>
          </ul>
          <h4 class="cons">✗ 劣势</h4>
          <ul class="bullet-list">
            <li>实施周期长，需12个月</li>
            <li>初始投入较大</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>
```

#### 6. 分析框架型（Analytical Framework）

**识别关键词**：SWOT、PEST、4P、5W1H、3C、波特五力、BCG矩阵、安索夫矩阵

**决策树**：

```
IF 提及"SWOT"、"优势"、"劣势"、"机会"、"威胁"：
    → 使用'SWOT分析'（2x2网格）
    
ELIF 提及"市场"、"产品"、"增长策略"：
    → 使用'安索夫矩阵'（市场-产品矩阵）
    
ELIF 提及"What"、"Why"、"Who"、"When"、"Where"、"How"：
    → 使用'5W1H'（六边形布局）
    
ELIF 提及"竞争"、"定位"、"市场地位"：
    → 使用'竞争定位四象限'（定位矩阵）
    
ELIF 提及"基本"、"期望"、"魅力"、"满意度"：
    → 使用'卡诺模型'（满意度矩阵）
    
ELSE：
    → 使用'矩阵'（通用2x2或3x3）
```

**示例文件**：

- `assets/swot-analysis-example.html`
- `assets/ansoff-matrix-example.html`
- `assets/competitive-4box-example.html`
- `assets/5w1h-example.html`
- `assets/kano-model-example.html`

**布局示例（SWOT分析）**：

```html
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">SWOT战略分析</h2>
  </div>
  <div class="slide-content">
    <div class="swot-grid">
      <div class="swot-box swot-strengths">
        <h4>💪 优势 (Strengths)</h4>
        <ul class="bullet-list">
          <li>技术领先，拥有核心专利</li>
          <li>品牌认知度高</li>
          <li>渠道网络完善</li>
        </ul>
      </div>
      <div class="swot-box swot-weaknesses">
        <h4>⚠️ 劣势 (Weaknesses)</h4>
        <ul class="bullet-list">
          <li>人才储备不足</li>
          <li>运营效率待提升</li>
          <li>创新速度放缓</li>
        </ul>
      </div>
      <div class="swot-box swot-opportunities">
        <h4>🌟 机会 (Opportunities)</h4>
        <ul class="bullet-list">
          <li>市场需求持续增长</li>
          <li>政策支持力度加大</li>
          <li>新技术带来新机遇</li>
        </ul>
      </div>
      <div class="swot-box swot-threats">
        <h4>⚡ 威胁 (Threats)</h4>
        <ul class="bullet-list">
          <li>竞争加剧，价格战</li>
          <li>经济环境不确定性</li>
          <li>法规政策变化</li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

#### 7. 转化流程型（Transformation/Funnel）

**识别关键词**：转化、漏斗、筛选、流失、通过率、转化率、阶段

**决策树**：

```
IF 阶段过滤数据递减：
    → 使用'漏斗图'（倒三角形阶段）
    
ELIF 价值创造过程含流动：
    → 使用'价值流图'（水平流动+价值标注）
    
ELIF 连续增减变动：
    → 使用'瀑布图'（带桥梁条形图）
    
ELSE：
    → 默认使用'漏斗图'
```

**示例文件**：

- `assets/funnel-chart-example.html`
- `assets/value-stream-example.html`
- `assets/waterfall-chart-example.html`

**布局示例（漏斗图）**：

```html
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">销售转化漏斗</h2>
  </div>
  <div class="slide-content">
    <div class="two-column">
      <div class="column" style="flex: 3;">
        <div class="funnel-container">
          <div class="funnel-stage" style="width: 100%; background: #556EE6;">
            <span class="funnel-label">访问量</span>
            <span class="funnel-value">10,000</span>
          </div>
          <div class="funnel-stage" style="width: 80%; background: #6f7de6;">
            <span class="funnel-label">注册用户</span>
            <span class="funnel-value">3,500</span>
          </div>
          <div class="funnel-stage" style="width: 60%; background: #918ce6;">
            <span class="funnel-label">活跃用户</span>
            <span class="funnel-value">1,200</span>
          </div>
          <div class="funnel-stage" style="width: 40%; background: #b19ce6;">
            <span class="funnel-label">付费转化</span>
            <span class="funnel-value">480</span>
          </div>
          <div class="funnel-stage" style="width: 25%; background: #F85d42;">
            <span class="funnel-label">复购用户</span>
            <span class="funnel-value">192</span>
          </div>
        </div>
      </div>
      <div class="column" style="flex: 2;">
        <h3 class="section-heading">转化率分析</h3>
        <ul class="card-list">
          <li><strong>访问→注册</strong>：35%，高于行业平均</li>
          <li><strong>注册→活跃</strong>：34%，需优化激活策略</li>
          <li><strong>活跃→付费</strong>：40%，表现优秀</li>
          <li><strong>付费→复购</strong>：40%，用户粘性好</li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

#### 8. 循环型（Cyclical/Iterative）

**识别关键词**：循环、迭代、反馈、持续、闭环、反复、优化、改进

**决策树**：

```
IF 含反馈的闭环流程：
    → 使用'循环图'（带箭头圆形）
    
ELIF 含阶段的迭代过程：
    → 使用'循环流'（圆形+标签分段）
    
ELIF 周期性数据对比：
    → 使用 Chart.js '极坐标图'
    
ELSE：
    → 默认使用'循环图'
```

**示例文件**：

- `assets/polar-chart-example.html`
- `assets/cycle-example.html`

**布局示例（PDCA循环）**：

```html
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">PDCA持续改进循环</h2>
  </div>
  <div class="slide-content">
    <div class="two-column">
      <div class="column" style="flex: 3;">
        <div class="cycle-container">
          <div class="cycle-item" style="top: 0; left: 50%; transform: translateX(-50%);">
            <div class="cycle-icon">📋</div>
            <h4>Plan 计划</h4>
            <p>制定目标与方案</p>
          </div>
          <div class="cycle-item" style="top: 50%; right: 5%;">
            <div class="cycle-icon">🚀</div>
            <h4>Do 执行</h4>
            <p>实施行动计划</p>
          </div>
          <div class="cycle-item" style="bottom: 5%; right: 25%;">
            <div class="cycle-icon">🔍</div>
            <h4>Check 检查</h4>
            <p>评估执行效果</p>
          </div>
          <div class="cycle-item" style="bottom: 5%; left: 25%;">
            <div class="cycle-icon">🔧</div>
            <h4>Act 改进</h4>
            <p>优化并标准化</p>
          </div>
        </div>
      </div>
      <div class="column" style="flex: 2;">
        <h3 class="section-heading">循环要点</h3>
        <ul class="bullet-list">
          <li><strong>持续迭代</strong>：每轮循环都是优化机会</li>
          <li><strong>闭环反馈</strong>：检查结果驱动改进</li>
          <li><strong>标准化</strong>：成功经验固化为流程</li>
          <li><strong>小步快跑</strong>：快速试错，持续改进</li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

#### 9. 因果/问题解决型（Causal/Problem-Solution）

**识别关键词**：原因、结果、问题、解决方案、根源、导致、引起、因为、所以

**决策树**：

```
IF 左侧问题，右侧解决方案：
    → 使用'问题-解决方案'（双列+箭头）
    
ELIF 80/20法则或关键因素：
    → 使用'帕累托图'（条形图+折线图）
    
ELIF 根因分析：
    → 使用'鱼骨图'（因果图）
    
ELIF KPI衡量：
    → 使用'仪表盘'（速度计样式）
    
ELSE：
    → 默认使用'问题-解决方案'
```

**示例文件**：

- `assets/problem-solution-example.html`
- `assets/pareto-chart-example.html`
- `assets/gauge-chart-example.html`
- `assets/fishbone-example.html`

**布局示例（问题-解决方案）**：

```html
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">核心问题与解决方案</h2>
  </div>
  <div class="slide-content">
    <div class="problem-solution-container">
      <div class="problem-column">
        <h3 class="problem-title">🔴 问题识别</h3>
        <div class="problem-item">
          <h4>问题一：客户流失率上升</h4>
          <p>Q3客户流失率达15%，较上季度增加5个百分点</p>
        </div>
        <div class="problem-item">
          <h4>问题二：运营成本增加</h4>
          <p>人力成本上涨20%，挤压利润空间</p>
        </div>
        <div class="problem-item">
          <h4>问题三：市场份额下降</h4>
          <p>主要竞争对手推出低价产品，抢占市场份额</p>
        </div>
      </div>
      <div class="solution-arrow">→</div>
      <div class="solution-column">
        <h3 class="solution-title">🟢 解决方案</h3>
        <div class="solution-item">
          <h4>方案一：客户关怀计划</h4>
          <p>建立客户成功团队，实施精准关怀</p>
        </div>
        <div class="solution-item">
          <h4>方案二：流程自动化</h4>
          <p>引入自动化工具，减少人力依赖</p>
        </div>
        <div class="solution-item">
          <h4>方案三：差异化竞争</h4>
          <p>强化服务优势，避免价格战</p>
        </div>
      </div>
    </div>
  </div>
</div>
```

---

## 特殊场景处理

### 内容不明确时

```
IF 内容结构不明确：
    ├─ 要点 ≤ 4个：
    │   → 使用'强调框'（安全默认选择）
    │
    ├─ 要点 5+个：
    │   → 使用'思维导图'（处理多项内容）
    │
    └─ 无法确定：
        → 要求用户澄清结构
```

### 多类型同时适用时

**优先级顺序**：

| 优先级 | 类型 | 触发条件 |
|-------|------|---------|
| 1 | 框架型 | 提及SWOT、5W1H等专业框架 |
| 2 | 时间型 | 包含日期、时间线元素 |
| 3 | 对比型 | 明确要求对比（如vs、相比） |
| 4 | 序列型 | 包含步骤、流程描述 |
| 5 | 并列型 | 默认情况，使用强调框 |

### 多部门协作流程

```
IF 流程涉及多角色/部门：
    → 使用'泳道图'（每角色/部门一条水平泳道）
```

**示例文件**：`assets/swimlane-example.html`

---

## 关键规则总结

### 必须遵守的原则

1. **图表选择原则**：
   - 数值型数据优先使用Chart.js图表
   - 概念型内容优先使用HTML/CSS可视化
   - 始终匹配可视化类型与内容结构

2. **布局原则**：
   - 图表必须使用两列或三列布局
   - 左列展示可视化，右列展示洞察分析
   - 三列布局用于多图表对比

3. **颜色原则**：
   - 严格遵循配色优先级表
   - 深蓝色（#556EE6）用于主要数据
   - 橙色（#F85d42）用于强调和重点

4. **内容原则**：
   - 100%保留所有数据点
   - 不得使用摘要替代完整内容
   - 洞察分析必须有数据支撑

### 禁止行为

| 行为 | 原因 |
|-----|------|
| 单列布局展示图表 | 浪费空间，缺乏洞察分析 |
| 纯文本要点作为结论 | 缺乏视觉化表达 |
| 跳过数据或简化内容 | 丢失关键信息 |
| 随机选择颜色 | 违反设计规范 |
| 不匹配内容结构 | 降低可读性和专业性 |

---

## 实施工作流

### 标准流程（6步）

**步骤1**：识别内容类型
- 判断是数值型数据还是概念型内容
- 确定具体的数据特征或结构类型

**步骤2**：选择可视化类型
- 根据决策树选择最合适的图表或图形
- 考虑多类型适用时的优先级

**步骤3**：确定布局方式
- 单图表选择两列布局
- 多图表对比选择三列布局
- 概念内容根据复杂度选择

**步骤4**：打开对应的示例文件
- 从`assets/`目录查找示例
- 复制CSS样式和HTML结构

**步骤5**：定制内容
- 替换实际数据和文本
- 调整颜色和尺寸

**步骤6**：集成到幻灯片
- 嵌入到slide容器中
- 添加标题和说明

### 快速参考表

| 场景 | 推荐图表 | 布局 | 示例文件 |
|-----|---------|------|---------|
| 趋势展示 | 折线图 | 两列 | `assets/line-chart-example.html` |
| 类别对比 | 柱状图 | 两列 | `assets/bar-chart-example.html` |
| 占比分析 | 环形图 | 两列 | `assets/doughnut-chart-example.html` |
| 多维对比 | 雷达图 | 两列 | `assets/radar-chart-example.html` |
| 时间线 | 时间线 | 单列 | `assets/timeline-example.html` |
| 流程 | 流程图 | 两列 | `assets/flowchart-example.html` |
| 框架 | SWOT | 矩阵 | `assets/swot-analysis-example.html` |
| 漏斗 | 漏斗图 | 两列 | `assets/funnel-chart-example.html` |
| 对比 | 对比图 | 两列 | `assets/pros-cons-example.html` |
| 循环 | 循环图 | 两列 | `assets/cycle-example.html` |
