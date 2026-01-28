---
name: "beauty-json"
description: "Convert HTML slide templates to JSON+HTML format. Invoke when generating JSON data for beauty-normal command or converting existing HTML examples to JSON-driven templates."
---

# Beauty-Json Skill

将HTML幻灯片示例文件转换为JSON+HTML格式，实现数据与展示分离。

## 📋 核心功能

**主要任务**：
1. 读取HTML示例文件（从 `beauty-html/assets/` 目录）
2. 提取HTML框架结构（去除具体内容）
3. 生成JSON数据结构（包含所有内容）
4. 创建JSON驱动的HTML模板

**适用场景**：
- 为 `beauty-normal` 命令生成JSON数据
- 将现有HTML示例转换为JSON+HTML格式
- 创建新的JSON驱动的幻灯片模板

---

## 🎯 JSON数据结构规范

### 1. 根结构

```json
{
  "presentation": {
    "meta": {
      "title": "演示文稿标题",
      "subtitle": "副标题",
      "author": "作者",
      "date": "日期"
    },
    "slides": [
      {
        "id": 1,
        "type": "cover|toc|section|content|end",
        "template": "01-cover-page|02-two-column|03-three-column|05-chart-text|...",
        "title": "幻灯片标题",
        "content": { ... }
      }
    ]
  }
}
```

### 2. 幻灯片类型与内容结构

#### 2.1 封面页 (cover)

```json
{
  "id": 1,
  "type": "cover",
  "template": "01-cover-page",
  "title": "封面页",
  "content": {
    "mainTitle": "跨境垂直平台战略报告",
    "subtitle": "平台模式 vs 个人IP模式深度分析",
    "meta": {
      "date": "2026年1月",
      "author": "战略分析团队"
    }
  }
}
```

#### 2.2 双列对比页 (two-column)

```json
{
  "id": 2,
  "type": "content",
  "template": "02-two-column-comparison",
  "title": "平台模式 vs 个人IP模式",
  "content": {
    "leftColumn": {
      "title": "平台模式",
      "items": [
        "可复制性强，易于规模化",
        "网络效应明显，壁垒高",
        "生态闭环，数据价值高",
        "资本吸引力强，估值高",
        "运营复杂度高，投入大",
        "冷启动困难，需要临界规模"
      ],
      "highlight": "适合：有资本、有资源、追求规模"
    },
    "rightColumn": {
      "title": "个人IP模式",
      "items": [
        "启动快，成本低",
        "个人影响力强，粘性高",
        "灵活性强，转型容易",
        "现金流稳定，风险低",
        "规模化困难，天花板低",
        "个人依赖强，不易复制"
      ],
      "highlight": "适合：个人创业者、内容创作者"
    }
  }
}
```

#### 2.3 三列布局页 (three-column)

```json
{
  "id": 3,
  "type": "content",
  "template": "03-three-column",
  "title": "三大核心策略",
  "content": {
    "columns": [
      {
        "title": "策略一",
        "items": ["要点1", "要点2", "要点3"],
        "icon": "📊"
      },
      {
        "title": "策略二",
        "items": ["要点1", "要点2", "要点3"],
        "icon": "🎯"
      },
      {
        "title": "策略三",
        "items": ["要点1", "要点2", "要点3"],
        "icon": "💡"
      }
    ]
  }
}
```

#### 2.4 图表+文本页 (chart-text)

```json
{
  "id": 4,
  "type": "content",
  "template": "05-chart-text",
  "title": "六大平台收入增长对比",
  "content": {
    "chart": {
      "type": "bar",
      "title": "2024年收入对比",
      "data": {
        "labels": ["GrowthBi", "Finder", "Foundy", "Clarity", "Panda", "Omega"],
        "datasets": [{
          "label": "年收入（百万美元）",
          "data": [120, 95, 88, 45, 35, 28],
          "backgroundColor": [
            "rgba(248, 93, 66, 0.8)",
            "rgba(85, 110, 230, 0.8)",
            "rgba(80, 165, 241, 0.8)",
            "rgba(52, 195, 143, 0.8)",
            "rgba(241, 180, 76, 0.8)",
            "rgba(116, 120, 141, 0.8)"
          ]
        }]
      },
      "options": {
        "responsive": true,
        "maintainAspectRatio": false
      }
    },
    "insights": [
      "GrowthBi引领增长，年增长率达120%",
      "Finder和Foundy保持稳健增长（80-90%）",
      "传统平台增长乏力，增速低于50%",
      "会员订阅模式是增长核心驱动力",
      "高客单价服务贡献主要利润"
    ],
    "highlight": "启示：会员订阅（稳定现金流）+ 高客单价服务（利润来源）是最佳商业模式"
  }
}
```

#### 2.5 目录页 (toc)

```json
{
  "id": 5,
  "type": "toc",
  "template": "08-table-of-contents",
  "title": "目录",
  "content": {
    "items": [
      { "number": "01", "title": "市场分析", "page": 3 },
      { "number": "02", "title": "竞争格局", "page": 8 },
      { "number": "03", "title": "战略建议", "page": 15 },
      { "number": "04", "title": "实施路径", "page": 22 }
    ]
  }
}
```

