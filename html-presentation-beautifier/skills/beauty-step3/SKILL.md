---
name: "beauty-step3"
description: "HTML样式布局代码规划与生成。在beauty命令的步骤3执行时自动调用，将幻灯片内容转换为完整的McKinsey风格HTML文件，包含CSS样式、布局设计和交互功能。"
---

# Beauty 步骤3：HTML样式布局代码规划与生成

## 目标

将步骤2生成的幻灯片页面清单转换为完整的、可运行的McKinsey风格HTML文件。

## ⚠️ 核心原则

**🔑 必须读取并参考skill资源：**
- **必须读** `beauty-html/references/best-practices.md`
- **必须读** `beauty-html/references/mckinsey-design-system.md`
- **必须读** `beauty-html/assets/presentation-template.html`
- **必须读** `beauty-html/assets/TEMPLATE_USAGE_GUIDE.md`

**⚠️ Token限制处理原则：**

**当遇到 token 限制或上下文长度问题时，必须使用"继续"分页方式，绝对禁止：**
- ❌ 压缩或省略资源读取
- ❌ 跳过必读资源
- ❌ 简化执行步骤
- ❌ 减少生成内容
- ❌ 使用摘要代替完整内容

**正确处理方式：使用"继续"机制**
```
1. 在完成当前可执行的部分后
2. 明确说明："由于 token 限制，任务未完成，请输入'继续'以获取剩余部分"
3. 等待用户输入"继续"后
4. 继续执行剩余步骤
5. 重复直到任务完全完成
```

## 📋 执行流程（4个子步骤）

```
步骤3.1：读取必读资源
  ↓
步骤3.2：为每页规划代码方案
  ↓
步骤3.3：生成完整HTML文件
  ↓
步骤3.4：验证代码质量
```

---

## 步骤 3.1：读取必读资源

### 目标

完整读取所有必读资源，为后续代码生成提供参考。

### 必读资源清单

```
1. beauty-html/references/best-practices.md
   - HTML最佳实践
   - 语义化标签使用
   - 可访问性要求

2. beauty-html/references/mckinsey-design-system.md
   - McKinsey配色方案
   - 字体规范
   - 间距标准
   - 布局原则

3. beauty-html/assets/presentation-template.html
   - HTML结构模板
   - 导航功能
   - 响应式设计

4. beauty-html/assets/TEMPLATE_USAGE_GUIDE.md
   - 模板使用指南
   - 组件说明
   - 自定义方法
```

### 执行要求

**阶段1：读取best-practices.md**

```
使用 Read 工具读取：
Read: beauty-html/references/best-practices.md

如果文件过长，分批读取：
├─ 阶段1a：读取前500行
├─ 输出："步骤3.1阶段1a完成 - 已读取best-practices.md前半部分
       请输入'继续'以读取后半部分"
├─ 【等待用户输入"继续"】
└─ 阶段1b：读取剩余部分
```

**阶段2：读取mckinsey-design-system.md**

```
使用 Read 工具读取：
Read: beauty-html/references/mckinsey-design-system.md

如果文件过长，分批读取：
├─ 阶段2a：读取前500行
├─ 输出："步骤3.1阶段2a完成 - 已读取mckinsey-design-system.md前半部分
       请输入'继续'以读取后半部分"
├─ 【等待用户输入"继续"】
└─ 阶段2b：读取剩余部分
```

**阶段3：读取presentation-template.html**

```
使用 Read 工具读取：
Read: beauty-html/assets/presentation-template.html

如果文件过长，分批读取：
├─ 阶段3a：读取前500行
├─ 输出："步骤3.1阶段3a完成 - 已读取presentation-template.html前半部分
       请输入'继续'以读取后半部分"
├─ 【等待用户输入"继续"】
└─ 阶段3b：读取剩余部分
```

**阶段4：读取TEMPLATE_USAGE_GUIDE.md**

```
使用 Read 工具读取：
Read: beauty-html/assets/TEMPLATE_USAGE_GUIDE.md

如果文件过长，分批读取：
├─ 阶段4a：读取前500行
├─ 输出："步骤3.1阶段4a完成 - 已读取TEMPLATE_USAGE_GUIDE.md前半部分
       请输入'继续'以读取后半部分"
├─ 【等待用户输入"继续"】
└─ 阶段4b：读取剩余部分
```

### 输出产物

- 所有必读资源的完整内容
- 关键设计规范摘要
- 模板结构说明

### 验证标准

- [ ] 所有4个资源都已完整读取
- [ ] 无资源被跳过或省略
- [ ] 已记录关键设计规范
- [ ] 已理解模板结构

---

## 步骤 3.2：为每页规划代码方案

### 目标

为步骤2生成的每一页幻灯片规划详细的代码方案，包括布局、CSS、HTML和JavaScript。

### 执行要求

#### 阶段1：分析页面特征

为每一页幻灯片分析以下特征：

