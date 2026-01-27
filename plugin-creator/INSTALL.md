# Plugin Creator 安装指南

## 📦 快速安装

### 方法一：自动安装（推荐）

在当前项目目录运行：

```bash
cp -r . ~/.claude/plugins/plugin-creator
```

### 方法二：创建符号链接

如果你想在开发时保持同步：

```bash
ln -s "$(pwd)" ~/.claude/plugins/plugin-creator
```

### 方法三：从 Git 仓库安装

```bash
cd ~/.claude/plugins
git clone https://github.com/Within-7/minto-plugin-tools.git
mv minto-plugin-tools/plugin-creator .
rm -rf minto-plugin-tools
```

## ✅ 验证安装

安装完成后，验证插件是否正确加载：

```bash
# 重启 Claude Code 或重新加载插件
/reload-plugins

# 查看帮助信息
/help

# 测试命令
/cc-plugin
```

你应该能看到：
- `/cc-plugin` 命令在自动完成列表中
- `plugin-builder` 代理可用
- `plugin-creator` 技能可用

## 📁 安装位置

插件将被安装到：
```
~/.claude/plugins/plugin-creator/
├── .plugin.json              # 插件配置
├── README.md                 # 使用文档
├── INSTALL.md               # 本安装指南
├── commands/                # 命令
│   └── cc-plugin.md
├── agents/                  # 代理
│   └── plugin-builder.md
└── skills/                  # 技能
    └── plugin-creator/
```

## 🔧 配置检查

### 检查 .plugin.json

确保配置文件格式正确：

```bash
cat ~/.claude/plugins/plugin-creator/.plugin.json
```

应该输出：
```json
{
  "name": "plugin-creator",
  "version": "1.0.0",
  "description": "A comprehensive tool for creating Claude Code plugins following best practices. Includes templates, validation scripts, and detailed documentation.",
  "author": "Plugin Creator",
  "homepage": "https://github.com/Within-7/minto-plugin-tools",
  "repository": "https://github.com/Within-7/mugin-tools",
  "commands": ["cc-plugin"],
  "agents": ["plugin-builder"],
  "skills": ["plugin-creator"]
}
```

### 验证 JSON 语法

```bash
python3 -m json.tool ~/.claude/plugins/plugin-creator/.plugin.json
```

如果没有错误输出，说明 JSON 格式正确。

## 🚀 使用示例

### 创建你的第一个插件

```bash
/cc-plugin 我想创建一个代码审查插件
```

### 查看可用组件

插件支持以下组件类型：
- **Commands**: 用户调用的斜杠命令（如 `/review-codAgents**: 自主处理复杂任务的代理
- **Skills**: 专业知识和工作流程
- **Hooks**: 事件驱动的自动化

## 🐛 故障排除

### 问题 1: 插件未加载

**症状**: 运行 `/cc-plugin` 提示命令未找到

**解决方案**:
1. 确认插件目录存在：
   ```bash
   ls -la ~/.claude/plugins/plugin-creator/
   ```

2. 检查 .plugin.json 格式：
   ```bash
   python3 -m json.tool ~/.claude/plugins/plugin-creator/.plugin.json
   ```

3. 重启 Claude Code 或运行：
   ```bash
   /reload-plugins
   ```

### 问题 2: 权限错误

**症状**: 复制文件时提示权限不足

**解决方案**:
```bash
chmod -R 755 ~/.claude/plugins/plugin-creator/
```

### 问题 3: 命令不在自动完成中

**症状**: 插件已加载但命令不显示

**解决方案**:
1. 确认命令文件存在：
   ```bash
   ls -la ~/.claude/plugins/plugin-creator/commands/
   ```

2. 检查文件名是否与 .plugin.json 中声明的一致

3. 验证命令文件有正确的 YAML frontmatter

### 问题 4: 代理或技能未加载

**症状**: 代理或技能无法使用

**解决方案**:
1. 检查文件结构：
   ```bash
   tree ~/.claude/plugins/plugin-creator/
   ```

2. 验证 YAML frontmatter 格式：
   ```bash
   head -20 ~/.claude/plugins/plugin-creator/agents/plugin-builder.md
   ```

## 🔄 更新插件

### 从 Git 更新

如果使用 Git 安装：
```bash
cd ~/.claude/plugins/plugin-creator
git pull origin main
/reload-plugins
```

更新

```bash
cd /path/to/your/plugin-creator
cp -r . ~/.claude/plugins/plugin-creator/
/reload-plugins
```

### 使用符号链接（开发模式）

如果使用符号链接，更改会自动同步：
```bash
# 只需重新加载插件
/reload-plugins
```

## 📊 验证安装成功

运行以下命令确认所有组件正常工作：

```bash
# 1. 查看插件列表
/help

# 2. 测试命令
/cc-plugin

# 3. 验证代理（在创建插件时会自动触发）
# 4. 验证技能（在创建插件时会自动使用）
```

## 🎯 下一步

安装成功后，你可以：

1. **阅读使用文档**
   ```bash
   cat ~/.claude/plugins/plugin-creator/README.md
   ```

2. **创建第一个插件**
   ```bash
   /cc-plugin
   ```

3. **查看示例**
   - 查看 commands/cc-plugin.md 了解命令结构
   - 查看 agents/plugin-builder.md 了解代理设计
   - 查看 skills/plugin-creator/ 了解技能组织

4. **探索最佳实践**
   - 参考官方文档：https://code.claude.com/docs/zh-CN/plugins
   - 查看社区插件示例

## 💡 提示

- 使用符号调试
- 定期更新插最新功能
- 遇到问题先查看故障排除部分
- 参考 README.md 获取详细使用说明

## 📞 获取帮助

如果遇到问题：
1. 查看本文档的故障排除部分
2. 阅读 README.md 中的详细说明
3. 访问 GitHub 仓库提交 Issue
4. 查看 Claude Code 官方文档

---

**安装完成！开始创建你的第一个插件吧！** 🚀

```bash
/cc-plugin
```
