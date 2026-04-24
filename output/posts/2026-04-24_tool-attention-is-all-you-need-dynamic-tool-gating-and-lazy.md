---
title: "Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax in Scalable Agentic Workflows"
source: arXiv
url: http://arxiv.org/abs/2604.21816v1
score: 104
model: tencent/hy3-preview:free
generated_at: 2026-04-24T19:52:17.072118
---

📌 Tool Attention 消除 MCP 工具税

都在拚百萬 token 上下文？其實 MCP 工具稅早把你的上下文浪費光。
每輪對話僅工具 schema 注入就佔 10k-60k token，上下文利用率超過 70% 就會出現推理退化。
這篇論文提出的解法，能把工具 token 用量砍掉 95%。

🤔 **MCP 工具税正在吃掉上下文与预算**
Model Context Protocol（MCP）是目前 LLM Agent 连接外部工具的主流接口，但现有实现依赖无状态、急切式的 schema 注入机制，每轮对话都会加载所有工具的完整 JSON schema，单此一项就會產生約 10k 到 60k token 的額外 payload。這些無效 token 會大幅撐大 Transformer 推理所需的 KV（键值）缓存，增加運算成本與延遲，且當上下文利用率接近已發表的 70% 断裂點時
