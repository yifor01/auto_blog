---
title: "Beyond Rows to Reasoning: Agentic Retrieval for Multimodal Spreadsheet Understanding and Editing"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2603.06503
score: 111
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-09T22:38:27.115906
---

📌 【PwC 最新研究】Excel 分析的 AI 革命：超越單次檢索，實現多步驟推理

企業 Excel 分析遇到的最大困境是什麼？當工作簿包含數百萬個儲存格、跨工作表依賴關係和嵌入式視覺元素時，現有 AI 方法不是遺漏關鍵資訊，就是壓縮數據導致解析度降低，甚至超出 LLM 上下文窗口限制。

🤔 **單次檢索的致命缺陷**

當前最先進的多模態檢索增強生成 (RAG) 技術，讓大型語言模型能夠分析企業級 Excel 工作簿。但這些方法存在三個關鍵缺陷：

1. 單次檢索會排除關鍵上下文
2. 壓縮會損失數據解析度
3. 天真的全上下文注入會超出 LLM 上下文窗口

這些限制阻礙了對複雜企業工作簿的可靠多步驟推理。

🧪 **200 小時專家評估驗證的突破**

PwC 團隊引入了「超越行到推理」(BRTR) 框架，這是一種多模態代理框架，用迭代工具調用迴圈取代單次檢索，支援從複雜分析到結構化編輯的端到端 Excel 工作流程。

BRTR 經過超過 200 小時的專家人工評估，在三個前沿試算表理解基準測試中達到最先全性能。

 **25 個百分點的絕對性能提升**

- FRTR-Bench：超越先前方法 25 個百分點
- SpreadsheetLLM：提升 7 個百分點
- FINCH：提升 32 個百分點

這些巨大的性能提升，意味著 BRTR 能夠真正理解和處理企業級 Excel 工作簿的複雜性。

💡 **NVIDIA NeMo Retriever 1B 稱霸混合數據**

研究團隊評估了五種多模態嵌入模型，發現 NVIDIA NeMo Retriever 1B 在混合表格和視覺數據上表現最佳。這種模型在處理 Excel 工作簿時，能夠有效平衡表格數據和視覺元素的理解能力。

 **GPT-5.2 提供最佳效率-準確度權衡**

在變更九種大型語言模型的實驗中，GPT-5.2 實現了最佳的效率-準確度權衡。這意味著在保持高準確度的同時，系統也能保持合理的計算成本。

⚠️ **每個組件都至關重要**

消融實驗確認了規劃器、檢索和迭代推理三個組件都對性能有重大貢獻。移除任何一個組件都會導致性能明顯下降，證明了 BRTR 架構的完整性。

🎯 **完整的可追溯性保證透明度**

BRTR 透過明確的工具調用追蹤保持完全的可追溯性。這意味著每個推理步驟都有清晰的記錄，這對於企業應用來說至關重要，因為需要能夠解釋和審計 AI 的決策過程。

🔗 **論文連結**
📝 Beyond Rows to Reasoning: Agentic Retrieval for Multimodal Spreadsheet Understanding and Editing
👤 Anmol Gulati, Sahil Sen, Waqar Sarguroh, Kevin Paul @ PricewaterhouseCoopers
🔗 論文：arxiv.org/abs/2603.06503

#AI #Excel #Multimodal #Spreadsheet #PwC #AgenticAI #RAG #LLM
