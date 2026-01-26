# HTML Presentation Reviewer 优化总结

## 优化日期
2025-01-25

## 优化目标
强化 `html-presentation-reviewer` agent，确保生成的 HTML 演示文稿：
1. **严格匹配 McKinsey 设计风格**（颜色/字体/布局）
2. **100% 保留内容**（不精简、不总结、不删减）
3. **只优化图文展示样式**，不修改内容本身

## 主要改进

### 1. ⭐ McKinsey 设计风格严格验证（新增最高优先级）

#### 1.1 颜色精确匹配验证
**新增功能**：
- 精确验证 8 个标准颜色的 hex 值
  ```css
  --primary-background: #FFFFFF
  --header-background: #000000
  --primary-accent: #F85d42
  --secondary-accent: #74788d
  --deep-blue: #556EE6
  --green: #34c38f
  --blue: #50a5f1
  --yellow: #f1b44c
  ```

- 自动检测并报告：
  - 任何颜色值不匹配 → CRITICAL
  - 使用非标准颜色 → CRITICAL
  - 颜色使用不一致 → MAJOR

- 验证方法：
  ```javascript
  // 提取 CSS 变量并逐个验证
  const actualValue = getComputedStyle(document.documentElement)
    .getPropertyValue(varName).trim();
  if (actualValue.toUpperCase() !== expectedValue.toUpperCase()) {
    reportCRITICAL(`颜色不匹配: ${varName}`);
  }
  ```

#### 1.2 字体大小精确验证
**新增功能**：
- 精确验证字体大小范围
  - 标题：48-64px（必须）
  - 副标题：28-36px（必须）
  - 正文：16-20px（必须）
  - 图表标签：12-14px（必须）

- 验证字体字重
  - 标题/副标题：bold（必须）
  - 正文：normal（必须）

- 自动检测并报告：
  - 标题 < 48px 或 > 64px → CRITICAL
  - 副标题 < 28px 或 > 36px → MAJOR
  - 正文 < 16px 或 > 20px → MAJOR
  - 使用错误的字重 → MAJOR

#### 1.3 布局精确验证
**新增功能**：
- 精确验证布局规范
  - 页边距：40-60px（必须）
  - 元素间距：20-30px（必须）
  - box-sizing: border-box（必须）
  - 响应式断点：1200px, 768px（必须）

- 自动检测并报告：
  - 页边距 < 40px 或 > 60px → MAJOR
  - 元素间距 < 20px 或 > 30px → MINOR
  - 对齐不一致 → MAJOR

#### 1.4 样式一致性验证
**新增功能**：
- 验证所有幻灯片使用统一样式
- 检测孤立的非标准样式
- 检测内联样式覆盖

- 自动检测并报告：
  - 幻灯片间样式不一致 → CRITICAL
  - 使用内联样式覆盖 → MAJOR
  - 样式冲突 → MAJOR

### 2. ⭐ 内容 100% 完整性验证（强化）

#### 2.1 精简模式检测
**新增功能**：
- 自动检测常见的精简模式
  ```javascript
  const simplificationPatterns = [
    /等/g,                    // "等"表示省略
    /主要|核心|关键/g,         // 概括性词语
    /包括|含有/g,             // 可能省略了详细列表
    /以及|和/g,               // 检查是否有省略
  ];
  ```

- 检测到精简模式 → CRITICAL

#### 2.2 数据完整性检查
**强化功能**：
- 验证数据点数量一致
- 验证数据值精确匹配
- 验证数据精度一致（不四舍五入）

- 自动检测并报告：
  - 数据点数量不匹配 → CRITICAL
  - 数据值不匹配 → CRITICAL
  - 数据精度损失 → CRITICAL

#### 2.3 列表完整性检查
**强化功能**：
- 验证列表项数量一致
- 验证列表项文本准确（原文）
- 检测"等"字省略

- 自动检测并报告：
  - 列表项数量不一致 → CRITICAL
  - 使用"等"字省略 → CRITICAL
  - 使用"主要"概括 → CRITICAL

### 3. 图表样式严格验证（强化）

#### 3.1 Chart.js 图表颜色验证
**新增功能**：
- 验证图表使用 McKinsey 调色板
- 不允许使用非标准颜色

