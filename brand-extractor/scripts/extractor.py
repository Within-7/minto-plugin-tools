#!/usr/bin/env python3
"""
PPT品牌信息提取器 v2.1
核心提取流程：解包 -> 解析TOC -> Phase1(目录前) + Phase2(目录后) -> 识别图片 -> 回写数据

使用方法：
    python extractor.py <ppt_path> <output_dir> <mode> [brand_name]

参数：
    ppt_path: PPT文件路径
    output_dir: 输出目录
    mode: catalog | detail | analysis | social
    brand_name: 品牌名称（可选，默认从PPT提取）

示例：
    python extractor.py /path/to/brand.pptx ./output detail buffy

v2.1 更新：
    - Detail模式采用两阶段提取
    - Phase1: 提取目录页之前的内容（Logo + 品牌概览）
    - Phase2: 提取目录页之后的内容，截止到"用户定位"之前
"""

import os
import sys
import json
import shutil
import zipfile
from pathlib import Path

# 导入内部模块
from toc_parser import TOCParser
from image_identifier import ImageIdentifier
from writer import Writer


class BrandExtractor:
    """品牌信息提取器"""

    def __init__(self, ppt_path: str, output_dir: str, mode: str, brand_name: str = None):
        self.ppt_path = ppt_path
        self.output_dir = output_dir
        self.mode = mode
        self.brand_name = brand_name

        # 工作目录
        self.work_dir = None
        self.unpacked_dir = None

        # 加载规则
        self.rules = self._load_rules()

        # 初始化子模块
        self.toc_parser = TOCParser()
        self.image_identifier = ImageIdentifier()
        self.writer = Writer()

    def _load_rules(self) -> dict:
        """加载当前模式的规则配置"""
        rules_dir = os.path.join(os.path.dirname(__file__), '..', 'rules')
        rules_file = os.path.join(rules_dir, f'{self.mode}.json')

        with open(rules_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def extract(self) -> dict:
        """
        主提取流程

        Returns:
            dict: 提取结果，包含图片列表和数据内容
        """
        print(f"开始提取 - 模式: {self.mode}")
        print(f"PPT文件: {self.ppt_path}")
        print(f"输出目录: {self.output_dir}")

        # Step 1: 解包PPT
        self.unpacked_dir = self._unpack_ppt()
        print(f"✓ PPT解包完成: {self.unpacked_dir}")

        # Step 2: 解析TOC，获取章节结构
        toc_structure = self.toc_parser.parse(self.unpacked_dir)
        print(f"✓ TOC解析完成: 找到 {len(toc_structure.get('sections', []))} 个章节")

        # Step 3: 根据mode和规则，定位目标章节的slide范围
        target_slides = self._locate_target_slides(toc_structure)
        print(f"✓ 目标slides定位完成: {target_slides}")

        # Step 4: 在目标slides中识别图片
        identified_images = self._identify_images(target_slides)
        print(f"✓ 图片识别完成: {len(identified_images)} 张图片")

        # Step 5: 复制图片到目标目录，重命名
        copied_images = self._copy_images(identified_images)
        print(f"✓ 图片复制完成: {len(copied_images)} 张图片")

        # Step 6: 回写数据文件
        result = self.writer.write(
            mode=self.mode,
            output_dir=self.output_dir,
            brand_name=self.brand_name,
            images=copied_images,
            toc_structure=toc_structure,
            unpacked_dir=self.unpacked_dir
        )
        print(f"✓ 数据回写完成: {result.get('data_file', 'N/A')}")

        # 清理工作目录
        self._cleanup()

        return {
            'success': True,
            'mode': self.mode,
            'brand_name': self.brand_name,
            'images': copied_images,
            'data_file': result.get('data_file')
        }

    def _unpack_ppt(self) -> str:
        """
        Step 1: 解包PPT文件

        Returns:
            str: 解包后的目录路径
        """
        # 创建工作目录
        self.work_dir = os.path.join(os.path.dirname(self.ppt_path), 'workspace')
        unpacked_dir = os.path.join(self.work_dir, 'unpacked')

        # 清理旧的解包目录
        if os.path.exists(unpacked_dir):
            shutil.rmtree(unpacked_dir)

        os.makedirs(unpacked_dir, exist_ok=True)

        # 解包PPT（pptx本质是zip文件）
        with zipfile.ZipFile(self.ppt_path, 'r') as zip_ref:
            zip_ref.extractall(unpacked_dir)

        return unpacked_dir

    def _locate_target_slides(self, toc_structure: dict) -> dict:
        """
        Step 3: 根据mode和规则，定位目标章节的slide范围

        Args:
            toc_structure: TOC解析器返回的章节结构

        Returns:
            dict: 目标slides信息，格式如：
            {
                'section_name': {
                    'slides': [5, 6, 7],
                    'images_needed': ['logo', 'product']
                }
            }
        """
        target_slides = {}

        if self.mode == 'catalog':
            # catalog模式：直接定位到Slide 1
            target_slides['cover'] = {
                'slides': [1],
                'images_needed': ['cover']
            }

        elif self.mode == 'detail':
            # detail模式：定位品牌介绍、产品定位、流量分布
            target_slides = self._locate_detail_sections(toc_structure)

        elif self.mode == 'analysis':
            # analysis模式：定位用户定位、用户画像、流量模型、基石流量（含外链）
            target_slides = self._locate_analysis_sections(toc_structure)

        elif self.mode == 'social':
            # social模式：定位营销活动章节
            target_slides = self._locate_social_sections(toc_structure)

        return target_slides

    def _locate_detail_sections(self, toc_structure: dict) -> dict:
        """
        定位detail模式的目标章节（v2.1 两阶段提取 + 横幅精准定位）

        Phase 1: 目录页之前
            - 品牌概览页（Slide 2，通常）→ 提取Logo + 基础信息

        Phase 2: 目录页之后，截止到"用户定位"之前
            - 品牌简介章节 → 独立站流量数据
            - 产品定位章节 → 爆款产品

        v2.1 优化：使用横幅文本精准定位章节边界
        """
        target_slides = {}
        toc_slide = toc_structure.get('toc_slide', 4)
        total_slides = toc_structure.get('total_slides', 100)

        # ==================== 横幅文本精准定位（v2.1核心优化）====================
        # 解析所有slides的横幅文本
        banner_info = self.toc_parser.parse_banners(1, total_slides)
        slide_sections = banner_info.get('slide_sections', {})

        # 找到"用户定位"章节的第一个slide作为边界
        user_position_start = self.toc_parser.find_boundary_slide('用户定位')

        if user_position_start:
            end_slide = user_position_start - 1
            print(f"  横幅定位: '用户定位' 从 Slide {user_position_start} 开始")
        else:
            # 回退到TOC估算方法
            sections = toc_structure.get('sections', [])
            user_section = self._find_section_by_keywords(sections, ['用户定位', '用户分析'])
            end_slide = total_slides
            if user_section and user_section.get('slides'):
                end_slide = min(user_section.get('slides', [])) - 1
            print(f"  TOC估算: 截止到 Slide {end_slide}")

        # ==================== Phase 1: 目录页之前 ====================
        pre_toc_slides = list(range(2, toc_slide))
        if pre_toc_slides:
            target_slides['brand_overview'] = {
                'slides': pre_toc_slides,
                'images_needed': ['logo'],
                'phase': 'pre_toc',
                'description': '品牌概览页（目录页之前）'
            }

        # ==================== Phase 2: 目录页之后（使用横幅精准定位）====================
        # 使用横幅文本获取每个章节的slides
        brand_intro_slides = self.toc_parser.get_section_slides('品牌简介')
        if not brand_intro_slides:
            brand_intro_slides = self.toc_parser.get_section_slides('品牌介绍')

        product_slides = self.toc_parser.get_section_slides('产品定位')
        if not product_slides:
            product_slides = self.toc_parser.get_section_slides('产品')

        # 过滤：只保留截止边界之前的slides
        if brand_intro_slides:
            filtered = [s for s in brand_intro_slides if s <= end_slide]
            if filtered:
                target_slides['brand_intro'] = {
                    'slides': filtered,
                    'images_needed': ['traffic'],
                    'phase': 'post_toc',
                    'description': '品牌简介章节（独立站流量数据）',
                    'detection_method': 'banner'
                }
                print(f"  横幅定位: '品牌简介' → Slides {filtered}")

        if product_slides:
            filtered = [s for s in product_slides if s <= end_slide]
            if filtered:
                target_slides['product'] = {
                    'slides': filtered,
                    'images_needed': ['product'],
                    'phase': 'post_toc',
                    'description': '产品定位章节（爆款产品）',
                    'detection_method': 'banner'
                }
                print(f"  横幅定位: '产品定位' → Slides {filtered}")

        # 如果横幅定位失败，回退到TOC估算
        if not target_slides.get('brand_intro') and not target_slides.get('product'):
            print("  横幅定位失败，回退到TOC估算方法")
            sections = toc_structure.get('sections', [])

            brand_intro = self._find_section_by_keywords(sections, ['品牌简介', '品牌介绍'])
            if brand_intro:
                intro_slides = [s for s in brand_intro.get('slides', []) if s <= end_slide]
                if intro_slides:
                    target_slides['brand_intro'] = {
                        'slides': intro_slides,
                        'images_needed': ['traffic'],
                        'phase': 'post_toc',
                        'description': '品牌简介章节（独立站流量数据）',
                        'detection_method': 'toc_estimate'
                    }

            product = self._find_section_by_keywords(sections, ['产品定位', '爆款产品'])
            if product:
                prod_slides = [s for s in product.get('slides', []) if s <= end_slide]
                if prod_slides:
                    target_slides['product'] = {
                        'slides': prod_slides,
                        'images_needed': ['product'],
                        'phase': 'post_toc',
                        'description': '产品定位章节（爆款产品）',
                        'detection_method': 'toc_estimate'
                    }

        print(f"  Phase1(目录前): Slides {pre_toc_slides}")
        print(f"  Phase2(目录后): 截止到 Slide {end_slide}")

        return target_slides

    def _locate_analysis_sections(self, toc_structure: dict) -> dict:
        """定位analysis模式的目标章节"""
        target_slides = {}
        sections = toc_structure.get('sections', [])

        # 查找用户定位章节
        user_position = self._find_section_by_keywords(sections, ['用户定位', '用户分析'])
        if user_position:
            target_slides['user_position'] = {
                'slides': user_position.get('slides', []),
                'images_needed': ['user_position']
            }

        # 查找用户画像章节
        persona = self._find_section_by_keywords(sections, ['用户画像', '人群画像'])
        if persona:
            target_slides['persona'] = {
                'slides': persona.get('slides', []),
                'images_needed': ['persona_1', 'persona_2']
            }

        # 查找流量模型章节
        flow_model = self._find_section_by_keywords(sections, ['流量模型', '流量路径'])
        if flow_model:
            target_slides['flow_model'] = {
                'slides': flow_model.get('slides', []),
                'images_needed': ['flow_model']
            }

        # 查找基石流量章节（包含外链分析）
        base_traffic = self._find_section_by_keywords(sections, ['基石流量', 'SEO', '外链'])
        if base_traffic:
            target_slides['base_traffic'] = {
                'slides': base_traffic.get('slides', []),
                'images_needed': ['backlink_pie', 'backlink_bar']
            }

        return target_slides

    def _locate_social_sections(self, toc_structure: dict) -> dict:
        """定位social模式的目标章节"""
        target_slides = {}
        sections = toc_structure.get('sections', [])

        # 查找营销活动章节
        marketing = self._find_section_by_keywords(sections, ['营销活动', 'KOL合作', '社媒'])
        if marketing:
            target_slides['marketing'] = {
                'slides': marketing.get('slides', []),
                'images_needed': [
                    'kol_chart',
                    'style_1', 'style_2', 'style_3',
                    'activity_1', 'activity_2', 'activity_3'
                ]
            }

        return target_slides

    def _find_section_by_keywords(self, sections: list, keywords: list) -> dict:
        """
        根据关键词查找章节

        Args:
            sections: 章节列表
            keywords: 关键词列表

        Returns:
            dict: 匹配的章节信息，未找到返回None
        """
        for section in sections:
            section_name = section.get('name', '').lower()
            for keyword in keywords:
                if keyword.lower() in section_name:
                    return section
        return None

    def _identify_images(self, target_slides: dict) -> list:
        """
        Step 4: 在目标slides中识别图片（v2.3 支持文字关键词匹配）

        Args:
            target_slides: 目标slides信息

        Returns:
            list: 识别出的图片列表
        """
        identified_images = []

        for section_name, section_info in target_slides.items():
            slides = section_info.get('slides', [])
            images_needed = section_info.get('images_needed', [])

            for slide_num in slides:
                # 获取该slide的所有图片
                slide_images = self._get_slide_images(slide_num)

                # 【v2.3新增】获取该slide的文字内容
                slide_texts = self.toc_parser._extract_slide_texts(slide_num)

                # 【v2.3新增】获取该slide的横幅文本（章节名）
                banner_text = self.toc_parser._extract_banner_section(slide_num)
                banner_section_name = banner_text.get('section_name', '') if banner_text else ''

                # 使用图片识别器识别
                for image_type in images_needed:
                    identified = self.image_identifier.identify(
                        slide_num=slide_num,
                        images=slide_images,
                        image_type=image_type,
                        section_name=section_name,
                        rules=self.rules,
                        slide_texts=slide_texts,  # v2.3新增
                        banner_text=banner_section_name  # v2.3新增
                    )
                    if identified:
                        identified_images.append(identified)

        return identified_images

    def _get_slide_images(self, slide_num: int) -> list:
        """
        获取指定slide的所有图片

        Args:
            slide_num: slide编号

        Returns:
            list: 图片信息列表
        """
        import xml.etree.ElementTree as ET

        images = []
        rels_path = os.path.join(self.unpacked_dir, f'ppt/slides/_rels/slide{slide_num}.xml.rels')

        if not os.path.exists(rels_path):
            return images

        try:
            tree = ET.parse(rels_path)
            root = tree.getroot()

            for rel in root.iter():
                target = rel.get('Target', '')
                rid = rel.get('Id', '')

                if 'media/image' in target and rid:
                    img_path = os.path.join(self.unpacked_dir, 'ppt/slides', target)
                    img_path = os.path.normpath(img_path)

                    if os.path.exists(img_path):
                        # 获取图片尺寸
                        size = os.path.getsize(img_path)
                        images.append({
                            'rid': rid,
                            'path': img_path,
                            'filename': os.path.basename(target),
                            'size': size
                        })
        except Exception as e:
            print(f"  警告: 解析rels失败 - {e}")

        return images

    def _copy_images(self, identified_images: list) -> list:
        """
        Step 5: 复制图片到目标目录，重命名

        Args:
            identified_images: 识别出的图片列表

        Returns:
            list: 复制后的图片信息列表
        """
        copied_images = []

        for img_info in identified_images:
            source_path = img_info.get('path')
            if not source_path or not os.path.exists(source_path):
                continue

            # 生成目标路径
            output_filename = img_info.get('output_filename', img_info.get('filename'))
            output_subdir = img_info.get('output_dir', 'assets/')

            # 替换品牌名占位符
            if self.brand_name:
                output_filename = output_filename.replace('{brand}', self.brand_name.lower())

            target_dir = os.path.join(self.output_dir, output_subdir)
            target_path = os.path.join(target_dir, output_filename)

            # 创建目录
            os.makedirs(target_dir, exist_ok=True)

            # 复制文件
            shutil.copy2(source_path, target_path)

            copied_images.append({
                **img_info,
                'target_path': target_path,
                'output_filename': output_filename
            })

        return copied_images

    def _cleanup(self):
        """清理工作目录"""
        if self.work_dir and os.path.exists(self.work_dir):
            shutil.rmtree(self.work_dir)


def main():
    """命令行入口"""
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)

    ppt_path = sys.argv[1]
    output_dir = sys.argv[2]
    mode = sys.argv[3]
    brand_name = sys.argv[4] if len(sys.argv) > 4 else None

    # 验证mode
    valid_modes = ['catalog', 'detail', 'analysis', 'social']
    if mode not in valid_modes:
        print(f"错误: 无效的mode '{mode}'，有效值: {valid_modes}")
        sys.exit(1)

    # 执行提取
    extractor = BrandExtractor(ppt_path, output_dir, mode, brand_name)
    result = extractor.extract()

    print("\n" + "=" * 60)
    print("提取完成!")
    print("=" * 60)
    print(f"模式: {result['mode']}")
    print(f"品牌: {result['brand_name']}")
    print(f"图片: {len(result['images'])} 张")
    print(f"数据: {result['data_file']}")


if __name__ == '__main__':
    main()
