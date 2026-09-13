---
title: 'Real-SWE: Benchmarking AI models on private, real-world, enterprise codebases'
source: Hacker News
url: https://withspecific.com/benchmarks/real-swe
model: claude-code/sonnet
generated_at: '2026-09-13T19:39:22.874266'
score: 82
---

📌 私有企業程式碼庫實測：頂尖模型解題率不到四成

TL;DR：新benchmark Real-SWE用真實企業私有程式碼庫測試coding agent，目前排名第一的模型組合解題率也僅38.8%。

在公開benchmark上戰績亮眼的coding agent，換到一間陌生公司的正式production程式碼庫裡，還能維持一樣的水準嗎？Real-SWE給出的答案並不樂觀。

🤔 為什麼需要一個「私有」benchmark

Specific團隊（Snagnik Das、Siddhant Paliwal、Janak Sunil）發布Real-SWE，這是一個以私有、真實企業程式碼庫評測前沿AI模型的benchmark。每個任務都取自向真實公司授權取得的正式production程式碼庫，是這些公司工程師實際要處理的問題，帶著既有產品的完整脈絡與複雜度。團隊認為，專家設計或合成出來的任務可以做得很精緻，但終究不是真實公司工程師逐字要處理的任務。

🧩 三個既有benchmark較少觸及的面向

Real-SWE鎖定三個特性：私有程式碼庫，agent必須面對網路上找不到程式碼與解法的專屬系統；有實際商業後果的任務，例如把帳單計費、稅務計算、客戶遷移做對；以及公司特有的複雜度，每間公司都有自己的規則與寫程式方式。範例任務之一，是修正一個以NestJS、TypeScript寫成的服務裡的發票計費邏輯，需要依照不同企業各自的結稅方式正確課稅，並串接TaxJar sandbox／production與InfluxDB帳本等外部服務。整體任務環境涵蓋AWS模擬器、Docker、Kubernetes、GitHub、Linear MCP、PostgreSQL、MySQL、MongoDB、Gel、Redis，以及Go、Python、Node.js、Vitest、Slack、Intercom、Google Drive、Email、ClickUp等工具與服務，且每個任務只開放該任務工作流程實際需要用到的服務。程式碼庫的挑選聚焦有相當使用規模與強大工程團隊的真實公司，包括一個擁有20萬以上用戶、App Store排名前100的類Luma／Partiful社交活動平臺，一個處理超過10萬份銀行對帳單的消費金融平臺，以及支援複雜商業流程的企業AI銷售平臺。Real-SWE採用各模型的原生harness進行評測，而不是把模型單獨拿出來測，用意是貼近企業工程師實際的工作方式。

📊 第一名解題率38.8%，且短任務失敗率一樣高

目前公布的leaderboard中，Fable 5.1搭配Claude Code的解題率（resolution rate，等同pass@1，每個任務跑8次獨立rollout取平均）最高，為38.8%；其後依序是GPT-6 Astra／Codex CLI（33.8%）、Gemini 3.8 Flash／Gemini CLI（31.2%）、GLM 5.3／Claude Code（28.8%）、並列第五的Grok 4.6／Grok Build與Muse Spark 1.3／Muse Code（皆為23.8%）、Kimi K3／Kimi Code（18.8%），最後是GPT-5.6 Sol／Codex CLI（16.2%）。即使是排名第一的組合，解題率也不到四成。團隊也統計了任務的複雜度指標：Real-SWE的指令長度中位數為1,742字元，介於FrontierCode（2,056字元）與DeepSWE（1,975字元）之間，高於Terminal-Bench 3（1,584字元）與FrontierSWE v2（992字元）；參考解答修改的檔案數中位數則達11個，明顯高於FrontierCode與DeepSWE的6個。另外，執行時間在10分鐘以內的rollout有71.4%以失敗收場（98次中70次失敗），執行時間10分鐘以上的rollout失敗率也有73.4%（542次中398次失敗），兩者相差不大。

💡 失敗多半發生在理解階段，而非執行深度不足

短rollout與長rollout的失敗率幾乎持平，這點頗值得玩味：如果失敗主要來自任務太難、需要更長推理，長rollout失敗率理應明顯偏低。但數據顯示不是這樣，這意味著許多失敗其實發生在早期，模型在釐清多個系統、理解既有商業邏輯與公司程式碼慣例的階段就已經卡關，而不是執行到後段才力有未逮。

🎯 實務啟示

對正在評估或導入coding agent的團隊來說，公開benchmark成績只能當參考基準，實際導入前最好用自己的私有程式碼庫與真實任務做一輪驗證；同時Real-SWE揭露的檔案數與失敗率數據也提醒，設計agent workflow時應該特別強化對既有商業邏輯與跨系統依賴的理解能力，而不只是一味加大模型規模或延長執行時間。

🔗 來源
- 標題：Real-SWE: Benchmarking AI models on private, real-world, enterprise codebases
- 作者／機構：Snagnik Das, Siddhant Paliwal, Janak Sunil
- 連結：https://withspecific.com/benchmarks/real-swe

#CodingAgent #Benchmark #SoftwareEngineering #LLM #AIAgents #EnterpriseAI #DeveloperTools #AIEvaluation #MachineLearning #RealSWE
