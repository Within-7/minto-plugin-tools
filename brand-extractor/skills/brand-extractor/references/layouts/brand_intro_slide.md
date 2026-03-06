# 品牌概览页布局参考

## 识别关键词
- `品牌概览`
- `品牌简介`
- `创立于`
- `品牌使命`
- `融资情况`

## ⚠️ 重要：此页面包含多个图片，必须先绘制布局

### 典型图片构成（以Bloomscape案例为例）

| 位置 | 尺寸特征 | rId映射 | 用途 | 是否提取 |
|------|----------|---------|------|----------|
| 左上角 (6,4) | <50×50 | → image2.png | 公司小logo | ❌ 忽略 |
| 品牌名区域 (172,60) | 300-400×60-100 | → image9.png | **品牌Logo** | ✅ 提取 |
| 右侧全屏 (680,12) | >500×500 | → image3.jpeg | 品牌主图/背景 | 视需求 |
| 行首图标 (40,183) | 30×35 | → image4.png | 装饰图标 | ❌ 忽略 |
| 行首图标 (40,231) | 30×35 | → image5.png | 装饰图标 | ❌ 忽略 |
| ... | 30×35 | → image6-8.png | 装饰图标 | ❌ 忽略 |

### 关键发现

**❌ 错误做法**：假设 image1/image2 是Logo
**✅ 正确做法**：通过XML位置+尺寸+rId映射确定

### 品牌Logo识别规则

```
1. 排除左上角小图（位置 x<50, y<50, 尺寸<50×50）
2. 找到位置在品牌名区域的图片：
   - 位置：x 在 100-300 之间
   - 位置：y 在 50-150 之间
   - 尺寸：宽度 200-450，高度 40-150
   - 比例：宽>高（Logo通常是横向的）
3. 通过rId映射到实际图片文件
```

## 标准布局结构

```
┌─────────────────────────────────────────────────────────────────────┐
│ [34×34]                                      Within-7.com           │
│ image2    任小姐 | 出海战略咨询                                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│              ┌─────────────────────────────────┐                    │
│              │     [品牌Logo image9.png]       │                    │
│              │     Bloomscape (327×79)         │                    │
│              │     位置: x=172, y=60           │                    │
│              └─────────────────────────────────┘                    │
│                                                                     │
│              品牌概览                                                │
│              ────────                                               │
│                                                                     │
│   [icon]   https://bloomscape.com/     ← image4 (忽略)             │
│   [icon]   创立于 2017 年               ← image5 (忽略)             │
│   [icon]   美国密歇根州                  ← image6 (忽略)             │
│   [icon]   2022 年销售额约 5000 万美金   ← image7 (忽略)             │
│   [icon]   核心产品是室内绿植            ← image8 (忽略)             │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   融资情况：...                                                     │
│   品牌使命：...                                                     │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                             [品牌主图 image3.jpeg]   │
│                                              右侧大图 608×760         │
└─────────────────────────────────────────────────────────────────────┘
```

## 图片提取检查清单

提取前必须完成：

- [ ] 解析 slide XML 获取所有元素位置
- [ ] 解析 rels 文件获取 rId → 图片文件 映射
- [ ] 绘制 Markdown 布局图（包含位置、尺寸）
- [ ] 标注每个图片的用途
- [ ] 与用户确认图片对应关系
- [ ] 确认后再复制图片

## Python代码示例

```python
import xml.etree.ElementTree as ET
import os

def analyze_brand_overview_slide(slide_path, rels_path, media_dir):
    """
    分析品牌概览页，返回Logo图片文件名
    """
    # 1. 解析slide XML获取图片位置
    tree = ET.parse(slide_path)
    root = tree.getroot()

    # 2. 解析rels获取rId映射
    rels_tree = ET.parse(rels_path)
    rid_to_image = {}
    for rel in rels_tree.iter():
        target = rel.get('Target', '')
        if 'media/image' in target:
            rid = rel.get('Id', '')
            rid_to_image[rid] = target.split('/')[-1]

    # 3. 遍历所有图片元素，找到品牌Logo
    logo_candidates = []
    for elem in root.iter():
        # 获取位置和尺寸
        off = elem.find('.//{ns}off')
        ext = elem.find('.//{ns}ext')
        if off is not None and ext is not None:
            x = int(off.get('x', 0)) // 9525  # EMU转像素
            y = int(off.get('y', 0)) // 9525
            cx = int(ext.get('cx', 0)) // 9525
            cy = int(ext.get('cy', 0)) // 9525

            # 判断是否为品牌Logo
            if 100 < x < 300 and 50 < y < 150 and cx > 150 and 40 < cy < 150:
                # 获取rId
                rid = elem.get('{ns}embed', '')
                if rid in rid_to_image:
                    logo_candidates.append({
                        'image': rid_to_image[rid],
                        'position': (x, y),
                        'size': (cx, cy)
                    })

    return logo_candidates
```

## 需要提取的内容

| 类型 | 内容 | 存入 |
|------|------|------|
| 图片 | 品牌Logo | `assets/brand_details/{brand}_logo.png` |
| 文本 | 基本信息（创立时间、地点、销售额） | Markdown |
| 文本 | 品牌使命 | Markdown |
| 文本 | 融资情况 | Markdown |
| 文本 | 官网URL | Markdown |
