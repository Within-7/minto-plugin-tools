---
description: "Transform documents into professional McKinsey-style HTML presentations. Strictly follow 4-step workflow: Document Analysis → Slide Design → HTML Generation → Code Review. Ensures 100% content preservation and McKinsey design standards. 将文档转化为专业 McKinsey 风格 HTML 演示文稿。严格遵循4步流程：文档分析 → 幻灯片设计 → HTML生成 → 代码审核，确保100%内容保留和McKinsey设计标准。"
args:
  - name: document
    description: "Document path to convert (supports .md, .txt, .json, .html) / 要转换的文档路径（支持 .md, .txt, .json, .html）"
    required: true
---

# Beauty 命令 / Beauty Command

将文档、数据、结论等信息转化为通俗连贯、明确清晰的 McKinsey 风格 HTML 演示文稿。

Transform documents, data, and conclusions into clear and coherent McKinsey-style HTML presentations.

## ⚠️ 核心原则 / Core Principles

**CRITICAL: Must strictly follow this 4-step workflow. No steps can be skipped!**
**关键：必须严格遵循以下4步固定流程，不得跳过任何步骤！**

### Step Workflow Enforcement / 步骤流程强制执行

**🔑 Steps 2 & 3: Mandatory Resource Reading / 步骤2、3必须读取skill资源**

**Step 2 (Chart Selection / 图文选择)** - MUST read:
- `beauty-html/references/chart-selection-guide.md`
- `beauty-html/assets/COMPONENTS_INDEX.md`
- `beauty-html/assets/LAYOUTS_INDEX.md`
- `beauty-html/assets/INDEX.md`

**Step 3 (HTML Generation / HTML生成)** - MUST read:
- `beauty-html/references/best-practices.md`
- `beauty-html/references/mckinsey-design-system.md`
- `beauty-html/assets/presentation-template.html`
- `beauty-html/assets/TEMPLATE_USAGE_GUIDE.md`
- `beauty-html/assets/COMPONENTS_INDEX.md`
- `beauty-html/assets/LAYOUTS_INDEX.md`
- `beauty-html/assets/INDEX.md`

**🔑 Step 4: Critical Validation - One-Vote Veto System / 第4步：关键验收 - 一票否决制**

**Content Integrity Check / 内容完整性检验**:
- ✅ MUST preserve 100% of original content (chapters, data, conclusions)
- ✅ 必须100%保留原文所有章节、数据、结论，零遗漏

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

### ⚠️ 执行强制机制 / Execution Enforcement Mechanism

**CRITICAL: This is a MANDATORY 4-step workflow. Step 4 MUST be executed after Step 3, no exceptions!**
**关键：这是强制性的4步流程。步骤4必须在步骤3之后执行，不得跳过！**

**Before starting ANY step, Claude Code MUST:**
**在开始任何步骤之前，Claude Code 必须：**

1. **Verify prerequisite completion / 验证前置条件完成**
   - Check if previous step output exists / 检查上一步输出是否存在
   - Validate previous step output quality / 验证上一步输出质量
   
2. **Invoke the correct skill / 调用正确的skill**
   - Step 1 → `beauty-step1` skill
   - Step 2 → `beauty-step2` skill  
   - Step 3 → `beauty-step3` skill
   - Step 4 → `beauty-step4` skill

3. **Cannot proceed to next step until / 不能跳到下一步，除非:**
   - Current step fully completed / 当前步骤完全完成
   - All verification checks passed / 所有验证检查通过
   - Output artifacts generated / 输出产物已生成
   - **For Step 3: Automatically invoke Step 4 after completion / 步骤3：完成后必须自动调用步骤4**
   - **For Step 4: MUST generate final verification report / 步骤4：必须生成最终验证报告**

### 📊 执行状态跟踪 / Execution State Tracking

**必须记录每个步骤的执行状态：**

