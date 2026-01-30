---
description: "Transform documents into professional McKinsey-style HTML presentations (JSON+HTML mode). Strictly follow 4-step workflow: Document Analysis → Slide Design → JSON Data Generation → HTML Rendering. Ensures 100% content preservation and McKinsey design standards. 将文档转化为专业 McKinsey 风格 HTML 演示文稿（JSON+HTML模式）。严格遵循4步流程：文档分析 → 幻灯片设计 → JSON数据生成 → HTML渲染，确保100%内容保留和McKinsey设计标准。"
args:
  - name: document
    description: "Document path to convert (supports .md, .txt, .json, .html) / 要转换的文档路径（支持 .md, .txt, .json, .html）"
    required: true
---

# Beauty-Normal 命令 / Beauty-Normal Command

将文档、数据、结论等信息转化为通俗连贯、明确清晰的 McKinsey 风格 HTML 演示文稿（使用 JSON+HTML 模式生成）。

Transform documents, data, and conclusions into clear and coherent McKinsey-style HTML presentations (using JSON+HTML mode generation).

## ⚠️ 核心原则 / Core Principles

**CRITICAL: Must strictly follow this 4-step workflow. No steps can be skipped!**
**关键：必须严格遵循以下4步固定流程，不得跳过任何步骤！**

### Step Workflow Enforcement / 步骤流程强制执行

**🔑 Steps 2 & 3: Mandatory Resource Reading / 步骤2、3必须读取skill资源**

**Step 2 (Chart Selection / 图文选择)** - MUST read:
- `beauty-html/references/chart-selection-guide.md`
- `beauty-html/assets/CHART_EXAMPLES_INDEX.md`
- `beauty-html/assets/INSIGHT_VISUALIZATION_GUIDE.md`

**Step 3 (JSON Data Generation / JSON数据生成)** - MUST read:
- `beauty-html/references/best-practices.md`
- `beauty-html/references/mckinsey-design-system.md`
- `beauty-html/assets/presentation-template.html`
- `beauty-html/assets/TEMPLATE_USAGE_GUIDE.md`

**🔑 Step 4: Critical Validation - One-Vote Veto System / 第4步：关键验收 - 一票否决制**

**Content Integrity Check / 内容完整性检验**:
- ✅ MUST preserve 100% of original content (chapters, data, conclusions)
- ✅ 必须100%保留原文所有章节、数据、结论，零遗漏

**JSON Data Check / JSON数据检验**:
- ✅ JSON format MUST be correct
- ✅ Data structure MUST be complete
- ✅ JSON格式必须正确，数据结构必须完整

**HTML Rendering Check / HTML渲染检验**:
- ✅ HTML MUST correctly render JSON data
- ✅ HTML必须能正确渲染JSON数据

**Code Quality Check / 代码质量检验**:
- ✅ MUST follow HTML best practices
- ✅ MUST be accessible and runnable
- ✅ 必须符合HTML最佳实践，可访问可运行

**Resource Usage Check / 资源使用检验**:
- ✅ MUST verify Steps 2 & 3 correctly read and used skill resources
- ✅ 必须验证步骤2和步骤3是否正确读取并使用了skill资源

**Rollback on Issues / 发现问题立即回退**:
- ⚠️ If ANY check fails, rollback to the corresponding step and re-execute
- ⚠️ 返回对应步骤重新执行，绝不将就

**⚠️ Token Limit Handling / Token限制处理原则**

**🔑 CORE RULE (MUST STRICTLY FOLLOW) / 最核心规则（必须严格遵守）**:
- ✅ If data is too large or token limit reached, automatically use "continue" mechanism for segmented loading
- ✅ 如果数据内容过大，或者token过长，则自动使用'继续'进行'分段'加载数据
- ❌ NEVER simplify, cut corners, or save tokens by skipping content
- ❌ 绝对不能精简、偷工减料的节省token
- ❌ STRICTLY PROHIBITED: Skipping content or using summaries to save tokens
- ❌ 严禁为了省token而跳过内容或使用摘要

**When encountering token limits / 当遇到 token 限制时:**

