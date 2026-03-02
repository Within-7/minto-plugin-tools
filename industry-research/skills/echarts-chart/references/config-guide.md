# ECharts 配置项说明

## 基础结构

```javascript
const option = {
  title: {},      // 标题配置
  tooltip: {},    // 提示框配置
  legend: {},     // 图例配置
  grid: {},       // 网格配置
  xAxis: {},      // X轴配置
  yAxis: {},      // Y轴配置
  series: []      // 系列数据配置
};
```

---

## Title 标题

```javascript
title: {
  text: '主标题',           // 主标题文本
  subtext: '副标题',        // 副标题文本
  left: 'center',          // 位置：left/center/right
  top: 10,                 // 上边距
  textStyle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333'
  }
}
```

---

## Tooltip 提示框

```javascript
tooltip: {
  trigger: 'axis',         // 触发方式：axis/item
  axisPointer: {
    type: 'shadow'         // 指示器类型：shadow/line/cross
  },
  formatter: '{b}<br/>{a}: {c}'  // 自定义格式
}
```

### 常用 formatter

| 变量 | 含义 |
|------|------|
| {a} | 系列名称 |
| {b} | 数据名称 |
| {c} | 数据值 |
| {d} | 百分比（饼图） |

---

## Legend 图例

```javascript
legend: {
  data: ['系列1', '系列2'],  // 图例数据
  orient: 'horizontal',     // 方向：horizontal/vertical
  left: 'center',           // 位置
  bottom: 10,               // 底部距离
  itemWidth: 25,            // 图例宽度
  itemHeight: 14            // 图例高度
}
```

---

## Grid 网格

```javascript
grid: {
  left: '3%',
  right: '4%',
  bottom: '15%',
  top: '15%',
  containLabel: true        // 包含坐标轴标签
}
```

---

## Axis 坐标轴

### X轴（类目轴）

```javascript
xAxis: {
  type: 'category',         // 类型：category/value
  data: ['A', 'B', 'C'],    // 类目数据
  axisLabel: {
    interval: 0,            // 标签显示间隔，0=全部显示
    rotate: 30              // 旋转角度
  },
  axisLine: {
    lineStyle: { color: '#666' }
  }
}
```

### Y轴（数值轴）

```javascript
yAxis: {
  type: 'value',
  name: '单位',             // 轴名称
  nameLocation: 'end',      // 名称位置
  axisLabel: {
    formatter: '{value}'    // 标签格式化
  },
  splitLine: {
    lineStyle: { type: 'dashed' }
  }
}
```

### 双Y轴配置

```javascript
yAxis: [
  {
    type: 'value',
    name: '金额(万)',
    position: 'left'
  },
  {
    type: 'value',
    name: '增速(%)',
    position: 'right',
    axisLabel: { formatter: '{value}%' }
  }
]
```

---

## Series 系列

### 柱状图

```javascript
{
  name: '系列名称',
  type: 'bar',
  data: [100, 200, 300],
  barWidth: '30%',          // 柱宽度
  itemStyle: {
    color: '#5470c6',       // 柱颜色
    borderRadius: [4, 4, 0, 0]  // 圆角
  },
  label: {
    show: true,             // 显示标签
    position: 'top',        // 位置：top/inside
    formatter: '{c}'
  }
}
```

### 折线图

```javascript
{
  name: '系列名称',
  type: 'line',
  data: [100, 200, 300],
  yAxisIndex: 0,            // 使用的Y轴索引
  smooth: true,             // 平滑曲线
  symbol: 'circle',         // 标记点形状
  symbolSize: 8,            // 标记点大小
  lineStyle: {
    width: 2,
    color: '#ee6666'
  },
  label: {
    show: true,
    position: 'top'
  }
}
```

### 饼图

```javascript
{
  type: 'pie',
  radius: ['40%', '70%'],   // 内外半径（环形图）
  center: ['50%', '50%'],   // 圆心位置
  avoidLabelOverlap: true,
  itemStyle: {
    borderRadius: 10,
    borderColor: '#fff',
    borderWidth: 2
  },
  label: {
    show: true,
    formatter: '{b}: {d}%'
  },
  data: [
    { value: 1048, name: 'A' },
    { value: 735, name: 'B' }
  ]
}
```

---

## 常用组合配置

### 柱状图+折线图（双Y轴）

```javascript
series: [
  {
    name: '金额',
    type: 'bar',
    yAxisIndex: 0,
    data: [...]
  },
  {
    name: '增速',
    type: 'line',
    yAxisIndex: 1,          // 使用第二个Y轴
    data: [...]
  }
]
```

### 堆叠柱状图

```javascript
series: [
  {
    name: 'A',
    type: 'bar',
    stack: 'total',         // 相同stack值会堆叠
    data: [...]
  },
  {
    name: 'B',
    type: 'bar',
    stack: 'total',
    data: [...]
  }
]
```

---

## 完整HTML模板

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>图表标题</title>
  <script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
  <style>
    body { margin: 0; padding: 20px; background: #f5f5f5; }
    #chart { width: 900px; height: 500px; margin: 0 auto; background: #fff; }
  </style>
</head>
<body>
  <div id="chart"></div>
  <script>
    const chart = echarts.init(document.getElementById('chart'));
    const option = {
      // 配置项...
    };
    chart.setOption(option);
    window.addEventListener('resize', () => chart.resize());
  </script>
</body>
</html>
```
