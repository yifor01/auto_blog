---
title: "PlanningBench: Generating Scalable and Verifiable Planning Data for Evaluating and Training Large Language Models"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.20873
score: 115
model: tencent/hy3-preview:free
generated_at: 2026-05-21T20:38:11.690177
---

📌 PlanningBench：可控生成規劃資料提升LLM規劃力  

規劃能力是LLM處理複雜任務的關鍵，但現有基準往往只是靜態資料集，難以控制難度與驗證。  
PlanningBench 提出可控生成框架，讓規劃資料變得可擴展、可驗證。  
這意味著我們可以系統地評估與訓練模型的規劃表現，而不再受固定基準的限制。  

🤔 **規劃資料的瓶須來自靜態基準**  
現有規劃評估多依賴固定的實例集合，這導致場景覆蓋有限、難度與表面特徵綁定、缺乏可伸縮生成與自動驗證的支援。研究團隊指出，這些限制阻礙了對LLM規劃能力的全面診斷與改進。  

🧪 **以分類樹與約束驅動的合成管線**  
PlanningBench 從真實規劃情境出發，抽象出超過30種任務類型、子任務、約束族與難度因子的分類樹。在該分類樹的引導下，採用約束驅動的合成管線實例化自包含的規劃問題，並內建自適應難度控制、品質過濾與實例層級的驗證核對表。這使得資料建構從靜態收集轉為可控生成，同時保持與真實任務的 grounding。  

💡 **模型在耦合約束下仍顯不足**  
使用PlanningBench評估開放原始與閉源前沿LLM時，發現目前的模型在必須同時滿足多個約束的情境下，難以產出完整的可執行解決方案。這說明即使在參數規模與訓練資料上已達一定水準，耦合約束的規劃任務仍是模型的薄弱環節。  

⚠️ **研究限制：樣本與驗證範圍**  
本工作主要聚焦於規劃資料的可控生成與驗證機制，未涵蓋所有可能的規劃領域或極端長 horizon 場景。此外，雖然展示了在驗證資料上進行強化學習能提升未見基準與廣泛指令遵循表現，但具體的訓練成本與收斂動態尚需後續工作進一步探討。  

🎯 **實務啟示：以可驗證資料導向規劃訓練**  
- 可透過PlanningBench生成的資料進行基準評估，快速定位模型在約束耦合方面的不足。  
- 在驗證過的規劃資料上進行強化學習，有助於提升模型在未見規劃任務及一般指令遵循上的泛化能力。  
- 研究進一步指出，具有明確唯一最優解或良好規範的問題能提供更清晰的獎勵訊號與較穩定的訓練動態，這在設計未來的規劃導向訓練時值得參考。  

🔗 **論文連結**  
📝 PlanningBench: Generating Scalable and Verifiable Planning Data for Evaluating and Training Large Language Models  
👤 Ziliang Zhao, Zenan Xu, Shuting Wang, Hongjin Qian, Yan Lei  
🏫 Renmin University of China; LLM Department, Hunyuan Team, Tencent; Beijing Academy of Artificial Intelligence; The Chinese University of Hong Kong  
🔗 https://arxiv.org/abs/2605.20873  

你認為可控生成的規劃資料在提升LLM實用性方面還有哪些潛力？歡迎留言討論 👇  

#AI #Planning #LLM #Reasoning #Agents #Tencent #RenminUniversity #HKU #MachineLearning
