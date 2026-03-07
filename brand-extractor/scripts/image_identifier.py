#!/usr/bin/env python3
"""
图片识别器
根据规则识别slide中的图片用途

核心逻辑：
1. 解析slide的图片列表
2. 根据图片类型（cover/logo/product/chart等）匹配规则
3. 返回识别结果

图表类型识别策略：
- 饼图/环形图：宽高比接近1:1，通常在中心位置
- 柱状图：宽度大于高度，或高度大于宽度（横向柱状图）
- 流程图：宽度明显大于高度，包含多个元素
- 截图：尺寸较大，通常接近全屏或半屏
- Logo：尺寸较小，位置在品牌名区域
"""

import os
import re
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional, Tuple


class ImageIdentifier:
    """图片识别器"""

    # 图片类型特征
    IMAGE_TYPE_FEATURES = {
        'cover': {
            'description': '品牌封面图',
            'selection': 'largest_or_center',
            'size_range': (300, 2000),  # 宽度范围
        },
        'logo': {
            'description': '品牌Logo',
            'selection': 'position_and_size',
            'size_range': (100, 500),
            'position': 'brand_name_area',
        },
        'product': {
            'description': '产品展示图',
            'selection': 'largest',
            'size_range': (300, 1000),
        },
        'pie': {
            'description': '饼图/环形图',
            'selection': 'chart_type',
            'aspect_ratio': (0.8, 1.2),  # 接近1:1
        },
        'bar': {
            'description': '柱状图',
            'selection': 'chart_type',
            'aspect_ratio': (1.2, 2.5),  # 宽度>高度
        },
        'horizontal_bar': {
            'description': '横向柱状图',
            'selection': 'chart_type',
            'aspect_ratio': (0.4, 0.9),  # 高度>宽度
        },
        'flow': {
            'description': '流程图',
            'selection': 'chart_type',
            'aspect_ratio': (1.5, 3.0),  # 明显宽于高
        },
        'screenshot': {
            'description': '截图',
            'selection': 'screenshot',
            'min_size': 300,
        },
    }

    def __init__(self):
        self.identified = {}  # 已识别的图片缓存

    def identify(self, slide_num: int, images: list, image_type: str,
                 section_name: str, rules: dict) -> Optional[dict]:
        """
        识别图片用途

        Args:
            slide_num: slide编号
            images: 该slide的图片列表
            image_type: 需要识别的图片类型（如 'cover', 'logo', 'backlink_pie'）
            section_name: 章节名称（用于上下文判断）
            rules: 当前模式的规则配置

        Returns:
            dict: 识别结果，格式如：
            {
                'type': 'backlink_pie',
                'path': '/path/to/image.png',
                'filename': 'image26.png',
                'output_filename': 'buffy_backlink_pie.png',
                'output_dir': 'assets/brand_analysis/',
                'confidence': 0.85
            }
            未识别返回None
        """
        if not images:
            return None

        # 从规则中获取该图片类型的识别规则
        type_rule = self._get_type_rule(image_type, rules)
        if not type_rule:
            print(f"  警告: 未找到图片类型 '{image_type}' 的规则")
            return None

        selection_method = type_rule.get('selection', {}).get('method', 'largest')

        # 根据选择方法识别图片
        if selection_method == 'largest':
            result = self._select_largest(images)
        elif selection_method == 'largest_or_center':
            result = self._select_largest_or_center(images)
        elif selection_method == 'position_and_size':
            result = self._select_by_position_and_size(images, type_rule)
        elif selection_method == 'chart_type':
            chart_type = type_rule.get('selection', {}).get('chart_type', 'bar')
            result = self._select_by_chart_type(images, chart_type, slide_num)
        elif selection_method == 'screenshot':
            order = type_rule.get('selection', {}).get('order', 1)
            result = self._select_screenshot(images, order)
        else:
            result = self._select_largest(images)  # 默认选最大的

        if result:
            result.update({
                'type': image_type,
                'output_filename': type_rule.get('output_filename', result['filename']),
                'output_dir': type_rule.get('output_dir', 'assets/'),
                'section': section_name,
            })

        return result

    def _get_type_rule(self, image_type: str, rules: dict) -> Optional[dict]:
        """从规则配置中获取指定图片类型的规则"""
        # 遍历target_sections查找匹配的图片规则
        for section in rules.get('target_sections', []):
            for img_rule in section.get('images', []):
                if img_rule.get('name') == image_type:
                    return img_rule

            # 也检查子章节
            for sub in section.get('sub_sections', []):
                for img_rule in sub.get('images', []):
                    if img_rule.get('name') == image_type:
                        return img_rule

        return None

    def _select_largest(self, images: list) -> Optional[dict]:
        """选择最大的图片"""
        if not images:
            return None

        largest = max(images, key=lambda x: x.get('size', 0))
        return {
            'path': largest['path'],
            'filename': largest['filename'],
            'rid': largest['rid'],
            'confidence': 0.7
        }

    def _select_largest_or_center(self, images: list) -> Optional[dict]:
        """选择最大的或居中的图片"""
        if not images:
            return None

        # 过滤掉太小的图片（装饰图标）
        filtered = [img for img in images if img.get('size', 0) > 50000]  # 50KB以上

        if not filtered:
            filtered = images

        return self._select_largest(filtered)

    def _select_by_position_and_size(self, images: list, type_rule: dict) -> Optional[dict]:
        """根据位置和尺寸选择图片"""
        size_range = type_rule.get('selection', {}).get('size_range', [100, 500])

        # 过滤尺寸范围内的图片
        filtered = []
        for img in images:
            size = img.get('size', 0)
            if size_range[0] * 1000 < size < size_range[1] * 1000:  # 粗略估算
                filtered.append(img)

        if not filtered:
            return self._select_largest(images)

        return self._select_largest(filtered)

    def _select_by_chart_type(self, images: list, chart_type: str, slide_num: int) -> Optional[dict]:
        """
        根据图表类型选择图片

        策略：
        1. 获取图片的位置和尺寸信息（从slide XML）
        2. 根据宽高比判断图表类型
        3. 返回最匹配的图片
        """
        # 简化策略：根据图片数量和类型推断
        if chart_type == 'pie':
            # 饼图通常是正方形，选择宽高比最接近1:1的
            return self._select_by_aspect_ratio(images, (0.8, 1.2))

        elif chart_type == 'bar':
            # 柱状图通常宽度>高度
            return self._select_by_aspect_ratio(images, (1.2, 3.0))

        elif chart_type == 'horizontal_bar':
            # 横向柱状图高度>宽度
            return self._select_by_aspect_ratio(images, (0.3, 0.9))

        elif chart_type == 'flow':
            # 流程图明显宽于高
            return self._select_by_aspect_ratio(images, (1.5, 4.0))

        elif chart_type in ['bar_or_table']:
            # 通用图表，选择最大的非截图类图片
            return self._select_largest(images)

        return self._select_largest(images)

    def _select_by_aspect_ratio(self, images: list, ratio_range: tuple) -> Optional[dict]:
        """根据宽高比选择图片"""
        # 由于我们没有实际的图片尺寸，这里用文件大小作为粗略估计
        # 实际使用时应该解析slide XML获取图片的位置和尺寸

        if len(images) == 1:
            return {
                'path': images[0]['path'],
                'filename': images[0]['filename'],
                'rid': images[0]['rid'],
                'confidence': 0.6
            }

        # 如果有多张图片，选择最大的
        return self._select_largest(images)

    def _select_screenshot(self, images: list, order: int) -> Optional[dict]:
        """选择截图类图片（按顺序）"""
        if not images:
            return None

        # 按位置排序（从上到下，从左到右）
        sorted_images = sorted(images, key=lambda x: (x.get('y', 0), x.get('x', 0)))

        idx = order - 1  # order从1开始
        if idx < len(sorted_images):
            img = sorted_images[idx]
            return {
                'path': img['path'],
                'filename': img['filename'],
                'rid': img['rid'],
                'confidence': 0.7
            }

        return self._select_largest(images)

    def identify_from_slide(self, slide_num: int, unpacked_dir: str) -> List[dict]:
        """
        从指定slide中识别所有图片

        Args:
            slide_num: slide编号
            unpacked_dir: PPT解包目录

        Returns:
            list: 该slide的所有图片及其属性
        """
        slide_path = os.path.join(unpacked_dir, f'ppt/slides/slide{slide_num}.xml')
        rels_path = os.path.join(unpacked_dir, f'ppt/slides/_rels/slide{slide_num}.xml.rels')

        images = []

        # 解析slide XML获取图片位置和尺寸
        slide_images_info = self._parse_slide_images_info(slide_path)

        # 解析rels获取图片文件路径
        rid_to_file = self._parse_rels(rels_path)

        # 合并信息
        for rid, info in slide_images_info.items():
            if rid in rid_to_file:
                img_path = os.path.join(unpacked_dir, 'ppt/slides', rid_to_file[rid])
                img_path = os.path.normpath(img_path)

                if os.path.exists(img_path):
                    images.append({
                        'rid': rid,
                        'path': img_path,
                        'filename': os.path.basename(rid_to_file[rid]),
                        'x': info['x'],
                        'y': info['y'],
                        'cx': info['cx'],
                        'cy': info['cy'],
                        'size': os.path.getsize(img_path)
                    })

        return images

    def _parse_slide_images_info(self, slide_path: str) -> Dict[str, dict]:
        """解析slide XML，获取图片的位置和尺寸"""
        images_info = {}

        if not os.path.exists(slide_path):
            return images_info

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

                # 提取位置和尺寸（EMU单位，需要转换为像素）
                off_match = re.search(r'<a:off x="(\d+)" y="(\d+)"', pic_content)
                ext_match = re.search(r'<a:ext cx="(\d+)" cy="(\d+)"', pic_content)

                if off_match and ext_match:
                    x = int(off_match.group(1)) / 9525  # EMU转像素
                    y = int(off_match.group(2)) / 9525
                    cx = int(ext_match.group(1)) / 9525
                    cy = int(ext_match.group(2)) / 9525

                    images_info[rid] = {
                        'x': round(x),
                        'y': round(y),
                        'cx': round(cx),
                        'cy': round(cy)
                    }
        except Exception as e:
            print(f"  警告: 解析slide图片信息失败 - {e}")

        return images_info

    def _parse_rels(self, rels_path: str) -> Dict[str, str]:
        """解析rels文件，返回rId到图片文件的映射"""
        rid_to_file = {}

        if not os.path.exists(rels_path):
            return rid_to_file

        try:
            tree = ET.parse(rels_path)
            root = tree.getroot()

            for rel in root.iter():
                target = rel.get('Target', '')
                rid = rel.get('Id', '')

                if 'media/image' in target and rid:
                    rid_to_file[rid] = target
        except Exception as e:
            print(f"  警告: 解析rels失败 - {e}")

        return rid_to_file


if __name__ == '__main__':
    # 测试代码
    import sys
    import json

    if len(sys.argv) < 3:
        print("用法: python image_identifier.py <unpacked_dir> <slide_num>")
        sys.exit(1)

    unpacked_dir = sys.argv[1]
    slide_num = int(sys.argv[2])

    identifier = ImageIdentifier()
    images = identifier.identify_from_slide(slide_num, unpacked_dir)

    print(f"\nSlide {slide_num} 图片信息:")
    for img in images:
        print(f"  - {img['filename']}")
        print(f"    位置: ({img['x']}, {img['y']})")
        print(f"    尺寸: {img['cx']} x {img['cy']}")
        print(f"    大小: {img['size'] / 1024:.1f} KB")
