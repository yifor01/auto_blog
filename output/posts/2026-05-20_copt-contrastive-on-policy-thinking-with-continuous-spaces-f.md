---
title: "CopT: Contrastive On-Policy Thinking with Continuous Spaces for General and Agentic Reasoning"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.20075
score: 133
model: tencent/hy3-preview:free
generated_at: 2026-05-20T20:46:33.818539
---

📌 **CopT：先答後思的推理鏈，提升準確度 23% 同時省 token 57%**

你是否曾經觀察到，大型語言模型在給出答案前常常先進行冗長的「思考」鏈，即使答案已經浮現？這種做法不只浪費 token，還可能延遲實用回覆的取得。

🤔 **將思考與回答的順序顛倒，能否同時獲得更高準確度與更低成本？**

研究團隊指出，現有的 Chain‑of‑thought (CoT) 將「思考」視為回答的必要前置步驟。當模型已經能夠辨識出合理答案時，強制進行額外思考會產生所謂的「performative reasoning」——既浪費資源又可能降低效率。

🧪 **先產出草稿答案，再以自身答案為條件進行 on‑policy 思考**

CopT 重新設計了推理管線：模型首先產出一個草稿答案；接著，以該草稿答案為條件，啟動後續的 on‑policy 思考，用於反思與糾正。為了判斷草稿答案是否足夠可靠，CopT 將連續空間的嵌入視為即時的對比驗證器。具體來說，它對比模型在離散 token 輸入與連續嵌入輸入下對同一組生成 token 的支持度，從而得到一個序列層級的反向 KL 值，用來估計答案的可靠度。理論分析顯示，在某些假設下，此估計的期望值等於未解決潛在狀態與輸出答案 token 之間的互情報，因而能捕捉與答案相關的不確定性，而非潛在狀態中的任意不確定性。

當草稿答案的可靠度不足時，CopT 會進一步進行 on‑policy 思考；此時第二個 KL 值動態調整草稿答案的可見度，在保留有用部分資訊的同時降低被不可靠內容誤導的風險。

🚀 **在數學、程式碼與代理推理任務上，準確度最高提升 23%，token 用量最多降低 57%**

實驗顯示，無需任何額外訓練，CopT 在多個基準上均能同時提升峰值準確度（最高達 23%）並減少 token 消耗（最高達 57%），在相同或更高的準確度下實現更高的效率。

💡 **關鍵在於「以答案驗證思考」而非「思考產出答案」**

與傳統 CoT 不同，CopT 把思考放在答案的驗證與修正階段。這意味著模型可以先利用其直接輸出的草稿答案作為參考，再依據該答案的可靠度決定是否需要額外思考。這種「答案先行」的策略讓模型在確信答案時能夠快速給出回覆，而在不確定時才啟動更深入的反思，從而在資源使用與效果之間取得更好的平衡。

⚠️ **僅於離線基準評估，未涉及真實互動環境的長期效果**

目前的結果來自數學、程式碼與代理推理的離線基準測試。論文未報告在真實互動或長期對話情境中的表現，亦未說明該方法在不同模型規模或訓練資料上的普適性。

🎯 **實務上可直接作為推理端的插件使用**

由於 CopT 不需要額外訓練，開發者可將其作為現有 LLM 推理流程的後處理模組，即時獲得更高的答案正確率與較低的 token 成本。在對成本敏感或需要快速回應的應用（例如程式碼輔助、數學題解答、代理規劃）中，這種「先答後思」的機制提供了可立即採用的效能提升途徑。

🔗 **論文連結**  
📝 CopT: Contrastive On-Policy Thinking with Continuous Spaces for General and Agentic Reasoning  
👤 Dachuan Shi, Hanlin Zhu, Xiangchi Yuan, Wanjia Zhao, Kejing Xia  
🏫 Georgia Tech; UC Berkeley; Stanford University; Microsoft  
🔗 https://arxiv.org/abs/2605.20075  
💻 程式碼：https://github.com/sdc17/CopT  

你在使用 AI 輔助編程或數學解題時，是否也會先給出草稿答案再進行驗證？歡迎在留言區分享你的經驗與看法 👇

#AI #LLM #Reasoning #CopT #GeorgiaTech #UCBerkeley #Stanford #Microsoft #機器學習 #自然語言處理
