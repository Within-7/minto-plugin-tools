"""
AI-powered analyzer for extracting information from natural language descriptions.

This is a simplified implementation that uses pattern matching and keyword detection
instead of requiring external AI services.
"""

import re
from typing import Dict, Any, List
from datetime import datetime, timedelta


class AIAnalyzer:
    """Analyze natural language work descriptions"""

    def __init__(self):
        """Initialize analyzer with keyword mappings"""
        self.urgency_keywords = {
            'very urgent': 5, 'extremely urgent': 5, '非常紧急': 5, '特别紧急': 5,
            'urgent': 4, 'asap': 4, '紧急': 4, '急': 4,
            'soon': 3, 'moderate': 3, '尽快': 3,
            'low priority': 2, 'not urgent': 2, '不急': 2,
            'whenever': 1, '随时': 1,
        }

        self.importance_keywords = {
            'very important': 5, 'critical': 5, 'crucial': 5, '非常重要': 5, '关键': 5,
            'important': 4, 'significant': 4, '重要': 4,
            'moderate': 3, '一般': 3,
            'low importance': 2, 'minor': 2, '次要': 2,
            'trivial': 1, '无关紧要': 1,
        }

        self.type_keywords = {
            'meeting': ['meeting', 'conference', 'call', 'discussion', '会议', '讨论', '电话会议'],
            'call': ['call', 'phone', 'telephone', '电话', '打电话'],
            'email': ['email', 'mail', 'message', '邮件', '发邮件'],
            'review': ['review', 'check', 'audit', 'inspect', '审查', '检查', '评审'],
            'coding': ['code', 'coding', 'develop', 'implement', 'program', '编码', '开发', '实现'],
            'bugfix': ['bug', 'fix', 'debug', 'issue', 'problem', '修bug', '修复', '问题'],
            'feature': ['feature', 'enhancement', 'improvement', '新功能', '功能', '增强'],
            'design': ['design', 'ui', 'ux', 'mockup', 'prototype', '设计', '原型'],
            'writing': ['write', 'document', 'documentation', 'report', '写', '文档', '报告'],
            'research': ['research', 'investigate', 'study', 'analyze', '研究', '调查', '分析'],
            'planning': ['plan', 'planning', 'schedule', 'organize', '计划', '规划', '安排'],
        }

    def analyze(self, description: str) -> Dict[str, Any]:
        """
        Analyze natural language description and extract information.

        Args:
            description: Natural language work description

        Returns:
            Dictionary containing:
            - summary: Brief summary
            - extracted_info: Extracted structured information
            - suggtions: List of suggestions
        """
        desc_lower = description.lower()

        # Extract information
        extracted = {
            '工作类型': self._detect_type(desc_lower),
            '紧急程度': self._detect_urgency(desc_lower),
            '重要程度': self._detect_importance(desc_lower),
        }

        # Generate summary
        summary = self._generate_summary(description, extracted)
        # Generate suggestions
        suggestions = self._generate_suggestions(description, extracted)

        return {
            'summary': summary,
            'extracted_info': extracted,
            'suggestions': suggestions,
        }

    def _detect_type(self, text: str) -> str:
        """Detect work type from text"""
        for work_type, keywords in self.type_keywords.items():
            for keyword in keywords:
                if keyword in text:
                    type_map = {
                        'meeting': '会议',
                        'call': '电话',
                        'email': '邮件',
                        'review': '审查/评审',
                        'coding': '编码',
                        'bugfix': 'Bug修复',
                        'feature': '新功能',
                        'design': '设计',
                        'writing': '写作',
                        'research': '研究',
                        'planning': '规划',
                    }
                    return type_map.get(work_type, '任务')
        return '任务'

    def _detect_urgency(self, text: str) -> str:
        """Detect urgency level from text"""
        max_urgency = 3  # Default: medium
        matched_keyword = None

        for keyword, level in self.urgency_keywords.items():
            if keyword in text:
                if level > max_urgency:
                    max_urgency = level
                    matched_keyword = keyword

        urgency_map = {
            1: '很低',
            2: '低',
            3: '中等',
            4: '高',
            5: '非常高',
        }
        return urgency_map[max_urgency]

    def _detect_importance(self, text: str) -> str:
        """Detect importance level from text"""
        max_importance = 3  # Default: medium
        matched_keyword = None

        for keyword, level in self.importance_keywords.items():
            if keyword in text:
                if level > max_importance:
                    max_importance = level
                    matched_keyword = keyword

        importance_map = {
            1: '很低',
            2: '低',
            3: '中等',
            4: '高',
            5: '非常高',
        }
        return importance_map[max_importance]

    def _generate_summary(self, description: str, extracted: Dict[str, Any]) -> str:
        """Generate brief summary"""
        work_type = extracted['工作类型']
        urgency = extracted['紧急程度']
        importance = extracted['重要程度']

        # Extract main action/subject (first 50 chars)
        main_subject = description[:50].strip()
        if len(description) > 50:
            main_subject += "..."

        summary = f"这是一个{urgency}紧急度、{importance}重要度的{work_type}类型工作: {main_subject}"
        return summary

    def _generate_suggestions(self, description: str, extracted: Dict[str, Any]) -> List[str]:
        """Generate actionable suggestions"""
        suggestions = []

        urgency = extracted['紧急程度']
        importance = extracted['重要程度']
        work_type = extracted['工作类型']

        # Urgency-based suggestions
        if urgency == '非常高':
            suggestions.append("建议立即处理此事项，优先级最高")
        elif urgency == '高':
            suggestions.append("建议在今天内完成")

        # Importance-based suggestions
        if importance == '非常高':
            suggestions.append("这是关键任务，建议分配足够时间和资源")
        elif importance == '高':
            suggestions.append("建议认真对待，确保质量")

        # Type-based suggestions
        type_suggestions = {
            '会议': "建议提前准备会议议程和相关材料",
            '电话': "建议准备好要讨论的要点",
            'Bug修复': "建议先重现问题，然后定位根因",
            '新功能': "建议先进行需求分析和设计评审",
            '设计': "建议收集参考案例和用户反馈",
            '研究': "建议记录研究过程和发现",
            '规划': "建议列出关键里程碑和依赖关系",
        }

        if work_type in type_suggestions:
            suggestions.append(type_suggestions[work_type])

        # Eisenhower matrix suggestion
        if urgency in ['高', '非常高'] and importance in ['高', '非常高']:
            suggestions.append("根据艾森豪威尔矩阵，这是Q1象限任务（紧急且重要），应立即执行")
        elif urgency in ['低', '很低'] and importance in ['高', '非常高']:
            suggestions.append("根据艾森豪威尔矩阵，这是Q2象限任务（不紧急但重要），建议安排时间处理")
        elif urgency in ['高', '非常高'] and importance in ['低', '很低']:
            suggestions.append("根据艾森豪威尔矩阵，这是Q3象限任务（紧急但不重要），考虑委托他人")
        else:
            suggestions.append("根据艾森豪威尔矩阵，这是Q4象限任务（不紧急不重要），考虑是否需要执行")

        return suggestions


if __name__ == "__main__":
    # Test the analyzer
    analyzer = AIAnalyzer()

    test_cases = [
        "紧急会议今天 #work @office",
        "完成项目报告",
        "修复登录bug #urgent",
        "重要的产品设计评审",
        "研究新技术方案",
    ]

    for description in test_cases:
        print(f"\n输入: {description}")
        result = analyzer.analyze(description)
        print(f"总结: {result['summary']}")
        print(f"提取信息: {result['extracted_info']}")
        print(f"建议: {result['suggestions']}")
