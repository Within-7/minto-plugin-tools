# 提取自检清单

在执行品牌信息提取任务时，按照以下清单逐项检查，确保提取准确。

---

## 通用检查项（所有模式）

### 阶段1：解包后检查

```
□ 解包目录是否存在 ppt/slides/ 目录？
□ 解包目录是否存在 ppt/media/ 目录？
□ 解包目录是否存在 ppt/slides/_rels/ 目录？
□ 是否成功识别了slide总数？
```

**如果检查失败**：
- 确认PPT文件路径正确
- 确认unzip命令执行成功
- 检查是否有读取权限

---

### 阶段2：定位Slide后检查

```
□ 是否找到了所有目标slide？
□ 关键词匹配是否准确？
□ 是否有遗漏的slide？
□ 是否有误判的slide？
```

**如果找不到目标slide**：
- 使用更通用的关键词重新搜索
- 扫描所有slide文本，手动定位
- 与用户确认PPT结构

---

### 阶段3：图片识别后检查

```
□ 是否绘制了Markdown布局结构图？
□ 是否列出了每个图片的：位置、尺寸、rId、文件名？
□ 是否判断了每个图片的用途？
□ 是否排除了装饰图标（<50×50）？
□ 是否用Read工具查看了关键图片？
```

**如果图片识别不确定**：
- 必须用Read查看实际图片内容
- 与用户确认后再复制
- 记录不确定的原因

---

### 阶段4：用户确认后检查

```
□ 是否向用户展示了图片识别结果？
□ 用户是否确认了图片对应关系？
□ 是否等待用户确认后再复制？
```

**禁止行为**：
- ❌ 在用户确认前就复制图片
- ❌ 假设图片用途而不验证
- ❌ 忽略用户的反馈意见

---

## 模式一：品牌目录检查项

```
□ 是否只提取了1张图片？
□ 图片是否为品牌主图/封面图？
□ 图片是否来自Slide 1（封面页）？
□ JSON文件是否放在 assets/brands/ 目录？
□ JSON是否包含 name, nameCN, description？
□ description 是否简短（5-10字）？
```

---

## 模式二：品牌详情检查项

```
□ 是否提取了3张图片？
  □ {brand}_logo.png - 品牌Logo
  □ {brand}_product.png - 产品展示图
  □ {brand}_traffic_distribution.png - 流量分布柱状图

□ Logo是否不是左上角小图标？
□ 流量图是否为柱状图（不是饼图）？
□ 产品图是否为实际产品（不是装饰图）？

□ 图片是否放在 assets/brand_details/ 目录？
□ Markdown是否放在 data/ 目录？
□ Markdown图片路径是否使用相对路径 ../assets/brand_details/ ？
□ Markdown是否包含7个产品特点？
□ Markdown是否包含4个KPI指标？
```

---

## 模式三：品牌分析检查项

```
□ 是否提取了6张图片？
  □ {brand}_user_position.png - 用户定位饼图
  □ {brand}_persona_1.png - 用户画像1
  □ {brand}_persona_2.png - 用户画像2
  □ {brand}_traffic_model.png - 流量模型图
  □ {brand}_backlink_source.png - 外链来源饼图
  □ {brand}_backlink_keywords.png - 外链关键词柱状图

□ 用户定位图是否为饼图/圆圈图？
□ 流量模型图是否为流程图？
□ 外链来源图是否为饼图？
□ 外链关键词图是否为横向柱状图？

□ 图片是否放在 assets/brand_analysis/ 目录？
□ JSON是否放在 data/ 目录？
□ JSON图片路径是否使用相对路径 ../assets/brand_analysis/ ？
```

---

## 模式四：品牌社媒检查项

```
□ 是否提取了7张图片？
  □ {brand}_kol_data.png - KOL合作数据
  □ {brand}_instagram.png - Instagram社媒
  □ {brand}_facebook.png - Facebook社媒
  □ {brand}_youtube.png - YouTube社媒
  □ {brand}_activity_1.png - 营销活动1
  □ {brand}_activity_2.png - 营销活动2
  □ {brand}_activity_3.png - 营销活动3

□ KOL数据图是否为表格/图表？
□ 社媒截图是否为实际平台界面？
□ 活动截图是否为营销活动内容？

□ 图片是否放在 assets/brand_social/ 目录？
□ JSON是否放在 data/ 目录？
□ JSON图片路径是否使用相对路径 ../assets/brand_social/ ？
```

---

## 最终输出检查

```
□ 输出目录结构是否正确？
  □ assets/brands/ (品牌目录)
  □ assets/brand_details/ (品牌详情)
  □ assets/brand_analysis/ (品牌分析)
  □ assets/brand_social/ (品牌社媒)
  □ data/ (数据文件)

□ 文件命名是否符合规范？
  □ 小写字母
  □ 下划线分隔
  □ 品牌名在前

□ 图片是否成功复制？
  □ 文件大小 > 0
  □ 可以正常打开

□ 数据文件格式是否正确？
  □ JSON格式有效
  □ Markdown格式正确
  □ 中文无乱码
```

---

## 错误恢复流程

如果检查发现问题：

```
1. 记录具体问题
2. 分析问题原因
3. 确定修复方案
4. 执行修复
5. 重新检查
6. 与用户确认
```

### 常见问题修复

| 问题 | 修复方法 |
|------|----------|
| 图片识别错误 | 重新分析布局，用Read查看图片内容 |
| 文件放错目录 | 移动到正确目录 |
| 文件命名不规范 | 重命名文件 |
| JSON格式错误 | 修复JSON语法 |
| 图片路径错误 | 修正相对路径 |
