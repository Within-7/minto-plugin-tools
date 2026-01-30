# 样式代码库

本文档提供幻灯片演示中使用的所有CSS样式定义，供Agent在生成HTML时参考使用。

---

## 1 列表样式

### 1.1 标准要点列表（bullet-list）

**适用场景**：普通并列要点内容。

**识别关键词**：以及、另外、此外、包括、同时。

**CSS样式**：

```css
.bullet-list {
    list-style: none;
    padding-left: 0;
}

.bullet-list li {
    position: relative;
    padding-left: 28px;
    margin-bottom: 18px;
    font-size: 18px;
    line-height: 1.7;
}

.bullet-list li::before {
    content: "•";
    position: absolute;
    left: 8px;
    color: #F85d42;
    font-weight: bold;
}
```

**HTML示例**：

```html
<ul class="bullet-list">
    <li><strong>数据驱动决策</strong>：基于大数据分析，提供精准决策支持</li>
    <li><strong>用户体验优先</strong>：持续优化产品交互，提升用户满意度</li>
    <li><strong>技术创新引领</strong>：保持技术前沿，快速迭代更新</li>
</ul>
```

---

### 1.2 编号列表（numbered-list）

**适用场景**：步骤、流程、顺序相关内容。

**识别关键词**：首先、其次、然后、最后、第一、第二、第三、步骤、阶段。

**CSS样式**：

```css
.numbered-list {
    list-style: none;
    padding-left: 0;
    counter-reset: item;
}

.numbered-list li {
    position: relative;
    padding-left: 50px;
    margin-bottom: 18px;
    font-size: 18px;
    line-height: 1.7;
}

.numbered-list li::before {
    counter-increment: item;
    content: counter(item);
    position: absolute;
    left: 0;
    width: 36px;
    height: 36px;
    background: #F85d42;
    color: white;
    text-align: center;
    line-height: 36px;
    font-weight: bold;
    border-radius: 0;
}
```

**HTML示例**：

```html
<ul class="numbered-list">
    <li><strong>第一步：需求分析</strong> - 深入了解客户需求，明确项目目标</li>
    <li><strong>第二步：方案设计</strong> - 制定详细实施方案，确定技术路线</li>
    <li><strong>第三步：落地执行</strong> - 按计划推进项目，定期汇报进展</li>
</ul>
```

---

### 1.3 卡片列表（card-list）

**适用场景**：需要突出显示的重要项目。

**识别关键词**：核心、关键、重要、主要、优势、特点。

**CSS样式**：

```css
.card-list {
    list-style: none;
    padding-left: 0;
}

.card-list li {
    background: #fafafa;
    border-left: 4px solid #556EE6;
    padding: 22px;
    margin-bottom: 18px;
}

.card-list li:nth-child(2) {
    border-left-color: #F85d42;
}

.card-list li:nth-child(3) {
    border-left-color: #34c38f;
}

.card-list li:nth-child(4) {
    border-left-color: #50a5f1;
}
```

**HTML示例**：

```html
<ul class="card-list">
    <li><strong>精准定位</strong>：深耕细分市场，满足用户核心需求</li>
    <li><strong>高效运营</strong>：自动化流程，降低运营成本30%</li>
    <li><strong>技术创新</strong>：持续研发投入，专利数量行业领先</li>
    <li><strong>生态合作</strong>：构建合作伙伴网络，实现共赢发展</li>
</ul>
```

---

### 1.4 对比列表（comparison-list）

**适用场景**：优劣势对比、两种方案对比、现在与未来对比。

**识别关键词**：对比、差异、优劣、vs、相比、优点、缺点。

**CSS样式**：

```css
.comparison-list {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 35px;
}

.comparison-list li {
    padding: 22px;
    background: #fafafa;
}

.pros-list li {
    border-left: 4px solid #34c38f;
}

.cons-list li {
    border-left: 4px solid #F85d42;
}
```

**HTML示例**：

```html
<ul class="comparison-list">
    <div class="pros-list">
        <li><strong>✓ 优势一</strong>：实施周期短，6个月可完成</li>
        <li><strong>✓ 优势二</strong>：初始投入较低</li>
    </div>
    <div class="cons-list">
        <li><strong>✗ 劣势一</strong>：扩展性有限</li>
        <li><strong>✗ 劣势二</strong>：长期维护成本高</li>
    </div>
</ul>
```

---

### 1.5 时间线列表（timeline-list）

**适用场景**：公司发展历程、项目里程碑、历史时间节点。