```
执行状态记录 / Execution State Tracking:

步骤 1：文档内容分析合并
├─ 执行状态：[待执行/执行中/已完成/失败]
├─ 开始时间：[时间戳]
├─ 结束时间：[时间戳]
├─ 验证结果：[通过/失败]
└─ 输出产物：[产物列表]

步骤 2：幻灯片内容转换与拆分
├─ 执行状态：[待执行/执行中/已完成/失败]
├─ 前置依赖：步骤1完成
├─ 幻灯片页数：[N页]
└─ 输出产物：[产物列表]

步骤 3：HTML样式布局代码规划与生成
├─ 执行状态：[待执行/执行中/已完成/失败]
├─ 前置依赖：步骤2完成
├─ HTML文件路径：[路径]
├─ 代码行数：[行数]
└─ 输出产物：[产物列表]

步骤 4：代码内容审核检验
├─ 执行状态：[待执行/执行中/已完成/失败]
├─ 前置依赖：步骤3完成
├─ 资源使用验证：[通过/失败]
├─ 内容完整性检查：[通过/失败]
├─ 代码质量检查：[通过/失败]
├─ 功能验证：[通过/失败]
├─ 总体验收：[通过/失败]
└─ 输出产物：[产物列表]
```

### ⚠️ 错误恢复机制 / Error Recovery Mechanism

**如果任何步骤失败，必须：**
```
1. 记录错误详情
2. 确定回退目标步骤
3. 输出回退建议
4. 等待用户确认
5. 返回对应步骤重新执行
6. 重新验证
7. 通过后继续下一步
```

### 🔄 自动步骤链 / Automatic Step Chaining

**步骤3完成后，必须自动执行步骤4：**
```
步骤3输出："✅ 步骤3完成 - HTML文件已生成
            文件路径：/path/to/file.html
            准备进入步骤4：代码内容审核检验"

步骤4输入："继续"（系统自动）
步骤4执行：自动调用 beauty-step4 skill
步骤4输出：完整验证报告
```

**⚠️ 禁止行为 / Prohibited Actions:**
- ❌ 步骤3完成后不执行步骤4
- ❌ 跳过任何验证检查
- ❌ 将就通过有问题的结果
- ❌ 不记录执行状态

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

### 步骤 2️⃣: Slide Content Conversion / 幻灯片内容转换与拆分

**Goal / 目标**: Convert document content completely into structured slide pages, ensuring zero omissions, clear logic, appropriate pagination.
将文档内容完整转换为结构化的幻灯片页面，确保内容零遗漏、逻辑清晰、页面适量。

**Execution Method / 执行方式**: Invoke `beauty-step2` skill / 调用 `beauty-step2` skill

**⚠️ Core Principles / 核心原则**:
- ✅ Preserve 100% of original content, zero omissions, zero compression, zero simplification
  100%保留原文所有内容，零遗漏、零压缩、零简化
  
- ✅ Each page content ≤ 8 key points, split if exceeds
  每页内容不超过8个要点，超过则分页展示
  
- ✅ When content too much, use "continue" mechanism for batch processing
  遇到内容过多时，使用"继续"机制分批处理
  
- ❌ ABSOLUTELY PROHIBITED to compress, omit, or simplify content to save tokens
  绝对禁止为了省token而压缩、省略、简化内容
  
- **🔑 CORE RULE**: If data too large or tokens too long, automatically use 'continue' for segmented loading, NEVER simplify or cut corners to save tokens, STRICTLY PROHIBITED to skip content or use summaries to save tokens
  **🔑 最核心规则**：如果数据内容过大，或者token过长，则自动使用'继续'进行'分段'加载数据，绝对不能精简、偷工减料的节省token，严禁为了省token而跳过内容或使用摘要

**🔑 Mandatory Resources / 必读资源**:
- `beauty-html/references/chart-selection-guide.md`
- `beauty-html/assets/COMPONENTS_INDEX.md`
- `beauty-html/assets/LAYOUTS_INDEX.md`
- `beauty-html/assets/INDEX.md`

**Execution Workflow / 执行流程** (automatically executed by skill / 由skill自动执行):
```
Step 2.1: Identify document structure hierarchy / 识别文档结构层次
  ↓
Step 2.2: Plan slide page types / 规划幻灯片页面类型
  ↓
Step 2.3: Split content to specific pages / 拆分内容到具体页面
  ↓
Step 2.4: Verify content integrity / 验证内容完整性
```

**Output Artifacts / 输出产物**:
- Complete slide page list (from page 1 to page N)
  完整的幻灯片页面清单（从第1页到第N页）
  
