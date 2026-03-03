---
name: print-layout
description: |
  HTML页面打印排版技能。将HTML文件改造为适合打印的专业排版页面。
  触发词：打印排版、打印样式、print layout、PDF导出、A4排版、打印配置、页面排版
---

# HTML页面打印排版技能

## 概述

这是一个专业的HTML页面打印排版技能，根据用户提供的配置（风格、字体、颜色、宽高比、打印边距等），将HTML文件改造为适合打印的专业排版页面。

## 核心能力

### 1. 页面尺寸配置

| 纸张尺寸 | 宽×高 (mm) | 宽×高 (px @96dpi) |
|---------|-----------|------------------|
| A4 | 210×297 | 794×1123 |
| A3 | 297×420 | 1123×1587 |
| Letter | 216×279 | 816×1056 |
| Legal | 216×356 | 816×1344 |

### 2. 打印边距配置

| 边距类型 | 常用值 | 说明 |
|---------|-------|------|
| 无边距 | 0mm | 全出血打印 |
| 窄边距 | 10mm | 最小边距 |
| 标准边距 | 20mm | 常用边距 |
| 宽边距 | 25mm | 适合装订 |

### 3. 字体配置

| 场景 | 推荐字体 | 字号 |
|------|---------|------|
| 标题 | 思源黑体、PingFang SC | 18-24pt |
| 正文 | 思源宋体、PingFang SC | 10-12pt |
| 表格 | Arial、Helvetica | 9-10pt |
| 代码 | JetBrains Mono、Consolas | 9pt |

### 4. 颜色配置

| 风格 | 主色调 | 适用场景 |
|------|-------|---------|
| 商业报告 | #1a1a2e / #16213e | 正式报告 |
| 科技风格 | #0f3460 / #533483 | 技术文档 |
| 简约风格 | #2c3e50 / #34495e | 通用文档 |
| 彩色风格 | #5470c6 / #ee6666 | 图表报告 |

## 配置参数

### 输入配置格式

```json
{
  "style": "business|tech|minimal|colorful",
  "paperSize": "A4|A3|Letter|Legal",
  "orientation": "portrait|landscape",
  "margin": {
    "top": "20mm",
    "right": "20mm",
    "bottom": "20mm",
    "left": "20mm"
  },
  "font": {
    "title": "思源黑体",
    "body": "思源宋体",
    "titleSize": "18pt",
    "bodySize": "11pt"
  },
  "color": {
    "primary": "#1a1a2e",
    "secondary": "#5470c6",
    "text": "#333333"
  },
  "printOptions": {
    "showPageNumber": true,
    "showHeader": true,
    "showFooter": true,
    "headerText": "",
    "footerText": ""
  }
}
```

## 处理流程

### Step 1: 解析配置

1. 读取用户提供的配置参数
2. 验证配置有效性
3. 应用默认值填充缺失配置

### Step 2: 生成打印样式

1. 创建 `@page` 规则
2. 创建 `@media print` 样式
3. 配置字体和颜色
4. 设置页面边距

### Step 3: 改造HTML

1. 添加打印样式 `<style>` 标签
2. 调整元素布局
3. 隐藏非打印元素
4. 优化图表尺寸

### Step 4: 输出文件

1. 生成改造后的HTML文件
2. 提供打印预览建议

## 相关命令

| 命令 | 用途 |
|------|------|
| `/print-layout <HTML文件> <配置>` | 改造HTML为打印排版 |

## 参考文档

- [纸张尺寸规格](./references/paper-sizes.md)
- [打印样式模板](./references/print-templates.md)
- [配置参数说明](./references/config-reference.md)

## 使用示例

### 示例1：A4商业报告

```
用户: 将 report.html 改造为A4打印格式
      风格：商业报告
      边距：上下20mm，左右15mm
      字体：思源黑体

AI: [生成打印样式，改造HTML，输出文件]
```

### 示例2：A3横向图表

```
用户: 将 charts.html 改造为打印格式
      纸张：A3横向
      边距：10mm
      显示页码

AI: [生成A3横向打印样式，添加页码，输出文件]
```

## 注意事项

1. **图表优化**：确保ECharts图表在打印时清晰可见
2. **颜色检查**：打印时深色背景可能变黑，建议浅色系
3. **分页控制**：避免图表被分页截断
4. **字体加载**：确保打印时字体已加载完成
5. **测试验证**：使用浏览器打印预览（Ctrl+P）测试效果
