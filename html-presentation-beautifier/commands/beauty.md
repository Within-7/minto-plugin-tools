---
name: beauty
description: 将文档转化为专业 McKinsey 风格 HTML 演示文稿。严格遵循5步流程：1.文档内容分析合并 2.幻灯片设计与图文选择（⚠️布局优先原则：2.0先确定页面布局（单列/双列/三列/卡片网格/图表文本），2.1再选择图表图文；必须读beauty-html/references/chart-selection-guide.md和assets/CHART_EXAMPLES_INDEX.md）⚠️智能布局选择：优先使用横向布局（双列/三列/卡片网格），避免纵向长列表，应用随机选择机制 3.转化为McKinsey风格HTML（必须读beauty-html/references/best-practices.md和mckinsey-design-system.md及assets/presentation-template.html）⚠️图表修复：强制width:100%、responsive:true、maintainAspectRatio:false，确保图表正常显示 4.合并为单HTML文件 5.代码审核检验。⚠️ 第5步必须严格检验：1.内容完整性（100%保留原文所有章节/数据/结论，零遗漏）2.代码质量（符合HTML最佳实践，可访问可运行）3.资源使用（必须读取并参考beauty-html中的所有资源）4.图表显示（宽度非0、大小合理）5.布局优化（充分利用横向空间）6.布局合理性（布局优先于图表选择）。任一标准未通过必须返回对应步骤重新执行。
---

# Beauty 命令

将文档、数据、结论等信息转化为通俗连贯、明确清晰的 McKinsey 风格 HTML 演示文稿。

## ⚠️ 核心原则

**必须严格遵循以下5步固定流程，不得跳过任何步骤：**

**🔑 步骤2、步骤3必须读取并参考skill资源：**
- **步骤2（图文选择）**：必须读 `beauty-html/references/chart-selection-guide.md`、`beauty-html/assets/CHART_EXAMPLES_INDEX.md`、`beauty-html/assets/INSIGHT_VISUALIZATION_GUIDE.md`
- **步骤3（HTML生成）**：必须读 `beauty-html/references/best-practices.md`、`beauty-html/references/mckinsey-design-system.md`、`beauty-html/assets/presentation-template.html`、`beauty-html/assets/TEMPLATE_USAGE_GUIDE.md`

**🔑 第5步是关键验收步骤，实行一票否决制：**
- **内容完整性检验**：必须100%保留原文所有章节、数据、结论，零遗漏
- **代码质量检验**：必须符合HTML最佳实践，可访问可运行
- **资源使用检验**：必须验证步骤2和步骤3是否正确读取并使用了skill资源
- **发现问题立即回退**：返回对应步骤重新执行，绝不将就

**⚠️ Token限制处理原则（严格执行，不得偷工减料）：**

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

**关键规则：**
- ✅ **质量 > 速度**：宁可多轮对话，不可降低质量
- ✅ **完整 > 简化**：宁可分多次执行，不可压缩内容
- ✅ **标准 > 妥协**：宁可触发继续，不可偷工减料

---

## 📋 固定5步执行流程

### 步骤 1️⃣：文档内容分析合并

**目标**：完整理解源文档内容，提取关键信息，建立内容结构。

**⚠️ Token限制处理机制：**

**如果文档过长无法一次性读取完整：**

```
正确做法（使用继续机制）：

步骤1.1：读取文档前半部分
├─ 使用 Read 工具读取文档（offset: 0, limit: 500）
├─ 提取前半部分的章节结构
├─ 记录前半部分的数据点
└─ 输出："步骤1.1完成 - 已分析文档前半部分（0-500行）
       请输入'继续'以分析后半部分"

【等待用户输入"继续"】

步骤1.2：读取文档后半部分
├─ 使用 Read 工具读取文档（offset: 500, limit: 500）
├─ 提取后半部分的章节结构
├─ 记录后半部分的数据点
└─ 输出："步骤1.2完成 - 已分析文档后半部分（500-1000行）
       文档分析100%完成"

【如果文档超过1000行，继续分片读取】

步骤1.3：合并分析结果
├─ 整合所有部分的分析结果
├─ 生成完整的章节结构清单
├─ 生成完整的数据点清单
└─ 进入步骤2
```

**❌ 禁止做法（偷工减料）：**
```
错误做法1：只读前几行
├─ Read 文件（limit: 50）
└─ ❌ 跳过了后面的内容

错误做法2：使用摘要
├─ 请用户总结文档内容
└─ ❌ 可能丢失细节

错误做法3：分步执行但不说明
├─ 只生成前半部分内容
└─ ❌ 用户不知道要继续
```

**执行要求**：
- ✅ 完整阅读源文档，不做任何修改或删减
- ✅ 识别文档类型（报告、分析、方案、研究等）
- ✅ 提取核心内容元素：
  - 标题层次结构（H1 → H2 → H3）
  - 关键数据和数值
  - 主要结论和见解
  - 重要建议和行动项
  - 对比关系和表格数据
- ✅ 建立内容逻辑结构：
  - 主题分组
  - 因果关系
  - 时间顺序
  - 优先级排序
- ✅ 记录所有定量数据（数字、百分比、货币等）

**输出产物**：
- 内容结构大纲（包含所有章节和要点）
- 数据点清单（所有可用于可视化的数值）
- 关键结论列表（必须完整保留）

**验证标准**：
- [ ] 所有原文内容已提取
- [ ] 无内容丢失或遗漏
- [ ] 数据点完整记录
- [ ] 逻辑结构清晰

---

### 步骤 2️⃣：幻灯片设计与图文形式选择

**⚠️ 必须严格参考图表资源和选择准则！**

**目标**：为每页幻灯片选择最佳呈现形式，确保信息清晰传达。

**⚠️ 强制要求：必须读取并参考以下资源**

#### 必读资源1：图表选择指南
```
文件路径：html-presentation-beautifier/skills/beauty-html/references/chart-selection-guide.md

必须使用Read工具读取此文件，并严格遵循其中的决策树：
- 9种内容结构类型的识别方法
- 每种类型对应的关键词
- 图表选择的决策树
- 推荐的示例文件路径
```

#### 必读资源2：图表示例索引
```
文件路径：html-presentation-beautifier/skills/beauty-html/assets/CHART_EXAMPLES_INDEX.md

必须使用Read工具读取此文件，了解：
- 所有可用的图表类型清单
- 每种图表的适用场景
- 核心实现代码
- McKinsey配色方案
```

#### 必读资源3：观点可视化指南
```
文件路径：html-presentation-beautifier/skills/beauty-html/assets/INSIGHT_VISUALIZATION_GUIDE.md

必须使用Read工具读取此文件，学习：
- 如何识别观点类型
- 观点与图表的映射关系
- 可视化实现的最佳实践
```

**执行要求**：

#### 2.0 页面布局规划（⚠️ 新增 - 优先级最高）

**⚠️ 关键原则：先确定页面布局，再选择图表/图文类型！**

**布局优先决策流程：**

```
步骤1：分析内容特征
├─ 内容类型：概念性 vs 数据性
├─ 观点数量：1个、2-3个、4-6个、7+个
├─ 数据密度：无数据、少量数据、大量数据
└─ 空间需求：纵向空间、横向空间

步骤2：选择基础布局类型
├─ 单列布局（1个观点）
├─ 双列布局（2-3个观点）
├─ 三列布局（3个并列观点）
├─ 卡片网格布局（4-6个观点）
├─ 图表+文本布局（包含数据可视化）
└─ 纯图表布局（数据密集型）

步骤3：确定垂直方向排列
├─ 上下布局：图表在上，文本在下
├─ 下上布局：文本在上，图表在下
├─ 左右布局：图表在左，文本在右
└─ 右左布局：文本在左，图表在右

步骤4：基于布局选择图表/图文类型
└─ 进入步骤2.1进行详细选择
```

**基础布局类型清单（12种，包含专业场景布局）：**

**L1. 单列布局（Single Column）**
```
适用场景：
- 单个核心观点
- 深度阐述内容
- 强调框、警告框
- 章节封面页

空间特征：
- 纵向空间利用
- 适合大量文字
- 视觉焦点集中

示例：封面页、章节封面、核心结论
```

**L2. 双列布局（Two Column）**
```
适用场景：
- 2个并列观点
- 2个对象对比
- A vs B 对比
- 优点 vs 缺点

空间特征：
- 横向空间50:50分割
- 两列内容对称
- 适合对比展示

CSS：grid-template-columns: 1fr 1fr;
示例：平台 vs 个人IP对比
```

**L3. 三列布局（Three Column）**
```
适用场景：
- 3个并列观点
- 3个选项对比
- 3个步骤/阶段
- 3个关键要素

空间特征：
- 横向空间33:33:33分割
- 三列内容对称
- 适合并列展示

CSS：grid-template-columns: repeat(3, 1fr);
示例：三个核心要素、三种定价策略
```

**L4. 卡片网格布局（Card Grid）**
```
适用场景：
- 4-6个并列观点
- 多个特性/功能
- 多个建议/要点
- 多个成功案例

空间特征：
- 自适应列数（2x2, 2x3, 3x2）
- 充分利用横向空间
- 每个卡片独立

CSS：grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
示例：六大平台启示（6个卡片）
```

**L5. 图表+文本布局（Chart + Text）**
```
适用场景：
- 包含数据可视化
- 图表 + 关键洞察
- 图表 + 详细说明
- 图表 + 数据表

空间特征：
- 图表占50-70%宽度
- 文本占30-50%宽度
- 横向排列

变体：
- 上图下文（图表在上，文本在下）
- 左图右文（图表在左，文本在右）
- 右图左文（图表在右，文本在左）

示例：估值对比图表 + 详细数据说明
```

**L6. 纯图表布局（Chart Only）**
```
适用场景：
- 数据密集型内容
- 大型图表展示
- 多图表对比
- 复杂数据可视化

空间特征：
- 图表占80-100%空间
- 最少的文字说明
- 视觉焦点在数据

示例：收入结构对比、时间投入曲线
```

**L7. 混合布局（Mixed Layout）**
```
适用场景：
- 复杂内容结构
- 多种类型混合
- 图表 + 卡片 + 文本
- 分层展示

组合方式：
- 顶部强调框 + 底部双列
- 左侧图表 + 右侧三列
- 上部表格 + 底部卡片

示例：商业模式设计（图表 + 双列 + 强调框）
```

**布局选择决策表：**

| 内容特征 | 观点数量 | 数据密度 | 推荐布局 | 替代布局 |
|---------|---------|---------|---------|---------|
| 单个观点 | 1 | 无 | 单列布局 | 强调框 |
| 对比关系 | 2 | 无/少 | 双列布局 | 对比表格 |
| 并列关系 | 3 | 无 | 三列布局 | 双列布局 |
| 并列关系 | 4-6 | 无 | 卡片网格 | 双列布局 |
| 数据可视化 | 1-2 | 大量 | 图表+文本 | 纯图表 |
| 数据对比 | 2+ | 大量 | 双列+图表 | 图表+表格 |
| 混合内容 | 3+ | 中等 | 混合布局 | 图表+文本 |

**⚠️ 布局选择规则（严格执行）：**

**规则1：空间利用率优先**
```
✅ 优先使用横向布局（双列、三列、卡片网格）
✅ 避免纵向长列表导致需要滚动
✅ 单屏内容不超过视口高度的80%
❌ 禁止：7+个观点使用单列纵向布局
```

**规则2：内容密度匹配**
```
低密度（1-2个观点）→ 单列或双列
中密度（3-4个观点）→ 双列或三列
高密度（5-6个观点）→ 卡片网格
超高密度（7+个观点）→ 分页或混合布局
```

**规则3：数据可视化优先**
```
包含图表时：
├─ 图表为主要内容 → 纯图表布局
├─ 图表+关键洞察 → 图表+文本布局
├─ 图表+详细说明 → 图表+文本布局（上图下文）
└─ 多个图表 → 混合布局（上下排列）
```

