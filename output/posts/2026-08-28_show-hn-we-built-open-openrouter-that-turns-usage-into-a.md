---
title: 'Show HN: We built open OpenRouter that turns usage into a better model'
source: Hacker News
url: https://github.com/experientiallabs/experiential
model: claude-code/sonnet
generated_at: '2026-08-28T18:02:47.739795'
score: 92
---

📌 開源版 OpenRouter？這個 Rust 閘道想用你的流量幫你練出專屬模型

TL;DR：Experiential 是開源模型閘道,整合上千個模型並零加價,還能用你的使用資料訓練專屬模型。

市面上的模型路由服務大多會在每筆呼叫上抽成,而且你的使用資料通常只是幫別人優化系統。這個 Show HN 專案想反其道而行：開源、零加價,還把你的流量變成訓練你自己模型的素材。

🤔 **管理自架、前沿與開源模型的統一入口**

作者在 Show HN 貼文中指出,團隊打造了一個開源的模型閘道（model gateway）,作為統一管理自架模型、前沿模型與開源模型的單一入口。他們指出,目前串接不同模型與供應商時,得處理各種設定上的差異，例如串流格式、tool call 呼叫方式、模型參數、rate limit 與各家不同的錯誤處理行為，這些瑣碎但麻煩的相容性問題正是這個閘道想解決的。

🧩 **Rust 原生打造,鎖定併發效能與低延遲**

這個閘道以 Rust 撰寫,目標是應付高併發場景。作者表示,採用自帶金鑰（BYOK）模式時,閘道只會增加不到 1 毫秒的延遲；若由 Experiential 提供供應商金鑰,延遲則低於 2 毫秒。專案宣稱涵蓋所有主要推論供應商,並整合超過 1,000 個模型,透過一個 codex agent 每天自動開 PR 更新模型清單。

路由邏輯的核心做法是：先用標準化的 OpenTelemetry（OTel）追蹤資料,挖掘出具代表性的真實任務,接著用文字世界模型（text world models）模擬不同模型在這些任務上的執行結果（rollout）,再套用 LLM 作為評審（LLM judge）給分,最後在提示詞的 embedding 之上訓練一個最近鄰（nearest neighbor）分類器,決定每次請求該路由到哪個模型。

📊 **與同類服務的差異：零加價、可混用本地模型、選擇性訓練**

作者強調,相較於其他類似專案,Experiential 是開源的、不收取加價費用,允許使用者混合自架模型與市集（marketplace）模型,並可選擇性地（opt-in）用自己的流量訓練專屬模型。基於前述的模擬機制,系統也能進一步提供快取命中最佳化建議、新模型推薦等附加功能。

⚠️ **路由效果並非萬無一失**

作者坦言,這套路由機制「通常」能在成本與品質之間畫出比單一模型呼叫更好的柏拉圖曲線（Pareto curve）,但「並不完美」,實際效果會依任務與流量特性而異。

🎯 **實務啟示**

如果你的團隊正在自建或評估 LLM 路由層,且在意供應商相容性瑣事與加價成本,可以考慮自行部署這個開源閘道,或先用其零加價的託管版本測試路由品質是否符合預期，再決定是否要啟用「用流量訓練專屬模型」這類進階功能。

🔗 **來源**
- 標題：Show HN: We built open OpenRouter that turns usage into a better model
- 作者／機構：SilenN（Hacker News / Experiential Labs）
- 連結：https://github.com/experientiallabs/experiential

#OpenSource #LLMGateway #ModelRouting #RustLang #OpenTelemetry #AIInfrastructure #LLMOps #MachineLearning #DeveloperTools #ModelTraining
