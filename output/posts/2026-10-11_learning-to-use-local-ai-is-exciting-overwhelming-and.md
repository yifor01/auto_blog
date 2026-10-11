---
title: Learning to use local AI is exciting, overwhelming, and frustrating
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/1008484/learning-local-ai-hermes-qwen-model-mac-studio-testing-diary-progress
model: claude-code/sonnet
generated_at: '2026-10-11T21:09:03.760283'
score: 45
---

📌 把 125B 參數模型塞進自己電腦，本地 AI 到底能幹什麼活

TL;DR：記者實測在 Mac Studio 上跑本地 agent 工具 Hermes，發現隱私優勢明顯，但設定與維運門檻比雲端 AI 高得多。

把最私密的資料交給雲端 AI，一直是很多人遲遲不敢全面擁抱 AI 助手的原因。隨著 Mac Studio 等桌機配備愈來愈大的統一記憶體、RTX Spark 這類主打 agentic AI 的 Windows 機種即將上市，「在自己電腦裡養一個只聽自己指揮的小幫手」這個想法變得更可行。The Verge 的 Antonio G. Di Benedetto 記錄了他用 M5 Ultra Mac Studio 跑本地大模型的第一手體驗，過程比想像中更混亂，也更有意思。

🧩 **工具與模型怎麼選**

他選用的是開源、可自架的桌面 agent 應用 Hermes Agent，支援 macOS、Windows、Linux，若只用本地 LLM 則完全免費。由於測試機配有 256GB 統一記憶體，理論上能跑絕大多數開源模型，但這也帶來新的問題：市面上模型種類多到數不清，各有專精用途。他最終透過 Hermes 內建的 onboarding 介面與模型選擇器，選了參數量 1250 億、模型檔案約 105GB 的 Qwen 3.8 Flash Next——邏輯很簡單：本地跑模型不用按 token 計費，不如一次選大的。設定完成後，他甚至把它接上 Telegram bot，讓手機也能遠端下指令。

📊 **四個實際跑過的任務**

- **每日簡報**：用 cron job 排程，讓 Hermes 掃過信箱與行事曆，整理出需要注意的事項外加簡短天氣預報，透過 Telegram 推送。他提到一開始任務常常失敗，後來才發現原因是排程時間（早上 7:30）macOS 處於睡眠狀態。
- **Steam 遊戲庫整理**：他有超過 400 款 Steam 遊戲需要手動分類，於是讓 Hermes 直接讀取本機已安裝的 Steam 用戶端，提出分類建議，並保留他自訂的「最愛」「合作遊戲」等分類。執行前需要申請 Steam Web API 金鑰並授權給 Hermes，整理完成後他隨即撤銷了這個權限。
- **本機資料分析**：讓 Hermes 分析個人財務記錄，以及比對新筆電規格做成表格——這兩項任務都是他「不願意、也不能」上傳雲端的資料，一個涉及隱私，一個涉及尚未公開的保密資訊，正是本地 AI 的核心價值所在。
- **筆電測試腳本自動化**（進行中）：為了把目前需要手動跑三輪取平均值、非常耗時的筆電效能測試自動化，他讓 Hermes 寫 Python 腳本，形容這個過程「相當於一番折騰」，目前仍在推進中。

⚠️ **沒有想像中的「魔法助理」**

文章也坦誠記錄了挫折：每日簡報功能曾多次故障；要讓模型真正產出有用結果，需要使用者自己不斷餵給它更多情境與需求，而不是裝好就能一鍵躺平。作者也特別提到自己對待 Hermes 的態度——不說「請」、不說「謝謝」，單純把它當成電腦程式而非數位朋友，這也呼應了本地 AI 目前的定位：一個需要持續調校、授權管理的工具，而非開箱即用的智慧夥伴。

🎯 **實務啟思**

這篇體驗談對工程師的參考價值在於：本地 agent 的落地瓶頸往往不在模型能力，而在「授權管理」與「任務拆解」——像 Steam API 金鑰用完即撤銷、cron job 要考慮系統睡眠狀態，這些都是雲端 AI 服務不太需要處理的細節。如果手上有敏感資料（財務記錄、未公開產品資訊）又想用 agent 自動化處理，本地部署目前仍是現實可行的折衷方案，但要有心理準備投入額外的維運時間。

🔗 **來源**
- 標題：Learning to use local AI is exciting, overwhelming, and frustrating
- 作者／機構：Antonio G. Di Benedetto, The Verge AI
- 連結：https://www.theverge.com/ai-artificial-intelligence/1008484/learning-local-ai-hermes-qwen-model-mac-studio-testing-diary-progress

#LocalAI #OnDeviceAI #OpenSource #Qwen #AIAgent #PrivacyFirst #MacStudio #SelfHosted #AgenticAI #LLM
