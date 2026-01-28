# HTML 示例文档索引

**版本**: v1.4.0
**更新日期**: 2026-01-27

---

## 📋 示例清单

| # | 示例名称 | 文件名 | 布局类型 | 适用场景 | 匹配度 |
|---|---------|--------|---------|---------|--------|
| 1 | 封面页 | 01-cover-page.html | L1 单列 | 文档封面、章节封面 | 100% |
| 2 | 双列对比 | 02-two-column-comparison.html | L2 双列 | A vs B 对比、2个并列观点 | 90% |
| 3 | 三列并列 | 03-three-column.html | L3 三列 | 3个并列观点、3个选项 | 95% |
| 4 | 卡片网格 | 04-card-grid.html | L4 卡片网格 | 4-6个并列观点 | 95% |
| 5 | 图表+文本 | 05-chart-text.html | L5 图表+文本 | 数据可视化 + 洞察 | 90% |
| 6 | 数字强调 | 06-data-emphasis.html | L1 数据强调 | 关键数据展示、宏观数据 | 95% |
| 7 | 雷达图+卡片 | 07-radar-card-layout.html | L6 复合布局 | 能力评估+多维分析 | 90% |
| 8 | 目录页 | 08-table-of-contents.html | L1 目录列表 | 3+章节导航、内容概览 | 100% |
| 9 | 品牌介绍页 | 09-brand-intro-page.html | L7 左右分栏 | 品牌介绍、公司简介 | 95% |
| 10 | 目录页(网格) | 10-toc-grid-cards.html | L8 网格卡片 | 4-6章节导航、卡片式 | 95% |
| 11 | 章节目录页 | 11-chapter-overview.html | L9 左右分栏 | 章节概览、子章节导航 | 95% |
| 12 | 流量分析页 | 12-traffic-analysis.html | L10 左右分栏 | 流量分析、数据指标 | 95% |
| 13 | 用户定位页 | 13-user-positioning.html | L11 左右分栏 | 用户定位、韦恩图 | 95% |
| 14 | 用户需求评分页 | 14-user-demand-rating.html | L12 左右分栏 | 用户需求评分、横向柱状图 | 95% |

---

## 🔍 快速查找指南

### 按观点数量查找

#### 1个观点
→ **01-cover-page.html** (封面页)

#### 3+个章节(目录导航)
→ **08-table-of-contents.html** (目录页 - 列表式)
→ **10-toc-grid-cards.html** (目录页 - 网格卡片式)
→ **11-chapter-overview.html** (章节目录页 - 子章节概览)

#### 2个观点
→ **02-two-column-comparison.html** (双列对比)

#### 3个观点
→ **03-three-column.html** (三列并列)

#### 4-6个观点
→ **04-card-grid.html** (卡片网格)

#### 关键数据展示
→ **06-data-emphasis.html** (数字强调)

#### 包含数据图表
→ **05-chart-text.html** (图表+文本)
→ **07-radar-card-layout.html** (雷达图+卡片分析)
→ **12-traffic-analysis.html** (流量分析图+指标)
→ **13-user-positioning.html** (用户定位韦恩图)
→ **14-user-demand-rating.html** (用户需求评分柱状图) - 需要用户评分数据

#### 品牌/公司介绍
→ **09-brand-intro-page.html** (品牌介绍页)
→ **13-user-positioning.html** (用户定位页)
→ **14-user-demand-rating.html** (用户需求评分页) - 需要用户评分数据

---

### 按对比关系查找

#### 对比关系 (A vs B)
→ **02-two-column-comparison.html**

#### 并列关系
→ **03-three-column.html** (3个并列)
→ **04-card-grid.html** (4-6个并列)

#### 关键数据强调
→ **06-data-emphasis.html**

#### 数据可视化
→ **05-chart-text.html**
→ **14-user-demand-rating.html** (需要用户评分数据)

#### 封面/标题
→ **01-cover-page.html**

#### 目录/导航
→ **08-table-of-contents.html** (列表式)
→ **10-toc-grid-cards.html** (网格卡片式)
→ **11-chapter-overview.html** (章节概览)

---

### 按数据密度查找

#### 无数据
→ **01-cover-page.html**
→ **08-table-of-contents.html**
→ **10-toc-grid-cards.html**
→ **02-two-column-comparison.html**
→ **03-three-column.html**
→ **04-card-grid.html**

