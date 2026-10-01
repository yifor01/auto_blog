---
title: Google DeepMind Unveils Gemini 4 Argon with 1M Output Tokens for Coding, Knowledge
  Work and Cyber Defense
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/30/google-deepmind-unveils-gemini-4-argon-with-1m-output-tokens-for-coding-knowledge-work-and-cyber-defense/
model: claude-code/sonnet
generated_at: '2026-10-01T22:02:28.280095'
score: 97
---

📌 Google DeepMind 發布 Gemini 4 Argon：單次輸出衝上 100 萬 token

TL;DR：輸出長度從 64K 跳到 1M token，長任務不用再被迫分段處理。

寫過大型重構或長篇報告的工程師都知道那種痛：模型輸出長度一到上限，就得把任務硬生生切成好幾輪對話，自己手動把上下文接回去。Google DeepMind 剛發布的 Gemini 4 Argon，把這個瓶頸直接往前推了 15 倍。

🤔 **被忽略的瓶頸：輸出長度，不是輸入長度**

Argon 是 Gemini 4 世代的第一個模型，鎖定長時間的軟體工程任務、企業知識工作（法務、財務）以及資安防禦這三個場景。Google DeepMind 表示 Argon 是為「複雜工作流程」打造的。目前主流前沿 API 的單次回應輸出上限都相當保守：Claude Opus 5.5、Claude Fable 5.1 與 GPT-6 Astra 都是 128K token。而 Argon 能在單一回應中生成最多 1M token，是前代 Gemini 模型 64K 上限的大幅躍進。Google 團隊的說法是，Argon 可以「深度思考」並在單一軌跡中產出數十萬 token，對開發者而言意味著大型重構或長報告可以一次做完，不必再跨回合拼接。

不過代價也很直接：以優惠價計算，跑滿 1M 輸出 token 要價 10 美元，優惠期結束後變成 20 美元。Google 目前尚未公開 Argon 的輸入 context window 大小。

🧩 **定價與釋出策略：先限量測試，再逐步開放**

Argon 的定價已經公開：優惠期為每 1M 輸入 token 2 美元、每 1M 輸出 token 10 美元；快取輸入 token 享 95% 折扣，換算下來只要每 1M 0.10 美元。優惠期結束後，價格會調整為輸入 4 美元、輸出 20 美元。Google 的 Logan Kilpatrick 已證實這組優惠期定價。

釋出節奏上，Google 採取分階段策略：先參與美國政府的「自願式」模型預發布存取計畫，蒐集早期測試者的回饋，並在更大規模釋出前持續迭代安全防護機制。

📊 **效能與成本：12/18 項基準測試領先，成本只要六成**

Google 將 Argon 與 GPT-6 Astra、Claude Opus 5.5、Claude Fable 5.1 做了比較，結果是在 18 項基準測試中 Argon 在 12 項全面領先、1 項並列第一。第三方機構 Artificial Analysis 指出，以折扣價計算，Argon 在 Intelligence Index 上與 GPT-6 Astra 打平，但每個任務的成本只要對手的六成。

在資安面向，Google 訓練 Argon 自主發現、驗證並修補關鍵軟體漏洞，並讓受信任的防禦方與 Google 內部團隊在沒有資安護欄限制的情況下使用。在專門測試漏洞修復能力的 CWE-bench v1 上，Argon 以 68% 的成績並列第一，而對手模型在這項測試中是跑在各自的 agent harness 裡。資安公司 Wiz 已經透過其 Scan for Good 計畫使用 Argon，並藉此在全球醫院廣泛使用的醫療軟體中發現一個關鍵漏洞，Google 表示先前的前沿模型都沒能找出這個漏洞。

Google 也提到目前已有數千名 Google 員工在內部使用 Argon，並表示會在更大規模釋出前持續強化安全防護措施。

🎯 **實務啟示**

對日常要處理大型程式碼庫重構、產出長篇法務／財務分析報告的工程團隊來說，1M 輸出 token 代表「一次做完」而不是「分段拼接」，可以省下大量管理上下文與重新餵入歷史的工程成本。但 20 美元（優惠後）或 10 美元（優惠期）的單次滿輸出成本也不低，實務上仍需評估任務是否真的需要如此長的單次輸出，或是用快取輸入搭配來控制成本。

🔗 **來源**
- 標題：Google DeepMind Unveils Gemini 4 Argon with 1M Output Tokens for Coding, Knowledge Work and Cyber Defense
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/30/google-deepmind-unveils-gemini-4-argon-with-1m-output-tokens-for-coding-knowledge-work-and-cyber-defense/

#GeminiArgon #GoogleDeepMind #LLM #AICoding #CyberDefense #AgenticAI #FrontierModels #AIInfrastructure #SoftwareEngineering #AIAgents
