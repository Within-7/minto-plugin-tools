#!/bin/bash
# Fix Suggestion Generator
# Generates fix suggestions without modifying files

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

generate_fixes() {
    local skill_file="$1"
    local report_file="${skill_file%.md}_fixes.md"

    echo "Generating fix suggestions for: $skill_file"
    echo "Report will be saved to: $report_file"

    {
        echo "# Fix Suggestions for $(basename $(dirname "$skill_file"))"
        echo ""
        echo "Generated: $(date)"
        echo ""
        echo "---"
        echo ""

        # Check filename
        filename=$(basename "$skill_file")
        if [ "$filename" != "SKILL.md" ]; then
            echo "## CRITICAL: Wrong Filename"
            echo ""
            echo "**Current:** $filename"
            echo "**Required:** SKILL.md"
            echo ""
            echo "**Fix:**"
            echo '```bash'
            echo "mv $filename SKILL.md"
            echo '```'
            echo ""
            echo "---"
            echo ""
        fi

        # Check YAML frontmatter
        if ! grep -q "^---$" "$skill_file"; then
            echo "## CRITICAL: Missing YAML Frontmatter"
            echo ""
            echo "**Issue:** SKILL.md must start with YAML frontmatter delimited by ---"
            echo ""
            echo "**Fix:** Add to top of file:"
            echo '```yaml'
            echo '---'
            echo 'name: Your Skill Name'
            echo 'description: This skill should be used when the user asks to task 1,'
            echo 'task 2, or mentions concept1, concept2.'
            echo 'version: 0.1.0'
            echo '---'
            echo '```'
            echo ""
            echo "---"
            echo ""
        fi

        # Check for required fields
        yaml_content=$(sed -n '/^---$/,/^---$/p' "$skill_file")

        if ! echo "$yaml_content" | grep -q "^name:"; then
            echo "## CRITICAL: Missing 'name' Field"
            echo ""
            echo "**Fix:** Add to frontmatter:"
            echo '```yaml'
            echo 'name: Your Skill Name'
            echo '```'
            echo ""
            echo "---"
            echo ""
        fi

        if ! echo "$yaml_content" | grep -q "^description:"; then
            echo "## CRITICAL: Missing 'description' Field"
            echo ""
            echo "**Fix:** Add to frontmatter:"
            echo '```yaml'
            echo 'description: This skill should be used when the user asks to task 1,'
            echo 'task 2, or mentions concept1, concept2.'
            echo '```'
            echo ""
            echo "---"
            echo ""
        else
            # Check description quality
            desc=$(echo "$yaml_content" | grep "^description:" | sed 's/description: *//')

            if ! echo "$desc" | grep -qi "This skill should be used when"; then
                echo "## MAJOR: Description Not in Third Person"
                echo ""
                echo "**Current:** $desc"
                echo ""
                echo "**Issue:** Should start with 'This skill should be used when...'"
                echo ""
                echo "**Fix:**"
                echo '```yaml'
                echo 'description: This skill should be used when the user asks to task 1,'
                echo 'task 2, or mentions concept1, concept2.'
                echo '```'
                echo ""
                echo "---"
                echo ""
            fi

            if ! echo "$desc" | grep -q '"'; then
                echo "## MAJOR: Description Lacks Specific Trigger Phrases"
                echo ""
                echo "**Current:** $desc"
                echo ""
                echo "**Issue:** Needs specific phrases in quotes"
                echo ""
                echo "**Fix:** Add 3-7 specific trigger phrases:"
                echo '```yaml'
                echo 'description: This skill should be used when the user asks to create a hook,'
                echo 'add a PreToolUse hook, validate tool use, or mentions hook events.'
                echo '```'
                echo ""
                echo "---"
                echo ""
            fi
        fi

        # Check for second person
        if grep -qi "you should\|you need to\|you can" "$skill_file"; then
            echo "## MAJOR: Uses Second Person Instead of Imperative Form"
            echo ""
            echo "**Issue:** Found instances of second person (you should, you need to)"
            echo ""
            echo "**Locations:**"
            grep -ni "you should\|you need to" "$skill_file" | head -5 | while IFS= read -r line; do
                echo "  - Line $(echo "$line" | cut -d: -f1): $(echo "$line" | cut -d: -f3-)"
            done
            echo ""
            echo "**Fix:** Convert to imperative form"
            echo ""
            echo "**Examples:**"
            echo "X: You should create the directory"
            echo "V: Create the directory"
            echo ""
            echo "X: You need to validate the syntax"
            echo "V: Validate the syntax"
            echo ""
            echo "---"
            echo ""
        fi

        # Check word count
        word_count=$(wc -w < "$skill_file" | awk '{print $1}')
        if [ "$word_count" -gt 3000 ]; then
            echo "## MAJOR: SKILL.md Too Long"
            echo ""
            echo "**Current:** $word_count words"
            echo "**Target:** Keep SKILL.md under 2,000 words"
            echo ""
            echo "**Fix:** Move detailed content to references/:"
            echo ""
            echo "1. Identify sections >500 words"
            echo "2. Move to references/detailed-topic.md"
            echo "3. Add cross-reference in SKILL.md"
            echo ""
            echo "---"
            echo ""
        elif [ "$word_count" -lt 1000 ]; then
            echo "## MAJOR: SKILL.md Too Short"
            echo ""
            echo "**Current:** $word_count words"
            echo "**Target:** 1,500-2,000 words"
            echo ""
            echo "**Fix:** Add essential content"
            echo "- Core concepts (400-600 words)"
            echo "- Essential procedures (600-800 words)"
            echo "- Quick reference (150-300 words)"
            echo ""
            echo "---"
            echo ""
        fi

        echo "## Summary"
        echo ""
        echo "Review these suggestions and apply fixes manually to improve skill quality."
        echo ""
        echo "Next steps:"
        echo "  1. Review the suggestions in the report"
        echo "  2. Apply fixes manually"
        echo "  3. Run validation again"

    } > "$report_file"

    echo ""
    echo "Fix suggestions generated: $report_file"
}

main() {
    if [ $# -eq 0 ]; then
        echo "Usage: $0 <skill-file>"
        exit 1
    fi

    generate_fixes "$1"
}

main "$@"
