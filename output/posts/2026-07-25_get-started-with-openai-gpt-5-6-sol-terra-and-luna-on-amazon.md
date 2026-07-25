---
title: Get started with OpenAI GPT-5.6 Sol, Terra, and Luna on Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/get-started-with-openai-gpt-5-6-sol-terra-and-luna-on-amazon-bedrock/
model: tencent/hy3:free
generated_at: '2026-07-25T07:50:32.342793'
score: 77
---

這是一篇針對產業新聞型別的技術報導。

📌 【Amazon Bedrock 新動態】OpenAI GPT-5.6 系列模型正式上架，提供三種能力層級供開發者選擇

TL;DR：OpenAI GPT-5.6 (Sol, Terra, Luna) 登陸 Amazon Bedrock，支援 272K context window 與 Responses API。

開發者在構建自主編碼代理（Agentic Coding）、長程推理（Long-horizon Reasoning）以及高吞吐量推論（High-volume Inference）工作負載時，往往需要在「尖端模型能力」與「基礎設施管理成本」之間取得平衡。現在，透過 Amazon Bedrock，你可以在熟悉的 API 架構下，直接呼叫 OpenAI 最新推出的 GPT-5.6 系列模型。

🧩 **GPT-5.6 命名系統：以能力層級區分模型**

OpenAI 在 GPT-5.6 引入了全新的命名邏輯：數字代表世代，而名稱（Sol、Terra、Luna）則代表具備永續性的能力層級（Capability Tiers），這些層級會隨著技術演進獨立更新。

📊 **三款模型對應不同工作負載**

| 模型名稱 | 定位與適用場景 |
| :--- | :--- |
| **Sol** | 旗艦級推理模型，專為複雜推理設計 |
| **Terra** | 平衡效能與成本，適用於日常生產環境 |
| **Luna** | 最佳化快速、低成本推論，適合對延遲敏感的任務 |

這三款模型皆具備以下共通特性：
- **輸入/輸出**：支援文字與圖片輸入，文字輸出。
- **上下文視窗**：272K token context window。
- **推理強度控制**：支援從 none 到 max 的六種推理強度（reasoning effort）設定，讓開發者無需更改 API 整合即可切換模型能力。
- **API 介面**：透過 OpenAI Responses API 進行存取。

🚀 **整合與開發者體驗**

- **存取方式**：開發者可透過 `bedrock-mantle` 端點存取，Base URL 格式為 `https://bedrock-mantle.{region}.api.aws`。
- **成本與管理**：定價與 OpenAI 原生費率一致，且使用量可計入現有的 AWS 承諾額度（AWS commitments）。
- **隱私與安全性**：提示詞（Prompts）與生成內容（Completions）不會被用於訓練模型，也不會與模型提供者共享。
- **進階功能**：支援 Prompt Caching（提示詞快取）以降低成本，並可衡量快取後的 token 使用量。

🎯 **實務啟示**

對於需要大規模部署 LLM 的工程師而言，這次更新的核心價值在於「右適化」（Right-sizing）：你可以根據任務的複雜度，在 Sol、Terra 與 Luna 之間靈活切換，同時利用 Amazon Bedrock 的區域處理（Regional processing）與安全管控能力，降低維護獨立模型基礎設施的負擔。

🔗 **來源**
- 標題：Get started with OpenAI GPT-5.6 Sol, Terra, and Luna on Amazon Bedrock
- 作者／機構：Zohreh Norouzi @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/get-started-with-openai-gpt-5-6-sol-terra-and-luna-on-amazon-bedrock/

#OpenAI #AmazonBedrock #GPT5 #LLM #CloudComputing #AWS #MachineLearning #GenerativeAI #SoftwareEngineering #CloudInfrastructure