**❌ PROHIBITED Actions / 禁止行为**:
- ❌ Compress or omit resource reading / 压缩或省略资源读取
- ❌ Skip mandatory resources / 跳过必读资源
- ❌ Simplify execution steps / 简化执行步骤
- ❌ Reduce generated content / 减少生成内容
- ❌ Use summaries instead of complete content / 使用摘要代替完整内容
- ❌ Simplify data content / 精简数据内容
- ❌ Cut corners to save tokens / 偷工减料节省token

**✅ CORRECT Approach: Use "Continue" Mechanism / 正确处理方式：使用"继续"机制**

```
1. Complete the current executable portion
   完成当前可执行的部分后
   
2. Explicitly state: "Due to token limit, task incomplete. Please input '继续' to get remaining parts"
   明确说明："由于 token 限制，任务未完成，请输入'继续'以获取剩余部分"
   
3. Wait for user to input "continue" / "继续"
   等待用户输入"继续"后
   
4. Continue with remaining steps
   继续执行剩余步骤
   
5. Repeat until task fully completed
   重复直到任务完全完成
```

**Segmented Loading Principles / 分段加载原则**:
- ✅ **Complete Preservation / 完整保留**: Every segment MUST preserve 100% of data, no omissions, no compression
  每段数据都必须100%保留，无遗漏、无压缩
  
- ✅ **Clear Segmentation / 分段清晰**: Clearly indicate current segment number and total segments
  明确标注当前是第几段，共几段
  
- ✅ **Continuous Execution / 连续执行**: Auto-prompt "continue" after each segment, wait for user confirmation
  每段完成后自动提示"继续"，等待用户确认
  
- ✅ **Quality Priority / 质量优先**: Better multiple rounds than lower quality
  宁可多轮对话，不可降低质量
  
- ❌ **NO Simplification / 禁止精简**: NEVER simplify data content to save tokens
  绝对不能为了省token而精简数据内容
  
- ❌ **NO Shortcuts / 禁止偷工**: NEVER cut corners to save tokens
  绝对不能为了省token而偷工减料

**Key Rules / 关键规则**:
- ✅ **Quality > Speed** / **质量 > 速度**: Better multiple rounds than lower quality / 宁可多轮对话，不可降低质量
- ✅ **Complete > Simplified** / **完整 > 简化**: Better multiple executions than compressed content / 宁可分多次执行，不可压缩内容
- ✅ **Standard > Compromise** / **标准 > 妥协**: Better trigger continue than cut corners / 宁可触发继续，不可偷工减料

---

## 📋 固定4步执行流程 / 4-Step Workflow

### ⚠️ Execution Enforcement / 执行强制机制

**Before starting ANY step, Claude Code MUST:**
**在开始任何步骤之前，Claude Code 必须：**

1. **Verify prerequisite completion / 验证前置条件完成**
   - Check if previous step output exists / 检查上一步输出是否存在
   - Validate previous step output quality / 验证上一步输出质量
   
2. **Invoke the correct skill / 调用正确的skill**
   - Step 1 → `beauty-step1` skill
   - Step 2 → `beauty-step2` skill  
   - Step 3 → `beauty-normal-step3` skill (⚠️ Note: different from beauty command)
   - Step 4 → `beauty-normal-step4` skill (⚠️ Note: different from beauty command)

3. **Cannot skip to next step until / 不能跳到下一步，除非:**
   - Current step fully completed / 当前步骤完全完成
   - All verification checks passed / 所有验证检查通过
   - Output artifacts generated / 输出产物已生成

---

### 步骤 1️⃣: Document Content Analysis / 文档内容分析合并

**Goal / 目标**: Fully understand source document, extract key information, establish content structure.
完整理解源文档内容，提取关键信息，建立内容结构。

**Execution Method / 执行方式**: Invoke `beauty-step1` skill / 调用 `beauty-step1` skill

**⚠️ Important Notes / 重要说明**:
- Reads entire document without modification or deletion
  此步骤会完整阅读源文档，不做任何修改或删减
  
- If document too long, skill automatically uses "continue" mechanism for batch reading
  如果文档过长，skill会自动使用"继续"机制分批读取
  
- **🔑 CORE RULE**: NEVER simplify or cut corners to save tokens
  **🔑 最核心规则**：绝对不能精简、偷工减料节省token
  