**规则4：响应式考虑**
```
桌面优先：
├─ 充分利用横向空间
├─ 多列布局（2-4列）
└─ 大型图表（高度500px）

平板/手机：
├─ 自动转换为单列
├─ 图表高度降低（400px）
└─ 保持可读性
```

**⚠️ 布局与内容的适配检查：**

在确定布局后，必须进行以下检查：

```
□ 布局是否适合观点数量？
□ 布局是否适合数据密度？
□ 布局是否充分利用横向空间？
□ 布局是否避免纵向滚动？
□ 布局是否与内容类型匹配？
□ 布局是否有足够的视觉层次？
```

**如果任何一项为"否"，则需要重新选择布局。**

---

#### 2.1 图表/图文形式选择（⚠️ 基于示例文档对比选择 + 已确定的布局）

**⚠️ 关键原则1：此步骤必须基于2.0确定的布局进行选择！**

**⚠️ 关键原则2：必须使用示例文档对比选择机制，而非凭空设计！**

**目标**：基于示例文档库，通过对比当前页面特征与示例特征，选择最佳示例模板并基于其生成内容。

---

**🎯 步骤2.1.1：读取示例文档索引**

**⚠️ 必须读取：**
```
Read: skills/beauty-html/examples/INDEX.md
```

**了解内容：**
- 📋 所有可用的示例类型
- 🔍 快速查找指南
- 🎯 匹配决策树
- 📊 各示例的匹配条件

---

**🎯 步骤2.1.2：分析当前页面特征**

**分析维度：**

1. **内容类型**
   - 概念性：观点、建议、要点
   - 数据性：包含数据、图表

2. **观点数量**
   - 1个：封面、单个结论
   - 2个：对比关系
   - 3个：并列关系
   - 4-6个：多个并列
   - 7+个：需要分组或分页

3. **数据密度**
   - 无数据：纯文字内容
   - 少量数据：1-2个数据点
   - 中等数据：3-5个数据点，适合1个图表
   - 大量数据：6+个数据点，适合多个图表

4. **对比关系**
   - 并列关系：多个平等的观点
   - 对比关系：A vs B，优点 vs 缺点
   - 流程关系：时间序列、步骤
   - 层级关系：金字塔、树状图

5. **特殊数据要求识别** ⚠️ 新增
   - 用户定位数据：是否包含7-10个用户群体及其关系
   - 用户评分数据：是否包含10+条评分数据（name + value格式）
   - 流量分析数据：是否包含多维度流量来源数据
   - 能力评估数据：是否包含5-8个维度的评分数据

**⚠️ 特殊数据要求对应示例：**
```
如果内容包含用户群体关系数据（7-10个群体）：
→ 考虑使用 13-user-positioning.html（L11布局）

如果内容包含用户评分数据（10+条，每条有name和value）：
→ 考虑使用 14-user-demand-rating.html（L12布局）
→ ⚠️ 数据格式要求：
   data = [
     {name: '需求名称1', value: 8.5},
     {name: '需求名称2', value: 7.2},
     ...
   ]

如果内容包含流量来源分布数据：
→ 考虑使用 12-traffic-analysis.html（L10布局）

如果内容包含多维度能力评估数据：
→ 考虑使用 07-radar-card-layout.html（L6布局）
```

***
```markdown
当前页面分析：
- 标题: __________
- 内容类型: 概念性 / 数据性
- 观点数量: ___ 个
- 数据密度: 无 / 少量 / 中等 / 大量
- 对比关系: 并列 / 对比 / 流程 / 层级
```

---

**🎯 步骤2.1.3：对比示例文档并计算匹配度**

**读取匹配的示例文档：**

根据步骤2.1.2的分析结果，从 INDEX.md 中找到匹配的示例，并读取对应的 HTML 文件。

**必须读取的示例资源：**
- ✅ `skills/beauty-html/examples/INDEX.md` - 示例索引
- ✅ `skills/beauty-html/examples/01-cover-page.html` - 封面页示例
- ✅ `skills/beauty-html/examples/02-two-column-comparison.html` - 双列对比示例
- ✅ `skills/beauty-html/examples/03-three-column.html` - 三列并列示例
- ✅ `skills/beauty-html/examples/04-card-grid.html` - 卡片网格示例
- ✅ `skills/beauty-html/examples/05-chart-text.html` - 图表+文本示例
- ✅ `skills/beauty-html/examples/06-data-emphasis.html` - 数字强调示例
- ✅ `skills/beauty-html/examples/07-radar-card-layout.html` - 雷达图+卡片示例
- ✅ `skills/beauty-html/examples/08-table-of-contents.html` - 目录页示例(列表式)
- ✅ `skills/beauty-html/examples/09-brand-intro-page.html` - 品牌介绍页示例
- ✅ `skills/beauty-html/examples/10-toc-grid-cards.html` - 目录页示例(网格式)
- ✅ `skills/beauty-html/examples/11-chapter-overview.html` - 章节目录页示例
- ✅ `skills/beauty-html/examples/12-traffic-analysis.html` - 流量分析页示例
- ✅ `skills/beauty-html/examples/13-user-positioning.html` - 用户定位页示例(韦恩图)
- ✅ `skills/beauty-html/examples/14-user-demand-rating.html` - 用户需求评分页示例(横向柱状图) ⚠️需要用户评分数据

**匹配度计算公式：**

```
匹配度 = Σ(特征匹配权重)

特征权重：
- 观点数量匹配：40%
- 数据密度匹配：30%
- 对比关系匹配：20%
- 特殊场景匹配：10%

匹配度阈值：
- ≥80%: 高度匹配，直接使用
- 60-79%: 中度匹配，可调整后使用
- <60%: 低匹配，参考但不直接使用
```

**示例对比过程：**

```markdown
当前页面分析：
- 标题: "市场分析"
- 观点数量: 3个（市场份额、增长趋势、竞争格局）
- 数据密度: 中等（包含市场份额百分比、增长率）
- 对比关系: 并列关系

示例对比过程：

1. 读取 INDEX.md，找到匹配的示例：

   示例1: 03-three-column.html (匹配度: 85%)
   ├─ 观点数量匹配: ✓ 3个完美匹配 (40%)
   ├─ 数据密度匹配: ✓ 中等数据匹配 (30%)
   ├─ 对比关系匹配: ✓ 并列关系匹配 (20%)
   └─ 特殊场景匹配: - 无特殊场景 (0%)
   → 总计: 80% (四舍五入)

   示例2: 04-card-grid.html (匹配度: 70%)
   ├─ 观点数量匹配: ○ 3个（4-6范围内部分匹配）(30%)
   ├─ 数据密度匹配: ✓ 中等数据匹配 (30%)
   ├─ 对比关系匹配: ✓ 并列关系匹配 (20%)
   └─ 特殊场景匹配: - 无特殊场景 (0%)
   → 总计: 80%

   示例3: 05-chart-text.html (匹配度: 65%)
   ├─ 观点数量匹配: ○ 3个（建议1-3个部分匹配）(25%)
   ├─ 数据密度匹配: ✓ 中等数据匹配 (30%)
   ├─ 对比关系匹配: ○ 数据+混合部分匹配 (15%)
   └─ 特殊场景匹配: - 无特殊场景 (0%)
   → 总计: 70%

2. 选择最高匹配度示例：
   → 03-three-column.html (85%)

3. 读取示例文档：
   Read: skills/beauty-html/examples/03-three-column.html

4. 记录选择：
   选择的示例: 03-three-column.html
   匹配度: 85%
   布局类型: L3 三列布局
```

---

**🎯 步骤2.1.4：基于示例生成内容**

**生成流程：**

1. **使用示例的 HTML 结构**
   - 复制示例的 HTML 框架
   - 保持示例的 CSS 样式
   - 保持示例的布局方式

2. **替换示例的内容为实际内容**
   - 替换标题为实际标题
   - 替换描述为实际内容
   - 替换数据为实际数据

3. **保持示例的样式和布局**
   - 保持颜色方案
   - 保持间距和对齐
   - 保持响应式设计

4. **根据需要调整细节**
   - 调整文字大小
   - 调整图表配置
   - 微调布局细节

**生成输出示例：**
```markdown
基于 03-three-column.html 生成：

✓ 使用三列布局结构
✓ 使用渐变色配色（列1: 紫色, 列2: 粉色, 列3: 蓝色）
✓ 保持卡片hover效果
✓ 替换为实际的市场分析内容
✓ 添加对应的图表（饼图、折线图、柱状图）
```

---

**⚠️ 严禁跳过示例对比步骤：**

- ❌ 禁止：凭空设计布局，不读取示例
- ❌ 禁止：不进行匹配度计算
- ❌ 禁止：选择低匹配度示例
- ❌ 禁止：跳过示例文档直接生成

- ✅ 必须：读取 INDEX.md 了解所有示例
- ✅ 必须：分析当前页面特征
- ✅ 必须：对比多个示例并计算匹配度
- ✅ 必须：选择匹配度最高的示例
- ✅ 必须：读取并基于示例文档生成
- ✅ 必须：在输出中说明选择的示例和匹配度

---

**💡 示例对比选择的优势：**

1. **设计质量保证**：所有示例都是经过优化的、符合 McKinsey 设计风格的
2. **风格一致性**：所有页面都基于相同的设计语言
3. **开发效率**：直接基于示例生成，无需从零设计
4. **可扩展性**：可以轻松添加新的示例类型
5. **可维护性**：示例库统一管理和更新

**执行流程：**

```
对于每个内容区域：
├─ 查看该区域在布局中的位置
├─ 判断该区域的内容类型
├─ 选择合适的图表/图文类型
└─ 确保与整体布局协调
```

**布局区域与图表/图文的对应关系：**

**双列布局的区域划分：**
```
左列区域：
├─ 适合：观点A、数据A、图表A
└─ 选择：基于左列内容特征

右列区域：
├─ 适合：观点B、数据B、图表B
└─ 选择：基于右列内容特征
```

**三列布局的区域划分：**
```
左列区域 | 中列区域 | 右列区域
观点A     | 观点B     | 观点C
数据A     | 数据B     | 数据C
```

**图表+文本布局的区域划分：**
```
图表区域（50-70%）：
├─ 适合：数据可视化
└─ 选择：Chart.js图表

文本区域（30-50%）：
├─ 适合：关键洞察、详细说明
└─ 选择：bullet-list、emphasis-box
```

---

#### 2.0 准备阶段（⚠️ 不可跳过！）

**第一步：读取所有必读资源**
```bash
# 必须执行以下读取操作
Read: html-presentation-beautifier/skills/beauty-html/references/chart-selection-guide.md
Read: html-presentation-beautifier/skills/beauty-html/assets/CHART_EXAMPLES_INDEX.md
Read: html-presentation-beautifier/skills/beauty-html/assets/INSIGHT_VISUALIZATION_GUIDE.md
```

**第二步：制作图表选择决策表**
```
原文内容 → 识别内容类型 → 对应关键词 → 推荐图表 → 示例文件路径
────────────────────────────────────────────────────────
例如：
"平台vs个人IP对比" → 对比型 → "对比、差异、vs" → pros-cons → assets/pros-cons-example.html
"3年发展路径" → 时间序列型 → "2024、2025、2026" → timeline → assets/timeline-example.html
"马斯洛需求层次" → 层级型 → "基础、高级" → pyramid → assets/pyramid-chart-example.html
```

#### 2.1 幻灯片页面规划

#### 2.1 幻灯片页面规划

**封面页**：
- 文档主标题
- 核心主题/副标题
- 日期或版本信息（如有）

**章节封面页**：
- 每个主要章节（H1）创建独立章节封面
- 章节标题 + 简短描述

**内容页**：
- 每个H2/H3标题对应1-3页内容
- 单页内容不超过7个要点
- 数据密集型内容独立成页

