# HTML Presentation Review - 测试示例

## 测试场景

这个示例展示如何使用新的 `html-presentation-reviewer` agent 来检查生成的 HTML 演示文稿。

## 示例 1: 基本使用

### 输入文档 (test.md)

```markdown
# 2024年销售分析报告

## 执行摘要

- 本年度销售额增长 25%
- 新市场拓展成效显著
- 客户满意度提升至 92%

## 销售数据

- Q1: 120万
- Q2: 150万
- Q3: 180万
- Q4: 200万

## 关键结论

1. 数字化营销贡献最大
2. 电商渠道快速增长
3. 客户复购率提升

## 建议

- 加大数字化投入
- 扩大电商团队
- 优化客户体验
```

### 执行流程

```bash
# Step 1: 使用 /beauty 命令生成演示文稿
/beauty test.md

# Step 2: 系统自动执行 5 个阶段
# Phase 1: 解析文档
# Phase 2: 规划幻灯片结构
# Phase 3: 应用 McKinsey 设计
# Phase 4: 生成 HTML
# Phase 5: 自动审查 ← 新增！

# Step 3: 查看审查报告
```

### 预期审查输出

```
✓ HTML Presentation Review Report

Overall Score: 95/100 - PASS

Content Integrity:     ✓ 100/100 (PASS)
  - 源文档章节: 4, HTML 章节: 4 ✓
  - 源文档要点: 10, HTML 要点: 10 ✓
  - 数据点: 4, 全部已可视化 ✓
  - 结论: 3, 全部已展示 ✓
  - 文本准确性: 100% 保留 ✓

Code Quality:          ✓  98/100 (PASS)
  - HTML 语法: 有效 ✓
  - CSS 语法: 正确 ✓
  - JavaScript: 完整 ✓
  - 无控制台错误 ✓

McKinsey Style:        ✓  95/100 (PASS)
  - 颜色方案: 符合标准 ✓
  - 排版: 层次清晰 ✓
  - 布局: 统一一致 ✓
  - 留白: 适当 ✓

Chart Validity:        ✓  92/100 (PASS)
  - 图表类型: bar chart (销售数据) ✓
  - 数据准确性: 正确 ✓
  - 配置: 完整 ✓

Interactivity:         ✓ 100/100 (PASS)
  - 导航: 正常 ✓
  - 键盘: 可用 ✓
  - 全屏: 工作 ✓
  - 响应式: 适配 ✓

Issues Found: 1
  Critical: 0
  Major: 0
  Minor: 1

Minor Issue:
1. [MINOR] 建议为图表添加数据标签
   - Location: slide-3 (销售数据)
   - Suggestion: 在柱状图上显示具体数值，提升可读性

Status: ✓ APPROVED for use
```

## 示例 2: 检测到问题

### 场景：生成有问题的 HTML

假设生成的 HTML 存在以下问题：

1. JavaScript 错误：`navigate` 函数未定义
2. 内容丢失：缺少 2 个要点
3. 样式不一致：边距不统一

### 审查输出

```
✗ HTML Presentation Review Report

Overall Score: 68/100 - NEEDS IMPROVEMENT

Content Integrity:     ✗  70/100 (FAIL)
  - 源文档章节: 4, HTML 章节: 4 ✓
  - 源文档要点: 10, HTML 要点: 8 ✗
  - 数据点: 4, 已可视化: 4 ✓
  - 结论: 3, 已展示: 3 ✓
  - 文本准确性: 80% 保留 ✗

  ❌ CRITICAL ISSUE:
  - 缺少 2 个要点 (源文档 10 个，HTML 仅 8 个)
  - 部分文本被改写（非原文）

Code Quality:          ✗  65/100 (FAIL)
  - HTML 语法: 有效 ✓
  - CSS 语法: 正确 ✓
  - JavaScript: 不完整 ✗
  - 控制台错误: 2 个 ✗

  ❌ CRITICAL ISSUES:
  1. Uncaught ReferenceError: navigate is not defined
     - Location: Line 508, onclick handler
     - Fix: Define navigate() function or use existing API

  2. Uncaught SyntaxError: missing ) after argument list
     - Location: Line 245
     - Fix: Check function call syntax

McKinsey Style:        ⚠  75/100 (NEEDS IMPROVEMENT)
  - 颜色方案: 基本符合 ✓
  - 排版: 部分不一致 ⚠
  - 布局: 边距不统一 ✗
  - 留白: 部分不足 ⚠

  ⚠ MAJOR ISSUE:
  - 边距不一致: slide-2 (50px), slide-4 (42px)
  - 建议: 统一所有幻灯片边距为 50px

Chart Validity:        ✓  90/100 (PASS)
Interactivity:         ✗  70/100 (FAIL)
  - 导航: 部分失效 ✗
  - JavaScript 错误导致功能异常 ✗

Issues Found: 6
  Critical: 3
  Major: 2
  Minor: 1

Critical Issues (必须修复):
1. [CRITICAL] JavaScript 错误：navigate 函数未定义
2. [CRITICAL] JavaScript 语法错误：缺少括号
3. [CRITICAL] 内容丢失：缺少 2 个要点

Major Issues (强烈建议修复):
4. [MAJOR] 边距不一致
5. [MAJOR] 文本被改写（非原文）

Minor Issues:
6. [MINOR] 建议添加数据标签

Recommendations:
❌ 必须先修复所有 Critical 问题
1. 修复 JavaScript 函数定义
2. 补充缺失的要点
3. 统一边距设置
4. 使用原文而非改写
5. 重新生成并审查

Status: ❌ NOT APPROVED - 必须修复后重新审查
```

