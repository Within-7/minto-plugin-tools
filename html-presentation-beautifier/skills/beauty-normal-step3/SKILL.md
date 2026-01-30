---
name: "beauty-normal-step3"
description: "JSON data generation and HTML rendering. Automatically invoked during step 3 of the beauty-normal command to convert slide content into JSON data structure and generate JSON-driven McKinsey-style HTML files, including CSS styles, JSON data, and JavaScript rendering logic. JSON数据生成与HTML渲染。在beauty-normal命令的步骤3执行时自动调用，将幻灯片内容转换为JSON数据结构，并生成JSON驱动的McKinsey风格HTML文件，包含CSS样式、JSON数据和JavaScript渲染逻辑。"
---

# Beauty-Normal 步骤3：JSON数据生成与HTML渲染 / Beauty-Normal Step 3: JSON Data Generation and HTML Rendering

## 目标 / Goal

将步骤2生成的幻灯片页面清单转换为JSON数据结构，并使用JSON+HTML方式生成完整的、可运行的McKinsey风格HTML文件。

Convert the slide page list generated in Step 2 into JSON data structure, and use JSON+HTML method to generate a complete, runnable McKinsey-style HTML file.

## ⚠️ 核心原则

**🔑 必须读取并参考skill资源：**
- **必须读** `beauty-html/references/best-practices.md`
- **必须读** `beauty-html/references/mckinsey-design-system.md`
- **必须读** `beauty-html/assets/presentation-template.html`
- **必须读** `beauty-html/assets/TEMPLATE_USAGE_GUIDE.md`
- **必须读** `beauty-html/assets/INDEX.md`
- **必须读** `beauty-json/SKILL.md`（⚠️ 新增：JSON数据结构规范）

**⚠️ Token限制处理原则：**

**🔑 最核心规则（必须严格遵守）：如果数据内容过大，或者token过长，则自动使用'继续'进行'分段'加载数据，绝对不能精简、偷工减料的节省token,严禁为了省token而跳过内容或使用摘要**

**当遇到 token 限制或上下文长度问题时，必须使用"继续"分页方式，绝对禁止：**
- ❌ 压缩或省略资源读取
- ❌ 跳过必读资源
- ❌ 简化执行步骤
- ❌ 减少生成内容
- ❌ 使用摘要代替完整内容
- ❌ 精简数据内容
- ❌ 偷工减料节省token

**正确处理方式：使用"继续"机制**
```
1. 在完成当前可执行的部分后
2. 明确说明："由于 token 限制，任务未完成，请输入'继续'以获取剩余部分"
3. 等待用户输入"继续"后
4. 继续执行剩余步骤
5. 重复直到任务完全完成
```

**分段加载原则：**
- ✅ **完整保留**：每段数据都必须100%保留，无遗漏、无压缩
- ✅ **分段清晰**：明确标注当前是第几段，共几段
- ✅ **连续执行**：每段完成后自动提示"继续"，等待用户确认
- ✅ **质量优先**：宁可多轮对话，不可降低质量
- ❌ **禁止精简**：绝对不能为了省token而精简数据内容
- ❌ **禁止偷工**：绝对不能为了省token而偷工减料

**关键规则：**
- ✅ **质量 > 速度**：宁可多轮对话，不可降低质量
- ✅ **完整 > 简化**：宁可分多次执行，不可压缩内容
- ✅ **标准 > 妥协**：宁可触发继续，不可偷工减料

## 📋 执行流程（4个子步骤）

```
步骤3.1：读取必读资源
  ↓
步骤3.2：设计JSON数据结构
  ↓
步骤3.3：生成完整HTML文件（4个阶段）
  ├─ 阶段1：生成HTML框架和完整CSS样式
  ├─ 阶段2：生成JSON数据（包含所有幻灯片内容）
  ├─ 阶段3：生成HTML容器和JavaScript渲染逻辑
  └─ 阶段4：生成结束标签
  ↓
步骤3.4：验证代码质量
```

---

## 步骤 3.1：读取必读资源

### 目标

完整读取所有必读资源，为后续JSON数据设计和HTML生成提供参考。

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

5. beauty-html/assets/INDEX.md（⚠️ 重要）
   - 14个布局示例（封面页、目录页、双列对比、三列并列等）
   - 23个图表示例（金字塔图、仪表盘、韦恩图、时间轴等）
   - 匹配决策树（帮助选择合适的布局）
   - 设计规范（颜色、字体、间距标准）
   - 布局类型清单（L1-L13）
   - 图表类型索引

6. beauty-json/SKILL.md（⚠️ 新增：JSON数据结构规范）
   - JSON数据结构规范
   - 幻灯片类型定义
   - 内容结构示例
   - HTML框架模板
   - 渲染函数规范
   - 转换流程

7. .ppt_assets/INDEX.md（如果存在，优先级最高）
   - 项目特定的布局示例
   - 项目特定的图表示例
   - 项目特定的样式和组件
   - ⚠️ 优先级规则：如果某个布局、图表或图文展示在 beauty-html/assets/INDEX.md 和 .ppt_assets/INDEX.md 中都存在，必须优先使用 .ppt_assets/INDEX.md 中的版本
   - 注意：只有当当前文件夹存在此文件时才读取
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

**阶段5：读取INDEX.md（⚠️ 重要）**

```
使用 Read 工具读取：
Read: beauty-html/assets/INDEX.md

此文件包含所有布局和图表示例的索引，是规划代码方案的关键参考。

如果文件过长，分批读取：
├─ 阶段5a：读取前500行
├─ 输出："步骤3.1阶段5a完成 - 已读取INDEX.md前半部分
       请输入'继续'以读取后半部分"
├─ 【等待用户输入"继续"】
└─ 阶段5b：读取剩余部分

完成后输出："步骤3.1阶段5完成 - 已读取全局布局和图表示例索引
       包含14个布局示例和23个图表示例"
```

