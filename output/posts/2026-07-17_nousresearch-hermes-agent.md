---
title: NousResearch/hermes-agent
source: GitHub Trending
url: https://github.com/NousResearch/hermes-agent
score: 100
model: tencent/hy3:free
generated_at: '2026-07-17T08:06:57.021525'
---

📌 【NousResearch 開源】Hermes Agent：會自己長出技能的 AI 代理

TL;DR：具備內建學習迴路的自我改進 AI agent，可跨平臺運作並自訂模型。

大多數 AI agent 用完即忘，下次對話又從零開始。NousResearch 的新開源專案 Hermes Agent 宣稱打破了這點——它內建學習迴圈，會從經驗中建立技能、跨會話記住你是誰。

🤔 **解決什麼問題、為誰而做**

Hermes Agent 是 Nous Research 打造的「自我改進 AI agent」，目標是讓 agent 不只能執行任務，還能在使用過程中持續累積知識。它適合希望 agent 長期陪伴、跨裝置協作，且不希望被單一模型或單一裝置綁死的開發者與使用者。

🧩 **核心架構與設計理念**

README 指出，專案由幾個關鍵設計組成：

- 封閉學習迴路（closed learning loop）：agent 自行整理記憶並定期自我提醒（periodic nudges）；在複雜任務後自主建立技能（autonomous skill creation），且技能會在使用中自我改進。
- 跨會話召回：採用 FTS5 會話搜尋，搭配 LLM 摘要來回溯過往對話；並透過 Honcho dialectic 方式建立使用者模型，深化對「你是誰」的理解。
- 開放標準相容：支援 agentskills.io 開放標準，避免技能格式被鎖死。
- 單一閘道（gateway）程式：同時對接 Telegram、Discord、Slack、WhatApp、Signal 與 CLI，並提供語音備忘錄轉錄與跨平臺對話延續。
- 完整終端機介面（TUI）：支援多行編輯、斜線指令自動補全、對話歷史、中斷並重定向、工具輸出串流。
- 排程自動化：內建 cron 排程器，可用自然語言設定每日報告、夜間備份、週審計等無人值守任務。

💡 **部署彈性與模型自由**

專案強調不綁定使用者的筆電：可在 5 美元 VPS、GPU 叢集，或閒置近乎零成本的 serverless 架構上執行；也能從 Telegram 遙控位於雲端 VM 的 agent。模型切換只需 `hermes model` 指令，支援 Nous Portal、OpenRouter、OpenAI、自託管端點等，無須改程式碼、無供應商鎖定。

🎯 **實務啟示**

對工程師而言，若正在評估長期記憶與跨平臺 agent 框架，Hermes Agent 的「技能自創＋自我改進＋開放標準」組合值得試跑；其單一 gateway 多平臺架構也降低了同時維護多個 bot 的負擔。但要注意，README 未提供實際效能基準或技能改進幅度的量化資料，匯入前建議以小規模 VPS 驗證學習迴路是否如描述運作。

🔗 **來源**
- 標題：NousResearch/hermes-agent
- 作者／機構：NousResearch
- 連結：https://github.com/NousResearch/hermes-agent

#AI #Agent #NousResearch #SelfImproving #LLM #OpenSource #SkillLearning #CrossPlatform #Automation #MemoryLoop
