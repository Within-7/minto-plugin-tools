#!/usr/bin/env python3
"""
TOC（目录）解析器 v2.1
解析PPT的目录页，建立章节名称到slide范围的映射

核心逻辑：
1. 定位TOC页（通常是Slide 4，特征是包含"报告目录"或"目录"）
2. 提取目录结构（章节名称、层级关系）
3. 【v2.1新增】解析每个slide的横幅文本，精准定位章节

横幅文本结构：
┌─────────────────────────────────────────────────────┐
│  Within-7.com    PARACHUTE    3. 用户定位    任小姐  │
│  [网站标识]     [品牌名]     [章节编号+名称]  [来源]  │
└─────────────────────────────────────────────────────┘
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
        self.banner_sections = {}  # 存储每个slide的横幅章节信息

    # ==================== 横幅文本解析（v2.1新增）====================

    def parse_banners(self, start_slide: int = 1, end_slide: int = None) -> dict:
        """
        解析所有slides的横幅文本，建立精准的章节映射

        Args:
            start_slide: 起始slide编号
            end_slide: 结束slide编号（默认到最后）

        Returns:
            dict: {
                'slide_sections': {slide_num: section_name, ...},
                'section_slides': {section_name: [slide_nums], ...}
            }
        """
        if end_slide is None:
            end_slide = self._get_total_slides()

        slide_sections = {}  # slide -> section
        section_slides = {}  # section -> [slides]

        for slide_num in range(start_slide, end_slide + 1):
            banner_info = self._extract_banner_section(slide_num)
            if banner_info:
                section_name = banner_info.get('section_name')
                if section_name:
                    slide_sections[slide_num] = section_name
                    if section_name not in section_slides:
                        section_slides[section_name] = []
                    section_slides[section_name].append(slide_num)

        self.banner_sections = {
            'slide_sections': slide_sections,
            'section_slides': section_slides
        }

        return self.banner_sections

    def _extract_banner_section(self, slide_num: int) -> Optional[dict]:
        """
        从slide中提取横幅文本，解析章节信息

        横幅文本格式：
        - "1. 品牌简介" / "2. 产品定位" / "3. 用户定位" 等
        - 通常在slide的前几个文本元素中

        Args:
            slide_num: slide编号

        Returns:
            dict: {
                'section_number': 3,
                'section_name': '用户定位',
                'brand_name': 'PARACHUTE',
                'source': '任小姐 出海战略咨询'
            }
        """
        texts = self._extract_slide_texts(slide_num)
        if not texts:
            return None

        # 横幅文本通常在前10个文本中
        banner_texts = texts[:10]

        result = {}

        for i, text in enumerate(banner_texts):
            text = text.strip()

            # 匹配章节编号 "1." "2." "3." 等
            if re.match(r'^\d+\.$', text):
                # 下一个文本通常是章节名称
                if i + 1 < len(banner_texts):
                    next_text = banner_texts[i + 1].strip()
                    # 检查是否是有效的章节名称
                    if self._is_valid_section_name(next_text):
                        result['section_number'] = int(text.rstrip('.'))
                        result['section_name'] = next_text

        # 提取品牌名称（通常是大写英文）
        for text in banner_texts:
            if re.match(r'^[A-Z]{3,}$', text) and text not in ['SEO', 'SEM', 'KOL']:
                result['brand_name'] = text
                break

        return result if result.get('section_name') else None

    def _is_valid_section_name(self, name: str) -> bool:
        """检查是否是有效的章节名称"""
        valid_sections = [
            '品牌简介', '品牌介绍', '品牌概览',
            '产品定位', '爆款产品', '产品介绍',
            '用户定位', '用户分析', '用户画像',
            '流量模型', '流量路径',
            '基石流量', 'SEO', 'SEM',
            '营销活动', 'KOL', '社媒'
        ]

        name_lower = name.lower()
        for valid in valid_sections:
            if valid.lower() in name_lower or name_lower in valid.lower():
                return True
        return False

    def get_slide_section(self, slide_num: int) -> Optional[str]:
        """
        获取指定slide所属的章节名称

        Args:
            slide_num: slide编号

        Returns:
            str: 章节名称，未找到返回None
        """
        if not self.banner_sections:
            self.parse_banners()

        return self.banner_sections.get('slide_sections', {}).get(slide_num)

    def get_section_slides(self, section_name: str) -> List[int]:
        """
        获取指定章节的所有slide编号

        Args:
            section_name: 章节名称（支持模糊匹配）

        Returns:
            list: slide编号列表
        """
        if not self.banner_sections:
            self.parse_banners()

        section_slides = self.banner_sections.get('section_slides', {})

        # 精确匹配
        if section_name in section_slides:
            return section_slides[section_name]

        # 模糊匹配
        for name, slides in section_slides.items():
            if section_name.lower() in name.lower() or name.lower() in section_name.lower():
                return slides

        return []

    def find_boundary_slide(self, section_name: str) -> Optional[int]:
        """
        找到指定章节的第一个slide（作为边界）

        Args:
            section_name: 章节名称

        Returns:
            int: 该章节的第一个slide编号，未找到返回None
        """
        slides = self.get_section_slides(section_name)
        return min(slides) if slides else None

    def _extract_banner_section(self, slide_num: int) -> Optional[dict]:
        """
        提取指定slide的横幅章节信息

        横幅格式：
        ┌─────────────────────────────────────────────────────┐
        │  Within-7.com    PARACHUTE    3. 用户定位    任小姐  │
        │  [网站标识]     [品牌名]     [章节编号+名称]  [来源]  │
        └─────────────────────────────────────────────────────┘

        Args:
            slide_num: slide编号

        Returns:
            dict: {
                'section_number': 3,
                'section_name': '用户定位',
                'brand_name': 'PARACHUTE',
                'source': '任小姐 出海战略咨询'
            }
        """
        texts = self._extract_slide_texts(slide_num)
        if not texts:
            return None

        # 横幅文本通常在前10个文本中
        banner_texts = texts[:10]

        result = {}

        for i, text in enumerate(banner_texts):
            text = text.strip()

            # 匹配章节编号 "1." "2." "3." 等
            if re.match(r'^\d+\.$', text):
                # 下一个文本通常是章节名称
                if i + 1 < len(banner_texts):
                    next_text = banner_texts[i + 1].strip()
                    # 检查是否是有效的章节名称
                    if self._is_valid_section_name(next_text):
                        result['section_number'] = int(text.rstrip('.'))
                        result['section_name'] = next_text

        # 提取品牌名称（通常是大写英文）
        for text in banner_texts:
            if re.match(r'^[A-Z]{3,}$', text) and text not in ['SEO', 'SEM', 'KOL']:
                result['brand_name'] = text
                break

        return result if result.get('section_name') else None

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