- **🔑 CORE PRINCIPLE**: If data too large or tokens too long, automatically use 'continue' for segmented loading, preserve 100% content, STRICTLY PROHIBITED to skip content or use summaries to save tokens
  **🔑 核心原则**：如果数据内容过大，或者token过长，则自动使用'继续'进行'分段'加载数据，100%保留所有内容，严禁为了省token而跳过内容或使用摘要

**Output Artifacts / 输出产物**:
- Content structure outline (includes all chapters and key points)
  内容结构大纲（包含所有章节和要点）
  
- Data point list (all values visualizable)
  数据点清单（所有可用于可视化的数值）
  
- Key conclusions list (must be fully preserved)
  关键结论列表（必须完整保留）

**Validation Criteria / 验证标准**:
- [ ] All original content extracted / 所有原文内容已提取
- [ ] No content loss or omission / 无内容丢失或遗漏
- [ ] Data points fully recorded / 数据点完整记录
- [ ] Logical structure clear / 逻辑结构清晰

---

### 步骤 2️⃣：幻灯片内容转换与拆分

**目标**：将文档内容完整转换为结构化的幻灯片页面，确保内容零遗漏、逻辑清晰、页面适量。

**执行方式**：调用 `beauty-step2` skill

**⚠️ 核心原则**：
- ✅ 100%保留原文所有内容，零遗漏、零压缩、零简化
- ✅ 每页内容不超过8个要点，超过则分页展示
- ✅ 遇到内容过多时，使用"继续"机制分批处理
- ❌ 绝对禁止为了省token而压缩、省略、简化内容
- **🔑 最核心规则：如果数据内容过大，或者token过长，则自动使用'继续'进行'分段'加载数据，绝对不能精简、偷工减料的节省token,严禁为了省token而跳过内容或使用摘要**

**🔑 必读资源**：
- `beauty-html/references/chart-selection-guide.md`
- `beauty-html/assets/CHART_EXAMPLES_INDEX.md`
- `beauty-html/assets/INSIGHT_VISUALIZATION_GUIDE.md`

**执行流程**（由skill自动执行）：
```
步骤2.1：识别文档结构层次
  ↓
步骤2.2：规划幻灯片页面类型
  ↓
步骤2.3：拆分内容到具体页面
  ↓
步骤2.4：验证内容完整性
```

**输出产物**：
- 完整的幻灯片页面清单（从第1页到第N页）
- 每页的详细内容（100%原文，无压缩）
- 每页的数据点、图表、表格（如有）
- 页面总数确认

**验证标准**：
- [ ] 所有页面已详细列出
- [ ] 每页内容完整（100%原文）
- [ ] 每页要点数≤8个
- [ ] 数据、图表、表格完整
- [ ] 页面编号连续
- [ ] 无内容遗漏

---

### 步骤 3️⃣：JSON数据生成与HTML渲染

**目标**：将步骤2生成的幻灯片页面清单转换为JSON格式数据，并使用JSON+HTML方式生成最终的McKinsey风格HTML文件。

**执行方式**：调用 `beauty-normal-step3` skill

**⚠️ 核心原则**：
- ✅ 必须读取并参考skill资源
- ✅ **强制使用** `best-practices.md` 和 `mckinsey-design-system.md` 中的所有设计规范
- ✅ **颜色规范强制执行**：必须使用McKinsey标准色板，禁止使用紫色渐变、AI生成色板
- ✅ **字体规范强制执行**：必须使用系统字体，禁止使用Inter、Roboto、Arial等通用字体
- ✅ **布局规范强制执行**：必须遵循McKinsey布局标准，禁止使用圆角卡片、通用模板
- ✅ **JSON数据结构规范**：必须使用标准JSON格式，包含所有幻灯片数据
- ✅ **HTML渲染规范**：HTML必须能够正确解析和渲染JSON数据
- ✅ 每个阶段的代码必须是完整的语法单元
- ✅ CSS必须在阶段1一次性完整生成
- ✅ JSON数据必须在阶段2完整生成
- ✅ HTML框架必须在阶段3完整生成
- ✅ JavaScript必须在阶段4完整生成（包含JSON数据解析和渲染逻辑）
- ✅ 每个阶段结束后提示用户输入"继续"
- ❌ 禁止跨阶段截断HTML标签
- ❌ 禁止省略CSS样式
- ❌ 禁止简化JSON数据结构
- ❌ 禁止简化图表代码
- ❌ **禁止使用非McKinsey风格的设计元素**（紫色渐变、圆角卡片、通用模板等）
- **🔑 最核心规则：如果数据内容过大，或者token过长，则自动使用'继续'进行'分段'加载数据，绝对不能精简、偷工减料的节省token,严禁为了省token而跳过内容或使用摘要**

