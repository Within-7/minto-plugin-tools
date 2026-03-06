# 完整提取示例：品牌详情模式

本文档展示从输入到输出的完整流程，供AI参考。

---

## 输入

```
PPT路径：/Users/mac/Downloads/brand.pptx
输出目录：/Users/mac/Downloads/output
品牌名称：Bloomscape（从PPT中提取）
品牌序号：323（从PPT中提取）
```

---

## Step 1：解包PPT

```bash
unzip "/Users/mac/Downloads/brand.pptx" -d ./workspace/unpacked
```

**解包后目录结构**：
```
unpacked/
├── ppt/
│   ├── slides/
│   │   ├── slide1.xml
│   │   ├── slide2.xml
│   │   └── ...
│   ├── slides/_rels/
│   │   ├── slide1.xml.rels
│   │   ├── slide2.xml.rels
│   │   └── ...
│   └── media/
│       ├── image1.jpeg
│       ├── image2.png
│       └── ...
└── ...
```

---

## Step 2：扫描文本，定位相关Slide

**执行命令**：
```bash
for i in $(seq 1 40); do
  echo "=== Slide $i ==="
  grep -o '<a:t>[^<]*</a:t>' ppt/slides/slide$i.xml 2>/dev/null | sed 's/<a:t>//g; s/<\/a:t>//g' | tr '\n' ' '
  echo ""
done
```

**扫描结果及判断**：

| Slide | 文本内容 | 判断 |
|-------|----------|------|
| 1 | Within-7.com 任小姐跨境品牌研究院 | 封面页，跳过 |
| **2** | Bloomscape 创立于 2017 年 美国密歇根州 | ✅ **品牌概览页**，提取Logo |
| 3 | 品牌介绍 产品定位 用户定位 | 目录页，跳过 |
| **6** | 流量来源分布 11,200 日活 网站基础数据 | ✅ **流量分布页**，提取柱状图 |
| **8** | 爆款产品 室内绿植 价格 $49 - $229 | ✅ **产品展示页**，提取产品图 |

---

## Step 3：绘制Slide 2布局结构

**执行命令**：
```bash
python3 << 'EOF'
import re

# 1. 解析rels获取rId到图片的映射
with open('ppt/slides/_rels/slide2.xml.rels', 'r') as f:
    rels_content = f.read()

rid_to_image = {}
for match in re.finditer(r'Id="(rId\d+)"[^>]*Target="../media/(image\d+\.\w+)"', rels_content):
    rid_to_image[match.group(1)] = match.group(2)

print("rId映射：", rid_to_image)

# 2. 解析slide XML获取图片位置
with open('ppt/slides/slide2.xml', 'r') as f:
    content = f.read()

pics = []
for pic_match in re.finditer(r'<p:pic[^>]*>(.*?)</p:pic>', content, re.DOTALL):
    rid_match = re.search(r'r:embed="(rId\d+)"', pic_match.group(1))
    off_match = re.search(r'<a:off x="(\d+)" y="(\d+)"', pic_match.group(1))
    ext_match = re.search(r'<a:ext cx="(\d+)" cy="(\d+)"', pic_match.group(1))

    if rid_match and off_match and ext_match:
        rid = rid_match.group(1)
        x = int(off_match.group(1)) / 9525  # EMU转像素
        y = int(off_match.group(2)) / 9525
        cx = int(ext_match.group(1)) / 9525
        cy = int(ext_match.group(2)) / 9525
        img = rid_to_image.get(rid, 'unknown')
        pics.append({'rid': rid, 'img': img, 'x': x, 'y': y, 'cx': cx, 'cy': cy})

for p in pics:
    print(f"  {p['rid']} -> {p['img']}: pos=({p['x']:.0f}, {p['y']:.0f}), size=({p['cx']:.0f}x{p['cy']:.0f})")
EOF
```

**输出结果**：
```
rId映射： {'rId1': 'image3.jpeg', 'rId2': 'image2.png', 'rId3': 'image4.png', 'rId8': 'image9.png', ...}
  rId1 -> image3.jpeg: pos=(629, 35), size=(689x689)
  rId2 -> image2.png: pos=(7, 4), size=(34x34)
  rId3 -> image4.png: pos=(629, 44), size=(679x676)
  rId8 -> image9.png: pos=(172, 60), size=(327x79)
```

