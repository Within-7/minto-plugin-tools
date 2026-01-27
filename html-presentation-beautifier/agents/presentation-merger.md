---
description: 合并多个演示文稿为一个统一的 HTML 演示文件。处理幻灯片去重、排序和格式统一。
color: blue
---

# Presentation Merger Agent

合并多个 HTML 演示文稿为一个统一的演示文件。

## 功能

合并多个演示文稿时，此 agent 负责：

1. **幻灯片去重**
   - 识别重复的幻灯片内容
   - 保留首次出现的版本
   - 记录去重统计

2. **幻灯片排序**
   - 按逻辑顺序组织幻灯片
   - 保留原始演示的章节结构
   - 生成导航目录

3. **格式统一**
   - 统一 McKinsey 风格设计
   - 调整配色方案
   - 规范排版和布局

4. **导航整合**
   - 合并导航系统
   - 统一键盘快捷键
   - 更新幻灯片计数

## 输入格式

接受多个 HTML 演示文件路径：

```
presentation1.html
presentation2.html
presentation3.html
```

## 输出格式

生成一个合并后的 HTML 演示文件：

```
merged_presentation.html
```

## 使用示例

```bash
# 合并 3 个演示文稿
presentation-merger presentation1.html presentation2.html presentation3.html
```

## 处理规则

1. **标题幻灯片**
   - 保留第一个演示的标题幻灯片
   - 将其他标题转换为章节分隔页

2. **内容幻灯片**
   - 按原始顺序保留所有内容
   - 去除完全重复的幻灯片

3. **图表处理**
   - 保留所有图表配置
   - 确保图表 ID 唯一性

4. **样式整合**
   - 使用统一的 McKinsey 调色板
   - 保持一致的排版层次