```markdown
页面特征分析：

页面 X：[页面标题]
├─ 页面类型：[P1/P2/P3/P4/P5]
├─ 内容类型：[概念性/数据性/对比性/流程性]
├─ 观点数量：[N个]
├─ 数据密度：[高/中/低]
├─ 对比关系：[并列/对比/递进]
├─ 包含图表：[是/否]
├─ 包含表格：[是/否]
└─ 推荐布局：[L1-L12]
```

#### 阶段2：选择布局类型

根据页面特征，选择合适的布局类型：

**布局类型清单（L1-L12）**

```
L1. 单列布局（Single Column）
   - 适用：1个核心观点
   - 示例：01-cover-page.html

L2. 双列布局（Two Columns）
   - 适用：2-3个对比观点
   - 示例：02-two-column-comparison.html

L3. 三列布局（Three Columns）
   - 适用：3个并列观点
   - 示例：03-three-column.html

L4. 卡片网格布局（Card Grid）
   - 适用：4-6个并列观点
   - 示例：04-card-grid.html

L5. 图表+文本布局（Chart + Text）
   - 适用：包含图表的页面
   - 示例：05-chart-text.html

L6. 左右分栏布局（Left-Right Split）
   - 适用：左侧导航+右侧内容
   - 示例：06-left-right-split.html

L7. 上下分栏布局（Top-Bottom Split）
   - 适用：上方图表+下方内容
   - 示例：07-top-bottom-split.html

L8. 列表式布局（List Layout）
   - 适用：目录页
   - 示例：08-table-of-contents.html

L9. 网格卡片布局（Grid Cards）
   - 适用：网格式目录
   - 示例：10-toc-grid-cards.html

L10. 时间线布局（Timeline）
   - 适用：流程步骤
   - 示例：11-timeline.html

L11. 章节首页布局（Chapter Cover）
   - 适用：章节首页
   - 示例：11-chapter-overview.html

L12. 强调框布局（Emphasis Box）
   - 适用：核心结论
   - 示例：12-emphasis-box.html
```

#### 阶段3：规划CSS样式

为每页规划需要的CSS样式：

```markdown
CSS样式规划：

页面 X：[页面标题]
├─ 布局CSS：
│   ├─ [布局容器类名]
│   └─ [布局子元素类名]
├─ 内容CSS：
│   ├─ [标题类名]
│   ├─ [文本类名]
│   └─ [列表类名]
├─ 特殊CSS：
│   ├─ [图表容器类名]
│   ├─ [表格样式类名]
│   └─ [卡片样式类名]
└─ 响应式CSS：
    ├─ [断点1样式]
    ├─ [断点2样式]
    └─ [断点3样式]
```

#### 阶段4：规划HTML结构

为每页规划HTML结构：

```markdown
HTML结构规划：

页面 X：[页面标题]
├─ 外层容器：
│   └─ <div class="slide [slide-class]">
├─ 页面标题：
│   └─ <h2 class="slide-title">[标题]</h2>
├─ 内容容器：
│   └─ <div class="slide-content">
├─ 具体内容：
│   ├─ [要点列表]
│   ├─ [图表容器]
│   └─ [表格]
└─ 闭合标签：
    └─ </div></div>
```

#### 阶段5：规划JavaScript代码

为包含图表的页面规划JavaScript代码：

```markdown
JavaScript规划：

页面 X：[页面标题]
├─ 图表类型：[Chart.js类型]
├─ Canvas ID：[唯一ID]
├─ 数据配置：
│   ├─ labels: [...]
│   ├─ datasets: [...]
│   └─ options: {...}
└─ 初始化代码：
    └─ new Chart(canvasId, config)
```

### ⚠️ Token限制处理：如果页面很多

```
如果幻灯片页面超过20页，必须分批规划：

阶段3a：规划前10页的代码方案
├─ 详细规划封面页、目录页、章节首页、前7页内容页
├─ 为每页选择布局类型并分析特征
├─ 列出所有CSS、HTML、JavaScript代码要点
└─ 输出："步骤3.2阶段3a完成 - 已规划前10页代码方案
       请输入'继续'以规划剩余页面"

【等待用户输入"继续"】

阶段3b：规划剩余页面的代码方案
├─ 详细规划剩余内容页和结束页
├─ 为每页选择布局类型并分析特征
├─ 列出所有CSS、HTML、JavaScript代码要点
└─ 输出："步骤3.2阶段3b完成 - 所有页面代码方案规划完成
       总页数：N页
       已进入步骤3.3"
```

### 输出产物

- 每页的代码规划方案
- 布局类型选择清单
- CSS样式汇总
- HTML结构汇总
- JavaScript代码汇总

### 验证标准

- [ ] 所有页面都已规划代码方案
- [ ] 每页都有合适的布局类型
- [ ] CSS样式清单完整
- [ ] HTML结构清晰
- [ ] JavaScript代码正确
- [ ] 无页面遗漏

---

## 步骤 3.3：生成完整HTML文件

### 目标

基于步骤3.2的代码规划方案，生成完整的、可运行的McKinsey风格HTML文件。

### 执行要求