- Detailed content for each page (100% original text, no compression)
  每页的详细内容（100%原文，无压缩）
  
- Data points, charts, tables for each page (if any)
  每页的数据点、图表、表格（如有）
  
- Confirmation of total page count
  页面总数确认

**Validation Criteria / 验证标准**:
- [ ] All pages listed in detail / 所有页面已详细列出
- [ ] Each page content complete (100% original) / 每页内容完整（100%原文）
- [ ] Each page key points ≤ 8 / 每页要点数≤8个
- [ ] Data, charts, tables complete / 数据、图表、表格完整
- [ ] Page numbers consecutive / 页面编号连续
- [ ] No content omissions / 无内容遗漏

---

### 步骤 3️⃣：HTML样式布局代码规划与生成

**目标**：将步骤2生成的幻灯片页面清单转换为完整的、可运行的McKinsey风格HTML文件。

**执行方式**：调用 `beauty-step3` skill

**⚠️ 核心原则**：
- ✅ 必须读取并参考skill资源
- ✅ **强制使用** `best-practices.md` 和 `mckinsey-design-system.md` 中的所有设计规范
- ✅ **颜色规范强制执行**：必须使用McKinsey标准色板，禁止使用紫色渐变、AI生成色板
- ✅ **字体规范强制执行**：必须使用系统字体，禁止使用Inter、Roboto、Arial等通用字体
- ✅ **布局规范强制执行**：必须遵循McKinsey布局标准，禁止使用圆角卡片、通用模板
- ✅ 每个阶段的代码必须是完整的语法单元
- ✅ CSS必须在阶段1一次性完整生成
- ✅ 每个幻灯片的HTML必须完整
- ✅ JavaScript必须在阶段4完整生成
- ✅ 每个阶段结束后提示用户输入"继续"
- ❌ 禁止跨阶段截断HTML标签
- ❌ 禁止省略CSS样式
- ❌ 禁止简化图表代码
- ❌ **禁止使用非McKinsey风格的设计元素**（紫色渐变、圆角卡片、通用模板等）
- **🔑 最核心规则：如果数据内容过大，或者token过长，则自动使用'继续'进行'分段'加载数据，绝对不能精简、偷工减料的节省token,严禁为了省token而跳过内容或使用摘要**

**🔑 完成后自动执行步骤4 / Auto-execute Step 4 after completion:**
```
步骤3完成时，必须输出：
✅ 步骤3：HTML样式布局代码规划与生成 - 100%完成
✓ HTML文件路径：[文件路径]
✓ 代码行数：[行数]
✓ 图表数量：[N个]
✓ 资源读取：7个必读资源100%完成
✓ 验证结果：6项验证100%通过

🔄 准备进入步骤4：代码内容审核检验
请输入"继续"以执行步骤4...
```

**⚠️ 禁止行为（强制执行）**：
- ❌ 步骤3完成后不准备步骤4
- ❌ 不生成HTML文件
- ❌ 不记录文件路径和行数
- ❌ 不输出验证结果摘要

**🔑 必读资源（强制执行）**：
- `beauty-html/references/best-practices.md` - **必须严格遵循所有最佳实践**
- `beauty-html/references/mckinsey-design-system.md` - **必须严格遵循所有设计规范**
- `beauty-html/assets/presentation-template.html` - 参考模板结构
- `beauty-html/assets/TEMPLATE_USAGE_GUIDE.md` - 模板使用指南
- `beauty-html/assets/COMPONENTS_INDEX.md` - 组件索引和选择指南
- `beauty-html/assets/LAYOUTS_INDEX.md` - 布局索引和选择指南
- `beauty-html/assets/INDEX.md` - 资源总索引

