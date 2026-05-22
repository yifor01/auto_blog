---
title: "google-research/timesfm"
source: GitHub Trending
url: https://github.com/google-research/timesfm
score: 127
model: tencent/hy3-preview:free
generated_at: 2026-05-22T20:18:48.219465
---

📌 **TimesFM 2.5：輕量長上下文時間序列模型**

你是否曾為了預測銷售、氣象或股票而為模型參數爆炸頭疼？TimesFM 2.5 卻用只有 200M 參數就支援 16K 長上下文。  
這意味著在不犧牲精度的情況下，你可以看更遠的歷史，同時仍能透過 Google 產品直接呼叫。

🤔 **時間序列預測亟需更實用的基礎模型**  
傳統預測模型往往需要針對每個領域重新訓練，且隨著歷史長度增加，計算成本呈指數級增長。Google Research 觀察到，產業界對於「可直接插入既有工作流程」的預測工具需求日益增長，尤其在需要長時序依賴與快速迭代的場景中。

🧪 **從 500M 參數的 decoder‑only 架構演進至 200M、16K 上下文的 TimesFM 2.5**  
TimesFM 採用 decoder‑only Transformer 作為基礎架構，先前版本在 ICML 2024 中發表。最新更新將參數數量從 500M 壓縮至 200M，同時將可處理的上下文長度從 2048 提升至 16K，並新增支援最高 1000 步的連續分位數預測（可選）。所有檢查點已在 Hugging Face 上公開，並提供 pip 安裝方式（例如 `pip install timesfm==1.3.0` 以載入舊版）。

🚀 **更輕量、更長上下文、更靈活的預測能力**  
參數減少不代表能力下降；相反，更小的模型在相同硬體上能跑更長的序列，減少記憶體瓶頸。延長的上下文使模型能捕捉到更遠的週期性或趨勢資訊，而新增的分位數預測則提供了不確定性量化，對風險管理尤為重要。此外，該版本透過 XReg 重新引入共變量支援，使外部特徵（如假日、促銷）能納入預測流程。

💡 **LoRA 微調、Agent 整合與社群貢獻提升實用性**  
2026 年 4 月的更新加入了使用 HuggingFace Transformers + PEFT（LoRA）的微調範例，使使用者能在小量領域資料上快速適應模型，而無需完整重訓。3 月的更新則由社群成員 @borealBytes 貢獻了 Agent 支援，並隨附 TimesFM SKILL.md 說明如何在自動化工作流程中呼叫模型。同時新增了單元測試與多項社群修正，提升了程式碼的穩定性與可維護性。

⚠️ **開放版本非官方產品，且仍需領域知識進行微調**  
儘管 TimesFM 已被整合至 BigQuery ML、Google Sheets 與 Vertex Model Garden，但 GitHub 上的此版本僅為開放原始碼，未獲 Google 官方正式支援。模型雖提供強大的預測基礎，但在特定產業或極端長序任務上，仍建議根據領域資料進行 LoRA 微調以獲得最佳結果。

🎯 **將 TimesFM 2.5 納入您的預測管線，先從 LoRA 微調與 Agent 呼叫開始**  
- 在 Google Sheets 或 BigQuery ML 中直接呼叫模型進行快速原型預測。  
- 利用提供的 LoRA 範例，用少量歷史資料微調模型以適應您的產業特性。  
- 若需自動化決策，參考 Agent 支援文件將模型封裝為可調用的服務。  
這樣既能享受基礎模型的廣泛知識，又能透過輕量微調貼近實際場景。

🔗 **論文與資源連結**  
📝 A decoder-only foundation model for time-series forecasting , ICML 2024  
👤 Google Research  
🔗 模型檢查點：https://huggingface.co/google/timesfm  
🔗 GitHub 專案：https://github.com/google-research/timesfm  
🔗 Google Research 部落格：https://research.google/blog/timesfm/  

你已經在專案中嘗試過 TimesFM 2.5 了嗎？歡迎在留言區分享你的使用經驗或遇到的挑戰 👇

#GoogleResearch #TimesFM #TimeSeriesForecasting #LoRA #AgentAI #BigQueryML #GoogleSheets #VertexModelGarden #機器學習 #資料科學
