---
title: 'OpenClaw Power, MacBook Simplicity: Five Days With Grok Bot'
source: Latent Space
url: https://www.latent.space/p/grok-bot
model: claude-code/sonnet
generated_at: '2026-09-05T19:19:29.272211'
score: 70
---

📌 五天實測 Grok Bot：把「Agent」做成人類看得懂的積木

TL;DR：Latent Space 作者實測 xAI 的 Grok Bot 五天，發現它把 agent 配置簡化成登入按鈕，但代價是把安全邊界也一併簡化掉了。

裝一臺新 MacBook 跟裝一臺 Linux 主機，體驗完全不同：前者開機即用，後者給你全部的自由與全部的設定負擔。作者用這個比喻來形容 Grok Bot 與 OpenClaw 的差異——而這個比喻背後，藏著一個關於「agent 這個抽象層要放在哪裡」的更大問題。

🤔 **設定一個 agent，只需要登入一次**

作者打開 Grok Bot 的外掛目錄，搜尋 X、點選外掛，跳出瀏覽器登入畫面，登入後就連上了——不需要碰程式碼、不需要安裝 MCP server 的 JSON 設定、也不需要貼 API 憑證。他請 Grok Bot 檢視自己的 X 貼文與興趣，產出每日新聞摘要；又用工作帳號連上 Freshdesk，設定一個每十五分鐘檢查一次新客服工單的支援 bot。要複製一個原本要花時間心力維護的工作流，他只需要透過瀏覽器登入。

🧩 **Bot 才是程式的原子單位**

作者認為，Grok Bot 並非可程式化程度較低，而是把可程式化的層級拉高了：在 OpenClaw 裡，客製化意味著要更貼近程式碼、設定檔、工具、skill、外掛與底層基礎設施；在 Grok Bot 裡，「Bot」本身變成程式的原子單位。你賦予 Bot 特定角色、連接不同工具，再把多個 Bot 組成一個更大的系統，Grok Bot 稱之為「group chat」。這被作者類比為程式語言從機器碼、組合語言、C 一路走向 Python 的抽象層演進：介面變成英文，被程式化的對象不再是函式或服務，而是一個「Bot」。

作者實際打造了一個 Agentic Engineer Bot：不綁定單一模型或工具，而是給它存取多個 agentic 工程系統的權限，並訂下路由規則——視覺、設計、前端工作交給 Claude Code，除錯與仔細讀程式碼交給 Codex，較簡單的任務交給 Grok Build CLI。任何跟程式碼相關的需求丟進 Grok Bot 生態系，都由這個 Agentic Engineer 依規則自行決定該用哪個工具，作者不必再自己判斷。他甚至用 Grok Bot 的虛擬電腦建立了一個 Claude Bot，在裡面安裝並登入 Claude Code CLI。

作為對照，OpenClaw 2.0 本週釋出，Quick Start 可以重用既有的 Claude Code 或 Codex 登入資訊，其瀏覽器應用也把大部分設定、外掛管理與自動化搬進了圖形或對話介面；OpenClaw 2 同樣內建原生 Codex runtime 與其他 coding-agent harness 的支援路由。差異在於呈現方式：Grok Bot 把 agent 當作第一級、人類可讀的建構積木，OpenClaw 則把底層機制暴露得更多。

💡 **「擬人化」不只是包裝，是組織思維的方式**

每個 Bot 都有自己的名字、角色、身份與描述，作者認為這不只是介面上的裝飾，更幫助他在系統內建立認知上的區隔：他會像思考人類團隊分工一樣，判斷「這件事該由誰主導」。使用 Grok Bot 時，他不太需要再去想 context window 還剩多少、何時該壓縮對話、何時該開新對話——這些關注點仍然存在，只是沒有被暴露在介面上。此外，Grok Bot 支援同一服務的多個帳號同時連接，作者把個人與工作用的 Google Calendar 都接上，得到單一視圖而不必在兩個介面間切換。

虛擬瀏覽器則讓 Grok Bot 的能力超出外掛目錄本身：Freshdesk 並非原生連接器，作者直接在虛擬瀏覽器中開啟，把 1Password 裡的登入資訊轉過去完成驗證，之後支援 Bot 就能每十五分鐘檢查一次工單。這讓一個普通網站變成了可自動化、可週期執行的瀏覽器工作流。

⚠️ **Bot 之間是組織邊界，不是安全邊界**

作者明白指出一項重要限制：他建立的每個 Bot 都共用同一臺電腦、同樣的檔案、瀏覽器 session 與登入狀態——分開的 Bot 只是組織上的區隔，並非安全邊界。另外，xAI 自己也提醒，瀏覽器工作流可能遇到介面改版、session 過期或 CAPTCHA 等問題，建議優先使用原生連接器而非瀏覽器模擬。

🎯 **對工程師的啟示**

Grok Bot 與 OpenClaw 的對照，本質上是「託管 agent 電腦」與「使用者自有 agent 平臺」兩種路線的取捨：前者用犧牲底層掌控權換取極低的設定成本，後者保留完整客製化空間但要自己承擔運維。如果你正在評估要不要把多個 coding agent（Claude Code、Codex 等）整合進單一工作流，這篇實測提醒你留意一件容易被忽略的事：把多個 agent 包裝成「角色」很好用，但只要它們共用同一份檔案系統與登入狀態，你的安全邊界設計就必須獨立於這層組織抽象之外去思考。

🔗 **來源**
- 標題：OpenClaw Power, MacBook Simplicity: Five Days With Grok Bot
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/grok-bot

#GrokBot #OpenClaw #AIAgents #AgenticWorkflow #ClaudeCode #Codex #AgentPlatform #xAI #LLMTooling #AIAutomation
