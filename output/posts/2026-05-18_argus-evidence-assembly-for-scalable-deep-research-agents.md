---
title: "Argus: Evidence Assembly for Scalable Deep Research Agents"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.16217
score: 102
model: tencent/hy3-preview:free
generated_at: 2026-05-18T20:36:10.669431
---

📌 【MiroMind 最新研究】Argus：讓 Deep Research Agent 拼湊證據而非暴力搜尋  

你以為讓 AI 同時開 64 條搜尋線程就能把答案寫出來？實際上，重複的證據不只浪費運算，還會把模型的上下文推向極限，導致報酬遞減。  

🤔 **Deep Research 仍停留在「單一軌跡」的暴力搜尋**  
現有的長 ReAct rollout 雖能探索複雜資訊，但一次只走一條路徑；而最近的 SOTA 系統透過平行搜尋與聚合來擴大推理時間計算。這種做法往往產出重複的證據片段，無法真正互補，隨著平行數增加，聚合內容會快速接近模型的 token 上限，進而降低效益。  

🧪 **Searcher‑Navigator 協作架構：把研究視為拼圖**  
論文提出 Argus，由兩個角色共同完成深度研究：  
- **Searcher**：採用傳統 ReAct 風格，針對特定子查詢蒐集證據軌跡。  
- **Navigator**：維護一個共享的證據圖（evidence graph），負責檢查哪些片段仍缺失、派遣 Searcher 去補充，並在圖完成後進行推理，給出帶有來源追溯的最終答案。  

Navigator 透過強化學習訓練，學會「驗證、派遣、合成」三項能力；Searcher 則獨立訓練，保持標準 ReAct 行為。這種設計讓 Navigator 無需重新訓練，即可支援單個 Searcher 或多個（平行）Searcher 的推論。  

📊 **單機與平行皆有顯著提升，上下文佔用仍受控**  
- 在單一 Searcher 情境下，Argus 在八個基準測試上的平均得分比基線高 **5.5 分**。  
- 使用 **8 個平行 Searcher** 時，平均提升達 **12.7 分**。  
- 擴大至 **64 個 Searcher** 在 BrowseComp 基準上達到 **86.2 分**，超越所有已評測的專有代理。  
- 此時 Navigator 的推理內容長度維持在 **21.5K token 以下**，未觸及模型上限。  

💡 **關鍵在於「互補證據」而非「重複搜尋」**  
實驗顯示，當平行搜尋產生大量重複片段時，聚合階段會佔用大量 token，導致邊際報酬下降。Argus 透過 Navigator 主動追蹤哪些證據仍缺失，引導 Searcher 去填補空白，使得每條新軌跡都帶來新資訊。這種「拼圖」思維不只減少運算浪費，也讓最終答案的來源追溯更清晰。  

⚠️ **研究限制：依賴 RL 訓練與 MoE 骨幹**  
- 本方法假設能夠進行強化學習訓練 Navigator，這對缺乏 RL 基礎設施的團隊可能是門檻。  
- 報告的實驗皆基於 35B‑A3B MoE 主幹模型，若換成密集或較小的架構，效能是否保持尚未驗證。  
- 目前僅報告了八個基準（包含 BrowseComp）的平均提升，未列出每個基準的具體分數，難以判斷在某些任務上的表現差異。  

🎯 **實務啟示：設計研究代理時優先考慮證據圖與任務分派**  
- 若目標是建立可擴展的 deep research 系統，可參考 Searcher‑Navigator 的職責劃分：讓檢索模組專注於收證，讓規劃模組負責證據的缺口偵測與合成。  
- 在資源允許的情況下，適度增加平行 Searcher 數量可帶來線性提升，但需監控聚合階段的 token 使用量，避免超出模型上限。  
- 對於無法進行大規模 RL 訓練的團隊，先以監督學習預訓練 Navigator 的基本驗證與派遣規則，再以少量強化學習微調，或許也是可行的折衷方案。  

🔗 **論文連結**  
📝 Argus: Evidence Assembly for Scalable Deep Research Agents  
👤 Zhen Zhang, Liangcai Su, Zhuo Chen, Xiang Lin, Haotian Xu @ MiroMind AI  
🔗 https://arxiv.org/abs/2605.16217  

你在構建 AI 研究代理時，是否也曾遇到「越搜尋越重複」的瓶頸？歡迎在留言區分享你的經驗或想法 👇  

#AI #DeepResearch #AgenticSystems #MiroMind #Argus #LLM #研究方法 #機器學習
