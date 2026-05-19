---
title: "GIM: Evaluating models via tasks that integrate multiple cognitive domains"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.18663
score: 113
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:37:18.420248
---

📌 **GIM：多認知整合基準**  

🎣 **當知識題庫被寫滿，抽象推理又脫離實際，我們該怎麼衡量模型的真實能力？**  

🤔 **研究背景**  
現有基準要么堆砌專門知識（如 GPQA、HLE），要么純抽象推理（如 ARC‑AGI）。前者容易把記憶誤當能力，後者則讓推理脫離實務情境。這使得評估要么過度依賴死記硬背，要么失去與真實任務的關聯。  

🧪 **研究設計**  
Meta Superintelligence Labs 團隊提出 Grounded Integration Measure（GIM），共 820 道原創題目（615 道公開，205 道私有）。每題需要同時調度多種認知操作——約束滿足、狀態追蹤、 epistemic vigilance（認知警覺）和 audience calibration（受眾校準）——在廣泛可得的知識基礎上完成，因此難度來源於「整合」而非專業知識或純抽象。題目皆由專家撰寫，多數採用 rubric‑decomposed 評分（中位數 6 個獨立判斷標準）。公開／私有題目的平衡切分內建了資料污染檢測機制。  

🔍 **核心發現**  
基於超過 200k 個 prompt‑response 對（橫跨 28 個模型），研究팀使用二參數 logistic IRT（2PL）模型進行校準，得到穩定的能力估計。該模型即使在原始正確率受噪聲或缺失數據影響時，也能正確排序不同的測試配置（模型＋思考層級）。  

💡 **深入分析**  
進一步的領板涵蓋 22 個模型與 47 個測試配置（獨特的 model‑thinking‑level 組合），並對 11 個模型在 35 個測試配置上進行了測試時計算（test‑time compute）與模型能力的權衡研究。結果顯示，同一模型家族內的配置選擇——例如思考預算（thinking budget）與量化程度——對最終表現的影響與模型本身的選擇同等重要。  

⚠️ **研究限制**  
根據目前公開的摘要，作者未具體說明研究的主要限制（如語言覆蓋、多模態擴展或長期穩定性測試等細節）。  

🎯 **實務啟示**  
工程師在比較模型時，不僅要看模型規模或訓練資料，亦應該考慮推理時的資源分配（如思考預算、量化策略）。GIM 提供的校準 ITR 參數與公開題目可直接用於本地評估，幫助偵測資料污染並獲得更具解釋力的能力分數。  

🔗 **論文連結**  
📝 GIM: Evaluating models via tasks that integrate multiple cognitive domains  
👤 Rohit Patel, Alexandre Rezende, Steven McClain @ Meta Superintelligence Labs  
🔗 https://arxiv.org/abs/2605.18663  

#AI #Benchmark #LLM #Meta #GIM #Evaluation
