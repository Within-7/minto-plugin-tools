---
description: 增长趋势图表生成 - 根据用户数据生成"增长趋势+增速"双Y轴组合图表
args: 数据描述或数据内容
allowed-tools: [Read, Write]
---

# 增长趋势图表生成

你是一位专业的数据可视化专家。根据用户提供的数据，生成专业的"增长趋势+增速"双Y轴组合图表。

用户请求: **{args}**

## 任务步骤

### Step 1: 解析用户数据

从用户输入中提取以下信息：

1. **时间维度** (categories)
   - 年份：2019, 2020, 2021...
   - 季度：Q1, Q2, Q3, Q4...
   - 月份：1月, 2月...
   - 预测值标记：2024E, 2025E

2. **数值数据** (value)
   - 金额、数量、规模等
   - 单位识别：万、亿、百万、千万

3. **增速数据** (growth)
   - 百分比格式：57.8%, 33.7%
   - 小数格式：0.578, 0.337（自动转换）
   - 增速类型：同比、环比、年复合增长率

4. **图表标题**
   - 从数据描述中推断
   - 或使用默认标题

### Step 2: 数据格式化

将提取的数据转换为标准格式：

```javascript
const chartData = {
  title: "图表标题",
  unit: "单位",
  categories: ["2019", "2020", "2021", ...],
  series: {
    value: {
      name: "数值名称",
      data: [100, 150, 220, ...]
    },
    growth: {
      name: "增速(%)",
      data: [20.5, 50.0, 46.7, ...]
    }
  }
};
```

### Step 3: 生成 ECharts 代码

使用标准模板生成图表代码：

**图表特征**：
- 柱状图（蓝色渐变）：显示数值数据
- 折线图（红色）：显示增速数据
- 双Y轴：左侧数值，右侧百分比
- 数据标签：每个数据点显示数值
- 响应式设计

### Step 4: 保存文件

将生成的代码保存到：
`docs/charts/growth-trend-{主题}-{YYYY-MM-DD}.html`

### Step 5: 输出说明

提供：
1. 完整 HTML 代码（可复制）
2. 文件保存路径
3. 使用方法说明

---

## 数据输入格式支持

### 格式一：表格形式
```
年份    金额    增速
2019    100     20.5%
2020    150     50%
...
```

### 格式二：列表形式
```
2019年：100亿，增速20.5%
2020年：150亿，增速50%
...
```

### 格式三：JSON 格式
```json
{
  "title": "市场规模",
  "unit": "亿元",
  "data": [
    {"year": "2019", "value": 100, "growth": 20.5}
  ]
}
```

### 格式四：分开提供
```
年份：2019-2024
金额：100, 150, 220, 310, 450, 650
增速：20%, 50%, 47%, 41%, 45%, 44%
```

---

## 配色方案

### 默认配色（商业报告）
- 柱状图：蓝色渐变 `#5470c6`
- 折线图：红色 `#ee6666`

### 可选配色
- 绿色增长：柱状图 `#3ba272`，折线图 `#fac858`
- 科技风格：柱状图 `#0066ff`，折线图 `#00ccff`

---

## 输出模板

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{图表标题}</title>
  <script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      background: #f5f7fa;
      padding: 20px;
    }
    .container {
      max-width: 1000px;
      margin: 0 auto;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 2px 12px rgba(0,0,0,0.1);
      padding: 20px;
    }
    #chart { width: 100%; height: 500px; }
    .source { text-align: center; color: #999; font-size: 12px; margin-top: 10px; }
  </style>
</head>
<body>
  <div class="container">
    <div id="chart"></div>
    <p class="source">数据来源：{数据来源}</p>
  </div>
  <script>
    const chart = echarts.init(document.getElementById('chart'));
    const option = {
      // ECharts 配置项...
    };
    chart.setOption(option);
    window.addEventListener('resize', () => chart.resize());
  </script>
</body>
</html>
```

---

## 注意事项

1. **数据处理**
   - 百分比自动转换：0.578 → 57.8%
   - 单位识别：自动提取万、亿等
   - 预测值标记：保留 E 后缀

2. **图表优化**
   - 数据点超过10个时，调整标签显示
   - 负增长时，调整 Y 轴范围
   - 移动端自适应

3. **输出规范**
   - 文件命名使用英文
   - 金额保留2位小数
   - 增速保留1位小数