**阶段6：读取beauty-json/SKILL.md（⚠️ 新增）**

```
使用 Read 工具读取：
Read: beauty-json/SKILL.md

此文件包含JSON数据结构规范，是设计JSON数据的关键参考。

如果文件过长，分批读取：
├─ 阶段6a：读取前500行
├─ 输出："步骤3.1阶段6a完成 - 已读取beauty-json/SKILL.md前半部分
       请输入'继续'以读取后半部分"
├─ 【等待用户输入"继续"】
└─ 阶段6b：读取剩余部分

完成后输出："步骤3.1阶段6完成 - 已读取JSON数据结构规范"
```

**阶段7：检查并读取.ppt_assets/INDEX.md（如果存在）**

```
使用 Read 工具读取：
Read: .ppt_assets/INDEX.md

注意：
- 只有当当前文件夹存在 .ppt_assets/INDEX.md 文件时才读取
- 如果文件不存在，跳过此步骤并输出："步骤3.1阶段7完成 - 未发现项目特定资源索引"
- 如果文件存在，读取完整内容

完成后输出："步骤3.1阶段7完成 - 已读取项目特定资源索引"
       （或："步骤3.1阶段7完成 - 未发现项目特定资源索引"）
```

### 输出产物

- 所有必读资源的完整内容
- 关键设计规范摘要
- 模板结构说明
- 布局和图表示例索引（14个布局示例、23个图表示例）
- 匹配决策树和设计规范
- JSON数据结构规范（⚠️ 新增）
- 项目特定资源索引（如果存在）

### 验证标准

- [ ] 所有5个基础资源都已完整读取（best-practices.md、mckinsey-design-system.md、presentation-template.html、TEMPLATE_USAGE_GUIDE.md、INDEX.md）
- [ ] 已读取JSON数据结构规范（beauty-json/SKILL.md）
- [ ] 已检查并读取项目特定资源索引（.ppt_assets/INDEX.md，如果存在）
- [ ] 无资源被跳过或省略
- [ ] 已记录关键设计规范
- [ ] 已理解模板结构
- [ ] 已了解所有可用的布局类型和图表示例
- [ ] 已掌握匹配决策树的使用方法
- [ ] 已掌握JSON数据结构规范（⚠️ 新增）

---

## 步骤 3.2：设计JSON数据结构

### 目标

为步骤2生成的每一页幻灯片设计JSON数据结构，确保数据完整性和结构规范性。

### 执行要求

#### 阶段0：读取布局和图表示例索引

**⚠️ 重要说明：在设计JSON数据结构之前，必须先读取布局和图表示例索引**

```
必读资源1：全局布局和图表示例索引
使用 Read 工具读取：
Read: beauty-html/assets/INDEX.md

此文件包含：
- 14个布局示例（封面页、目录页、双列对比、三列并列等）
- 23个图表示例（金字塔图、仪表盘、韦恩图、时间轴等）
- 匹配决策树（帮助选择合适的布局）
- 设计规范（颜色、字体、间距标准）
```

```
必读资源2：项目特定资源索引（如果存在）
使用 Read 工具读取：
Read: .ppt_assets/INDEX.md

注意：
- 只有当当前文件夹存在 .ppt_assets/INDEX.md 文件时才读取
- 如果文件不存在，跳过此步骤
- 此文件可能包含项目特定的布局、图表、样式示例
```

**执行流程：**

```
步骤3.2阶段0a：读取全局索引
├─ 读取 beauty-html/assets/INDEX.md
├─ 了解所有可用的布局类型和图表示例
├─ 记录匹配决策树和设计规范
└─ 输出："步骤3.2阶段0a完成 - 已读取全局布局和图表示例索引"

步骤3.2阶段0b：检查并读取项目特定索引
├─ 检查是否存在 .ppt_assets/INDEX.md
├─ 如果存在，读取该文件
├─ 了解项目特定的资源和自定义布局
└─ 输出："步骤3.2阶段0b完成 - 已检查并读取项目特定资源索引"
       （如果文件不存在，输出："步骤3.2阶段0b完成 - 未发现项目特定资源索引"）
```

**使用索引的原则：**

```
⚠️ 优先级规则（必须严格遵守）：

优先级1：.ppt_assets/INDEX.md（项目特定资源）
├─ 如果存在，优先级最高
├─ 如果某个布局、图表或图文展示在 beauty-html/assets/INDEX.md 和 .ppt_assets/INDEX.md 中都存在，必须优先使用 .ppt_assets/INDEX.md 中的版本
└─ 适用于：项目特定的需求、自定义布局、定制化图表

优先级2：beauty-html/assets/INDEX.md（全局资源）
├─ 默认资源库
├─ 包含14个布局示例和23个图表示例
└─ 适用于：通用场景、标准布局、常见图表

使用流程：

1. 在为每页设计JSON数据结构时，首先检查 .ppt_assets/INDEX.md 是否存在
2. 如果存在，在 .ppt_assets/INDEX.md 中查找匹配的布局或图表
3. 如果 .ppt_assets/INDEX.md 中没有找到，再查找 beauty-html/assets/INDEX.md
4. 根据页面特征，使用匹配决策树选择最合适的布局类型
5. 如果需要图表，从优先级最高的索引文件中选择合适的图表类型
6. 确保生成的JSON数据结构符合 beauty-json/SKILL.md 中的规范
```

#### 阶段1：分析页面特征

为每一页幻灯片分析以下特征：