**总结页**：
- 核心结论汇总
- 行动建议列表
- 下一步计划

#### 2.2 图文形式选择策略（⚠️ 必须基于chart-selection-guide.md）

**⚠️ 严格执行：基于已读取的chart-selection-guide.md进行选择**

**📊 智能布局选择机制（⚠️ 新增）**

**核心原则：根据内容结构智能选择最佳布局，充分利用横向空间**

**布局决策树：**

```
1. 判断内容类型和数据量
   ├─ 单个观点 + 无数据 → 单列布局 + 强调框
   ├─ 2-3个并列观点 → 双列/三列布局
   ├─ 4-6个并列观点 → 卡片网格布局（2x2或2x3）
   ├─ 7+个观点 → 分页或分组展示
   └─ 包含数据图表 → 图表+文本混合布局

2. 判断对比关系
   ├─ A vs B 对比 → 双列对比布局
   ├─ 多个选项对比 → 对比表格
   └─ before/after → 左右对比布局

3. 判断时间/流程
   ├─ 3-5步骤 → 横向流程图
   ├─ 时间序列 → timeline布局
   └─ 复杂流程 → 分阶段展示

4. 随机选择机制（当有多种可选布局时）
   └─ 使用Math.random()随机选择一种布局
```

**布局类型清单（12种布局类型）：**

**L1. 单列布局**
- **适用场景**：单个核心观点、深度阐述、强调框
- **内容密度**：低
- **示例**：核心结论、重要警示、关键建议

**L2. 双列布局**
- **适用场景**：2-3个并列观点、A/B对比、左右对照
- **内容密度**：中
- **示例**：方案A vs 方案B、优势 vs 劣势

**L3. 三列布局**
- **适用场景**：3个并列观点、3个选项、3个步骤
- **内容密度**：中高
- **示例**：三个核心要素、三种解决方案

**L4. 卡片网格布局**
- **适用场景**：4-6个并列观点、多个要点、特性列表
- **内容密度**：高
- **变体**：
  - 2x2网格（4个要点）
  - 2x3网格（6个要点）
  - 3x2网格（6个要点）
- **示例**：关键成功要素、产品特性、注意事项

**L5. 图表+文本布局**
- **适用场景**：包含数据可视化 + 关键洞察
- **内容密度**：中高
- **变体**：
  - 上图下文
  - 左图右文
  - 右图左文

**L6. 表格布局**
- **适用场景**：多维度对比、结构化数据
- **内容密度**：高
- **示例**：功能对比表、价格表、参数表

**L7. 混合布局**
- **适用场景**：复杂内容、多种类型混合
- **内容密度**：极高
- **组合方式**：
  - 顶部强调框 + 底部双列
  - 左侧图表 + 右侧三列
  - 上部表格 + 底部卡片

**L8. 目录页布局**
- **适用场景**：文档目录、章节导航、内容概览
- **内容密度**：中
- **变体**：
  - 列表式（08-table-of-contents.html）
  - 网格卡片式（10-toc-grid-cards.html）
  - 章节概览式（11-chapter-overview.html）
- **示例**：3+章节导航、子章节概览

**L9. 品牌介绍布局**
- **适用场景**：品牌介绍、公司简介、产品介绍
- **内容密度**：中高
- **布局特征**：左右分栏(45:55)，左侧信息列表，右侧视觉大图
- **示例**：品牌Logo + 信息点列表 + 品牌大图

**L10. 数据分析布局**
- **适用场景**：流量分析、数据报告、指标展示
- **内容密度**：高
- **布局特征**：左右分栏(60:40)，左侧图表，右侧指标网格
- **示例**：堆叠柱状图 + 关键数据指标

**L11. 用户定位布局（韦恩图）**
- **适用场景**：用户定位、用户群体关系、核心用户识别
- **内容密度**：中高
- **布局特征**：左右分栏(58:42)，左侧韦恩图(白底)侧说明(灰底)
- **数据要求**：7-10个用户群体，圆圈大小代表占比
- **示例文件**：`13-user-positioning.html`

**L12. 用户需求评分布局（横向柱状图）**
- **适用场景**：用户需求分析、产品需求优先级、评分排名展示
- **内容密度**：高
- **布局特征**：左右分栏(65:35)，左侧柱状图(白底)，右侧说明(灰底)
- **数据要求**：⚠️ 需要10+条用户评分数据（每条包含name和value）
- **示例文件**：`14-user-demand-rating.html`
- **图表类型**：ECharts横向柱状图，黄色渐变

**⚠️ 布局选择规则（严格执行）：**

**规则1：空间利用率优先**
```
✅ 优先使用横向布局（双列、三列、网格）
✅ 避免纵向长列表导致需要滚动
✅ 单屏内容不超过视口高度的80%
❌ 禁止：7+个观点使用单列纵向布局
```

**规则2：内容分组原则**
```
如果超过6个观点：
├─ 按主题分组（2-3组）
├─ 每组使用独立布局
└─ 或分页展示（每页不超过6个观点）
```

**规则3：随机选择机制**
```
当有多种可选布局时（例如：双列 vs 三列）：
├─ 识别所有适合的布局类型
├─ 使用随机算法选择一种
└─ 确保布局多样性，避免单调
```

**规则4：图表布局强制要求**
```
包含数据图表的页面：
├─ 必须使用图表+文本混合布局
├─ 图表宽度至少占50%
├─ 图表容器必须有明确宽度（CSS）
└─ 配置Chart.js的responsive: true
```

**9种内容结构类型识别与图表映射：**

**类型1：递进型**
- **关键词**：首先、其次、最后、第一步、第二步、阶段、步骤
- **推荐图表**：
  - 3-5步骤无分支 → progression（简单箭头流程）
  - 带时间标签（日期、年份）→ timeline（水平时间轴）
  - 有决策点或分支 → flowchart（流程图，带菱形决策节点）
  - 多阶段并行活动 → strategy-roadmap（泳道时间轴）
- **示例文件**：
  - `assets/flowchart-example.html`
  - `assets/timeline-example.html`
  - `assets/strategy-roadmap-example.html`

**类型2：时间序列型**
- **关键词**：年份（2024）、季度（Q1）、月份、过去、现在、未来、趋势、预测
- **推荐图表**：
  - 明确时间顺序 → timeline（带里程碑的水平时间轴）
  - 战略规划多阶段 → strategy-roadmap（多轨道时间轴）
  - 数值趋势数据 → Chart.js 'line' 图表
- **示例文件**：
  - `assets/timeline-example.html`
  - `assets/strategy-roadmap-example.html`

**类型3：并列型**
- **关键词**：同时、以及、另外、此外、包括
- **推荐图表**：
  - 2-4个等权重要点 → emphasis-box（网格强调框）
  - 5+个要点从中心展开 → mindmap（径向布局）
  - 2x2或3x3框架 → matrix（网格布局）
  - 带标签的水平对比 → mckinsey-label-bar（麦肯锡标签条形图）
- **示例文件**：
  - `assets/mindmap-example.html`
  - `assets/mckinsey-label-bar-example.html`

**类型4：层级型**
- **关键词**：基础、中级、高级、核心、外围、层次、级别
- **推荐图表**：
  - 自下而上层级（基础→顶层）→ pyramid（向上三角形金字塔）
  - 自上而下层级（最重要→细节）→ inverted-pyramid（倒金字塔）
  - 组织结构 → tree（层级框图）
- **示例文件**：
  - `assets/pyramid-chart-example.html`
  - `assets/inverted-pyramid-example.html`

**类型5：对比型**
- **关键词**：对比、差异、优劣、vs、相比、两者、A方案B方案、现状vs目标
- **推荐图表**：
  - 两种状态并排（before/after，current/target）→ comparison（左右布局）
  - 优缺点对比 → pros-cons（两列带+/-）
  - 重叠集合或共享属性 → venn-diagram（韦恩图圆形）
  - 变量对比 → slider-chart（交互式滑块对比）
- **示例文件**：
  - `assets/pros-cons-example.html`
  - `assets/venn-diagram-example.html`
  - `assets/slider-chart-example.html`

**类型6：分析框架型**
- **关键词**：SWOT、PEST、4P、5W1H、3C、波特五力、BCG矩阵
- **推荐图表**：
  - 提及"SWOT"、"优势"、"劣势"、"机会"、"威胁" → swot-analysis（2x2网格）
  - 提及"市场"、"产品"、"增长策略" → ansoff-matrix（安索夫矩阵）
  - 提及What、Why、Who、When、Where、How → 5w1h（六边形布局）
  - 提及"竞争"、"定位"、"市场地位" → competitive-4box（定位矩阵）
  - 提及"基本"、"期望"、"魅力"、"满意度" → kano-model（满意度矩阵）
- **示例文件**：
  - `assets/swot-analysis-example.html`
  - `assets/ansoff-matrix-example.html`
  - `assets/competitive-4box-example.html`
  - `assets/5w1h-example.html`
  - `assets/kano-model-example.html`

**类型7：转化流程型**
- **关键词**：转化、漏斗、筛选、流失、通过率、转化率、阶段
- **推荐图表**：
  - 逐阶段筛选且数量递减 → funnel-chart（倒三角阶段）
  - 有流程的价值创造过程 → value-stream（带增值的水平流）
  - 顺序增减 → waterfall-chart（带桥接的条形图）
- **示例文件**：
  - `assets/funnel-chart-example.html`
  - `assets/value-stream-example.html`

**类型8：循环型**
- **关键词**：循环、迭代、反馈、持续、闭环、反复、优化、改进
- **推荐图表**：
  - 带反馈的闭环流程 → cycle（带箭头的圆形）
  - 有阶段的迭代过程 → circular-flow（带标签段的圆形）
  - 循环数据对比 → polar-chart（Chart.js polarArea）
- **示例文件**：
  - `assets/polar-chart-example.html`

**类型9：因果/问题解决型**
- **关键词**：原因、结果、问题、解决方案、根源、导致、引起、因为、所以
- **推荐图表**：
  - 问题在左，解决方案在右 → problem-solution（带箭头的双列）
  - 80/20法则或关键因素 → pareto-chart（条形图+折线图）
  - 根本原因分析 → fishbone（因果图）
  - KPI测量 → gauge-chart（速度计）
- **示例文件**：
  - `assets/problem-solution-example.html`
  - `assets/pareto-chart-example.html`
  - `assets/gauge-chart-example.html`

**⚠️ 重要规则**：

1. **严禁使用纯文本项目符号列表**来呈现结论/见解
2. **必须为概念性内容分配可视化类型**
3. **可视化匹配内容结构**，而非仅考虑美观
4. **引用示例文件**以获取实施指导
5. **使用McKinsey配色方案**进行所有可视化

**数据可视化选择（基于Chart.js）：**

```
看"对比" → 条形图/柱状图
  - 类别比较（收入、成本、市场份额）
  - 横向对比（A vs B）
  - 时间点对比（今年 vs 去年）

看"趋势" → 折线图/面积图
  - 时间序列数据
  - 连续变化趋势
  - 增长/下降轨迹

看"占比" → 饼图/环形图/堆叠柱状图
  - 市场份额（≤5个主体）
  - 预算分配
  - 构成分析

看"分布" → 散点图/箱型图
  - 数据分布模式
  - 异常值识别
  - 相关性分析

看"排名" → 横向条形图
  - 按指标排序
  - Top N列表
  - 优先级展示
```

#### 2.3 页面布局设计

**单列布局**：
- 适用于：要点列表、单一主题
- 内容密度：中等

**双列布局**：
- 适用于：对比分析、左图右文
- 内容密度：高

**三列布局**：
- 适用于：并列要点、多个数据点
- 内容密度：很高

**中心聚焦**：
- 适用于：核心结论、强调信息
- 内容密度：低但突出

**上/下分栏**：
- 适用于：上图下文、上文下表
- 内容密度：可变

