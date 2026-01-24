# Plugin Creator

一个专业的 Claude Code 插件创建工具，帮助你快速构建符合最佳实践的高质量插件。

## ✨ 特性

- 🚀 **快速创建**: 通过交互式问答快速生成完整的插件结构
- 📋 **规范遵循**: 严格遵循官方 Claude Code 插件开发规范
- 🎯 **组件化设计**: 支持 Commands、Agents、Skills、Hooks 等所有组件类型
- ✅ **自动验证**: 自动验证 JSON/YAML 语法和文件结构
- 📚 **完整文档**: 自动生成 README 和组件文档
- 🎨 **最佳实践**: 内置插件开发最佳实践指南

## 📦 安装

1. 克隆或下载此插件到 Claude Code 插件目录：

```bash
cd ~/.claude/plugins
git clone <repository-url> plugin-creator
```

2. 重启 Claude Code 或运行：

```bash
/reload-plugins
```

3. 验证安装：

```bash
/help
```

你应该能看到 `/cc-plugin` 命令。

## 🚀 使用方法

### 基本用法

直接运行命令，然后根据提示回答问题：

```bash
/cc-plugin
```

### 带需求描述

你也可以直接提供插件需求：

```bash
/cc-plugin 我想创建一个代码审查插件，能够自动检查代码质量和安全问题
```

### 交互式创建流程

工具会引导你完成以下步骤：

1. **插件基本信息**
   - 插件名称（kebab-case 格式）
   - 插件描述
   - 作者信息

2. **组件选择**
   - ✅ Commands - 用户调用的斜杠命令
   - ✅ Agents - 自主处理复杂任务的代理
   - ✅ Skills - 专业知识和工作流
   - ✅ Hooks - 事件驱动的自动化

3. **组件详情**
   - 根据选择的组件类型，提供具体配置
   - 命令名称和参数
   - 代理功能和工具需求
   - 技能领域和知识范围
   - Hook 事件类型和行为

4. **自动生成**
   - 完整的目录结构
   - 规范的 .plugin.json 配置
   - 所有组件文件（带 YAML frontmatter）
   - 完整的 README 文档

## 📁 生成的插件结构

```
your-plugin/
├── .plugin.json              # 插件清单配置
├── README.md                 # 插件文档
├── commands/                 # 命令文件
│   ├── command1.md
│   └── command2.md
├── agents/                   # 代理文件
│   ├── agent1.md
│   └── agent2.md
├── skills/                   # 技能文件
│   ├── skill1.md
│   └── skill2.md
└── hooks/                    # Hook 文件
    ├── pre-tool-use/
    ├── post-tool-use/
    ├── stop/
    └── ...
```

## 🎯 组件说明

### Commands（命令）

用户通过 `/command-name` 调用的斜杠命令。

**适用场景：**
- 代码生成
- 快速分析
- 工作流自动化
- 一键操作

**示例：**
```bash
/review-code
/generate-tests
/optimize-imports
```

### Agents（代理）

自主处理复杂多步骤任务的智能代理。

**适用场景：**
- 多文件重构
- 复杂分析任务
- 项目脚手架
- 自动化工作流

**特点：**
- 完整的工具访问权限
- 多阶段任务处理
- 自主决策能力

### Skills（技能）

提供专业领域知识和工作流程。

**适用场景：**
- 框架最佳实践
- 设计模式指南
- 编码规范
- 领域专业知识

**特点：**
- 自包含的知识体系
- 详细的流程指导
- 实用示例

### Hooks（钩子）

基于事件的自动化触发器。

**可用事件：**
- PreToolUse - 工具执行前
- PostToolUse - 工具执行后
- Stop - 会话停止时
- SessionStart - 会话开始时
- UserPromptSubmit - 用户提交提示后
- 等等...

**适用场景：**
- 输入验证
- 安全检查
- 自动日志
- 状态管理

## 📝 示例

### 示例 1: 创建代码审查插件

```bash
/cc-plugin 创建一个代码审查插件
```

工具会询问：
1. 插件名称：`code-reviewer`
2. 选择组件：Commands ✓, Agents ✓
3. 命令详情：`review` - 审查当前代码
4. 代理详情：`code-analyzer` - 深度分析代码质量

生成的插件包含：
- `/review` 命令用于快速审查
- `code-analyzer` 代理用于深度分析
- 完整的文档和示例

### 示例 2: 创建测试生成器

```bash
/cc-plugin 自动生成单元测试
```

工具会生成：
- `/generate-tests` 命令
- `test-generator` 代理
- `testing-best-practices` 技能
- 完整的测试生成工作流

## ⚙️ 配置

### 插件配置文件

生成的 .plugin.json 示例：

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "插件描述",
  "author": "Your Name",
  "commands": ["command1", "command2"],
  "agents": ["agent1"],
  "skills": ["skill1"],
  "hooks": {
    "PreToolUse": ["safety-check"]
  }
}
```

### 组件文件格式

**命令文件** (commands/command-name.md):
```markdown
---
description: 命令简短描述
args:
  - name: arg_name
    description: 参数描述
    required: false
---

# 命令详细说明

Claude 执行此命令的详细指令...
```

**代理文件** (agents/agent-name.md):
```markdown
---
description: 何时触发此代理
color: blue
tools:
  - Read
  - Write
  - Bash
---

# 代理系统提示

你是一个专门用于...的代理
```

## 🔍 验证和测试

工具会自动进行以下验证：

1. ✅ JSON 语法验证
2. ✅ YAML frontmatter 验证
3. ✅ 文件引用完整性检查
4. ✅ 命名规范检查
5. ✅ 必需字段检查

## 🎓 最佳实践

### 命名规范
- 使用 kebab-case: `my-plugin-name`
- 命令使用动词: `review-code`, `generate-tests`
- 描述性名称: `code-reviewer` 而非 `cr`

### 文档
- 每个组件都要有清晰的描述
- 提供实用的示例
- 记录所有配置选项

### 组件设计
- Commands: 用于用户调用的操作
- Agents: 用于自主多步骤任务
- Skills: 用于专业知识领域
- Hooks: 用于事件自动化

## 🐛 故障排除

### 插件未加载
**问题**: 安装后插件未显示

**解决方案**:
1. 验证 JSON 语法: `python3 -m json.tool .plugin.json`
2. 确认插件在 `~/.claude/plugins/` 目录
3. 重启 Claude Code
4. 检查名称冲突

### 命令未找到
**问题**: 命令不在自动完成中显示

**解决方案**:
1. 确认命令在 .plugin.json 中声明
2. 检查文件存在: `commands/command-name.md`
3. 确保文件名完全匹配
4. 运行 `/reload-plugins`

### YAML 错误
**问题**: 组件因 YAML 错误加载失败

**解决方案**:
1. 验证 YAML 语法
2. 确保 `---` 分隔符存在
3. 检查缩进（使用空格，不用制表符）
4. 验证必需字段存在

## 📚 参考资源

- [官方文档](https://code.claude.com/docs/zh-CN/plugins)
- [示例插件](~/.claude/plugins/)
- [GitHub 社区插件](https://github.com/search?q=claude-code-plugin)

## 🤝 贡献

欢迎提交问题和改进建议！

## 📄 许可证

MIT License

## 🙏 致谢

基于 Claude Code 官方插件开发规范创建。

---

**开始创建你的第一个插件：**

```bash
/cc-plugin
```

祝你开发愉快！ 🚀