**识别关键词**：年份、日期、过去、现在、未来、历程、发展、里程碑。

**CSS样式**：

```css
.timeline-list {
    list-style: none;
    padding-left: 30px;
    border-left: 2px solid #e0e0e0;
}

.timeline-list li {
    position: relative;
    padding-bottom: 28px;
}

.timeline-list li::before {
    content: "";
    position: absolute;
    left: -36px;
    top: 6px;
    width: 12px;
    height: 12px;
    background: #F85d42;
    border-radius: 0;
}

.timeline-list li:last-child {
    padding-bottom: 0;
}
```

**HTML示例**：

```html
<ul class="timeline-list">
    <li><strong>2018年</strong>：公司成立，完成首轮融资</li>
    <li><strong>2020年</strong>：产品上线，用户突破100万</li>
    <li><strong>2022年</strong>：市场扩张，营收破亿</li>
    <li><strong>2024年</strong>：战略升级，启动国际化</li>
</ul>
```

---

### 1.6 图标列表（icon-list）

**适用场景**：每项需要图标或数字标识、分类说明内容。

**识别关键词**：类型、分类、方面、维度、要素。

**CSS样式**：

```css
.icon-list {
    list-style: none;
    padding-left: 0;
}

.icon-list li {
    display: flex;
    align-items: flex-start;
    margin-bottom: 22px;
}

.icon-list .icon {
    width: 40px;
    height: 40px;
    background: #556EE6;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 18px;
    font-size: 18px;
}

.icon-list .content {
    flex: 1;
}
```

**HTML示例**：

```html
<ul class="icon-list">
    <li>
        <div class="icon">📊</div>
        <div class="content">
            <strong>数据分析</strong>
            <p>深度挖掘数据价值，提供决策支持</p>
        </div>
    </li>
    <li>
        <div class="icon">🎯</div>
        <div class="content">
            <strong>精准营销</strong>
            <p>基于用户画像，实现精准触达</p>
        </div>
    </li>
    <li>
        <div class="icon">🔄</div>
        <div class="content">
            <strong>持续优化</strong>
            <p>迭代改进，保持竞争力</p>
        </div>
    </li>
</ul>
```

---

## 2 列表样式选择速查表

| 内容类型 | 推荐样式 | 优先级 | 适用场景 |
|---------|---------|--------|---------|
| 普通并列要点 | 标准要点列表 | ★★★★★ | 默认选择，5个及以下要点 |
| 步骤或流程 | 编号列表 | ★★★★★ | 首先、其次、最后、时间顺序 |
| 重要项目突出 | 卡片列表 | ★★★★☆ | 核心、关键、优势类内容 |
| 优劣势对比 | 对比列表 | ★★★★☆ | 方案对比、优缺点分析 |
| 时间线或里程碑 | 时间线列表 | ★★★★☆ | 年份、历程、发展阶段 |
| 带标签分类 | 图标列表 | ★★★☆☆ | 分类说明、维度分析 |

---

## 3 列表样式应用规则

1. **自动识别**：根据内容关键词自动选择合适的列表样式。
2. **混合使用**：同一页面可以使用多种列表样式。
3. **样式一致性**：同一层级的列表保持样式一致。
4. **颜色搭配**：使用设计系统指定的配色方案。
5. **内容适配**：根据要点数量和内容长度选择样式。

---

## 4 配色方案

### 4.1 品牌主色

| 颜色名称 | 色值 | 用途 |
|---------|------|------|
| 主色调 | #556EE6 | 卡片列表第一项、图标列表图标背景 |
| 强调色 | #F85d42 | 编号列表、要点列表、时间线节点 |
| 成功色 | #34c38f | 优点列表、正确标记 |
| 信息色 | #50a5f1 | 卡片列表第四项、辅助信息 |
| 边框色 | #e0e0e0 | 时间线边框、卡片边框 |

### 4.2 中性色

| 颜色名称 | 色值 | 用途 |
|---------|------|------|
| 背景色 | #fafafa | 卡片列表、对比列表背景 |
| 文字色 | #333333 | 主要文字 |
| 次要文字 | #666666 | 次要文字 |

---

## 5 字体规范

### 5.1 字号

| 元素 | 字号 | 行高 |
|-----|------|------|
| 页面标题 | 32px | 1.5 |
| 章节标题 | 28px | 1.5 |
| 要点标题 | 20px | 1.6 |
| 要点内容 | 18px | 1.7 |
| 辅助文字 | 16px | 1.6 |
| 时间线年份 | 18px | 1.5 |