```markdown
页面特征分析：

页面 X：[页面标题]
├─ 页面类型：[cover|toc|section|content|end]
├─ 内容类型：[概念性/数据性/对比性/流程性]
├─ 观点数量：[N个]
├─ 数据密度：[高/中/低]
├─ 对比关系：[并列/对比/递进]
├─ 包含图表：[是/否]
├─ 包含表格：[是/否]
├─ 推荐布局：[L1-L13]
└─ 推荐模板：[模板文件名]
```

#### 阶段2：选择JSON数据结构类型

根据页面特征，选择合适的JSON数据结构类型：

**JSON数据结构类型清单（基于beauty-json/SKILL.md）**

```
类型1：封面页 (cover)
   - 模板：01-cover-page
   - 数据结构：
     {
       "mainTitle": "主标题",
       "subtitle": "副标题",
       "meta": {
         "date": "日期",
         "author": "作者"
       }
     }

类型2：双列对比页 (two-column)
   - 模板：02-two-column-comparison
   - 数据结构：
     {
       "leftColumn": {
         "title": "左列标题",
         "items": ["要点1", "要点2", ...],
         "highlight": "强调内容"
       },
       "rightColumn": {
         "title": "右列标题",
         "items": ["要点1", "要点2", ...],
         "highlight": "强调内容"
       }
     }

类型3：三列布局页 (three-column)
   - 模板：03-three-column
   - 数据结构：
     {
       "columns": [
         {
           "title": "列标题",
           "items": ["要点1", "要点2", ...],
           "icon": "图标"
         },
         ...
       ]
     }

类型4：图表+文本页 (chart-text)
   - 模板：05-chart-text
   - 数据结构：
     {
       "chart": {
         "type": "bar|line|pie|...",
         "title": "图表标题",
         "data": {
           "labels": [...],
           "datasets": [...]
         },
         "options": {...}
       },
       "insights": ["洞察1", "洞察2", ...],
       "highlight": "强调内容"
     }

类型5：目录页 (toc)
   - 模板：08-table-of-contents
   - 数据结构：
     {
       "items": [
         { "number": "01", "title": "章节标题", "page": 3 },
         ...
       ]
     }

类型6：章节首页 (section)
   - 模板：11-chapter-overview
   - 数据结构：
     {
       "subtitle": "章节副标题",
       "description": "章节描述"
     }

类型7：数据强调页 (data-emphasis)
   - 模板：06-data-emphasis
   - 数据结构：
     {
       "metrics": [
         {
           "value": "数值",
           "label": "标签",
           "description": "描述"
         },
         ...
       ]
     }
```

#### 阶段3：设计JSON数据结构

为每一页设计详细的JSON数据结构：

```markdown
JSON数据结构设计：

页面 X：[页面标题]
├─ 幻灯片ID：[数字ID]
├─ 幻灯片类型：[cover|toc|section|content|end]
├─ 模板类型：[模板文件名]
├─ 幻灯片标题：[标题]
└─ 内容结构：
    ├─ [根据选择的JSON数据结构类型]
    ├─ [详细列出所有字段]
    └─ [确保100%保留所有内容]
```

**设计原则：**

```
✅ 必须遵守的原则：

1. 数据完整性原则
   - 100%保留步骤2中的所有内容
   - 不得遗漏任何文本、数据、图表信息
   - 确保JSON数据结构完整

2. 结构规范性原则
   - 严格遵循beauty-json/SKILL.md中的JSON数据结构规范
   - 使用标准字段名称
   - 保持数据结构一致性

3. 模板匹配原则
   - 根据页面特征选择合适的模板类型
   - 使用INDEX.md中的匹配决策树
   - 优先使用项目特定资源（如果存在）

4. 数据类型原则
   - 文本内容使用字符串
   - 数值数据使用数字
   - 列表数据使用数组
   - 对象数据使用对象

5. 可扩展性原则
   - JSON数据结构应易于扩展
   - 支持添加新字段
   - 保持向后兼容性
```

#### 阶段4：验证JSON数据结构

为每一页验证JSON数据结构的正确性：

```markdown
JSON数据结构验证：

页面 X：[页面标题]
├─ 结构完整性：
│   ├─ [ ] 所有必需字段都已包含
│   ├─ [ ] 字段名称符合规范
│   └─ [ ] 数据类型正确
├─ 内容完整性：
│   ├─ [ ] 100%保留所有内容
│   ├─ [ ] 无内容遗漏
│   └─ [ ] 无内容篡改
├─ 结构规范性：
│   ├─ [ ] 符合beauty-json/SKILL.md规范
│   ├─ [ ] 与模板类型匹配
│   └─ [ ] 数据结构一致
└─ 可扩展性：
    ├─ [ ] 易于扩展
    └─ [ ] 向后兼容
```

### ⚠️ Token限制处理：如果页面很多

```
如果幻灯片页面超过20页，必须分批设计JSON数据结构：

阶段3a：设计前10页的JSON数据结构
├─ 详细分析前10页的页面特征
├─ 为每页选择合适的JSON数据结构类型
├─ 设计详细的JSON数据结构
├─ 验证JSON数据结构的正确性
└─ 输出："步骤3.2阶段3a完成 - 已设计前10页JSON数据结构
       请输入'继续'以设计剩余页面"

【等待用户输入"继续"】

阶段3b：设计剩余页面的JSON数据结构
├─ 详细分析剩余页面的页面特征
├─ 为每页选择合适的JSON数据结构类型
├─ 设计详细的JSON数据结构
├─ 验证JSON数据结构的正确性
└─ 输出："步骤3.2阶段3b完成 - 所有页面JSON数据结构设计完成
       总页数：N页
       已进入步骤3.3"
```

### 输出产物

