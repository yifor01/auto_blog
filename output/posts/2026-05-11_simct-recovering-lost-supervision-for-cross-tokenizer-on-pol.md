---
title: "SimCT: Recovering Lost Supervision for Cross-Tokenizer On-Policy Distillation"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.07711
score: 111
model: tencent/hy3-preview:free
generated_at: 2026-05-11T20:29:15.811261
---

📌 【USTC & Tencent 等】SimCT：解決異種 tokenizer 下的 on‑policy distillation 監控信號遺失  

當老師與學生模型切斷詞時，傳統的 on‑policy distillation 會悄悄丟掉大半的教學訊號——你有沒有想過，這可能是為什麼跨模型蒸餾總是難以提升？  

🤔 **異種 tokenizer 讓監控信號對半斷裂**  
On‑policy distillation (OPD) 假設老師與學生的預測可以逐 token 對齊。然而，當兩模型使用不同的 tokenizer 時，許多位置的 token 根本無法直接匹配，導致大量的教師信號被「共享 token」匹配機制 silenziosamente 捨棄。  

🧪 **以共同可實現的多 token 片段為橋樑**  
SimCT（Simple Cross‑Tokenizer OPD）保持 OPD 原始損失函式不變，僅將監督空間擴展：除了共享的單 token 外，還參與比較老師與學生都能實現的短多‑token 續段。這些續段正是兩個 tokenizer 能同時產生的最細粒度監督介面，更粗的單位會遮蔽對 on‑policy 學習有用的老師‑學生差異。  

📊 **在數學推理與程式碼生成基準上持續領先**  
作者在三組異質 teacher‑student 配對上，分別測試了數學推理與程式碼生成基準。實驗顯示 SimCT 一致優於傳共享‑vocabulary OPD 與代表性的跨 tokenizer 基線，且消融實驗證實提升來源正是透過恢復原本被 exact shared‑token matching 棄掉的監督信號。  

💡 **最細粒度的共同可 token 化監督介面**  
透過理論分析，SimCT 證明所選用的 multi‑token 續段是兩種 tokenizer 共同能夠產生的最小單位；使用更長的片段雖能增加覆蓋率，但會引入無法同時實現的組織，反而減少有用的教師‑學生區分。  

⚠️ **樣本僅限於特定任務，長效泛化尚未驗證**  
目前結果僅基於數學推理與程式碼生成兩類基準，未涵蓋其他領域（如開放式對話或多模態任務）；此外，實驗未探討長期訓練或更大規模模型的行為，長效效果仍需後續工作驗證。  

🎯 **工程師可直接採用 joint‑tokenizable 片段來補回蒸餾信號**  
對於需要在異種 tokenizer 間進行模型壓縮或知識遷移的場景，SimCT 提供了一種「零改動」的損失函式擴展方式：只需在蒸餾過程中加入可同時被兩端 tokenizer 生成的短續段作為監督目標，即可回復原本被遺失的教師信號，從而在推理與程式碼任務上獲得明顯提升。  

🔗 **論文連結**  
📝 SimCT: Recovering Lost Supervision for Cross-Tokenizer On-Policy Distillation  
👤 Jie Sun, Mao Zheng, Mingyang Song, Qiyong Zhong, Yilin Cheng  
🏫 University of Science and Technology of China; Large Language Model Department, Tencent; Shanghai Innovation Institute; Zhongguancun Academy  
🔗 論文：https://arxiv.org/abs/2605.07711  
💻 程式碼：https://github.com/sunjie279/SimCT-  

你在跨模型蒸餾時是否也遇過 tokenizer 不匹配的問題？歡迎在留言區分享你的經驗或想法 👇  

#AI #KnowledgeDistillation #LLM #Tokenizer #USTC #Tencent #MachineLearning #NLP #CodeGeneration #MathReasoning