### 5.2 字重

| 元素 | 字重 | 说明 |
|-----|------|------|
| 页面标题 | bold | 加粗 |
| 章节标题 | bold | 加粗 |
| 要点标题 | bold | 加粗 |
| 要点内容 | normal | 常规 |
| 辅助文字 | normal | 常规 |

---

## 6 间距规范

| 元素 | 上方间距 | 下方间距 | 左侧间距 | 右侧间距 |
|-----|---------|---------|---------|---------|
| 列表项 | 0 | 18px | 28px或50px | 0 |
| 卡片列表项 | 0 | 18px | 4px（左边框） | 0 |
| 时间线项 | 0 | 28px | 30px | 0 |
| 图标列表项 | 0 | 22px | 0 | 0 |
| 两列布局 | 0 | 0 | 35px（列间距） | 0 |

---

## 7 响应式适配

### 7.1 断点设置

| 断点名称 | 屏幕宽度 | 布局变化 |
|---------|---------|---------|
| 大屏桌面 | ≥1200px | 完整布局 |
| 中屏桌面 | 992px-1199px | 保持原布局 |
| 小屏设备 | 768px-991px | 调整列间距 |
| 移动设备 | <768px | 单列布局 |

### 7.2 响应式规则

```css
@media (max-width: 768px) {
    .comparison-list {
        grid-template-columns: 1fr;
        gap: 20px;
    }
    
    .bullet-list li,
    .numbered-list li {
        padding-left: 24px;
        font-size: 16px;
    }
    
    .numbered-list li {
        padding-left: 44px;
    }
}
```

---

## 8 使用说明

### 8.1 选择列表样式的步骤

1. **分析内容类型**：确定内容是普通要点、步骤流程、对比分析还是时间线。
2. **查找识别关键词**：根据内容中的关键词匹配对应的列表样式。
3. **检查要点数量**：确保要点数量适合所选样式。
4. **应用CSS类名**：在HTML的ul或ol元素上添加对应的class。
5. **检查视觉效果**：确保列表样式与整体设计风格一致。

### 8.2 常见问题

**问题1：要点超过6个，使用哪种样式？**

答案：要点数量不是决定因素。如果是无序的并列要点，使用标准要点列表；如果是步骤或流程，使用编号列表；如果是时间相关，使用时间线列表。

**问题2：同一页面可以使用多种列表样式吗？**

答案：可以。同一页面的不同部分可以使用不同的列表样式，但建议每个部分内部保持样式一致。

**问题3：如何自定义颜色？**

答案：直接修改变量定义中的颜色值即可。建议使用设计系统中定义的标准颜色，如#F85d42（橙色）、#556EE6（深蓝色）等。

---

## 9 内容丰富化模板 [NEW]

本章节提供内容页描述和图表解释说明的CSS样式模板，用于实现内容的丰富化和完整表达。

### 9.1 页面导语样式（page-intro）

**适用场景**：内容页开头的核心观点概述。

**CSS样式**：

```css
.page-intro {
    background: var(--color-bg-secondary, #F5F7FA);
    padding: var(--spacing-lg, 24px);
    border-left: 4px solid var(--color-accent, #F85d42);
    margin-bottom: var(--spacing-xl, 32px);
    border-radius: 0 var(--radius-md, 4px) var(--radius-md, 4px) 0;
}

.page-intro p {
    font-size: var(--font-size-body, 14px);
    line-height: var(--line-height-relaxed, 1.6);
    color: var(--color-text, #1A202C);
    margin: 0;
}
```

**HTML示例**：

```html
<div class="page-intro">
    <p>本页面深入分析目标市场的规模和增长趋势，为后续战略规划提供数据支撑。通过对北美返校季市场的详细研究，我们发现该市场具有显著的规模优势和持续增长动力，为业务拓展提供了坚实的市场基础。</p>
</div>
```

### 9.2 要点详细展开样式（content-point）

**适用场景**：每个要点的完整描述，包含背景、具体内容、数据支撑、影响分析、结论。

**CSS样式**：