- 每页的JSON数据结构设计
- JSON数据结构类型选择清单
- 页面特征分析结果
- JSON数据结构验证报告

### 验证标准

- [ ] 所有页面的JSON数据结构都已设计完成
- [ ] 每页的JSON数据结构类型选择正确
- [ ] 所有内容都已包含在JSON数据结构中
- [ ] JSON数据结构符合beauty-json/SKILL.md规范
- [ ] JSON数据结构易于扩展和维护
- [ ] 无内容遗漏或篡改
- [ ] 数据类型正确
- [ ] 字段名称符合规范

---

## 步骤 3.3：生成完整HTML文件（4个阶段）

### 目标

将步骤2生成的幻灯片页面清单和步骤3.2设计的JSON数据结构转换为完整的、可运行的JSON驱动HTML文件。

### ⚠️ 核心原则

**🔑 必须遵守的原则：**

1. **分阶段生成原则**
   - 必须按照4个阶段依次生成
   - 每个阶段必须是完整的语法单元
   - 每个阶段结束后提示用户输入"继续"

2. **代码完整性原则**
   - HTML结构必须完整
   - CSS样式必须完整
   - JavaScript代码必须完整
   - JSON数据必须完整

3. **数据完整性原则**
   - JSON数据必须100%保留所有内容
   - 不得遗漏任何文本、数据、图表信息
   - 确保JSON数据结构完整

4. **设计规范原则**
   - 严格遵循McKinsey设计规范
   - 使用标准色板
   - 使用系统字体
   - 禁止使用非McKinsey风格元素

5. **渲染逻辑原则**
   - JavaScript必须能够正确解析JSON数据
   - JavaScript必须能够正确渲染HTML
   - 所有图表必须正确显示
   - 响应式设计必须正常工作

### 执行流程

#### 阶段1：生成HTML框架和完整CSS样式

**目标**：生成HTML文档框架和完整的CSS样式。

**输出内容**：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>McKinsey风格演示文稿</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <style>
        /* CSS变量定义 - McKinsey规范 */
        :root {
            --primary-background: #FFFFFF;
            --primary-accent: #F85d42;
            --deep-blue: #556EE6;
            --text-black: #000000;
            --text-dark: #333333;
            --text-gray: #74788d;
            --text-light: #FFFFFF;
            --element-spacing: 25px;
            --column-gap: 35px;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
            background: #f5f7fa;
            padding: 40px 20px;
        }

        .slide {
            max-width: 1200px;
            margin: 0 auto;
            background: var(--primary-background);
            border-radius: 12px;
            padding: 50px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            margin-bottom: 40px;
        }

        /* 页眉 */
        .slide-header {
            text-align: center;
            margin-bottom: 50px;
        }

        .slide-header h2 {
            font-size: 56px;
            font-weight: bold;
            color: var(--text-black);
            margin-bottom: 10px;
            line-height: 1.2;
        }

        /* 封面页样式 */
        .cover-page {
            text-align: center;
        }

        .cover-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 60vh;
        }

        .cover-content h1 {
            font-size: 56px;
            font-weight: bold;
            color: var(--text-black);
            margin-bottom: 30px;
            line-height: 1.2;
        }

        .cover-content .subtitle {
            font-size: 32px;
            font-weight: bold;
            color: var(--primary-accent);
            margin-bottom: 50px;
        }

        .cover-content .divider {
            width: 100px;
            height: 4px;
            background: linear-gradient(90deg, var(--primary-accent), var(--deep-blue));
            margin: 30px auto;
            border-radius: 2px;
        }

        .cover-content .meta-info {
            margin-top: 40px;
            padding-top: 30px;
            border-top: 2px solid #f0f0f0;
            width: 100%;
            max-width: 600px;
        }

        .cover-content .meta-info p {
            font-size: 18px;
            color: var(--text-gray);
            margin: 10px 0;
        }

        /* 双列布局样式 */
        .two-column-page .comparison-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: var(--column-gap);
            position: relative;
        }

        .two-column-page .comparison-container::before {
            content: '';
            position: absolute;
            left: 50%;
            top: 0;
            bottom: 0;
            width: 2px;
            background: linear-gradient(180deg, transparent, #e0e0e0 20%, #e0e0e0 80%, transparent);
            transform: translateX(-50%);
        }

        .two-column-page .column {
            padding: 30px;
            border-radius: 12px;
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        }

        .two-column-page .column:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.12);
        }

        .two-column-page .column.left {
            background: var(--primary-accent);
            color: var(--text-light);
        }

        .two-column-page .column.right {
            background: var(--deep-blue);
            color: var(--text-light);
        }

        .two-column-page .column-header {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 25px;
            text-align: center;
            padding-bottom: 15px;
            border-bottom: 2px solid rgba(255,255,255,0.3);
        }

        .two-column-page .column-content {
            list-style: none;
        }

        .two-column-page .column-content li {
            padding: 12px 0;
            font-size: 18px;
            line-height: 1.6;
            position: relative;
            padding-left: 30px;
        }

        .two-column-page .column-content li::before {
            content: '✓';
            position: absolute;
            left: 0;
            font-weight: bold;
        }

        .two-column-page .highlight-box {
            background: rgba(255,255,255,0.15);
            padding: 20px;
            border-radius: 8px;
            margin-top: 25px;
            text-align: center;
            font-weight: 600;
            font-size: 16px;
        }

        /* 图表+文本布局样式 */
        .chart-text-page .chart-text-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            align-items: center;
        }

        .chart-text-page .chart-section {
            min-height: 500px;
        }

        .chart-text-page .chart-container {
            position: relative;
            width: 100% !important;
            min-width: 300px !important;
            max-width: 100% !important;
            height: 500px;
            margin: 0 auto;
            background: var(--primary-background);
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            box-sizing: border-box;
        }

        .chart-text-page .chart-container canvas {
            width: 100% !important;
            height: 100% !important;
            display: block !important;
        }

        .chart-text-page .text-section {
            padding: 20px;
        }

        .chart-text-page .insight-title {
            font-size: 28px;
            font-weight: bold;
            color: var(--primary-accent);
            margin-bottom: 25px;
        }

        .chart-text-page .insight-list {
            list-style: none;
        }

        .chart-text-page .insight-list li {
            padding: 15px 0;
            font-size: 18px;
            line-height: 1.7;
            color: var(--text-dark);
            border-bottom: 1px solid #eee;
            position: relative;
            padding-left: 30px;
        }

        .chart-text-page .insight-list li::before {
            content: '💡';
            position: absolute;
            left: 0;
            font-size: 20px;
        }

        .chart-text-page .insight-list li:last-child {
            border-bottom: none;
        }

        .chart-text-page .highlight-box {
            background: rgba(248, 249, 250, 1);
            border-left: 4px solid var(--deep-blue);
            padding: 20px;
            border-radius: 4px;
            margin-top: 25px;
        }

        .chart-text-page .highlight-box p {
            font-size: 16px;
            color: var(--deep-blue);
            font-weight: 600;
            margin: 0;
        }

        /* 响应式 */
        @media (max-width: 768px) {
            .slide {
                padding: 30px 20px;
            }

            .slide-header h2 {
                font-size: 36px;
            }

            .two-column-page .comparison-container {
                grid-template-columns: 1fr;
                gap: 20px;
            }

            .two-column-page .comparison-container::before {
                display: none;
            }

            .chart-text-page .chart-text-container {
                grid-template-columns: 1fr;
                gap: 30px;
            }

            .chart-text-page .chart-container {
                height: 400px;
                min-height: 400px;
            }
        }

        @media (max-width: 480px) {
            .cover-content h1 {
                font-size: 36px;
            }

            .cover-content .subtitle {
                font-size: 24px;
            }
        }
    </style>
