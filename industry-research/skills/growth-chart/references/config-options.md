# 增长趋势图表 - 配置参数

## 图表配置项

### 基础配置

| 参数 | 类型 | 默认值 | 说明 |
|------|------|-------|------|
| `title` | string | "市场规模及增速趋势" | 图表主标题 |
| `subtitle` | string | "" | 图表副标题 |
| `width` | string | "900px" | 图表宽度 |
| `height` | string | "500px" | 图表高度 |

### 数据配置

| 参数 | 类型 | 默认值 | 说明 |
|------|------|-------|------|
| `valueName` | string | "金额(百万)" | 数值系列名称 |
| `growthName` | string | "增速(%)" | 增速系列名称 |
| `valueUnit` | string | "百万" | 数值单位 |
| `valueDecimals` | number | 2 | 数值小数位 |
| `growthDecimals` | number | 1 | 增速小数位 |

### 颜色配置

| 参数 | 类型 | 默认值 | 说明 |
|------|------|-------|------|
| `barColor` | string | "#5470c6" | 柱状图颜色 |
| `barColorGradient` | boolean | true | 是否使用渐变 |
| `lineColor` | string | "#ee6666" | 折线图颜色 |
| `showArea` | boolean | true | 是否显示面积 |

### 标签配置

| 参数 | 类型 | 默认值 | 说明 |
|------|------|-------|------|
| `showBarLabel` | boolean | true | 显示柱状图标签 |
| `showLineLabel` | boolean | true | 显示折线图标签 |
| `labelFontSize` | number | 10 | 标签字体大小 |
| `barLabelPosition` | string | "top" | 柱状图标签位置 |
| `lineLabelPosition` | string | "top" | 折线图标签位置 |

### Y轴配置

| 参数 | 类型 | 默认值 | 说明 |
|------|------|-------|------|
| `yAxisLeftName` | string | "金额(百万)" | 左Y轴名称 |
| `yAxisRightName` | string | "增速(%)" | 右Y轴名称 |
| `yAxisRightMin` | number | 0 | 右Y轴最小值 |
| `yAxisRightMax` | number | 100 | 右Y轴最大值 |
| `autoAxisMax` | boolean | true | 自动计算Y轴最大值 |

---

## 配置示例

### 默认配置

```javascript
const defaultConfig = {
  title: "市场规模及增速趋势",
  subtitle: "",
  width: "900px",
  height: "500px",

  valueName: "金额(百万)",
  growthName: "增速(%)",
  valueUnit: "百万",
  valueDecimals: 2,
  growthDecimals: 1,

  barColor: "#5470c6",
  barColorGradient: true,
  lineColor: "#ee6666",
  showArea: true,

  showBarLabel: true,
  showLineLabel: true,
  labelFontSize: 10,

  yAxisRightMin: 0,
  yAxisRightMax: 100,
  autoAxisMax: true
};
```

### 营收报告配置

```javascript
const revenueConfig = {
  title: "年度营收及增长",
  valueName: "营收(亿元)",
  growthName: "同比增速(%)",
  valueUnit: "亿元",

  barColor: "#3ba272",    // 绿色系
  lineColor: "#fc8452",   // 橙色系

  showArea: false,        // 不显示面积
  yAxisRightMax: 80       // 最大增速80%
};
```

### 用户增长配置

```javascript
const userGrowthConfig = {
  title: "用户增长趋势",
  valueName: "用户数(万)",
  growthName: "环比增速(%)",
  valueUnit: "万",

  barColor: "#5470c6",
  lineColor: "#ee6666",

  valueDecimals: 0,       // 用户数不显示小数
  yAxisRightMin: -20,     // 允许负增长
  yAxisRightMax: 100
};
```

---

## 颜色预设

### 商业报告（默认）

```javascript
colors: {
  bar: "#5470c6",        // 蓝色
  line: "#ee6666"        // 红色
}
```

### 科技风格

```javascript
colors: {
  bar: "#0066ff",        // 科技蓝
  line: "#00ccff"        // 青色
}
```

### 绿色增长

```javascript
colors: {
  bar: "#3ba272",        // 绿色
  line: "#fac858"        // 黄色
}
```

### 简约风格

```javascript
colors: {
  bar: "#5470c6",        // 蓝色
  line: "#91cc75"        // 浅绿
}
```

---

## 柱状图渐变配置

```javascript
// 启用渐变
itemStyle: {
  color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
    { offset: 0, color: '#83bff6' },      // 顶部颜色
    { offset: 0.5, color: '#5470c6' },    // 中间颜色
    { offset: 1, color: '#3a5a8c' }       // 底部颜色
  ]),
  borderRadius: [4, 4, 0, 0]              // 顶部圆角
}

// 禁用渐变（纯色）
itemStyle: {
  color: '#5470c6',
  borderRadius: [4, 4, 0, 0]
}
```

---

## 折线图面积配置

```javascript
// 启用面积
areaStyle: {
  color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
    { offset: 0, color: 'rgba(238, 102, 102, 0.3)' },
    { offset: 1, color: 'rgba(238, 102, 102, 0.05)' }
  ])
}

// 禁用面积
areaStyle: null
```

---

## 响应式配置

```javascript
// 根据屏幕宽度调整
const isMobile = window.innerWidth < 768;

const config = {
  width: isMobile ? '100%' : '900px',
  height: isMobile ? '400px' : '500px',
  labelFontSize: isMobile ? 8 : 10,
  showBarLabel: !isMobile,      // 移动端隐藏柱状图标签
  showLineLabel: !isMobile      // 移动端隐藏折线图标签
};
```

---

## 特殊配置

### 显示数据表格

```javascript
// 在图表下方显示数据表格
showDataTable: true,
dataTableConfig: {
  header: ['年份', '金额', '增速'],
  align: 'center'
}
```

### 导出配置

```javascript
// 支持导出图片
exportConfig: {
  enabled: true,
  formats: ['png', 'svg'],
  fileName: 'growth-chart'
}
```
