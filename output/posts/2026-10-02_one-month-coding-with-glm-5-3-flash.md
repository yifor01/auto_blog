---
title: One month coding with GLM 5.3 Flash
source: Hacker News
url: https://wagtail.org/blog/one-month-on-glm-53-flash/
model: claude-code/sonnet
generated_at: '2026-10-02T21:38:26.865737'
score: 85
---

📌 開源模型挑戰：GLM 5.3 Flash用一個月後學到的事

TL;DR：Wagtail團隊挑戰整月只用開源模型GLM 5.3 Flash，結果意外燒掉遠超預期的能源與成本，教訓比省錢更珍貴。

把整個九月的日常開發都押在單一高效開源模型上，聽起來是個漂亮的控制變因實驗。但2B個token燒完之後，故事走向完全不一樣。

🤔 一場「只用一個模型」的實驗

Wagtail團隊設定九月目標：全部工程工作只用GLM 5.3 Flash這顆高效開源模型，並透過AgentsView追蹤token流向、成本與能源消耗。前半個月表現亮眼，穩定控制在預算內（約68美元、4kWh電力、365公克碳排放）。

📊 後半個月失守，1B token跑去別的模型

整個月2B token裡，最終只有一半、約1B token留在目標模型上，其餘1B流向了其他模型。問題出在兩個地方：一是一個「氛圍編程（vibe coding）」的Wagtail MCP伺服器原型，選錯模型後幾乎一夜燒掉450M token、150美元、5kWh電力，團隊事後估算同樣成果換個更合適的模型，成本或許能省下約五倍；二是推理供應商的基礎設施容量問題，GLM 5.3 Flash因為太熱門（在他們工作所需模型的帕雷托前緣上名列前茅），出現效能degradation,團隊被迫切換到DeepSeek V4.1 Flash、Qwen 3.8 Flash等替代模型。

💡 省錢之外，實驗本身也要花錢

團隊也指出，除了日常工程的「省模型」策略，持續用大量不同模型做實驗與基準測試(替Wagtail相關任務建立跨模型benchmark)同樣是必要成本，這樣才能用具體數據引導使用者選擇更精簡的選項，也有助於agent skills與新CLI原型的推廣。最終結算，這個月用了約35kWh能源，而不是原訂目標的10kWh，以挑戰本身而言technically算是失敗。

🎯 給工程團隊的實務啟示

持續、在地化地量測使用狀況，不只看token數，還要看能源消耗、花費與實際產出的關聯;幫實驗與原型開發單獨編列預算，不要跟日常任務混在一起算;導入分工更細的多代理模式(orchestrator、scout、implementer、reviewer)搭配有邊界的目標設定，避免模型選錯導致成本失控;日常開發完全可以仰賴一兩個「flash級」平價模型打天下。

🔗 來源
- 標題：One month coding with GLM 5.3 Flash
- 作者／機構：ThibWeb
- 連結：https://wagtail.org/blog/one-month-on-glm-53-flash/

#GLM53Flash #OpenSourceAI #AIEngineering #LLMCost #VibeCoding #AgenticAI #SustainableAI #DeepSeek #Qwen #Wagtail