按照章节顺序逐个生成幻灯片，每个章节包含以下内容：
1. 阶段1：生成HTML框架和完整CSS样式
2. 阶段2：按章节逐个生成幻灯片（封面页、目录页、章节首页、内容页、结束页），每个幻灯片包含HTML和对应的JavaScript图表代码

**⚠️ 重要说明**：
- 每个章节的所有幻灯片必须一次性完整生成
- 每个幻灯片必须包含完整的HTML结构和对应的JavaScript图表代码
- 100%保留步骤2中的所有内容，禁止简化、禁止压缩、禁止删减
- 如果token不足，使用"继续"机制分批处理，但必须保证每个章节的完整性
- 每个章节生成完成后，提示用户输入"继续"以生成下一个章节

### ⚠️ 关键原则

- ✅ 每个阶段的代码必须是完整的语法单元
- ✅ CSS必须在阶段1一次性完整生成
- ✅ 每个幻灯片的HTML必须完整
- ✅ 每个幻灯片的JavaScript图表代码必须紧跟在HTML之后
- ✅ 每个章节的所有内容必须100%保留
- ✅ 每个章节生成完成后提示用户输入"继续"
- ✅ 遇到token限制时使用"继续"机制，但必须保证章节完整性
- ❌ 禁止跨阶段截断HTML标签
- ❌ 禁止省略CSS样式
- ❌ 禁止简化图表代码
- ❌ 禁止压缩或删减任何内容
- ❌ 禁止为了省token而跳过任何幻灯片或内容
- ❌ 禁止将JavaScript图表代码与HTML分离

---

#### 阶段1：生成HTML框架和完整CSS样式

**执行流程：**

```markdown
✅ 阶段1/4：生成HTML框架和完整CSS样式

生成内容：
1. DOCTYPE声明和HTML根元素
2. head标签和meta设置
3. Chart.js CDN引用
4. 完整的CSS样式（约600-800行）
5. body开始标签
6. 导航栏结构
7. 幻灯片容器开始标签
```

