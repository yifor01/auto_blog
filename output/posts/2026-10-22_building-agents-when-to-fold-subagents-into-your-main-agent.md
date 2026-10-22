---
title: 'Building agents: When to fold subagents into your main agent loop'
source: Claude Blog
url: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
model: claude-code/sonnet
generated_at: '2026-10-22T20:41:19.683679'
pinned: true
---

📌 【Anthropic 實務分享】多 Agent 架構未必更好,該收回主迴圈了

TL;DR:Anthropic 實務發現,搭配 skills 的單一 agent 常比多 subagent 架構品質更好、成本與延遲更低。

把每個團隊的功能都包成一個 subagent,組織圖就這樣直接複製成了 agent 架構圖。這是 Anthropic Applied AI 團隊在多個企業部署中反覆看到的模式,而他們的結論是:這套架構常常在幫倒忙。

🤔 **企業導入 agent 常踩的坑**

Subagent(擁有獨立 context window、工具與指令,由協調者 orchestrate)本是 agent 設計的核心元件,擅長驗證、平行作業與模組化權限控管。但 Anthropic 在多個企業部署的比較中觀察到,搭配 skills 的單一 agent,在品質上經常同時勝過「一個 prompt 包辦所有事」與「多 subagent」兩種設計,而且成本與延遲通常更低。例如某公司的客服 agent 裡塞了十幾個專家 subagent,結果品牌語氣難以維持一致,還拖慢了使用體驗。

Anthropic 也點名了企業常見的失敗模式:每個團隊各自開發 subagent,造成重疊氾濫、無人統一維護的「subagent sprawl」;每個團隊往 system prompt 加一句話,形成規則互相衝突、語氣不一致的「Frankenprompt」;各團隊自訂過度本地化的評測指標,沒人掌管全局分數,導致決策依據是被稀釋過的數字;以及多 agent 架構本身疊加的延遲成本——某客戶實測顯示,改用單一 agent loop 後執行速度約快了 2 倍。

🧩 **用「漸進式揭露」取代 orchestrator-subagent**

Anthropic 建議的替代方案是透過 skills 漸進揭露 context、透過 tool search 漸進揭露工具:agent 一開始只看到 skills 與工具的簡短描述,真正需要時才完整載入。這樣做有三個理由:共享 context 能讓模型看到前面每一步的結果並串連起來,比多個 subagent 各自回傳摘要產生更豐富的洞見,也避免了資訊在交接間逐步失真的「電話遊戲」;漸進式揭露能避免 context 膨脹,讓團隊建立處理多種任務的單一 agent,而不必把所有內容一次塞進冗長的 system prompt,Anthropic 提到他們藉此把 Claude Code 給進階模型的 system prompt 削減了超過 80%;模型能力也在持續提升,從 Opus 4.5 開始,模型能在單一迴圈裡處理的事情遠超多數團隊預期,讓一部分原本靠 harness 手刻的邏輯變得多餘。

建議的單一迴圈設計是:一個模型、一個 context window 跑在 open-ended 的 tool loop 裡,harness 只設定上限,例如回合數與成本預算、寫入權限閥;每個回合模型發出一批 tool calls,harness 平行執行後把原始結果交還給同一個模型,模型再決定下一步是再跑一批、問使用者問題、還是給出答案;迴圈在模型給出答案或碰到預算上限時停止,之後可選擇性跑目標或 verifier 檢查。模型在第一回合就把計畫寫進 context,並隨結果持續修正。這跟傳統 orchestrator 加 specialist 設計的關鍵差異在於:寫計畫的模型與執行計畫的模型是同一個,所以能在回合中途隨時調整計畫。

⚠️ **subagent 仍有它的位置**

Anthropic 強調 subagent 並非該被淘汰,適合使用的情境包括:單一 agent loop 已出現可量測的 context 膨脹效能衰退;多個任務需要平行處理,且能用完就丟棄全新的 context window;或單一 agent 在工具選擇上出現混亂、system prompt 裡存在衝突指令。若真的要走多 agent 路線,建議從最簡單的模式開始(例如 generator-verifier、orchestrator-subagent),並依「context 邊界」切分工作,讓每個 subagent 只處理需要很少外部資訊的任務,回傳精簡結果。

🎯 **實務啟示**

如果你的 agent 架構正逐漸變成組織圖的翻版,值得停下來問的不是「要不要再加一個 subagent」,而是「這段邏輯能不能靠 system prompt、skills 與 tool search 讓模型自己判斷」。Anthropic 提到他們也提供了 migration kit,可以跑一個引導流程來評估現有 subagent 是否該收回主迴圈,並附帶可在模擬系統上先試跑的 demo。

🔗 **來源**
- 標題:Building agents: When to fold subagents into your main agent loop
- 作者/機構:Anthropic
- 連結:https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop

#AIAgents #AgentArchitecture #Anthropic #ClaudePlatform #Subagents #LLMEngineering #AgentDesign #ToolUse #PromptEngineering #AIOrchestration
