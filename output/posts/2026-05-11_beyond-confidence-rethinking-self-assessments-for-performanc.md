---
title: "Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.07806
score: 96
model: tencent/hy3-preview:free
generated_at: 2026-05-11T20:55:03.116207
---

📌 **LLM 自評新維度：努力與能力勝過信心**  

你以為模型說「我很有信心」就代表它正確嗎？研究顯示，單一的信心分數常常過於樂觀，反而失靈。  
這篇論文提出用六個心理維度來重新評估模型的自我判斷，看看哪些維度真的能預測失誤。  

🤔 **為什麼單一的信心不夠可靠**  
在高風險應用中，我們需要模型能夠誠實地報告自己的錯誤可能性。以往的做法主要依賴模型給出的機率估計或 verbalized confidence，但實證顯示這種單一指標往往過於樂觀，無法一致地預測模型失誤。  

🧪 **六維度自我評估與廣泛實驗**  
研究團隊借鑒人類認知評估理論，將自我評估分解為六個 appraisal-based 維度（包括努力、能力以及情感相關的維度），並在 confidence 之外一起進行測量。他們在 12 種不同規模的大型語言模型與橫跨八個領域的 38 個任務上，比較這些維度預測模型失誤的效用。  

📊 **能力相關維度表現更佳，情感維度貢獻有限**  
結果顯示，與能力相關的維度——特別是努力和能力——在多數設定下能與 confidence 持平或優於它。此外，effort 提供的估計較不過於樂觀，且在不同模型規模間保持穩定。相比之下，情感相關的維度只提供微弱的預測信號。  

💡 **任務特性決定哪個維度最具情報量**  
最有預測力的維度會隨任務類型而變化：在需要深度推理的任務中，effort 是最佳預測因子；而在以檢索為主的任務中，ability 和 confidence 則更具預測力。這意味著，模型的自我評估不該採用「一刀切」的單一指標，而應該依賴任務特性來選擇適合的維度。  

⚠️ **研究範圍與後續需求**  
本研究僅涵蓋了所測試的 12 個模型與 38 個任務，未涵蓋所有可能的應用場景。維度的數值來自於模型的語言表達，可能受到提示設計的影響。未來工作可探索這些維度在更大規模模型、實時交互或不同提示策略下的表現，以及如何將它們納入模型部署的安全監控機制。  

🎯 **對工程師的實務啟示**  
- 在推理密集型應用（如數學推理、代碼生成）中，監測模型自報的「努力」可能比單純看 confidence 更能預警失誤。  
- 在檢索導向型任務（如問答、文檔檢索）中，能夠結合 ability 與 confidence 來獲得較可靠的自我評估。  
- 開發多維度自我評估介面（例如同時收集 effort、ability、confidence 等回饋）有助於建立更穩健的模型可靠性檢測系統，從而在部署前減少過度依賴模型過樂觀的自我報告所帶來的風險。  

🔗 **論文連結**  
📝 Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs  
👤 Sree Bhattacharyya, Samarth Khanna, Leona Chen, Lucas Craig, Tharun Dilliraj (The Pennsylvania State University)  
🔗 https://arxiv.org/abs/2605.07806  

你在使用 AI 輔助工具時，會注意到模型的自我報告嗎？歡迎在留言區分享你的觀察與經驗 👇  

#AI #LLM #SelfAssessment #ModelReliability #PennState #MachineLearning #AI安全 #自然語言處理
