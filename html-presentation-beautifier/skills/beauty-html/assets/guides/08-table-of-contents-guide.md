# 目录页示例 (08-table-of-contents.html)

## 📋 示例概述

**文件名**: 08-table-of-contents.html
**布局类型**: L1 目录列表布局
**适用场景**: 目录导航、章节概览、内容索引
**匹配度**: 100%

---

## 🎯 适用场景

### 最佳使用场景
1. **多章节文档**: 3个或以上章节的报告、分析文档
2. **章节导航**: 需要清晰导航结构的长文档
3. **内容概览**: 让读者快速了解文档结构
4. **专业报告**: McKinsey/BCG 风格的咨询报告
5. **演示文稿**: 封面页后的第二页

### 内容特征
- **章节数量**: 3个或以上章节
- **章节编号**: 01, 02, 03... 或 1, 2, 3...
- **章节标题**: 简洁明确的标题
- **章节描述**: 可选的简短说明(15-30字)
- **页码**: 可选的页码标注

---

## 🎨 设计特点

### 布局结构
```
┌─────────────────────────────────────────┐
│             目录                         │ (页面标题,48px,居中)
│  ═══════════════════════════════════    │ (红色下划线)
│                                          │
│  ┌──────────────────────────────────┐  │
│  │ 01  执行摘要                  P.3 │  │ (目录项1)
│  │     核心发现与关键建议概览      │  │
│  └──────────────────────────────────┘  │
│                                          │
│  ┌──────────────────────────────────┐  │
│  │ 02  市场分析                  P.8 │  │ (目录项    行业趋势、竞争格局与市场机会│  │
│  └──────────────────────────────────┘  │
│                                          │
│  ┌──────────────────────────────────┐  │
│  │ 03  能力评估                 P.15 │  │ (目录项3)
│  │     组织能力、资源配置与核心竞争力│  │
│  └──────────────────────────────────┘  │
│                                          │
│  ...                            │
└─────────────────────────────────────────┘
```

### 颜色系统
- **页面标题**: `#000000` (黑色)
- **标题下划线**: `#F85d42` (主强调色)
- **章节编号**: `#F85d42` (主强调色,32px,加粗)
- **章节标题**: `#333333` (深灰色,24px,600)
- **章节描述**: `#74788d` (灰色,16px)
- **页码**: `#74788d` (灰色,18px)
- **卡片背景**: `#fafafa` (浅灰色)
- **悬停背景**: `#f0f0f0` (更深灰色)
- **悬停左边框**: `#F85d42` (主强调色,4px)

### 字体规范
- **页面标题**: 48px, Bold, #000000
- **章节编号**: old, #F85d42
- **章节标题**: 24px, 600, #333333
- **章节描述**: 16px, Regular, #74788d
- **页码**: 18px, Regular, #74788d