**输出产物**：
- 幻灯片页面规划表（包含每页标题、内容要点、布局类型）
- 图表类型分配表（哪些数据用什么图表）
- 视觉元素清单（需要的图标、插图类型）

**验证标准**：
- [ ] 每页信息量适中（不超过7个要点）
- [ ] 图表类型选择合理
- [ ] 布局清晰易读
- [ ] 视觉层次分明
- [ ] 所有原文内容都有对应的呈现方式

---

### 步骤 3️⃣：转化为 McKinsey 商业风格 HTML

**⚠️ 必须严格参考HTML生成准则和模板！**

**目标**：生成符合 McKinsey/BCG 标准的专业 HTML 幻灯片。

**⚠️ 强制要求：必须读取并参考以下资源**

#### 必读资源1：最佳实践指南
```
文件路径：html-presentation-beautifier/skills/beauty-html/references/best-practices.md

必须使用Read工具读取，严格遵循：
- 内容完整性原则（不总结、不篡改、不添加）
- 信息层次原则
- 数据可视化原则
- 颜色使用原则
- 字体排版原则
- 布局间距原则
```

#### 必读资源2：McKinsey设计系统
```
文件路径：html-presentation-beautifier/skills/beauty-html/references/mckinsey-design-system.md

必须使用Read工具读取，严格遵循：
- 完整的配色方案（CSS变量定义）
- 排版层次规范
- 组件样式规范
- 响应式设计规范
```

#### 必读资源3：模板使用指南
```
文件路径：html-presentation-beautifier/skills/beauty-html/references/template-guide.md

必须使用Read工具读取，学习：
- 完整HTML模板结构
- 占位符使用方法
- 导航功能实现
- 图表集成方法
```

#### 必读资源4：完整演示文稿模板
```
文件路径：html-presentation-beautifier/skills/beauty-html/assets/presentation-template.html

必须使用Read工具读取，作为：
- HTML结构的基础模板
- CSS样式的参考标准
- JavaScript功能的实现范例
```

#### 必读资源5：模板使用指南
```
文件路径：html-presentation-beautifier/skills/beauty-html/assets/TEMPLATE_USAGE_GUIDE.md

必须使用Read工具读取，了解：
- 模板的各个部分说明
- 如何修改和定制模板
- 最佳实践建议
```

**执行要求**：

#### 3.0 准备阶段（⚠️ 不可跳过！）

**第一步：读取所有必读资源**
```bash
# 必须执行以下读取操作
Read: html-presentation-beautifier/skills/beauty-html/references/best-practices.md
Read: html-presentation-beautifier/skills/beauty-html/references/mckinsey-design-system.md
Read: html-presentation-beautifier/skills/beauty-html/references/template-guide.md
Read: html-presentation-beautifier/skills/beauty-html/assets/presentation-template.html
Read: html-presentation-beautifier/skills/beauty-html/assets/TEMPLATE_USAGE_GUIDE.md
```

**第二步：基于模板创建HTML文件**
```
1. 从 presentation-template.html 复制基础结构
2. 替换所有占位符 {{PLACEHOLDER}} 为实际内容
3. 根据步骤2选择的图表类型，从 assets/ 对应示例文件复制代码
4. 严格遵循 best-practices.md 和 mckinsey-design-system.md 的规范
```

#### 3.1 设计系统应用（严格遵循mckinsey-design-system.md）

#### 3.1 设计系统应用

**McKinsey 标准配色方案**：
```css
/* 必须严格遵循以下配色 */
--color-bg: #FFFFFF                    /* 纯白背景 */
--color-text-primary: #000000          /* 纯黑主文字 */
--color-text-secondary: #333333        /* 深灰正文 */
--color-accent-primary: #F85d42        /* 橙色强调 */
--color-accent-secondary: #74788d      /* 灰蓝辅助 */
--color-blue: #556EE6                  /* 深蓝数据 */
--color-green: #34c38f                 /* 绿色成功 */
--color-light-blue: #50a5f1            /* 浅蓝中性 */
--color-yellow: #f1b44c                /* 黄色警告 */
```

**排版层次规范**：
```css
/* 标题系统 */
.title-main {
  font-size: 64px;
  font-weight: 700;
  color: #000000;
  line-height: 1.2;
}

.title-section {
  font-size: 48px;
  font-weight: 700;
  color: #000000;
  border-bottom: 3px solid #F85d42;
}

.title-slide {
  font-size: 42px;
  font-weight: 700;
  color: #000000;
  margin-bottom: 30px;
}

.subtitle {
  font-size: 28-36px;
  font-weight: 600;
  color: #F85d42;
}

/* 正文系统 */
.body-primary {
  font-size: 20px;
  font-weight: 400;
  color: #333333;
  line-height: 1.6;
}

.body-secondary {
  font-size: 16px;
  font-weight: 400;
  color: #74788d;
  line-height: 1.5;
}

/* 图表标签 */
.chart-label {
  font-size: 14px;
  font-weight: 500;
  color: #333333;
}
```

#### 3.2 页面结构实现

**标准页面结构**：
```html
<div class="slide">
  <!-- 页面标题 -->
  <h2 class="slide-title">页面标题</h2>

  <!-- 内容区域 -->
  <div class="slide-content">
    <!-- 根据步骤2选择的布局方式 -->
  </div>
</div>
```

**布局模板**：

1. **要点列表布局**：
```html
<ul class="bullet-list">
  <li>要点1</li>
  <li>要点2</li>
  <li>要点3</li>
</ul>
```

2. **双列对比布局**：
```html
<div class="two-column-layout">
  <div class="column-left">
    <h3>A方案</h3>
    <ul>...</ul>
  </div>
  <div class="column-right">
    <h3>B方案</h3>
    <ul>...</ul>
  </div>
</div>
```

3. **图表+文本布局**：
```html
<div class="chart-text-layout">
  <div class="chart-container">
    <canvas id="chart1"></canvas>
  </div>
  <div class="key-insights">
    <h3>关键发现</h3>
    <ul>...</ul>
  </div>
</div>
```

4. **强调框布局**：
```html
<div class="emphasis-box">
  <div class="emphasis-icon">💡</div>
  <div class="emphasis-content">
    <h3>核心结论</h3>
    <p>详细说明...</p>
  </div>
</div>
```

5. **三列布局（⚠️ 新增）**：
```html
<div class="three-column-layout">
  <div class="column">
    <h3>要点1</h3>
    <p>内容1...</p>
  </div>
  <div class="column">
    <h3>要点2</h3>
    <p>内容2...</p>
  </div>
  <div class="column">
    <h3>要点3</h3>
    <p>内容3...</p>
  </div>
</div>
```

6. **卡片网格布局（⚠️ 新增）**：
```html
<div class="highlight-cards">
  <div class="highlight-card">
    <h4>卡片1标题</h4>
    <div class="number">100</div>
    <p>卡片1内容</p>
  </div>
  <div class="highlight-card">
    <h4>卡片2标题</h4>
    <div class="number">200</div>
    <p>卡片2内容</p>
  </div>
  <div class="highlight-card">
    <h4>卡片3标题</h4>
    <div class="number">300</div>
    <p>卡片3内容</p>
  </div>
  <div class="highlight-card">
    <h4>卡片4标题</h4>
    <div class="number">400</div>
    <p>卡片4内容</p>
  </div>
</div>
```

#### 3.3 CSS关键修复（⚠️ 新增 - 解决图表宽度为0的问题）

**⚠️ 严格执行以下CSS修复，确保图表正常显示**

**修复1：图表容器CSS（必须包含）**
```css
/* Chart Container - 必须包含这些样式 */
.chart-container {
  position: relative;
  width: 100% !important;              /* ⚠️ 强制100%宽度 */
  min-width: 300px !important;         /* ⚠️ 最小宽度300px */
  max-width: 100% !important;          /* ⚠️ 最大宽度100% */
  height: 500px;                       /* 固定高度 */
  margin: 40px 0;                      /* 上下边距 */
  background: white;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  box-sizing: border-box;              /* ⚠️ 包含padding在宽度内 */
}

/* Chart Canvas - 必须包含 */
.chart-container canvas {
  width: 100% !important;              /* ⚠️ 强制100%宽度 */
  height: 100% !important;             /* ⚠️ 强制100%高度 */
  display: block !important;           /* ⚠️ 块级显示 */
}

/* 确保父容器也有宽度 */
.slide-content {
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
}
```

**修复2：Chart.js配置（必须包含）**
```javascript
// ⚠️ 每个图表都必须包含这些配置
const chartOptions = {
  responsive: true,                    // ⚠️ 必须为true
  maintainAspectRatio: false,          // ⚠️ 必须为false
  plugins: {
    legend: {
      position: 'bottom',
      labels: {
        font: {
          size: 14
        }
      }
    },
    title: {
      display: true,
      text: '图表标题',
      font: {
        size: 18,
        weight: 'bold'
      },
      padding: {
        bottom: 20
      }
    }
  },
  scales: {
    x: {
      ticks: {
        font: {
          size: 12
        }
      }
    },
    y: {
      beginAtZero: true,
      ticks: {
        font: {
          size: 12
        }
      }
    }
  }
};

// 创建图表
new Chart(ctx, {
  type: 'bar',  // 或 'line', 'doughnut' 等
  data: chartData,
  options: chartOptions
});
```

**修复3：布局CSS优化（充分利用横向空间）**
```css
/* Three Column Layout - 三列布局 */
.three-column-layout {
  display: grid;
  grid-template-columns: repeat(3, 1fr);  /* ⚠️ 三等分 */
  gap: 30px;
  margin: 40px 0;
}

.three-column-layout .column {
  background: #f9f9f9;
  padding: 25px;
  border-radius: 8px;
  border-left: 4px solid var(--color-accent-primary);
}

/* Highlight Cards Grid - 卡片网格 */
.highlight-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));  /* ⚠️ 自适应列数 */
  gap: 25px;
  margin: 40px 0;
}

.highlight-card {
  background: white;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  border-top: 4px solid var(--color-accent-primary);
  text-align: center;
}

.highlight-card .number {
  font-size: 42px;
  font-weight: 700;
  color: var(--color-accent-primary);
  margin: 15px 0;
}

/* Chart + Text Layout - 图表文本混合布局 */
.chart-text-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;  /* 左右等分 */
  gap: 40px;
  align-items: center;
  margin: 40px 0;
}

/* 响应式调整 */
@media (max-width: 1024px) {
  .three-column-layout {
    grid-template-columns: 1fr;      /* 平板/手机改为单列 */
  }

  .chart-text-layout {
    grid-template-columns: 1fr;      /* 平板/手机改为纵向 */
  }

  .chart-container {
    height: 400px;                   /* 降低高度 */
    padding: 20px;
  }
}
```

**⚠️ 图表显示问题排查清单：**

**问题：图表宽度为0（width="0"）**
```
✅ 检查项1：.chart-container是否有width: 100%
✅ 检查项2：canvas是否有width: 100% !important
✅ 检查项3：Chart.js配置中responsive: true
✅ 检查项4：Chart.js配置中maintainAspectRatio: false
✅ 检查项5：父容器.slide-content是否有max-width
✅ 检查项6：是否在DOMContentLoaded之后初始化图表
```

**问题：图表显示过小或过大**
```
✅ 检查项1：.chart-container的height是否合理（400-500px）
✅ 检查项2：是否设置了maintainAspectRatio: false
✅ 检查项3：父容器宽度是否受限
```

**问题：多个图表只有部分显示**
```
✅ 检查项1：每个图表的canvas ID是否唯一
✅ 检查项2：所有图表是否在DOMContentLoaded中初始化
✅ 检查项3：每个图表的变量名是否唯一
```

#### 3.4 Token限制处理策略（分批生成HTML）

**⚠️ 当HTML文件过大无法一次生成完整时：**

