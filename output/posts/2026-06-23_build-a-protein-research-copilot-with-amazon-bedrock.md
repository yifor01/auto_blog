---
title: Build a protein research copilot with Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-a-protein-research-copilot-with-amazon-bedrock-agentcore/
score: 96
model: google/gemma-4-31b-it:free
generated_at: '2026-06-23T20:27:13.734823'
---

📌 【AWS 實作】利用 Bedrock AgentCore 打造蛋白質研究 Copilot，將序列搜尋自然語言化

TL;DR：結合 Bedrock AgentCore 與 ESM-C 300M 嵌入模型，將複雜的蛋白質相似度搜尋轉化為對話式 AI 助手。

蛋白質研究者經常面臨一個極其耗時的挑戰：必須在數以千計的胜肽（peptide）序列中手動搜尋結構相似的候選者。這個過程不僅緩慢且容易出錯，更需要深厚的領域專業知識才能解讀結果。

🤔 **從手動搜尋到對話式 AI 助手**

為了改變這種現況，透過建立蛋白質研究 Copilot，研究人員可以用自然語言直接查詢，由系統自動生成 embedding 並總結結果，將整個工作流整合在單一的對話介面中。

🧩 **單一執行時、多工具的代理架構**

該系統採用 tool-use 模式，由一個 Strands Agent 協調三個專門工具來處理完整的研究流程。其核心設計理念是維持部署簡單，同時確保關注點分離（separation of concerns）。

當研究人員提交自然語言查詢時，流程如下：
解析自然語言查詢 → 轉換為結構化參數 → 利用蛋白質 embedding 搜尋相似胜肽 → 結合科學背景總結結果。

系統由以下五個關鍵元件構成：
- **Strands Agents SDK**：負責協調單一 Agent 內的三個專門工具。
- **Amazon Bedrock AgentCore**：用於生產環境的部署與服務。
- **Amazon Aurora PostgreSQL-Compatible Edition**：搭配 pgvector 擴充功能，儲存胜肽的 embedding。
- **ESM-C 300M**：由 EvolutionaryScale 開發的蛋白質語言模型，負責產生 960 維度的 embedding，用以捕捉氨基酸序列的結構與功能特性。
- **協調機制**：Orchestrator Agent 會根據使用者查詢，決定何時以及如何呼叫對應工具。

💡 **利用蛋白質語言模型實現結構搜尋**

這套系統的核心在於 ESM-C 300M 模型。該模型能將氨基酸序列轉化為高維向量，使得具有相似生物功能的兩種胜肽會產生相近的 embedding，從而讓 AI 能精準地在大型資料集中找出結構相似的候選者。

🎯 **實務啟示**

對於 AI 工程師而言，此案例展示了如何將「特定領域模型（ESM-C 300M）」與「代理框架（Bedrock AgentCore）」結合。關鍵在於將複雜的專業搜尋流程拆解為多個專門工具，再由一個 Orchestrator 負責排程，這能有效降低部署複雜度，同時提供直覺的自然語言操作介面。

🔗 **來源**
- 標題：Build a protein research copilot with Amazon Bedrock AgentCore
- 作者／機構：Yuan Tian @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/build-a-protein-research-copilot-with-amazon-bedrock-agentcore/

#AWS #AmazonBedrock #ProteinResearch #Bioinformatics #LLM #AgentCore #pgvector #ESMC #Embedding #MachineLearning