</head>
<body>
    <div id="presentation-container"></div>
```

**完成提示**：

```
输出："步骤3.3阶段1完成 - 已生成HTML框架和完整CSS样式
       请输入'继续'以生成JSON数据"
```

**【等待用户输入"继续"】**

#### 阶段2：生成JSON数据（包含所有幻灯片内容）

**目标**：生成完整的JSON数据，包含所有幻灯片内容。

**输出内容**：

```javascript
    <script>
        const presentationData = {
            "presentation": {
                "meta": {
                    "title": "[演示文稿标题]",
                    "subtitle": "[副标题]",
                    "author": "[作者]",
                    "date": "[日期]"
                },
                "slides": [
                    {
                        "id": 1,
                        "type": "cover",
                        "template": "01-cover-page",
                        "title": "封面页",
                        "content": {
                            "mainTitle": "[主标题]",
                            "subtitle": "[副标题]",
                            "meta": {
                                "date": "[日期]",
                                "author": "[作者]"
                            }
                        }
                    },
                    {
                        "id": 2,
                        "type": "toc",
                        "template": "08-table-of-contents",
                        "title": "目录",
                        "content": {
                            "items": [
                                { "number": "01", "title": "[章节标题]", "page": 3 },
                                { "number": "02", "title": "[章节标题]", "page": 8 },
                                ...
                            ]
                        }
                    },
                    {
                        "id": 3,
                        "type": "section",
                        "template": "11-chapter-overview",
                        "title": "[章节标题]",
                        "content": {
                            "subtitle": "[章节副标题]",
                            "description": "[章节描述]"
                        }
                    },
                    {
                        "id": 4,
                        "type": "content",
                        "template": "02-two-column-comparison",
                        "title": "[页面标题]",
                        "content": {
                            "leftColumn": {
                                "title": "[左列标题]",
                                "items": ["[要点1]", "[要点2]", ...],
                                "highlight": "[强调内容]"
                            },
                            "rightColumn": {
                                "title": "[右列标题]",
                                "items": ["[要点1]", "[要点2]", ...],
                                "highlight": "[强调内容]"
                            }
                        }
                    },
                    {
                        "id": 5,
                        "type": "content",
                        "template": "05-chart-text",
                        "title": "[页面标题]",
                        "content": {
                            "chart": {
                                "type": "bar",
                                "title": "[图表标题]",
                                "data": {
                                    "labels": ["[标签1]", "[标签2]", ...],
                                    "datasets": [{
                                        "label": "[数据集标签]",
                                        "data": [数值1, 数值2, ...],
                                        "backgroundColor": [
                                            "rgba(248, 93, 66, 0.8)",
                                            "rgba(85, 110, 230, 0.8)",
                                            ...
                                        ]
                                    }]
                                },
                                "options": {
                                    "responsive": true,
                                    "maintainAspectRatio": false
                                }
                            },
                            "insights": ["[洞察1]", "[洞察2]", ...],
                            "highlight": "[强调内容]"
                        }
                    },
                    ...
                ]
            }
        };
```

**⚠️ 重要说明**：

1. **数据完整性**：必须100%保留步骤2中的所有内容
2. **结构规范性**：必须遵循beauty-json/SKILL.md中的JSON数据结构规范
3. **模板匹配**：必须根据页面特征选择合适的模板类型
4. **图表配置**：必须正确配置所有图表数据

**完成提示**：

```
输出："步骤3.3阶段2完成 - 已生成JSON数据（包含所有幻灯片内容）
       总页数：N页
       请输入'继续'以生成HTML容器和JavaScript渲染逻辑"
