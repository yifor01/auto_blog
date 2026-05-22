---
title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.22763
score: 107
model: tencent/hy3-preview:free
generated_at: 2026-05-22T20:38:38.288063
---

📌 【DeepMind 最新研究】AI 協助正式證明，解開 9 個 Erdős 問題  

你以為 AI 只能猜測數學答案？實際上，它現在能產出可機器驗證的正式證明，而且每題只要幾百美元。  

🤔 **數學研究的瓶頂：推理不可靠，證明難以驗證**  
大型語言模型在數學推理上表現越來越好，但其輸出的可靠性仍是限制因素。缺乏嚴格的驗證機制，使得 AI 雖能給出直覺答案，卻難以直接用於正式證明的撰寫。  

🧪 **大規模實證：讓 LLM 產出 Lean 形式證明並交叉驗證**  
研究團隊首次進行大規模評估，利用 LLM 生成 Lean 形式語言的證明，並透過 Lean 的型別檢查與定理驗證來確保正確性。實驗覆蓋了兩個公開問題集：353 個未解的 Erdős 問題與 492 個 OEIS 猜想。  

 **核心發現**：最強代理自主解決 9/353 個開放 Erdős 問題，證明 44/492 個 OEIS 猜想，每題成本僅幾百美元  
- 最強代理在無人干預的情況下，自給自足地完成了 9 個 Erdős 問題的正式證明。  
- 在 OEIS 猜想上，該代理成功證明了 44 個，佔總數的約 9%。  
- 每題的運算成本被描述為「幾百美元」，顯示此方法在資金上具備可行性。  

💡 **深入分析**：交替 LLM 生成與 Lean 驗證的基本代理能復現成功，但較難問題成本更高  
- 一個簡單的設計——讓 LLM 產出候選證明，隨即用 Lean 進行驗證，若失敗則重新生成——能夠復現上述 Erdős 的成功。  
- 然而，在較為挑戰性的問題上，此交替流程需要更多迭代，導致總體成本上升。這指出代理的效率與問題難度緊密相關。  

⚠️ **研究限制**：僅評估特定問題集（Erdős、OEIS），未說明在其他數學分支的表現；每題成本僅數百美元，但未探討大規模應用的總體費用  
- 實驗聚焦於兩個明確的開放問題集，無法直接推論至所有數學領域。  
- 論文僅提供單題成本估算，尚未討論若將此方法推廣至數百甚至數千題時的總體開銷與基礎設施需求。  

🎯 **實務啟示**：數學家可將 AI 當作形式證明的助手，先讓模型產出候選證明，再用形式驗證過濾錯誤；AI 工程師則可專注於設計更高效的交替策略  
- 對數學研究者：利用 AI 產出初步證明草形，再透過 Lean 等形式系統完成嚴格驗證，可大幅減少人工探索的試誤成本。  
- 對 AI 系統設計者：在 LLM 生成與形式驗證之間尋求更佳的平衡點——例如引入導向性提示、早期剪枝或強化學習——以降低在難題上的迭代次數與成本。  

🔗 **論文連結**  
📝 Advancing Mathematics Research with AI-Driven Formal Proof Search  
👤 George Tsoukalas, Anton Kovsharov, Sergey Shirobokov, Anja Surina, Moritz Firsching (Google DeepMind; Aarhus University; Google)  
🔗 https://arxiv.org/abs/2605.22763  

你認為這種「AI 生成＋形式驗證」的模式，在你的研究或工作中有什麼潛在應用？歡迎在留言區分享你的想法 👇  

#AI #數學 #形式證明 #Lean #DeepMind #Erdős #OEIS #機器學習 #科研工具
