---
title: BerriAI/litellm
source: GitHub Trending
url: https://github.com/BerriAI/litellm
score: 88
model: google/gemma-4-31b-it:free
generated_at: '2026-06-24T20:10:22.574159'
---

📌 【BerriAI】LiteLLM：用一套 OpenAI 格式，呼叫超過 100 種 LLM 的統一閘道

TL;DR：開源 AI Gateway，將 100+ 個 LLM 供應商統一為 OpenAI 格式，減少切換模型的開發成本。

在開發 LLM 應用時，最頭痛的往往不是提示詞工程，而是每個模型供應商的 SDK、驗證方式、請求格式與錯誤型別都截然不同。每切換一個模型，就得重寫一遍整合程式碼。

🤔 **管理多個 LLM 供應商的開發摩擦**

當專案需要同時使用 OpenAI、Anthropic、Gemini 或 Azure 等不同模型時，工程師必須面對繁瑣的 SDK 管理與格式轉換。LiteLLM 的核心目標就是消除這種摩擦，讓開發者能透過單一介面與所有模型溝通。

🧩 **統一 API 介面與部署靈活性**

LiteLLM 提供兩種使用方式，滿足不同規模的開發需求：
- **Python SDK**：直接作為函式庫整合程序式碼中。
- **AI Gateway (Proxy Server)**：部署為集中式服務，供整個團隊或組織使用。

其核心功能包含：
- **OpenAI 格式相容**：支援直接替換供應商而無需重寫程式碼。
- **廣泛的端點支援**：涵蓋 `/chat/completions`、`/embeddings`、`/images`、`/audio`、`/rerank` 等多種端點。
- **企業級管理功能**：內建虛擬金鑰 (Virtual Keys)、花費追蹤 (Spend Tracking)、護欄 (Guardrails)、負載平衡 (Load Balancing) 以及管理後臺。

📊 **高效能表現與實務採用**

根據其基準測試，LiteLLM 在 1k RPS (每秒請求數) 的壓力下，P95 延遲僅為 8ms。目前已有 Netflix 等企業採用此方案。

🎯 **實務啟示**

對於需要頻繁對比不同模型效能，或希望在基礎設施層面統一管理 LLM 成本與許可權的團隊，LiteLLM 提供了一個低成本的抽象層。工程師可以將其視為「LLM 的介面卡」，在不變動業務邏輯的前提下，快速切換底層模型以最佳化成本或效能。

🔗 **來源**
- 標題：litellm
- 作者／機構：BerriAI
- 連結：https://github.com/BerriAI/litellm

#LLM #AIGateway #OpenAI #OpenSource #Python #API #Infrastructure #SoftwareEngineering #BerriAI #LiteLLM
