# Pyspider Strategy Deep Dive & Rules

## 通用红线：异常管理 (Exception Management)
*   **禁止**：`except Exception as e: pass`。
*   **允许**：对于网络波动（如 599），使用 `@catch_status_code_error` 让 Pyspider 处理。
*   **监控对齐红线 (NEW)**：**核心资源缺失（如 Cookie/Proxy 枯竭）禁止在 `on_message` 或 `on_start` 阶段直接抛错。** 必须通过 `save` 透传错误标记，在 `callback` 阶段抛出异常。
*   **目的**：确保异常发生在 Pyspider 的任务生命周期内，从而产生红色 `FAILED` 状态，触发项目熔断并发送 n8n Webhook。

## 重构红线：零字段损耗 (Zero Field Loss)
*   **原则**：对已有生产脚本进行优化时，数据结构（Payload/Result）的优先级高于代码优雅度。
*   **动作**：禁止删除任何看起来“没用”的 API 参数（如 `nodeIdPaths`），除非明确知道它是脏数据。

## 通用接口：on_message 驱动
所有脚本必须实现以下结构：
```python
def on_message(self, project, message):
    if project == self.project_name: return message
    # 解析来自 Dispatcher 的消息
    url = message.get('url')
    if url:
        self.crawl(url, callback=self.index_page)
```

## 策略分级 (A-E)
*   **策略 A (BD V3)**: 针对顶级反爬，执行三步走状态机。
*   **策略 B (Cookie)**: 强制使用 `ispProxy_us_`，在 `save` 中透传 `forced_cookies`。
*   **策略 C (SSR)**: 住宅代理，正则提取。
*   **策略 D (API)**: 数据中心代理，配合 MongoDB 任务状态位。