**绘制Markdown布局图**：
```markdown
## Slide 2 布局结构（品牌概览页）

| 图片 | rId | 文件 | 位置 (x, y) | 尺寸 | 用途判断 |
|------|-----|------|-------------|------|----------|
| 1 | rId2 | image2.png | (7, 4) | 34×34 | ⚠️ 左上角小图标，忽略 |
| 2 | rId8 | image9.png | (172, 60) | 327×79 | ✅ **品牌Logo** |
| 3 | rId1 | image3.jpeg | (629, 35) | 689×689 | 右侧背景图，可选提取 |
| 4 | rId3 | image4.png | (629, 44) | 679×676 | 右侧图片，可选提取 |

### 布局示意图
┌─────────────────────────────────────────────────────────────┐
│ [34×34]                              Within-7.com           │
│ image2  任小姐 | 出海战略咨询                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│         ┌─────────────────────────┐                         │
│         │  [品牌Logo image9.png]  │                         │
│         │  Bloomscape (327×79)    │                         │
│         └─────────────────────────┘                         │
│                                                             │
│         品牌概览                                            │
│         ────────                                            │
│                                                             │
│   [icon]  创立于 2017 年                                    │
│   [icon]  美国密歇根州                                       │
│   [icon]  2022 年销售额约 5000 万美金                        │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                    [背景图 image3.jpeg]      │
│                                     右侧大图 689×689          │
└─────────────────────────────────────────────────────────────┘
```

---

## Step 4：确认图片对应关系

**向用户展示**：
```
我识别到以下图片：
- 品牌Logo: image9.png (327×79) - 位于品牌名区域，位置(172, 60)
- 流量分布图: image12.png (788×611) - 来自Slide 6流量分布页
- 产品展示图: image16.png (1965×1298) - 来自Slide 8爆款产品页

请确认是否正确？
```

**用户确认后继续**

---

## Step 5：复制图片到目标目录

```bash
# 创建目录
mkdir -p "/Users/mac/Downloads/output/assets/brand_details"

# 复制并重命名图片
cp ppt/media/image9.png "/Users/mac/Downloads/output/assets/brand_details/bloomscape_logo.png"
cp ppt/media/image12.png "/Users/mac/Downloads/output/assets/brand_details/bloomscape_traffic_distribution.png"
cp ppt/media/image16.png "/Users/mac/Downloads/output/assets/brand_details/bloomscape_product.png"
```

---

## Step 6：提取文本数据

**从Slide 2提取**：
- 品牌名称：Bloomscape
- 创立时间：2017年
- 创立地点：美国密歇根州
- 销售额：2022年约5000万美金
- 品牌使命：帮助加强用户与植物的关系...

**从Slide 8提取**：
- 产品名称：室内绿植（Indoor Plants）
- 产品价格：$49 - $229
- 产品特点：7条

**从Slide 6提取**：
- 日均活跃用户：14,637
- 平均停留时长：01:11
- 人均访问页面：1.87
- 用户跳出率：65.54%

---

## Step 7：生成Markdown文件

**输出路径**：`/Users/mac/Downloads/output/data/brand_bloomscape_detail.md`

```markdown
# 品牌详情：Bloomscape
品牌序号：323

## 品牌背景与定位
- 基本信息：创立于2017年，美国密歇根州，2022年销售额约5000万美元，创始人来自温室种植家族
- 用户画像：核心用户是家居博主，喜欢用植物装饰室内，需要容易照顾、品相好、上镜的植物
- 品牌使命："帮助加强用户与植物的关系。通过将健康的、现成的植物送到家门口..."
- 竞争优势：直接从温室发货、3-4天快速配送、创新包装保护植物、专业养植知识支持
- 官网：https://bloomscape.com/

## 爆款产品
- 产品名称：室内绿植（Indoor Plants）
- 产品价格：$49 - $229
- 产品特点（7条）：
  1. 直接从温室发货，运输快速
  2. 植物在运输过程中都经过精心呵护
  3. 创新包装将植物牢固地固定到位
  4. 新手友好分类推荐
  5. 能够快速帮助非专业养植用户挑选
  6. 丰富的品种选择
  7. 每个产品都有用户评论数参考

## 流量来源分布
![流量分布图](../assets/brand_details/bloomscape_traffic_distribution.png)

## 核心运营指标
| 指标 | 数值 |
|-----|-----|
| 日均活跃用户 | 14,637 |
| 平均停留时长 | 01:11 |
| 人均访问页面 | 1.87 |
| 用户跳出率 | 65.54% |
```

---

## 最终输出结构

```
/Users/mac/Downloads/output/
├── assets/
│   └── brand_details/
│       ├── bloomscape_logo.png              # 7.7 KB
│       ├── bloomscape_traffic_distribution.png  # 128 KB
│       └── bloomscape_product.png            # 1965 KB
└── data/
    └── brand_bloomscape_detail.md            # 2.1 KB
```

---

## 自检清单

提取完成后，检查以下项目：

- [ ] Logo图片是否正确（不是左上角小图标）
- [ ] 流量图是否为柱状图（不是饼图）
- [ ] 产品图是否为实际产品展示（不是装饰图）
- [ ] Markdown中图片路径是否正确（`../assets/brand_details/`）
- [ ] 品牌名称和序号是否正确提取
- [ ] 7个产品特点是否都提取到了
- [ ] 4个KPI指标是否都提取到了