- 验证方法：
  ```javascript
  const chartColors = ['#F85d42', '#556EE6', '#34c38f', '#50a5f1', '#f1b44c'];
  dataset.backgroundColor.forEach(color => {
    if (!chartColors.includes(color.toUpperCase())) {
      reportMAJOR(`图表使用非标准颜色: ${color}`);
    }
  });
  ```

#### 3.2 图表字体验证
**新增功能**：
- 验证图表标题：28-36px
- 验证坐标轴标签：12-14px
- 验证图例：12-14px

- 自动检测并报告：
  - 字体大小不符合 → MAJOR
  - 字重不符合 → MAJOR

#### 3.3 概念图表验证
**强化功能**：
- 验证颜色使用 McKinsey 调色板
- 验证字体大小符合规范
- 验证线条/边框使用标准颜色

- 自动检测并报告：
  - 使用非标准颜色 → MAJOR
  - 字体大小不符合 → MAJOR
  - 布局错误 → CRITICAL

### 4. 报告格式增强（新增详细输出）

#### 4.1 设计风格专项报告
**新增字段**：
```json
{
  "mckinsey_design_style_compliance": {
    "score": 95,
    "status": "PASS",
    "checks": {
      "color_scheme_compliant": {
        "status": true,
        "details": {
          "--primary-background": "#FFFFFF ✓",
          "--header-background": "#000000 ✓",
          // ... 逐个验证每个颜色
        }
      },
      "typography_compliant": {
        "status": true,
        "details": {
          "title_font_size": "48-64px ✓",
          // ... 逐个验证每个字体规范
        }
      },
      "layout_compliant": {
        "status": true,
        "details": {
          "slide_padding": "40-60px ✓",
          // ... 逐个验证每个布局规范
        }
      }
    }
  }
}
```

#### 4.2 内容完整性详细分析
**新增字段**：
```json
{
  "content_integrity": {
    "detailed_analysis": {
      "text_preservation_rate": "100%",
      "word_count_match": true,
      "detected_simplification_patterns": [],
      "missing_content": []
    }
  }
}
```

#### 4.3 评分细化
**新增字段**：
```json
{
  "review_summary": {
    "design_style_score": 95,
    "content_integrity_score": 100
  }
}
```

## 审查流程优化

### 原流程（3 个步骤）
1. 读取 HTML 和源文档
2. 执行自动检查
3. 生成审查报告

### 新流程（5 个步骤，更严格）
1. **读取 HTML 和源文档**
2. **第一阶段：McKinsey 设计风格严格验证** ⭐
   - 颜色精确匹配验证（逐个 hex 值）
   - 字体大小精确验证（逐个范围）
   - 布局精确验证（页边距、间距）
   - 样式一致性验证（所有幻灯片）
3. **第二阶段：内容 100% 完整性验证** ⭐
   - 章节完整性检查
   - 数据点完整性检查（包括精度）
   - 文本完整性检查（包括精简模式检测）
   - 列表完整性检查
4. **第三阶段：图表样式严格验证**
   - Chart.js 图表颜色/字体验证
   - 概念图表颜色/字体验证
5. **生成详细审查报告**
   - McKinsey 设计风格专项报告
   - 内容完整性详细分析
   - 问题优先级排序

## 问题严重程度调整

### CRITICAL（新增更多项）
**原有**：
- 内容缺失或丢失
- 代码语法错误
- JavaScript 运行时错误

**新增**：
- 内容被总结/压缩
- 使用非 McKinsey 颜色
- 字体大小严重偏离规范（<48px 或 >64px 标题）
- 精简模式检测
- 数据精度损失

### MAJOR（调整标准）
**原有**：
- 格式不一致
- 表达不清
- 计算错误

**新增/调整**：
- 颜色使用近似值（非精确匹配）
- 字体大小轻微偏离规范
- 布局不一致
- 图表使用非标准颜色
- 图表字体大小不符合规范
- 样式不一致

### MINOR（保持不变）
- 拼写错误
- 标点问题
- 样式小瑕疵
- 可访问性建议
- 代码优化建议

## 验证规则示例

### 示例 1：颜色验证

**❌ 失败案例**：
```css
/* 使用了近似值，不符合要求 */
--primary-accent: #F85D43;  /* 应为 #F85d42 */
--header-background: #111;  /* 应为 #000000 */
```

