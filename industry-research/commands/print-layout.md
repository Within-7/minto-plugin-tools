---
description: HTML打印排版 - 将HTML文件改造为适合配置要求的打印排版页面
args: HTML文件路径 [配置参数]
allowed-tools: [Read, Write, Grep, Glob]
---

# HTML打印排版

你是一位专业的排版设计师。根据用户提供的配置，将HTML文件改造为适合打印的专业排版页面。

用户请求: **{args}**

## 任务步骤

### Step 1: 解析输入

1. 获取HTML文件路径
2. 解析配置参数（风格、字体、颜色、边距等）
3. 应用默认值填充缺失配置

### Step 2: 读取HTML文件

1. 读取原始HTML内容
2. 分析现有结构
3. 识别需要保留/隐藏的元素

### Step 3: 生成打印样式

根据配置生成 `@media print` 样式：

```css
@media print {
  @page {
    size: {paperSize} {orientation};
    margin: {margin};
  }

  body {
    font-family: {fontFamily};
    font-size: {fontSize};
    color: {textColor};
    background: {bgColor};
  }

  /* ... 其他样式 */
}
```

### Step 4: 改造HTML

1. 在 `<head>` 中添加打印样式 `<style>` 标签
2. 调整元素类名和属性
3. 添加页眉页脚元素（如需要）
4. 设置分页控制

### Step 5: 输出文件

保存改造后的HTML到：
`{原文件名}-print.html`

---

## 配置参数格式

### 简化格式（推荐）

```
风格: business
纸张: A4
方向: 纵向
边距: 20mm
字体: 思源黑体
```

### JSON格式

```json
{
  "style": "business",
  "paperSize": "A4",
  "orientation": "portrait",
  "margin": {"top": "25mm", "right": "20mm", "bottom": "30mm", "left": "20mm"},
  "font": {"title": "思源黑体", "body": "思源宋体", "bodySize": "11pt"},
  "color": {"primary": "#1a1a2e", "text": "#333"}
}
```

---

## 预设风格

| 风格 | 特点 | 适用场景 |
|------|------|---------|
| business | 专业、深色调 | 商业报告、研究文档 |
| tech | 现代、科技感 | 技术文档、产品说明 |
| minimal | 简约、大边距 | 通用文档、简报 |
| colorful | 彩色、活力 | 图表报告、演示文档 |

---

## 纸张规格

| 纸张 | 尺寸 | 横向有效区域(20mm边距) |
|------|------|----------------------|
| A4 | 210×297mm | 170×257mm |
| A3 | 297×420mm | 257×380mm |
| Letter | 216×279mm | 176×239mm |

---

## 输出示例

### 输入

```
/print-layout report.html
      风格: business
      纸张: A4
      边距: 上下25mm，左右20mm
      显示页码
```

### 输出

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>报告</title>
  <style>
    /* 原有样式 */

    @media print {
      @page {
        size: A4 portrait;
        margin: 25mm 20mm;
      }

      body {
        font-family: "思源黑体", sans-serif;
        font-size: 11pt;
        color: #1a1a2e;
        background: #fff;
      }

      /* 页脚页码 */
      @bottom-center {
        content: "第 " counter(page) " 页";
        font-size: 9pt;
        color: #666;
      }

      /* 分页控制 */
      h1, h2, h3 { page-break-after: avoid; }
      table, figure { page-break-inside: avoid; }

      /* 隐藏非打印元素 */
      nav, .sidebar, .no-print { display: none !important; }
    }
  </style>
</head>
<body>
  <!-- 原有内容 -->
</body>
</html>
```

---

## 注意事项

1. **图表优化**
   - 确保ECharts图表在打印时清晰
   - 设置合适的canvas分辨率
   - 避免图表被分页截断

2. **颜色处理**
   - 深色背景在打印时可能变黑
   - 建议使用浅色背景或白色背景
   - 确保文字与背景对比度足够

3. **分页控制**
   - 表格、图表设置 `page-break-inside: avoid`
   - 标题设置 `page-break-after: avoid`
   - 必要时手动插入分页符

4. **测试验证**
   - 使用浏览器打印预览（Ctrl+P）测试
   - 检查不同页面的显示效果
   - 验证页眉页脚位置
