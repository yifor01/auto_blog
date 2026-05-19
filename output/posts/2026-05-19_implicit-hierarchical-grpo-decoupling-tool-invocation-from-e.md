---
title: "Implicit Hierarchical GRPO: Decoupling Tool Invocation from Execution for Tool-Integrated Mathematical Reasoning"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.18500
score: 124
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:20:40.583288
---

📌 【Meituan】解耦工具調用，數學推理提升 2.5%

你以為讓大模型邊想邊用工具就能變得更強？研究卻發現，這種「即時調用」反而可能打斷模型的思考連貫性。

🤔 **工具即時執行可能削弱推理連貫性**

現有的工具整合方法往往把「呼叫工具」與「立即執行」綁在一起。這種設計雖方便，但會在模型推理的中途插入外部操作，導致思路被中斷，表達空間受限，最終影響推理表現。

🧪 **先提出「延遲執行」概念，再建立階層控制框架**

論文首次形式化了「將工具呼叫與執行分離」的問題，並提出延遲執行機制。在此基礎上，設計了一個階層控制框架，並理論推導出一個 surrogate loss，使得隱式階層政策（IH‑GRPO）能學習與顯式階層政策等價的行為。

 **在 Qwen3 系列模型上取得 1.87%~2.53% 的絕對提升**

在六個領域外的數學推理基準上，IH‑GRPO 分別在 Qwen3‑1.7B、Qwen3‑4B、Qwen3‑8B 上比最強基線高出 1.87%、2.16%、2.53%。此外，該方法在其他領域也帶來穩定的性能改善。

💡 **解耦讓模型能更專注於推理本身**

透過把工具呼叫視為高階決策，而把實際執行延後，模型在推理階段能保持更完整的思考鏈。階層控制則讓低層專注於工具使用細節，高層負責何時與如何呼叫工具，兩層之間透過 surrogate loss 進行隱式協調。

⚠️ **僅在數學推理與少數其他領域驗證，長期穩定性尚未探討**

實驗主要聚焦於六個領域外的數學推理基準以及少數其他領域，未涵蓋更廣泛的任務集合。此外，論文未報告長期對話或連續使用情況下的表現變化。

🎯 **工具使用時可考慮「先決策後執行」的設計**

在構建 LLM‑Agent 或工具增強系統時，可將工具的呼叫決策與實際執行分離：先讓模型規劃要使用哪些工具、何時使用，再由外部執行器統一處理。這種設計有助於保持推理的連貫性，同時仍能獲得工具帶來的能力提升。

🔗 **論文連結**  
📝 Implicit Hierarchical GRPO: Decoupling Tool Invocation from Execution for Tool‑Integrated Mathematical Reasoning  
👤 Li Wang, Xiaohan Wang, Xiaodong Lu, Zipeng Zhang, Jinyang Wu @ Meituan; Tsinghua University  
🔗 論文：https://arxiv.org/abs/2605.18500  
💻 程式碼：https://github.com/Lumina04/IH-GRPO-01  

你在設計工具增強模型時，是否也曾感覺到即時執行會打斷思考？歡迎在留言區分享你的經驗與想法 👇

#AI #LLM #ToolUse #MathematicalReasoning #Meituan #Tsinghua #GRPO #AgenticAI
