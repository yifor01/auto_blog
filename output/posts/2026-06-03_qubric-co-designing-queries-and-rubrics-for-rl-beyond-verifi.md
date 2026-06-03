---
title: 'QUBRIC: Co-Designing Queries and Rubrics for RL Beyond Verifiable Rewards'
source: arXiv
url: http://arxiv.org/abs/2606.03968v1
score: 97
model: tencent/hy3-preview:free
generated_at: '2026-06-03T21:43:22.038324'
---

📌 **QUBRIC：共同設計查詢與評分規則**  
你以為只能靠對答案來訓練 AI？當問題沒有標準答案時，傳統強化學習會失效。QUBRIC 提出一個方法：同時重新設計問題與評分規則，讓模型在開放式任務上也能獲得有效回饋。  

🤔 **當獎勵無法直接驗證時，評分規則本身成為瓶頸**  
現有的 rubric‑based RL 方法會在固定的查詢分布上優化評分規則。然而，開放式查詢容易產生模糊的規則；若過度限縮查詢，則會引入無法被任何模型驗證的虛構參考，導致所有回答都得不到獎勵訊號。這意味著 rubric 的品質最終受限於查詢的結構。  

🧪 **共同重塑開放式問題與對應評分規則**  
QUBRIC 透過三個步驟實現查詢與規則的共同設計：首先，利用教師模型提取關鍵點，將開放式查詢改寫為具體、可評估的情境問題；其次，以對比方式生成規則，把教師策略與學生策略的差距轉換為查詢層級的評分標準；最後，透過可學習過濾（learnability filtering）僅保留資訊豐富的查詢‑規則對，作為 GRPO 訓練的依據。  

📈 **在 ArenaHard 上提升 5.5 分，並在法律、道德、敘事推理基準上平均提升 6.3 分**  
僅使用指令跟隨資料進行訓練，QUBRIC 在 ArenaHard 基準上相對於 SFT 基線獲得了 +5.5 點的提升。進一步在三個持-out 基準（法律、道德、敘事推理）上測試，平均提升達到 +6.3 點，且改進主要集中在推理相關的維度。  

💡 **提升主要集中在推理相關維度，顯示查詢‑評分規則共同設計強化了模型的深層理解**  
實驗結果表明，當查詢被重新構造成具體情境且評分規則能夠精準捕捉教師與學生的差距時，模型不僅在給定任務上表現更好，也能將這種能力轉移到需要複雜推理的領域。這說明共同設計過程幫助模型建立了更穩固的內部推理框架，而非僅靠表面的模式匹配。  

⚠️ **方法依賴教師模型的關鍵點提取，且僅在指令跟隨數據上訓練，長效與更大規模模型的表現有待觀察**  
雖然 QUBRIC 在現有實驗中表現穩健，但其效果仍取決於教師模型能否提供高品質的關鍵點。此外，目前的訓練僅限於指令跟隨資料，尚未在更大規模或更長 horizon 的強化學習設定中進行驗證。  

🎯 **工程師可直接將 QUBRIC 框架加入現有 GRPO 訓練流程，提升難以驗證任務的表現**  
對於希望在無法直接給出正確答案的情境下仍能進行強化學習的團隊，QUBRIC 提供了一種可插拔的方法：先取得教師模型的關鍵點，重新產生情境式查詢與對應規則，過濾後用於 GRPO 優化。這樣的流程不需要額外的標註成本，即可在法律檢索、道德判斷或故事生成等任務上獲得明顯提升。  

🔗 **論文連結**  
📝 QUBRIC: Co-Designing Queries and Rubrics for RL Beyond Verifiable Rewards  
👤 Rongzhi Zhang, Rui Feng, Zhihan Zhang, Jingfeng Yang, Qingyu Yin  
🔗 http://arxiv.org/abs/2606.03968v1  

#AI #ReinforcementLearning #RLVR #QUBRIC #GRPO #InstructionFollowing #Reasoning #MachineLearning #研究分享
