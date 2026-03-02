# ECharts 常用图表模板

## 1. 双Y轴组合图（柱状图+折线图）

适用场景：展示数值与增速、销售额与增长率

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>双Y轴组合图</title>
  <script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
</head>
<body>
  <div id="chart" style="width: 900px; height: 500px;"></div>
  <script>
    const chart = echarts.init(document.getElementById('chart'));
    const option = {
      title: {
        text: '市场规模及增速',
        left: 'center'
      },
      tooltip: {
        trigger: 'axis',
        axisPointer: { type: 'cross' }
      },
      legend: {
        data: ['金额(百万)', '增速(%)'],
        bottom: 10
      },
      grid: {
        left: '3%',
        right: '4%',
        bottom: '15%',
        containLabel: true
      },
      xAxis: {
        type: 'category',
        data: ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024E'],
        axisLabel: { interval: 0 }
      },
      yAxis: [
        {
          type: 'value',
          name: '金额(百万)',
          position: 'left',
          axisLabel: { formatter: '{value}' }
        },
        {
          type: 'value',
          name: '增速(%)',
          position: 'right',
          axisLabel: { formatter: '{value}%' },
          min: 0,
          max: 100
        }
      ],
      series: [
        {
          name: '金额(百万)',
          type: 'bar',
          data: [578.31, 773.13, 1118.42, 1401.06, 1596.11, 1801.92, 2108.99, 2834.17, 4167.44, 7185.38],
          itemStyle: { color: '#5470c6' },
          label: {
            show: true,
            position: 'top',
            fontSize: 10,
            formatter: '{c}'
          }
        },
        {
          name: '增速(%)',
          type: 'line',
          yAxisIndex: 1,
          data: [57.8, 33.7, 44.7, 25.3, 13.9, 12.9, 17.0, 34.4, 47.0, 72.4],
          itemStyle: { color: '#ee6666' },
          label: {
            show: true,
            position: 'top',
            formatter: '{c}%'
          }
        }
      ]
    };
    chart.setOption(option);
  </script>
</body>
</html>
```

---

## 2. 多系列柱状图

适用场景：多年份对比、多产品对比

```javascript
option = {
  title: { text: '各季度销售额对比', left: 'center' },
  tooltip: { trigger: 'axis' },
  legend: { data: ['2022', '2023', '2024'], bottom: 10 },
  xAxis: {
    type: 'category',
    data: ['Q1', 'Q2', 'Q3', 'Q4']
  },
  yAxis: {
    type: 'value',
    name: '销售额(万元)'
  },
  series: [
    {
      name: '2022',
      type: 'bar',
      data: [100, 150, 180, 200]
    },
    {
      name: '2023',
      type: 'bar',
      data: [120, 180, 210, 240]
    },
    {
      name: '2024',
      type: 'bar',
      data: [150, 200, 250, 300]
    }
  ]
};
```

---

## 3. 堆叠柱状图

适用场景：展示构成变化、成本结构

```javascript
option = {
  title: { text: '收入构成分析', left: 'center' },
  tooltip: { trigger: 'axis' },
  legend: { data: ['产品销售', '服务收入', '其他收入'], bottom: 10 },
  xAxis: {
    type: 'category',
    data: ['2020', '2021', '2022', '2023', '2024']
  },
  yAxis: { type: 'value', name: '收入(万元)' },
  series: [
    {
      name: '产品销售',
      type: 'bar',
      stack: 'total',
      data: [320, 380, 420, 480, 550]
    },
    {
      name: '服务收入',
      type: 'bar',
      stack: 'total',
      data: [120, 180, 250, 320, 400]
    },
    {
      name: '其他收入',
      type: 'bar',
      stack: 'total',
      data: [30, 40, 50, 60, 80]
    }
  ]
};
```

---

## 4. 饼图

适用场景：市场份额、占比分析

```javascript
option = {
  title: { text: '市场份额分布', left: 'center' },
  tooltip: {
    trigger: 'item',
    formatter: '{b}: {c}万 ({d}%)'
  },
  legend: { orient: 'vertical', left: 'left' },
  series: [
    {
      type: 'pie',
      radius: ['40%', '70%'],
      avoidLabelOverlap: false,
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
        { value: 1048, name: '企业A' },
        { value: 735, name: '企业B' },
        { value: 580, name: '企业C' },
        { value: 484, name: '企业D' },
        { value: 300, name: '其他' }
      ]
    }
  ]
};
```

---

## 5. 多折线图

适用场景：多指标趋势对比

```javascript
option = {
  title: { text: '关键指标趋势', left: 'center' },
  tooltip: { trigger: 'axis' },
  legend: { data: ['营收', '利润', '用户数(万)'], bottom: 10 },
  xAxis: {
    type: 'category',
    data: ['2020', '2021', '2022', '2023', '2024']
  },
  yAxis: { type: 'value' },
  series: [
    {
      name: '营收',
      type: 'line',
      data: [820, 932, 1101, 1534, 1890],
      smooth: true
    },
    {
      name: '利润',
      type: 'line',
      data: [620, 732, 901, 1234, 1490],
      smooth: true
    },
    {
      name: '用户数(万)',
      type: 'line',
      data: [150, 230, 380, 560, 820],
      smooth: true
    }
  ]
};
```

---

## 6. 面积图

适用场景：累积趋势、市场份额变化

```javascript
option = {
  title: { text: '累计销售额', left: 'center' },
  tooltip: { trigger: 'axis' },
  xAxis: {
    type: 'category',
    data: ['1月', '2月', '3月', '4月', '5月', '6月']
  },
  yAxis: { type: 'value', name: '累计(万元)' },
  series: [
    {
      type: 'line',
      data: [100, 230, 410, 680, 950, 1300],
      areaStyle: {},
      smooth: true
    }
  ]
};
```

---

## 配色方案

### 商业报告（推荐）
```javascript
color: ['#5470c6', '#ee6666', '#91cc75', '#fac858', '#73c0de', '#3ba272', '#fc8452']
```

### 科技风格
```javascript
color: ['#00f2f2', '#0066ff', '#ff00cc', '#ffcc00', '#00ff66']
```

### 简约风格
```javascript
color: ['#5470c6', '#91cc75', '#fac858', '#ee6666']
```