```
正确做法（分批生成）：

阶段1：生成HTML结构框架
├─ 生成 <!DOCTYPE html> 到 <nav class="navbar"> 导航栏
├─ 内联所有CSS样式（完整的<style>标签）
├─ 生成幻灯片容器开始标签 <div class="presentation-container">
└─ 输出："阶段1完成 - HTML框架和CSS已生成（约30%）
       请输入'继续'以生成幻灯片内容"

【等待用户输入"继续"】

阶段2：生成前半部分幻灯片
├─ 生成幻灯片 1-10（封面页到第10页）
├─ 每页包含完整的HTML结构
├─ 确保所有内容和数据准确
└─ 输出："阶段2完成 - 已生成前10页幻灯片（60%）
       请输入'继续'以生成剩余幻灯片"

【等待用户输入"继续"】

阶段3：生成后半部分幻灯片
├─ 生成幻灯片 11-20（第11页到结束页）
├─ 每页包含完整的HTML结构
├─ 确保所有内容和数据准确
└─ 输出："阶段3完成 - 已生成后10页幻灯片（90%）
       请输入'继续'以生成脚本和结束标签"

【等待用户输入"继续"】

阶段4：生成JavaScript和结束标签
├─ 生成 <script> 标签开始
├─ 生成导航逻辑
├─ 生成所有图表初始化代码
├─ 生成事件监听器
├─ 生成 </script> 和 </body></html>
└─ 输出："阶段4完成 - HTML文件100%生成完成
       文件已保存"
```

**关键规则：**

1. **保持完整性**：
   - ✅ 每个阶段的代码都必须是完整的语法单元
   - ✅ CSS必须在一个阶段内完整生成
   - ✅ 每个幻灯片的HTML必须完整
   - ✅ JavaScript必须完整

2. **可衔接性**：
   - ✅ 使用明确的阶段标记
   - ✅ 每个阶段结束说明进度百分比
   - ✅ 提示用户输入"继续"
   - ✅ 确保下一阶段可以无缝衔接

3. **验证点**：
   - ✅ 每个阶段完成后验证该部分的内容完整性
   - ✅ 检查是否有截断的标签
   - ✅ 确认下一阶段的起始位置

**❌ 禁止做法（偷工减料）：**

```
错误做法1：压缩CSS
├─ 只生成部分样式
└─ ❌ 导致页面显示异常

错误做法2：省略幻灯片
├─ 只生成前10页，后面用省略号
└─ ❌ 丢失内容

错误做法3：简化图表
├─ 用文本描述代替图表代码
└─ ❌ 无法正常显示

错误做法4：不告诉用户要继续
├─ 生成一部分就停止
└─ ❌ 用户不知道发生了什么

错误做法5：一次生成失败后就放弃
├─ 说"由于限制无法完成"
└─ ❌ 任务未完成
```

**分批生成的示例模板：**

```bash
# 阶段1输出模板
阶段1/4：HTML框架和CSS样式生成中...

已生成：
✅ DOCTYPE 和 HTML 根元素
✅ head 标签和 meta 设置
✅ Chart.js CDN 引用
✅ 完整的 CSS 样式（约600行）
✅ 导航栏结构

进度：30%完成
【请输入"继续"以生成前半部分幻灯片】

# 阶段2输出模板
阶段2/4：生成前半部分幻灯片...

已生成：
✅ 幻灯片 1：封面页
✅ 幻灯片 2：章节封面
✅ 幻灯片 3-10：内容页（包含所有图表和数据）

进度：60%完成
【请输入"继续"以生成后半部分幻灯片】

# 阶段3输出模板
阶段3/4：生成后半部分幻灯片...

已生成：
✅ 幻灯片 11-18：剩余内容页
✅ 幻灯片 19：总结页
✅ 幻灯片 20：结束页

进度：90%完成
【请输入"继续"以生成JavaScript和结束标签】

# 阶段4输出模板
阶段4/4：生成JavaScript和完成文件...

已生成：
✅ 导航逻辑（showSlide, nextSlide, previousSlide）
✅ 键盘控制
✅ 全屏切换
✅ 所有图表初始化代码（6个图表）
✅ 事件监听器
✅ 结束标签（</script></body></html>）

✅ 任务100%完成！
文件已保存至：/path/to/output.html
```

**处理图表代码过长的情况：**

```
如果某个图表的初始化代码特别长：

方案1：跨阶段生成
├─ 阶段2：生成前3个图表的初始化代码
└─ 阶段4：生成后3个图表的初始化代码

方案2：单独提示继续
├─ 生成前2个图表后
└─ 输出："图表代码较长，请输入'继续'以生成剩余图表"
```

**确保文件可用的关键检查：**

每个阶段完成后必须检查：
- [ ] HTML标签是否闭合（如果该阶段应该闭合）
- [ ] CSS语法是否正确
- [ ] 数据是否准确
- [ ] 下次生成可以从哪里继续
- [ ] 用户是否知道要输入"继续"

**⚠️ 强制要求：从步骤2选择的图表类型，必须读取对应的示例文件**

**实施流程：**

**第一步：读取对应图表的示例文件**
```
根据步骤2选择的图表类型，读取对应的示例文件：

例如：
- 选择了pyramid → Read: assets/pyramid-chart-example.html
- 选择了timeline → Read: assets/timeline-example.html
- 选择了swot-analysis → Read: assets/swot-analysis-example.html
- 选择了funnel-chart → Read: assets/funnel-chart-example.html
...以此类推
```

**第二步：从示例文件中复制代码**
```
必须复制以下内容：

1. CSS样式（从<style>标签中）
   - 复制该图表特定的CSS类
   - 复制McKinsey配色变量（如尚未包含）
   - 复制响应式样式

2. HTML结构（从<body>中的图表容器）
   - 复制图表容器结构
   - 复制所有必需的类名和ID
   - 保持DOM层次结构

3. JavaScript代码（从<script>标签中）
   - 复制Chart.js配置（如使用Chart.js）
   - 复制自定义渲染逻辑（如纯CSS图表）
   - 复制交互处理代码
```

**第三步：定制化修改**
```
将示例代码中的占位数据替换为实际数据：

1. 修改数据源
   - 替换labels为实际标签
   - 替换data为实际数值
   - 替换title为实际标题

2. 调整样式（如需要）
   - 根据内容量调整容器高度
   - 根据数据量调整图表尺寸
   - 保持McKinsey配色不变

3. 集成到幻灯片
   - 将图表代码插入到对应幻灯片的内容区
   - 确保与导航系统兼容
   - 测试响应式行为
```

**示例：复制金字塔图代码**

```bash
# 1. 读取示例文件
Read: assets/pyramid-chart-example.html

# 2. 从文件中提取以下部分：

CSS部分：
```css
/* 从 <style> 标签中复制 */
.pyramid-container {
    position: relative;
    width: 100%;
    max-width: 600px;
    margin: 40px auto;
}

.pyramid-level {
    position: relative;
    margin: 0 auto;
    text-align: center;
    color: white;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
}

.pyramid-top {
    width: 200px;
    height: 0;
    padding-bottom: 173px; /* 等边三角形比例 */
    background: #F85d42;
    clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
}

/* ... 其他层级样式 ... */
```

HTML部分：
```html
<!-- 图表容器 -->
<div class="pyramid-container">
    <div class="pyramid-level pyramid-top">
        <span class="pyramid-text">顶层内容</span>
    </div>
    <div class="pyramid-level pyramid-middle">
        <span class="pyramid-text">中层内容</span>
    </div>
    <div class="pyramid-level pyramid-bottom">
        <span class="pyramid-text">底层内容</span>
    </div>
</div>
```

# 3. 修改为实际内容
将"顶层内容"、"中层内容"、"底层内容"替换为实际数据
```

**⚠️ 禁止事项**：
- ❌ 不要凭记忆编写图表代码
- ❌ 不要使用AI生成的图表代码
- ❌ 不要随意修改McKinsey配色
- ❌ 不要省略CSS样式细节
- ❌ 不要忽略响应式样式

**✅ 必须做到**：
- ✅ 每个图表都从assets/示例文件复制代码
- ✅ 严格保持McKinsey设计风格
- ✅ 确保所有样式都已复制
- ✅ 测试图表在不同屏幕尺寸下的表现
- ✅ 验证图表可访问性（alt标签、aria属性等）

**常用图表示例文件快速索引**：
```
层级型：
  - assets/pyramid-chart-example.html
  - assets/inverted-pyramid-example.html

时间序列型：
  - assets/timeline-example.html
  - assets/strategy-roadmap-example.html

对比型：
  - assets/pros-cons-example.html
  - assets/venn-diagram-example.html
  - assets/slider-chart-example.html

分析框架型：
  - assets/swot-analysis-example.html
  - assets/ansoff-matrix-example.html
  - assets/competitive-4box-example.html
  - assets/5w1h-example.html
  - assets/kano-model-example.html

流程型：
  - assets/flowchart-example.html
  - assets/funnel-chart-example.html
  - assets/value-stream-example.html

其他：
  - assets/mindmap-example.html
  - assets/gauge-chart-example.html
  - assets/pareto-chart-example.html
  - assets/problem-solution-example.html
  - assets/swimlane-example.html
```

**Chart.js图表实现（数据图表专用）**：

```javascript
// 从对应示例文件复制Chart.js配置
// 例如：bar-chart、line-chart、doughnut-chart等

new Chart(ctx, {
  type: 'bar', // 根据数据类型选择
  data: {
    labels: ['类别A', '类别B', '类别C'], // 实际数据
    datasets: [{
      label: '数据系列',
      data: [10, 20, 30], // 实际数值
      backgroundColor: ['#F85d42', '#556EE6', '#34c38f'] // McKinsey配色
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
          font: { size: 14 },
          color: '#333333'
        }
      },
      title: {
        display: true,
        text: '图表标题', // 实际标题
        font: { size: 18, weight: 'bold' },
        color: '#000000',
        padding: 20
      },
      tooltip: {
        backgroundColor: 'rgba(0, 0, 0, 0.8)',
        padding: 12,
        titleFont: { size: 14 },
        bodyFont: { size: 13 }
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          color: '#333333',
          font: { size: 12 }
        },
        grid: {
          color: '#e0e0e0',
          drawBorder: false
        }
      },
      x: {
        ticks: {
          color: '#333333',
          font: { size: 12 }
        },
        grid: {
          display: false
        }
      }
    }
  }
});
```

**输出产物**：
- 完整的 HTML 页面代码
- 内联 CSS 样式（遵循 McKinsey 配色）
- JavaScript 图表配置代码

**验证标准**：
- [ ] 所有幻灯片使用统一配色方案
- [ ] 排版层次清晰一致
- [ ] 图表样式专业美观
- [ ] 页面布局符合设计规范
- [ ] 所有内容正确渲染

---

### 步骤 4️⃣：合并为单个 HTML 文件

**目标**：将所有幻灯片、样式、脚本合并为一个独立的 HTML 文件。

**执行要求**：

#### 4.1 文件结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>演示文稿标题</title>

  <!-- 外部依赖：仅允许 Chart.js CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>

  <!-- 内联样式：所有 CSS 必须内联 -->
  <style>
    /* McKinsey 风格 CSS（约500-600行） */
    * { margin: 0; padding: 0; box-sizing: border-box; }
    /* ... 完整样式定义 ... */
  </style>
