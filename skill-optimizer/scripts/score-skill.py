#!/usr/bin/env python3
"""
Skill Quality Scoring Script
Dynamically scores skills based on issues found (0-100 scale)
"""

import sys
import re
import yaml
from pathlib import Path

def score_skill(skill_file):
    """Score a skill file based on quality criteria."""
    path = Path(skill_file)

    if not path.exists():
        return {"error": "File not found", "score": 0}

    content = path.read_text()

    # Initialize scores
    structure_score = 30
    content_score = 40
    trigger_score = 30

    issues = []

    # Extract YAML frontmatter
    yaml_match = re.search(r'^---$(.*?)^---$', content, re.MULTILINE | re.DOTALL)
    if not yaml_match:
        issues.append(("CRITICAL", "Missing YAML frontmatter"))
        return {"score": 0, "issues": issues}

    try:
        frontmatter = yaml.safe_load(yaml_match.group(1))
    except:
        issues.append(("CRITICAL", "Invalid YAML syntax"))
        return {"score": 0, "issues": issues}

    # Structure checks (30 points)
    if 'name' not in frontmatter:
        structure_score -= 10
        issues.append(("CRITICAL", "Missing 'name' field"))

    if 'description' not in frontmatter:
        structure_score -= 10
        issues.append(("CRITICAL", "Missing 'description' field"))
    else:
        # Check third person
        desc = frontmatter.get('description', '')
        if not desc.startswith('This skill should be used when'):
            trigger_score -= 10
            issues.append(("MAJOR", "Description doesn't use third person"))

        # Check for specific triggers
        if '"' not in desc:
            trigger_score -= 10
            issues.append(("MAJOR", "Description lacks specific trigger phrases"))
        else:
            # Count trigger phrases
            triggers = len(re.findall(r'"([^"]+)"', desc))
            if triggers < 3:
                trigger_score -= 5
                issues.append(("MINOR", f"Only {triggers} trigger phrases (need 3-7)"))

    # Check filename
    if path.name != 'SKILL.md':
        structure_score -= 10
        issues.append(("CRITICAL", f"Wrong filename: {path.name} (must be SKILL.md)"))

    if 'version' not in frontmatter:
        structure_score -= 5
        issues.append(("MINOR", "Missing 'version' field"))

    # Content checks (40 points)
    word_count = len(content.split())
    if word_count < 1000:
        content_score -= 15
        issues.append(("MAJOR", f"SKILL.md too short ({word_count} words, target 1500-2000)"))
    elif word_count > 3000:
        content_score -= 15
        issues.append(("MAJOR", f"SKILL.md too long ({word_count} words, move to references/)"))
    elif word_count >= 1500 and word_count <= 2000:
        content_score += 5  # Bonus for ideal length

    # Check for second person
    second_person = re.findall(r'\b(you should|you need to|you can|you might)\b', content, re.IGNORECASE)
    if second_person:
        content_score -= min(15, len(second_person) * 5)
        issues.append(("MAJOR", f"Found {len(second_person)} instances of second person (use imperative form)"))

    # Check for references
    if 'references/' not in content and word_count > 2000:
        content_score -= 10
        issues.append(("MAJOR", "SKILL.md >2000 words but no references/ found"))

    # Calculate total
    total_score = structure_score + content_score + trigger_score
    total_score = max(0, min(100, total_score))

    # Categorize
    if total_score >= 90:
        category = "Excellent"
    elif total_score >= 70:
        category = "Good"
    elif total_score >= 50:
        category = "Fair"
    else:
        category = "Needs Work"

    return {
        "score": total_score,
        "category": category,
        "structure": structure_score,
        "content": content_score,
        "triggers": trigger_score,
        "issues": issues
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 score-skill.py <skill-file>")
        sys.exit(1)

    skill_file = sys.argv[1]
    result = score_skill(skill_file)

    if "error" in result:
        print(f"❌ Error: {result['error']}")
        sys.exit(1)

    print(f"\n📊 Skill Quality Score: {result['score']}/100 ({result['category']})")
    print(f"\nBreakdown:")
    print(f"  Structure: {result['structure']}/30")
    print(f"  Content:   {result['content']}/40")
    print(f"  Triggers:  {result['triggers']}/30")

    if result['issues']:
        print(f"\nIssues found: {len(result['issues'])}")
        for severity, issue in result['issues']:
            emoji = "🔴" if severity == "CRITICAL" else "🟡" if severity == "MAJOR" else "🔵"
            print(f"  {emoji} [{severity}] {issue}")
    else:
        print("\n✅ No issues found!")

if __name__ == "__main__":
    main()
