---
title: "ThoughtTrace: Understanding User Thoughts in Real-World LLM Interactions"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.20087
score: 107
model: tencent/hy3-preview:free
generated_at: 2026-05-20T21:09:51.940413
---

📌 【Johns Hopkins / MIT / Google Research 最新研究】ThoughtTrace：首次捕捉真實人機對話中的使用者思緒  

🎣 你以為 AI 只看見你說的話？——研究發現，你的潛在想法才是關鍵  

🤔 **現有資料只記錄語句，卻漏掉了背後的思考**  
Conversational AI 已服務數十億使用者，但現有資料集僅保留人類發送的訊息與模型的回覆，缺少使用者在送出提示前或收到回覆後所想的「思緒」。這使得我們難以理解人機互動背後的認知動態，也限制了模型對使用者真實需求的建模。  

🧪 **1,058 位使用者、2,155 次多輪對話、10,174 則思緒標註**  
研究團隊構建了 ThoughtTrace，這是目前規模最大的資料集，包含：  
- 1,058 位不同使用者  
- 2,155 段真實世界的多輪人類–AI 對話  
- 17,058 個對話輪次  
- 10,174 則使用者自報的思緒（他們發送提示的原因以及對助手回應的反應）  
資料橫跨 20 種不同的語言模型，涵蓋廣泛的主題與較長的對話時程。  

🔍 **思緒與訊息在語義上明顯不同，且難為前沿 LLM 直接推斷**  
分析顯示：  
- 思緒的語義內容與使用者實際發送的訊息有顯著區別  
- 即便是目前最強的前沿語言模型，僅憑對話脈絡也難以準確推斷出這些思緒  
- 思緒內容多樣化，且與對話的不同階段（開頭、中段、結尾）相關聯  

💡 **思緒可作為新型資料 modality，提升下游模型表現**  
研究進一步展示了思緒的實用價值：  
1. 作為推論時的額外內容，思緒能改善使用者行為預測的準確度  
2. 以思緒為導向的回覆改寫（thought‑guided rewrites）可提供細緻的對齊訊號，有助於訓練更具個人化的助手  

⚠️ **資料規模尚屬首次發布，社群可见度有待提升**  
雖然 ThoughtTrace 提供了全新的研究視角，但該資料集最近才在 arXiv 上公布（未來日期），目前在社群中的討論度尚未擴大，屬於具潛力但尚未成為熱門話題的工作。  

🎯 **將使用者思緒納入模型設計，有助於建立更貼近真實需求的助手**  
- 未來可將思緒作為推論階段的上下文，提升對使用者下一步行為的預測  
- 在訓練階段利用思緒導向的改寫，產出更精準的對齊訊號，從而訓練出能更好適應使用者 latent goals、偏好與需求的個人化模型  

🔗 **論文連結**  
📝 ThoughtTrace: Understanding User Thoughts in Real-World LLM Interactions  
👤 Chuanyang Jin, Binze Li, Haopeng Xie, Cathy Mengying Fang, Tianjian Li (Johns Hopkins University; Massachusetts Institute of Technology; Google Research)  
🔗 https://arxiv.org/abs/2605.20087  

你在與 AI 對話時，常會有哪些未說出口的想法？歡迎在留言區分享你的觀察 👇  

#AI #LLM #HumanAIInteraction #ThoughtTrace #JohnsHopkins #MIT #GoogleResearch #NLP #機器學習 #個人化助手
