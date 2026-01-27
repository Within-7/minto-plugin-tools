#!/bin/bash
# Skill Validation Script
# Validates SKILL.md files for structure, content, and best practices compliance

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Counters
CRITICAL=0
MAJOR=0
MINOR=0

# Function to print colored output
print_error() {
    echo -e "${RED}❌ ERROR: $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  WARNING: $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Function to validate a single SKILL.md file
validate_skill() {
    local skill_file="$1"
    local issues=()

    echo ""
    echo "======================================="
    echo "Validating: $skill_file"
    echo "======================================="

    # Check if file exists
    if [ ! -f "$skill_file" ]; then
        print_error "File does not exist"
        ((CRITICAL++))
        return 1
    fi

    # Check filename
    filename=$(basename "$skill_file")
    if [ "$filename" != "SKILL.md" ]; then
        print_error "Wrong filename (must be SKILL.md, not $filename)"
        ((CRITICAL++))
        issues+=("CRITICAL: Wrong filename - must be SKILL.md")
    else
        print_success "Filename is correct (SKILL.md)"
    fi

    # Check for YAML frontmatter delimiters
    if ! grep -q "^---$" "$skill_file"; then
        print_error "Missing YAML frontmatter delimiters (---)"
        ((CRITICAL++))
        issues+=("CRITICAL: Missing YAML frontmatter delimiters")
    else
        print_success "YAML frontmatter delimiters present"
    fi

    # Extract YAML frontmatter
    yaml_content=$(sed -n '/^---$/,/^---$/p' "$skill_file")

    # Check for required field: name
    if echo "$yaml_content" | grep -q "^name:"; then
        print_success "Has 'name' field"
    else
        print_error "Missing required 'name' field"
        ((CRITICAL++))
        issues+=("CRITICAL: Missing 'name' field in frontmatter")
    fi

    # Check for required field: description
    if echo "$yaml_content" | grep -q "^description:"; then
        print_success "Has 'description' field"
    else
        print_error "Missing required 'description' field"
        ((CRITICAL++))
        issues+=("CRITICAL: Missing 'description' field in frontmatter")
    fi

    # Check description uses third person
    description=$(echo "$yaml_content" | grep "^description:" | sed 's/description: *//')
    if echo "$description" | grep -qi "This skill should be used when"; then
        print_success "Description uses third person"
    else
        print_warning "Description should use third person (start with 'This skill should be used when...')"
        ((MAJOR++))
        issues+=("MAJOR: Description doesn't use third person")
    fi

    # Check description has specific trigger phrases
    if echo "$description" | grep -q '"'; then
        print_success "Description includes specific trigger phrases (in quotes)"
    else
        print_warning "Description lacks specific trigger phrases (add phrases in quotes like \"create a hook\")"
        ((MAJOR++))
        issues+=("MAJOR: Description lacks specific trigger phrases")
    fi

    # Check for version field (optional but recommended)
    if echo "$yaml_content" | grep -q "^version:"; then
        print_success "Has 'version' field"
    else
        print_info "Missing 'version' field (optional but recommended)"
        ((MINOR++))
        issues+=("MINOR: Missing 'version' field")
    fi

    # Check for second person in body
    if grep -qi "you should\|you need to\|you can\|you might" "$skill_file"; then
        print_warning "Found second person (use imperative form instead)"
        ((MAJOR++))
        issues+=("MAJOR: Uses second person instead of imperative form")
        # Show first occurrence
        echo -e "${YELLOW}   Found at lines:$(grep -ni "you should\|you need to" "$skill_file" | head -1 | cut -d: -f1)${NC}"
    else
        print_success "Uses imperative form (no second person found)"
    fi

    # Check word count
    word_count=$(wc -w < "$skill_file" | awk '{print $1}')
    if [ "$word_count" -lt 1000 ]; then
        print_warning "SKILL.md seems too short ($word_count words, target 1500-2000)"
        ((MAJOR++))
        issues+=("MAJOR: SKILL.md too short ($word_count words, need 1500-2000)")
    elif [ "$word_count" -gt 3000 ]; then
        print_warning "SKILL.md too long ($word_count words, target <2000, move content to references/)"
        ((MAJOR++))
        issues+=("MAJOR: SKILL.md too long ($word_count words, move details to references/)")
    else
        print_success "Appropriate length ($word_count words)"
    fi

    # Check for references to supporting files
    if grep -q "references/" "$skill_file"; then
        print_success "References supporting files"
    else
        print_info "No references to supporting files found"
    fi

    # Print summary
    if [ ${#issues[@]} -eq 0 ]; then
        echo ""
        print_success "✅ No issues found! Skill follows best practices."
    else
        echo ""
        echo "Issues found:"
        for issue in "${issues[@]}"; do
            if [[ $issue == CRITICAL* ]]; then
                echo -e "${RED}  $issue${NC}"
            elif [[ $issue == MAJOR* ]]; then
                echo -e "${YELLOW}  $issue${NC}"
            else
                echo -e "${BLUE}  $issue${NC}"
            fi
        done
    fi

    echo ""
}

# Main script
main() {
    if [ $# -eq 0 ]; then
        echo "Usage: $0 <skill-file-or-directory>"
        echo ""
        echo "Examples:"
        echo "  $0 skills/my-skill/SKILL.md"
        echo "  $0 skills/"
        exit 1
    fi

    target="$1"

    if [ -f "$target" ]; then
        # Single file
        validate_skill "$target"
    elif [ -d "$target" ]; then
        # Directory - find all SKILL.md files
        echo "Scanning directory for SKILL.md files..."
        skill_files=$(find "$target" -name "SKILL.md" -type f)
        skill_count=$(echo "$skill_files" | grep -c .)

        if [ "$skill_count" -eq 0 ]; then
            print_error "No SKILL.md files found in $target"
            exit 1
        fi

        echo "Found $skill_count skill file(s)"
        echo ""

        while IFS= read -r skill_file; do
            validate_skill "$skill_file"
        done <<< "$skill_files"

        # Overall summary
        echo "======================================="
        echo "Overall Summary"
        echo "======================================="
        print_success "Skills validated: $skill_count"
        if [ $CRITICAL -gt 0 ]; then
            echo -e "${RED}Critical issues: $CRITICAL${NC}"
        fi
        if [ $MAJOR -gt 0 ]; then
            echo -e "${YELLOW}Major issues: $MAJOR${NC}"
        fi
        if [ $MINOR -gt 0 ]; then
            echo -e "${BLUE}Minor issues: $MINOR${NC}"
        fi
        if [ $CRITICAL -eq 0 ] && [ $MAJOR -eq 0 ] && [ $MINOR -eq 0 ]; then
            print_success "All skills passed validation!"
        fi
    else
        print_error "Invalid target: $target (not a file or directory)"
        exit 1
    fi
}

main "$@"
