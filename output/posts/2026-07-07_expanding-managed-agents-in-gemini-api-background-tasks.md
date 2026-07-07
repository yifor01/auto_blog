---
title: 'Expanding Managed Agents in Gemini API:  background tasks, remote MCP and
  more'
source: Google AI Blog
url: https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api/
score: 126
model: google/gemma-4-31b-it:free
generated_at: '2026-07-07T21:00:08.875141'
---

📌 Gemini API 新增 Managed Agents 功能：支援背景執行、遠端 MCP 與自訂函式

TL;DR：Google 在 Gemini API 中為 Managed Agents 加入背景任務、遠端 MCP 連線與憑證重新整理，讓開發者能更輕鬆建置可長時間執行的生產級代理。

🎣 開場  
在開發自動化 AI 代理時，最常碰到的瓶頸是「長時間執行」與「跨服務認證」的管理。Google 這次針對 Gemini API 的 Managed Agents 釋出多項新功能，直接回應開發者對可靠性與可維護性的需求。

🤔 背景：Managed Agents 的核心價值  
Managed Agents 讓開發者只需呼叫單一端點，Gemini 便在雲端沙盒內負責推理、程式碼執行、套件安裝、檔案管理與網路資訊抓取。這樣的抽象層已足以支援 AI 編碼助理，只要在本機安裝 `gemini-interactions-api` skill 即可開始使用。

🧩 新增功能概覽  
- **背景執行 (background execution)**：將 `background: true` 加入請求，即可讓互動在伺服器端非同步執行。API 立即回傳一個 ID，客戶端可透過輪詢或串流方式取得任務進度，甚至在稍後重新連線繼續監控。  
- **遠端 MCP 伺服器整合**：支援直接連線至遠端 Managed Control Plane (MCP) 伺服器，減少自行部署控制平面的複雜度。  
- **自訂函式呼叫 (custom function calling)**：開發者可在代理流程中註冊自訂函式，讓 Gemini 在推理過程中動態呼叫外部程式碼。  
- **憑證重新整理 (credential refresh)**：在多輪互動中，系統會自動更新存取憑證，避免因過期而中斷服務。

📊 使用方式示例（以 @google/genai JavaScript SDK 為例）  
```js
import { Gemini } from '@google/genai';

// 建立互動，啟用背景模式
const interaction = await Gemini.interact({
  prompt: '分析大型資料集並產生報告',
  background: true,   // ← 交給伺服器非同步執行
});

// 取得任務 ID 後可輪詢狀態
const status = await Gemini.checkStatus(interaction.id);
```
*Python、cURL 版範例請參考 Antigravity agent 檔案。*

💡 深入分析：為什麼這些改進重要  
- **長時間任務不再依賴持久連線**：傳統上必須保持 HTTP 連線才能等待結果，易受網路中斷影響。背景模式將計算移至雲端，客戶端只要儲存回傳的 ID，即可彈性取得結果。  
- **遠端 MCP 降低部署門檻**：開發者不必自行管理 MCP 基礎設施，只要提供遠端服務位址，即可利用 Google 已建置的安全沙盒。  
- **自訂函式提升彈性**：允許代理在執行期間呼叫企業內部 API 或專屬工具，擴充套件了 Gemini 代理的適用範圍。  
- **憑證自動重新整理保證連續性**：對於需要多輪授權的應用（如資料庫存取、雲端服務），自動重新整理機制避免因憑證過期導致的中斷。

⚠️ 限制與注意事項  
- 背景執行僅在 Gemini Interactions API 支援的沙盒環境內可用，需確認服務已開啟 `background` 引數。  
- 遠端 MCP 整合仍需要事先在 Google Cloud 上設定授權與網路存取許可權，檔案中未說明具體步驟，建議先行閱讀官方指南。  

🎯 實務啟示  
- **建置長時間跑的資料處理代理**：可直接利用背景執行，避免前端逾時或頻繁重試。  
- **整合內部系統**：透過自訂函式呼叫，將 Gemini 代理與企業既有 API 串接，實現端到端自動化。  
- **安全性考量**：憑證重新整理機制減少手動更新的風險，適合需要持續存取受保護資源的應用。

🔗 來源  
- 標題：Expanding Managed Agents in Gemini API: background tasks, remote MCP and more  
- 作者／機構：Google — Philipp Schmid, Mariano Cocirio  
- 連結：https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api/

#GeminiAPI #ManagedAgents #BackgroundExecution #RemoteMCP #CustomFunctions #CredentialRefresh #AIAgents #GoogleAI #DeveloperTools #CloudSandbox
