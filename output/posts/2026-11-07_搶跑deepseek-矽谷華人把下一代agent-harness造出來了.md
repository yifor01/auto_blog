---
title: 搶跑DeepSeek！矽谷華人把下一代Agent Harness造出來了！？
source: 量子位
url: https://www.qbitai.com/2026/11/508264.html
model: claude-code/sonnet
generated_at: '2026-11-07T21:03:11.317633'
score: 78
---

📌 DeepSeek才喊出Super-agent，矽谷團隊半年前已落地

TL;DR：DeepSeek 提出 Super-agent 架構願景之際，矽谷團隊 Comma 早已用 Router＋Worker 架構實際運行近半年。

當一個 AI 可以同時推進一千、一萬，甚至十萬個任務時，瓶頸會變成誰？答案可能不是算力，而是人類自己的注意力。

🤔 **人只能同時盯 3 到 5 個 Session，Agent 卻能無限併發**

DeepSeek Harness 團隊近日發文，針對這個落差提出下一代「Super-agent」的架構設想：一個擁有連續上下文、能自主排程多個 agent 平行工作、甚至 7×24 小時在線的超級智慧體，把人類的注意力從多工排程中解放出來。他們為此提出四大標準——連續、高效、主動、持久：連續代表記憶與上下文貫通，高效來自多個 worker 並行協作，主動代表 agent 能自主推進任務，持久則支撐長期在線與自主修復。

🧩 **巧合的架構共識：單 Session + Router（主腦）+ 多 Worker（執行者）**

就在 DeepSeek 文章引發熱議的同時，矽谷華人團隊 AFK AI 的產品 Comma 被重新「看懂」——因為它早在半年前，就把類似的架構裝進了自己的產品。Comma 底層採用「單 Router＋多 Worker」設計：一個常駐 Router 統一接收使用者指令、統籌全域調度，多個擁有獨立上下文的 Worker 在背後並行執行任務、回報結果，使用者只需要面對一個長期存在的主對話框，這也是團隊提出的理念——「一個團隊，一個對話」。

跨環境能力則依託團隊自研的分散式 Agent 執行框架「Salix」：透過第三方應用連接器接收不同平臺的事件，由可程式設計的 Loop 持續監聽，需要時再喚醒 Agent 處理。目前打通的通訊與協作工具包括微信、Signal、iMessage、Linear，並支援安全自部署、BYOK，以及接入 Codex、Claude Code。在記憶管理上，Comma 把長期狀態存在模型上下文之外，讓 Router 與獨立 Worker 分工，避免海量任務細節不斷擠佔主對話；更進一步，系統會把 Agent 的任務結果、人工修改與驗收回饋轉化為訓練訊號，持續迭代團隊自己的小模型，且新模型必須在內部測試中勝過舊版本才能正式上崗——報導中舉的例子是，v3 模型曾把退款請求誤判為 Bug，在學習人工糾正後，升級到 v4 便能正確識別為帳務問題。

📊 **從 Bridge 到 Comma 的半年時間軸**

- 2026 年 4 月 28 日：團隊公開 Comma 的前身「Bridge」，介面已出現 Lead Agent（主 Agent）與 Subagents（子 Agent）的架構設計。
- 5 月 20 日：明確「每個群組一個 Router Session」。
- 6 月 3 日：固定主對話與任務委派機制正式上線（文中提到約 20 天後，Anthropic 推出理念相近的 Claude Tag，讓同一個 Slack 頻道共享同一個 Claude）。
- 8 月：推進 Session 切換能力。
- 9 月：引入共享 Session 的資訊流控制機制。
- 9 月 30 日：Comma 正式開源，隨後公開基於 Lean 形式化驗證的安全機制。

💡 **兩岸團隊「不謀而合」，但敘事多來自團隊自述**

報導認為，DeepSeek 與 AFK AI 在架構上殊途同歸，反映出業界對 Agent Harness 的期待正從「任務吞吐量」轉向「能承接的責任與複雜事務量」。不過要留意的是，本文大量內容來自作者本人實際使用 Comma 的主觀體驗（例如請 Comma 做遊戲 demo、整理週報），以及團隊自述的時間軸與模型迭代案例，並非第三方的獨立驗證結果。

⚠️ **具體效能與驗證細節仍不透明**

文中沒有提供 Comma 回應延遲、並發規模、小模型迭代所用評測集大小，或 Lean 形式化驗證具體覆蓋範圍等可驗證的量化數據，這些描述目前仍停留在產品敘事層面。

🎯 **實務啟示**

如果要設計長期自主運作的個人或團隊 Agent 系統，Router 統籌＋Worker 並行執行、把長期記憶移出主 context、以及「新模型必須先打贏舊模型才能上線」這類安全迭代機制，都是值得參考的設計思路。

🔗 **來源**
- 標題：搶跑DeepSeek！矽谷華人把下一代Agent Harness造出來了！？
- 作者／機構：田、晏林（量子位）
- 連結：https://www.qbitai.com/2026/11/508264.html

#AIAgent #SuperAgent #DeepSeek #MultiAgent #AgentHarness #LLMOps #PersonalAgent #AIProductivity #AgentMemory #AIInfrastructure
