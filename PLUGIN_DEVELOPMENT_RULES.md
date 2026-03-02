# Plugin 开发规范

> 基于 `brand-research` 插件结构制定的标准开发规范

---

## 1. 目录结构规范

```
plugin-name/
├── plugin.json              # 必需 - 插件清单
├── README.md                # 必需 - 插件说明文档
├── .claude-plugin/
│   └── plugin.json          # 可选 - 兼容旧版清单
├── commands/                # 命令目录
│   └── command-name.md      # 命令定义文件
├── skills/                  # 技能目录
│   └── skill-name/
│       ├── SKILL.md         # 必需 - 技能定义
│       └── references/      # 可选 - 参考文档
│           ├── template.md
│           └── guide.md
└── agents/                  # 可选 - 代理目录
    └── agent-name.md
```

### 检查清单

- [ ] 根目录存在 `plugin.json`
- [ ] 根目录存在 `README.md`
- [ ] `commands/` 或 `skills/` 至少存在一个
- [ ] 每个 skill 目录包含 `SKILL.md`

---

## 2. plugin.json 规范

### 必需字段

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "插件功能描述（中文，一句话说明核心功能）",
  "author": "author-name"
}
```

### 完整字段示例

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "插件功能描述 - 详细说明插件的用途和核心能力",
  "author": "within-7",
  "homepage": "https://github.com/within-7/minto-plugins",
  "repository": "https://github.com/within-7/minto-plugins",
  "keywords": ["keyword1", "keyword2", "关键词", "标签"],
  "commands": [
    "./commands/command1.md",
    "./commands/command2.md"
  ],
  "skills": [
    "./skills/skill-name"
  ],
  "agents": [
    "./agents/agent-name.md"
  ]
}
```

### 字段规范

| 字段 | 必需 | 类型 | 说明 |
|------|------|------|------|
| `name` | ✅ | string | 插件名称，kebab-case 格式 |
| `version` | ✅ | string | 语义化版本号 (semver) |
| `description` | ✅ | string | 功能描述，建议包含触发场景 |
| `author` | ✅ | string | 作者或组织名称 |
| `homepage` | ⭕ | string | 项目主页 URL |
| `repository` | ⭕ | string | 代码仓库 URL |
| `keywords` | ⭕ | array | 关键词数组，包含中英文 |
| `commands` | ⭕ | array | 命令文件路径数组 |
| `skills` | ⭕ | array | 技能目录路径数组 |
| `agents` | ⭕ | array | 代理文件路径数组 |

### 版本号规范

遵循语义化版本 (Semantic Versioning)：
- **MAJOR** (主版本): 不兼容的 API 变更
- **MINOR** (次版本): 向后兼容的功能新增
- **PATCH** (补丁版本): 向后兼容的问题修正

```
1.0.0 → 1.0.1  # bug 修复
1.0.0 → 1.1.0  # 新增功能
1.0.0 → 2.0.0  # 破坏性变更
```

---

## 3. README.md 规范

### 必需章节

1. **标题与简介** - 插件名称和一句话描述
2. **功能特性** - 核心功能列表（使用 emoji 增强可读性）
3. **安装方法** - 安装步骤
4. **使用方法** - 命令示例
5. **版本历史** - 变更记录

### 模板

```markdown
# Plugin Name - 插件简介

Claude Code 插件，用于 [核心功能描述]。

## 功能特性

- 🔍 **特性1**：描述
- ✅ **特性2**：描述
- 📊 **特性3**：描述

## 安装

\`\`\`bash
# 安装命令
\`\`\`

## 使用方法

\`\`\`
/command-name <参数>
\`\`\`

示例：
\`\`\`
/command-name 示例参数
\`\`\`

## 配置（可选）

如有配置项，在此说明。

## 版本历史

- v1.0.0 - 初始版本

## 许可证

MIT
```

---

## 4. Commands 规范

### 文件结构

```markdown
---
description: 命令功能描述
args: 参数名称
allowed-tools: [WebSearch, Read, Write, Grep, Glob]
---

# 命令标题

你是一个 [角色定义]。用户请求: **{args}**

## 任务步骤

### Step 1: 步骤标题

执行内容...

### Step 2: 步骤标题

执行内容...

---

## 注意事项

1. 注意点1
2. 注意点2
```

### Frontmatter 规范

| 字段 | 必需 | 说明 |
|------|------|------|
| `description` | ✅ | 命令功能描述，用于帮助文档 |
| `args` | ⭕ | 参数说明，用于提示用户输入 |
| `allowed-tools` | ⭕ | 允许使用的工具列表 |