### 交互效果
- **悬停效果**:
  - 背景色变深 (#fafafa → #f0f0f0)
  - 左边框显示红色 (4px #F85d42)
  - 向右平移 5px
  - 过渡时间 0.3s

---

## 🔧 使用方法

### 步骤1: 识别适用场景
```markdown
✅ 文档是否有3个或以上章节?
✅ 是否需要在封面页后展示目录?
✅ 是否需要章节导航功能?
✅ 是否是专业报告或演示文稿?

如果以上全部为"是",使用此示例。
```

### 步骤2: 准备内容
```markdown
对于每个章节,准备:
1. 章节编号: 01, 02, 03... 或 1, 2, 3...
2. 章节标题: 简洁明确,5-10个汉字
3. 章节描述(可选): 15-30字的简短说明
4. 页码(可选): P.3, P.8, P.15...
```

### 步骤3: 替换内容
```html
<!-- 1. 替换页面标题(如果需要) -->
<h1 class="page-title">目录</h1>
<!-- 或者 -->
<h1 class="page-title">Table of Contents</h1>
<h1 class="page-title">内容概览</h1>

<!-- 2. 替换目录项 -->
<div class="toc-item">
    <div class="toc-number">01</div>
    <div class="toc-content">
        <div class="toc-title">执行摘要</div>
        <div class="toc-description">核心发现与关键建议概览</div>
    </div>
    <div class="toc-page">P.3</div>
</div>

<!-- 3. 添加更多目录项(复制上面的结构) -->
<div class="toc-item">
    <div class="toc-number">02</div>
    <div class="toc-content">
        <div class="toc-title">[章节标题]</div>
        <div class="toc-description">[章节描述]</div>
    </div>
    <div class="toc-page">P.[页码]</div>
</div>
```

### 步骤4: 调整数量
```html
<!-- 删除不需要的目录项 -->
<!-- 或者复制粘贴添加更多目录项 -->

<!-- 建议目录项数量: -->
- 最少: 3个章节
- 推荐: 5-7个章节
- 最多: 10个章节 (超过10个考虑分页或分组)
```

---

## 💡 最佳实践

### 1. 章节编号设计
```html
<!-- 方式1: 两位数编号 (推荐) -->
<div class="toc-number">01</div>
<div class="toc-number">02</div>

<!-- 方式2: 单位数编号 -->
<div class="toc-number">1</div>
<div class="toc-number">2</div>

<!-- 方式3: 罗马数字 -->
<div class="toc-number">I</div>
<div class="toc-number">II</div>

<!-- 方式4: 字母编号 -->
<div class="toc-number">A</div>
<div class="toc-number">B</div>
```

### 2. 章节标题长度
- **理想长度**: 5-10个汉字
- **最大长度**: 15个汉字
- **过长处理**: 使用省略号或换行

```html
<!-- 理想长度 -->
<div class="toc-title">市场分析</div>

<!-- 适中长度 -->
<div class="toc-title">数字化转型战略规划</div>

<!-- 过长需要优化 -->
<div class="toc-title">基于大数据的客户行为分析与精准营销策略研究</div>
<!-- 优化为 -->
<div class="toc-title">客户行为分析与营销策略</div>
```

### 3. 章节描述使用
```html
<!-- 有描述 (推荐) -->
<div class="toc-content">
    <div class="toc-title">市场分析</div>
    <div class="toc-description">行业趋势、竞争格局与市场机会</div>
</div>

<!-- 无描述 (简洁风格) -->
<div class="toc-content">
    <div class="toc-title">市场分析</div>
</div>
```

### 4. 页码显示
```html
<!-- 有页码 (推荐) -->
<div class="toc-page">P.3</div>

<!-- 无页码 (隐藏或删除) -->
<div class="toc-page" style="display: none;"></div>

<!-- 不同页码格式 -->
<div class="toc-page">P.3</div>    <!-- 推荐 -->
<div class="toc-page">第3页</div>
<div class="toc-page">3</div>
<div class="toc-page">Slide 3</div>
```

### 5. 响应式适配
```css
/* 移动端自动适配 */
@media (max-width: 768px) {
    .toc-item {
        flex-direction: column;  /* 纵向排列 */
    }
    .toc-number {
        margin-bottom: 10px;     /* 编号下方间距 */
    }
    .toc-page {
        margin-top: 10px;        /* 页码上方间距 */
    }
}
```

---

## 🚫 不适用场景

### 不要使用此示例的情况
1. **章节少于3个**: 使用封面页或单页内容
2. **章节过多(10+)**: 考虑分组或多页目录
3. **需要多级目录**: 使用树状目录结构
4. **需要可点击导航**: 添加 JavaScript 锚点跳转
5. **非正式文档**: 使用更简洁的布局

---

## 📈 变体建议

### 变体1: 两列目录布局
```css
.toc-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}
```

### 变体2: 分组目录
```html
<div class="toc-group">
    <h3 class="toc-group-title">第一部分: 现状分析</h3>
    <div class="toc-item">...</div>
    <div class="toc-item">...</div>
</div>

<div class="toc-group">
    <h3 class="toc-group-title">第二部分: 战略规划</h3>
    <div -item">...</div>
    <div class="toc-item">...</div>
</div>
```

### 变体3: 带图标的目录
```html
<div class="toc-item">
    <div class="toc-icon">📊</div>
    <div class="toc-number">01</div>
    <div class="toc-content">
        <div class="toc-title">市场分析</div>
        <div class="toc-description">行业趋势与竞争格局</div>
    </div>
</div>
```

### 变体4: 可点击导航
```html
<a href="#section-1" class="toc-item">
    <div class="toc-number">01</div>
    <div class="toc-content">
        <div class="toc-title">执行摘要</div>
        <div class="toc-description">核心发现与关键建议</div>
    </div>
    <div class="toc-page">P.3</div>
</a>
```

---

## 📊 实际案例

### 案例1: 咨询报告目录
```
01 - 执行摘要 (核心发现与关键建议概览)
02 - 市场分析 (行业趋势、竞争格局与市场机会)
03 - 能力评估 (组织能力、资源配置与核心竞争力)
04 - 战略建议 (增长路径、优先事项与实施计划)
05 - 财务预测 (收入模型、成本分析与投资回报)
06 - 实施路线图 (关键里程碑、资源需求与风险管理)
07 - 附录 (详细数据、方法论与参考资料)
```

### 案例2: 产品分析报告目录
```
1. 产品概述
2. 市场定位
3. 用户研究
4. 竞品分析
5. 功能规划
6. 技术架构
7. 商业模式
8. 实施计划
```

### 案例3: 年度报告目录
```
一、公司概况
二、经营回顾
三、财务分析
四、业务进展
五、未来展望
六、风险提示
七、附录资料
```

---

## 🎯 与其他示例的配合使用

### 标准文档结构
```
第1页: 01-cover-page.html (封面页)
第2页: 08-table-of-contents.html (目录页) ← 本示例
第3页: 02/03/04-*.html (内容页)
第N页: 01-cover-page.html (结束页,可选)
```

### 使用时机
- **必须使用**: 3+章节的正式报告
- **推荐使用**: 5+页的演示文稿
- **可选使用**: 简短文档(可直接进入内容)

---

## 🔄 更新日志

### v1.0 (2026-01-27)
- ✨ 初始版本
- ✨ 卡片式目录项布局
- ✨ 悬停效果和交互设计
- ✨ 响应式移动端适配
- ✨ 支持章节编号、标题、描述、页码

---

**维护者**: HTML Presentation Beautifier Team
**最后更新**: 2026-01-27
**示例文件**: 08-table-of-contents.html