**✅ 通过案例**：
```css
/* 精确匹配 McKinsey 标准 */
--primary-accent: #F85d42;
--header-background: #000000;
```

### 示例 2：字体大小验证

**❌ 失败案例**：
```css
/* 标题太小 */
.title { font-size: 36px; }  /* 应为 48-64px */

/* 副标题太大 */
.subtitle { font-size: 40px; }  /* 应为 28-36px */
```

**✅ 通过案例**：
```css
/* 符合 McKinsey 标准 */
.title { font-size: 56px; }     /* 48-64px ✓ */
.subtitle { font-size: 32px; }  /* 28-36px ✓ */
.body { font-size: 18px; }      /* 16-20px ✓ */
```

### 示例 3：内容完整性验证

**❌ 失败案例**：
```markdown
<!-- 源文档 -->
- 要点 1
- 要点 2
- 要点 3
- 要点 4
- 要点 5

<!-- HTML（被精简） -->
- 要点 1
- 要点 2
- 要点 3 等  <!-- 使用了"等"，CRITICAL -->
```

```markdown
<!-- 源文档 -->
市场规模：1723.498 亿美元

<!-- HTML（精度损失） -->
市场规模：1723 亿美元  <!-- CRITICAL -->
```

**✅ 通过案例**：
```markdown
<!-- 源文档和 HTML 完全一致 -->
- 要点 1
- 要点 2
- 要点 3
- 要点 4
- 要点 5

<!-- 数据精度完全一致 -->
市场规模：1723.498 亿美元
```

## 使用建议

### 对于生成幻灯片的 subagent

1. **严格遵守 McKinsey 设计规范**
   - 复制粘贴精确的 hex 颜色值
   - 使用精确的字体大小范围
   - 遵循精确的布局规范

2. **100% 保留内容**
   - 不要总结
   - 不要压缩
   - 不要使用"等"字
   - 不要使用"主要"、"核心"等概括词
   - 保持数据精度一致

3. **使用标准图表**
   - Chart.js 图表必须使用 McKinsey 颜色
   - 概念图表必须使用 McKinsey 颜色
   - 图表字体必须符合规范

### 对于审查流程

1. **Phase 5 必须执行**
   - 每次生成 HTML 后自动触发
   - 不可跳过

2. **Critical 问题必须修复**
   - 颜色不匹配 → 重新生成
   - 内容精简 → 重新生成
   - 字体大小严重偏离 → 重新生成

3. **Major 问题强烈建议修复**
   - 颜色近似值 → 修正
   - 字体大小轻微偏离 → 修正
   - 布局不一致 → 修正

## 效果预期

### 优化前
- ✅ 基本设计风格检查
- ⚠️ 颜色验证不够精确
- ⚠️ 字体验证不够严格
- ⚠️ 内容完整性检查不够全面
- ⚠️ 可能遗漏精简模式

### 优化后
- ✅ **McKinsey 设计风格严格验证**
  - 精确到 hex 值的颜色验证
  - 精确到像素的字体验证
  - 精确到像素的布局验证
- ✅ **内容 100% 完整性保证**
  - 精简模式自动检测
  - 数据精度验证
  - 列表完整性验证
- ✅ **详细的问题报告**
  - McKinsey 设计风格专项报告
  - 内容完整性详细分析
  - 明确的修复建议

## 文件更新清单

- ✅ `agents/html-presentation-reviewer.md` - 完全重写审查逻辑
  - 新增 McKinsey 设计风格严格验证部分
  - 强化内容完整性验证部分
  - 增强报告格式
  - 更新问题严重程度标准

- ✅ `HTML_REVIEW_ENHANCEMENT_SUMMARY.md` - 本文档
  - 记录所有优化内容
  - 提供使用建议
  - 提供验证示例

## 下一步建议

1. **测试新审查流程**
   - 使用现有 HTML 测试
   - 验证颜色检测是否准确
   - 验证精简模式检测是否有效

2. **更新生成 subagent**
   - 强调 McKinsey 规范的重要性
   - 强调内容 100% 保留的要求
   - 提供规范检查清单

3. **收集反馈**
   - 实际使用中的问题
   - 需要进一步优化的地方
   - 新的验证需求

---

**优化完成日期**: 2025-01-25
**优化人员**: Claude Code
**版本**: 2.0.0