```

**【等待用户输入"继续"】**

#### 阶段3：生成HTML容器和JavaScript渲染逻辑

**目标**：生成HTML容器和JavaScript渲染逻辑，实现JSON数据的动态渲染。

**输出内容**：

```javascript

        function renderCoverPage(content) {
            return `
                <div class="slide cover-page">
                    <div class="cover-content">
                        <h1>${content.mainTitle}</h1>
                        <div class="divider"></div>
                        <p class="subtitle">${content.subtitle}</p>
                        <div class="meta-info">
                            <p>报告日期：${content.meta.date}</p>
                            <p>作者：${content.meta.author}</p>
                        </div>
                    </div>
                </div>
            `;
        }

        function renderTocPage(content) {
            return `
                <div class="slide toc-page">
                    <div class="slide-header">
                        <h2>目录</h2>
                    </div>
                    <div class="toc-content">
                        ${content.items.map(item => `
                            <div class="toc-item">
                                <span class="toc-number">${item.number}</span>
                                <span class="toc-title">${item.title}</span>
                                <span class="toc-page">P${item.page}</span>
                            </div>
                        `).join('')}
                    </div>
                </div>
            `;
        }

        function renderSectionPage(content) {
            return `
                <div class="slide section-page">
                    <div class="section-content">
                        <h1>${content.subtitle}</h1>
                        <p class="section-description">${content.description}</p>
                    </div>
                </div>
            `;
        }

        function renderTwoColumnPage(content) {
            return `
                <div class="slide two-column-page">
                    <div class="slide-header">
                        <h2>${content.title}</h2>
                    </div>
                    <div class="comparison-container">
                        <div class="column left">
                            <div class="column-header">${content.leftColumn.title}</div>
                            <ul class="column-content">
                                ${content.leftColumn.items.map(item => `<li>${item}</li>`).join('')}
                            </ul>
                            <div class="highlight-box">
                                💡 ${content.leftColumn.highlight}
                            </div>
                        </div>
                        <div class="column right">
                            <div class="column-header">${content.rightColumn.title}</div>
                            <ul class="column-content">
                                ${content.rightColumn.items.map(item => `<li>${item}</li>`).join('')}
                            </ul>
                            <div class="highlight-box">
                                💡 ${content.rightColumn.highlight}
                            </div>
                        </div>
                    </div>
                </div>
            `;
        }

        function renderChartTextPage(content, slideId) {
            const canvasId = `chart-${slideId}`;

            return `
                <div class="slide chart-text-page">
                    <div class="slide-header">
                        <h2>${content.title}</h2>
                    </div>
                    <div class="chart-text-container">
                        <div class="chart-section">
                            <div class="chart-container">
                                <canvas id="${canvasId}"></canvas>
                            </div>
                        </div>
                        <div class="text-section">
                            <div class="insight-title">关键洞察</div>
                            <ul class="insight-list">
                                ${content.insights.map(insight => `<li>${insight}</li>`).join('')}
                            </ul>
                            <div class="highlight-box">
                                <p>💡 ${content.highlight}</p>
                            </div>
                        </div>
                    </div>
                </div>
            `;
        }

        function renderPresentation(data) {
            const container = document.getElementById('presentation-container');

            data.presentation.slides.forEach(slide => {
                let slideHTML = '';

                switch(slide.type) {
                    case 'cover':
                        slideHTML = renderCoverPage(slide.content);
                        break;
                    case 'toc':
                        slideHTML = renderTocPage(slide.content);
                        break;
                    case 'section':
                        slideHTML = renderSectionPage(slide.content);
                        break;
                    case 'content':
                        if (slide.template === '02-two-column-comparison') {
                            slideHTML = renderTwoColumnPage(slide.content);
                        } else if (slide.template === '05-chart-text') {
                            slideHTML = renderChartTextPage(slide.content, slide.id);
                        }
                        break;
                    default:
                        console.warn('Unknown slide type:', slide.type);
                }

                container.innerHTML += slideHTML;
            });

            renderCharts(data);
        }

        function renderCharts(data) {
            data.presentation.slides.forEach(slide => {
                if (slide.type === 'content' && slide.template === '05-chart-text' && slide.content.chart) {
                    const canvasId = `chart-${slide.id}`;
                    const ctx = document.getElementById(canvasId);

                    if (ctx) {
                        new Chart(ctx, {
                            type: slide.content.chart.type,
                            data: slide.content.chart.data,
                            options: {
                                ...slide.content.chart.options,
                                responsive: true,
                                maintainAspectRatio: false,
                                plugins: {
                                    legend: {
                                        display: true,
                                        position: 'top',
                                        labels: {
                                            font: {
                                                size: 14,
                                                family: '-apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", sans-serif'
                                            }
                                        }
                                    },
                                    title: {
                                        display: true,
                                        text: slide.content.chart.title,
                                        font: {
                                            size: 18,
                                            weight: 'bold',
                                            family: '-apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", sans-serif'
                                        },
                                        padding: 20,
                                        color: '#000000'
                                    },
                                    tooltip: {
                                        backgroundColor: 'rgba(0, 0, 0, 0.8)',
                                        titleFont: {
                                            size: 14,
                                            weight: 'bold'
                                        },
                                        bodyFont: {
                                            size: 13
                                        },
                                        padding: 12
                                    }
                                },
                                scales: {
                                    y: {
                                        beginAtZero: true,
                                        title: {
                                            display: true,
                                            text: slide.content.chart.data.datasets[0].label,
                                            font: {
                                                size: 14,
                                                weight: 'bold'
                                            },
                                            color: '#333333'
                                        },
                                        ticks: {
                                            font: {
                                                size: 13
                                            },
                                            color: '#333333'
                                        },
                                        grid: {
                                            color: '#f0f0f0'
                                        }
                                    },
                                    x: {
                                        ticks: {
                                            font: {
                                                size: 13
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
                }
            });
        }

        document.addEventListener('DOMContentLoaded', function() {
            renderPresentation(presentationData);
        });
```

**⚠️ 重要说明**：

1. **渲染函数完整性**：必须为每种幻灯片类型提供渲染函数
2. **图表渲染正确性**：必须正确配置所有图表选项
3. **响应式配置**：必须设置 `responsive: true` 和 `maintainAspectRatio: false`
4. **事件监听**：必须在DOMContentLoaded事件中初始化渲染

**完成提示**：

```
输出："步骤3.3阶段3完成 - 已生成HTML容器和JavaScript渲染逻辑
       请输入'继续'以生成结束标签"
```

**【等待用户输入"继续"】**

#### 阶段4：生成结束标签

**目标**：生成HTML文档的结束标签。

**输出内容**：

```html
    </script>
</body>
</html>
```

**完成提示**：

```
输出："步骤3.3阶段4完成 - 已生成结束标签
       HTML文件生成完成！
       总代码行数：约1300行
       已进入步骤3.4"
```

### ⚠️ Token限制处理：如果内容很多

```
如果JSON数据或JavaScript代码很长，必须分批生成：

阶段3a：生成HTML框架和CSS样式
├─ 生成完整的HTML文档框架
├─ 生成完整的CSS样式
└─ 输出："步骤3.3阶段3a完成 - 已生成HTML框架和CSS样式
       请输入'继续'以生成JSON数据"

【等待用户输入"继续"】

阶段3b：生成JSON数据（分批）
├─ 生成JSON数据的前半部分（前10页）
├─ 输出："步骤3.3阶段3b完成 - 已生成JSON数据前半部分（前10页）
       请输入'继续'以生成JSON数据后半部分"

【等待用户输入"继续"】

阶段3c：生成JSON数据后半部分
├─ 生成JSON数据的后半部分（剩余页面）
├─ 输出："步骤3.3阶段3c完成 - 已生成JSON数据后半部分（剩余页面）
       请输入'继续'以生成JavaScript渲染逻辑"

【等待用户输入"继续"】

阶段3d：生成JavaScript渲染逻辑
├─ 生成所有渲染函数
├─ 生成图表渲染逻辑
├─ 生成初始化代码
└─ 输出："步骤3.3阶段3d完成 - 已生成JavaScript渲染逻辑
       请输入'继续'以生成结束标签"

【等待用户输入"继续"】

阶段3e：生成结束标签
├─ 生成HTML结束标签
└─ 输出："步骤3.3阶段3e完成 - 已生成结束标签
       HTML文件生成完成！
       总代码行数：约1300行
       已进入步骤3.4"
```

### 输出产物

- 完整的HTML文件（约1300行）
- CSS样式（约800行）
- JSON数据（约200行，包含所有幻灯片内容）
- JavaScript代码（约300行，包含JSON解析和渲染逻辑）
- 图表配置（根据实际需求）

### 验证标准

- [ ] HTML结构完整且正确
- [ ] CSS样式完整且符合规范
- [ ] JavaScript代码完整且无错误
- [ ] JSON数据完整且格式正确
- [ ] JSON数据包含所有幻灯片内容
- [ ] JavaScript能够正确解析JSON数据
- [ ] JavaScript能够正确渲染HTML
- [ ] 所有图表都已正确配置
- [ ] 响应式设计完备
- [ ] 无语法错误

---

## 步骤 3.4：验证代码质量

### 目标

全面检查生成的HTML文件，确保代码质量和功能完整性。

### 验证项目

#### 1. 代码完整性检查

```
□ HTML结构完整
  - DOCTYPE声明正确
  - html、head、body标签完整
  - 所有标签正确闭合
  - 无语法错误

□ CSS样式完整
  - CSS变量定义完整
  - 所有样式类都已定义
  - 响应式样式完整
  - 无语法错误

□ JavaScript代码完整
  - 所有渲染函数都已定义
  - 图表渲染逻辑完整
  - 事件监听正确
  - 无语法错误

□ JSON数据完整
  - JSON格式正确（可通过JSON.parse验证）
  - JSON包含所有幻灯片数据
  - 每个幻灯片包含完整内容
  - 数据结构符合规范
  - 无数据遗漏
  - 无数据错误
```

#### 2. 数据完整性检查

```
□ 所有幻灯片都已包含
□ 所有内容都已包含（100%保留）
□ 所有数据都已包含
□ 所有图表都已包含
□ 无内容被压缩或省略
□ 无内容被篡改或简化
```

#### 3. HTML渲染功能检查

```
□ HTML能够正确加载JSON数据
□ JavaScript能够正确解析JSON
□ JavaScript能够正确渲染所有幻灯片
□ 所有内容正确显示
□ 所有图表正确显示
□ 导航功能正常
□ 响应式设计正常
```

#### 4. 设计规范验证（一票否决制）

```
**颜色规范验证**：
□ 使用McKinsey标准色板（#FFFFFF, #000000, #F85d42, #74788d, #556EE6, #34c38f, #50a5f1, #f1b44c）
□ 未使用紫色渐变背景
□ 未使用AI生成的色板
□ 未使用非McKinsey颜色组合
□ 主色调为白色背景+黑色标题
□ 强调色使用正确（#F85d42用于关键高亮）
□ 图表颜色使用标准色板
□ 对比度符合可读性标准（≥4.5:1）

**字体规范验证**：
□ 使用系统字体（-apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC"等）
□ 未使用Inter、Roboto、Arial等通用字体
□ 标题字体大小符合规范（48-64px）
□ 副标题字体大小符合规范（28-36px）
□ 正文字体大小符合规范（16-20px）
□ 图表标签字体大小符合规范（12-14px）
□ 字体粗细使用正确（标题bold，正文regular）
□ 行高符合规范（1.6-1.8）

**布局规范验证**：
□ 未使用圆角卡片（border-radius: 8px等）
□ 未使用通用模板布局
□ 边距符合规范（40-60px）
□ 元素间距符合规范（20-30px）
□ 两列布局间距符合规范（30-40px）
□ 图表容器最小高度符合规范（400px）
□ 所有元素对齐到网格
□ 视觉平衡良好

**设计风格验证**：
□ 整体风格符合McKinsey标准
□ 无装饰性图标或图形
□ 无不必要的动画效果
□ 阴影使用最小化（0-2px）
□ 边框使用最小化（仅在需要时使用）
□ 白空间充足（不拥挤）
□ 专业、简洁、无杂乱
```

#### 5. 功能验证

```
□ 基本功能正常
□ JSON数据加载正常
□ JSON解析正常
□ HTML渲染正常
□ 图表显示正常
□ 导航功能正常
□ 响应式设计正常
□ 浏览器兼容性良好
□ 无功能性问题
```

### 输出产物

- 代码完整性验证报告
- 数据完整性验证报告
- HTML渲染功能验证报告
- 设计规范验证报告
- 功能验证报告
- 最终验证报告

### 验证标准

- [ ] 所有验证项目都通过
- [ ] 无严重问题
- [ ] 可正常运行
- [ ] JSON格式正确
- [ ] HTML渲染正常
- [ ] 符合McKinsey标准
- [ ] **设计规范全部符合**（颜色、字体、布局、风格）
- [ ] **未使用非McKinsey风格元素**（紫色渐变、圆角卡片、通用模板等）

---

## 📊 预期输出

### 最终产物

1. **完整的HTML文件**
   - 文件名：`[文档标题]_McKinsey风格演示(JSON模式).html`
   - 文件大小：约70KB
   - 总代码行数：约1300行
   - 加载时间：<1秒（本地）
   - 依赖项：Chart.js CDN（唯一外部依赖）
   - 特点：JSON数据驱动，HTML动态渲染

2. **JSON数据**
   - 嵌入在HTML中的JSON数据
   - 包含所有幻灯片内容
   - 结构化数据格式
   - 易于维护和修改

3. **验收报告**
   - 代码完整性验证报告
   - 数据完整性验证报告
   - HTML渲染功能验证报告
   - 设计规范验证报告
   - 功能验证报告
   - 最终验证报告

### 质量标准

- **代码完整性**：A+（HTML、CSS、JavaScript、JSON都完整）
- **数据完整性**：A+（100%保留所有内容）
- **JSON数据质量**：A+（格式正确，结构完整）
- **HTML渲染质量**：A+（正确渲染JSON数据）
- **设计质量**：A+（完全符合McKinsey标准）
- **功能完整性**：A+（所有功能正常）
- **总体评分**：A+（优秀）

---

## 🎯 成功标准

### 执行成功标志

当以下所有条件都满足时，步骤3执行成功：

**流程完成度**：
- ✅ 所有4个步骤都已执行完成
- ✅ 步骤3.3的4个阶段都已执行完成
- ✅ 每个步骤的验证标准都通过
- ✅ 无步骤被跳过或中断

**资源使用验证**：
- ✅ 已读取所有必读资源（best-practices.md、mckinsey-design-system.md、presentation-template.html、TEMPLATE_USAGE_GUIDE.md、INDEX.md）
- ✅ 已读取JSON数据结构规范（beauty-json/SKILL.md）
- ✅ 已读取布局和图表示例索引（INDEX.md）
- ✅ 已检查并读取项目特定资源（.ppt_assets/INDEX.md，如果存在）

**代码完整性验证**：
- ✅ HTML结构完整且正确
- ✅ CSS样式完整且符合规范
- ✅ JavaScript代码完整且无错误
- ✅ JSON数据完整且格式正确
- ✅ JSON数据包含所有幻灯片内容
- ✅ JavaScript能够正确解析JSON数据
- ✅ JavaScript能够正确渲染HTML
- ✅ 所有图表都已正确配置
- ✅ 响应式设计完备
- ✅ 无语法错误

**数据完整性验证**：
- ✅ 所有幻灯片都已包含（100%保留）
- ✅ 所有内容都已包含（无压缩、无省略）
- ✅ 所有数据都已包含（数值、百分比、货币等）
- ✅ 所有图表都已包含（完整的图表配置）
- ✅ 无内容被篡改或简化

**HTML渲染验证**：
- ✅ HTML能够正确加载JSON数据
- ✅ JavaScript能够正确解析JSON
- ✅ JavaScript能够正确渲染所有幻灯片
- ✅ 所有内容正确显示
- ✅ 所有图表正确显示
- ✅ 导航功能正常
- ✅ 响应式设计正常

**设计规范验证**（一票否决制）：
- ✅ 颜色规范：使用McKinsey标准色板，未使用紫色渐变、AI生成色板
- ✅ 字体规范：使用系统字体，未使用Inter、Roboto、Arial等通用字体
- ✅ 布局规范：未使用圆角卡片、通用模板布局
- ✅ 设计风格：符合McKinsey标准，专业、简洁、无杂乱

**功能验证**：
- ✅ HTML文件可以正常运行
- ✅ JSON数据可以正确加载
- ✅ JSON数据可以正确解析
- ✅ HTML可以正确渲染
- ✅ 所有功能都正常工作
- ✅ 图表显示正常
- ✅ 导航功能正常
- ✅ 响应式设计正常

**输出**：McKinsey风格HTML演示文稿（JSON+HTML模式）
