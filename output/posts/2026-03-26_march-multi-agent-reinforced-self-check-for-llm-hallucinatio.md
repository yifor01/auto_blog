---
title: "MARCH: Multi-Agent Reinforced Self-Check for LLM Hallucination"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2603.24579
score: 126
model: gpt-4o-free
generated_at: 2026-03-26T19:32:39.422870
---

📌【阿里巴巴團隊新突破】三代理論破解 LLM 幻覺難題，MARCH 框架讓小模型也能追平大模型！

你是否曾因大型語言模型（LLM）的「幻覺」（hallucination）問題感到困擾？當 AI 開始生成看似真實卻完全虛構的內容，特別是在需要檢索輔助生成（Retrieval-Augmented Generation, RAG）的場景時，這不僅損害了用戶體驗，也限制了技術的實際應用範圍。

阿里巴巴 Qwen 團隊與香港中文大學（深圳）研究人員聯手，提出了一種全新框架——MARCH（Multi-Agent Reinforced Self-Check for Hallucination），專門為解決這一問題而設計，並公開了相關程式碼供社群使用。

🤔 **LLM 自我審查的盲點：確認偏誤如何限制真實性？**

目前解決幻覺問題的主流做法是讓 LLM 自己「審查」輸出的內容是否符合檢索到的證據。然而，這種 LLM-as-a-judge 方法存在一個致命缺陷：審查者往往無法跳脫原始生成內容的框架，容易繼承生成的錯誤，形成「確認偏誤」（confirmation bias）。

這意味著，越是依賴 LLM 自我審查，就越可能讓錯誤循環擴大。

🧪 **三代理論：MARCH 框架的巧妙設計**

MARCH 創新地引入了「三代理論」架構，透過資訊不對稱（information asymmetry）來打破確認偏誤，實現更嚴格的事實對齊：

1️⃣ **Solver**：生成初始的 RAG 回應。這是整個流程的起點，也是其他代理後續工作的基礎。

2️⃣ **Proposer**：將 Solver 的輸出拆解為可驗證的「原子命題」（atomic propositions）。這一步的關鍵在於將複雜的敘述分解為小單位，便於逐一驗證。

3️⃣ **Checker**：針對每個原子命題，獨立驗證其是否符合檢索到的證據，而不參考 Solver 的原始輸出。這種刻意的資訊不對稱避免了審查者受到生成內容的「污染」。

此外，MARCH 採用多代理強化學習（Multi-Agent Reinforcement Learning, MARL）進行訓練，使三個代理可以協同進化，共同提升事實準確性。

🎯 **核心發現：小模型也能追平大模型的表現！**

透過廣泛的幻覺基準測試，MARCH 顯著降低了幻覺率，並展現以下亮點：

- 在 8B 參數規模下，搭配 MARCH 的 LLM 在多項任務中達到與封閉源大型模型相當的性能。
- 相較於傳統的 LLM 自我審查方法，MARCH 的框架在事實準確性上展現出顯著提升。

這意味著，MARCH 不僅優化了小模型的能力，還為 LLM 的真實性改進提供了一條可擴展的技術路徑。

⚠️ **研究的限制與未來方向**

雖然 MARCH 在現有基準測試中表現亮眼，但其適用性仍需進一步探索，特別是在更複雜的多模態場景和實時應用中。此外，資訊不對稱的設計是否會在某些情境下引入新的偏誤，也是未來需要關注的問題。

🔗 **實務啟示：MARCH 框架的應用潛力**

- 對於開發檢索輔助生成（RAG）系統的工程師，MARCH 提供了一個可落地的解決方案，顯著提升輸出內容的真實性。
- 開源程式碼已經釋出，方便開發者快速試驗並整合到現有系統中。

🔗 **論文連結與程式碼**
📝 **MARCH: Multi-Agent Reinforced Self-Check for LLM Hallucination**  
👤 Zhuo Li, Yupeng Zhang, Pengyu Cheng, Jiajun Song, Mengyu Zhou  
🏢 Alibaba Qwen Large Model Application Team & The Chinese University of Hong Kong, Shenzhen  
📄 論文：<https://arxiv.org/abs/2603.24579>  
💻 程式碼：<https://github.com/Qwen-Applications/MARCH>

你對這種三代理論的自我審查方法有什麼看法？歡迎在留言區討論！👇

#AI #LLM #MARCH #Hallucination #RAG #Alibaba #Qwen
