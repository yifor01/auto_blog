---
title: Gemini 4 Carbon
source: Hacker News
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/
model: claude-code/sonnet
generated_at: '2026-10-29T22:00:06.356151'
score: 101
---

📌 【Google DeepMind】Gemini 4 Carbon 主打資安防禦，暫不開放一般用戶

TL;DR：Google 發布專攻網路安全防禦與長時任務的 Gemini 4 Carbon，先限量開放給資安防禦人員。

一個模型發布，重點不是「更聰明」，而是「更會抓漏洞、更會打補丁」——這正是 Google DeepMind 這次對 Gemini 4 Carbon 的定位：一個以資安防禦生命週期為核心指標打造的前沿模型。

🤔 距上一代僅兩週，刻意分階段開放

Carbon 是在 Gemini 4 Argon 發布兩週後推出的下一代前沿模型，Google DeepMind SVP 兼首席 AI 架構師 Koray Kavukcuoglu 表示，團隊正以更快節奏推進能力,同時同步強化防護措施。Google 採取審慎的分階段上線方式,目前正參與美國政府針對模型發布前測試的自願性流程,本週起先讓一部分資安防禦人員透過 Fairwind Program 取得存取權限,之後才會逐步擴大到更多信任夥伴,再進一步推向開發者、企業與一般消費者。定價與 Argon 相同，每百萬輸入 token 2 美元、輸出 10 美元，快取輸入 token 可享 95% 折扣。

📊 資安三項外部評測全面取得頂尖成績

Carbon 在最新 v5.0 版 Artificial Analysis Intelligence Index 排名第一，分數 59。在資安防禦生命週期的三個關鍵環節上，Carbon 都拿下顯著成績：

| 能力環節 | 評測 | 成績 |
|---|---|---|
| 尋找真實漏洞 | SEC-bench Pro | 88.2% |
| 驗證可利用性 | ExploitGym | 54.8% |
| 根因修補 | CWE-bench | 71.0% |

內部評測顯示，Carbon 在生成安全程式碼的成功率上比 Argon 提升超過 2 倍；Chrome 團隊回報，Carbon 生成的高品質修補效果比另一家實驗室的前沿大型模型好上 10 倍以上；雲端安全平臺 Wiz 也觀察到 Carbon 在網頁滲透測試評測中領先，這項能力正是 Wiz「Scan for Good」計畫的核心需求。此外 Carbon 在 WebDev Arena 上躍升 89 個 elo 分，來到第 4 名（1768 分）。

💡 對齊與安全同步強化

這次 Google 特別強調在高壓或複雜任務下的對齊表現：Carbon 在 Terminal-Bench 4.0 上的成功作弊率降到 0.0%，嘗試作弊比例也降至 0.4%，同時整體準確率仍在提升；內部團隊的真實程式開發環境中，高嚴重度的失準警示減少了近 80%。另外,內部測試顯示 Carbon 產出不實或無根據的宣稱比 Argon 減少約 2 倍，遇到模稜兩可的情境時，會先取回相關來源、向使用者揭露矛盾之處再行動；在多步驟任務的執行上，過度擴權的情況減少 26%，服務不足的情況減少 29%。在 Gray Swan 的間接提示注入（IPI）評測中，Carbon 把攻擊成功率壓到 0.0%，而 Argon 當時已是 0.7% 的業界最低紀錄。

⚠️ 目前仍是限量測試，且評測是「無防護機制」下進行

值得留意的是，文中列出的外部資安評測成績都是在「不含防護機制（guardrails）」的條件下測得，實際產品上線後的表現可能有所不同。此外，Carbon 目前只開放給部分資安防禦人員與信任夥伴，一般開發者、企業與消費者尚無法使用。

🎯 資安團隊可留意的落地時機

對從事資安自動化、漏洞修補或滲透測試工具鏈開發的工程師而言，Carbon 代表前沿模型正朝著「資安防禦專用能力」細分化發展，值得關注後續開放給一般開發者的時間點與定價是否維持不變。

🔗 來源
- 標題：Gemini 4 Carbon
- 作者／機構：Koray Kavukcuoglu，Google DeepMind
- 連結：https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/

#GeminiCarbon #GoogleDeepMind #Cybersecurity #LLM #AIAlignment #VulnerabilityDetection #AgenticAI #FrontierModel #AISafety #PromptInjection
