---
title: "When Planning Fails Despite Correct Execution: On Epistemic Calibration for LLM-Based Multi-Agent Systems"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.23414
score: 97
model: tencent/hy3-preview:free
generated_at: 2026-05-25T21:05:34.620252
---

📌 **當執行正確卻仍失敗：LLM 多代理規劃的認知校準**  

你以為 AI 代理只要把計畫執行得沒錯，任務就一定會成功？最新研究指出，即使每一步都正確執行，系統仍可能因「不知道自己不知道」而失敗。  

🤔 **認知誤判讓完美計畫變成失敗**  
論文提出一種隱蔽失誤——** epistemic miscalibration in planning**。代理在評估計畫可行性時，可能錯誤地過高或過低估計自己的知識。這種誤判在規劃階段是潛在的：生成的計畫看起來自洽且可執行，沒有可觀察的執行錯誤；但隨著新資訊的出現，過去的誤判可能被掩蓋，甚至隨時間重複發生。  

🧪 **EPC‑AW：透過資訊一致性偵測與校準**  
為應對此問題，作者設計了 **Epistemic Planning Calibration Agentic Workflow (EPC‑AW)**。其核心包含兩個機制：  
1. **Information‑consistency‑based Plan Selection**：選擇在不同代理、不同資訊條件下評估結果穩定的計畫。  
2. **Consistency‑guided Epistemic State Refinement**：利用過去評估的不一致來隨時間調整代理的認知狀態，使後續規劃更具校準性。  

實驗顯示，採用 EPC‑AW 能將系統層級的成功率平均提升 **9.75%**。  

💡 **為什麼資訊一致性能揭示認知誤判？**  
當代理對自身知識的判斷不準時，同一個計畫在不同代理或資訊情境下的可行性評估會出現波動。EPC‑AW 透過檢測這種不穩捕捉到潛在的 epistemic miscalibration，並藉由過去的偏差來校準未來的知識狀態，從而減少因認知錯誤導致的規劃失誤。  

⚠️ **研究範圍與待驗證點**  
- 本研究聚焦於規劃階段的認知校準，未直接處理執行錯誤或其他類型的失誤。  
- 所報告的成功率提升基於特定實驗設定，需在更多任務類型、代理數量與環境下進一步驗證其普遍適用性。  

🎯 **給工程師的實務建議**  
- 在多代理 LLM 系統中，除了監執行結果，亦可加入 **計畫評估的一致性檢查** 作為早期警訊。  
- 可參考 EPC‑AW 的兩個步驟：先選擇在多代理間評估穩定的計畫，再利用評估不一致來微調代理的知識表示，以提升長期規劃可靠性。  

🔗 **論文連結**  
📝 When Planning Fails Despite Correct Execution: On Epistemic Calibration for LLM-Based Multi-Agent Systems  
👤 Zehao Wang, Shilong Jin, Zhao Cao, Lanjun Wang (Tianjin University; Renmin University of China)  
🔗 https://arxiv.org/abs/2605.23414  

你的多代理系統是否也在不知不觉中因「認知誤判」而踩雷？歡迎在留言區分享你的觀察與經驗 👇  

#AI #MultiAgent #LLM #Planning #EpistemicCalibration #TianjinUniversity #RenminUniversity #MachineLearning #AIResearch
