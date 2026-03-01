---
name: sync-spider
description: "同步 PySpider 脚本到代码仓。使用场景：(1) AI 生成新爬虫脚本后需要上传 (2) 更新现有爬虫脚本 (3) 将本地脚本持久化到 git 仓库。执行：写入本地文件 → git commit → git push → webhook 自动同步到 webui"
---

# Sync Spider

将 PySpider 脚本同步到代码仓库，触发 webhook 自动更新到 webui。

## 使用场景

| 场景 | 说明 |
|------|------|
| AI 生成新脚本 | AI 写完爬虫代码后调用此 skill |
| 更新现有脚本 | 修改脚本后同步到仓库 |
| 批量同步 | 多个脚本一起提交 |

## 执行流程

```
1. 写入本地文件: /Users/mac/Desktop/spiders-x/{project_name}.py
2. git add {project_name}.py
3. git commit -m "feat: {project_name}"
4. git push
5. webhook 自动触发 → projectdb 更新 → webui 显示
```

## 参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| project_name | string | 是 | 项目名，如 `ScrapingAmazonList` |
| script_content | string | 是 | 脚本完整内容 |
| commit_message | string | 否 | 自定义 commit 信息，默认自动生成 |

## 调用示例

```
同步单个脚本:
sync_spider(project_name="ScrapingAmazonList", script_content="...")

自定义 commit 信息:
sync_spider(project_name="ScrapingAmazonList", script_content="...", commit_message="fix: 修复分页bug")
```

## 执行脚本

```bash
python scripts/sync_spider.py --project_name "ScrapingAmazonList" --script_content "..."
```

## 注意事项

- 确保 spiders-x 目录是 git 仓库
- 确保有 push 权限
- 脚本文件名自动添加 `.py` 后缀
- 如果文件已存在会覆盖

## 错误处理

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| git push failed | 无权限或网络问题 | 检查 git 配置和网络 |
| file write error | 权限问题 | 检查目录写权限 |
| not a git repo | 目录不是 git 仓库 | 确认目录正确 |
