#!/bin/bash

# HTML Presentation Beautifier Plugin 发布脚本
# 将插件发布到全局 Claude Code 配置中

set -e

PLUGIN_NAME="html-presentation-beautifier"
PLUGIN_SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GLOBAL_PLUGIN_DIR="$HOME/.claude/plugins"
PUBLISH_MODE="${1:-copy}"

echo "🚀 HTML Presentation Beautifier Plugin 发布工具"
echo "================================================"
echo ""

# 检查插件源目录是否存在
if [ ! -d "$PLUGIN_SOURCE" ]; then
    echo "❌ 错误: 插件源目录不存在: $PLUGIN_SOURCE"
    exit 1
fi

# 检查必要的配置文件
if [ ! -f "$PLUGIN_SOURCE/.claude-plugin/plugin.json" ]; then
    echo "❌ 错误: 找不到插件配置文件 .claude-plugin/plugin.json"
    exit 1
fi

if [ ! -f "$PLUGIN_SOURCE/plugin.json" ]; then
    echo "❌ 错误: 找不到根目录配置文件 plugin.json"
    exit 1
fi

# 显示插件信息
echo "📦 插件信息:"
echo "   名称: $PLUGIN_NAME"
echo "   源目录: $PLUGIN_SOURCE"
echo "   目标目录: $GLOBAL_PLUGIN_DIR/$PLUGIN_NAME"
echo ""

# 解析发布模式
case "$PUBLISH_MODE" in
    copy|--copy|-c)
        PUBLISH_MODE="copy"
        echo "📋 发布模式: 复制 (copy)"
        ;;
    link|--link|-l)
        PUBLISH_MODE="link"
        echo "🔗 发布模式: 符号链接 (link)"
        ;;
    *)
        echo "❌ 错误: 不支持的发布模式 '$PUBLISH_MODE'"
        echo ""
        echo "用法: $0 [copy|link]"
        echo "  copy  - 复制插件到全局目录（默认）"
        echo "  link  - 创建符号链接到全局目录（开发时推荐）"
        exit 1
        ;;
esac

echo ""
echo "⏳ 开始发布..."

# 创建全局插件目录
mkdir -p "$GLOBAL_PLUGIN_DIR"

# 根据模式执行发布
if [ "$PUBLISH_MODE" = "copy" ]; then
    # 复制模式
    if [ -d "$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME" ]; then
        echo "⚠️  插件已存在于全局目录，正在备份旧版本..."
        BACKUP_DIR="$GLOBAL_PLUGIN_DIR/${PLUGIN_NAME}_backup_$(date +%Y%m%d_%H%M%S)"
        
        # 尝试移动旧版本
        if mv "$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME" "$BACKUP_DIR" 2>/dev/null; then
            echo "✅ 旧版本已备份到: $BACKUP_DIR"
        else
            echo "❌ 错误: 无法移动旧版本，权限不足"
            echo "💡 提示: 请手动删除旧版本或使用 sudo 权限"
            echo "   rm -rf $GLOBAL_PLUGIN_DIR/$PLUGIN_NAME"
            exit 1
        fi
    fi

    echo "📦 正在复制插件文件..."
    cp -R "$PLUGIN_SOURCE" "$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME"
    
    # 删除不需要的文件和目录
    cd "$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME"
    rm -rf archive presentation_demo
    echo "✅ 已清理开发文件"

elif [ "$PUBLISH_MODE" = "link" ]; then
    # 链接模式
    if [ -e "$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME" ]; then
        echo "⚠️  插件链接已存在，正在删除旧链接..."
        
        # 尝试删除旧链接
        if rm -rf "$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME" 2>/dev/null; then
            echo "✅ 旧链接已删除"
        else
            echo "❌ 错误: 无法删除旧链接，权限不足"
            echo "💡 提示: 请手动删除旧链接或使用 sudo 权限"
            echo "   rm -rf $GLOBAL_PLUGIN_DIR/$PLUGIN_NAME"
            exit 1
        fi
    fi

    echo "🔗 正在创建符号链接..."
    if ln -s "$PLUGIN_SOURCE" "$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME" 2>/dev/null; then
        echo "✅ 符号链接创建成功"
    else
        echo "❌ 错误: 无法创建符号链接，权限不足"
        echo "💡 提示: 请使用 sudo 权限或检查目录权限"
        exit 1
    fi
fi

# 验证发布结果
echo ""
echo "🔍 验证发布结果..."

if [ ! -d "$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME" ]; then
    echo "❌ 错误: 发布失败，目标目录不存在"
    exit 1
fi

# 检查关键文件
REQUIRED_FILES=(
    ".claude-plugin/plugin.json"
    "plugin.json"
    "commands/beauty.md"
    "skills/beauty-html/SKILL.md"
)

ALL_FILES_OK=true
for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME/$file" ]; then
        echo "❌ 缺少关键文件: $file"
        ALL_FILES_OK=false
    fi
done

if [ "$ALL_FILES_OK" = false ]; then
    echo "❌ 发布验证失败"
    exit 1
fi

# 验证 JSON 格式
echo "📝 验证 JSON 格式..."
if ! python3 -m json.tool "$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME/.claude-plugin/plugin.json" > /dev/null 2>&1; then
    echo "❌ 错误: .claude-plugin/plugin.json 格式无效"
    exit 1
fi

if ! python3 -m json.tool "$GLOBAL_PLUGIN_DIR/$PLUGIN_NAME/plugin.json" > /dev/null 2>&1; then
    echo "❌ 错误: plugin.json 格式无效"
    exit 1
fi

echo "✅ JSON 格式验证通过"

# 显示发布成功信息
echo ""
echo "✅ 发布成功！"
echo ""
echo "📁 插件已安装到: $GLOBAL_PLUGIN_DIR/$PLUGIN_NAME"
echo ""
echo "📋 下一步操作:"
echo "   1. 重启 Claude Code 或运行: /reload-plugins"
echo "   2. 验证插件: /help"
echo "   3. 测试命令: /beauty --help"
echo ""
echo "🔧 插件组件:"
echo "   命令: /beauty"
echo "   代理: presentation-merger, content-merger, visualization-optimizer, content-reviewer, html-presentation-reviewer"
echo "   技能: beauty-html"
echo ""

# 提供卸载提示
echo "💡 如需卸载插件，请运行:"
echo "   rm -rf $GLOBAL_PLUGIN_DIR/$PLUGIN_NAME"
echo "   /reload-plugins"
echo ""
