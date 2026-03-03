# 配置参数说明

## 完整配置结构

```typescript
interface PrintLayoutConfig {
  // 基础配置
  style: 'business' | 'tech' | 'minimal' | 'colorful';
  paperSize: 'A4' | 'A3' | 'Letter' | 'Legal';
  orientation: 'portrait' | 'landscape';
  dpi: 96 | 150 | 200 | 300;

  // 边距配置
  margin: {
    top: string;      // 如 "20mm"
    right: string;
    bottom: string;
    left: string;
  };

  // 字体配置
  font: {
    title: string;      // 标题字体
    body: string;       // 正文字体
    titleSize: string;  // 标题字号，如 "18pt"
    bodySize: string;   // 正文字号
    lineHeight: number; // 行高，如 1.6
  };

  // 颜色配置
  color: {
    primary: string;    // 主色调
    secondary: string;  // 次要色调
    accent: string;     // 强调色
    text: string;       // 文字颜色
    background: string; // 背景色
  };

  // 页眉页脚
  header: {
    show: boolean;
    text: string;
    align: 'left' | 'center' | 'right';
    fontSize: string;
  };

  footer: {
    show: boolean;
    text: string;
    showPageNumber: boolean;
    align: 'left' | 'center' | 'right';
    fontSize: string;
  };

  // 打印选项
  printOptions: {
    showPageNumber: boolean;
    showHeaderOnFirstPage: boolean;
    avoidBreakInside: string[];  // 避免分页的元素选择器
    forceBreakBefore: string[];  // 强制分页前的元素选择器
    hideElements: string[];      // 隐藏的元素选择器
    showLinkUrl: boolean;        // 是否显示链接URL
  };
}
```

---

## 预设风格配置

### 商业报告 (business)

```json
{
  "style": "business",
  "paperSize": "A4",
  "orientation": "portrait",
  "margin": {
    "top": "25mm",
    "right": "20mm",
    "bottom": "30mm",
    "left": "20mm"
  },
  "font": {
    "title": "思源黑体",
    "body": "思源宋体",
    "titleSize": "24pt",
    "bodySize": "11pt",
    "lineHeight": 1.8
  },
  "color": {
    "primary": "#1a1a2e",
    "secondary": "#5470c6",
    "accent": "#ee6666",
    "text": "#333333",
    "background": "#ffffff"
  },
  "header": {
    "show": true,
    "text": "商业研究报告",
    "align": "center",
    "fontSize": "9pt"
  },
  "footer": {
    "show": true,
    "showPageNumber": true,
    "align": "center",
    "fontSize": "9pt"
  }
}
```

### 科技风格 (tech)

```json
{
  "style": "tech",
  "paperSize": "A4",
  "orientation": "portrait",
  "margin": {
    "top": "20mm",
    "right": "20mm",
    "bottom": "20mm",
    "left": "20mm"
  },
  "font": {
    "title": "SF Pro Display",
    "body": "SF Pro Text",
    "titleSize": "28pt",
    "bodySize": "10pt",
    "lineHeight": 1.6
  },
  "color": {
    "primary": "#0f3460",
    "secondary": "#533483",
    "accent": "#00f2f2",
    "text": "#16213e",
    "background": "#ffffff"
  }
}
```

### 简约风格 (minimal)

```json
{
  "style": "minimal",
  "paperSize": "A4",
  "orientation": "portrait",
  "margin": {
    "top": "25mm",
    "right": "25mm",
    "bottom": "25mm",
    "left": "25mm"
  },
  "font": {
    "title": "Helvetica Neue",
    "body": "Helvetica Neue",
    "titleSize": "22pt",
    "bodySize": "11pt",
    "lineHeight": 1.8
  },
  "color": {
    "primary": "#2c3e50",
    "secondary": "#34495e",
    "accent": "#3498db",
    "text": "#2c3e50",
    "background": "#ffffff"
  }
}
```

### 彩色风格 (colorful)

```json
{
  "style": "colorful",
  "paperSize": "A4",
  "orientation": "portrait",
  "margin": {
    "top": "20mm",
    "right": "15mm",
    "bottom": "20mm",
    "left": "15mm"
  },
  "font": {
    "title": "PingFang SC",
    "body": "PingFang SC",
    "titleSize": "20pt",
    "bodySize": "11pt",
    "lineHeight": 1.6
  },
  "color": {
    "primary": "#5470c6",
    "secondary": "#91cc75",
    "accent": "#ee6666",
    "text": "#333333",
    "background": "#ffffff"
  }
}
```

---

## 参数详解

### 1. 纸张尺寸 (paperSize)

| 值 | 说明 | 适用场景 |
|---|------|---------|
| A4 | 210×297mm | 标准报告、文档 |
| A3 | 297×420mm | 大型图表、海报 |
| Letter | 216×279mm | 北美标准 |
| Legal | 216×356mm | 法律文件 |

### 2. 方向 (orientation)

| 值 | 说明 | 适用场景 |
|---|------|---------|
| portrait | 纵向 | 文字报告、表格 |
| landscape | 横向 | 图表、宽表格 |

### 3. 边距 (margin)

**推荐值：**

| 场景 | 上 | 右 | 下 | 左 |
|------|---|---|---|---|
| 标准报告 | 25mm | 20mm | 30mm | 20mm |
| 图表报告 | 15mm | 15mm | 20mm | 15mm |
| 简约文档 | 25mm | 25mm | 25mm | 25mm |
| 装订报告 | 25mm | 20mm | 25mm | 30mm |

### 4. 字体 (font)

**中文字体推荐：**

| 字体 | 类型 | 适用场景 |
|------|------|---------|
| 思源黑体 | 无衬线 | 标题、商业报告 |
| 思源宋体 | 衬线 | 正文、正式文档 |
| PingFang SC | 无衬线 | 苹果系统默认 |
| 方正黑体 | 无衬线 | 传统印刷 |

**英文字体推荐：**

| 字体 | 类型 | 适用场景 |
|------|------|---------|
| Helvetica Neue | 无衬线 | 现代简约 |
| Times New Roman | 衬线 | 正式文档 |
| Arial | 无衬线 | 通用 |
| Georgia | 衬线 | 阅读优化 |

### 5. 字号参考

| 元素 | 推荐字号 |
|------|---------|
| 主标题 H1 | 22-28pt |
| 副标题 H2 | 16-20pt |
| 小标题 H3 | 14-16pt |
| 正文 | 10-12pt |
| 注释 | 8-9pt |
| 页眉页脚 | 8-9pt |

### 6. 颜色建议

**打印友好颜色：**

```css
/* 深色系 - 打印清晰 */
--dark-primary: #1a1a2e;
--dark-secondary: #16213e;
--dark-text: #333333;

/* 浅色系 - 适合背景 */
--light-bg: #ffffff;
--light-gray: #f5f5f5;
--light-border: #e0e0e0;

/* 强调色 - 少量使用 */
--accent-blue: #5470c6;
--accent-red: #ee6666;
--accent-green: #91cc75;
```

**避免：**
- 深色背景（打印时可能变黑）
- 低对比度颜色组合
- 过多彩色（黑白打印时会丢失）

---

## 常见问题

### Q1: 图表打印模糊

```json
{
  "dpi": 200,
  "printOptions": {
    "chartScale": 2
  }
}
```

### Q2: 表格被分页截断

```json
{
  "printOptions": {
    "avoidBreakInside": ["table", ".chart-container", "figure"]
  }
}
```

### Q3: 页眉页脚不显示

确保在HTML中添加对应元素：

```html
<div id="header">页眉内容</div>
<div id="footer">
  第 <span class="page-number"></span> 页
</div>
```
