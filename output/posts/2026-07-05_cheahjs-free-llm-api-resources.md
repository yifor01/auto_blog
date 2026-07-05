---
title: cheahjs/free-llm-api-resources
source: GitHub Trending
url: https://github.com/cheahjs/free-llm-api-resources
score: 82
model: google/gemma-4-31b-it:free
generated_at: '2026-07-05T19:33:34.270681'
---

📌 【資源整理】想測試 LLM API 但不想花錢？這份清單幫你找齊免費路徑

TL;DR：彙整多個提供免費額度或試用點數的 LLM API 供應商，適合開發者快速原型開發。

對於 AI 工程師來說，測試不同模型的效能或快速搭建原型時，最頭痛的往往不是程式碼，而是每個平臺都要綁信用卡、且試用額度不一的繁瑣過程。

🛠️ **合法且多元的免費 API 供應商清單**

這個專案彙整了多個提供免費訪問或試用點數（credits）的 LLM API 服務。值得注意的是，作者明確排除所有非正規的服務（例如透過反向工程獲取的聊天機器人 API），確保列出的資源皆為合法路徑。

📦 **可直接使用的免費供應商（Free Providers）**

清單中涵蓋了多個知名平臺，開發者可根據需求選擇：
- 基礎平臺：Google AI Studio, NVIDIA NIM, Mistral (La Plateforme / Codestral), HuggingFace Inference。
- 閘道與推理服務：Vercel AI Gateway, OpenCode Zen, Cerebras, Groq, Cohere, GitHub Models, Cloudflare Workers AI。

💳 **提供試用點數的供應商（Providers with trial credits）**

除了完全免費的選項，部分平臺提供初始試用點數供開發者測試，包括：
- Fireworks, Baseten, Nebius, Novita, AI21, Upstage, NLP Cloud, Alibaba Cloud (International), Model Studio, Modal, Inference.net, Hyperbolic, SambaNova Cloud, Scaleway, Generative APIs。

💡 **以 OpenRouter 為例的配額限制**

針對 OpenRouter 的具體限制，README 指出其免費方案如下：
- 請求限制：每分鐘 20 次請求 / 每天 50 次請求。
- 額外提升：若進行 10 美元的終身儲值，每日請求上限可提升至 1000 次。
- 支援模型：包含 Llama 3.1 405B, Llama 3.2 3B Instruct, Llama 3.3 70B Instruct, 以及 NVIDIA Nemotron 系列、Google Gemma 4 系列等多款模型（模型間共用配額）。

⚠️ **使用原則：請勿濫用**

作者特別提醒，請勿濫用這些免費服務，否則可能會導致這些寶貴的免費資源被供應商關閉。

🎯 **實務啟示**

對於開發者而言，這份清單提供了一個快速切換模型的「實驗場」。在正式決定將模型部署至生產環境前，可以利用 Groq 或 Cerebras 等高效能推理平臺測試延遲，或透過 OpenRouter 快速對比不同模型（如 Llama 3.3 與 Gemma 4）的輸出差異，而無需為每個平臺單獨設定帳單。

🔗 **來源**
- 標題：free-llm-api-resources
- 作者／機構：cheahjs
- 連結：https://github.com/cheahjs/free-llm-api-resources

#LLM #API #OpenSource #DeveloperTools #FreeResources #MachineLearning #Llama3 #Gemma4 #AI #OpenRouter
