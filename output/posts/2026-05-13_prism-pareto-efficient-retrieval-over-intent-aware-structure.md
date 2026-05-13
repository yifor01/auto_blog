---
title: "PRISM: Pareto-Efficient Retrieval over Intent-Aware Structured Memory for Long-Horizon Agents"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.12260
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-13T20:41:51.215149
---

📌 **PRISM：長程AI代理的記憶檢索新方案**  

你以為把記憶窗口調大就能讓AI回答更準？其實單純加長上下文不只浪費 token，還可能把有用訊息埋在噪聲裡。  

🤔 **長程記憶的兩難：準確度 vs. 成本**  
長時間對話的語言代理會產生遠超固定 context window 的對話史。現有做法要麼直接擴大窗口（導致推理成本爆炸），要麼在 ingest 階段做大規模事實抽取（耗費大量 token），或是啟發式圖遍歷（準確度與效率都難以兼顧）。如何在嚴格的 token 預算內，仍能找到最關鍵的證據，成為代理記憶管理的核心痛點。  

🧪 **訓練免費的圖結構檢索框架**  
PRISM 將長程記憶建構為一個帶類型關係的圖，並提出四個互補的推理時元件：  
1. **Hierarchical Bundle Search** – 在類型化路徑模板上進行層次式束搜尋，快速縮小候選範圍。  
2. **Query‑Sensitive Edge Costing** – 根據偵測到的查詢意圖動態調整邊權重，使遍歷更貼合任務需求。  
3. **Evidence Compression** – 把候選束壓縮成緊湊的答案側上下文，直接喂給 LLM。  
4. **Adaptive Intent Routing** – 大部分查詢走零‑LLM 層（僅靠圖結構與規則），只有真正需要深度理解時才呼叫 LLM。  

透過將檢索建模為「typed path template 上的最小成本選擇」，並搭配 LLM 端的壓縮步驟，PRISM 能在不修改上游 ingest pipeline、也不需任何微調的情況下，於嚴格的 context 預算內挑出最相關的證據。  

🚀 **LoCoMo 基準測試：同協議下準確度顯著提升，token 成本僅為 baseline 的十分之一**  
- 在 LoCoMo 基準上，PRISM 取得的 LLM‑judge 準確度顯著高於所有同協議 baseline。  
- 同時，所需的 context budget 僅為 baseline 的約 10%（即一個數量級的減少）。  
- 這使得 PRISM 在「準確度‑context‑成本」的 Pareto 前緣上佔據了先前空白的角落，證明了在不犧牲服務成本的前提下提升答案品質的可行性。  

💡 **關鍵洞察：意圖導向的邊權重與自適應路由是效率的引擎**  
實驗顯示，Query‑Sensitive Edge Costing 能讓搜尋更快聚焦於與使用者意圖相關的子圖；Adaptive Intent Routing 則將約 80% 的查詢導向零‑LLM 層，大幅降低 LLM 呼叫頻率。Evidence Compression 則確保即使在極小的 token 預算內，也能保留足夠的語義資訊供 LLM 進行最終推論。這四個元件的正交組合，才讓 PRISM 能在同等或更低的成本下實現更高的準確度。  

⚠️ **研究限制：目前僅在單一基準上驗證，圖品質與更新頻率未深入探討**  
- 實驗僅限於 LoCoMo 基準，尚未在其他長程代理任務（如多步驟規劃、跨檔案對話）上進行廣泛驗證。  
- PRISM 的效能依賴於所建構的圖結構的完整性與正確性；若 ingest 階段的關係抽取噪聲較大，可能影響檢索品質。  
- 雖然宣稱訓練免費，但仍需在部署時維護圖的增量更新機制，此部份在論文中未給出具體實作細節。  

🎯 **對工程師的實務建議：可直接插入現有 pipeline，顯著降低 serving 成本**  
- 無需重新訓練或修改現有的資料 ingest 流程，只要將記憶存成帶類型關係的圖，即可啟用 PRISM 的四個元件。  
- 對於成本敏感的線上代理服務（如客服、協助程式設計等），可先啟用 Adaptive Intent Routing，讓大部分簡單查詢走零‑LLM 路徑，只在必要時呼叫 LLM 進行最終生成。  
- 若進一步提升準確度，可調整 Evidence Compression 的壓縮率或微調 Query‑Sensitive Edge Costing 的權重參數，以在特定應用場景中尋找更佳的準確度‑成本平衡點。  

🔗 **論文連結**  
📝 PRISM: Pareto-Efficient Retrieval over Intent-Aware Structured Memory for Long-Horizon Agents  
👤 Jingyi Peng, Zhongwei Wan, Weiting Liu, Qiuzhuang Sun (Singapore Management University; The Ohio State University; Fudan University)  
🔗 https://arxiv.org/abs/2605.12260  

你的長程代理目前是怎麼管理記憶的？是否曾為過大的 context window 頭疼？歡迎在留言區分享你的經驗與想法 👇  

#AI #LLM #Agent #MemoryManagement #Retrieval #PRISM #LoCoMo #NLP #MachineLearning #服務成本 #圖檢索
