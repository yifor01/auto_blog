---
title: How Intuit built an agentic disaster recovery assistant with Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-intuit-built-an-agentic-disaster-recovery-assistant-with-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-09-04T19:49:09.202266'
score: 91
---

📌 Intuit 怎麼用 Amazon Bedrock，把災難復原的「判斷」也交給 AI

TL;DR：Intuit 打造 EWOK Agent，用 Amazon Bedrock 把災難復原決策自動化，執行仍交給既有的確定性系統。

當數千個微服務橫跨多個 AWS 區域，一次可靠的 failover 該怎麼協調？這對 Intuit 這種支撐 TurboTax、QuickBooks、Mailchimp、Credit Karma 等產品的公司來說，是規模化之後才會浮現的真實難題。

🤔 系統會執行，但「該怎麼判斷」還是要靠老工程師的經驗

Intuit 內部原本就有一套集中式災難復原系統 EWOK（Ecosystem Wide Orchestrator Kit），服務擁有者用 YAML 宣告復原意圖，EWOK 負責協調底層的運算、資料庫、網路、快取與非同步工作負載，把支援的工作負載復原時間從數小時壓縮到約 20 分鐘。但 EWOK 解決的是「執行」，沒有解決「決策」：該套用哪個復原流程、資產是否真的就緒、復原過程中冒出的例外狀況該怎麼處理，長期以來都仰賴資深 on-call 工程師的隱性知識（tribal knowledge）。

文章舉了一個具體例子：在 change-freeze window（為了保護服務可用性、限制變更的關鍵時段，例如報稅季）期間，failover 請求預設會被系統拒絕，工程師必須熟悉緊急覆寫流程才能繼續執行。這類判斷過去只存在於人的記憶裡。

🧩 EWOK Agent：模型負責判斷，EWOK 負責確定性執行

為了補上這塊決策缺口，Intuit 打造了 EWOK Agent，一個以 Amazon Bedrock 為推理層、疊加在既有 EWOK 系統之上的 AI agent，過去八個月已由 Intuit 內部多個團隊實際用來執行 failover。文章特別強調一個貫穿全文的設計原則：模型決定「做什麼」，EWOK Agent 確定性地執行「怎麼做」。

選擇 Amazon Bedrock 的原因，是它讓團隊能透過單一 API 存取多家供應商的基礎模型，評估並替換適合 failover 推理的模型時不需要重新設計整個 agent 架構；同時內建 Amazon Bedrock Guardrails 與安全隱私保護，資料不會被用於訓練模型，並在傳輸與靜態時皆加密，這在 agent 直接操作生產環境的財務系統時尤其關鍵。由於 Bedrock 是全託管服務，這層推理能力可以疊加在 EWOK 之上，不需要自行佈建或維運模型基礎設施。EWOK Agent 目前以外掛形式提供，工程師可以直接從 Intuit 的工程入口網站或慣用的 IDE 安裝使用。

架構設計的核心是把「寫給人看的 runbook」改寫成「skill」，也就是同時可被人閱讀、也可被機器消費的能力定義：每個 skill 是一份 Markdown 檔案，其中的 schema 會直接編譯成模型推理時使用的工具定義，skill 描述的動作再透過真正的執行器呼叫 EWOK 的 API。Prompt 主體刻意採用結構化、規則導向的格式，而不是自由散文，讓 change-freeze window 之類的政策關卡（policy gate）能以明確的條件分支寫進 skill 內容裡，取代過去存在工程師記憶中的判斷。Skill 本身刻意設計為與基礎模型無關，中間有一層薄的 Amazon Bedrock 層負責把 skill 與具體的基礎模型串接起來，讓模型能依上下文選擇合適的能力。

從工程師的實際體驗來看，一句「Failover payments-gateway in production」的自然語言請求，就取代了過去一連串的 runbook 查閱與 console 操作；工程師仍留在迴圈中做判斷與核准，但不再需要親自扮演 orchestrator 的角色。每一次執行都會透過 change record 在變更管理系統中留下正式紀錄，確保每一次 failover 都經過授權且可追溯，走的是與人工操作者相同的流程。

🎯 這個模式能複製到 EWOK 以外的系統嗎

文章特別點出，EWOK 本身是 Intuit 的內部系統，但「typed skills、薄 Bedrock 層、對確定性執行器加上有邊界的 agentic loop」這套模式並不綁定 EWOK，可以套用到任何暴露出可驗證、可稽核 API 的系統上。對正在思考如何把 LLM 導入高風險維運場景的團隊來說，這個「模型只負責決策、執行永遠交給既有確定性系統」的邊界劃分，或許比模型本身的選型更值得參考。

🔗 來源
- 標題：How Intuit built an agentic disaster recovery assistant with Amazon Bedrock
- 作者／機構：Suvojit Dasgupta, AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/how-intuit-built-an-agentic-disaster-recovery-assistant-with-amazon-bedrock/

#AmazonBedrock #DisasterRecovery #AIAgents #Intuit #AWS #SRE #AgenticAI #CloudInfrastructure #LLMOps #DevOps
