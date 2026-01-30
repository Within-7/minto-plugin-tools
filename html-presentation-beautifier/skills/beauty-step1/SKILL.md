---
name: "beauty-step1"
description: "Document content analysis and merging. Automatically invoked during step 1 of the beauty command to fully understand source document content, extract key information, and establish content structure. 文档内容分析合并。在beauty命令的步骤1执行时自动调用，用于完整理解源文档内容，提取关键信息，建立内容结构。"
---

# Beauty 步骤1：文档内容分析合并 / Beauty Step 1: Document Content Analysis

## 目标 / Goal

完整理解源文档内容，提取关键信息，建立内容结构。

Fully understand source document content, extract key information, and establish content structure.

## ⚠️ Token限制处理机制 / Token Limit Handling Mechanism

**如果文档过长无法一次性读取完整 / If document too long to read at once:**

```
正确做法（使用继续机制）/ Correct Approach (Use Continue Mechanism):

步骤1.1：读取文档前半部分 / Step 1.1: Read first half of document
├─ 使用 Read 工具读取文档（offset: 0, limit: 500）
   Use Read tool to read document (offset: 0, limit: 500)
├─ 提取前半部分的章节结构
   Extract chapter structure from first half
├─ 记录前半部分的数据点
   Record data points from first half
└─ 输出："步骤1.1完成 - 已分析文档前半部分（0-500行）
       请输入'继续'以分析后半部分"
   Output: "Step 1.1 complete - Analyzed first half of document (lines 0-500)
           Please input 'continue' to analyze the second half"

【等待用户输入"继续" / Wait for user to input "continue"】

步骤1.2：读取文档后半部分 / Step 1.2: Read second half of document
├─ 使用 Read 工具读取文档（offset: 500, limit: 500）
   Use Read tool to read document (offset: 500, limit: 500)
├─ 提取后半部分的章节结构
   Extract chapter structure from second half
├─ 记录后半部分的数据点
   Record data points from second half
└─ 输出："步骤1.2完成 - 已分析文档后半部分（500-1000行）
       文档分析100%完成"
   Output: "Step 1.2 complete - Analyzed second half of document (lines 500-1000)
           Document analysis 100% complete"

【如果文档超过1000行，继续分片读取 / If document exceeds 1000 lines, continue segmented reading】

步骤1.3：合并分析结果 / Step 1.3: Merge analysis results
├─ 整合所有部分的分析结果
   Integrate analysis results from all parts
├─ 生成完整的章节结构清单
   Generate complete chapter structure list
├─ 生成完整的数据点清单
   Generate complete data point list
└─ 进入步骤2
   Proceed to Step 2
```

**❌ 禁止做法（偷工减料）/ Prohibited Actions (Cutting Corners):**
```
错误做法1：只读前几行 / Wrong Approach 1: Only read first few lines
├─ Read 文件（limit: 50）
   Read file (limit: 50)
└─ ❌ 跳过了后面的内容
   ❌ Skipped remaining content

错误做法2：使用摘要 / Wrong Approach 2: Use summaries
├─ 请用户总结文档内容
   Ask user to summarize document content
└─ ❌ 可能丢失细节
   ❌ May lose details

错误做法3：分步执行但不说明 / Wrong Approach 3: Execute in steps without explanation
├─ 只生成前半部分内容
   Only generate first half of content
└─ ❌ 用户不知道要继续
   ❌ User doesn't know to continue
```

## 执行要求 / Execution Requirements

- ✅ 完整阅读源文档，不做任何修改或删减
  Fully read source document without any modification or deletion
  
- ✅ 识别文档类型（报告、分析、方案、研究等）
  Identify document type (report, analysis, plan, research, etc.)
  
- ✅ 提取核心内容元素 / Extract core content elements:
  - 标题层次结构（H1 → H2 → H3）
    Title hierarchy (H1 → H2 → H3)
  - 关键数据和数值
    Key data and numerical values
  - 主要结论和见解
    Main conclusions and insights
  - 重要建议和行动项
    Important recommendations and action items
  - 对比关系和表格数据
    Comparison relationships and table data
    
- ✅ 建立内容逻辑结构 / Establish content logical structure:
  - 主题分组
    Topic grouping
  - 因果关系
    Causal relationships
  - 时间顺序
    Chronological order
  - 优先级排序
    Priority ranking
    
- ✅ 记录所有定量数据（数字、百分比、货币等）
  Record all quantitative data (numbers, percentages, currency, etc.)

## 输出产物 / Output Artifacts

- 内容结构大纲（包含所有章节和要点）
  Content structure outline (includes all chapters and key points)
  
- 数据点清单（所有可用于可视化的数值）
  Data point list (all values available for visualization)
  
- 关键结论列表（必须完整保留）
  Key conclusions list (must be fully preserved)

## 验证标准 / Validation Criteria

- [ ] 所有原文内容已提取 / All original content extracted
- [ ] 无内容丢失或遗漏 / No content loss or omission
- [ ] 数据点完整记录 / Data points fully recorded
- [ ] 逻辑结构清晰 / Logical structure clear

## 完成后输出 / Output Upon Completion

```
✅ 步骤1：文档内容分析合并 - 100%完成
✅ Step 1: Document Content Analysis - 100% Complete

分析摘要 / Analysis Summary:
- 文档类型 / Document type: [报告/分析/方案/研究 / Report/Analysis/Plan/Research]
- 章节数量 / Chapter count: [N个H2章节 / N H2 chapters]
- 数据点数量 / Data point count: [N个 / N points]
- 关键结论 / Key conclusions: [N个 / N conclusions]

输出产物 / Output Artifacts:
✓ 内容结构大纲 / Content structure outline
✓ 数据点清单 / Data point list
✓ 关键结论列表 / Key conclusions list

验证结果 / Validation Results:
✓ 内容完整性：100% / Content integrity: 100%
✓ 数据准确性：已验证 / Data accuracy: Verified
✓ 结构清晰度：优秀 / Structure clarity: Excellent

准备进入步骤2 / Ready to proceed to Step 2
```
