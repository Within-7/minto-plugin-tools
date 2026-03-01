# Pyspider Production SOP (V5.0 - Dual-Mode Standard)

## 🏗 开发模式：从零构建 (New Project Mode)
1.  **选样板**：根据目标网站特征，从 `REFERENCE_INDEX.json` 选择 Strategy A-E。
2.  **定契约**：查清 `ScrapingMongoQuery` 中预设的 `name` 和 `scrap_key`。
3.  **组装**：强制使用 `Functions.get_dict_by_dot` 和 `raise Exception` 变红逻辑。

## 🛡 优化模式：火线修理 (Refactor & Debug Mode) - 【核心红线】
1.  **契约锁定 (Pre-Audit)**：
    *   **Headers 基因**：必须通过 `read_file` 提取旧代码全量 Headers（含 Sec-* 字段）。
    *   **数据资产**：必须提取旧代码中所有的输出键名（Result Keys）。
2.  **影子还原原则 (Shadow Preservation)**：
    *   **严禁阉割指纹**：禁止为了代码简洁而删除原有的浏览器指纹 Headers。
    *   **字段 1:1 对齐**：优化后的 `result` 字段名必须与旧版本像素级一致，严禁增减、修改。
    *   **代理继承**：严禁随意更改旧代码验证过的代理类型（如 MX 住宅代理）。
3.  **透明化审计**：如果优化后的行数明显减少，必须在执行前说明“精简了哪些冗余逻辑”，严禁偷摸删除核心逻辑。

## 📋 全局工程红线 (Global Redlines)
1.  **异常必红**：严禁 `logger.error` 后静默 `return`，必须 `raise Exception` 触发 FAILED。
2.  **三位一体**：`Script (on_message)` + `Git (Pure .py)` + `DB (register_business.py)` 必须同步闭环。
3.  **禁改 Name**：严禁在更新数据库配置时修改 `name` 字段，否则会打断调度映射。
4.  **仓库洁癖**：Git 仅提交 `.py`。严禁提交 `./skills`、`.md`、`.json`。

## 🗣 沟通协议
*   **非读必同步**：任何修改、写库操作前，必须同步逻辑变更并获得确认。
