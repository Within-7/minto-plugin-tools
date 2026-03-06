#!/usr/bin/env python3
"""
PPT Slide布局分析工具
用于分析PPT中每个slide的图片布局，输出Markdown格式的布局结构

使用方法：
    python slide_analyzer.py <unpacked_dir> [slide_num]

参数：
    unpacked_dir: PPT解包后的目录路径
    slide_num: 可选，指定分析的slide编号，不指定则分析所有slide

示例：
    # 分析所有slide
    python slide_analyzer.py ./workspace/unpacked

    # 只分析slide 2
    python slide_analyzer.py ./workspace/unpacked 2

输出：
    Markdown格式的布局结构，包含每个图片的位置、尺寸和rId映射
"""

import os
import sys
import re
import xml.etree.ElementTree as ET
from pathlib import Path


def parse_rels(rels_path):
    """解析rels文件，返回rId到图片文件的映射"""
    rid_to_image = {}

    if not os.path.exists(rels_path):
        return rid_to_image

    try:
        tree = ET.parse(rels_path)
        root = tree.getroot()

        for rel in root.iter():
            target = rel.get('Target', '')
            rid = rel.get('Id', '')

            if 'media/image' in target and rid:
                # 提取图片文件名
                image_name = target.split('/')[-1]
                rid_to_image[rid] = image_name
    except Exception as e:
        print(f"  警告: 解析rels失败 - {e}")

    return rid_to_image


def extract_text_from_slide(slide_path):
    """从slide中提取所有文本"""
    texts = []

    if not os.path.exists(slide_path):
        return texts

    try:
        with open(slide_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 提取<a:t>标签中的文本
        for match in re.finditer(r'<a:t>([^<]*)</a:t>', content):
            text = match.group(1).strip()
            if text:
                texts.append(text)
    except Exception as e:
        print(f"  警告: 提取文本失败 - {e}")

    return texts


def analyze_slide_images(slide_path, rels_path):
    """分析slide中的所有图片，返回图片信息列表"""
    images = []

    # 获取rId映射
    rid_to_image = parse_rels(rels_path)

    if not os.path.exists(slide_path):
        return images

    try:
        with open(slide_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 查找所有p:pic元素
        for pic_match in re.finditer(r'<p:pic[^>]*>(.*?)</p:pic>', content, re.DOTALL):
            pic_content = pic_match.group(1)

            # 提取rId
            rid_match = re.search(r'r:embed="(rId\d+)"', pic_content)
            if not rid_match:
                continue
            rid = rid_match.group(1)

            # 提取位置和尺寸
            off_match = re.search(r'<a:off x="(\d+)" y="(\d+)"', pic_content)
            ext_match = re.search(r'<a:ext cx="(\d+)" cy="(\d+)"', pic_content)

            if off_match and ext_match:
                x = int(off_match.group(1)) / 9525  # EMU转像素
                y = int(off_match.group(2)) / 9525
                cx = int(ext_match.group(1)) / 9525
                cy = int(ext_match.group(2)) / 9525

                image_file = rid_to_image.get(rid, 'unknown')

                # 判断图片用途
                purpose = judge_image_purpose(x, y, cx, cy)

                images.append({
                    'rid': rid,
                    'image': image_file,
                    'x': round(x),
                    'y': round(y),
                    'cx': round(cx),
                    'cy': round(cy),
                    'purpose': purpose
                })
    except Exception as e:
        print(f"  警告: 分析图片失败 - {e}")

    # 按位置排序（从上到下，从左到右）
    images.sort(key=lambda i: (i['y'], i['x']))

    return images


def judge_image_purpose(x, y, cx, cy):
    """根据位置和尺寸判断图片用途"""

    # 装饰小图标：尺寸小于50x50
    if cx < 50 and cy < 50:
        return "⚠️ 忽略（装饰小图标）"

    # 品牌Logo：位于品牌名区域，横向矩形
    if 100 < x < 400 and 40 < y < 200 and cx > 150 and 30 < cy < 150:
        return "✅ 品牌Logo"

    # 产品展示图：大尺寸图片
    if cx > 300 and cy > 300:
        return "可能是产品图/背景图"

    # 流量图/饼图：中等尺寸
    if 300 < cx < 900 and 200 < cy < 700:
        return "可能是图表"

    return "待确认"


def generate_layout_markdown(slide_num, texts, images):
    """生成Markdown格式的布局结构"""
    md = f"## Slide {slide_num} 布局结构\n\n"

    # 文本摘要（前200字符）
    text_summary = ' '.join(texts)[:200]
    md += f"**文本摘要**: {text_summary}...\n\n"

    # 图片表格
    if images:
        md += "| 序号 | rId | 图片文件 | 位置 (x, y) | 尺寸 (w×h) | 用途判断 |\n"
        md += "|------|-----|----------|-------------|------------|----------|\n"

        for i, img in enumerate(images, 1):
            md += f"| {i} | {img['rid']} | {img['image']} | ({img['x']}, {img['y']}) | {img['cx']}×{img['cy']} | {img['purpose']} |\n"
    else:
        md += "*此slide没有图片*\n"

    return md


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    unpacked_dir = sys.argv[1]
    specific_slide = int(sys.argv[2]) if len(sys.argv) > 2 else None

    slides_dir = os.path.join(unpacked_dir, 'ppt/slides')
    rels_dir = os.path.join(unpacked_dir, 'ppt/slides/_rels')

    if not os.path.isdir(slides_dir):
        print(f"错误: 找不到slides目录 - {slides_dir}")
        sys.exit(1)

    # 获取所有slide文件
    slide_files = sorted([f for f in os.listdir(slides_dir) if f.startswith('slide') and f.endswith('.xml')],
                        key=lambda x: int(re.search(r'\d+', x).group()))

    print(f"# PPT Slide布局分析报告\n")
    print(f"解包目录: {unpacked_dir}")
    print(f"Slide总数: {len(slide_files)}\n")
    print("---\n")

    for slide_file in slide_files:
        slide_num = int(re.search(r'\d+', slide_file).group())

        # 如果指定了slide，只分析那个
        if specific_slide and slide_num != specific_slide:
            continue

        slide_path = os.path.join(slides_dir, slide_file)
        rels_path = os.path.join(rels_dir, f"slide{slide_num}.xml.rels")

        print(f"## Slide {slide_num}\n")

        # 提取文本
        texts = extract_text_from_slide(slide_path)

        # 分析图片
        images = analyze_slide_images(slide_path, rels_path)

        # 生成布局报告
        print(generate_layout_markdown(slide_num, texts, images))
        print()


if __name__ == '__main__':
    main()
