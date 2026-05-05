---
title: "MolViBench: Evaluating LLMs on Molecular Vibe Coding"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.02351
score: 102
model: tencent/hy3-preview:free
generated_at: 2026-05-05T20:04:29.759830
---

📌 【港理工等高校】MolViBench：評測 LLM 的分子程式生成能力

當我們談論 LLM 寫程式，多半聚焦在 HumanEval 或 SWE-bench 這類通用軟體工程任務。但當場景轉向藥物發現，需要 LLM 同時具備「程式設計」、「分子結構理解」與「化學領域推理」三種能力時，現有的評測標準就顯得力不從心。

🤔 **通用程式碼測試無法驗證化學專業**

目前的 Benchmark 存在明顯的斷層。HumanEval 等指標不需要任何化學知識，而 S^2-Bench 等化學測試又僅止於知識回憶或屬性預測，無法評估「可執行程式碼」。這導致一個關鍵問題：當化學家透過自然語言（Vibe Coding）要求 LLM 生成分子篩選流程時，我們該如何評斷模型是真的懂化學，還是只是隨機拼湊 API？

🧪 **358 個任務，橫跨 5 大認知層次**

由香港理工大學、新加坡國立大學與復旦大學團隊提出的 MolViBench，是首個專為 Molecular Vibe Coding 設計的基準測試。它包含 358 個精選任務，從簡單的單一 API 呼叫，到端到端的虛擬篩選（Virtual Screening）流程設計，涵蓋了 12 種真實世界的藥物發現工作流。

 **不只看程式碼跑不跑得通，還要看化學對不對**

論文提出了一個多層次評估框架，這是技術上的一大亮點。它結合了「類型感知輸出比對」與「基於 AST 的 API 語義回溯分析」。這意味著評測不僅關注程式碼是否可執行，更深度檢查 API 的使用語義是否符合化學邏輯。研究團隊系統性評估了 9 個前沿編碼 LLM，並比較了三種真實世界常用的 Vibe Coding 範式，為模型選型提供了細粒度的診斷數據。

💡 **將 LLM 整合進藥物發現流程的診斷工具**

對於正在構建 AI 驅動藥物發現（AIDD）平台的工程團隊而言，MolViBench 提供了一個可落地的測試平台。它揭示了單純的 Code 能力強（如 GPT-4 在 SWE-bench 高分）並不代表在化學領域就能勝任。這促使開發者重新思考：我們的模型是否真的具備跨領域的推理能力？

⚠️ **聚焦藥物發現，通用化學場景待補足**

作為一個專注於特定領域的 Benchmark，MolViBench 目前的任務主要集中於藥物發現工作流，對於材料科學或基礎有機化學的其他分支覆蓋較少。此外，雖然任務設計精細，但 358 個任務相對於龐大的化學空間仍屬有限，且 LLM 的快速迭代也意味著 Benchmark 需要持續更新。

🎯 **選型與優化：別只看通用 Coding 分數**

- 在導入 LLM 進行化學任務自動化時，應參考特定領域的 Benchmark 結果。
- 開發者應關注模型在「API 語義理解」上的表現，而不僅是可執行性。
- 對於需要高度客製化化學流程的場景，MolViBench 提供的診斷維度能直接指導 Prompt 設計與模型微調。

🔗 **論文連結**
📝 MolViBench: Evaluating LLMs on Molecular Vibe Coding
👤 Jiatong Li, Yuxuan Ren, Weida Wang, Changmeng Zheng, Xiao-yong Wei
🏫 The Hong Kong Polytechnic University; National University of Singapore; Fudan University
🔗 論文：https://arxiv.org/abs/2605.02351

你認為目前的 LLM 在處理跨領域（如生物/化學+程式）任務時，最大的瓶頸是什麼？歡迎在留言區討論 👇

#AI #LLM #DrugDiscovery #Bioinformatics #MachineLearning #MolecularVibeCoding #港理工 #NUS #復旦大學
