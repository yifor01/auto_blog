---
title: Gemini 4 Carbon is now available
source: Google DeepMind
url: https://deepmind.google/blog/gemini-4-carbon-is-now-available/
model: claude-code/sonnet
generated_at: '2026-11-11T23:38:45.746033'
score: 129
---

📌 【Google DeepMind】Gemini 4 Carbon上線,主打長程agentic工作與資安能力

TL;DR：Gemini 4 Carbon正式開放,定位為處理複雜多步驟任務的frontier模型,資安基準測試表現突出。

當多數團隊還在用模型處理單輪任務時,Google DeepMind 給出的答案是:把一個提示變成一整個可追蹤的 AI 代理團隊。這就是 Gemini 4 Carbon 與 Google Antigravity 新功能 /swarm 的組合。

🤔 **Argon 與 Carbon 的分工**

繼先前推出的 Gemini 4 Argon 之後,Carbon 進一步推進前沿能力。官方定位很明確:Argon 仍是多數軟體工程與知識工作的首選,而 Carbon 專門用於測試模型智能極限的任務,像是複雜、多步驟的程式碼撰寫與除錯,以及開放式的科學研究——它會用更多 token 來深入探索、推理與執行延伸的驗證迴圈。兩週前,Carbon 已先透過 Fairwind Program 提供給一批資安防禦團隊試用。

📊 **基準測試排名與定價**

在測試真實工作流程的獨立基準上,Carbon 在 CursorBench 4.0、Perplexity 的 WANDR、Zapier 的 AutomationBench 上均排名第一,且每項任務成本比次佳的外部模型低超過兩倍。在與 Artificial Analysis 合作推出的新基準 Multimodal Knowledge Agent(MKA,測試模型在多模態 agentic 工作流程中的表現)上,Carbon 排名第二,平均任務成本卻比表現最佳的模型低六倍以上。在資安能力方面,透過 Fairwind Program 測試,Carbon 在尋找漏洞(SEC-bench Pro)、利用漏洞(ExploitGym)、修補漏洞(CWE-bench v1)三項基準上均領先。在 Google 內部的自動化系統 Project Fortify 中,Carbon 在掃描任務上達到 100% 召回率,在分類(triage)任務上達到 95% 精確率;在開源程式碼庫測試中,相較 Argon 已有的強勁召回率,再提升超過 25%。Gemini 4 Carbon 透過 API 在 Google AI Studio 與 Gemini for business 開放給所有付費開發者與企業,定價與 Argon 相同,每百萬輸入 token 2 美元、每百萬輸出 token 10 美元。

🧩 **/swarm:把提示變成代理團隊**

Google Antigravity 新預覽的 /swarm 功能,讓開發者可以把 Carbon 指派給架構設計、協調、稽核等最需要深度推理的角色,同時搭配更輕量快速的模型在平行、隔離的工作區中執行任務,再由對抗式驗證器(adversarial verifiers)檢查每一次變更。文中展示的案例包括:用七份市政規劃 PDF 與單一提示,重建出一棟辦公室的 3D 模型;以及一個以 Google 園區為場景的開放世界 3D 遊戲。

⚠️ **行銷案例多,架構細節少**

必須指出的是,這篇公告大量展示的是產品案例與基準排名,對 Carbon 本身的模型架構(例如參數規模、訓練方式)幾乎沒有揭露,讀者無法從中判斷其技術實現的具體差異,只能依賴官方提供的基準數字與第三方評測結果做判斷。

🎯 **實務啟示**

如果團隊的工作負載是標準的軟體工程與知識工作,Argon 可能已經足夠;但如果任務本身就在測試模型推理深度的極限(複雜除錯、跨子系統根因調查、大型架構重構),Carbon 搭配 /swarm 的多代理模式值得評估,尤其在資安情境中,Fairwind Program 的早期數據顯示其漏洞掃描與修補能力有實質提升。

🔗 **來源**
- 標題：Gemini 4 Carbon is now available
- 作者／機構：Google DeepMind
- 連結：https://deepmind.google/blog/gemini-4-carbon-is-now-available/

#Gemini4Carbon #GoogleDeepMind #LLM #AIAgents #Cybersecurity #SoftwareEngineering #AgenticAI #GenerativeAI #AIBenchmark #GoogleAntigravity