#### 2.6 章节首页 (section)

```json
{
  "id": 6,
  "type": "section",
  "template": "11-chapter-overview",
  "title": "第一章 市场分析",
  "content": {
    "subtitle": "市场规模与增长趋势",
    "description": "深入分析当前市场状况，识别关键增长机会"
  }
}
```

#### 2.7 数据强调页 (data-emphasis)

```json
{
  "id": 7,
  "type": "content",
  "template": "06-data-emphasis",
  "title": "关键数据",
  "content": {
    "metrics": [
      {
        "value": "120%",
        "label": "年增长率",
        "description": "市场高速增长"
      },
      {
        "value": "$5.2B",
        "label": "市场规模",
        "description": "2024年市场规模"
      },
      {
        "value": "85%",
        "label": "市场份额",
        "description": "头部企业占比"
      }
    ]
  }
}
```

---

## 🎨 HTML框架模板规范

### 1. 通用HTML结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>McKinsey风格演示文稿</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <style>
        /* CSS样式 - McKinsey规范 */
    </style>
</head>
<body>
    <div id="presentation-container"></div>

    <script>
        // JSON数据
        const presentationData = {
            "presentation": {
                "meta": { ... },
                "slides": [ ... ]
            }
        };

        // 渲染函数
        function renderPresentation(data) {
            const container = document.getElementById('presentation-container');
            // 渲染逻辑
        }

        // 初始化
        document.addEventListener('DOMContentLoaded', function() {
            renderPresentation(presentationData);
        });
    </script>
</body>
</html>
```

### 2. 模板渲染函数

#### 2.1 封面页渲染

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
```

#### 2.2 双列对比页渲染

```javascript
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
```

#### 2.3 图表+文本页渲染

```javascript
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
```

---

## 🔄 转换流程

### 步骤1：读取HTML示例文件

```javascript
function readHTMLTemplate(templateName) {
    const templatePath = `beauty-html/assets/${templateName}.html`;
    // 读取HTML文件内容
}
```

### 步骤2：提取HTML框架

**提取规则**：
1. 保留完整的HTML结构（DOCTYPE, html, head, body）
2. 保留CSS样式（完整的<style>标签）
3. 保留JavaScript框架（完整的<script>标签结构）
4. 移除具体内容数据（替换为占位符或数据绑定）
5. 保留图表配置框架（移除具体数据）

### 步骤3：生成JSON数据

**数据提取规则**：
1. 从HTML中提取所有文本内容
2. 识别数据结构（列表、表格、图表数据）
3. 按照JSON结构规范组织数据
4. 确保数据完整性（100%保留）

### 步骤4：创建JSON驱动的HTML

**整合规则**：
1. 使用提取的HTML框架
2. 嵌入JSON数据（在<script>标签中）
3. 实现渲染函数（根据JSON数据动态生成HTML）
4. 确保图表正确渲染（Chart.js配置）

---

## 📊 支持的模板类型

| 模板文件 | 模板类型 | JSON结构 |
|---------|---------|---------|
| 01-cover-page.html | 封面页 | cover |
| 02-two-column-comparison.html | 双列对比 | two-column |
| 03-three-column.html | 三列布局 | three-column |
| 04-card-grid.html | 卡片网格 | card-grid |
| 05-chart-text.html | 图表+文本 | chart-text |
| 06-data-emphasis.html | 数据强调 | data-emphasis |
| 08-table-of-contents.html | 目录页 | toc |
| 11-chapter-overview.html | 章节首页 | section |
| 12-traffic-analysis.html | 流量分析 | chart-text |
| 13-user-positioning.html | 用户定位 | chart-text |
| 14-user-demand-rating.html | 用户需求评分 | chart-text |

---

## 🎯 使用示例

### 示例1：转换封面页

**输入HTML**：`01-cover-page.html`

**输出JSON**：
```json
{
  "presentation": {
    "slides": [{
      "id": 1,
      "type": "cover",
      "template": "01-cover-page",
      "title": "封面页",
      "content": {
        "mainTitle": "跨境垂直平台战略报告",
        "subtitle": "平台模式 vs 个人IP模式深度分析",
        "meta": {
          "date": "2026年1月",
          "author": "战略分析团队"
        }
      }
    }]
  }
}
```

**输出HTML框架**：
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>McKinsey风格演示文稿</title>
    <style>
        /* 完整的CSS样式（从原HTML提取） */
    </style>
</head>
<body>
    <div id="presentation-container"></div>

    <script>
        const presentationData = { /* JSON数据 */ };

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

        function renderPresentation(data) {
            const container = document.getElementById('presentation-container');
            data.presentation.slides.forEach(slide => {
                if (slide.type === 'cover') {
                    container.innerHTML += renderCoverPage(slide.content);
                }
            });
        }

        document.addEventListener('DOMContentLoaded', function() {
            renderPresentation(presentationData);
        });
    </script>
