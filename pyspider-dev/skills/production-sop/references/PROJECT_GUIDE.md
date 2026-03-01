# Pyspider Project Constitution (Constitution V4.9)

## 1. 核心架构与决策
*   **Strategy A (BrightData V3)**: 针对顶级反爬。
    *   **BD 纯净请求协议 (The Pure Protocol)**:
        1. **参数严禁加塞**：URL 中严禁添加任何非官方文档要求的参数（如 `_t`, `timestamp`）。
        2. **物理 1:1 对齐**：Payload 必须使用 `separators=(',', ':')` 且层级必须与官方 CURL 示例完全一致。
        3. **原生传参**：强制使用 `self.crawl(url, params={...})` 构造请求，严禁手动拼接 URL 字符串以防格式错误。
    *   **硬性红线**：必须校验 `records` 字段。若 `status` 为 `ready/done` 但 `records == 0`，必须抛出 `BD_EMPTY_DATA`。

## 2. 绝对工程红线
*   **监控解耦 (Observer Pattern)**：脚本内禁止直接调用飞书/Webhook。报警分发由 `result_collector.py` 完成。
*   **异常变红原则**：必须通过 `raise Exception` 触发 Pyspider 的 `FAILED` 状态。
*   **仓库纯净**：只准提交 `.py` 脚本。严禁提交 `./skills`, `.md`, `.json`。
*   **业务注册闭环**：新脚本上线必须执行 `Script -> Git -> register_business.py`，且**严禁修改 `name` 字段**。
