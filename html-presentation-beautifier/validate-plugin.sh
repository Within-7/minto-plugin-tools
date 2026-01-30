#!/bin/bash

# HTML Presentation Beautifier Plugin 验证脚本
# 验证插件是否正确配置并可以被 Claude Code 加载

set -e

PLUGIN_NAME="html-presentation-beautifier"
PLUGIN_SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GLOBAL_PLUGIN_DIR="$HOME/.claude/plugins"
VERBOSE="${1:-}"

echo "🔍 HTML Presentation Beautifier Plugin 验证工具"
echo "================================================"
echo ""

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 计数器
TOTAL_CHECKS=0
PASSED_CHECKS=0
FAILED_CHECKS=0

# 验证函数
check() {
    local check_name="$1"
    local check_command="$2"
    
    TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
    
    if [ -n "$VERBOSE" ]; then
        echo -n "检查: $check_name ... "
    fi
    
    if eval "$check_command" > /dev/null 2>&1; then
        echo -e "${GREEN}✅${NC} $check_name"
        PASSED_CHECKS=$((PASSED_CHECKS + 1))
        return 0
    else
        echo -e "${RED}❌${NC} $check_name"
        FAILED_CHECKS=$((FAILED_CHECKS + 1))
        return 1
    fi
}

# 1. 检查源目录结构
echo -e "${BLUE}📁 检查源目录结构${NC}"
echo "----------------------------------------"
check "插件源目录存在" "[ -d '$PLUGIN_SOURCE' ]"
check ".claude-plugin 目录存在" "[ -d '$PLUGIN_SOURCE/.claude-plugin' ]"
check "commands 目录存在" "[ -d '$PLUGIN_SOURCE/commands' ]"
check "agents 目录存在" "[ -d '$PLUGIN_SOURCE/agents' ]"
check "skills 目录存在" "[ -d '$PLUGIN_SOURCE/skills' ]"
echo ""

# 2. 检查配置文件
echo -e "${BLUE}📝 检查配置文件${NC}"
echo "----------------------------------------"
check "plugin.json 存在" "[ -f '$PLUGIN_SOURCE/plugin.json' ]"
check ".claude-plugin/plugin.json 存在" "[ -f '$PLUGIN_SOURCE/.claude-plugin/plugin.json' ]"
check "README.md 存在" "[ -f '$PLUGIN_SOURCE/README.md' ]"
check "CHANGELOG.md 存在" "[ -f '$PLUGIN_SOURCE/CHANGELOG.md' ]"
echo ""

# 3. 检查命令文件
echo -e "${BLUE}⚡ 检查命令文件${NC}"
echo "----------------------------------------"
check "beauty.md 命令文件存在" "[ -f '$PLUGIN_SOURCE/commands/beauty.md' ]"
echo ""

# 4. 检查代理文件
echo -e "${BLUE}🤖 检查代理文件${NC}"
echo "----------------------------------------"
check "presentation-merger.md 代理存在" "[ -f '$PLUGIN_SOURCE/agents/presentation-merger.md' ]"
check "content-merger.md 代理存在" "[ -f '$PLUGIN_SOURCE/agents/content-merger.md' ]"
check "visualization-optimizer.md 代理存在" "[ -f '$PLUGIN_SOURCE/agents/visualization-optimizer.md' ]"
check "content-reviewer.md 代理存在" "[ -f '$PLUGIN_SOURCE/agents/content-reviewer.md' ]"
check "html-presentation-reviewer.md 代理存在" "[ -f '$PLUGIN_SOURCE/agents/html-presentation-reviewer.md' ]"
echo ""

# 5. 检查技能文件
echo -e "${BLUE}🎯 检查技能文件${NC}"
echo "----------------------------------------"
check "beauty-html/SKILL.md 存在" "[ -f '$PLUGIN_SOURCE/skills/beauty-html/SKILL.md' ]"
check "beauty-html/assets 目录存在" "[ -d '$PLUGIN_SOURCE/skills/beauty-html/assets' ]"
check "beauty-html/templates 目录存在" "[ -d '$PLUGIN_SOURCE/skills/beauty-html/templates' ]"
check "beauty-html/references 目录存在" "[ -d '$PLUGIN_SOURCE/skills/beauty-html/references' ]"
echo ""

# 6. 验证 JSON 格式
echo -e "${BLUE}🔧 验证 JSON 格式${NC}"
echo "----------------------------------------"
check "plugin.json JSON 格式有效" "python3 -m json.tool '$PLUGIN_SOURCE/plugin.json'"
check ".claude-plugin/plugin.json JSON 格式有效" "python3 -m json.tool '$PLUGIN_SOURCE/.claude-plugin/plugin.json'"
echo ""

