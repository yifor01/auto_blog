---
title: "HARNESS-LM: A Three-Phase Training Recipe for Harnessing SLMs in Sponsored Search Retrieval"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.23572
score: 118
model: tencent/hy3-preview:free
generated_at: 2026-05-25T20:33:40.199763
---

📌 微軟三階段壓縮搜尋模型  

你以得更大的模型一定代表更好的搜尋？微軟證明，只要用對方法，小模型也能贏過大模型，而且快 27 倍。  

🤔 **贏得精準度卻犧牲速度，大模型在實際廣告檢索中難以落地**  
贊助搜尋需要同時兼顧召回品質與線上延遲。億參數級的 Small Language Model (SLM) 檢索器在公共基準上表現優異，但因計算成本高、響應慢，難以直接部署在高吞吐、低延遲的廣告系統中。  

🧪 **三階段訓練食譜：從十億參數教師到次六億參數學生**  
HARNESS-LM (HLM) 包含三個步驟：  
1. 以十億參數級 SLM (如 Qwen3-Embedding-4B/8B) 微調出高效能的「教師」檢索器；  
2. 以 L2 對齊目標將教師的查詢向量蒸餾到參數量低於 600M 的學生編碼器；  
3. 最後以對比學習細練，進一步提升學生的檢索表現。  
作者同時進行了實驗研究，比較了不同對齊目標、嵌入維度、模型規模、架構與優化策略，以尋找在生產環境中最有效的組合。  

 **在真實 Bing Ads 基準上恢復超過 98% 精準度，同時降低延遲 27 倍**  
在真實的 Bing Ads 評估基準上，HLM 學生模型復原了教師檢索器超過 98% 的精準度（Precision）。線上測量顯示，查詢編碼器延遲降低了最高 27×，吞吐量提升了約 20×（在 NVIDIA A100 GPU 上）。線上 A/B 測試進一步顯示，相較於目前在產線運行的檢索器集合，使用已部署的 1.9億參數 HLM 模型帶來 +1% 收入、+0.6% 展示、+0.4% 點擊的提升。  

💡 **L2 對齊 + 對比細練，是穩傳遞知識的關鍵**  
消融研究表明，僅用 L2 對齊已能將教師的表示空間有效傳遞給學生；而在此基礎上加入對比細練階段，能進一步彌補因模型尺寸縮小而導致的檢索落差，使得精準度損失降到可忽略不計的程度。這說明知識蒸餾不只是單純的表示匹配，後續的任務導向細練對保留檢索能力至關重要。  

⚠️ **僅在 Bing Ads 環境驗證，其他領域效能尚未探討**  
本研究的實驗與線上測試均基於真實的 Bing Ads 流量。雖然結果顯示顯著的效能與商業提升，但未在其他搜尋或推薦場域進行驗證，因此無法直接保證相同的壓縮比例與提升在所有 SLM 型檢索器上成立。  

🎯 **適合低延遲檢索系統，可直接採用三階段蒸餾流程**  
對於需要在毫秒級響應時間內服務大量查詢的廣告、電商或企業搜尋系統，HLM 提供了一個可落地的食譜：先訓練高效能教師，再以 L2 對齊蒸餾至目標規模，最後以對比學習微調。此流程不依賴全新的架構創新，而是將已知的蒸餾技術組織化，使工程團隊能在現有基礎設施上快速獲得精準度與效率的雙重提升。  

🔗 **論文連結**  
📝 HARNESS-LM: A Three-Phase Training Recipe for Harnessing SLMs in Sponsored Search Retrieval  
👤 Vipul Gupta, Shikhar Mohan, Lakshya Kumar, Pranjal Chitale, Nikit Begwani @ Microsoft AI  
🔗 https://arxiv.org/abs/2605.23572  

#MicrosoftAI #SponsoredSearch #Retrieval #ModelDistillation #SLM #LowLatency #BingAds #MachineLearning #InformationRetrieval #AIEngineering