```css
.content-point {
    margin-bottom: var(--spacing-xl, 32px);
    padding-bottom: var(--spacing-lg, 24px);
    border-bottom: 1px solid var(--color-border, #E2E8F0);
}

.content-point:last-child {
    border-bottom: none;
    margin-bottom: 0;
}

.point-title {
    font-size: var(--font-size-h4, 18px);
    font-weight: var(--font-weight-semibold, 600);
    color: var(--color-blue, #556EE6);
    margin-bottom: var(--spacing-md, 16px);
}

.point-content {
    background: var(--color-bg, #FFFFFF);
    padding: var(--spacing-lg, 24px);
    border-radius: var(--radius-md, 4px);
    border: 1px solid var(--color-border-light, #E2E8F0);
}

.point-content p {
    font-size: var(--font-size-body, 14px);
    line-height: var(--line-height-relaxed, 1.6);
    color: var(--color-text, #1A202C);
    margin-bottom: var(--spacing-sm, 8px);
}

.point-content p:last-child {
    margin-bottom: 0;
}

.point-content strong {
    color: var(--color-accent, #F85d42);
    font-weight: var(--font-weight-semibold, 600);
}

.point-content .background-description {
    background: var(--color-bg-secondary, #F5F7FA);
    padding: var(--spacing-sm, 8px) var(--spacing-md, 16px);
    border-radius: var(--radius-sm, 4px);
    margin-bottom: var(--spacing-md, 16px);
}

.point-content .data-support {
    background: rgba(85, 110, 230, 0.08);
    padding: var(--spacing-sm, 8px) var(--spacing-md, 16px);
    border-radius: var(--radius-sm, 4px);
    border-left: 3px solid var(--color-blue, #556EE6);
}

.point-content .conclusion {
    background: rgba(248, 93, 66, 0.08);
    padding: var(--spacing-sm, 8px) var(--spacing-md, 16px);
    border-radius: var(--radius-sm, 4px);
    border-left: 3px solid var(--color-accent, #F85d42);
}
```

**HTML示例**：

```html
<div class="content-point">
    <h3 class="point-title">要点一：市场规模庞大且持续增长</h3>
    <div class="point-content">
        <p class="background-description"><strong>背景描述：</strong>根据最新市场调研数据，北美返校季市场近年来保持稳定增长态势。</p>
        <p class="main-description"><strong>具体内容：</strong>2024年北美返校季市场规模达到365.9亿美元，预计2025年将增长至394亿美元。这一增长趋势反映了家长对教育投资的持续重视，以及学生返校购物需求的刚性特征。</p>
        <p class="data-support"><strong>数据支撑：</strong>市场规模从365.9亿美元增长至394亿美元，同比增长约7.7%，显著高于整体零售市场增速。</p>
        <p class="impact-analysis"><strong>影响分析：</strong>市场的整体规模为业务拓展提供了充足的市场空间，而持续增长则意味着市场机会的长期可持续性。</p>
        <p class="conclusion"><strong>结论说明：</strong>北美返校季市场具有显著的规模优势和持续增长动力，是值得重点投入的战略市场。</p>
    </div>
</div>
```

### 9.3 关联说明样式（content-connections）

**适用场景**：揭示多个要点之间的逻辑关系。

**CSS样式**：

```css
.content-connections {
    background: var(--color-bg-secondary, #F5F7FA);
    padding: var(--spacing-lg, 24px);
    border-radius: var(--radius-md, 4px);
    margin-top: var(--spacing-xl, 32px);
    border: 1px dashed var(--color-gray-light, #CBD5E0);
}

.content-connections h4 {
    font-size: var(--font-size-h5, 16px);
    font-weight: var(--font-weight-semibold, 600);
    color: var(--color-gray, #74788d);
    margin-bottom: var(--spacing-md, 16px);
    display: flex;
    align-items: center;
}

.content-connections h4::before {
    content: "↔";
    margin-right: var(--spacing-sm, 8px);
    font-size: var(--font-size-body, 14px);
}

.content-connections p {
    font-size: var(--font-size-body, 14px);
    line-height: var(--line-height-relaxed, 1.6);
    color: var(--color-text, #1A202C);
    margin-bottom: var(--spacing-sm, 8px);
}

.content-connections p:last-child {
    margin-bottom: 0;
}
```

**HTML示例**：

```html
<div class="content-connections">
    <h4>要点关联说明</h4>
    <p>上述三个要点相互支撑，共同构成了对市场机会的完整分析。市场规模是基础，决定了业务拓展的天花板；增长趋势是动力，指明了市场的发展方向；区域分布是策略依据，为资源配置提供了指引。</p>
    <p>三者结合，形成了"市场规模→增长动力→区域策略"的完整逻辑链条，为后续战略规划奠定了坚实基础。</p>
</div>
```

### 9.4 图表洞察面板样式（insight-panel）

**适用场景**：图表页的右侧解释说明区域。

**CSS样式**：