</body>
</html>
```

### 示例2：转换图表+文本页

**输入HTML**：`05-chart-text.html`

**输出JSON**：
```json
{
  "presentation": {
    "slides": [{
      "id": 4,
      "type": "content",
      "template": "05-chart-text",
      "title": "六大平台收入增长对比",
      "content": {
        "chart": {
          "type": "bar",
          "title": "2024年收入对比",
          "data": {
            "labels": ["GrowthBi", "Finder", "Foundy", "Clarity", "Panda", "Omega"],
            "datasets": [{
              "label": "年收入（百万美元）",
              "data": [120, 95, 88, 45, 35, 28],
              "backgroundColor": [
                "rgba(248, 93, 66, 0.8)",
                "rgba(85, 110, 230, 0.8)",
                "rgba(80, 165, 241, 0.8)",
                "rgba(52, 195, 143, 0.8)",
                "rgba(241, 180, 76, 0.8)",
                "rgba(116, 120, 141, 0.8)"
              ]
            }]
          },
          "options": {
            "responsive": true,
            "maintainAspectRatio": false
          }
        },
        "insights": [
          "GrowthBi引领增长，年增长率达120%",
          "Finder和Foundy保持稳健增长（80-90%）",
          "传统平台增长乏力，增速低于50%",
          "会员订阅模式是增长核心驱动力",
          "高客单价服务贡献主要利润"
        ],
        "highlight": "启示：会员订阅（稳定现金流）+ 高客单价服务（利润来源）是最佳商业模式"
      }
    }]
  }
}
```

---

## ⚠️ Token限制处理原则（严格执行，不得偷工减料）

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

---

## ⚠️ 注意事项

### 1. 数据完整性
- ✅ 必须100%保留原HTML中的所有内容
- ✅ 不得遗漏任何文本、数据、图表信息
- ✅ 确保JSON数据结构完整

### 2. 设计规范
- ✅ 严格遵循McKinsey设计规范
- ✅ 使用标准色板（#FFFFFF, #000000, #F85d42, #74788d, #556EE6, #34c38f, #50a5f1, #f1b44c）
- ✅ 使用系统字体（-apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC"等）
- ✅ 禁止使用非McKinsey风格元素（紫色渐变、圆角卡片、通用模板等）

### 3. 图表配置
- ✅ 强制设置 `responsive: true`
- ✅ 强制设置 `maintainAspectRatio: false`
- ✅ 强制设置 `width: 100% !important`
- ✅ 确保图表容器最小高度为400px

### 4. 响应式设计
- ✅ 保留所有响应式CSS规则
- ✅ 确保移动端显示正常
- ✅ 保持McKinsey设计标准

### 5. 代码质量
- ✅ HTML结构完整且正确
- ✅ CSS样式完整且符合规范
- ✅ JavaScript代码完整且无错误
- ✅ 无语法错误
- ✅ 无冗余代码

---

## 🚀 执行流程

### 自动化转换流程

```
开始
  ↓
步骤1：读取HTML示例文件
  ├─ 从beauty-html/assets/读取HTML文件
  ├─ 解析HTML结构
  └─ 提取CSS和JavaScript框架
  ↓
步骤2：提取HTML框架
  ├─ 保留HTML结构
  ├─ 保留CSS样式
  ├─ 保留JavaScript框架
  └─ 移除具体内容数据
  ↓
步骤3：生成JSON数据
  ├─ 提取所有文本内容
  ├─ 识别数据结构
  ├─ 组织JSON数据
  └─ 验证数据完整性
  ↓
步骤4：创建JSON驱动的HTML
  ├─ 整合HTML框架
  ├─ 嵌入JSON数据
  ├─ 实现渲染函数
  └─ 验证渲染效果
  ↓
完成！输出JSON数据和HTML文件
```

---

## 📝 输出产物

### 1. JSON数据文件
- 文件名：`[模板名称]_data.json`
- 格式：标准JSON格式
- 内容：包含所有幻灯片内容数据

### 2. HTML框架文件
- 文件名：`[模板名称]_template.html`
- 格式：标准HTML5格式
- 内容：HTML框架 + CSS样式 + JavaScript渲染逻辑

### 3. 完整HTML文件
- 文件名：`[模板名称]_complete.html`
- 格式：标准HTML5格式
- 内容：HTML框架 + JSON数据 + 渲染逻辑

---

## 🎯 成功标准

### 转换成功标志

当以下所有条件都满足时，转换成功：

**数据完整性**：
- ✅ 所有原HTML内容都已提取到JSON
- ✅ 无内容遗漏或丢失
- ✅ 数据结构符合规范
- ✅ JSON格式正确

**代码完整性**：
- ✅ HTML结构完整且正确
- ✅ CSS样式完整且符合规范
- ✅ JavaScript代码完整且无错误
- ✅ 渲染函数正确实现

**功能验证**：
- ✅ HTML可以正确加载JSON数据
- ✅ JavaScript可以正确解析JSON
- ✅ JavaScript可以正确渲染HTML
- ✅ 所有内容正确显示
- ✅ 所有图表正确显示
- ✅ 响应式设计正常

**设计规范**：
- ✅ 严格遵循McKinsey设计规范
- ✅ 使用标准色板
- ✅ 使用系统字体
- ✅ 未使用非McKinsey风格元素
