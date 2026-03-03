# 打印样式模板

## 模板一：商业报告（A4纵向）

```css
/* 打印样式 - 商业报告 */
@media print {
  @page {
    size: A4 portrait;
    margin: 20mm 15mm;
    @top-center {
      content: "商业研究报告";
      font-size: 9pt;
      color: #666;
    }
    @bottom-center {
      content: "第 " counter(page) " 页";
      font-size: 9pt;
      color: #666;
    }
  }

  /* 重置背景 */
  body {
    background: #fff !important;
    color: #1a1a2e !important;
    font-family: "思源黑体", "PingFang SC", sans-serif;
    font-size: 11pt;
    line-height: 1.6;
  }

  /* 标题样式 */
  h1 {
    font-size: 24pt;
    color: #1a1a2e;
    border-bottom: 2px solid #5470c6;
    padding-bottom: 10px;
    page-break-after: avoid;
  }

  h2 {
    font-size: 18pt;
    color: #16213e;
    page-break-after: avoid;
  }

  h3 {
    font-size: 14pt;
    color: #333;
    page-break-after: avoid;
  }

  /* 表格样式 */
  table {
    width: 100%;
    border-collapse: collapse;
    page-break-inside: avoid;
  }

  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
    font-size: 10pt;
  }

  th {
    background: #f5f5f5 !important;
    color: #333 !important;
  }

  /* 图表容器 */
  .chart-container {
    page-break-inside: avoid;
    margin: 20px 0;
  }

  /* 隐藏非打印元素 */
  nav, .sidebar, .ads, .no-print {
    display: none !important;
  }

  /* 链接显示URL */
  a[href]:after {
    content: " (" attr(href) ")";
    font-size: 9pt;
    color: #666;
  }
}
```

---

## 模板二：图表报告（A4横向）

```css
/* 打印样式 - 图表报告 */
@media print {
  @page {
    size: A4 landscape;
    margin: 15mm;
  }

  body {
    background: #fff !important;
  }

  /* 图表全宽显示 */
  .chart-container, #chart {
    width: 257mm !important;
    max-width: 257mm !important;
    height: auto !important;
  }

  /* 每页一个图表 */
  .chart-page {
    page-break-after: always;
    page-break-inside: avoid;
  }

  .chart-page:last-child {
    page-break-after: avoid;
  }

  /* 图表标题 */
  .chart-title {
    font-size: 16pt;
    font-weight: bold;
    color: #1a1a2e;
    margin-bottom: 10px;
  }

  /* 数据来源 */
  .chart-source {
    font-size: 9pt;
    color: #666;
    margin-top: 10px;
  }

  /* 页码 */
  @bottom-right {
    content: counter(page) " / " counter(pages);
  }
}
```

---

## 模板三：简约风格（A4纵向）

```css
/* 打印样式 - 简约风格 */
@media print {
  @page {
    size: A4 portrait;
    margin: 25mm 20mm;
  }

  body {
    font-family: "Helvetica Neue", Arial, sans-serif;
    font-size: 11pt;
    color: #2c3e50;
    line-height: 1.8;
  }

  h1 {
    font-size: 22pt;
    color: #2c3e50;
    font-weight: 300;
    margin-bottom: 20px;
  }

  h2 {
    font-size: 16pt;
    color: #34495e;
    font-weight: 400;
    margin-top: 25px;
  }

  p {
    margin-bottom: 12px;
    text-align: justify;
  }

  /* 强调色 */
  .highlight {
    color: #3498db;
  }

  /* 引用块 */
  blockquote {
    border-left: 3px solid #3498db;
    padding-left: 15px;
    color: #7f8c8d;
    font-style: italic;
  }

  /* 列表 */
  ul, ol {
    margin-left: 20px;
    margin-bottom: 12px;
  }

  li {
    margin-bottom: 6px;
  }
}
```

---

## 模板四：科技风格（A4纵向）