## 示例 3: 优秀输出

### 场景：完美的 HTML 生成

```
✓ HTML Presentation Review Report

Overall Score: 98/100 - EXCELLENT

Content Integrity:     ✓ 100/100 (PASS)
  - 所有章节完整 ✓
  - 所有要点保留 ✓
  - 所有数据可视化 ✓
  - 文本 100% 准确 ✓

Code Quality:          ✓ 100/100 (PASS)
  - 代码完美 ✓
  - 无任何错误 ✓

McKinsey Style:        ✓  98/100 (PASS)
  - 设计标准 ✓
  - 专业美观 ✓

Chart Validity:        ✓  95/100 (PASS)
Interactivity:         ✓ 100/100 (PASS)

Issues Found: 1
  Critical: 0
  Major: 0
  Minor: 1

Minor Issue:
1. [MINOR] 可选：添加 ARIA 标签提升可访问性
   - Impact: 低
   - Effort: 低

Status: ✓ EXCELLENT - Approved for immediate use
```

## 测试清单

使用这个清单验证 review 功能：

### ✅ 功能测试

- [ ] Phase 5 自动触发
- [ ] HTML 文件正确读取
- [ ] 源文档正确读取
- [ ] 内容完整性检查执行
- [ ] 代码质量检查执行
- [ ] McKinsey 样式检查执行
- [ ] 图表验证执行
- [ ] 交互功能测试执行
- [ ] 审查报告正确生成
- [ ] 评分准确

### ✅ 问题检测测试

- [ ] 检测缺失内容
- [ ] 检测文本改写
- [ ] 检测 JavaScript 错误
- [ ] 检测语法错误
- [ ] 检测样式不一致
- [ ] 检测图表类型不当
- [ ] 检测交互功能失效

### ✅ 报告格式测试

- [ ] 包含总体评分
- [ ] 包含各维度评分
- [ ] 包含问题列表
- [ ] 包含严重程度分类
- [ ] 包含修复建议
- [ ] 包含状态判断

### ✅ 评分标准测试

- [ ] 95-100: 优秀
- [ ] 85-94: 良好
- [ ] 75-84: 一般
- [ ] 65-74: 需要改进
- [ ] <65: 不合格

## 如何运行测试

### 方法 1: 使用真实文档

```bash
# 准备测试文档
echo "# 测试报告
- 要点 1
- 要点 2
- 要点 3" > test.md

# 执行 beauty 命令
/beauty test.md

# 等待 Phase 5 自动审查完成
# 查看审查报告
```

### 方法 2: 手动调用 reviewer

```bash
# 如果已有 HTML 文件
# 直接调用 html-presentation-reviewer agent
# 输入 HTML 文件路径和源文档路径
```

### 方法 3: 单元测试

创建测试用例验证 reviewer 的各个功能：

```javascript
// 测试内容完整性检查
test('Content Integrity Check', () => {
  const source = { sections: 5, bullets: 20 };
  const html = { sections: 5, bullets: 20 };
  expect(checkContentIntegrity(source, html)).toBe(true);
});

// 测试代码质量检查
test('Code Quality Check', () => {
  const html = '<html>...</html>';
  const issues = checkCodeQuality(html);
  expect(issues.critical).toBe(0);
});

// 测试样式合规检查
test('Style Compliance Check', () => {
  const css = '.slide { margin: 50px; }';
  const compliant = checkMcKinseyStyle(css);
  expect(compliant).toBe(true);
});
```

## 预期结果

成功实施后，用户将看到：

1. ✅ **自动质量保证** - 每次生成后自动检查
2. ✅ **内容完整性保证** - 确保 100% 内容保留
3. ✅ **代码质量保证** - 无语法或运行时错误
4. ✅ **样式合规保证** - 符合 McKinsey 标准
5. ✅ **清晰的问题报告** - 明确指出需要修复的地方
6. ✅ **可操作的建议** - 提供具体修复方案

## 常见问题排查

### Q: Phase 5 没有触发？

**A: 检查以下项：**
- plugin.json 是否包含 html-presentation-reviewer
- SKILL.md 是否包含 Phase 5 定义
- Agent 文件是否存在于正确位置

### Q: 审查报告不准确？

**A: 验证以下项：**
- 源文档路径正确
- HTML 文件路径正确
- 文件内容可读取
- Agent 配置正确

### Q: 评分不合理？

**A: 确认以下项：**
- 评分标准配置正确
- 检查逻辑完整
- 测试用例覆盖全面

## 下一步

1. ✅ 在真实文档上测试 review 功能
2. ✅ 验证问题检测准确性
3. ✅ 确认报告格式清晰
4. ✅ 收集用户反馈
5. ✅ 持续优化 reviewer agent

---

**注意**: 这个测试示例展示了 review 功能的核心用例。实际使用中，reviewer 会根据具体文档内容和生成的 HTML 进行详细检查。
