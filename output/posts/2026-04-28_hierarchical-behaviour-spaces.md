---
title: "Hierarchical Behaviour Spaces"
source: ChatPaper/AI
url: https://arxiv.org/abs/2604.24558
score: 109
model: tencent/hy3-preview:free
generated_at: 2026-04-28T20:31:48.042585
---

📌 階層行為空間方法  

你以為階層強化學習的威力來自長期規劃？最新研究指出，其實關鍵在於探索。  

🤔 **階層 RL 需要更好的選項表示方式**  
現有階層強化學習多依賴單一選項獎勵函數來描述子目標，這限制了可學習策略的表達力。近期工作雖能在數十億時間步上取得成功，但仍受預設獎勵函數的單一性所 constrain。  

🧪 **在 NetHack Learning Environment 上測試線性組合獎勵**  
研究團隊提出 Hierarchical Behaviour Spaces (HBS) 方法：不再為每個選項固定一個獎勵函數，而是變成一組基底獎勵函數，由高層控制器指定其線性組合，從而誘導出更豐富的行為空間。他們在 NetHack Learning Environment 上進行實驗，以驗證此設計的效果。  

🔍 **HBS 在 NetHack 上表現強勢，且層級優勢源於探索而非長期推理**  
實驗結果顯示 HBS 能達成強於基線的表現。進一步分析發現，該方法的優勢主要來自於增加探索的能力，而非傳統認為的長期推理或遞歸規劃。  

💡 **線性獎勵組合擴展了可學習的策略空間**  
透過將多個獎勵函數以權重相加，控制器可以在同一個選項內產生多樣化的行為模式。這使得階層架構不再只是「選擇預定子目標」，而是能夠在子目標內部進行細粒度的行為調整，從而在探索階段獲得更多有用的經驗。  

⚠️ **主要以單一複雜環境評估，泛化能力待驗證**  
目前的實驗集中在 NetHack 這個高難度、長時延的環境中。雖然論文提到方法具跨任務擴展潛力，但尚未在其他基準上進行系統驗證，因此泛化性仍需後續工作檢核。  

🎯 **設計階層 Agent 時可考慮以獎勵函數基底進行線性組合以提升探索**  
對於需要在稀疏獎勵或長 horizon 任務中進行探索的應用，將階層結構與獎勵函數線性組合結合，或許能提供一種既保持層級抽象又增強行為多樰性的設計方向。工程師在實作時可嘗試將現有的 option‑critic 框架替換為可學習的獎勵基底組合層。  

🔗 **論文連結**  
📝 Hierarchical Behaviour Spaces  
👤 Michael Tryfan Matthews, Anssi Kanervisto, Jakob Foerster, Pierluca D'Oro, Scott Fujimoto @ Meta Superintelligence Labs; University of Oxford  
🔗 https://arxiv.org/abs/2604.24558  

你認為在階層 RL 中以獎勵函數基底進行線性組合是一條值得探索的路徑嗎？歡迎在留言區分享你的看法 👇  

#AI #ReinforcementLearning #HierarchicalRL #Meta #Oxford #NetHack #AgentDesign #MachineLearning
