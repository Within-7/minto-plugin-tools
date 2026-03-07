#!/usr/bin/env python3
"""
数据回写模块
将提取的数据写入到目标目录

支持的输出格式：
1. JSON格式 - 用于 catalog, analysis, social 模式
2. Markdown格式 - 用于 detail 模式

输出文件路径约定：
- catalog: assets/brands/brand_{brand}_catalog.json
- detail: data/brand_{brand}_detail.md
- analysis: data/brand_{brand}_analysis.json
- social: data/brand_{brand}_social.json
"""

import os
import json
import re
from typing import Dict, List, Optional
from datetime import datetime


class Writer:
    """数据回写器"""

    def __init__(self):
        self.brand_number = "01"  # 默认品牌序号

    def write(self, mode: str, output_dir: str, brand_name: str,
              images: list, toc_structure: dict, unpacked_dir: str) -> dict:
        """
        主写入方法

        Args:
            mode: 提取模式（catalog/detail/analysis/social）
            output_dir: 输出目录
            brand_name: 品牌名称
            images: 已识别并复制的图片列表
            toc_structure: 目录结构
            unpacked_dir: PPT解包目录（用于提取文本数据）

        Returns:
            dict: 写入结果，包含文件路径等信息
        """
        self.output_dir = output_dir
        self.brand_name = brand_name or "unknown"
        self.images = images
        self.toc_structure = toc_structure
        self.unpacked_dir = unpacked_dir

        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)

        # 根据模式选择写入方法
        if mode == 'catalog':
            return self._write_catalog()
        elif mode == 'detail':
            return self._write_detail()
        elif mode == 'analysis':
            return self._write_analysis()
        elif mode == 'social':
            return self._write_social()
        else:
            raise ValueError(f"未知的模式: {mode}")

    def _write_catalog(self) -> dict:
        """写入品牌目录数据（JSON格式）"""
        data = {
            "name": self.brand_name.upper(),
            "nameCN": f"{self.brand_name} 品牌",  # 默认格式，需要后续补充
            "description": "品牌描述"  # 默认格式，需要后续补充
        }

        # 写入文件
        output_file = os.path.join(self.output_dir, f"assets/brands/brand_{self.brand_name.lower()}_catalog.json")
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return {'data_file': output_file, 'format': 'json'}

    def _write_detail(self) -> dict:
        """写入品牌详情数据（Markdown格式）"""
        # 构建Markdown内容
        content = self._build_detail_markdown()

        # 写入文件
        output_file = os.path.join(self.output_dir, f"data/brand_{self.brand_name.lower()}_detail.md")
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)

        return {'data_file': output_file, 'format': 'markdown'}

    def _build_detail_markdown(self) -> str:
        """构建品牌详情Markdown内容"""
        # 图片路径映射
        image_paths = {}
        for img in self.images:
            img_type = img.get('type')
            output_dir = img.get('output_dir', '')
            output_filename = img.get('output_filename', '')
            image_paths[img_type] = f"{output_dir}{output_filename}"

        # 构建Markdown
        md = f"""# 品牌详情：{self.brand_name.upper()}
品牌序号：{self.brand_number}

## 品牌背景与定位
- 基本信息：[待提取]
- 用户画像：[待提取]
- 品牌使命：[待提取]
- 竞争优势：[待提取]

## 爆款产品
- 产品名称：[待提取]
- 产品价格：[待提取]
- 产品特点（7条）：
  1. [待提取]
  2. [待提取]
  3. [待提取]
  4. [待提取]
  5. [待提取]
  6. [待提取]
  7. [待提取]

## 流量来源分布
| 来源 | 占比 |
|-----|-----|
| Direct | [待提取] |
| Search | [待提取] |
| Social | [待提取] |
| Referrals | [待提取] |
| Mail | [待提取] |

## 核心运营指标
| 指标 | 数值 |
|-----|-----|
| 日均活跃用户 | [待提取] |
| 平均停留时长 | [待提取] |
| 人均访问页面 | [待提取] |
| 用户跳出率 | [待提取] |

## 图片文件
- 产品图：{image_paths.get('product', '[待提取]')}
- 品牌Logo：{image_paths.get('logo', '[待提取]')}
- 流量分布图：{image_paths.get('traffic', '[待提取]')}
"""
        return md

    def _write_analysis(self) -> dict:
        """写入品牌分析数据（JSON格式）"""
        # 图片路径映射
        image_paths = {}
        for img in self.images:
            img_type = img.get('type')
            output_dir = img.get('output_dir', '')
            output_filename = img.get('output_filename', '')
            image_paths[img_type] = f"../{output_dir}{output_filename}"

        data = {
            "brandNumber": self.brand_number,
            "brandName": self.brand_name.upper(),
            "logoPath": "../assets/logo.png",

            "userPositionImagePath": image_paths.get('user_position', '../assets/brand_analysis/unknown_user_position.png'),

            "userNeeds": {
                "coreNeeds": "[待提取]核心诉求",
                "scenarios": "[待提取]使用场景",
                "decisionFactors": "[待提取]决策因素",
                "channels": "[待提取]购买渠道"
            },

            "personaImage1Path": image_paths.get('persona_1', '../assets/brand_analysis/unknown_persona_1.png'),
            "personaImage2Path": image_paths.get('persona_2', '../assets/brand_analysis/unknown_persona_2.png'),

            "flowModelImagePath": image_paths.get('flow_model', '../assets/brand_analysis/unknown_flow_model.png'),

            "seoTraffic": {
                "text": "品牌<strong>基石流量</strong>主要来自SEO自然搜索，关键词集中在[待提取]等方向。",
                "keywords": [
                    {"rank": 1, "keyword": "[待提取]", "type": "[类型]", "traffic": "[流量]"},
                    {"rank": 2, "keyword": "[待提取]", "type": "[类型]", "traffic": "[流量]"},
                    {"rank": 3, "keyword": "[待提取]", "type": "[类型]", "traffic": "[流量]"},
                    {"rank": 4, "keyword": "[待提取]", "type": "[类型]", "traffic": "[流量]"},
                    {"rank": 5, "keyword": "[待提取]", "type": "[类型]", "traffic": "[流量]"}
                ]
            },

            "backlinkTypes": "[待提取]外链合作网站类型说明",
            "backlinkKeywords": "[待提取]外链热门关键词说明",
            "backlinkPieImagePath": image_paths.get('backlink_pie', '../assets/brand_analysis/unknown_backlink_pie.png'),
            "backlinkBarImagePath": image_paths.get('backlink_bar', '../assets/brand_analysis/unknown_backlink_bar.png')
        }

        # 写入文件
        output_file = os.path.join(self.output_dir, f"data/brand_{self.brand_name.lower()}_analysis.json")
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return {'data_file': output_file, 'format': 'json'}

    def _write_social(self) -> dict:
        """写入品牌社媒数据（JSON格式）"""
        # 图片路径映射
        image_paths = {}
        for img in self.images:
            img_type = img.get('type')
            output_dir = img.get('output_dir', '')
            output_filename = img.get('output_filename', '')
            image_paths[img_type] = f"../{output_dir}{output_filename}"

        data = {
            "brandNumber": self.brand_number,
            "brandName": self.brand_name.upper(),
            "logoPath": "../assets/logo.png",

            "kolStats": {
                "summary": "[待提取]KOL合作数据摘要（支持<strong>HTML</strong>加粗）",
                "imagePath": image_paths.get('kol_chart', '../assets/brand_social/unknown_kol_chart.png'),
                "points": [
                    "[待提取]要点一：合作重心集中在某平台",
                    "[待提取]要点二：某方面有增长空间",
                    "[待提取]要点三：整体趋势描述"
                ]
            },

            "socialStyle": {
                "items": [
                    {"title": "[待提取]风格标题1", "imagePath": image_paths.get('style_1', '../assets/brand_social/unknown_style_1.png')},
                    {"title": "[待提取]风格标题2", "imagePath": image_paths.get('style_2', '../assets/brand_social/unknown_style_2.png')},
                    {"title": "[待提取]风格标题3", "imagePath": image_paths.get('style_3', '../assets/brand_social/unknown_style_3.png')}
                ]
            },

            "activity1": {
                "title": "[待提取]活动标题1",
                "description": "[待提取]活动描述1",
                "imagePath": image_paths.get('activity_1', '../assets/brand_social/unknown_activity_1.png')
            },
            "activity2": {
                "title": "[待提取]活动标题2",
                "description": "[待提取]活动描述2",
                "imagePath": image_paths.get('activity_2', '../assets/brand_social/unknown_activity_2.png')
            },
            "activity3": {
                "title": "[待提取]活动标题3",
                "description": "[待提取]活动描述3",
                "imagePath": image_paths.get('activity_3', '../assets/brand_social/unknown_activity_3.png')
            }
        }

        # 写入文件
        output_file = os.path.join(self.output_dir, f"data/brand_{self.brand_name.lower()}_social.json")
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return {'data_file': output_file, 'format': 'json'}

    def update_brand_number(self, number: str):
        """更新品牌序号"""
        self.brand_number = number

    def update_data_from_ppt(self, ppt_texts: dict):
        """
        从PPT文本中更新数据（预留接口）

        Args:
            ppt_texts: PPT各slide的文本内容
        """
        # TODO: 实现从PPT文本中提取数据的逻辑
        # 这个方法在后续细化时实现
        pass


if __name__ == '__main__':
    # 测试代码
    print("Writer模块测试")

    writer = Writer()

    # 模拟测试数据
    test_images = [
        {
            'type': 'user_position',
            'output_dir': 'assets/brand_analysis/',
            'output_filename': 'test_user_position.png'
        },
        {
            'type': 'backlink_pie',
            'output_dir': 'assets/brand_analysis/',
            'output_filename': 'test_backlink_pie.png'
        },
        {
            'type': 'backlink_bar',
            'output_dir': 'assets/brand_analysis/',
            'output_filename': 'test_backlink_bar.png'
        }
    ]

    # 测试analysis模式
    result = writer.write(
        mode='analysis',
        output_dir='./test_output',
        brand_name='test',
        images=test_images,
        toc_structure={},
        unpacked_dir=''
    )

    print(f"写入完成: {result['data_file']}")
