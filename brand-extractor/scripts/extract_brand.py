#!/usr/bin/env python3
"""
PPT品牌信息提取辅助脚本
用于从解包后的PPT XML文件中提取文本内容和图片关系
"""

import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def extract_text_from_slide(slide_path):
    """从幻灯片XML中提取所有文本"""
    texts = []
    try:
        tree = ET.parse(slide_path)
        root = tree.getroot()
        for elem in root.iter():
            if elem.text and elem.text.strip():
                text = elem.text.strip()
                if len(text) > 1:
                    texts.append(text)
    except Exception as e:
        print(f"Error reading {slide_path}: {e}")
    return texts


def get_slide_images(slide_num, unpacked_dir):
    """获取指定幻灯片关联的所有图片"""
    rels_path = os.path.join(unpacked_dir, f"ppt/slides/_rels/slide{slide_num}.xml.rels")
    images = []

    if not os.path.exists(rels_path):
        return images

    try:
        tree = ET.parse(rels_path)
        root = tree.getroot()

        # 命名空间
        ns = {'rel': 'http://schemas.openxmlformats.org/package/2006/relationships'}

        for rel in root.findall('.//rel:Relationship', ns):
            rel_type = rel.get('Type', '')
            target = rel.get('Target', '')

            # 检查是否为图片关系
            if 'image' in rel_type and target:
                # 获取图片完整路径
                img_path = os.path.join(unpacked_dir, 'ppt/slides', target)
                img_path = os.path.normpath(img_path)

                if os.path.exists(img_path):
                    size = os.path.getsize(img_path)
                    images.append({
                        'path': img_path,
                        'filename': os.path.basename(target),
                        'size': size,
                        'size_str': format_size(size)
                    })
    except Exception as e:
        print(f"Error reading {rels_path}: {e}")

    return images


def format_size(size):
    """格式化文件大小"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.1f}{unit}"
        size /= 1024
    return f"{size:.1f}TB"


def scan_all_slides(unpacked_dir):
    """扫描所有幻灯片，提取文本和图片"""
    slides_dir = os.path.join(unpacked_dir, 'ppt/slides')

    if not os.path.exists(slides_dir):
        print(f"Error: Slides directory not found: {slides_dir}")
        return {}

    slides_data = {}
    slide_files = sorted([f for f in os.listdir(slides_dir) if f.startswith('slide') and f.endswith('.xml')])

    for slide_file in slide_files:
        slide_num = int(''.join(filter(str.isdigit, slide_file)))
        slide_path = os.path.join(slides_dir, slide_file)

        texts = extract_text_from_slide(slide_path)
        images = get_slide_images(slide_num, unpacked_dir)

        slides_data[slide_num] = {
            'file': slide_file,
            'texts': texts,
            'images': images
        }

    return slides_data


def find_content_slides(slides_data, keywords):
    """根据关键词查找包含特定内容的幻灯片"""
    matches = []

    for slide_num, data in slides_data.items():
        text_combined = ' '.join(data['texts']).lower()

        for keyword in keywords:
            if keyword.lower() in text_combined:
                matches.append({
                    'slide': slide_num,
                    'keyword': keyword,
                    'preview': data['texts'][:5]  # 前5个文本片段
                })
                break

    return matches


def print_slide_summary(slides_data):
    """打印幻灯片摘要"""
    print(f"\n找到 {len(slides_data)} 张幻灯片:\n")
    print("-" * 60)

    for slide_num in sorted(slides_data.keys()):
        data = slides_data[slide_num]
        texts = data['texts']
        images = data['images']

        # 获取第一个有意义的文本作为标题
        title = next((t for t in texts if len(t) > 2 and not t.isdigit()), "无标题")

        print(f"Slide {slide_num}: {title[:30]}...")
        print(f"  文本片段: {len(texts)}")
        print(f"  图片数量: {len(images)}")

        if images:
            for img in images:
                print(f"    - {img['filename']} ({img['size_str']})")

        print()


def main():
    if len(sys.argv) < 2:
        print("用法: python extract_brand.py <unpacked_dir>")
        print("示例: python extract_brand.py ./workspace/unpacked")
        sys.exit(1)

    unpacked_dir = sys.argv[1]

    if not os.path.exists(unpacked_dir):
        print(f"Error: Directory not found: {unpacked_dir}")
        sys.exit(1)

    print(f"扫描目录: {unpacked_dir}")

    slides_data = scan_all_slides(unpacked_dir)
    print_slide_summary(slides_data)

    # 查找关键内容
    print("\n" + "=" * 60)
    print("内容定位:")
    print("=" * 60)

    # 品牌相关关键词
    brand_keywords = ['品牌', '简介', '创立', '使命', '背景', '定位']
    brand_matches = find_content_slides(slides_data, brand_keywords)
    if brand_matches:
        print("\n【品牌信息】可能在以下幻灯片:")
        for m in brand_matches:
            print(f"  Slide {m['slide']}: 匹配关键词 '{m['keyword']}'")

    # 产品相关关键词
    product_keywords = ['产品', '爆款', '展示', '特点', '价格']
    product_matches = find_content_slides(slides_data, product_keywords)
    if product_matches:
        print("\n【产品信息】可能在以下幻灯片:")
        for m in product_matches:
            print(f"  Slide {m['slide']}: 匹配关键词 '{m['keyword']}'")

    # KPI相关关键词
    kpi_keywords = ['指标', '活跃', '停留', '跳出', '访问', '流量']
    kpi_matches = find_content_slides(slides_data, kpi_keywords)
    if kpi_matches:
        print("\n【KPI指标】可能在以下幻灯片:")
        for m in kpi_matches:
            print(f"  Slide {m['slide']}: 匹配关键词 '{m['keyword']}'")


if __name__ == '__main__':
    main()