**生成代码示例：**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[文档标题] - McKinsey风格演示文稿</title>

  <!-- Chart.js CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>

  <style>
    /* ========================================
       McKinsey Design System - CSS Variables
       ======================================== */
    :root {
      /* 配色方案 */
      --color-bg: #FFFFFF;
      --color-text-primary: #000000;
      --color-text-secondary: #333333;
      --color-accent-primary: #F85d42;
      --color-accent-secondary: #74788d;
      --color-blue: #556EE6;
      --color-green: #34c38f;
      --color-light-blue: #50a5f1;
      --color-yellow: #f1b44c;

      /* 字体大小 */
      --font-size-title-main: 64px;
      --font-size-title-section: 48px;
      --font-size-title-slide: 42px;
      --font-size-subtitle: 36px;
      --font-size-body-primary: 20px;
      --font-size-body-secondary: 16px;

      /* 间距 */
      --spacing-xs: 10px;
      --spacing-sm: 20px;
      --spacing-md: 30px;
      --spacing-lg: 40px;
      --spacing-xl: 60px;
    }

    /* ========================================
       Base Styles
       ======================================== */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
      background-color: var(--color-bg);
      color: var(--color-text-secondary);
      line-height: 1.6;
      overflow-x: hidden;
    }

    /* ========================================
       Navigation Bar
       ======================================== */
    .navbar {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 80px;
      background: white;
      border-bottom: 2px solid #e0e0e0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 var(--spacing-xl);
      z-index: 1000;
      box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }

    .navbar h1 {
      font-size: 24px;
      font-weight: 700;
      color: var(--color-text-primary);
    }

    .nav-controls {
      display: flex;
      align-items: center;
      gap: var(--spacing-sm);
    }

    .nav-btn {
      padding: 12px 24px;
      background: var(--color-accent-primary);
      color: white;
      border: none;
      border-radius: 6px;
      font-size: 16px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.3s ease;
    }

    .nav-btn:hover {
      background: #d94a2f;
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(248, 93, 66, 0.3);
    }

    .nav-btn:disabled {
      background: #ccc;
      cursor: not-allowed;
      transform: none;
    }

    .slide-counter {
      font-size: 18px;
      font-weight: 600;
      color: var(--color-text-secondary);
      padding: 0 var(--spacing-sm);
    }

    /* ========================================
       Presentation Container
       ======================================== */
    .presentation-container {
      margin-top: 80px;
      width: 100%;
      min-height: calc(100vh - 80px);
    }

    /* ========================================
       Slide Base Styles
       ======================================== */
    .slide {
      display: none;
      width: 100%;
      max-width: 1400px;
      margin: 0 auto;
      padding: var(--spacing-xl);
      min-height: calc(100vh - 80px);
      animation: fadeIn 0.5s ease-in-out;
    }

    .slide.active {
      display: block;
    }

    @keyframes fadeIn {
      from {
        opacity: 0;
        transform: translateY(20px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .slide-title {
      font-size: var(--font-size-title-slide);
      font-weight: 700;
      color: var(--color-text-primary);
      margin-bottom: var(--spacing-md);
      border-bottom: 3px solid var(--color-accent-primary);
      padding-bottom: var(--spacing-sm);
    }

    .slide-content {
      width: 100%;
      max-width: 1400px;
      margin: 0 auto;
    }

    /* ========================================
       Cover Page (P1)
       ======================================== */
    .slide.title-slide {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
    }

    .title-main {
      font-size: var(--font-size-title-main);
      font-weight: 700;
      margin-bottom: var(--spacing-md);
      line-height: 1.2;
    }

    .subtitle {
      font-size: var(--font-size-subtitle);
      font-weight: 600;
      color: rgba(255, 255, 255, 0.9);
      margin-bottom: var(--spacing-sm);
    }

    .date-info {
      font-size: var(--font-size-body-primary);
      color: rgba(255, 255, 255, 0.8);
    }

    /* ========================================
       Chapter Cover (P3)
       ======================================== */
    .slide.section-slide {
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding-left: 100px;
    }

    .chapter-number {
      font-size: 72px;
      font-weight: 700;
      color: var(--color-accent-primary);
      margin-bottom: var(--spacing-sm);
    }

    .chapter-title {
      font-size: var(--font-size-title-section);
      font-weight: 700;
      color: var(--color-text-primary);
      margin-bottom: var(--spacing-md);
    }

    .chapter-description {
      font-size: var(--font-size-body-primary);
      color: var(--color-text-secondary);
      margin-bottom: var(--spacing-lg);
      max-width: 800px;
    }

    .sub-chapter-list {
      list-style: none;
      font-size: var(--font-size-body-primary);
      color: var(--color-text-secondary);
    }

    .sub-chapter-list li {
      padding: var(--spacing-sm) 0;
      border-bottom: 1px solid #e0e0e0;
    }

    .sub-chapter-list li:before {
      content: "→ ";
      color: var(--color-accent-primary);
      font-weight: 700;
      margin-right: var(--spacing-xs);
    }

    /* ========================================
       Table of Contents (P2) - Grid Cards
       ======================================== */
    .toc-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: var(--spacing-md);
      margin: var(--spacing-lg) 0;
    }

    .toc-card {
      background: white;
      padding: var(--spacing-lg);
      border-radius: 12px;
      border-left: 6px solid var(--color-accent-primary);
      box-shadow: 0 4px 12px rgba(0,0,0,0.08);
      transition: all 0.3s ease;
      cursor: pointer;
    }

    .toc-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 8px 20px rgba(0,0,0,0.12);
    }

    .chapter-number-small {
      font-size: 36px;
      font-weight: 700;
      color: var(--color-accent-primary);
      margin-bottom: var(--spacing-sm);
    }

    .toc-card h3 {
      font-size: 24px;
      font-weight: 700;
      color: var(--color-text-primary);
      margin-bottom: var(--spacing-xs);
    }

    /* ========================================
       Three Column Layout (L3)
       ======================================== */
    .three-column-layout {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: var(--spacing-md);
      margin: var(--spacing-lg) 0;
    }

    .three-column-layout .column {
      background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
      padding: var(--spacing-md);
      border-radius: 12px;
      border-left: 4px solid var(--color-accent-primary);
      transition: all 0.3s ease;
    }

    .three-column-layout .column:nth-child(1) {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
    }

    .three-column-layout .column:nth-child(2) {
      background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
      color: white;
    }

    .three-column-layout .column:nth-child(3) {
      background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
      color: white;
    }

    .three-column-layout .column:hover {
      transform: translateY(-5px);
      box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }

    .three-column-layout .column h3 {
      font-size: 24px;
      font-weight: 700;
      margin-bottom: var(--spacing-sm);
    }

    .number-highlight {
      font-size: 42px;
      font-weight: 700;
      margin: var(--spacing-sm) 0;
    }

    /* ========================================
       Card Grid Layout (L4)
       ======================================== */
    .highlight-cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: var(--spacing-md);
      margin: var(--spacing-lg) 0;
    }

    .highlight-card {
      background: white;
      padding: var(--spacing-md);
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.08);
      border-top: 4px solid var(--color-accent-primary);
      transition: all 0.3s ease;
    }

    .highlight-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }

    .card-title {
      font-size: 22px;
      font-weight: 700;
      color: var(--color-text-primary);
      margin-bottom: var(--spacing-xs);
    }

    .card-subtitle {
      font-size: 16px;
      font-weight: 600;
      color: var(--color-accent-primary);
      margin-bottom: var(--spacing-sm);
    }

    .card-content {
      list-style: none;
      font-size: 16px;
      color: var(--color-text-secondary);
    }

    .card-content li {
      padding: 6px 0;
      padding-left: 20px;
      position: relative;
    }

    .card-content li:before {
      content: "•";
      color: var(--color-accent-primary);
      font-weight: 700;
      position: absolute;
      left: 0;
    }

    /* ========================================
       Chart + Text Layout (L5)
       ======================================== */
    .chart-text-layout {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: var(--spacing-lg);
      align-items: center;
      margin: var(--spacing-lg) 0;
    }

    .chart-container {
      position: relative;
      width: 100% !important;
      min-width: 300px !important;
      max-width: 100% !important;
      height: 500px;
      margin: var(--spacing-lg) 0;
      background: white;
      padding: var(--spacing-md);
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.08);
      box-sizing: border-box;
    }

    .chart-container canvas {
      width: 100% !important;
      height: 100% !important;
      display: block !important;
    }

    .text-content {
      padding: var(--spacing-md);
    }

    .text-content h3 {
      font-size: 28px;
      font-weight: 700;
      color: var(--color-text-primary);
      margin-bottom: var(--spacing-sm);
    }

    .key-insights {
      list-style: none;
      font-size: var(--font-size-body-primary);
      color: var(--color-text-secondary);
    }

    .key-insights li {
      padding: var(--spacing-sm) 0;
      padding-left: 30px;
      position: relative;
      border-bottom: 1px solid #e0e0e0;
    }

    .key-insights li:before {
      content: "✓";
      color: var(--color-green);
      font-weight: 700;
      font-size: 20px;
      position: absolute;
      left: 0;
    }

    /* ========================================
       Bullet List
       ======================================== */
    .bullet-list {
      list-style: none;
      font-size: var(--font-size-body-primary);
      color: var(--color-text-secondary);
      margin: var(--spacing-md) 0;
    }

    .bullet-list li {
      padding: var(--spacing-sm) 0;
      padding-left: 30px;
      position: relative;
    }

    .bullet-list li:before {
      content: "•";
      color: var(--color-accent-primary);
      font-weight: 700;
      font-size: 24px;
      position: absolute;
      left: 0;
    }

    /* ========================================
       Emphasis Box
       ======================================== */
    .emphasis-box {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: var(--spacing-lg);
      border-radius: 12px;
      margin: var(--spacing-lg) 0;
      box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
    }

    .emphasis-box h3 {
      font-size: 28px;
      font-weight: 700;
      margin-bottom: var(--spacing-sm);
    }

    .emphasis-box p {
      font-size: var(--font-size-body-primary);
      line-height: 1.8;
    }

    /* ========================================
       Fullscreen Button
       ======================================== */
    .fullscreen-btn {
      position: fixed;
      bottom: 30px;
      right: 30px;
      width: 50px;
      height: 50px;
      background: var(--color-accent-primary);
      color: white;
      border: none;
      border-radius: 50%;
      font-size: 24px;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(248, 93, 66, 0.3);
      transition: all 0.3s ease;
      z-index: 999;
    }

    .fullscreen-btn:hover {
      background: #d94a2f;
      transform: scale(1.1);
    }

    /* ========================================
       Responsive Design
       ======================================== */
    @media (max-width: 1024px) {
      .navbar {
        padding: 0 var(--spacing-md);
      }

      .slide {
        padding: var(--spacing-md);
      }

      .title-main {
        font-size: 48px;
      }

      .three-column-layout {
        grid-template-columns: 1fr;
      }

      .chart-text-layout {
        grid-template-columns: 1fr;
      }

      .chart-container {
        height: 400px;
        padding: var(--spacing-sm);
      }

      .highlight-cards {
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      }
    }

    @media (max-width: 768px) {
      .navbar h1 {
        font-size: 18px;
      }

      .nav-btn {
        padding: 10px 16px;
        font-size: 14px;
      }

      .slide-counter {
        font-size: 14px;
      }

      .title-main {
        font-size: 36px;
      }

      .slide-title {
        font-size: 32px;
      }

      .chart-container {
        height: 350px;
      }

      .highlight-cards {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <nav class="navbar">
    <h1>[文档标题]</h1>
    <div class="nav-controls">
      <button class="nav-btn" id="prevBtn">上一页</button>
      <span class="slide-counter">1 / N</span>
      <button class="nav-btn" id="nextBtn">下一页</button>
    </div>
  </nav>

  <div class="presentation-container">
```

**输出提示：**

```
✅ 阶段1/4完成：已生成HTML框架和完整CSS样式（约800行）

已完成：
- DOCTYPE声明和HTML根元素
- head标签和meta设置
- Chart.js CDN引用
- 完整的CSS样式（McKinsey配色、响应式设计）
- body开始标签
- 导航栏结构
- 幻灯片容器开始标签

请输入'继续'以生成前半部分幻灯片（阶段2/4）
```

---

#### 阶段2：按章节逐个生成幻灯片（包含HTML和JavaScript图表代码）

**执行流程：**

```markdown
✅ 阶段2/3：按章节逐个生成幻灯片（包含HTML和JavaScript图表代码）

生成方式：
- 按照步骤2生成的幻灯片页面清单，逐个章节生成所有幻灯片
- 每个章节包含：封面页、目录页、章节首页、该章节的所有内容页
- 每个幻灯片必须包含：完整的HTML结构 + 对应的JavaScript图表代码
- 100%保留步骤2中的所有内容，禁止简化、禁止压缩、禁止删减
- 如果token不足，使用"继续"机制分批处理，但必须保证每个章节的完整性
```

**⚠️ 重要说明：**

```
1. 必须按照步骤2生成的幻灯片页面清单顺序逐个生成
2. 每个幻灯片的所有内容必须100%保留，包括：
   - 所有要点（bullet points）
   - 所有数据点（数值、百分比、货币等）
   - 所有表格（完整的行列数据）
   - 所有图表（完整的配置和数据）
   - 所有结论（完整文字）
3. 每个幻灯片必须包含：
   - 完整的HTML结构（<div class="slide">...</div>）
   - 对应的JavaScript图表初始化代码（如果有图表）
4. JavaScript图表代码必须紧跟在对应幻灯片的HTML之后
5. 每个幻灯片的HTML必须完整，不能跨章节截断
6. 遇到token限制时，必须使用"继续"机制，但必须保证当前章节的所有幻灯片都生成完成
7. 禁止为了省token而跳过任何幻灯片或内容
8. 禁止使用"..."或"更多内容"等省略方式
9. 禁止将JavaScript图表代码与HTML分离
```

**生成代码示例：**

```html
    <!-- 封面页 -->
    <div class="slide title-slide active" id="slide-1">
      <h1 class="title-main">[文档主标题]</h1>
      <p class="subtitle">[副标题]</p>
      <p class="date-info">[日期]</p>
    </div>

    <!-- 目录页 -->
    <div class="slide" id="slide-2">
      <h2 class="slide-title">目录 / Contents</h2>
      <div class="slide-content">
        <div class="toc-grid">
          <div class="toc-card">
            <div class="chapter-number-small">01</div>
            <h3>[第一章标题]</h3>
          </div>
          <div class="toc-card">
            <div class="chapter-number-small">02</div>
            <h3>[第二章标题]</h3>
          </div>
          <!-- ... 更多章节卡片，100%保留所有章节 ... -->
        </div>
      </div>
    </div>

    <!-- 第一章章节首页 -->
    <div class="slide section-slide" id="slide-3">
      <div class="chapter-number">01</div>
      <h2 class="chapter-title">[第一章标题]</h2>
      <p class="chapter-description">[章节描述]</p>
      <ul class="sub-chapter-list">
        <li>1.1 [子章节1.1标题]</li>
        <li>1.2 [子章节1.2标题]</li>
        <!-- ... 所有子章节，100%保留 ... -->
      </ul>
    </div>

    <!-- 第一章内容页1：三列布局 -->
    <div class="slide" id="slide-4">
      <h2 class="slide-title">[页面标题]</h2>
      <div class="slide-content">
        <div class="three-column-layout">
          <div class="column">
            <h3>[标题1]</h3>
            <div class="number-highlight">[数字1]</div>
            <p>[内容1完整文字]</p>
          </div>
          <div class="column">
            <h3>[标题2]</h3>
            <div class="number-highlight">[数字2]</div>
            <p>[内容2完整文字]</p>
          </div>
          <div class="column">
            <h3>[标题3]</h3>
            <div class="number-highlight">[数字3]</div>
            <p>[内容3完整文字]</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 第一章内容页2：卡片网格布局 -->
    <div class="slide" id="slide-5">
      <h2 class="slide-title">[页面标题]</h2>
      <div class="slide-content">
        <div class="highlight-cards">
          <div class="highlight-card">
            <h4 class="card-title">[卡片1标题]</h4>
            <p class="card-subtitle">[副标题]</p>
            <ul class="card-content">
              <li>[要点1完整文字]</li>
              <li>[要点2完整文字]</li>
              <li>[要点3完整文字]</li>
              <!-- ... 所有要点，100%保留 ... -->
            </ul>
          </div>
          <!-- ... 所有卡片，100%保留 ... -->
        </div>
      </div>
    </div>

    <!-- 第一章内容页3：图表+文本布局 -->
    <div class="slide" id="slide-6">
      <h2 class="slide-title">[页面标题]</h2>
      <div class="slide-content">
        <div class="chart-text-layout">
          <div class="chart-container">
            <canvas id="chart-1"></canvas>
          </div>
          <div class="text-content">
            <h3>[标题]</h3>
            <ul class="key-insights">
              <li>[要点1完整文字]</li>
              <li>[要点2完整文字]</li>
              <li>[要点3完整文字]</li>
              <!-- ... 所有要点，100%保留 ... -->
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- 第一章内容页3对应的JavaScript图表代码 -->
    <script>
      document.addEventListener('DOMContentLoaded', function() {
        const ctx1 = document.getElementById('chart-1');
        if (ctx1) {
          new Chart(ctx1, {
            type: 'bar',
            data: {
              labels: ['标签1', '标签2', '标签3', '标签4', '标签5'],
              datasets: [{
                label: '数据系列1',
                data: [数值1, 数值2, 数值3, 数值4, 数值5],
                backgroundColor: '#F85d42',
                borderColor: '#d94a2f',
                borderWidth: 2
              }]
            },
            options: {
              responsive: true,
              maintainAspectRatio: false,
              plugins: {
                legend: {
                  display: true,
                  position: 'top',
                  labels: {
                    font: {
                      size: 14
                    },
                    color: '#333333'
                  }
                },
                title: {
                  display: true,
                  text: '[图表标题]',
                  font: {
                    size: 18,
                    weight: 'bold'
                  },
                  color: '#000000',
                  padding: {
                    bottom: 20
                  }
                }
              },
              scales: {
                y: {
                  beginAtZero: true,
                  ticks: {
                    font: {
                      size: 12
                    },
                    color: '#333333'
                  },
                  grid: {
                    display: true,
                    color: '#e0e0e0'
                  }
                },
                x: {
                  ticks: {
                    font: {
                      size: 12
                    },
                    color: '#333333'
                  },
                  grid: {
                    display: false
                  }
                }
              }
            }
          });
        }
      });
    </script>

    <!-- 第一章内容页4：另一个图表 -->
    <div class="slide" id="slide-7">
      <h2 class="slide-title">[页面标题]</h2>
      <div class="slide-content">
        <div class="chart-text-layout">
          <div class="chart-container">
            <canvas id="chart-2"></canvas>
          </div>
          <div class="text-content">
            <h3>[标题]</h3>
            <ul class="key-insights">
              <li>[要点1完整文字]</li>
              <li>[要点2完整文字]</li>
              <li>[要点3完整文字]</li>
              <!-- ... 所有要点，100%保留 ... -->
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- 第一章内容页4对应的JavaScript图表代码 -->
    <script>
      document.addEventListener('DOMContentLoaded', function() {
        const ctx2 = document.getElementById('chart-2');
        if (ctx2) {
          new Chart(ctx2, {
            type: 'line',
            data: {
              labels: ['标签1', '标签2', '标签3', '标签4', '标签5'],
              datasets: [{
                label: '数据系列1',
                data: [数值1, 数值2, 数值3, 数值4, 数值5],
                borderColor: '#556EE6',
                backgroundColor: 'rgba(85, 110, 230, 0.1)',
                borderWidth: 3,
                fill: true,
                tension: 0.4
              }]
            },
            options: {
              responsive: true,
              maintainAspectRatio: false,
              plugins: {
                legend: {
                  display: true,
                  position: 'top',
                  labels: {
                    font: {
                      size: 14
                    },
                    color: '#333333'
                  }
                },
                title: {
                  display: true,
                  text: '[图表标题]',
                  font: {
                    size: 18,
                    weight: 'bold'
                  },
                  color: '#000000',
                  padding: {
                    bottom: 20
                  }
                }
              },
              scales: {
                y: {
                  beginAtZero: true,
                  ticks: {
                    font: {
                      size: 12
                    },
                    color: '#333333'
                  },
                  grid: {
                    display: true,
                    color: '#e0e0e0'
                  }
                },
                x: {
                  ticks: {
                    font: {
                      size: 12
                    },
                    color: '#333333'
                  },
                  grid: {
                    display: false
                  }
                }
              }
            }
          });
        }
      });
    </script>

    <!-- ... 第一章的所有内容页，每个包含HTML和对应的JavaScript图表代码，100%保留所有内容 ... -->

    <!-- 第二章章节首页 -->
    <div class="slide section-slide" id="slide-X">
      <div class="chapter-number">02</div>
      <h2 class="chapter-title">[第二章标题]</h2>
      <p class="chapter-description">[章节描述]</p>
      <ul class="sub-chapter-list">
        <li>2.1 [子章节2.1标题]</li>
        <li>2.2 [子章节2.2标题]</li>
        <!-- ... 所有子章节，100%保留 ... -->
      </ul>
    </div>

    <!-- 第二章的所有内容页，每个包含HTML和对应的JavaScript图表代码，100%保留所有内容 ... -->

    <!-- ... 所有章节的所有幻灯片，每个包含HTML和对应的JavaScript图表代码，100%保留所有内容 ... -->

    <!-- 结束页 -->
    <div class="slide" id="slide-N">
      <h2 class="slide-title">谢谢 / Thank You</h2>
      <div class="slide-content" style="text-align: center;">
        <p style="font-size: 36px; margin-bottom: 30px;">谢谢观看</p>
        <p style="font-size: 24px; color: #666;">[联系方式]</p>
        <p style="font-size: 20px; color: #999; margin-top: 20px;">Questions?</p>
      </div>
    </div>

    <!-- 幻灯片容器结束标签 -->
  </div>

  <!-- 全屏按钮 -->
  <button class="fullscreen-btn" id="fullscreenBtn">⛶</button>
```

**输出提示：**

```
✅ 阶段2/3完成：已按章节逐个生成所有幻灯片（包含HTML和JavaScript图表代码）（100%）

已完成：
- 封面页（P1）：1页
- 目录页（P2）：X页
- 章节首页（P3）：N页
- 内容页（P4）：M页（每个包含HTML和对应的JavaScript图表代码）
- 结束页（P5）：1页

当前进度：页面1 - N 全部生成完成
内容完整性：100%（无遗漏、无删减、无简化）
图表代码完整性：100%（每个图表都有对应的JavaScript初始化代码）

请输入'继续'以生成导航逻辑和结束标签（阶段3/3）
```

---

#### 阶段3：生成导航逻辑和结束标签

**执行流程：**

```markdown
✅ 阶段3/3：生成导航逻辑和结束标签

生成内容：
- 导航逻辑（上一页/下一页、键盘导航）
- 全屏切换功能
- HTML结束标签
```

**⚠️ 重要说明：**

```
1. 阶段3只生成导航逻辑和结束标签
2. 不再生成图表初始化代码（图表代码已在阶段2中跟随每个幻灯片的HTML一起生成）
3. 导航逻辑包括：按钮导航、键盘导航、全屏切换
4. 确保HTML标签正确闭合
```

**生成代码示例：**

```html
  <script>
    // ========================================
    // Navigation Logic
    // ========================================
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const slideCounter = document.querySelector('.slide-counter');
    const fullscreenBtn = document.getElementById('fullscreenBtn');
    let currentSlide = 0;

    function showSlide(index) {
      if (index < 0 || index >= slides.length) return;

      slides[currentSlide].classList.remove('active');
      currentSlide = index;
      slides[currentSlide].classList.add('active');

      slideCounter.textContent = `${currentSlide + 1} / ${slides.length}`;

      prevBtn.disabled = currentSlide === 0;
      nextBtn.disabled = currentSlide === slides.length - 1;
    }

    prevBtn.addEventListener('click', () => {
      showSlide(currentSlide - 1);
    });

    nextBtn.addEventListener('click', () => {
      showSlide(currentSlide + 1);
    });

    // Keyboard Navigation
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        showSlide(currentSlide - 1);
      } else if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') {
        showSlide(currentSlide + 1);
      }
    });

    // Fullscreen Toggle
    fullscreenBtn.addEventListener('click', () => {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
      } else {
        document.exitFullscreen();
      }
    });
  </script>
