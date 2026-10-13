---
title: How Flo Health built safer, more useful open models with Databricks AI Runtime
source: Databricks
url: https://www.databricks.com/blog/how-flo-health-built-safer-more-useful-open-models-databricks-ai-runtime
model: claude-code/sonnet
generated_at: '2026-10-12T23:56:03.298722'
score: 87
---

📌 Flo Health 如何用 AI 評審把醫學安全訓練進模型權重

TL;DR：女性健康 App Flo 用 AI 評審取代人工標註，微調後綜合達標率從 16% 升到 47%。

當一款月活躍用戶達 8,100 萬的健康 App 決定導入生成式 AI，容錯空間幾乎是零，回答既要醫學上安全，又不能只會說「請去看醫生」這種安全但沒用的廢話。Flo Health 選擇的解法，是自己動手把「什麼叫做好答案」變成可訓練的訊號。

🤔 問題：安全與有用，常常互相拖累
Flo 從傳統 ML 走向生成式 AI 驅動的個人化洞察時，發現單靠通用大模型 API 會帶來成本、供應商生命週期依賴，以及難以把 Flo 自身領域知識編碼進模型等限制。團隊設定了兩個目標：醫學安全是基礎，有用性是目標。以「我的月經為什麼遲來？」這個問題為例，只回「請洽詢醫療專業人員」算安全但不太有用；只列出常見生活作息原因則比較有幫助，但從醫學安全角度來看並不完整。Flo 想要的答案，要同時兼顧實用資訊、適當情境與對的安全網。

🧩 方法：用 AI 評審把醫學風險拆成可測試的規則
Flo 的醫療、產品與工程團隊把醫學風險拆解成具體、可一致測試的規則（rubric）。舉例來說，團隊發現針對症狀類問題的回答容易「過度安心」，於是訂出「balanced causes」規則，要求回答在相關情況下必須同時涵蓋良性與可能嚴重的病因。這些規則接著被轉成一個個 AI judge，每個 judge 都有明確定義、評分指引與訓練案例，並用合成案例與匿名化的真實用戶實驗案例進行驗證；當 AI judge 的判斷與人工初評不一致時，由盲測的臨床審查員仲裁，建立 ground truth。最終框架包含 26 個 judge，分成三大類別。

有了這套評估系統，Flo 接著把同一批 judge 當作訓練時的 reward 訊號，採用 Reinforcement Fine-Tuning 做法：訓練過程中產生多個候選回答，用評估系統挑出最強的，再微調模型，把品質直接編碼進權重，而不是每次推論都靠昂貴的 best-of-N 搜尋。整個流程產生了超過 15,000 題合成問題，並以隱私優先的原則建構訓練配對：輸入來自模型生成或匿名彙總的訊號，而非用戶自己寫的自由文字或可識別資訊，因此臨床專家只需要負責定義與驗證「安全」的標準，不必逐筆人工標註訓練資料。

💡 踩過的坑：安全分數一度卡住不動
第一版做法暴露了一個問題：有用性有進步，但醫學安全幾乎沒動，原因是偏好配對（preference pair）沒有充分區分出醫學品質的程度差異。Flo 的解法是加入分級的安全分數：先通過二元安全門檻的回答，再依符合醫學準則的完整程度重新排序，讓偏好配對呈現更清楚的醫學安全對比。

整個 generate-score-select-train 迴圈相當吃運算資源。Flo 的訓練堆疊結合了 Databricks AI Runtime、LLM Foundry 與 Compose-RL，並用 MLflow 做追蹤與 checkpoint 管理：AI Runtime 提供 serverless GPU 環境，LLM Foundry 負責分散式訓練，Compose-RL 提供偏好最佳化層。實際微調時用了 32 張 NVIDIA H100 GPU，搭配 PyTorch 與 Fully Sharded Data Parallel（FSDP），先跑 SFT 再接 DPO。

📊 數據：綜合達標率三倍成長

| 指標 | 微調前 | 微調後 |
|---|---|---|
| 醫學安全 | 34% | 約 61% |
| 有用性 | 42% | 76% |
| 兩者同時達標 | 16% | 47% |

⚠️ 限制與留意的前提
文中提到「用微調模型取代前沿模型 API 可將推論成本降低一個數量級」是 Flo 團隊自己的估計，並非獨立驗證數據。第一版方法在安全與有用性之間失衡的經驗也說明：單純堆資料量不保證兩個目標同步進步，評估框架的設計（例如分級安全分數）往往才是關鍵。

🎯 實務啟示
Flo 最終留下來的資產，與其說是那個 47% 的分數，更是一套可重複使用的評估與訓練系統——團隊已計畫把同一套醫學安全與有用性準則，套用到 Gemma、Qwen、Kimi 等更新的開放權重模型上。對於同樣需要把「領域專家標準」轉成訓練訊號的團隊，Flo 的路徑（rubric → AI judge → 合成資料 → RFT/DPO）是個值得參考的樣板。

🔗 來源
- 標題：How Flo Health built safer, more useful open models with Databricks AI Runtime
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/how-flo-health-built-safer-more-useful-open-models-databricks-ai-runtime

#FloHealth #Databricks #FineTuning #AIAlignment #HealthTech #ReinforcementLearning #DPO #OpenModels #ResponsibleAI #MachineLearning
