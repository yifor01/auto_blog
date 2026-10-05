---
title: How Cresta turned CX expertise into an agent builder on the Claude Agent SDK
source: Claude Blog
url: https://claude.com/blog/how-cresta-turned-cx-expertise-into-an-agent-builder-on-the-claude-agent-sdk
model: claude-code/sonnet
generated_at: '2026-10-05T23:16:57.943456'
pinned: true
---

📌 Cresta 用 Claude Agent SDK 打造能自我進化的客服 Agent 建構工具

TL;DR：Cresta 以 Claude Agent SDK 為底層,打造 Conductor,讓團隊能用自然語言建立並持續優化客服 AI agent。

客服對話裡,一句「我要退款」背後可能藏著好幾層需要查證的脈絡：是哪一筆訂單、退貨期限是否已過、帳款狀態是否正常。要讓 agent 正確回應,往往得同時查核購買紀錄、退款政策、帳戶歷史與付款狀態。Cresta 把累積多年的客服判斷力,變成一個能幫其他團隊打造 agent 的「meta-agent」。

🤔 背景：客服 Agent 難在「脈絡」,不只是語言

Cresta 成立於 2017 年,由 CEO Ping Wu 帶領,累計募資超過 2.7 億美元、年度經常性收入（ARR）超過 1 億美元,客戶包含 United Airlines、CVS Health、Marriott 等企業。Cresta 的平臺提供能獨立處理對話的 AI agent、給真人客服的即時建議,以及揪出業務改善方向的對話洞察。build 與維護這些 agent,需要組織做出關鍵判斷：agent 該知道什麼、要存取哪些系統、哪裡該保有彈性、哪裡又必須固定行為。Cresta 想把這份判斷力開放給更多團隊,而不必每次都從零開始,Conductor 因此誕生。

🧩 Conductor：一個「造 agent 的 agent」

Conductor 是一個自然語言 agent 建構工具,使用者描述想做什麼,Conductor 便引導流程,從有脈絡依據的藍圖出發,一路走到實作、評估與最佳化。Cresta 最早是用 Claude Sonnet 與 Claude Opus 打造內部版本,協助內部團隊支援客戶部署；接下來的問題是,能否把這套系統變成客戶可以直接在平臺內使用的產品。為了支撐這種開放式的開發工作,Conductor 採用 Claude Agent SDK 作為通用執行引擎,負責蒐集脈絡、呼叫工具、寫程式碼並執行、再根據結果調整。Cresta Conductor 工程主管 Renjie Li 表示,團隊原本就把 Claude Code 當內部開發工具使用,因為它在軟體開發面向的 agent 建構上效果很好；Claude Agent SDK 則讓他們能以程式化的方式使用同一套 agentic 開發引擎,再接上 Cresta 自身的對話洞察、CX 專業、評估機制與執行環境。Cresta 表示,在 Cresta 與合作夥伴的早期使用案例中,Conductor 讓初次部署時間大約縮短了一半。

📊 自我進化的知識飛輪

Conductor 建立在既有的 CX agent 開發最佳實務之上,屬於會自我改進的 meta-agent。團隊用它建立、調整愈多 agent,就會沉澱出愈多自己的模式、工作流程與專業判斷,形成一個知識飛輪：上線後的實際互動、工作流程結果與回饋,會變成下一輪改進的訊號。Conductor 也協助建構者把從一次 agent 開發中學到的經驗,轉成可重複使用的記憶素材,包含模式、業務規則與評估方法,再以「skill」的形式分享給團隊其他成員,讓大家能從同一套驗證過的做法出發。

💡 深入分析：在「彈性」與「決定性」之間畫線

寫出第一版 prompt 只是建構一個實用 agent 的一部分。更難的判斷是：對話在哪裡該保留彈性,哪裡又需要明確的業務規則與受控的工具行為。Renjie Li 指出,太過追求「決定性」會讓團隊陷入試圖窮舉每一種分支的龐大決策樹；但對高度監管、風險容忍度低的產業而言,有些企業關鍵流程必須每次都正確執行。Conductor 協助找出並強化這些需要固定行為的環節與其實作方式,同時保留改善整體體驗的彈性。它會依據歷史對話,幫團隊判斷哪裡該讓真人留在流程中,哪裡可以讓模型自行調整；設定好這些邊界後,開發者仍需針對要求測試這些固定邏輯,並隨著業務規則變動持續修訂測試內容。

