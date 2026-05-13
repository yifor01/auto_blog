---
title: "Rollout Cards: A Reproducibility Standard for Agent Research"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.12131
score: 101
model: tencent/hy3-preview:free
generated_at: 2026-05-13T20:45:35.824783
---

📌 **Rollout Cards：Agent 研究的可重現新標準**  

你以為 Agent 的分數能直接比較？研究顯示，只改變計分規則，就可能讓排名顛倒 20.9 個百分點。  

🤔 **當分數背後的過程被隱藏，比較失去意義**  
在強化學習與 Agent 研究中，論文常僅報告最終分數，卻未保存產生這些分數的完整運行記錄（rollout）。這意味著同一段行為，因評估選取的片段或不同的報告規則，可能得到截然不同的分數，導致實際比較不可靠。  

🧪 **對 50 個熱門訓練與評估倉庫的結構化審計**  
研究團隊審計了 50 個公開的訓練與評估倉庫，發現沒有一個在報告頭條分數時，同時說明有多少次運行失敗、錯誤或被跳過。此外，他們記錄了 37 個案例：僅因報告規則的不同（例如如何計算成功率、成本或時間），同樣的證據就能改變任務成功率、成本/token 統計或時間測量，有時變化劇烈。  

 **以運行記錄為重點，提出 Rollout Cards**  
論文將可重現性的單位從「報告分數」轉移到「運行記錄」本身。他們提出 **Rollout Cards** —— 一種發布套件，保存完整的運行記錄，並明確說明所使用的視角（view）、報告規則（reporting rule）以及被排除的運行（drops manifest）。這樣，讀者可以檢查實際產分數的過程，而非只看最終數字。  

🔬 **兩種驗證方式：部分公開釋出與重新評分**  
首先，他們在四個領域（工具安全、多智慧體系統、定理證明、搜尋）進行了部分公開的 Rollout Card 釋出，使得原始報告未曾涵蓋的額外分析成為可能。其次，他們保存了跨短答、程式碼生成與工具使用三類基準的原始輸出，僅更改報告規則，就發現報告分數會變動多達 **20.9 個百分點**，在某些情況下甚至會逆轉模型的排名。  

⚠️ **樣本限制與實作範圍**  
此研究的結論基於對現有公開倉庫的審計與特定基準的重新評分；未涵蓋所有可能的 Agent 任務或報告變體。此外，所提出的 Rollout Cards 需要研究團隊在發布時主動保存運行記錄，這在現有工作流程中可能額外增加工程成本。  

🎯 **為未來研究提供即用工具**  
團隊將 Rollout Cards 的參考實作整合到開源強化學習平台 **Ergon**，並公開發布 Ergon 產出的 Rollout Card 匯集，涵蓋工具使用、軟體工程、網頁互動、多智慧體協調、安全與搜尋等基準。這樣，後續研究者可以直接下載並驗證，或在自己的實驗中採用相同的可重現標準。  

🔗 **論文連結**  
📝 Rollout Cards: A Reproducibility Standard for Agent Research  
👤 Charlie Masters, Ziyuan Liu, Stefano V. Albrecht (Deepflow; Nanyang Technological University)  
🔗 https://arxiv.org/abs/2605.12131  

你目前在評估 Agent 時，會檢查運行記錄还是只看最終分數？歡迎在留言區分享你的看法與實務經驗 👇  

#AI #Agent #Reproducibility #RolloutCard #Deepflow #NTU #Ergon #MachineLearning #研究方法
