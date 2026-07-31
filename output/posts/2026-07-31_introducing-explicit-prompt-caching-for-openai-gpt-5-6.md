---
title: Introducing explicit prompt caching for OpenAI GPT-5.6 models on Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/introducing-explicit-prompt-caching-for-openai-gpt-5-6-models-on-amazon-bedrock/
model: tencent/hy3:free
generated_at: '2026-07-31T08:43:37.751997'
score: 81
---

📌 【Amazon Bedrock 新功能】GPT-5.6 系列正式登場，顯式 Prompt Caching 讓 Agent 成本直降九成

TL;DR：OpenAI GPT-5.6 系列登陸 Amazon Bedrock，新增「顯式 Prompt Caching」功能，重複使用的快取輸入可享 90% 折扣。

OpenAI 最新的 GPT-5.6 系列模型現在已經在 Amazon Bedrock 上正式可用。這次更新不僅帶來了全新的模型家族，更引入了「顯式 Prompt Caching（Explicit Prompt Caching）」功能，讓開發者能精準控制哪些 Prompt 內容需要被快取，大幅優化 Agentic Workflow（代理型工作流）的成本結構。

🧩 **GPT-5.6 家族：針對不同需求提供三種能力層級**

這次在 Amazon Bedrock 上推出的 GPT-5.6 模型家族，根據任務複雜度分為三個層級：

- **GPT-5.6 Sol**：專為最複雜的推理（Reasoning）與 Agentic Coding（代理編程）工作設計。
- **GPT-5.6 Terra**：適合日常生產環境中，兼顧效能與成本的平衡型工作負載。
- **GPT-5.6 Luna**：針對高吞吐量、快速任務（如分類與摘要）進行最佳化。

💡 **顯式 Prompt Caching：精準控制快取內容並節省 90% 成本**

以往的快取機制通常是隱式的，而這次 GPT-5.6 引入的「顯式 Prompt Caching」讓開發者擁有更精確的控制權。

- **節省成本**：使用快取的輸入內容（Cached input），其費用僅為原來的 10%（即 90% 折扣）。
- **快取時效**：快取內容會保留 30 分鐘，供後續請求重複使用。
- **最佳適用場景**：在 Agentic Workflow 中，系統指令（System instructions）、工具定義（Tool definitions）以及參考文件（Reference documents）通常會在多次呼叫中重複出現，使用此功能能獲得最大價值。

🛠️ **開發者整合指南：使用 OpenAI 相容的 Responses API**

開發者可以透過 Amazon Bedrock 的 `bedrock-mantle` 端點，使用與 OpenAI 相容的 Responses API 來呼叫這些模型。

- **身份驗證**：建議使用由 AWS 憑證產生的短期 Bearer Token。
- **實作方式**：開發者可以在安裝 OpenAI SDK 的同時，安裝 Token 產生器，並利用標準的 AWS 憑證鏈（如 IAM Roles 或環境變數）來建立 Client。

🎯 **實務啟示**

對於正在開發 Agent 或需要處理大量長文本（Long Context）的工程師來說，這是一個關鍵的成本優化手段。透過手動指定需要快取的 Prompt 區塊，可以大幅降低在重複對話或複雜代理任務中的 Token 消耗支出。

🔗 **來源**
- 標題：Introducing explicit prompt caching for OpenAI GPT-5.6 models on Amazon Bedrock
- 作者／機構：Melanie Li @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/introducing-explicit-prompt-caching-for-openai-gpt-5-6-models-on-amazon-bedrock/

#OpenAI #AmazonBedrock #GPT56 #PromptCaching #GenerativeAI #LLM #AWS #MachineLearning #AIEngineering #AgenticWorkflow