**🔑 必读资源（强制执行）**：
- `beauty-html/references/best-practices.md` - **必须严格遵循所有最佳实践**
- `beauty-html/references/mckinsey-design-system.md` - **必须严格遵循所有设计规范**
- `beauty-html/assets/presentation-template.html` - 参考模板结构
- `beauty-html/assets/TEMPLATE_USAGE_GUIDE.md` - 模板使用指南

**执行流程**（由skill自动执行）：
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

**JSON数据结构规范**：
```json
{
  "presentation": {
    "title": "演示文稿标题",
    "subtitle": "副标题",
    "author": "作者",
    "date": "日期",
    "slides": [
      {
        "id": 1,
        "type": "cover|toc|section|content|end",
        "title": "幻灯片标题",
        "content": {
          "heading": "主标题",
          "subheading": "副标题",
          "points": ["要点1", "要点2", "..."],
          "data": {
            "chart": {
              "type": "bar|line|pie|table",
              "config": {...}
            }
          }
        }
      }
    ]
  }
}
```

**输出产物**：
- 完整的HTML文件（约1300行）
- CSS样式（约800行）
- JSON数据（约200行，包含所有幻灯片内容）
- JavaScript代码（约300行，包含JSON解析和渲染逻辑）
- 图表配置（根据实际需求）

**验证标准**：

**代码完整性**：
- [ ] HTML结构完整
- [ ] CSS样式完整
- [ ] JavaScript功能完整
- [ ] JSON数据结构完整且格式正确
- [ ] JSON数据包含所有幻灯片内容
- [ ] JavaScript能够正确解析JSON数据
- [ ] JavaScript能够正确渲染HTML
- [ ] 所有图表已配置
- [ ] 响应式设计完备
- [ ] 无语法错误

**JSON数据验证**：
- [ ] JSON格式正确（可通过JSON.parse验证）
- [ ] JSON包含所有幻灯片数据
- [ ] 每个幻灯片包含完整内容
- [ ] 数据结构符合规范
- [ ] 无数据遗漏
- [ ] 无数据错误

**HTML渲染验证**：
- [ ] HTML能够正确加载JSON数据
- [ ] JavaScript能够正确解析JSON
- [ ] JavaScript能够正确渲染所有幻灯片
- [ ] 所有内容正确显示
- [ ] 所有图表正确显示
- [ ] 导航功能正常

**设计规范强制检查（一票否决制）**：

**颜色规范检查**：
- [ ] 使用McKinsey标准色板（#FFFFFF, #000000, #F85d42, #74788d, #556EE6, #34c38f, #50a5f1, #f1b44c）
- [ ] 未使用紫色渐变背景
- [ ] 未使用AI生成的色板
- [ ] 未使用非McKinsey颜色组合
- [ ] 主色调为白色背景+黑色标题
- [ ] 强调色使用正确（#F85d42用于关键高亮）
- [ ] 图表颜色使用标准色板
- [ ] 对比度符合可读性标准（≥4.5:1）

**字体规范检查**：
- [ ] 使用系统字体（-apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC"等）
- [ ] 未使用Inter、Roboto、Arial等通用字体
- [ ] 标题字体大小符合规范（48-64px）
- [ ] 副标题字体大小符合规范（28-36px）
- [ ] 正文字体大小符合规范（16-20px）
- [ ] 图表标签字体大小符合规范（12-14px）
- [ ] 字体粗细使用正确（标题bold，正文regular）
- [ ] 行高符合规范（1.6-1.8）

**布局规范检查**：
- [ ] 未使用圆角卡片（border-radius: 8px等）
- [ ] 未使用通用模板布局
- [ ] 边距符合规范（40-60px）
- [ ] 元素间距符合规范（20-30px）
- [ ] 两列布局间距符合规范（30-40px）
- [ ] 图表容器最小高度符合规范（400px）
- [ ] 所有元素对齐到网格
- [ ] 视觉平衡良好

