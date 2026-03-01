# Database & Business Consistency Guide

## 1. 业务注册 (Registration)
新脚本完成后，必须在 `ScrapingMongoQuery` 中增加映射记录名。
*   **Pipeline 规则**：使用 `$match` 匹配 `scrap_key` -> 使用 `$project` 映射字段。
*   **字段命名**：映射后的字段名应使用中文，方便 Excel 展示。
*   **工具调用**：`python3 skills/tools/register_business.py '<JSON>'`

## 2. 彻底销毁 (Destruction)
删除一个 `.py` 脚本时，必须遵循以下联动：
1.  **物理删除**：`rm [Script].py`。
2.  **Git 同步**：`git add .` -> `git commit`。
3.  **库表清理**：调用 `python3 skills/tools/delete_project.py [project_name]` 从 MongoDB 核心表中移除该项目。
