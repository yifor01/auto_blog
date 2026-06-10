---
title: "Decocted Experience Improves Test-Time Inference in LLM Agents"
source: ChatPaper/AI
url: https://arxiv.org/abs/2604.04373
score: 124
model: gpt-4o-free
generated_at: 2026-04-07T13:12:01.942872
---

📌 【MIT/Stanford 最新研究】用「精煉經驗」突破 LLM 推論瓶頸

你以為狂加推論算力就能讓 AI Agent 變聰明？MIT 與 Stanford 最新研究指出，盲目擴展運算資源只會導致預算浪費與次優探索。真正決定表現的關鍵，其實藏在「如何整理過去的經驗」。展開了解如何用更少的算力，換取更強的推論能力。

🤔 **算力堆疊遭遇邊際效益遞減，上下文構建成為新維度**

近年來，不更新模型權重而專注於「測試時擴展 (Test-Time Scaling)」已成為提升 LLM 效能的主流方向。透過增加推論階段的運算預算（例如拉長思考鏈、擴大採樣或執行搜尋演算法），模型在數學與程式任務上的表現確實顯著提升。然而，面對複雜的推理與代理 (Agentic) 任務時，單純堆疊算力不僅成本高昂，更容易將預算浪費在無效的探索路徑上。本研究提出一個關鍵觀點：除了算力 (Compute)，「上下文 (Context)」應被視為另一個可系統性擴展的維度。如何將過去的互動軌跡轉化為高品質的輸入提示，成為突破效能瓶頸的核心。

🧪 **橫跨數學推理、網頁瀏覽與軟體工程的系統性驗證**

研究團隊並未侷限於單一任務類型，而是將驗證場景擴展至三類高複雜度領域：數學推理、網頁瀏覽 (Web Browsing) 與軟體工程任務。實驗設計聚焦於 Agent 在測試階段的行為軌跡，系統性比較不同上下文構建策略對推論表現的影響。研究不僅觀察效能隨經驗累積的縮放曲線，更深入剖析哪些特徵能定義「高品質上下文」，以及何種資料結構最適合支援經驗的儲存與檢索。

 **「精煉經驗」有效突破推論成本與效能的權衡**

研究明確指出，有效的上下文構建高度依賴「精煉經驗 (Decocted Experience)」。直接將原始互動紀錄或完整軌跡塞入 Prompt 會造成訊號雜訊比過低，反而干擾模型判斷。透過將經驗提煉為結構化知識，Agent 能在相同甚至更低的推論預算下，達成更精準的決策路徑。這證明測試時效能的提升，並非只能靠暴力增加 Token 運算，而是可以透過優化輸入資訊的「資訊密度」來實現。

💡 **萃取精華、結構化組織與關鍵資訊檢索的閉環機制**

「精煉經驗」的運作機制可拆解為三個關鍵環節：
1. **萃取本質 (Extracting Essence)**：從冗長的執行軌跡中過濾無效嘗試，保留對解決問題具決定性的步驟與決策邏輯。
2. **結構化組織 (Organizing Coherently)**：將離散的經驗片段轉為具有語意關聯的知識單元，避免碎片化資訊造成語境斷裂。
3. **顯著性檢索 (Retrieving Salient Information)**：依據當前任務特徵，動態召回最相關的經驗片段組合成 Prompt 上下文。

這套機制顯示，高品質的 Agent 記憶系統不應只是日誌紀錄 (Log)，而必須具備動態壓縮、關聯重建與情境感知檢索的能力。資料結構的選擇（如圖結構、索引樹或向量分層）直接決定了經驗能否被高效轉化為推論優勢。

⚠️ **聚焦上下文設計，動態環境適應性與量化細節待考**

本研究主要驗證「精煉經驗」作為上下文構建機制的概念有效性與設計原則。實驗設定偏向可控的任務環境，對於高度動態、即時反饋多變的開放世界場景，經驗萃取的即時性與結構化成本仍需進一步評估。此外，公開摘要未詳述具體的基準模型、量化增益數據與底層資料結構的實作細節，後續開源或技術報告發布後，將有待工程社群進一步進行基準測試 (Benchmark) 驗證。

🎯 **Agent 開發應從「暴力搜尋」轉向「經驗記憶庫優化」**

對實務開發者而言，這項研究提供明確的架構優化方向：
- 重新評估推論預算分配策略，減少對單純增加採樣數或搜尋深度的依賴。
- 在 Agent 架構中引入經驗壓縮層，將成功與失敗的軌跡轉化為可檢索的結構化知識。
- 優化 Prompt Context 的組裝邏輯，確保注入的經驗具備高語意密度與任務相關性。

與其讓模型在推論時重新摸索，不如讓它在執行前就能「站在過去的自己肩膀上」。這正是高效能 Agent 架構演進的必經之路。

🔗 **論文連結**
📝 Decocted Experience Improves Test-Time Inference in LLM Agents
👤 Maohao Shen, Kaiwen Zha, Zexue He, Zhang-Wei Hong, Siru Ouyang
🏛️ Massachusetts Institute of Technology; Stanford University; MIT-IBM Watson AI Lab; University of Illinois at Urbana-Champaign; University of California, Los Angeles
🔗 論文：https://arxiv.org/abs/2604.04373

你的 Agent 目前如何管理歷史經驗？是原始 Log 堆疊，還是已有結構化記憶設計？歡迎在留言區交流架構設計心得 👇

#LLM #TestTimeScaling #AIAgents #MachineLearning #MIT #Stanford #PromptEngineering #系統架構 #推論優化
