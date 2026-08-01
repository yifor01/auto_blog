---
title: Nous Research Ships Three Integration Paths for Hermes Agent and Buzz, Block’s
  Open Source Nostr Workspace for Humans and Agents
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/31/nous-research-ships-three-integration-paths-for-hermes-agent-and-buzz-blocks-open-source-nostr-workspace-for-humans-and-agents/
model: tencent/hy3:free
generated_at: '2026-08-01T08:10:55.106942'
score: 87
---

📌 Nous Research 三種 Buzz 整合路徑釋出 Hermes Agent 支援  

TL;DR：Nous Research 釋出 Hermes Agent 支援 Buzz，提供三種自託管整合方式，讓人類與 AI 代理共享 Nostr 頻道。  

🎣 當 AI 代理也能擁有自己的 Nostr 身份時，人機協作的頻道不再需要傳統的 bot‑token 模型，這意味著身份、審計與訊息傳遞都能在同一個自託管環境中完成。  

🤔 背景與問題  
在先前的 AI 整合方案中，代理通常依賴平臺發放的 bot token 來取得身份，這限制了代理的獨立識別與審計能力。Buzz 透過 Nostr 協議將每則訊息作為簽署事件儲存在使用者自行擁有的中繼器上，人類與代理皆以金鑰對 (keypair) 代表身份，從而移除對 bot token 的依賴。  

🧩 方法與架構（三種整合路徑）  
摘要指出，Hermes Agent 的支援分為三種依執行位置而異的整合路徑：  

1. **Buzz Desktop 受控執行階段**  
   - 在 Buzz Desktop 內開啟 Settings → Runtimes，Hermes 會自動出現。  
   - 安裝程式會將 hermes‑acp 啟動器寫入 ~/.local/bin，透過登入 shell PATH 進行探索。  
   - Buzz 在本機以預設 harness 形式啟動 Hermes，傳入方為 ACP over stdio。  

2. **Relay Bridge（適合託管代理身份）**  
   - Buzz 的 buzz‑acp harness 將頻道透過 stdio 與 hermes‑acp 連結，再經由 WebSocket 連到中繼器。  
   - 此方式僅是傳輸層整合，不需額外安裝第二套軟體。  
   - 被啟動的子程序共享與該主機上 Hermes 相同的設定、憑證、記憶體、技能與狀態。  

3. **原生 Gateway 平臺（最深層整合）**  
   - 隨附的 buzz plugin 讓 Buzz 成為 Hermes 的一般訊息平臺，與 Telegram、Discord 並列。  
   - 支援頻道、私訊、提及門檻、執行緒回覆、反應、圖片與定時傳送（cron delivery）。  
   - Hermes 保留自己的核準、記憶與會話管理。  
   - 設定步驟為 hermes gateway setup。  
   - 入站透過持久的 NIP‑42 驗證 Nostr WebSocket 進行，內建依賴免費的 BIP‑340 簽章，失敗時自動回退至 CLI polling。  
   - 出站永遠經由 buzz CLI。  
   - 傳輸設定接受 auto、websocket 或 poll，poll_interval 預設為 4 秒。  
   - 建議的預設值為私有模式：  
     * require_mention: true → 代理僅在被頻道提及時回覆，私訊則一直發送。  
     * allow_all_users: false → 僅允許列出的 npubs 或十六進位公鑰存取。  
     * interim_assistant_messages: false 與 tool_progress: off → 工具日誌不會出現在頻道中。  
   - 事件會根據 per‑channel 高水位線按 event id 去重，並過濾掉代理自身的公鑰訊息。  

📊 數據與授權資訊  
- Buzz 以 Apache‑2.0 授權發布，目前在 GitHub 上擁有 18.8k 個星標。  
- Hermes Agent 使用 MIT 授權。  

💡 深入分析  
文章強調，三種路徑分別對應不同使用規模：  
- 個人開發者或小團隊可透過 Buzz Desktop 零設定快速啟用。  
- 中規模平臺團隊則適合採用 Relay Bridge，因其中繼器依賴 Postgres、Redis 與 S3/MinIO。  
- 企業層面則建議先以試點方式評估，因為行動客戶端與工作流審核閘門仍在開發中。  

⚠️ 限制與尚未完成的功能  
- 行動客戶端以及工作流批准閘門目前仍在鋪設中，企業在正式採用前應先行試點。  
- 文件未提及效能基準或延遲數據，因此實際部署時仍需自行驗證。  

🎯 實務啟示  
- 若是想快速體驗人機共同頻道，個人開發者可直接安裝 Buzz Desktop，啟用 Hermes 後即可在同一個頻道看到人類與代理的訊息。  
- 平臺工程師若需在現有基礎設施上運行代理，可採用 Relay Bridge，利用現有的 Postgres、Redis 與物件儲存作為中繼器後端。  
- 對於希望將 Buzz 完全納入 Hermes 訊息生態的企業，則應先評估原生 Gateway 平臺的適合度，並注意目前仍缺少行動端與審核流程的完整支援。  

🔗 來源  
- 標題：Nous Research Ships Three Integration Paths for Hermes Agent and Buzz, Block’s Open Source Nostr Workspace for Humans and Agents  
- 作者／機構：Michal Sutter  
- 連結：https://www.marktechpost.com/2026/07/31/nous-research-ships-three-integration-paths-for-hermes-agent-and-buzz-blocks-open-source-nostr-workspace-for-humans-and-agents/  

#NousResearch #HermesAgent #Buzz #Nostr #OpenSource #AIIntegration #SelfHosted #DeveloperTools #MarkTechPost #AgenticWorkflow