</head>
<body>
  <!-- 导航栏 -->
  <nav class="navbar">
    <h1>演示文稿标题</h1>
    <div class="nav-controls">
      <button class="nav-btn" onclick="previousSlide()">← 上一页</button>
      <span class="slide-counter">
        <span id="currentSlide">1</span> / <span id="totalSlides">N</span>
      </span>
      <button class="nav-btn" onclick="nextSlide()">下一页 →</button>
    </div>
  </nav>

  <!-- 幻灯片容器 -->
  <div class="presentation-container">
    <!-- 幻灯片 1：封面 -->
    <div class="slide title-slide active">
      <h1 class="title">主标题</h1>
      <p class="subtitle">副标题</p>
    </div>

    <!-- 幻灯片 2：章节封面 -->
    <div class="slide section-slide">
      <h1 class="title">章节标题</h1>
    </div>

    <!-- 幻灯片 3-N：内容页 -->
    <div class="slide">
      <h2 class="slide-title">页面标题</h2>
      <div class="slide-content">
        <!-- 内容：列表、图表、表格等 -->
      </div>
    </div>

    <!-- ... 更多幻灯片 ... -->
  </div>

  <!-- 全屏按钮 -->
  <button class="fullscreen-btn" onclick="toggleFullscreen()">⛶</button>

  <!-- 内联脚本：所有 JavaScript 必须内联 -->
  <script>
    // 导航逻辑
    let currentSlide = 0;
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;

    function showSlide(n) {
      // 切换幻灯片逻辑
    }

    function nextSlide() {
      showSlide(currentSlide + 1);
    }

    function previousSlide() {
      showSlide(currentSlide - 1);
    }

    // 键盘控制
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === ' ') {
        nextSlide();
      } else if (e.key === 'ArrowLeft') {
        previousSlide();
      } else if (e.key === 'Escape') {
        if (document.fullscreenElement) {
          document.exitFullscreen();
        }
      }
    });

    // 全屏切换
    function toggleFullscreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
      } else {
        document.exitFullscreen();
      }
    }

    // 图表初始化
    function initializeCharts() {
      // 所有 Chart.js 图表初始化代码
      // 严格遵循步骤3中定义的图表配置
    }

    // 页面加载完成后初始化
    document.addEventListener('DOMContentLoaded', () => {
      initializeCharts();
    });
  </script>
</body>
</html>
```

#### 4.2 合并检查清单

- [ ] 所有 CSS 样式已内联到 `<style>` 标签
- [ ] 所有 JavaScript 代码已内联到 `<script>` 标签
- [ ] Chart.js 通过 CDN 引用（唯一允许的外部依赖）
- [ ] 所有幻灯片已包含在 `.presentation-container` 中
- [ ] 幻灯片总数 (`totalSlides`) 正确更新
- [ ] 导航控件完整且功能正常
- [ ] 全屏按钮已添加

#### 4.3 文件大小优化

- 压缩 CSS（去除空格和注释）
- 优化 JavaScript（避免重复代码）
- 图表数据使用 JSON 格式（最小化）
- 总文件大小控制在合理范围（通常 < 500KB）

**输出产物**：
- 单个完整的 HTML 文件
- 文件命名：`原文件名_beautified.html`

**验证标准**：
- [ ] 文件可独立在浏览器中打开
- [ ] 无外部文件依赖（除 Chart.js CDN）
- [ ] 所有幻灯片完整显示
- [ ] 导航功能正常工作
- [ ] 图表正确渲染
- [ ] 响应式设计生效

---

### 步骤 5️⃣：代码内容审核检验

**⚠️ 最关键步骤！必须严格执行！**

**目标**：全面检查生成的 HTML 演示文稿，确保质量和完整性。

**执行要求**：

#### 5.1 🔍 资源使用验证（必须100%通过）

**⚠️ 验证步骤2和步骤3是否正确读取并使用了skill资源**

**步骤2资源使用验证：**

**验证方法1：检查图表选择是否基于chart-selection-guide.md**
```
□ 是否读取了 chart-selection-guide.md？
□ 是否识别了内容结构类型（9种类型之一）？
□ 是否根据决策树选择了对应的图表？
□ 是否记录了选择理由（关键词匹配）？

如果否 → 返回步骤2重新执行
```

**验证方法2：检查是否参考了图表示例文件**
```
□ 是否读取了 CHART_EXAMPLES_INDEX.md？
□ 每个选择的图表是否都有对应的示例文件？
□ 是否从示例文件中复制了代码？
□ 图表类型与内容是否匹配？

如果否 → 返回步骤2重新执行
```

**验证方法3：检查是否阅读了观点可视化指南**
```
□ 是否读取了 INSIGHT_VISUALIZATION_GUIDE.md？
□ 是否根据观点类型选择了可视化方式？
□ 是否避免了纯文本项目符号列表？

如果否 → 返回步骤2重新执行
```

**步骤3资源使用验证：**

**验证方法1：检查是否基于最佳实践生成**
```
□ 是否读取了 best-practices.md？
□ HTML结构是否符合语义化要求？
□ CSS是否遵循了设计原则？
□ 是否保持了内容完整性（不总结、不篡改）？

如果否 → 返回步骤3重新执行
```

**验证方法2：检查是否遵循了McKinsey设计系统**
```
□ 是否读取了 mckinsey-design-system.md？
□ 是否使用了定义的配色方案？
□ 字体大小是否符合规范？
□ 间距是否符合标准？

如果否 → 返回步骤3重新执行
```

**验证方法3：检查是否使用了模板**
```
□ 是否读取了 presentation-template.html？
□ HTML结构是否基于模板？
□ 导航功能是否完整？
□ 是否包含了模板中的所有必要组件？

如果否 → 返回步骤3重新执行
```

**验证方法4：检查图表代码来源**
```
□ 每个图表的代码是否来自assets/示例文件？
□ 是否完整复制了CSS、HTML、JavaScript？
□ 是否根据实际数据进行了定制？
□ McKinsey配色是否保持一致？

如果否 → 返回步骤3重新执行
```

**资源使用检查清单：**
```
步骤2 - 幻灯片设计阶段：
□ 已读取：references/chart-selection-guide.md
□ 已读取：assets/CHART_EXAMPLES_INDEX.md
□ 已读取：assets/INSIGHT_VISUALIZATION_GUIDE.md
□ 已制作：图表选择决策表（内容类型 → 关键词 → 推荐图表 → 示例文件）
□ 已记录：每个图表的选择理由
□ 已复制：对应示例文件的代码

步骤3 - HTML生成阶段：
□ 已读取：references/best-practices.md
□ 已读取：references/mckinsey-design-system.md
□ 已读取：references/template-guide.md
□ 已读取：assets/presentation-template.html
□ 已读取：assets/TEMPLATE_USAGE_GUIDE.md
□ 已复制：所有选中图表的示例代码
□ 已应用：McKinsey配色和排版规范
□ 已保持：内容完整性（零篡改、零遗漏）

❌ 发现任何资源未读取或未使用 → 立即返回对应步骤重新执行
```

**⚠️ 回退触发条件：**
```
以下任一情况发生，必须回退：

1. 步骤2未读chart-selection-guide.md
   → 返回步骤2，读取资源后重新选择图表

2. 步骤2选择的图表与chart-selection-guide.md不符
   → 返回步骤2，根据指南重新选择

3. 步骤2未从assets/示例文件复制代码
   → 返回步骤2，读取示例文件后复制代码

4. 步骤3未读best-practices.md
   → 返回步骤3，读取资源后重新生成HTML

5. 步骤3生成的HTML不符合mckinsey-design-system.md规范
   → 返回步骤3，根据规范重新生成

6. 步骤3未基于presentation-template.html
   → 返回步骤3，使用模板重新生成
```


#### 5.1.5 🔍 Token限制处理验证（新增）

**⚠️ 验证是否正确处理了 token 限制问题**

**检查AI是否因为 token 限制而偷工减料：**

**验证项目1：是否使用了"继续"机制**
```
□ 是否在任何阶段使用了"继续"分批处理？
□ 是否明确说明了进度百分比？
□ 是否提示用户输入"继续"？
□ 分批处理后是否最终完成了100%的内容？

如果否 → 可能存在偷工减料，需要检查：
- 是否跳过了某些资源读取？
- 是否省略了某些内容生成？
- 是否使用了简化版而非完整版？
```

**验证项目2：资源读取是否完整**
```
□ 步骤2读取的3个资源是否完整读取？
□ 步骤3读取的5个资源是否完整读取？
□ 如果资源文件很长，是否分批读取？
□ 是否有"请输入'继续'以读取剩余内容"的提示？

如果否 → 说明AI为了省token而跳过了资源
→ 返回步骤2或步骤3重新执行
```

**验证项目3：内容生成是否完整**
```
□ 是否所有章节都已生成？
□ 是否所有图表都已生成？
□ 是否所有数据都已包含？
□ HTML文件是否是完整的（标签闭合）？
□ JavaScript是否完整（无语法错误）？

如果否 → 说明AI为了省token而压缩了内容
→ 返回步骤3重新生成完整内容
```

**Token限制处理的验收标准：**

✅ **合格标准：**
- 遇到 token 限制时，明确说明并使用"继续"机制
- 分批处理但最终100%完成所有内容
- 所有资源都已完整读取（可能分批）
- 最终生成的HTML文件完整可用
- 没有因为 token 限制而丢失任何内容

❌ **不合格标准（需要回退）：**
- 为了省 token 而跳过资源读取
- 为了省 token 而简化内容
- 为了省 token 而使用摘要代替完整代码
- 分批生成但最终内容不完整
- 没有提示用户"继续"导致任务中止

**正确的"继续"机制示例：**
```
✅ 阶段1完成：已读取资源前半部分
【请输入"继续"以读取剩余部分】

用户输入："继续"

✅ 阶段2完成：资源100%读取完成
【已进入下一步骤】
```

#### 5.1.6 🔍 图表显示和布局优化验证（⚠️ 新增）

**⚠️ 验证图表是否正常显示，布局是否充分利用横向空间**

**检查AI是否正确处理了图表显示和布局优化：**

**验证项目1：图表容器CSS是否正确**
```
□ .chart-container是否包含width: 100% !important？
□ .chart-container是否包含min-width: 300px !important？
□ .chart-container是否包含max-width: 100% !important？
□ canvas元素是否包含width: 100% !important？
□ canvas元素是否包含height: 100% !important？
□ .chart-container是否包含box-sizing: border-box？

如果否 → 图表宽度可能为0，返回步骤3修复CSS
```

**验证项目2：Chart.js配置是否正确**
```
□ 所有图表是否设置了responsive: true？
□ 所有图表是否设置了maintainAspectRatio: false？
□ 图表是否有合理的height（400-500px）？
□ 图表是否在DOMContentLoaded之后初始化？
□ 每个图表的canvas ID是否唯一？
□ 每个图表的变量名是否唯一？

如果否 → 图表无法正常显示，返回步骤3修复配置
```

**验证项目3：布局是否充分利用横向空间**
```
□ 是否优先使用横向布局（双列、三列、网格）？
□ 是否避免纵向长列表导致需要滚动？
□ 单屏内容是否不超过视口高度的80%？
□ 4-6个观点是否使用卡片网格布局？
□ 2-3个观点是否使用双列或三列布局？

如果否 → 布局不够优化，返回步骤2或3优化布局
```

**验证项目4：随机选择机制是否正确应用**
```
□ 当有多种可选布局时，是否使用了随机选择？
□ 布局选择是否有足够的多样性（避免单调）？
□ 布局类型是否与内容结构匹配？

如果否 → 布局过于单一，返回步骤2优化选择逻辑
```

**验证项目5：图表实际显示效果**
```
□ 打开HTML文件，检查所有图表是否可见？
□ 检查图表宽度是否为正常值（非0）？
□ 检查图表高度是否合理（400-500px）？
□ 检查图表数据是否正确显示？
□ 检查图表交互是否正常（悬停、点击）？

如果否 → 图表显示有问题，返回步骤3修复
```

**图表显示问题诊断流程：**

```
问题1：图表宽度为0
├─ 检查：.chart-container { width: 100% !important; }
├─ 检查：canvas { width: 100% !important; }
├─ 检查：Chart.js配置 responsive: true
└─ 解决方案：添加上述CSS和配置

问题2：图表显示过小
├─ 检查：.chart-container { height: 500px; }
├─ 检查：Chart.js配置 maintainAspectRatio: false
└─ 解决方案：调整高度和配置