**设计风格检查**：
- [ ] 整体风格符合McKinsey标准
- [ ] 无装饰性图标或图形
- [ ] 无不必要的动画效果
- [ ] 阴影使用最小化（0-2px）
- [ ] 边框使用最小化（仅在需要时使用）
- [ ] 白空间充足（不拥挤）
- [ ] 专业、简洁、无杂乱

---

### 步骤 4️⃣：代码内容审核检验

**⚠️ 最关键步骤！必须严格执行！**

**目标**：全面检查生成的 HTML 演示文稿，确保质量和完整性。

**执行方式**：调用 `beauty-normal-step4` skill

**⚠️ 核心原则**：实行一票否决制
- **内容完整性检验**：必须100%保留原文所有章节、数据、结论，零遗漏
- **JSON数据检验**：JSON格式必须正确，数据结构必须完整
- **HTML渲染检验**：HTML必须能正确渲染JSON数据
- **代码质量检验**：必须符合HTML最佳实践，可访问可运行
- **资源使用检验**：必须验证步骤2和步骤3是否正确读取并使用了skill资源
- **发现问题立即回退**：返回对应步骤重新执行，绝不将就

**执行流程**（由skill自动执行）：
```
步骤4.1：资源使用验证
  ↓
步骤4.2：内容完整性检查
  ↓
步骤4.3：JSON数据格式检查
  ↓
步骤4.4：HTML渲染功能检查
  ↓
步骤4.5：代码质量检查
  ↓
步骤4.6：功能验证
  ↓
步骤4.7：生成最终报告
```

**验证项目**：

#### 资源使用验证
```
步骤2资源：
□ 已读取：references/chart-selection-guide.md
□ 已读取：assets/CHART_EXAMPLES_INDEX.md
□ 已读取：assets/INSIGHT_VISUALIZATION_GUIDE.md

步骤3资源：
□ 已读取：references/best-practices.md
□ 已读取：references/mckinsey-design-system.md
□ 已读取：assets/presentation-template.html
□ 已读取：assets/TEMPLATE_USAGE_GUIDE.md
```

#### 内容完整性检查
```
□ 所有章节都已包含
□ 所有要点都已包含
□ 所有数据都已包含
□ 所有表格都已包含
□ 所有结论都已包含
□ 无内容被压缩或省略
□ 无内容被篡改或简化
```

#### JSON数据格式检查
```
□ JSON格式正确（可通过JSON.parse验证）
□ JSON包含所有幻灯片数据
□ 每个幻灯片包含完整内容
□ 数据结构符合规范
□ 无数据遗漏
□ 无数据错误
□ 无JSON语法错误
```

#### HTML渲染功能检查
```
□ HTML能够正确加载JSON数据
□ JavaScript能够正确解析JSON
□ JavaScript能够正确渲染所有幻灯片
□ 所有内容正确显示
□ 所有图表正确显示
□ 导航功能正常
□ 响应式设计正常
```

#### 代码质量检查
```
□ HTML结构正确
□ CSS样式正确
□ JavaScript代码正确
□ JSON数据正确
□ 可访问性符合标准
□ 性能优化合理
□ 无语法错误
□ 无冗余代码
```

#### 设计规范验证（一票否决制）
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

#### 功能验证
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

**输出产物**：
- 资源使用验证报告
- 内容完整性验证报告
- JSON数据格式验证报告
- HTML渲染功能验证报告
- 代码质量验证报告
- 功能验证报告
- 最终验收报告

**验证标准**：
- [ ] 所有验证项目都通过
- [ ] 无严重问题
- [ ] 可正常运行
- [ ] JSON格式正确
- [ ] HTML渲染正常
- [ ] 符合McKinsey标准
- [ ] **设计规范全部符合**（颜色、字体、布局、风格）
- [ ] **未使用非McKinsey风格元素**（紫色渐变、圆角卡片、通用模板等）

---

## 🚀 执行流程

### 自动化执行流程

本命令会自动调用以下4个skill，按顺序执行：

