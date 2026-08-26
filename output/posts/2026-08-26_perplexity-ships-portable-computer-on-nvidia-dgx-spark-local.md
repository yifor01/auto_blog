---
title: 'Perplexity Ships Portable Computer on NVIDIA DGX Spark: Local Harness, OS-Enforced
  Sandbox, and Zero Per-Token Cost for Local Steps'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/25/perplexity-ships-portable-computer-on-nvidia-dgx-spark-local-harness-os-enforced-sandbox-and-zero-per-token-cost-for-local-steps/
model: claude-code/sonnet
generated_at: '2026-08-26T06:24:15.374790'
score: 95
---

📌 Perplexity 把 Agent 平臺搬進 DGX Spark，本地任務零 token 費用

TL;DR：Perplexity 推出 Portable Computer，將整套 agent 系統打包跑在 NVIDIA DGX Spark 上，本地步驟不收 per-token 費用，只有需要時才升級到雲端模型。

當多數 AI agent 產品都在比拚雲端模型的推理能力時，Perplexity 選了一條反方向的路：把 agent harness、orchestrator、planner、tool router 和後訓練模型整套搬到你桌上的硬體裡跑。這不是一個帶檔案選取器的本地聊天工具，而是把推論伺服器、工具沙箱與應用程式連接器都封裝成一個系統，省去自己架設推論服務、手動接工具的工夫。

🤔 **本地優先，但不是本地唯一**

Portable Computer 是 Perplexity 既有 agentic Computer 平臺的本地優先（local-first）版本，跑在 NVIDIA DGX Spark 上。每個任務都從本機開始，交給本地模型處理的工作不收 per-token 費用。當某個步驟需要即時網路資訊或前沿推理能力時，orchestrator 會停下來詢問使用者，取得同意後才把「那一個步驟」送到 15 個以上的雲端模型之一，其餘對話與工具存取不會離開本機。

🧩 **模型選擇、沙箱與隱私把關怎麼做**

使用者可以選擇 Qwen 3.8 27B 或 PPLX 27B（Perplexity 針對自家 harness 後訓練的版本），NVIDIA Nemotron 3.5 Lightning（開源 30B MoE 模型）標示為即將推出，也支援自帶模型與推論伺服器（bring-your-own）。

程式碼與工具呼叫都在一個 OS 強制執行的沙箱內運行，限制行程、檔案系統路徑與網路存取；如果沙箱不可用，系統會直接停用工具執行，而不是悄悄降級運作。Gmail、Outlook、Slack、GitHub 等連接器都透過本地 orchestrator 路由。

在送出任何雲端呼叫前，harness 會先挑選相關的上下文，跑一個 PII 分類器過濾，並明確顯示哪些內容即將離開機器；獲準的步驟送往雲端模型，遠端顧問只回傳文字建議，不會直接存取本地檔案、工具或對話內容。

針對小模型的 context 限制，Perplexity 也做了針對性工程：Qwen 3.8 27B 標榜 260K token 的視窗，但過了約 100K 就會出現效能衰退，因此 harness 刻意讓 system prompt 與工具集保持精簡，需要時才動態載入特定技能，把連接器暴露成精簡的 CLI 工具而非完整的 MCP 定義，並在執行過程中壓縮過時的上下文。

📊 **本地跑分逼近前沿模型，混合模式最具參考價值**

| Benchmark | Computer（本地模型） | 對照組 |
|---|---|---|
| Local Knowledge Work Bench（53 題） | Qwen 3.8 27B 82.6%，PPLX 27B 85.4% | Pi harness 77.6%、Hermes 74.0%（同模型） |
| BrowseComp | 66.7% | Pi 50.2%、Hermes 43.9%（Wall time 少 51%、token 少 70%，對比 Pi） |
| ParseBench-100（視覺文件理解） | 65.1% | Pi 34.6%、Hermes 13.9% |
| Terminal Bench 2.1 | 純本地 59.6%（近乎零邊際成本）；升級雲端顧問後 73.0%，約每次 rollout 0.415 美元 | Claude Opus 5 單獨執行 82.4%，約 0.65 美元 |

Terminal Bench 2.1 的結果最能說明混合架構的定位：升級到雲端顧問能明顯拉近與前沿模型的差距，但沒有完全補平，同時成本只有純雲端方案的約六成。

⚠️ **硬體門檻不低，平臺支援也有限**

DGX Spark 安裝需要 GB10 superchip、128GB 記憶體、至少 1TB 儲存空間；Qwen 3.8 27B orchestrator 以 3-bit 量化出貨，下載檔案 17.4GB，需要 32GB RAM，Nemotron 3.5 Lightning 則是 4-bit、19GB，需要 36GB RAM。其他系統需要 DGX OS 或 ARM/x64 上的 Ubuntu，搭配至少 24GB VRAM 的 RTX GPU。目前僅支援單臺 DGX Spark，多機叢集仍在路線圖上未出貨。可用性方面，Linux 版優先開放給 Pro、Max、Enterprise Pro 與 Enterprise Max 訂閱者，Windows 預計 9 月跟進，macOS 未列入路線圖。

🎯 **實務啟示**

對於需要大量重複性 agent 任務（例如跨 repo 遷移或長時間驗證迴圈）的團隊，「本地任務零邊際 token 成本」是這個方案最直接的經濟誘因；但由於仍需高規格硬體與 Linux 環境，短期內更適合已有 DGX 系列設備、且對資料落地有要求的團隊先行評估，而非泛用個人電腦的替代方案。

🔗 **來源**
- 標題：Perplexity Ships Portable Computer on NVIDIA DGX Spark: Local Harness, OS-Enforced Sandbox, and Zero Per-Token Cost for Local Steps
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/08/25/perplexity-ships-portable-computer-on-nvidia-dgx-spark-local-harness-os-enforced-sandbox-and-zero-per-token-cost-for-local-steps/

#Perplexity #NVIDIA #DGXSpark #LocalAI #AgenticAI #Qwen #EdgeInference #AISandbox #LLM #OnDeviceAI
