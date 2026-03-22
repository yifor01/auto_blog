---
title: "LaSER: Internalizing Explicit Reasoning into Latent Space for Dense Retrieval"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2603.01425
score: 123
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-03T19:50:55.779446
---

📌 【LaSER: 讓檢索器學會「無聲思考」】

隨著大型語言模型 (LLM) 的興起，檢索系統從傳統的編碼器架構進化到生成式模型。但你知道嗎？儘管LLM擁有強大的推理能力，現有的檢索器卻只把它當作靜態編碼器使用，沒能真正發揮它的推理潛力。

🤔 **推理能力擺著不用？檢索器的關鍵瓶頸**

當前最先進的檢索系統仍然主要依賴LLM的編碼能力，而非其推理能力。為了解決這個問題，現有的做法是先生成明確的推理鏈 (Chain-of-Thought, CoT) 再進行檢索，但這種「重寫再檢索」的流程會造成難以接受的延遲。

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