```
开始
  ↓
步骤1：beauty-step1
  ├─ 读取源文档
  ├─ 分析内容结构
  ├─ 提取数据点
  └─ 生成内容大纲
  ↓
步骤2：beauty-step2
  ├─ 读取图表选择指南
  ├─ 规划幻灯片页面
  ├─ 拆分内容到页面
  └─ 验证内容完整性
  ↓
步骤3：beauty-normal-step3
  ├─ 读取设计规范和模板
  ├─ 设计JSON数据结构
  ├─ 生成HTML框架和CSS
  ├─ 生成JSON数据
  ├─ 生成JavaScript渲染逻辑
  └─ 验证代码质量
  ↓
步骤4：beauty-normal-step4
  ├─ 验证资源使用
  ├─ 检查内容完整性
  ├─ 检查JSON数据格式
  ├─ 检查HTML渲染功能
  ├─ 检查代码质量
  ├─ 验证设计规范
  └─ 生成验收报告
  ↓
完成！输出HTML文件和验收报告
```

### 执行保证

- ✅ **自动执行**：所有步骤自动调用，无需手动干预
- ✅ **质量保证**：每步都有验证标准，确保质量
- ✅ **错误恢复**：发现问题自动回退到对应步骤
- ✅ **完整保留**：100%保留原文所有内容
- ✅ **设计标准**：严格遵循McKinsey设计规范
- ✅ **JSON驱动**：使用JSON数据驱动HTML渲染

---

## ⚠️ 回退机制

### 回退触发条件

以下任一情况发生，必须回退到对应步骤重新执行：

#### 回退到步骤1
```
□ 文档分析不完整
□ 章节结构识别错误
□ 数据点遗漏
□ 结论遗漏
```

#### 回退到步骤2
```
□ 资源未读取（chart-selection-guide.md等）
□ 图表选择错误
□ 内容被压缩或省略
□ 分页不合理
□ 页面遗漏
```

#### 回退到步骤3
```
□ 资源未读取（best-practices.md等）
□ JSON数据结构错误
□ JSON格式错误
□ JSON数据不完整
□ HTML结构错误
□ CSS样式错误
□ JavaScript代码错误
□ JavaScript无法解析JSON
□ JavaScript无法正确渲染HTML
□ 图表配置错误
□ 响应式设计问题
□ **颜色规范不符合**（使用紫色渐变、AI生成色板、非McKinsey颜色）
□ **字体规范不符合**（使用Inter、Roboto、Arial等通用字体）
□ **布局规范不符合**（使用圆角卡片、通用模板布局）
□ **设计风格不符合**（装饰性图标、不必要动画、过度阴影等）
```

### 回退执行流程

```
发现问题
  ↓
确定回退目标步骤
  ↓
记录问题详情
  ↓
输出回退建议
  ↓
等待用户确认
  ↓
返回对应步骤重新执行
  ↓
重新验证
  ↓
通过后继续
```

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
   - 资源使用验证报告
   - 内容完整性验证报告
   - JSON数据格式验证报告
   - HTML渲染功能验证报告
   - 代码质量验证报告
   - 功能验证报告
   - 最终验收报告

### 质量标准

- **内容完整性**：A+（100%保留）
- **JSON数据质量**：A+（格式正确，结构完整）
- **HTML渲染质量**：A+（正确渲染JSON数据）
- **代码质量**：A+（符合最佳实践）
- **设计质量**：A+（完全符合McKinsey标准）
- **功能完整性**：A+（所有功能正常）
- **总体评分**：A+（优秀）

---

## 💡 使用建议

### 最佳实践

**1. 文档准备**
- 使用结构化的文档格式（Markdown、HTML、JSON优先）
- 确保文档包含清晰的章节层次
- 提供完整的数据和结论
- 避免使用过于复杂的嵌套结构

**2. 首次使用**
- 建议先用小文档（<10页）测试
- 熟悉4步执行流程
- 了解验证标准和回退机制
- 确认输出符合预期

**3. Token管理**
- 遇到token限制时，耐心等待"继续"提示
- 不要中断执行，等待完整完成
- 大文档会自动分批处理
- 质量优先于速度

**4. 质量检查**
- 步骤4是关键验收步骤，务必认真执行
- 所有验证项目都必须通过
- 发现问题立即回退修复
- 不要忽略任何警告