问题3：多个图表只有部分显示
├─ 检查：每个canvas ID唯一性
├─ 检查：DOMContentLoaded中初始化
└─ 解决方案：修复ID和初始化逻辑

问题4：纵向长列表需要滚动
├─ 检查：观点数量
├─ 如果4-6个 → 使用卡片网格布局
├─ 如果7+个 → 分页或分组展示
└─ 解决方案：返回步骤2优化布局选择

问题5：布局过于单调
├─ 检查：是否使用了多种布局类型
├─ 解决方案：应用随机选择机制
└─ 解决方案：增加布局多样性
```

**图表显示和布局的验收标准：**

✅ **合格标准：**
- 所有图表都正常显示（宽度非0）
- 图表大小合理（高度400-500px）
- 布局充分利用横向空间
- 避免纵向长列表导致滚动
- 4-6个观点使用卡片网格布局
- 布局有足够的多样性

❌ **不合格标准（需要回退）：**
- 图表宽度为0或过小
- 图表配置不正确
- 纵向长列表导致需要滚动
- 布局过于单一（所有页面都用单列）
- 多个观点未使用网格布局
- 未充分利用横向空间

**回退触发条件：**

```
以下任一情况发生，必须回退：

1. 发现图表宽度为0
   → 返回步骤3，添加修复CSS

2. 发现图表配置不正确
   → 返回步骤3，修复Chart.js配置

3. 发现纵向长列表需要滚动
   → 返回步骤2或3，优化布局

4. 发现布局过于单一
   → 返回步骤2，应用随机选择机制

5. 发现多个观点未使用网格布局
   → 返回步骤2或3，改用卡片网格
```

**正确的图表和布局示例：**

```
✅ 正确示例1：图表容器CSS
.chart-container {
  width: 100% !important;
  min-width: 300px !important;
  max-width: 100% !important;
  height: 500px;
  box-sizing: border-box;
}

✅ 正确示例2：Chart.js配置
{
  responsive: true,
  maintainAspectRatio: false,
  // ... 其他配置
}

✅ 正确示例3：卡片网格布局（4-6个观点）
<div class="highlight-cards">
  <div class="highlight-card">...</div>
  <div class="highlight-card">...</div>
  <div class="highlight-card">...</div>
  <div class="highlight-card">...</div>
</div>

✅ 正确示例4：三列布局（3个观点）
<div class="three-column-layout">
  <div class="column">...</div>
  <div class="column">...</div>
  <div class="column">...</div>
</div>

❌ 错误示例1：单列长列表（7+个观点）
<div class="slide">
  <ul class="bullet-list">
    <li>观点1</li>
    <li>观点2</li>
    <!-- ... 7+个观点，需要滚动 -->
  </ul>
</div>

❌ 错误示例2：缺少width: 100%
.chart-container {
  /* 缺少width: 100% */
  height: 500px;
}
```

---

#### 5.1.7 🔍 布局合理性验证（⚠️ 新增）

**⚠️ 验证是否在步骤2.0中先确定布局，再选择图表/图文**

**检查AI是否按照正确的顺序进行布局和图表选择：**

**验证项目1：布局选择是否在图表选择之前**
```
□ 是否在步骤2.0中先确定了页面布局？
□ 是否基于内容特征（观点数量、数据密度）选择布局？
□ 是否记录了每页幻灯片的布局类型？
□ 是否在确定布局后才进入步骤2.1选择图表？

如果否 → 说明顺序错误，返回步骤2重新执行
```

**验证项目2：布局类型选择是否合理**
```
□ 1个观点是否使用单列布局？
□ 2-3个观点是否使用双列或三列布局？
□ 4-6个观点是否使用卡片网格布局？
□ 7+个观点是否分页或使用混合布局？
□ 包含图表的页面是否使用图表+文本布局？

如果否 → 说明布局选择不合理，返回步骤2.0重新选择
```

**验证项目3：布局与内容的匹配度**
```
□ 对比内容是否使用双列或对比表格？
□ 并列内容是否使用三列或卡片网格？
□ 数据密集内容是否使用图表+文本布局？
□ 单个核心观点是否使用单列或强调框？

如果否 → 说明布局与内容不匹配，返回步骤2.0重新选择
```

**验证项目4：布局空间利用率**
```
□ 是否充分利用横向空间（避免左右空白）？
□ 是否避免纵向长列表导致需要滚动？
□ 单屏内容是否不超过视口高度的80%？
□ 图表容器宽度是否为100%？

如果否 → 说明空间利用率不足，返回步骤2.0或3优化
```

**验证项目5：布局多样性**
```
□ 20页幻灯片是否至少使用了3种不同布局？
□ 是否避免所有页面都使用相同布局？
□ 布局选择是否有足够的视觉变化？

如果否 → 说明布局过于单一，返回步骤2.0增加多样性
```

**布局合理性验收标准：**

✅ **合格标准：**
- 在步骤2.0中先确定布局，再选择图表
- 布局类型与内容特征匹配
- 充分利用横向空间，避免纵向滚动
- 布局有足够的多样性（至少3种）
- 图表+文本布局正确配置

❌ **不合格标准（需要回退）：**
- 先选择图表再确定布局（顺序错误）
- 7+个观点使用单列布局（空间浪费）
- 所有页面使用相同布局（过于单调）
- 布局与内容类型不匹配（对比用单列）
- 图表宽度为0或过小（配置错误）

**回退触发条件：**

```
以下任一情况发生，必须回退：

1. 发现布局选择在图表选择之后
   → 返回步骤2，先执行2.0布局规划，再执行2.1图表选择

2. 发现7+个观点使用单列布局
   → 返回步骤2.0，改用卡片网格或混合布局

3. 发现所有页面都使用相同布局
   → 返回步骤2.0，增加布局多样性

4. 发现布局与内容类型不匹配
   → 返回步骤2.0，重新选择布局类型

5. 发现横向空间大量空白
   → 返回步骤2.0或3，优化为多列布局
```

**正确的布局选择流程示例：**

```
✅ 正确示例：步骤2.0 → 步骤2.1

步骤2.0（布局规划）：
页面16：六大平台启示
├─ 内容特征：6个并列要点，无数据
├─ 观点数量：6个
├─ 数据密度：低
└─ 确定布局：卡片网格布局（L4）

步骤2.1（图表选择）：
页面16：六大平台启示
├─ 左列区域（卡片1-3）：商业模式、用户定位、定价策略
├─ 右列区域（卡片4-6）：内容策略、增长策略、风险规避
└─ 选择呈现方式：highlight-card + bullet-list

结果：充分利用横向空间，6个要点横向排列，无需滚动
```

```
❌ 错误示例：直接选择图表，忽略布局规划

错误做法：
页面16：六大平台启示
├─ ❌ 直接选择：bullet-list（单列布局）
├─ ❌ 结果：6个要点纵向排列，需要上下滚动
└─ ❌ 问题：横向空间大量浪费，用户体验差

正确做法：
├─ ✅ 先确定布局：卡片网格布局（步骤2.0）
├─ ✅ 再选择呈现：highlight-card（步骤2.1）
└─ ✅ 结果：横向排列，无需滚动，空间充分利用
```

**布局决策检查清单：**

在生成HTML之前，必须完成以下检查：

```
□ 已为每页幻灯片确定布局类型（L1-L12）
□ 已记录每页选择的布局理由
□ 已验证布局与内容特征匹配
□ 已验证布局空间利用率
□ 已验证布局多样性
□ 确认布局在图表选择之前确定
```

**如果任何一项为"否"，不得进入步骤3，必须返回步骤2重新规划布局。**

---

#### 5.2 🔍 内容完整性检查（必须100%通过）

**⚠️ 严格检验方法 - 逐章对照原文档：**

**第一步：提取原文档的所有章节结构**
```
使用工具提取文档的所有标题
推荐使用 Read 工具完整阅读文档，记录所有标题层级
```

**第二步：制作章节对照清单**
创建一个对照表，逐项检查：
```
原文档章节                    幻灯片页码    是否完整    备注
────────────────────────────────────────────────────
章节1：标题                    第X页         □ 是 □ 否
  - 子章节1.1                  第Y页         □ 是 □ 否
  - 子章节1.2                  第Z页         □ 是 □ 否
章节2：标题                    第A页         □ 是 □ 否
...
```

**第三步：逐项内容验证**

**✅ 必须验证的内容类型：**
- [ ] **所有一级标题（#）**：必须全部呈现为独立章节封面页
- [ ] **所有二级标题（##）**：必须全部呈现为幻灯片页面标题或独立页面
- [ ] **所有三级标题（###）**：必须全部包含在对应页面中
- [ ] **所有数据表格**：必须完整转换为HTML表格或图表
- [ ] **所有数值数据**：
  - 金额（如：14-21亿、150-200万）
  - 百分比（如：15%、65%）
  - 数量（如：50万用户、6000万）
  - 对比值（如：10-20倍差距）
- [ ] **所有结论性陈述**：
  - "强烈建议"类结论
  - "关键"类要点
  - "优势/劣势"分析
  - "成功案例"列举
- [ ] **所有建议和行动计划**：
  - 时间线（如：3年目标、5年目标）
  - 行动步骤
  - 实操建议
- [ ] **所有对比分析**：
  - A vs B 对比表
  - 优缺点对比
  - 差异分析

**❌ 发现内容缺失时的处理：**

**立即停止！执行回退流程：**

1. **记录缺失内容**
```
缺失内容清单：
1. 缺失章节：《XXX章节》
   - 缺失原因：[分析原因]
   - 应包含内容：[列出缺失的具体内容]
2. 缺失数据：XXX数值
3. 缺失结论：XXX结论
```

2. **返回步骤1（文档内容分析）**
```
⚠️ 检验未通过！返回步骤1重新分析文档

问题原因：
[例如：步骤1中未提取"商业模式"章节的标题结构]

重新执行：
- 重新完整阅读文档
- 补充提取缺失的章节内容
- 更新内容结构大纲
- 验证无遗漏后再进入步骤2
```

3. **返回步骤2（幻灯片设计）**
```
⚠️ 检验未通过！返回步骤2重新设计

问题原因：
[例如：步骤2中页面规划遗漏了"商业模式"章节]

重新执行：
- 补充缺失章节的页面规划
- 更新幻灯片页面规划表
- 为缺失内容选择合适的呈现形式
- 验证规划完整性后再进入步骤3
```

4. **返回步骤3（HTML生成）**
```
⚠️ 检验未通过！返回步骤3重新生成

问题原因：
[例如：步骤3中生成HTML时遗漏了部分内容]