```css
.insight-panel {
    padding: var(--spacing-xl, 32px);
    background: var(--color-bg-secondary, #F5F7FA);
    border-radius: var(--radius-lg, 8px);
    height: 100%;
    overflow-y: auto;
}

.insight-section {
    margin-bottom: var(--spacing-xl, 32px);
}

.insight-section:last-child {
    margin-bottom: 0;
}

.insight-section h4 {
    font-size: var(--font-size-h5, 16px);
    font-weight: var(--font-weight-semibold, 600);
    color: var(--color-accent, #F85d42);
    margin-bottom: var(--spacing-md, 16px);
    padding-bottom: var(--spacing-sm, 8px);
    border-bottom: 2px solid var(--color-accent-light, rgba(248, 93, 66, 0.2));
}

.insight-section p {
    font-size: var(--font-size-body, 14px);
    line-height: var(--line-height-relaxed, 1.6);
    color: var(--color-text, #1A202C);
}

.insight-section ul {
    margin-top: var(--spacing-sm, 8px);
    padding-left: var(--spacing-lg, 24px);
}

.insight-section li {
    font-size: var(--font-size-body, 14px);
    line-height: var(--line-height-relaxed, 1.6);
    color: var(--color-text, #1A202C);
    margin-bottom: var(--spacing-xs, 4px);
}

.insight-section .action-recommendations {
    background: rgba(52, 195, 143, 0.1);
    padding: var(--spacing-md, 16px);
    border-radius: var(--radius-md, 4px);
    border-left: 3px solid var(--color-green, #34c38f);
}

.insight-section .action-recommendations h4 {
    color: var(--color-green, #34c38f);
    border-bottom-color: rgba(52, 195, 143, 0.3);
}
```

**HTML示例**：

```html
<div class="insight-panel">
    <div class="insight-section chart-overview">
        <h4>图表概述</h4>
        <p>本图表展示了2024-2025年北美返校季家庭消费支出的变化趋势。通过柱状图的直观对比，我们可以清晰看到市场规模从365.9亿美元增长至394亿美元，反映出返校季消费市场的持续增长态势。</p>
    </div>
    <div class="insight-section data-interpretation">
        <h4>数据解读</h4>
        <p><strong>2024年市场规模：</strong>365.9亿美元，反映了后疫情时代消费者对返校购物需求的恢复和稳定。电子品类表现最为亮眼，同比增长18.5%。</p>
        <p><strong>2025年市场规模：</strong>394亿美元，预计增长约7.7%。这一增长主要受到学费上涨、新技术产品更新换代、家长期望提升等因素驱动。</p>
    </div>
    <div class="insight-section insight-analysis">
        <h4>洞察分析</h4>
        <p><strong>洞察1：</strong>7.7%的年增长率明显高于CPI和整体零售增速，说明返校季消费具有较强的抗周期属性。</p>
        <p><strong>洞察2：</strong>电子品类18.5%的增速远超整体平均，反映出学生数字化学习需求的结构性转变。</p>
        <p><strong>洞察3：</strong>市场增长不仅来自学生数量增加，更来自单客消费金额的提升，体现消费升级趋势。</p>
    </div>
    <div class="insight-section action-recommendations">
        <h4>行动建议</h4>
        <ul>
            <li>加大电子品类布局，特别是与数字化学习相关的设备和配件</li>
            <li>提前规划库存以应对返校季峰值需求</li>
            <li>关注产品升级换代机会，推出更高价值的产品组合</li>
        </ul>
    </div>
</div>
```

### 9.5 图表+洞察两列布局样式

**适用场景**：图表页的整体布局，图表在左，洞察在右。

**CSS样式**：

```css
.chart-insight-layout {
    display: grid;
    grid-template-columns: 55% 45%;
    gap: var(--spacing-xl, 32px);
    margin-top: var(--spacing-xl, 32px);
}

.chart-container {
    background: var(--color-bg-secondary, #F5F7FA);
    padding: var(--spacing-lg, 24px);
    border-radius: var(--radius-lg, 8px);
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 400px;
}

.chart-container canvas,
.chart-container svg {
    max-width: 100%;
    height: auto;
}

@media (max-width: 992px) {
    .chart-insight-layout {
        grid-template-columns: 1fr;
        gap: var(--spacing-lg, 24px);
    }
    
    .chart-container {
        min-height: 300px;
    }
}
```

**HTML示例**：