</body>
</html>
```

**输出提示：**

```
✅ 阶段3/3完成：已生成导航逻辑和结束标签（100%）

已完成：
- 导航逻辑（上一页/下一页）
- 键盘导航（方向键、空格键）
- 全屏切换功能
- HTML结束标签

HTML文件生成完成！
总代码行数：约1200行
文件大小：约60KB

建议的文件名：
[文档标题]_McKinsey风格演示文稿.html
```

### 输出产物

- 完整的HTML文件（约1200行）
- CSS样式（约800行）
- JavaScript代码（约100行）
- 图表配置（根据实际需求）

### 验证标准

- [ ] HTML结构完整
- [ ] CSS样式完整
- [ ] JavaScript功能完整
- [ ] 所有图表已配置
- [ ] 响应式设计完备
- [ ] 无语法错误

---

## 步骤 3.4：验证代码质量

### 目标

全面检查生成的HTML文件，确保质量和完整性。

### 执行要求

#### 验证项目1：内容完整性验证

```
□ 所有页面都已生成？
□ 页面数量与步骤2一致？
□ 所有内容都已包含？
□ 无遗漏、无删减、无简化？
```

#### 验证项目2：HTML结构验证

```
□ DOCTYPE声明正确？
□ HTML标签正确闭合？
□ 语义化标签使用正确？
□ ID唯一性检查通过？
```

#### 验证项目3：CSS样式验证

```
□ McKinsey配色方案正确？
□ 字体大小符合规范？
□ 间距符合标准？
□ 响应式设计完备？
```

#### 验证项目4：JavaScript功能验证

```
□ 导航功能正常？
□ 键盘导航正常？
□ 全屏切换正常？
□ 图表初始化正常？
```

#### 验证项目5：图表显示验证

```
□ 所有图表容器宽度为100%？
□ Chart.js配置正确？
□ 图表数据准确？
□ 图表交互正常？
```

#### 验证项目6：响应式设计验证

```
□ 桌面端显示正常？
□ 平板端显示正常？
□ 手机端显示正常？
□ 断点设置合理？
```

### 输出产物

- 验证报告
- 问题清单（如有）
- 修正建议（如有）

### 验证标准

- [ ] 所有验证项目都通过
- [ ] 无严重问题
- [ ] 可正常运行
- [ ] 符合McKinsey标准

---

## 完成后输出

```
✅ 步骤3：HTML样式布局代码规划与生成 - 100%完成

输出摘要：
- 资源读取：4个必读资源100%读取完成
- 代码规划：N页全部规划完成
- 布局选择：平均匹配度92%（85%-100%）
- HTML生成：1200行代码，4个阶段100%完成
- 图表数量：X个Chart.js图表
- 验证结果：6项验证100%通过
- 文件大小：约60KB
- 质量评分：A+（完全符合McKinsey标准）

输出产物：
1. 代码规划方案（已生成）
2. 完整HTML文件（已生成）
3. 验证报告（已生成）

已进入步骤4：代码内容审核检验
```
