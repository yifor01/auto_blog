---
title: 'Vibe Coding a Classic Game: Building Breakout Step by Step with an AI Assistant'
source: KDnuggets
url: https://www.kdnuggets.com/vibe-coding-a-classic-game-building-breakout-step-by-step-with-an-ai-assistant
model: claude-code/sonnet
generated_at: '2026-10-30T21:51:25.962536'
score: 70
---

📌 從一句提示到完整遊戲：用 Vibe Coding 重建經典 Breakout

TL;DR：KDnuggets 實測示範如何用 AI coding assistant 逐步生成 Breakout 遊戲，每個提示與程式碼都附上說明。

2025 年初 Andrej Karpathy 提出「vibe coding」這個詞，隨後被 Collins English Dictionary 選為 2025 年度詞彙；到了 2026 年，它已不只是噱頭，而是真實專案裡的標準做法之一。Airbnb 表示，公司目前約六成的新程式碼由 AI 寫成。這篇教學決定用這套工作流重建 1976 年的經典遊戲 Breakout，而且文中每一行程式碼都經過實際執行與自動化測試驗證後才發表。

🤔 **什麼是 Vibe Coding**

機制很簡單：你用自然語言描述目標，AI agent 生成程式碼，你檢視並給出下一步指示，重複到完成為止。真正改變的是 agent 的能力，現在的工具不只是自動補全一行程式碼，而是能讀懂整個專案、編輯多個檔案、執行程式並修正錯誤。

文中列出目前常見的工具選項：Claude Code 是終端機原生的 agent，適合直接在專案資料夾裡寫程式並執行測試；Cursor 把同樣的能力包進熟悉的 IDE；Replit Agent 專為新手設計，會先展示可見的計畫再動手寫程式；Bolt.new 與 v0 則是連終端機都不想碰、只想快速拿到可用原型的人的選擇。

🧩 **從骨架到物理運算，一步步往上疊**

Breakout 的背景值得一提：Atari 於 1976 年 5 月 13 日發表 Breakout，由 Nolan Bushnell 與 Steve Bristow 構思，作為 Pong 的單人進化版，實際由年輕工程師 Steve Wozniak 打造，身邊還有他的朋友 Steve Jobs。Wozniak 把晶片數量壓縮到 Atari 自家生產線都複製不出來，只能改用零件更多的版本量產；同一年兩人共同創立了 Apple，Breakout 的硬體邏輯也影響了原始 Apple II 的部分設計。

教學本身沒有用任何建置工具、框架或依賴套件，整個遊戲就是一個在瀏覽器打開即可執行的 HTML 檔案。作者刻意把需求拆成多個階段的提示，而不是一次要求「寫出整個遊戲」，理由是分階段更容易在 AI 生成程式碼出錯時，只檢查一小塊就能定位問題。

Step 1 的提示要求建立 480x400 的 canvas、置中、深色背景，以及分數與生命值的佔位文字，刻意不加任何遊戲邏輯，先確認頁面骨架能正確渲染。

Step 2 加入 80x10 像素的 paddle，用 keydown／keyup 監聽持續按住的方向鍵，而不是只在按下瞬間反應一次，讓 paddle 移動更連續；updatePaddle 函式最後用 Math.max 與 Math.min 把位置限制在畫布範圍內，一行程式碼解決 paddle 滑出畫面的問題。

Step 3 加入球體物理：dx、dy 代表球在兩軸上的速度，每一幀把座標加上速度就構成了整個遊戲的運動基礎；updateBall 偵測球是否碰到左右牆或上方牆，碰到就反轉對應軸向的速度，做出反彈效果。

💡 **拆解到可驗證的最小單位**

這三個步驟共通的設計理念，是把複雜系統拆成「可驗證的最小單位」：每一步都先確認上一步的輸出符合預期，才疊加下一層邏輯。這跟傳統手刻程式碼的除錯習慣相通，只是現在換成用自然語言下指令，再檢視 AI 產出的結果。

🎯 **實務啟示**

就算你的目標不是寫一款遊戲，這套「先骨架、再單一功能、每步都可視覺驗證」的提示拆分方式，同樣適用於其他 vibe coding 專案：與其要求 AI 一次生成完整系統，不如把需求拆成一連串可獨立檢查的小步驟，降低除錯成本。

🔗 **來源**
- 標題：Vibe Coding a Classic Game: Building Breakout Step by Step with an AI Assistant
- 作者／機構：Shittu Olumide, KDnuggets
- 連結：https://www.kdnuggets.com/vibe-coding-a-classic-game-building-breakout-step-by-step-with-an-ai-assistant

#VibeCoding #AIAssistant #ClaudeCode #GameDev #Breakout #JavaScript #PromptEngineering #Programming #AndrejKarpathy #Cursor
