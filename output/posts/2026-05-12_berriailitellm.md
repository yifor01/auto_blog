---
title: "BerriAI/litellm"
source: GitHub Trending
url: https://github.com/BerriAI/litellm
score: 115
model: tencent/hy3-preview:free
generated_at: 2026-05-12T20:38:14.673514
---

📌 【BerriAI】LiteLLM：一個統一 OpenAI 介面，支援 100+ LLM  

你是否曾因要切換不同 LLM 提供者而寫了好幾套 SDK？這個開源專案說它能讓你只用一行程式碼就搞定。  

🤔 **管理多個 LLM 變得越來越複雜**  
如今市面上有 OpenAI、Anthropic、Gemini、Bedrock、Azure 等十餘家供應商，各自的 SDK、認證方式、請求格式與錯誤處理都不相同。對於需要同時呼叫多個模型的應用來說，這意味著要維護大量重複的程式碼與測試流程，開發效率因而大打折扣。  

🧪 **LiteLLM 的設計：統一介面 + 代理伺服器**  
LiteLLM 提供兩種使用方式：  
1. **Python SDK** – 直接在程式中呼叫 `completion()`，內部會依照設定自動轉換為對應供應商的 API。  
2. **AI Gateway (Proxy Server)** – 部署為獨立服務，團隊內部所有請求經過此 gateway，統一走 OpenAI 格式，後續由 LiteLLM 轉發至真正的供應商。  

該專案宣稱支援 **100+ LLM 提供者**，涵蓋聊天、嵌入、圖像、音訊、批次處理、重排序等常見端點（`/chat/completions`、`/embeddings`、`/images` 等），並提供以下企業級功能：  
- 虛擬金鑰管理  
- 消費追蹤與預警  
- 安全防護欄位（guardrails）  
- 負載平衡  
- 管理儀表板  

根據基準測試，在 **1k RPS** 下，**P95 延遲約為 8ms**，顯示其在高並發場景下的響應速度。  

💡 **為什麼統一介面能減少開發負擔？**  
- **免除 SDK 切換**：開發者只需學習一次 OpenAI 格式，即可在不同供應商間無縫切換，程式碼不需重寫。  
- **集中治理**：所有請求經過同一個 gateway，審計、花費控制與政策執行變得更簡單。  
- **降低維護成本**：不必為每個供應商維護獨立的錯誤處理與重試邏輯，減少因 API 變更導致的突發故障。  

⚠️ **已知限制（根據現有說明）**  
- 文件中未提及對最新模型版本的即時支援情況，需自行確認特定供應商的更新頻率。  
- 企業版功能（例如進階安全合規、SLA）僅在說明中簡單帶過，細部實作尚未公開。  
- 作為開源專案，長期穩定度與社群回應速度仍取決於貢獻者的投入。  

🎯 **實務建議**  
- 若你的產品需要同時測試或切換多個 LLM（例如 A/B 測試不同供應商的效能），可先以 Python SDK 原型驗證。  
- 對於需要統一監控與成本控制的內部平台，考慮部署 LiteLLM Proxy 作為內部 AI Gateway，搭配其消費追蹤與儀表板進行預算管理。  
- 在正式上線前，請自行進行安全審查與效能基準測試，以確保符合貴組織的合規與延遲需求。  

🔗 **專案連結**  
📦 GitHub：https://github.com/BerriAI/litellm  
📖 文件與範例：同上連結內的 Docs 區塊  

你有在專案中嘗試過統一多模型介面的需求嗎？歡迎在留言區分享你的經驗或疑問 👇  

#LiteLLM #AIgateway #OpenAI #LLM #BerriAI #多模型應用 #開源工具 #AI基礎設施
