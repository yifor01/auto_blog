---
title: "Inductive Deductive Synthesis: Enabling AI to Generate Formally Verified Systems"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.23109
score: 127
model: tencent/hy3-preview:free
generated_at: 2026-05-25T20:21:51.341331
---

📌 【UC Berkeley/Google】Inductive Deductive Synthesis：AI 生成可形式驗證的分散式系統  

你以為 AI 寫程式已經夠好？但對於需要嚴格正確性的分散式系統，它仍常失敗——因為測試無法保證所有可能的事件交錯都符合一致性等形式屬性。  

🤔 **形式保證的缺口**  
現有的程式生成代理（例如 Codex‑GPT‑5.4、Claude‑Code‑Opus‑4.6）在產生、測試與重構程式碼方面表現不錯，但對於必須在每種事件交錯下都成立的性質（如讀寫一致性）仍難以達到完整覆蓋。事實上，這些 SOTA 代理在七個分散式 key‑value-store 規格中僅成功通過兩項。  

🧪 **Inductive Deductive Synthesis (IDS) 框架**  
本文提出的 IDS 是一個具代理能力的 LLM 系統，它同時且遞增地合成實作與證明，並從失敗嘗試中學習，系統地嘗試更具希望的策略。IDS 將形式驗證的過程納入同一個迴圈，亦將效能回饋納入同一個學習過程。  

🚀 **核心發現**  
在相同的七個分散式 key‑value-store 規格上，IDS 達成了 7/7 的完全通過率，平均每個規格耗時約 6.8 小時、成本約 106 美元。與專家花費的月甚至年級工作相比，這相當於約 200 倍的速度提升；與現有 SOTA 代理相比，成本降低約 17%。此外，IDS 產出的實作在效能上可達到已發表已驗證系統的三倍。  

💡 **關鍵洞察**  
IDS 的成功來自於「實作」與「證明」的共同演化：當證明失敗時，系統會獲得具體的反饋來調整實作；當實作無法滿足效能目標時，同樣的回饋會驅動證明的調整。這種雙向學習使得系統能夠自動探索並收斂於同時符合正確性與效能的解。  

⚠️ **研究限制**  
實驗僅聚焦於分散式 key‑value-store 的規格集合；未涵蓋其他類型的形式屬性或更大規模的系統。此外，成本與時間的估算基於特定的硬體與模型設定，不同環境下的表現可能有所不同。  

🎯 **實務啟示**  
對於需要形式正確性的領域（例如共識協議、金融交易系統），IDS 提供了一種可自動化的途徑，能大幅縮短驗證週期並降低專家投入。工程團隊可嘗試將類似的「實作‑證明共生」迴圈納入現有的 AI 輔助開發流程，尤其在成本與時間敏感的專案中。  

🔗 **論文連結**  
📝 Inductive Deductive Synthesis: Enabling AI to Generate Formally Verified Systems  
👤 Shubham Agarwal, Alexander Krentsel, Shu Liu, Mert Cemri, Audrey Cheng (UC Berkeley; Google; UC Santa Cruz)  
🔗 https://arxiv.org/abs/2605.23109  

你是否曾因缺乏形式保證而對 AI 生成的程式感到不安？這項工作顯示，讓 AI 同時學會寫程式與證明正確性，或許是未來可信賴軟體的關鍵一步。歡迎在留言區分享你的看法 👇  

#AI #FormallyVerifiedSystems #InductiveDeductiveSynthesis #UCBerkeley #GoogleResearch #分散式系統 #程式驗證 #機器學習 #軟體工程