# 7. 检查全局插件目录
echo -e "${BLUE}🌐 检查全局插件目录${NC}"
echo "----------------------------------------"
check "全局插件目录存在" "[ -d '$GLOBAL_PLUGIN_DIR' ]"
check "插件已发布到全局目录" "[ -d '$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME' ]"
echo ""

# 8. 验证插件内容
if [ -d "$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME" ]; then
    echo -e "${BLUE}✨ 验证已发布的插件${NC}"
    echo "----------------------------------------"
    check "全局 plugin.json 存在" "[ -f '$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME/plugin.json' ]"
    check "全局 .claude-plugin/plugin.json 存在" "[ -f '$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME/.claude-plugin/plugin.json' ]"
    check "全局 beauty.md 命令存在" "[ -f '$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME/commands/beauty.md' ]"
    check "全局 beauty-html 技能存在" "[ -f '$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME/skills/beauty-html/SKILL.md' ]"
    check "全局 plugin.json JSON 格式有效" "python3 -m json.tool '$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME/plugin.json'"
    check "全局 .claude-plugin/plugin.json JSON 格式有效" "python3 -m json.tool '$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME/.claude-plugin/plugin.json'"
    echo ""
fi

# 9. 检查插件元数据
echo -e "${BLUE}📊 检查插件元数据${NC}"
echo "----------------------------------------"
if [ -f "$PLUGIN_SOURCE/.claude-plugin/plugin.json" ]; then
    PLUGIN_VERSION=$(python3 -c "import json; print(json.load(open('$PLUGIN_SOURCE/.claude-plugin/plugin.json')).get('version', 'N/A'))" 2>/dev/null || echo "N/A")
    PLUGIN_DESC=$(python3 -c "import json; print(json.load(open('$PLUGIN_SOURCE/.claude-plugin/plugin.json')).get('description', 'N/A'))" 2>/dev/null || echo "N/A")
    
    echo -e "${GREEN}✅${NC} 版本: $PLUGIN_VERSION"
    echo -e "${GREEN}✅${NC} 描述: ${PLUGIN_DESC:0:80}..."
    TOTAL_CHECKS=$((TOTAL_CHECKS + 2))
    PASSED_CHECKS=$((PASSED_CHECKS + 2))
else
    echo -e "${RED}❌${NC} 无法读取插件元数据"
    TOTAL_CHECKS=$((TOTAL_CHECKS + 2))
    FAILED_CHECKS=$((FAILED_CHECKS + 2))
fi
echo ""

# 10. 检查脚本权限
echo -e "${BLUE}🔐 检查脚本权限${NC}"
echo "----------------------------------------"
check "publish.sh 可执行" "[ -x '$PLUGIN_SOURCE/publish.sh' ]"
check "validate-plugin.sh 可执行" "[ -x '$PLUGIN_SOURCE/validate-plugin.sh' ]"
check "install.sh 可执行" "[ -x '$PLUGIN_SOURCE/install.sh' ]"
echo ""

# 显示总结
echo "========================================"
echo "📊 验证总结"
echo "========================================"
echo -e "总检查数: $TOTAL_CHECKS"
echo -e "${GREEN}通过: $PASSED_CHECKS${NC}"
if [ $FAILED_CHECKS -gt 0 ]; then
    echo -e "${RED}失败: $FAILED_CHECKS${NC}"
else
    echo -e "${GREEN}失败: $FAILED_CHECKS${NC}"
fi
echo ""

# 显示状态
if [ $FAILED_CHECKS -eq 0 ]; then
    echo -e "${GREEN}🎉 所有检查通过！插件配置正确。${NC}"
    echo ""
    
    if [ -d "$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME" ]; then
        echo -e "${BLUE}✅ 插件已发布到全局目录${NC}"
        echo ""
        echo "📋 下一步:"
        echo "   1. 重启 Claude Code 或运行: /reload-plugins"
        echo "   2. 验证插件: /help"
        echo "   3. 测试命令: /beauty --help"
    else
        echo -e "${YELLOW}⚠️  插件尚未发布到全局目录${NC}"
        echo ""
        echo "📋 要发布插件，请运行:"
        echo "   ./publish.sh copy    # 复制模式"
        echo "   ./publish.sh link    # 链接模式（开发时推荐）"
    fi
    
    exit 0
else
    echo -e "${RED}❌ 验证失败！请修复上述问题。${NC}"
    echo ""
    echo "💡 提示: 使用 '$0 verbose' 查看详细检查信息"
    exit 1
fi