```html
<div class="chart-insight-layout">
    <div class="chart-container">
        <!-- 图表HTML（柱状图/折线图/饼图等） -->
        <canvas id="marketChart"></canvas>
    </div>
    <div class="insight-panel">
        <!-- 洞察面板HTML -->
    </div>
</div>
```

### 9.6 内容页整体结构模板

**CSS样式**：

```css
.content-page {
    max-width: 1200px;
    margin: 0 auto;
    padding: var(--spacing-xl, 32px);
}

.page-title {
    font-size: var(--font-size-h2, 32px);
    font-weight: var(--font-weight-bold, 700);
    color: var(--color-text, #1A202C);
    margin-bottom: var(--spacing-xl, 32px);
    padding-bottom: var(--spacing-md, 16px);
    border-bottom: 3px solid var(--color-accent, #F85d42);
}

.content-body {
    margin-bottom: var(--spacing-xl, 32px);
}
```

**HTML示例**：

```html
<div class="slide content-page" id="slide-5" data-title="市场机会分析">
    <div class="slide-header">
        <span class="slide-title">市场机会分析</span>
    </div>
    
    <div class="slide-content">
        <h2 class="page-title">市场机会分析</h2>
        
        <!-- 页面导语 -->
        <div class="page-intro">
            <p>本页面深入分析目标市场的规模和增长趋势，为后续战略规划提供数据支撑。通过对北美返校季市场的详细研究，我们发现该市场具有显著的规模优势和持续增长动力。</p>
        </div>
        
        <!-- 详细内容 -->
        <div class="content-body">
            <div class="content-point">
                <h3 class="point-title">要点一：市场规模庞大且持续增长</h3>
                <div class="point-content">
                    <p class="background-description"><strong>背景描述：</strong>[背景信息]</p>
                    <p class="main-description"><strong>具体内容：</strong>[完整描述]</p>
                    <p class="data-support"><strong>数据支撑：</strong>[相关数据]</p>
                    <p class="impact-analysis"><strong>影响分析：</strong>[影响说明]</p>
                    <p class="conclusion"><strong>结论说明：</strong>[结论]</p>
                </div>
            </div>
            
            <div class="content-point">
                <h3 class="point-title">要点二：[要点标题]</h3>
                <div class="point-content">
                    <p class="background-description"><strong>背景描述：</strong>[背景信息]</p>
                    <p class="main-description"><strong>具体内容：</strong>[完整描述]</p>
                    <p class="data-support"><strong>数据支撑：</strong>[相关数据]</p>
                    <p class="impact-analysis"><strong>影响分析：</strong>[影响说明]</p>
                    <p class="conclusion"><strong>结论说明：</strong>[结论]</p>
                </div>
            </div>
        </div>
        
        <!-- 关联说明 -->
        <div class="content-connections">
            <h4>要点关联说明</h4>
            <p>[多个要点之间的逻辑关系说明]</p>
        </div>
    </div>
</div>
```

### 9.7 颜色变量定义

**建议在全局CSS中定义以下变量**：

```css
:root {
    /* 基础颜色 */
    --color-bg: #FFFFFF;
    --color-bg-secondary: #F5F7FA;
    --color-text: #1A202C;
    --color-text-secondary: #4A5568;
    --color-border: #E2E8F0;
    --color-border-light: #EDF2F7;
    
    /* 设计系统颜色 */
    --color-accent: #F85d42;
    --color-accent-light: rgba(248, 93, 66, 0.2);
    --color-blue: #556EE6;
    --color-green: #34c38f;
    --color-gray: #74788d;
    --color-gray-light: #CBD5E0;
    
    /* 间距变量 */
    --spacing-xs: 4px;
    --spacing-sm: 8px;
    --spacing-md: 16px;
    --spacing-lg: 24px;
    --spacing-xl: 32px;
    --spacing-2xl: 48px;
    
    /* 圆角变量 */
    --radius-sm: 4px;
    --radius-md: 4px;
    --radius-lg: 8px;
    
    /* 字体大小变量 */
    --font-size-xs: 12px;
    --font-size-body: 14px;
    --font-size-body-secondary: 13px;
    --font-size-h5: 16px;
    --font-size-h4: 18px;
    --font-size-h3: 24px;
    --font-size-h2: 32px;
    
    /* 字体粗细变量 */
    --font-weight-normal: 400;
    --font-weight-medium: 500;
    --font-weight-semibold: 600;
    --font-weight-bold: 700;
    
    /* 行高变量 */
    --line-height-normal: 1.5;
    --line-height-relaxed: 1.6;
    --line-height-loose: 1.8;
}
```