**🔑 设计系统强制规范（新增）**：
- **头部导航栏规范**：
  - 背景色：黑色 (#000000)
  - 文字色：白色 (#FFFFFF)
  - 高度：60px
  - 定位：position: fixed, z-index: 100
  - 封面页隐藏：`.cover-slide .slide-header { display: none; }`

- **图表使用规范**：
  - 图表页面必须使用2列或3列布局，禁止单列布局
  - 图表+洞察布局：图表左侧55% + 洞察右侧45%（推荐）
  - 多图表对比布局：每列33%，并排对比
  - 图表颜色必须使用设计系统配色：#556EE6（深蓝）、#F85d42（橙）、#34c38f（绿）、#50a5f1（蓝）、#f1b44c（黄）

**🔑 新增设计规范强制执行**：

- **背景颜色规范**：
  - 主背景色：白色 (#FFFFFF)
  - 标题栏背景：黑色 (#000000)
  - 主要强调色：橙色 (#F85d42)
  - 辅助色：灰色 (#74788d)
  - 辅助色系：
    - 深蓝色 (#556EE6)
    - 绿色 (#34c38f)
    - 蓝色 (#50a5f1)
    - 黄色 (#f1b44c)
  - 封面页使用纯色背景（从以下颜色随机选取：#556EE6、#F85d42、#34c38f、#50a5f1、#f1b44c、#000000），白色文字
  - 章节首页使用纯色背景（从以下颜色随机选取：#556EE6、#F85d42、#34c38f、#50a5f1、#f1b44c、#000000），白色文字
  - 结束页使用纯色背景（从以下颜色随机选取：#556EE6、#F85d42、#34c38f、#50a5f1、#f1b44c、#000000），白色文字
  - 图表颜色必须使用设计系统配色：#556EE6（深蓝）、#F85d42（橙）、#34c38f（绿）、#50a5f1（蓝）、#f1b44c（黄）
  - 强调色块使用橙色 (#F85d42)
  - 辅助文字使用灰色 (#74788d)

- **章节概览规范**：
  - 每个章节首页必须包含章节概览列表
  - 章节概览必须列出当前章节的所有子标题
  - 章节概览必须包含每个子标题对应的页码
  - 章节概览必须使用2列网格布局
  - 章节概览样式必须与整体设计保持一致

- **动态导航规范**：
  - 内容页头部导航栏标题必须随页面切换实时更新
  - 每个幻灯片必须有唯一的data-title属性
  - 封面页导航栏必须隐藏
  - 章节首页导航栏必须隐藏
  - 动态导航功能必须使用JavaScript实现

- **图文列表规范**：
  - 所有文字内容列表必须使用图文格式，禁止使用传统HTML list格式（<ul><li>）
  - 图文列表必须使用卡片或媒体对象样式
  - 列表项必须包含图标/数字+标题+描述的完整结构
  - 图文列表布局必须合理（2列或垂直列表）
  - 图文列表样式必须与整体设计保持一致

**执行流程**（由skill自动执行）：
```
步骤3.1：读取必读资源
  ↓
步骤3.2：为每页规划代码方案
  ↓
步骤3.3：生成完整HTML文件（3个阶段）
  ├─ 阶段1：生成HTML框架和完整CSS样式
  ├─ 阶段2：按章节逐个生成幻灯片（封面页、目录页、章节首页、内容页、结束页）
  └─ 阶段3：生成JavaScript代码和结束标签
  ↓
步骤3.4：验证代码质量
```

**输出产物**：
- 完整的HTML文件（约1200行）
- CSS样式（约800行）
- JavaScript代码（约100行）
- 图表配置（根据实际需求）

**验证标准**：

**代码完整性**：
- [ ] HTML结构完整
- [ ] CSS样式完整
- [ ] JavaScript功能完整
- [ ] 所有图表已配置
- [ ] 响应式设计完备
- [ ] 无语法错误

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
- [ ] **图表页面使用2列或3列布局**（禁止单列）
- [ ] **图表+洞察布局正确**（图表左侧55% + 洞察右侧45%）
- [ ] **多图表对比布局正确**（每列33%）

**导航栏规范检查** ⭐ 新增：
- [ ] 头部导航栏存在：`.slide-header`
- [ ] 导航栏背景色：黑色 (#000000)
- [ ] 导航栏文字色：白色 (#FFFFFF)
- [ ] 导航栏高度：60px
- [ ] 导航栏固定定位：position: fixed
- [ ] 导航栏z-index：100
- [ ] 封面页导航栏隐藏：`.cover-slide .slide-header { display: none; }`

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
**CRITICAL: This is the MOST CRITICAL step! MUST be strictly executed!**

**目标**：全面检查生成的 HTML 演示文稿，确保质量和完整性。

**执行方式**：调用 `beauty-step4` skill

**⚠️ 核心原则**：实行一票否决制
- **内容完整性检验**：必须100%保留原文所有章节、数据、结论，零遗漏
- **代码质量检验**：必须符合HTML最佳实践，可访问可运行
- **资源使用检验**：必须验证步骤2和步骤3是否正确读取并使用了skill资源
- **发现问题立即回退**：返回对应步骤重新执行，绝不将就

**🔑 强制验证项目（必须全部通过）：**
```
资源使用验证：
□ 步骤2资源：已读取 chart-selection-guide.md、CHART_EXAMPLES_INDEX.md、INSIGHT_VISUALIZATION_GUIDE.md
□ 步骤3资源：已读取 best-practices.md、mckinsey-design-system.md、presentation-template.html
□ 所有资源都已正确使用

内容完整性验证：
□ 所有章节都已包含
□ 所有要点都已包含
□ 所有数据都已包含
□ 无内容被压缩或省略

代码质量验证：
□ HTML结构正确
□ CSS样式正确
□ JavaScript代码正确
□ 无语法错误

设计规范验证：
□ 使用McKinsey标准色板
□ 未使用紫色渐变
□ 未使用圆角卡片
□ 图表使用2列或3列布局
```

**🔑 完成后必须生成完整报告：**
```
✅ 步骤4：代码内容审核检验 - 100%完成

验证摘要：
- 资源使用验证：✅ 通过（X/Y项）
- 内容完整性检查：✅ 通过（X/Y项）
- 代码质量检查：✅ 通过（X/Y项）
- 功能验证：✅ 通过（X/Y项）

总体验收：✅ 通过（X/Y项）

质量评分：A+（优秀/良好/合格/不合格）

输出产物：
1. 验证报告
2. 问题清单（如有）
3. 修正建议（如有）

🎉 全部4步流程执行完成！
HTML演示文稿已生成，可直接使用。
```

**⚠️ 禁止行为（强制执行）**：
- ❌ 跳过步骤4不执行
- ❌ 验证走过场
- ❌ 将就通过有问题的结果
- ❌ 不生成完整验证报告

**执行流程**（由skill自动执行）：
```
步骤4.1：资源使用验证
  ↓
步骤4.2：内容完整性检查
  ↓
步骤4.3：代码质量检查
  ↓
步骤4.4：功能验证
  ↓
步骤4.5：生成最终报告
```

**验证项目**：

#### 资源使用验证
```
步骤2资源：
□ 已读取：references/chart-selection-guide.md
□ 已读取：assets/COMPONENTS_INDEX.md
□ 已读取：assets/LAYOUTS_INDEX.md
□ 已读取：assets/INDEX.md

步骤3资源：
□ 已读取：references/best-practices.md
□ 已读取：references/mckinsey-design-system.md
□ 已读取：assets/presentation-template.html
□ 已读取：assets/TEMPLATE_USAGE_GUIDE.md
□ 已读取：assets/COMPONENTS_INDEX.md
□ 已读取：assets/LAYOUTS_INDEX.md
□ 已读取：assets/INDEX.md
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

#### 代码质量检查
```
□ HTML结构正确
□ CSS样式正确
□ JavaScript代码正确
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
□ **图表页面使用2列或3列布局**（禁止单列）
□ **图表+洞察布局正确**（图表左侧55% + 洞察右侧45%）
□ **多图表对比布局正确**（每列33%）

**导航栏规范验证** ⭐ 新增：
□ 头部导航栏存在：`.slide-header`
□ 导航栏背景色：黑色 (#000000)
□ 导航栏文字色：白色 (#FFFFFF)
□ 导航栏高度：60px
□ 导航栏固定定位：position: fixed
□ 导航栏z-index：100
□ 封面页导航栏隐藏：`.cover-slide .slide-header { display: none; }`

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
□ 图表显示正常
□ 响应式设计正常
□ 浏览器兼容性良好
□ 无功能性问题
```

**输出产物**：
- 资源使用验证报告
- 内容完整性验证报告
- 代码质量验证报告
- 功能验证报告
- 最终验收报告

**验证标准**：
- [ ] 所有验证项目都通过
- [ ] 无严重问题
- [ ] 可正常运行
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
步骤3：beauty-step3
  ├─ 读取设计规范和模板
  ├─ 规划代码方案
  ├─ 生成HTML、CSS、JavaScript
  └─ 验证代码质量
  ↓
步骤4：beauty-step4
  ├─ 验证资源使用
  ├─ 检查内容完整性
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
□ HTML结构错误
□ CSS样式错误
□ JavaScript代码错误
□ 图表配置错误
□ 响应式设计问题
□ **颜色规范不符合**（使用紫色渐变、AI生成色板、非McKinsey颜色）
□ **字体规范不符合**（使用Inter、Roboto、Arial等通用字体）
□ **布局规范不符合**（使用圆角卡片、通用模板布局）
□ **设计风格不符合**（装饰性图标、不必要动画、过度阴影等）
□ **导航栏规范不符合**（背景色非黑色、文字色非白色、高度非60px、未固定定位等）
□ **图表布局不符合**（使用单列布局、未使用2列/3列布局）
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
   - 文件名：`[文档标题]_McKinsey风格演示文稿.html`
   - 文件大小：约60KB
   - 总代码行数：约1200行
   - 加载时间：<1秒（本地）
   - 依赖项：Chart.js CDN（唯一外部依赖）

2. **验收报告**
   - 资源使用验证报告
   - 内容完整性验证报告
   - 代码质量验证报告
   - 功能验证报告
   - 最终验收报告

### 质量标准

- **内容完整性**：A+（100%保留）
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
A：可以。生成的HTML文件是标准的HTML5格式，可以直接用任何文本编辑器修改。但建议在修改后重新运行步骤4验证。

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

**代码质量验证**：
- ✅ HTML结构完整且正确
- ✅ CSS样式完整且符合规范
- ✅ JavaScript代码完整且无错误
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
- ✅ 所有功能都正常工作
- ✅ 图表显示正常
- ✅ 导航功能正常
- ✅ 响应式设计正常

**验收报告**：
- ✅ 验收报告全部通过
- ✅ 无严重问题
- ✅ 无设计规范违规

### 输出文件

成功执行后会生成以下文件：

**1. HTML演示文稿文件**
```
文件名：[文档标题]_McKinsey风格演示文稿.html
文件大小：约60KB
代码行数：约1200行
格式：HTML5
依赖项：Chart.js CDN（https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js）
```

**2. 验收报告**
```
包含以下内容：
- 资源使用验证报告
- 内容完整性验证报告
- 代码质量验证报告
- 设计规范验证报告
- 功能验证报告
- 最终验收报告
- 质量评分（A+为最高）
```

### 执行失败情况

如果出现以下情况，命令执行失败：

**步骤1失败**：
- ❌ 无法读取源文档
- ❌ 文档格式不支持
- ❌ 文档内容为空

**步骤2失败**：
- ❌ 无法读取必读资源
- ❌ 内容被压缩或省略
- ❌ 页面规划不合理

**步骤3失败**：
- ❌ 无法读取必读资源
- ❌ HTML生成不完整
- ❌ 设计规范不符合（使用非McKinsey风格）
- ❌ 代码存在严重错误

**步骤4失败**：
- ❌ 验证不通过
- ❌ 存在设计规范违规
- ❌ 存在内容遗漏

**失败处理**：
- 自动回退到失败的步骤
- 提供详细的失败原因
- 给出修复建议
- 等待用户确认后重新执行

---

## 📝 注意事项

1. **不要跳过任何步骤**：每个步骤都有其重要性，必须按顺序执行
2. **不要偷工减料**：宁可多轮对话，不可降低质量
3. **不要压缩内容**：宁可分批处理，不可省略细节
4. **不要跳过资源**：所有必读资源都必须完整读取
5. **不要忽略验证**：步骤4的验收是关键，必须严格执行

---

## 🔧 故障排除

### 问题诊断流程

```
遇到问题？
  ↓
检查错误类型
  ↓
查看对应解决方案
  ↓
尝试修复
  ↓
重新执行
  ↓
问题解决？
  ├─ 是 → 完成
  └─ 否 → 联系支持
```

### 常见问题与解决方案

#### 问题1：步骤1无法读取完整文档

**症状**：
- 提示"无法读取文档"
- 提示"文档格式不支持"
- 提示"文档内容为空"

**可能原因**：
- 文档路径错误
- 文档格式不支持
- 文档权限问题
- 文档内容为空

**解决方案**：
1. 检查文档路径是否正确（使用绝对路径或相对路径）
2. 确认文档格式是否支持（.md, .txt, .json, .html）
3. 检查文档权限（确保可读）
4. 确认文档内容不为空
5. 使用"继续"机制分批读取（如果文档过长）

#### 问题2：步骤2图表选择错误

**症状**：
- 提示"图表选择错误"
- 提示"内容被压缩或省略"
- 提示"分页不合理"

**可能原因**：
- 未正确读取图表选择指南
- 页面内容过多未分页
- 图表类型与数据不匹配

**解决方案**：
1. 返回步骤2重新执行
2. 仔细阅读 `chart-selection-guide.md`
3. 根据决策树重新选择图表
4. 确保每页内容不超过8个要点
5. 验证数据点与图表类型匹配

#### 问题3：步骤3HTML生成不完整

**症状**：
- 提示"HTML生成不完整"
- 提示"资源未读取"
- 提示"设计规范不符合"

**可能原因**：
- 未正确读取必读资源
- 使用了非McKinsey风格元素
- 代码生成被token限制中断

**解决方案**：
1. 返回步骤3重新执行
2. 确保所有必读资源都已读取（best-practices.md、mckinsey-design-system.md等）
3. 检查是否使用了紫色渐变、圆角卡片等非McKinsey元素
4. 使用"继续"机制分批生成（如果代码过长）
5. 验证颜色、字体、布局符合McKinsey标准

#### 问题4：步骤4验证不通过

**症状**：
- 提示"验证不通过"
- 提示"存在设计规范违规"
- 提示"存在内容遗漏"

**可能原因**：
- 设计规范不符合
- 内容被压缩或省略
- 代码存在错误

**解决方案**：
1. 查看详细的验证报告
2. 根据报告返回对应步骤
3. 修复具体问题（颜色、字体、布局、内容等）
4. 重新执行验证
5. 确保所有验证项目都通过

#### 问题5：生成的HTML文件无法打开

**症状**：
- 浏览器无法打开HTML文件
- 显示乱码
- 图表不显示

**可能原因**：
- 文件编码问题
- Chart.js CDN无法访问
- 浏览器兼容性问题

**解决方案**：
1. 确认文件编码为UTF-8
2. 检查网络连接（Chart.js CDN需要网络）
3. 尝试不同浏览器（Chrome、Firefox、Safari、Edge）
4. 检查浏览器控制台错误（F12）
5. 确认JavaScript已启用

#### 问题6：响应式设计不正常

**症状**：
- 在手机上显示混乱
- 在平板上布局错位
- 图表在小屏幕上不显示

**可能原因**：
- 响应式断点设置不当
- CSS媒体查询缺失
- 图表容器高度固定

**解决方案**：
1. 检查CSS中的媒体查询
2. 确认图表容器使用相对高度
3. 测试不同屏幕尺寸（320px、768px、1024px、1440px）
4. 验证flex和grid布局正确
5. 确保所有元素都有max-width限制

### 获取帮助

如果以上解决方案都无法解决问题：

1. **查看详细日志**：检查每个步骤的输出日志
2. **验证资源文件**：确认所有必读资源都存在且可读
3. **检查文档格式**：确认源文档格式正确
4. **联系支持**：提供详细的错误信息和执行日志

### 日志级别

```
INFO：正常执行信息
WARN：警告信息（不影响执行）
ERROR：错误信息（需要修复）
FATAL：致命错误（执行失败）
```

---

## 📚 相关资源

### Skill文档
- `.trae/skills/beauty-step1/SKILL.md` - 步骤1：文档内容分析合并
- `.trae/skills/beauty-step2/SKILL.md` - 步骤2：幻灯片内容转换与拆分
- `.trae/skills/beauty-step3/SKILL.md` - 步骤3：HTML样式布局代码规划与生成
- `.trae/skills/beauty-step4/SKILL.md` - 步骤4：代码内容审核检验

### 参考资源
- `beauty-html/references/chart-selection-guide.md` - 图表选择指南
- `beauty-html/references/best-practices.md` - HTML最佳实践
- `beauty-html/references/mckinsey-design-system.md` - McKinsey设计系统
- `beauty-html/assets/presentation-template.html` - 演示文稿模板
- `beauty-html/assets/TEMPLATE_USAGE_GUIDE.md` - 模板使用指南
- `beauty-html/assets/CHART_EXAMPLES_INDEX.md` - 图表示例索引
- `beauty-html/assets/INSIGHT_VISUALIZATION_GUIDE.md` - 观点可视化指南
- `beauty-html/assets/INDEX.md` - 布局和图表示例索引（全局）
- `.ppt_assets/INDEX.md` - 项目特定资源索引（如果存在，优先级最高）

---

## 📝 命令最佳实践

### 执行原则

**1. 质量优先**
- 宁可多轮对话，不可降低质量
- 宁可分批处理，不可压缩内容
- 宁可触发继续，不可偷工减料

**2. 完整性保证**
- 100%保留原文所有内容
- 零遗漏、零压缩、零简化
- 所有章节、数据、结论都必须包含

**3. 标准强制执行**
- 严格遵循McKinsey设计规范
- 颜色、字体、布局必须符合标准
- 禁止使用非McKinsey风格元素

**4. 资源必须读取**
- 所有必读资源都必须完整读取
- 优先使用项目特定资源（.ppt_assets/INDEX.md）
- 确保资源使用验证通过

**5. 错误立即回退**
- 发现问题立即返回对应步骤
- 不将就，不继续执行
- 确保所有验证都通过

### 性能优化

**1. Token管理**
- 遇到token限制时使用"继续"机制
- 分批读取大文档
- 分批生成HTML代码

**2. 执行效率**
- 自动化执行4个步骤
- 无需手动干预
- 自动验证和回退

**3. 质量保证**
- 每步都有验证标准
- 实行一票否决制
- 确保输出质量

### 输出规范

**1. 文件命名**
- 使用清晰的文件名：`[文档标题]_McKinsey风格演示文稿.html`
- 避免特殊字符
- 使用UTF-8编码

**2. 文件格式**
- 标准HTML5格式
- 包含完整的DOCTYPE声明
- 正确闭合所有标签

**3. 依赖管理**
- 唯一外部依赖：Chart.js CDN
- 使用稳定版本（4.4.0）
- 提供CDN备用方案

**4. 验收报告**
- 包含所有验证项目
- 提供详细的问题描述
- 给出明确的修复建议

---

## 🎯 命令总结

### 核心价值

**Beauty命令的核心价值**：
- ✅ **自动化**：自动执行4步流程，无需手动干预
- ✅ **质量保证**：严格的验证标准和回退机制
- ✅ **标准遵循**：100%符合McKinsey设计规范
- ✅ **内容完整**：100%保留原文所有内容
- ✅ **错误恢复**：自动回退和修复机制

### 适用场景

**最适合的场景**：
- 需要将文档转换为演示文稿
- 要求专业、简洁的设计风格
- 需要数据可视化和图表
- 需要符合McKinsey/BCG标准

**不适合的场景**：
- 需要高度自定义的动画效果
- 需要复杂的交互功能
- 需要非McKinsey风格的设计

### 成功指标

**执行成功的标志**：
- 所有4个步骤都已完成
- 所有验证项目都通过
- HTML文件可以正常运行
- 符合McKinsey设计标准
- 内容100%保留

**质量评分标准**：
- A+：优秀（所有验证都通过，无任何问题）
- A：良好（所有验证都通过，有少量警告）
- B：合格（所有验证都通过，有一些问题）
- C：不合格（存在严重问题，需要修复）
- D：失败（存在致命错误，需要重新执行）

---

**Beauty命令已准备就绪！**

**使用方法**：`/beauty [文档路径]`

**示例**：`/beauty ./my-document.md`

**支持格式**：.md, .txt, .json, .html

**输出**：McKinsey风格HTML演示文稿 + 验收报告