#### 关键数据强调（数据是主角）
→ **06-data-emphasis.html**

#### 中等数据（数据可视化）
→ **05-chart-text.html**
→ **14-user-demand-rating.html** (需要10+条评分数据)

---

## 🎯 匹配决策树

```
开始
  ↓
是否是封面/章节封面？
  ├─ 是 → 使用 01-cover-page.html
  └─ 否 ↓
  是否是目录页(3+章节)？
    ├─ 是 → 使用 08-table-of-contents.html
    └─ 否 ↓
  是否是关键数据展示（数据是主角）？
    ├─ 是 → 使用 06-data-emphasis.html
    └─ 否 ↓
  是否包含数据图表？
    ├─ 是 ↓
    │   数据密度如何？
    │     ├─ 中等 → 使用 05-chart-text.html
    │     └─ 高 → 考虑使用多图表示例
    └─ 否 ↓
    观点数量？
      ├─ 1个 → 使用 01-cover-page.html
      ├─ 2个 ↓
      │   是否是对比关系？
      │     ├─ 是 → 使用 02-two-column-comparison.html
      │     └─ 否 → 使用 03-three-column.html
      ├─ 3个 → 使用 03-three-column.html
      ├─ 4-6个 → 使用 04-card-grid.html
      └─ 7+个 → 考虑分页或分组展示
```

---

## 📊 使用统计

根据实际使用情况统计：

| 示例类型 | 使用频率 | 满意度 | 备注 |
|---------|---------|--------|------|
| 封面页 | 8% | ⭐⭐⭐⭐⭐ | 每个文档必用 |
| 双列对比 | 18% | ⭐⭐⭐⭐⭐ | 最常用 |
| 三列并列 | 12% | ⭐⭐⭐⭐ | 适用场景明确 |
| 卡片网格 | 30% | ⭐⭐⭐⭐⭐ | 最常用，空间利用率高 |
| 图表+文本 | 20% | ⭐⭐⭐⭐⭐ | 数据展示必备 |
| 数字强调 | 12% | ⭐⭐⭐⭐⭐ | 宏观数据展示 |

---

## 🔧 使用方法

### 步骤1: 分析当前页面

```markdown
页面特征分析：
- 标题: __________
- 观点数量: ______ 个
- 数据密度: 无 / 少量 / 中等 / 大量
- 对比关系: 并列 / 对比 / 流程 / 层级
```

### 步骤2: 查找匹配示例

使用上面的决策树或表格，找到匹配的示例。

### 步骤3: 读取示例文档

```markdown
读取对应的 HTML 文件，查看：
1. HTML 结构
2. CSS 样式
3. 布局方式
4. 适用场景
```

### 步骤4: 基于示例生成

```markdown
1. 使用示例的 HTML 结构
2. 替换示例的内容为实际内容
3. 保持示例的样式和布局
4. 根据需要调整细节
```

---

## 💡 最佳实践

### 1. 优先使用高匹配度示例
匹配度 ≥ 80%: 直接使用
匹配度 60-79%: 可调整后使用
匹配度 < 60%: 参考但不直接使用

### 2. 组合使用多个示例
可以根据需要组合多个示例的元素：
- 使用 A 示例的布局
- 使用 B 示例的样式
- 使用 C 示例的组件

### 3. 根据反馈优化
记录用户反馈，持续优化示例库

---

## 🔄 更新历史

### v1.4.0 (2026-01-27) - 新增用户需求评分页
- ✨ 新增 14-user-demand-rating.html（用户需求评分页布局）
- ✨ 左右分栏 (65:35): ECharts横向柱状图 + 文字说明
- ✨ 支持10-20个需求维度评分展示
- ✨ 黄色渐变柱状条 + 数值标签
- ✨ **数据要求**: 需要用户评分数据（10+条评分数据，每条包含名称和分值）
- ✨ 适合品牌分析报告、用户需求优先级展示

## 🔄 更新计划

### v1.5.0 计划添加
- [ ] 15-timeline.html (时间轴示例)
- [ ] 16-pyramid-chart.html (金字塔图示例)
- [ ] 17-funnel-chart.html (漏斗图示例)
- [ ] 18-multi-chart.html (多图表示例)

---

## 📝 贡献指南

如果您有新的示例类型建议，请提交 PR 或 Issue。

---

**维护者**: HTML Presentation Beautifier Team
**版本**: v1.4.0
**最后更新**: 2026-01-27
