#!/usr/bin/env python3
"""
TOC（目录）解析器
解析PPT的目录页，建立章节名称到slide范围的映射

核心逻辑：
1. 定位TOC页（通常是Slide 4，特征是包含"报告目录"或"目录"）
2. 提取目录结构（章节名称、层级关系）
3. 根据目录结构，估算每个章节对应的slide范围
"""

import os
import re
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional, Tuple


class TOCParser:
    """目录解析器"""

    def __init__(self):
        self.toc_slide_num = None
        self.toc_structure = {}

    def parse(self, unpacked_dir: str) -> dict:
        """
        解析PPT目录结构

        Args:
            unpacked_dir: PPT解包后的目录路径

        Returns:
            dict: 目录结构，格式如下：
            {
                'toc_slide': 4,
                'total_slides': 32,
                'sections': [
                    {
                        'name': '品牌介绍',
                        'level': 1,
                        'slides': [5, 6, 7],  # 对应的slide范围
                        'sub_sections': []
                    },
                    ...
                ]
            }
        """
        self.unpacked_dir = unpacked_dir

        # Step 1: 定位TOC页
        self.toc_slide_num = self._find_toc_slide()
        if not self.toc_slide_num:
            print("警告: 未找到目录页，使用默认结构")
            return self._get_default_structure()

        print(f"  TOC页定位: Slide {self.toc_slide_num}")

        # Step 2: 解析目录结构
        toc_items = self._parse_toc_content(self.toc_slide_num)
        print(f"  TOC内容: {len(toc_items)} 个章节")

        # Step 3: 获取总slide数
        total_slides = self._get_total_slides()

        # Step 4: 估算每个章节的slide范围
        sections = self._estimate_slide_ranges(toc_items, total_slides)

        self.toc_structure = {
            'toc_slide': self.toc_slide_num,
            'total_slides': total_slides,
            'sections': sections
        }

        return self.toc_structure

    def _find_toc_slide(self) -> Optional[int]:
        """
        定位TOC页

        策略：
        1. 扫描前10个slide
        2. 查找包含"报告目录"、"目录"等关键词的slide
        3. 通常在Slide 4

        Returns:
            int: TOC页的slide编号，未找到返回None
        """
        toc_keywords = ['报告目录', '目录', 'content', '目录']

        for slide_num in range(1, 11):  # 扫描前10页
            texts = self._extract_slide_texts(slide_num)
            text_combined = ' '.join(texts).lower()

            for keyword in toc_keywords:
                if keyword.lower() in text_combined:
                    # 额外验证：目录页通常有多个章节编号
                    if self._has_chapter_numbers(texts):
                        return slide_num

        return None

    def _has_chapter_numbers(self, texts: list) -> bool:
        """检查文本中是否包含章节编号（如 1. 2. 3.）"""
        count = 0
        for text in texts:
            # 匹配 "1." "2." 等章节编号
            if re.match(r'^\d+\.$', text.strip()):
                count += 1
            if count >= 3:  # 至少3个章节编号
                return True
        return False

    def _parse_toc_content(self, slide_num: int) -> List[dict]:
        """
        解析TOC页的内容，提取章节列表

        Args:
            slide_num: TOC页的slide编号

        Returns:
            list: 章节列表，格式如：
            [
                {'name': '品牌介绍', 'level': 1, 'sub_items': []},
                {'name': '产品定位', 'level': 1, 'sub_items': []},
                ...
            ]
        """
        texts = self._extract_slide_texts(slide_num)
        toc_items = []

        # 解析章节结构
        current_main = None
        for i, text in enumerate(texts):
            text = text.strip()

            # 匹配主章节 "1. 品牌介绍"
            main_match = re.match(r'^(\d+)\.\s*(.+)$', text)
            if main_match:
                section_name = main_match.group(2).strip()
                current_main = {
                    'name': section_name,
                    'level': 1,
                    'sub_items': []
                }
                toc_items.append(current_main)
                continue

            # 匹配子章节 "• SEO分析"
            if text.startswith('•') and current_main:
                sub_name = text.lstrip('•').strip()
                current_main['sub_items'].append({
                    'name': sub_name,
                    'level': 2
                })

        return toc_items

    def _extract_slide_texts(self, slide_num: int) -> List[str]:
        """从slide中提取所有文本"""
        slide_path = os.path.join(self.unpacked_dir, f'ppt/slides/slide{slide_num}.xml')
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

    def _get_total_slides(self) -> int:
        """获取PPT的总slide数"""
        slides_dir = os.path.join(self.unpacked_dir, 'ppt/slides')
        slide_files = [f for f in os.listdir(slides_dir) if f.startswith('slide') and f.endswith('.xml')]
        return len(slide_files)

    def _estimate_slide_ranges(self, toc_items: List[dict], total_slides: int) -> List[dict]:
        """
        估算每个章节的slide范围

        策略：
        1. TOC页通常是Slide 4
        2. 内容从Slide 5开始
        3. 根据章节数量均分slides（简化策略，后续可优化）

        Args:
            toc_items: 章节列表
            total_slides: 总slide数

        Returns:
            list: 带slide范围的章节列表
        """
        if not toc_items:
            return []

        # 内容起始slide（TOC之后）
        content_start = self.toc_slide_num + 1
        content_slides = total_slides - content_start + 1

        # 简化策略：按章节数均分
        sections_count = len(toc_items)
        slides_per_section = content_slides // sections_count

        sections = []
        for i, item in enumerate(toc_items):
            start_slide = content_start + i * slides_per_section
            end_slide = start_slide + slides_per_section - 1

            # 最后一个章节延伸到末尾
            if i == sections_count - 1:
                end_slide = total_slides

            section = {
                'name': item['name'],
                'level': item['level'],
                'slides': list(range(start_slide, end_slide + 1)),
                'sub_sections': []
            }

            # 处理子章节（如果有）
            if item.get('sub_items'):
                sub_items = item['sub_items']
                sub_slides_per_section = slides_per_section // max(len(sub_items), 1)

                for j, sub_item in enumerate(sub_items):
                    sub_start = start_slide + j * sub_slides_per_section
                    sub_end = sub_start + sub_slides_per_section - 1

                    if j == len(sub_items) - 1:
                        sub_end = end_slide

                    section['sub_sections'].append({
                        'name': sub_item['name'],
                        'level': sub_item['level'],
                        'slides': list(range(sub_start, sub_end + 1))
                    })

            sections.append(section)

        return sections

    def _get_default_structure(self) -> dict:
        """返回默认的目录结构（当TOC解析失败时使用）"""
        return {
            'toc_slide': 4,
            'total_slides': 20,
            'sections': [
                {'name': '品牌介绍', 'level': 1, 'slides': list(range(5, 8)), 'sub_sections': []},
                {'name': '产品定位', 'level': 1, 'slides': list(range(8, 11)), 'sub_sections': []},
                {'name': '用户定位', 'level': 1, 'slides': list(range(11, 14)), 'sub_sections': []},
                {'name': '流量模型', 'level': 1, 'slides': list(range(14, 17)), 'sub_sections': []},
                {'name': '基石流量', 'level': 1, 'slides': list(range(17, 20)), 'sub_sections': []},
            ]
        }

    def find_section(self, section_name: str) -> Optional[dict]:
        """
        根据章节名称查找章节信息

        Args:
            section_name: 章节名称（支持模糊匹配）

        Returns:
            dict: 章节信息，未找到返回None
        """
        for section in self.toc_structure.get('sections', []):
            if section_name.lower() in section.get('name', '').lower():
                return section

            # 也搜索子章节
            for sub in section.get('sub_sections', []):
                if section_name.lower() in sub.get('name', '').lower():
                    return sub

        return None


if __name__ == '__main__':
    # 测试代码
    import sys

    if len(sys.argv) < 2:
        print("用法: python toc_parser.py <unpacked_dir>")
        sys.exit(1)

    parser = TOCParser()
    result = parser.parse(sys.argv[1])

    print("\n解析结果:")
    print(f"  TOC页: Slide {result['toc_slide']}")
    print(f"  总Slide数: {result['total_slides']}")
    print(f"  章节结构:")

    for section in result['sections']:
        slides = section['slides']
        print(f"    - {section['name']}: Slide {slides[0]}-{slides[-1]} ({len(slides)}张)")

        for sub in section.get('sub_sections', []):
            sub_slides = sub['slides']
            print(f"        • {sub['name']}: Slide {sub_slides[0]}-{sub_slides[-1]}")