📊 怎麼評估一個「造 agent 的 agent」

Conductor 的好壞,是以它「建構 agent 的能力」來衡量。Cresta 讓 Conductor 跑過一組建構任務：建立新 agent、為既有 agent 寫測試案例、修改既有 agent,以及執行根因分析。完成任務不是唯一標準,團隊同時檢視結果、達成過程與使用的資源,評估維度如下：

| 評估項目 | 對應問題 |
|---|---|
| Outcome（結果） | Conductor 是否產出了符合需求且可用的成果？ |
| Execution path（執行路徑） | 是否使用了適當的工具與必要的脈絡？ |
| Quality（品質） | 結果與精心策劃的參考答案相比如何？ |
| Resource use（資源使用） | 任務花了多少時間與模型用量？ |

這組任務同時扮演安全網的角色：每當有新的 Claude 模型推出,或 Conductor 框架更新,Cresta 會用同一組任務與評分方式重新測試,確認哪裡變好、哪裡還需要改進,才會決定是否採用變更。這套評估紀律也內建在 Conductor 本身,讓使用者的團隊能自行檢查 agent 是否照預期運作。Conductor 會把建構過程中捕捉到的需求與邊界情境,轉成評估模組裡的測試,讓團隊在政策、串接系統與對話模式改變時,持續監控那些「每次都必須正確」的流程。

🧩 架構：Claude Agent SDK 當底層引擎,Conductor 疊加 CX 專業

Cresta 把 Conductor 設計成 CX 專屬的 agent 開發控制層,整合對話資料、領域專業與開發實務,再透過政策、可觀測性、驗證與回饋驅動的改進機制來治理每一次 agent 執行。Claude Agent SDK 位於 Conductor 之下,作為通用的執行引擎,負責蒐集脈絡、呼叫工具、寫程式碼並執行；Conductor 則在上層疊加 Cresta 的 CX 工作流程、工具與領域脈絡。團隊評估 SDK 時,對照的是 Conductor 實際要處理的工作：多步驟任務、大量脈絡與重複的工具呼叫,審查範圍涵蓋資料隱私、租戶架構、組織層級金鑰分配、控制與整個實作的可觀測性。Cresta 工程副總 Xiangru Chen 表示,Anthropic 提供了一個強健的通用 agentic 軟體開發基礎,讓團隊能把工程投資放在 Cresta 真正能創造長久客戶價值的地方。

🎯 實務啟示

對於想打造垂直領域 agent 平臺的團隊,Cresta 的做法提供一個可借鏡的分工方式：把通用的 agentic 執行引擎交給像 Claude Agent SDK 這樣的基礎設施,自己的工程投入則集中在領域判斷、評估機制與知識累積上。另外,Conductor 針對「建構 agent 的 agent」本身建立的 outcome、execution path、quality、resource use 四維評估架構,也是其他團隊在打造自己的 agent builder 時,值得參考的實務框架。

⚠️ 留意的侷限

Cresta 提到的「初次部署時間大約縮短一半」,是來自 Cresta 與合作夥伴早期使用案例的自述數字,並非第三方驗證結果；文章也未揭露更多模型版本或架構細節,僅提及採用 Claude Sonnet、Claude Opus 與 Claude Agent SDK。

🔗 來源
- 標題：How Cresta turned CX expertise into an agent builder on the Claude Agent SDK
- 作者／機構：Anthropic（Claude Blog）
- 連結：https://claude.com/blog/how-cresta-turned-cx-expertise-into-an-agent-builder-on-the-claude-agent-sdk

#Anthropic #ClaudeAgentSDK #Cresta #AIAgents #CustomerExperience #EnterpriseAI #AgentBuilder #ConversationalAI #LLMOps #AIEvaluation
