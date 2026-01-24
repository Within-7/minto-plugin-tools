# Plugin Creator 快速开始

## ✅ 安装状态

插件已成功安装到：
```
~/.claude/plugins/plugin-creator/
```

## 🚀 立即使用

### 1. 创建你的第一个插件

```bash
/cc-plugin
```

然后按照交互式提示回答问题。

### 2. 带需求描述创建

```bash
/cc-plugin 我想创建一个代码审查插件，能够自动检查代码质量和安全问题
```

## 📋 可用命令

| 命令 | 说明 |
|------|------|
| `/cc-plugin` | 启动插件创建向导 |
| `/cc-plugin [需求描述]` | 直接提供需求创建插件 |

## 🎯 可创建的组件

### Commands（命令）
用户通过 `/command-name` 调用的斜杠命令

**示例**:
- `/review-code` - 代码审查
- `/generate-tests` - 生成测试
- `/optimize-imports` - 优化导入

### Agents（代理）
自主处理复杂多步骤任务的智能代理

**示例**:
- `code-analyzer` - 深度代码分析
- `test-generator` - 自动生成测试
- `refactor-assistant` - 重构助手

### Skills（技能）
提供专业领域知识和工作流程

**示例**:
- `react-best-practices` - React 最佳实践
- `security-guidelines` - 安全指南
- `testing-patterns` - 测试模式

### Hooks（钩子）
基于事件的自动化触发器

**可用事件**:
- `PreToolUse` - 工具执行前
- `PostToolUse` - 工具执行后
- `SessionStart` - 会话开始
- `Stop` - 会话停止

## 💡 使用示例

### 示例 1: 创建代码审查插件

```bash
/cc-plugin
```

回答问题：
1. 插件名称: `code-reviewer`
2. 插件描述: `自动审查代码质量、安全性和最佳实践`
3. 作者: `Your Name`
4. 选择组件: Commands ✓, Agents ✓
5. 命令名称: `review`
6. 命令描述: `审查当前文件或项目的代码质量`
7. 代理名称: `code-analyzer`
8. 代理描述: `深度分析代码并提供改进建议`

生成的插件包含：
- `/review` 命令用于快速审查
- `code-analyzer` 代理用于深度分析
- 完整的 README 和文档

### 示例 2: 创建测试生成器

```bash
/cc-plugin 自动生成单元测试的插件
```

工具会自动：
1. 分析需求
2. 建议组件结构
3. 生成完整的插件代码
4. 创建文档和示例

### 示例 3: 创建最佳实践技能

```bash
/cc-plugin
```

选择：
- 组件: Skills ✓
- 技能名称: `react-performance`
- 技能描述: `React 性能优化最佳实践`

生成的技能包含：
- 详细的性能优化指南
- 实用的代码示例
- 常见问题和解决方案

## 📁 生成的插件结构

```
your-plugin/
├── .plugin.json              # 插件配置清单
├── README.md                 # 完整文档
├── commands/                 # 命令目录
│   └── command-name.md       # 命令文件
├── agents/                   # 代理目录
│   └── agent-name.md         # 代理文件
├── skills/                   # 技能目录
│   └── skill-name/           # 技能目录
│       └── index.md          # 技能主文件
└── hooks/                    # Hook 目录
    └── event-name/           # 事件目录
        └── hook-  # Hook 文件
```

## 🔍 验证插件

创建插件后，验证它是否正确：

```bash
# 1. 进入插件目录
cd ~/.claude/plugins/your-plugin

# 2. 验证 JSON 语法
python3 -m json.tool .plugin.json

# 3. 检查文件结构
ls -la

# 4. 安装插件（如果还未安装）
# 已在 ~/.claude/plugins/ 目录中，无需额外操作

# 5. 重新加载插件
/reload-plugins

# 6. 测试命令
/your-command
```

## ⚙️ 组件文件格式

### 命令文件 (commands/command-name.md)

