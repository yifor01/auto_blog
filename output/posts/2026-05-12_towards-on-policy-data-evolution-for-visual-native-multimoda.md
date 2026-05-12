---
title: "Towards On-Policy Data Evolution for Visual-Native Multimodal Deep Search Agents"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.10832
score: 119
model: tencent/hy3-preview:free
generated_at: 2026-05-12T20:27:16.067717
---

📌 On‑Policy Data Evolution 強化多模態深搜  

你以為多模態 AI 已經能夠『看』並『搜尋』解決開放式問題？最新研究顯示，現有系統在視覺證據重複利用與訓練數據自我進化上仍有明顯瓶頸。  

🤔 **視覺證據難以重複使用，訓練數據難以隨代理進化**  
現有的多模態深度搜尋代理在使用搜尋、瀏覽或轉換工具時，會把回傳的影像視為暫時性輸出，後續工具無法再次引用這些中間視覺證據。同時，訓練資料多半是靠固定的製備流程產出，無法追蹤代理能力隨訓練而變化的需求。  

🧪 **圖像銀行協議與 On‑policy Data Evolution 閉環**  
研究首先提出一種以「圖像銀行」為核心的視覺原生代理 harness：每一次工具回傳的影像都會被註冊為可定址的參考，使得中間視覺證據能被後續工具重新消費。在此 harness 上，團隊設計了 On‑policy Data Evolution (ODE)：一個閉環的資料產生器，會根據目前策略的 rollout 結果在每一輪自我精煉，使得該輪的訓練資料正好對應該策略仍需學習的內容。同一框架既能產出多樣化的監督微調資料，也能產出政策導向的強化學習資料，覆蓋代理訓練的完整生命週期。  

🔟 **ODE 讓 Qwen3-VL-8B 在 8 個多模態深度搜尋基準上平均提升 14.1%，超越 Gemini‑2.5 Pro**  
在 8 個多模態深度搜尋基準上，ODE 讓 Qwen3-VL-8B 的平均分數從 24.9% 提升至 39.0%。在 30B 規模下，平均分數從 30.6% 提升至 41.5%。這些提升幅度均超過了在標準代理工作流程中的 Gemini‑2.5 Pro 基準分數（37.9%），表明該方法在相同設定下能取得更佳表現。  

💡 **圖像銀行重複使用與回饋驅動的演化讓視覺證據可被後續工具重新消費，並產生更貼合策略的訓練數據**  
進一步分析顯示，圖像銀行的可重複使用機制特別有利於需要反覆視覺精煉的複雜任務。而 ODE 的回饋導向演化產出的監督微調追蹤更具基礎性，強化學習任務也更能匹配當前策略，從而提升學習效率。  

⚠️ **僅報告平均提升，未詳述具個別基準表現或長效穩定性**  
論文著重於各基準的平均改善，未提供每個基準的詳細分數或隨訓練輪數的長期穩定性分析，這些細節仍需後續工作補充。  

🎯 **實務啟示：工程師可直接採用圖像銀行協議與 ODE 框架進行視覺原生代理的訓練，實現數據隨策略自我精煉**  
對於希望建立能夠反覆利用中間視覺證據、並讓訓練資料自動貼合代理能力的多模態深度搜尋系統，研究提供了可直接實作的 harness 與閉環資料生成流程。團隊已將相關程式碼與 harness 開源，供社群實驗與擴充。  

🔗 **論文連結**  
📝 Towards On-Policy Data Evolution for Visual-Native Multimodal Deep Search Agents  
👤 Shijue Huang, Hangyu Guo, Chenxin Li, Junting Lu, Xinyu Geng (HKUST, CUHK, Peking University, Tsinghua University, University of Edinburgh)  
🔗 https://arxiv.org/abs/2605.10832  

你是否已在專案中嘗試過類似的「圖像銀行」或「On‑policy 資料演化」機制？歡迎在留言區分享你的經驗與疑問 👇  

#AI #Multimodal #VisualReasoning #AgentWorkflow #ODE #HKUST #CUHK #PaperSharing