**5. 浏览器测试**
- 生成后在不同浏览器中测试效果
- 推荐浏览器：Chrome、Firefox、Safari、Edge
- 测试响应式设计（桌面、平板、手机）
- 验证图表显示和交互
- 验证JSON数据加载和渲染

**6. JSON数据维护**
- JSON数据嵌入在HTML中，易于查看和修改
- 修改JSON数据后刷新页面即可看到效果
- 可以导出JSON数据用于其他用途
- JSON数据结构清晰，易于理解

### 常见问题

**Q1：执行时间过长怎么办？**
A：这是正常的，特别是对于大文档。系统会自动分批处理，请耐心等待"继续"提示。

**Q2：如何确保设计符合McKinsey标准？**
A：系统会自动验证设计规范，包括颜色、字体、布局。如果不符合，会自动回退到步骤3重新生成。

**Q3：可以跳过某些步骤吗？**
A：不可以。所有4个步骤都必须执行，每个步骤都有其重要性。跳过步骤会导致质量下降。

**Q4：如何处理项目特定的需求？**
A：在项目根目录下创建 `.ppt_assets/INDEX.md` 文件，定义项目特定的布局、图表和样式。系统会优先使用项目资源。

**Q5：生成的HTML文件可以修改吗？**
A：可以。生成的HTML文件是标准的HTML5格式，可以直接用任何文本编辑器修改。JSON数据嵌入在HTML中，修改JSON数据后刷新页面即可看到效果。但建议在修改后重新运行步骤4验证。

**Q6：JSON+HTML模式和普通HTML模式有什么区别？**
A：JSON+HTML模式将所有幻灯片内容存储为JSON数据，然后通过JavaScript动态渲染HTML。这种方式的优势是：
- 数据与展示分离，易于维护
- 可以轻松导出JSON数据用于其他用途
- 修改内容只需修改JSON数据
- 更灵活的内容管理

**Q7：如何导出JSON数据？**
A：JSON数据嵌入在HTML的`<script>`标签中，可以直接复制出来保存为.json文件。

---

## 🎯 成功标准

### 执行成功标志

当以下所有条件都满足时，命令执行成功：

**流程完成度**：
- ✅ 所有4个步骤都已执行完成
- ✅ 每个步骤的验证标准都通过
- ✅ 无步骤被跳过或中断

**资源使用验证**：
- ✅ 步骤2：已读取3个必读资源（chart-selection-guide.md、CHART_EXAMPLES_INDEX.md、INSIGHT_VISUALIZATION_GUIDE.md）
- ✅ 步骤3：已读取4个必读资源（best-practices.md、mckinsey-design-system.md、presentation-template.html、TEMPLATE_USAGE_GUIDE.md）
- ✅ 步骤3：已读取布局和图表示例索引（INDEX.md）
- ✅ 步骤3：已检查并读取项目特定资源（.ppt_assets/INDEX.md，如果存在）

**内容完整性验证**：
- ✅ 所有原文章节都已包含（100%保留）
- ✅ 所有要点都已包含（无压缩、无省略）
- ✅ 所有数据都已包含（数值、百分比、货币等）
- ✅ 所有表格都已包含（完整的行列数据）
- ✅ 所有结论都已包含（完整文字）
- ✅ 无内容被篡改或简化

**JSON数据验证**：
- ✅ JSON格式正确（可通过JSON.parse验证）
- ✅ JSON包含所有幻灯片数据
- ✅ 每个幻灯片包含完整内容
- ✅ 数据结构符合规范
- ✅ 无数据遗漏
- ✅ 无数据错误
- ✅ 无JSON语法错误

**HTML渲染验证**：
- ✅ HTML能够正确加载JSON数据
- ✅ JavaScript能够正确解析JSON
- ✅ JavaScript能够正确渲染所有幻灯片
- ✅ 所有内容正确显示
- ✅ 所有图表正确显示
- ✅ 导航功能正常
- ✅ 响应式设计正常

**代码质量验证**：
- ✅ HTML结构完整且正确
- ✅ CSS样式完整且符合规范
- ✅ JavaScript代码完整且无错误
- ✅ JSON数据完整且正确
- ✅ 所有图表都已正确配置
- ✅ 响应式设计完备
- ✅ 无语法错误

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

**输出**：McKinsey风格HTML演示文稿（JSON+HTML模式） + 验收报告