```css
/* 打印样式 - 科技风格 */
@media print {
  @page {
    size: A4 portrait;
    margin: 20mm;
    @top-left {
      content: "CONFIDENTIAL";
      font-size: 8pt;
      color: #999;
      text-transform: uppercase;
    }
  }

  body {
    font-family: "SF Pro Display", "Segoe UI", sans-serif;
    font-size: 10pt;
    color: #0f3460;
  }

  /* 深色标题 */
  h1 {
    font-size: 28pt;
    font-weight: 700;
    color: #0f3460;
    letter-spacing: -0.5px;
  }

  h2 {
    font-size: 18pt;
    font-weight: 600;
    color: #16213e;
    border-left: 4px solid #533483;
    padding-left: 12px;
  }

  /* 代码块 */
  pre, code {
    font-family: "JetBrains Mono", "Consolas", monospace;
    font-size: 9pt;
    background: #f8f9fa !important;
    padding: 10px;
    border-radius: 4px;
  }

  /* 数据表格 */
  .data-table {
    border: none;
  }

  .data-table th {
    background: #0f3460 !important;
    color: #fff !important;
    font-weight: 500;
  }

  .data-table td {
    border-bottom: 1px solid #e0e0e0;
  }

  .data-table tr:nth-child(even) {
    background: #f8f9fa !important;
  }
}
```

---

## 模板五：多页报告（完整版）

```html
<style>
@media print {
  /* 页面设置 */
  @page {
    size: A4 portrait;
    margin: 25mm 20mm 30mm 20mm;
  }

  @page :first {
    margin-top: 30mm;
  }

  /* 页眉 */
  @top-left {
    content: element(header);
  }

  /* 页脚 */
  @bottom-center {
    content: element(footer);
  }

  /* 重置 */
  body {
    background: #fff !important;
    font-family: "思源宋体", "Noto Serif SC", serif;
    font-size: 11pt;
    color: #333;
    line-height: 1.8;
  }

  /* 封面 */
  .cover {
    page-break-after: always;
    text-align: center;
    padding-top: 100px;
  }

  .cover h1 {
    font-size: 32pt;
    margin-bottom: 30px;
  }

  .cover .subtitle {
    font-size: 16pt;
    color: #666;
  }

  .cover .meta {
    margin-top: 100px;
    font-size: 12pt;
    color: #999;
  }

  /* 目录 */
  .toc {
    page-break-after: always;
  }

  .toc h2 {
    font-size: 18pt;
    border-bottom: 1px solid #333;
    padding-bottom: 10px;
  }

  .toc-item {
    display: flex;
    justify-content: space-between;
    padding: 5px 0;
    border-bottom: 1px dotted #ccc;
  }

  /* 正文 */
  .content h2 {
    font-size: 16pt;
    page-break-after: avoid;
  }

  .content h3 {
    font-size: 14pt;
    page-break-after: avoid;
  }

  /* 图表 */
  figure {
    page-break-inside: avoid;
    margin: 20px 0;
    text-align: center;
  }

  figure img {
    max-width: 100%;
  }

  figcaption {
    font-size: 10pt;
    color: #666;
    margin-top: 8px;
  }

  /* 表格 */
  table {
    page-break-inside: avoid;
    width: 100%;
  }

  /* 页眉元素 */
  #header {
    position: running(header);
    font-size: 9pt;
    color: #666;
    border-bottom: 1px solid #ccc;
    padding-bottom: 5px;
  }

  /* 页脚元素 */
  #footer {
    position: running(footer);
    font-size: 9pt;
    color: #666;
    text-align: center;
  }

  #footer .page-number::after {
    content: counter(page);
  }

  #footer .total-pages::after {
    content: counter(pages);
  }

  /* 隐藏屏幕元素 */
  .screen-only {
    display: none !important;
  }
}
</style>
```

---

## 快速应用

### 最小化打印样式

```css
@media print {
  body { background: #fff; }
  nav, .sidebar, footer { display: none; }
  .no-print { display: none !important; }
}
```

### ECharts 图表打印优化

```css
@media print {
  .chart-container canvas {
    max-width: 100% !important;
    height: auto !important;
  }

  /* 确保图表不被分页 */
  .chart-container {
    page-break-inside: avoid;
  }
}
```
