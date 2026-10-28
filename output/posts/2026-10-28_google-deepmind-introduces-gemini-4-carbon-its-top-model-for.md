---
title: Google DeepMind Introduces Gemini 4 Carbon, Its Top Model for Cyber Defense
  and Coding
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/28/google-deepmind-gemini-4-carbon-frontier-model/
model: claude-code/sonnet
generated_at: '2026-10-28T21:50:36.952931'
score: 101
---

📌 Google DeepMind 發布 Gemini 4 Carbon：專攻網路防禦與長時任務 coding 的頂尖模型

TL;DR：Carbon 在 v5.0 Artificial Analysis Intelligence Index 拿下第一，但目前只開放給受信任的網路防禦人員。

一個模型能連續跑好幾天只做一件事：在大型程式碼庫與底層系統中找出並修補細微的 bug。這是 Google DeepMind 團隊對 Gemini 4 Carbon 內部測試的描述，而這款模型現在卻幾乎沒人能用到。

🤔 **繼 Argon 之後的第二個 Gemini 4 模型**

Gemini 4 Carbon 是 Google 目前最強的前沿模型（frontier model），專為長時程（long-horizon）agentic coding 與網路安全防禦打造。它在更新後的 v5.0 Artificial Analysis Intelligence Index 上以 59 分排名第一。Carbon 是第二個 Gemini 4 模型，前一個是 Gemini 4 Argon。Google 團隊表示，這款模型針對困難、長時間運行的工程工作而設計，內部團隊觀察到 Carbon 能針對單一任務連續運行數天，例如在大型程式碼庫與底層系統中定位並修補細微錯誤。Google 也針對全端網頁開發與多模態理解對 Carbon 做了調整，在 WebDev Arena 上 Carbon 的 Elo 分數提升 89 點，來到第 4 名、1769 分。

📊 **多項 Benchmark 領先，方法論需留意**

Google 在發布文章中公布了 17 項對照數據，Carbon 是以最高 thinking 設定運行，而大多數對手的數字是各家自行回報（依 Google 的評估方法論）。在 agentic coding 方面，Carbon 在 Terminal-Bench 4.0（AA）拿下 65.2%，領先 Opus 5.5 的 59.6%；在 SWE-sweep 上以 9.6% 些微領先 GPT-6 Astra 的 9.5%；但在 FrontierSWE 上，GPT-6 Astra 以 65.5% 領先 Carbon 的 61.2%。在電腦操作與知識工作方面，Carbon 在 Agents' Last Exam v1.1 拿下 77.4%，在 Vending-Bench 2 的模擬中以 16,484 美元的銀行餘額位居所有列出模型之首。長文本與科學類別中，GraphWalks 差距最大：Carbon 96.2% 對比 GPT-6 Astra 的 71.8%，另外在 RiemannBench 拿下 80.0%。

🧩 **網路防禦：找漏洞、驗證、修補的完整流程**

Google 將 Carbon 圍繞「尋找、驗證、修補」的完整防禦生命週期打造。網路安全相關的 Benchmark 是在沒有防護機制（guardrails）的情況下進行評估，SEC-bench Pro 與 ExploitGym 的分數是 Google 用自家 Antigravity harness 自行計算，其中 ExploitGym 是在關閉緩解機制（mitigations off）的狀態下執行。內部測試顯示，Carbon 在生成安全程式碼方面的成功率比 Argon 高出 2 倍以上。Google 團隊表示，Chrome 團隊發現 Carbon 在產出高品質修補程式方面，比另一家實驗室的模型強 10 倍以上；Wiz 則回報 Carbon 在其網頁滲透測試 Benchmark 中領先。Carbon 延續了 Argon 的分層防護架構，包括訓練階段防護、即時濫用防禦、提示注入（prompt-injection）韌性，以及思維鏈（chain-of-thought）監控。

⚠️ **目前幾乎沒人能用**

這些都是 Google 自家內部或自行執行的數據，目前尚無獨立覆現結果。存取權方面，Google 正參與美國政府的自願性發布前測試流程，本週僅有一小部分網路防禦人員獲得存取權，更多受信任的合作夥伴將透過 Fairwind Program 陸續加入，該計畫優先提供給政府機構、關鍵基礎設施營運商與核心科技平臺。一般開發者、企業與消費者要等到之後才能使用，Google 未公布具體時間。價格沿用 Argon 的早鳥價：輸入每百萬 token 2 美元，輸出每百萬 token 10 美元，快取輸入享 95% 折扣，早鳥期結束後將漲至 4 美元與 20 美元。

🎯 **實務啟示**

Carbon 展現的是「頂尖效能」與「可用性」之間的落差，目前多數工程師連 API 都摸不到，只能先關注其公開的架構理念（找漏洞→驗證→修補的完整流程，以及分層防護設計），作為未來 agentic coding 與安全工具設計的參考方向；真正能上手測試，恐怕要等開放範圍擴大之後。

🔗 **來源**
- 標題：Google DeepMind Introduces Gemini 4 Carbon, Its Top Model for Cyber Defense and Coding
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/28/google-deepmind-gemini-4-carbon-frontier-model/

#GoogleDeepMind #Gemini4Carbon #AgenticCoding #CyberSecurity #FrontierModel #LLM #AIforSecurity #SoftwareEngineering #AIBenchmark #AISafety
