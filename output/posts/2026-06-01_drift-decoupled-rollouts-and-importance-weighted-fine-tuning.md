---
title: "DRIFT: Decoupled Rollouts and Importance-Weighted Fine-Tuning for Efficient Multi-Turn Optimization"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.31455
score: 94
model: tencent/hy3-preview:free
generated_at: 2026-06-01T22:15:09.005806
---

📌 **【HuggingFace Daily Papers】DRIFT：透過解耦 Rollout 與重要性加權微調，達成近似 RL 的多輪對話學習效率**

你是否曾經為了讓聊天模型在多輪對話中表現更好，而不得不投入大量的在線強化學習（RL）資源？當每一次互動都需要模型與環境即時交互時，計算成本會快速爆炸，尤其在大型語言模型上更是難以承受。

🤔 **多輪互動學習的成本瓶頂**  
傳統的 RLHF 或直接強化學習需要模型在線上與使用者或模擬環境進行大量回合（rollout）才能學習到理想的行為。這樣的過程不只耗費大量 GPU 小時，還難以在實務管線中快速迭代。因此，尋找能夠利用已有離線數據，同時保有 RL 級別學習效果的方法成為當務之急。

🧪 **解耦 Rollout + 重要性加權的監督微調**  
DRIFT 框架的核心是兩個設計：  
1. **解耦 Rollout**：先利用已有的離線軌跡（例如人類示範或之前的模型產生的對話）作為學習基礎，避免每次訓練都需要重新產生線上互動。  
2. **重要性加權監督微調（Importance‑Weighted SFT）**：在使用這些離線軌跡進行監督學習時，根據軌跡與目標策略之間的分布差異計算重要性權重，以修正離線數據所帶來的偏差，使微調過程更接近真實的強化學習目標。

透過這兩個步驟，DRIFT 能在不額外進行線上 Rollout 的情況下，利用既有數據完成多輪互動的策略優化。

📊 **近似 RL 的表現，但計算開銷大幅降低**  
根據論文的說明，DRIFT 在多輪互動基準上達到與傳統強化學習相近的性能，而所需的計算資源僅為傳統 RL 的一小部分。這意味著在相同的硬體預算下，可以進行更多次的實驗或針對更大規模的模型進行微調。

💡 **為何這對工程師而言是個好消息？**  
- **對 RLHF 管線的補充**：若你正在透過人類回饋進行強化學習，DRIFT 提供了一種可先利用已有對話數據進行預訓練的途徑，後續再以少量線上互動微調，可顯著降低實驗循環時間。  
- **適用於 Agentic 系統**：多輪決策與環境互動是 Agent 的核心需求，能夠在離線階段就獲得較好的策略，有助於減少線上探索風險。  
- **微調效率提升**：重要性加權的監督微調相較於純粹的 behavioural cloning，能更好地對齊目標分布，從而在少量計算下獲得更佳的對話品質。

⚠️ **方法的效能依賴離線軌跡的品質與覆蓋度**  
由於 DRIFT 的學習基礎是離線數據，若這些軌跡無法充分覆蓋目標任務的狀態空間，或存在系統性偏差，則重要性加權可能無法完全修正所帶來的誤差。因此，在實際應用時仍需評估並可能補充高品質的對話軌跡，或搭配少量線上 Rollout 以提升穩健性。

🎯 **實務建議：先跑離線預訓練，再以少量線上互動微調**  
若你的團隊正在尋找降低 RL 成本的做法，可考慮先使用 DRIFT 的流程：  
1. 收集或重現高品質的多輪對話軌跡（可來自人類示範、過去模型產出或合成數據）。  
2. 以重要性加權的監督微調在這些軌跡上進行初步優化。  
3. 最後僅用少量線上互動（例如少量的人類回饋或模擬環境）進行最終微調，以對齊真實目標。  
這樣的「離線先行、線上補充」策略，既能保留 RL 的學習優勢，又能大幅節省計算資源。

🔗 **論文連結**  
📝 DRIFT: Decoupled Rollouts and Importance-Weighted Fine-Tuning for Efficient Multi-Turn Optimization  
👤 作者：未在提供的資訊中列出  
🔗 https://huggingface.co/papers/2605.31455  

你在多輪對話模型的訓練中，是否也曾受到線上 RL 高成本的限制？歡迎在留言區分享你的看法或實驗經驗 👇

#AI #ReinforcementLearning #RLHF #MultiTurn #FineTuning #HuggingFace #DRIFT #AgenticSystems #MachineLearning
