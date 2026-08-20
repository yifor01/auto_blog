---
title: How to Answer AI System Design Interview Questions
source: KDnuggets
url: https://www.kdnuggets.com/how-to-answer-ai-system-design-interview-questions
model: claude-code/sonnet
generated_at: '2026-08-20T06:33:31.096064'
score: 90
---

📌 面試題從「設計 YouTube」變成「設計 ChatGPT」，你答得出來嗎？

TL;DR：AI 系統設計面試考的不是 LLM API 怎麼呼叫，而是延遲、成本、品質與安全之間的取捨，這裡是一套可重複套用的七步框架。

多年來系統設計面試的固定題目是「設計 YouTube」「設計 Uber」「設計 WhatsApp」，如今招募 AI Engineer、Applied Scientist、GenAI Engineer 的公司，換成了「設計 ChatGPT」「設計客服 AI」「設計 GitHub Copilot 」「設計 AI 程式碼審查工具」。多數工程師都能呼叫 LLM API，但能解釋周邊架構、並在壓力下捍衛設計決策的人少得多，而這正是這輪面試真正在測的能力。

🤔 為什麼題目換了

AI 相關職缺成長快到重塑了整個面試流程。根據引用的資料，AI Engineer 連續兩年被列為美國成長最快的職缺第一名，2025 年職缺數年增 143%；LinkedIn 的數據顯示，2023 到 2025 年間美國新增 75,000 個相關職缺，AI／ML 職缺佔科技市場比重從 10% 升到 50%。隨著量能上升，題目也轉向「AI-first 軟體」：如何把 LLM 包裝進產品，設計 agentic loop、整合 retrieval、權衡成本，模型內部原理的重要性反而下降。

🧩 一套框架，套用所有「設計 X」題目

面試官通常會挑 3 到 5 個面向深入追問「上次哪裡出錯」，而不是每個主題都蜻蜓點水，真正拉開差距的是候選人有沒有實際上線過系統的經驗。文中整理出的框架分七步：

1. 釐清（Clarify）：資料來源、隱私規則、延遲預算、對事實錯誤的容忍度、預期規模、新鮮度需求，以及能否呼叫第三方 API 或必須自架。
2. 估算（Estimate）：每秒 token 數、context window 大小、embedding 量、每次呼叫成本、尖峰 QPS。
3. 架構草圖：一個穩健的預設架構依序是輸入層 → 安全與 PII 層 → orchestrator → retrieval（向量資料庫加 reranker）→ 依任務難度路由的模型 → LLM 後守門機制 → 回應串流 → observability。
4. 深挖（Deep dive）：挑一兩個元件深談，例如 RAG 策略（chunking、BM25 混合密集檢索、reranking）、prompt 設計、快取（精確與語意快取）、模型分層。
5. 取捨（Trade-offs）：明確講出延遲 vs 品質、RAG vs fine-tuning、成本上限、容量吃緊時的備援模型。
6. 失敗模式與 observability：幻覺、prompt injection、供應商中斷、embedding 漂移、多租戶隔離，以及各自的偵測方式。
7. 演進（Evolution）：A/B 測試 prompt、回饋迴路、上線前的 eval gate、漸進式模型遷移。

文中最常被提到的失敗，是還沒釐清需求、限制與成功標準就急著給方案，第一步務必花足夠時間。

💡 五個必須答得出來的核心元件

- **RAG**：核心是 query encoder、retriever、generator 三件事，生產環境還要加上文件 chunking、embedding pipeline、向量檢索、快取、評估日誌，並確保使用者拉不到不該存取的資料。RAG 本身能把幻覺降低約 40% 到 71%。
- **模型路由（Model Routing）**：GPT-4 等級模型每百萬 input/output token 約 10 美元／30 美元，回應延遲 3 到 5 秒，一個每天處理一萬則對話、每則五千 token 的 agent 若全用單一供應商，月費會衝破 7,500 美元。由於 60% 到 80% 的請求屬於例行性問題，把簡單請求導向便宜模型、留給前沿模型處理難題，通常能省下 40% 到 70% 成本；結合路由、語意快取、prompt 壓縮與串流，可在維持品質下砍掉 40% 到 60% 的整體成本。
- **Guardrails**：分兩層，LLM 之前處理輸入驗證、PII 遮蔽與 prompt injection 防禦，LLM 之後處理 schema 檢查、拒答政策與對照檢索內容的事實查核。多層 guardrails（系統提示、RAG grounding、引用強制、信心分數、監控）能把幻覺風險從基準的 3% 到 20%，降到 71% 到 89% 的降幅範圍。
- **評估與 Observability**：記錄模型版本、檢索 metadata、工具呼叫軌跡、安全決策、延遲與每請求成本，用 prompt hash 而非原文避免隱私問題；離線評估（用 LLM-as-judge 對照人工標註校準）搭配線上指標（faithfulness、context recall、answer relevance）並用。
- **Agentic Loop**：流程是請求接收 → context 組裝 → LLM 推理 → 動作驗證 → 沙箱執行 → 結果處理 → 狀態更新 → 迴圈或停止，關鍵是職責分離：LLM 負責推理、orchestrator 控制流程、policy engine 治理、沙箱負責執行。

🎯 引用真實系統，展現你讀過的不只是教學文

能說出真實系統細節，勝過只會畫通用架構圖。GitHub Copilot 的 IDE extension 會抓遊標前後的程式碼、開啟的檔案、import 與語言 metadata 組成 prompt，用 Fill-in-the-Middle（FIM）技術補齊鄰近分頁與檔案路徑後送到後端，FIM 相較純前綴 prompting 能帶來約 10% 的相對採用率提升，GitHub 另外還跑一個獨立模型為補全結果做品質與安全評分。其他值得一提的系統包括 Uber 的 GenAI Gateway（涵蓋 60 多個用例的 PII 遮蔽層）、Airbnb 帶 chain-of-thought 與 guardrails 的對話式 AI、Perplexity 用 Vespa.ai 支撐每日兩億次查詢、Slack 在 escrow VPC 中運行模型的無狀態 RAG，以及 Anthropic 由 Opus 當 orchestrator、Sonnet 當 subagent 的多代理研究系統。

🔗 來源
- 標題：How to Answer AI System Design Interview Questions
- 作者／機構：Nate Rosidi，KDnuggets
- 連結：https://www.kdnuggets.com/how-to-answer-ai-system-design-interview-questions

#SystemDesign #AIEngineering #TechInterview #RAG #LLM #ModelRouting #Guardrails #AIAgents #GenAI #Career