重新执行：
- 补充生成缺失内容的幻灯片
- 确保所有规划的内容都已生成
- 验证内容完整性后再进入步骤4
```

#### 5.4 设计规范检查

**McKinsey 风格验证**：
- [ ] 配色方案严格遵循规范
- [ ] 排版层次清晰一致
- [ ] 字体大小符合规范
- [ ] 间距和留白适当
- [ ] 页面布局整洁专业

**视觉质量评估**：
- [ ] 图表清晰易读
- [ ] 文字对比度充足
- [ ] 视觉层次分明
- [ ] 无杂乱或拥挤感
- [ ] 整体风格统一

#### 5.5 功能性测试

**导航功能**：
- [ ] "上一页"按钮正常工作
- [ ] "下一页"按钮正常工作
- [ ] 键盘方向键控制正常
- [ ] 空格键翻页正常
- [ ] 幻灯片计数器准确
- [ ] 页面切换流畅

**交互功能**：
- [ ] 全屏模式正常
- [ ] ESC退出全屏正常
- [ ] 图表悬停提示显示
- [ ] 图表交互响应灵敏

**响应式设计**：
- [ ] 桌面端显示正常
- [ ] 平板端显示正常
- [ ] 移动端显示正常
- [ ] 不同屏幕尺寸自适应

#### 5.6 兼容性测试

**浏览器兼容性**：
- [ ] Chrome 浏览器正常显示
- [ ] Safari 浏览器正常显示
- [ ] Firefox 浏览器正常显示
- [ ] Edge 浏览器正常显示

**性能检查**：
- [ ] 页面加载速度合理（< 3秒）
- [ ] 幻灯片切换流畅无卡顿
- [ ] 图表渲染无延迟
- [ ] 无 JavaScript 错误

#### 5.7 ✅ 代码质量检查（严格遵循HTML最佳实践）

**⚠️ 必须验证的HTML最佳实践：**

**A. HTML结构与可访问性**
- [ ] **DOCTYPE声明**：必须包含 `<!DOCTYPE html>`
- [ ] **语言属性**：`<html lang="zh-CN">` 正确设置
- [ ] **字符编码**：`<meta charset="UTF-8">` 必须在head中
- [ ] **视口设置**：`<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- [ ] **语义化标签**：
  - 使用 `<nav>` 而非 `<div class="nav">`
  - 使用 `<section>` 或 `<article>` 包含内容块
  - 使用 `<h1>-<h6>` 而非样式化标题
  - 使用 `<button>` 而非 `<div onclick="...">`
  - 表格使用 `<thead>`, `<tbody>`, `<th>`, `<td>`
- [ ] **图片替代文本**：所有 `<img>` 必须有 `alt` 属性
- [ ] **表单标签**：输入框必须有对应的 `<label>`

**B. CSS最佳实践**
- [ ] **响应式设计**：
  - 使用媒体查询 `@media (max-width: ...)`
  - 使用相对单位（rem, em, %）而非固定px
  - 移动端优先设计
- [ ] **性能优化**：
  - 避免过度嵌套选择器（最多3层）
  - 使用类选择器而非标签选择器
  - 避免使用 `!important`
  - 合并重复样式
- [ ] **可维护性**：
  - 使用CSS变量（`:root`）定义颜色和尺寸
  - BEM命名规范或一致的命名约定
  - 注释说明复杂样式

**C. JavaScript最佳实践**
- [ ] **错误处理**：
  ```javascript
  // 必须包含错误处理
  try {
      // 图表初始化代码
  } catch (error) {
      console.error('图表初始化失败:', error);
      // 向用户显示友好提示
  }
  ```
- [ ] **DOM操作**：
  - 等待DOM加载完成：`document.addEventListener('DOMContentLoaded', ...)`
  - 缓存DOM查询：`const slides = document.querySelectorAll('.slide')`
  - 事件委托（如适用）
- [ ] **性能优化**：
  - 避免在循环中操作DOM
  - 使用 `requestAnimationFrame` 进行动画
  - 防抖/节流事件处理（如resize, scroll）
- [ ] **内存泄漏检查**：
  - 移除事件监听器（如需要）
  - 清空定时器和间隔器
  - 避免闭包中的循环引用

**D. 外部依赖**
- [ ] **CDN链接**：
  - 使用可靠的CDN（如 jsdelivr, unpkg）
  - 指定版本号（如 `@4.4.0`）而非 `@latest`
  - 检查CDN可访问性
- [ ] **备用方案**：
  ```html
  <!-- 如果CDN失败，提供备用方案 -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
  <script>
      if (typeof Chart === 'undefined') {
          document.body.innerHTML = '<div style="padding:40px;text-align:center;">无法加载图表库，请检查网络连接</div>';
      }
  </script>
  ```

**E. 浏览器兼容性**
- [ ] **前缀处理**：使用 `autoprefixer` 或手动添加浏览器前缀
- [ ] **降级方案**：为不支持的浏览器提供基本功能
- [ ] **特性检测**：使用 `Modernizr` 或手动检测

**❌ 代码质量未通过时的处理：**

**立即执行修复流程：**

1. **记录问题清单**
```
代码质量问题清单：
1. HTML问题：
   - [ ] 缺少DOCTYPE声明
   - [ ] 未使用语义化标签
   - [ ] 缺少viewport设置
2. CSS问题：
   - [ ] 无响应式设计
   - [ ] 使用!important过多
3. JavaScript问题：
   - [ ] 无错误处理
   - [ ] DOM加载前执行
4. 兼容性问题：
   - [ ] CDN不可访问
   - [ ] 特定浏览器不支持
```

2. **返回步骤3（HTML生成）**
```
⚠️ 代码质量检验未通过！返回步骤3重新生成

问题原因：
[列出具体的代码质量问题]

重新执行：
- 修复所有HTML结构问题
- 添加必要的meta标签和语义化标签
- 优化CSS性能和可维护性
- 完善JavaScript错误处理
- 测试浏览器兼容性
- 验证所有最佳实践后再进入步骤4
```

3. **常见问题修复模板**

**修复示例1：添加错误处理**
```javascript
// ❌ 错误写法
const ctx = document.getElementById('myChart');
new Chart(ctx, { ... });

// ✅ 正确写法
try {
    const ctx = document.getElementById('myChart');
    if (!ctx) {
        throw new Error('无法找到图表容器');
    }
    new Chart(ctx, { ... });
} catch (error) {
    console.error('图表初始化失败:', error);
    // 显示友好错误提示
}
```

**修复示例2：DOM加载检查**
```javascript
// ❌ 错误写法
const slides = document.querySelectorAll('.slide');
showSlide(0);

// ✅ 正确写法
document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slide');
    if (slides.length === 0) {
        console.error('未找到任何幻灯片');
        return;
    }
    showSlide(0);
});
```

**修复示例3：响应式设计**
```css
/* ❌ 错误写法 */
.slide-content {
    width: 1400px;
    padding: 60px;
}

/* ✅ 正确写法 */
.slide-content {
    max-width: 1400px;
    width: 100%;
    padding: 60px;
}

@media (max-width: 1024px) {
    .slide-content {
        padding: 30px;
    }
}
```

#### 5.8 🎯 最终验收标准（一票否决制）

**⚠️ 以下任一标准未通过，即为不合格，必须回退重新执行！**

**✅ 标准一：内容完整性（核心标准，一票否决）**

**检验方法：逐章对照原文档**
```
必须100%满足：
□ 所有章节标题已呈现
□ 所有子章节已包含
□ 所有数据点已保留
□ 所有结论已呈现
□ 所有建议已包含
□ 所有表格已转换
□ 所有对比分析已呈现

✓ 零遗漏原则：任何内容缺失，即为不合格
✓ 零篡改原则：任何内容曲解，即为不合格
✓ 准确性原则：任何数据错误，即为不合格
```

**❌ 发现任何内容问题 → 立即返回步骤1重新分析**

**✅ 标准二：代码质量（核心标准，一票否决）**

**检验方法：HTML最佳实践检查清单**
```
必须100%满足：
□ DOCTYPE声明正确
□ 语言和字符编码设置
□ 视口和响应式设计
□ 语义化HTML标签
□ JavaScript错误处理
□ DOM加载检查
□ CDN可访问性
□ 浏览器兼容性

✓ 可访问性原则：不符合WCAG标准，即为不合格
✓ 性能原则：加载过慢或有错误，即为不合格
✓ 兼容性原则：主流浏览器无法访问，即为不合格
```

**❌ 发现任何代码问题 → 立即返回步骤3重新生成**

**✅ 标准三：设计规范（重要标准）**
- [ ] McKinsey配色方案严格遵循
- [ ] 排版层次清晰一致
- [ ] 页面布局整洁专业

**✅ 标准四：功能完整（重要标准）**
- [ ] 导航功能正常
- [ ] 图表正确渲染
- [ ] 交互流畅自然

**✅ 标准五：用户体验（加分项）**
- [ ] 加载速度快（<3秒）
- [ ] 动画流畅自然
- [ ] 键盘快捷键支持

---

**📋 最终验收流程：**

```
第一步：内容完整性检验（最重要！）
├─ 提取原文档所有章节标题
├─ 制作章节对照表
├─ 逐项检查是否呈现
└─ ❌ 如有缺失 → 返回步骤1重新分析

第二步：代码质量检验（最重要！）
├─ HTML结构检查
├─ CSS最佳实践检查
├─ JavaScript错误处理检查
├─ 浏览器兼容性测试
└─ ❌ 如有问题 → 返回步骤3重新生成

第三步：设计规范检验
└─ McKinsey风格一致性检查

第四步：功能测试
├─ 导航测试
├─ 图表测试
└─ 交互测试

第五步：签发交付
✅ 所有标准通过 → 可以交付
❌ 任一标准未通过 → 重新执行流程
```

**⚠️ 重要提醒：**

1. **内容完整性 > 设计美观 > 功能炫酷**
   宁可设计简单，不可丢失内容
   宁可功能基础，不可遗漏数据

2. **代码质量 > 创意实现 > 快速完成**
   宁可多花时间，必须保证代码规范
   宁可延迟交付，不可交付有问题的代码

3. **发现问题，立即回退，绝不将就**
   第一个发现的问题就是最严重的问题
   解决第一个问题，可能解决后续所有问题

4. **重新执行时，先解决问题根源**
   内容缺失 → 回到步骤1（分析阶段）
   设计遗漏 → 回到步骤2（设计阶段）
   代码问题 → 回到步骤3（生成阶段）
   合并问题 → 回到步骤4（合并阶段）

**输出产物**：
- 质量检验报告（包含所有检查项结果）
- 发现的问题列表（如有）
- 优化建议（如有）

**验证标准**：
- [ ] 所有检查项通过
- [ ] 无严重问题
- [ ] 无阻塞性缺陷
- [ ] 可以交付使用

---

## 🎯 使用方法

### 基本用法

```
/beauty 文件路径
```

### 多文件处理

```
/beauty 文件1.md 文件2.pdf 文件3.txt
```

### 输出位置

生成的 HTML 文件将保存在原文件同目录下，命名规则：
- `文件.md` → `文件_beautified.html`
- `文件.pdf` → `文件_beautified.html`
- `文件.txt` → `文件_beautified.html`

---

## ⚠️ 重要提醒

1. **必须严格遵循5步流程**：不得跳过任何步骤
2. **内容完整性优先**：宁可多做页面，不可丢失内容
3. **设计规范必遵守**：配色、排版必须符合 McKinsey 标准
4. **质量检验必执行**：必须完成步骤5的所有检查项
5. **用户交付承诺**：确保交付的是可用的专业演示文稿

---

## 📊 支持的文件格式

- **Markdown** (.md) - 推荐
- **Text** (.txt)
- **JSON** (.json) - 结构化数据
- **PDF** (.pdf) - 需要文本提取
- **Word** (.docx) - 需要文本提取

---

## 🎨 McKinsey 设计系统速查

| 元素 | 规范 |
|------|------|
| **背景色** | `#FFFFFF` (纯白) |
| **主文字** | `#000000` (纯黑) |
| **正文文字** | `#333333` (深灰) |
| **强调色** | `#F85d42` (橙色) |
| **辅助色** | `#74788d` (灰蓝) |
| **数据色** | `#556EE6` (深蓝) |
| **成功色** | `#34c38f` (绿色) |
| **警告色** | `#f1b44c` (黄色) |
| **主标题** | 64px, 粗体, 黑色 |
| **副标题** | 28-36px, 粗体, 橙色 |
| **正文** | 16-20px, 常规, 深灰 |
| **行高** | 1.5-1.6 |
| **页面边距** | 60-80px |
| **元素间距** | 20-30px |

---

## 🚀 执行检查清单

在执行 `/beauty` 命令前，确认：

- [ ] 已完整阅读源文档
- [ ] 理解5步流程要求
- [ ] 明确输出目标
- [ ] 准备好进行质量检验

执行后，验证：

- [ ] HTML 文件已生成
- [ ] 文件可正常打开
- [ ] 所有内容完整
- [ ] 所有功能正常
- [ ] 通过质量检验