### 命令文件命名

- 使用 kebab-case：`brand-analyze.md`
- 文件名即为命令名：`/brand-analyze`
- 避免使用空格和特殊字符

### 内容编写规范

1. **角色定义** - 开头明确 AI 扮演的角色
2. **步骤化** - 使用 `Step N:` 结构化任务流程
3. **占位符** - 使用 `{args}` 引用用户输入
4. **工具限定** - 明确允许使用的工具
5. **输出路径** - 明确结果保存位置

---

## 5. Skills 规范

### 目录结构

```
skills/
└── skill-name/
    ├── SKILL.md              # 必需
    └── references/           # 可选
        ├── template.md       # 模板文件
        ├── guide.md          # 使用指南
        └── sources.md        # 数据源清单
```

### SKILL.md 规范

```markdown
---
name: skill-name
description: |
  技能描述。当用户 [触发场景] 时触发。
  触发词：关键词1、关键词2、关键词3
---

# 技能标题

## 概述

简要描述技能的用途和核心能力。

## 核心能力

### 1. 能力名称

- 具体能力点
- 具体能力点

### 2. 能力名称

- 具体能力点

## 方法论（可选）

描述技能的执行方法论。

## 相关命令

| 命令 | 用途 |
|------|------|
| `/command` | 命令用途 |

## 参考文档

- [文档名称](./references/file.md)

## 使用示例

\`\`\`
用户: 示例请求
AI: 响应内容...
\`\`\`

## 注意事项

1. 注意点1
2. 注意点2
```

### Frontmatter 规范

| 字段 | 必需 | 说明 |
|------|------|------|
| `name` | ✅ | 技能名称，与目录名一致 |
| `description` | ✅ | 描述 + 触发场景 + 触发词 |

### references 目录

用于存放参考文档：
- **template.md** - 输出模板
- **guide.md** - 操作指南
- **sources.md** - 数据源/信息源清单

---

## 6. Marketplace 注册规范

插件需要在 `.claude-plugin/marketplace.json` 中注册：

```json
{
  "name": "plugin-name",
  "description": "插件描述（与 plugin.json 一致）",
  "source": "./plugin-name",
  "category": "productivity|development|design|integration"
}
```

### 分类 (category)

| 分类 | 说明 |
|------|------|
| `productivity` | 生产力工具 |
| `development` | 开发工具 |
| `design` | 设计工具 |
| `integration` | 集成工具 |

---

## 7. 验证清单

开发完成后，使用以下清单验证插件是否符合规范：

### 基础结构

- [ ] `plugin.json` 存在且格式正确
- [ ] `README.md` 存在且包含必需章节
- [ ] 目录结构符合规范

### plugin.json

- [ ] `name` 使用 kebab-case
- [ ] `version` 符合 semver 规范
- [ ] `description` 清晰描述功能
- [ ] `keywords` 包含中英文关键词
- [ ] 路径引用正确

### Commands

- [ ] frontmatter 包含 `description`
- [ ] 文件名使用 kebab-case
- [ ] 任务流程结构化（Step N）
- [ ] 使用 `{args}` 引用参数

### Skills

- [ ] 目录名与 `name` 字段一致
- [ ] `SKILL.md` 包含 frontmatter
- [ ] `description` 包含触发词
- [ ] 参考文档路径正确

### Marketplace

- [ ] 在 `marketplace.json` 中注册
- [ ] `category` 分类正确
- [ ] `source` 路径正确

---

## 8. 命名规范

### 插件名称

- 格式：`kebab-case`
- 示例：`brand-research`, `business-plan-generator`
- 避免：`BrandResearch`, `brand_research`

### 命令名称

- 格式：`kebab-case`
- 示例：`brand-analyze`, `create-outline`
- 调用方式：`/brand-analyze`

### 技能名称

- 格式：`kebab-case`
- 与目录名保持一致

---

## 9. Git 提交规范

使用 Conventional Commits：

```
feat: add new plugin
feat: add new command to plugin
fix: correct plugin manifest
docs: update plugin README
refactor: restructure plugin directory
chore: bump version to 1.1.0
```

---

## 10. 示例参考

完整示例请参考 `brand-research` 插件：

```
brand-research/
├── plugin.json
├── README.md
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   └── brand-analyze.md
└── skills/
    └── brand-research/
        ├── SKILL.md
        └── references/
            ├── report-template.md
            └── info-sources.md
```
