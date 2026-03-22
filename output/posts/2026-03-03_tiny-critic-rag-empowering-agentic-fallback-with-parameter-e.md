---
title: "Tiny-Critic RAG: Empowering Agentic Fallback with Parameter-Efficient Small Language Models"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2603.00846
score: 110
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-03T20:08:13.842186
---

📌 【Tiny-Critic RAG】用小模型做評估，Agentic RAG 成本砍半

Agentic RAG 讓 LLM 具備自主推理能力，但一個問題很難迴避：為了讓 AI 自己判斷要不要呼叫工具、要不要重跑流程，我們得用超大模型做評估，這成本誰來付？

🤔 **用 GPT-4 做門神，成本太高了**

現在的 Agentic RAG 很依賴大模型做「反思者」角色，判斷結果是否可信、是否需要重跑。但問題是：一個 1750 億參數的模型，只是為了輸出「Yes/No」，就要跑完整的前向傳播，這就像用超跑載一塊郵票，效率極低。

更慘的是在自主代理場景，如果第一次資訊檢索就錯了，模型會花很多 token 在無意義的推理和重複的工具呼叫上，不只慢，成本也直線上升。

🧪 **52 位工程師的隨機對照實驗**

這是一項隨機對照實驗 (RCT)，招募了 52 位軟體工程師（大多為初級）。參與者需學習一個新的 Python 函式庫 (Trio)，一組可以使用 AI 助手，另一組必須手動編程。完成任務後，立即進行知識測驗。

 **用 AI 的那組，測驗分數低了 17%**

- AI 組平均分數：50%
- 手動編程組平均分數：67%
- 這相當於整整兩個等級的差距 (Cohen's d=0.738, p=0.01)

差距最大的是 Debugging 題型，代表使用 AI 輔助的開發者，可能在「判斷程式碼哪裡錯了、為什麼錯」的能力上發展受阻。

💡 **用 AI 建立理解 vs. 用 AI 取代思考**

研究團隊歸納出不同的 AI 互動模式：

低分模式（平均 < 40%）：完全讓 AI 寫、逐漸依賴 AI、用 AI 除錯但不理解問題
高分模式（平均 ≥ 65%）：先讓 AI 產生再追問理解、要求同時解釋、只問概念自己寫

關鍵差異：高分者用 AI 來「建立理解」，低分者用 AI 來「取代思考」。

⚠️ **樣本小、僅測短期記憶，長期效果未知**

樣本數較小 (n=52)、測驗在任務後立即進行、長期學習效果未知、此研究使用對話式 AI 助手而非 Agentic 工具。

🎯 **刻意練習仍然重要，AI 學習模式值得善用**

- 認知上的努力對能力養成是必要的
- Claude 有 Code Learning 模式，ChatGPT 有 Study Mode
- 與其說「幫我寫」，不如說「解釋這段為什麼這樣設計」

🔗 **論文連結**
📝 How AI Impacts Skill Formation
👤 Judy Hanwen Shen & Alex Tamkin @ Anthropic
🔗 論文：arxiv.org/abs/2601.20245

你的 AI 輔助開發習慣是哪一種模式？歡迎分享你的觀察 👇

#AI #Coding #MachineLearning #軟體工程 #Anthropic #Claude #技術成長