```markdown
---
description: 命令的简短描述
args:
  - name: file_path
    description: 要处理的文件路径
    required: false
---

# 命令详细说明

当用户运行此命令时，你应该：

1. 第一步操作
2. 第二步操作
3. 返回结果

## 示例

用户输入: `/command-name src/app.js`
你应该: 分析文件并提供反馈
```

### 代理文件 (agents/agent-name.md)

```markdown
---
description: 何时触发此代理的描述
color: blue
tools:
  - Read
  - Write
  - Bash
  -n---

# 代理系统提示

你是一个专门用于 [具体任务] 的代理。

## 你的职责

1. 职责一
2. 职责二
3. 职责三

## 工作流程

1. 分析需求
2. 执行操作
3. 验证结果
4. 提供反馈
```

### 技能文件 (skills/skill-name/index.md)

```markdown
---
description: 技能的简短描述
---

# 技能名称

## 概述

这个技能提供 [领域] 的专业知识和最佳实践。

## 核心原则

1. 原则一
2. 原则二
3. 原则三

## 最佳实践

### 实践一

说明和示例...

### 实践二

说明和示例...

## 示例

实际应用``

## 🎓 最佳实践

### 命名规范
- ✅ 使用 kebab-case: `my-plugin-name`
- ✅ 命令使用动词: `review-code`, `generate-tests`
- ✅ 描述性名称: `code-reviewer` 而非 `cr`
- ❌ 避免特殊字符和空格

### 描述规范
- ✅ 清晰简洁，一句话说明用途
- ✅ 使用主动语态
- ✅ 突出核心功能
- ❌ 避免过于笼统或模糊

### 组件选择
- **Commands**: 用户主动调用的一次性操作
- **Agents**: 需要多步骤、自主决策的复杂任务
- **Skills**: 提供专业知识和指导
- **Hooks**: 自动响应事件的后台操作

## 🐛 常见问题

###: 插件创建后在哪里？

A: 默认在当前工作目录创建，你需要手动移动到 `~/.claude/plugins/`

```bash
mv your-plugin ~/.claude/plugins/
/reload-plugins
```

### Q: 如何修改生成的插件？

A: 直接编辑生成的文件：
- 修改 `.plugin.json` 更改配置
- 编辑组件 `.md` 文件更改行为
- 运行 `/reload-plugins` 重新加载

### Q: 可以同时创建多个组件吗？

A: 可以！在选择组件类型时，选择多个选项。

### Q: 生成的插件可以直接使用吗？

A: 可以，但建议：
1. 审查生成的代码
2. 根据具体需求调整
3. 测试所有功能
4. 完善文档

### Q: 如何分享我的插件？

A:
1. 将插件上传到 GitHub
2. 在 README 中添加安装说明
3. 分享仓库链接
4. 考虑提交到 Claude Code 插件市场

## 📚 进一步学习

### 官方资源
- [Claude Code 插件文档](https://code.claude.com/docs/zh-CN/plugins)
- [插件开发指南](https://code.claude.com/docs/zh-CN/plugins/development)
- [API 参考](https://code.claude.com/docs/zh-CN/plugins/api)

### 示例插件
查看已安装的插件获取灵感：
```bash
ls ~/.claude/plugins/
```

### 社区
- [GitHub 插件示例](https://github.com/search?q=claude-code-plugin)
- [Discord 社区](https://discord.gg/claude)

## 🎯 下一步

1. **创建第一个插件**
   ```bash
   /cc-plugin
   ```

2. **测试和迭代**
   - 创建简单的插件开始
   - 测试所有功能
   - 根据反馈改进

3. **探索高级功能**
   - 组合多个组件
   - 使用 Hooks 自动化
   - 创建技能库

4. **分享你的插件**
   - 上传到 GitHub
   - 编写完整文档
   - 收集用户反馈

---

**开始创建吧！** 🚀

```bash
/cc-plugin
```

有问题？查看 [完整文档](README.md) 或 [安装指南](INSTALL.md)
