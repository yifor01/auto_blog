---
title: Nous Research Ships Bot Mode for Hermes Agent, Turning Agent Profiles Into
  a Roster of Named Bots
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/17/nous-research-hermes-bot-mode/
model: claude-code/sonnet
generated_at: '2026-08-18T06:32:47.082758'
score: 86
---

📌 一個 Hermes 帳號變一群 Bot，Nous Research 讓 AI agent 互相 @ 對方

TL;DR：Hermes Desktop 內建 Bot Mode，把單一 agent session 變成一組具名機器人，彼此能用 @mention 交接工作。

如果你的 AI agent 工作流程一直只有一個聊天視窗、一個人格、一份記憶，那 Nous Research 剛出的這個功能值得留意：Bot Mode 把單一 agent session 清單改成一整個「機器人名冊」，每個 bot 都是獨立的 Hermes profile，有自己的聊天紀錄、記憶、技能與固定模型，還能透過一個常駐的 Agent Inbox 互相傳訊、用 @mention 交接工作。

🤔 **從一日 beta 到預設內建**

Bot Mode 最初由共同創辦人 Teknium 以獨立外掛形式做一日公開 beta 測試，蒐集回饋後承諾整合進主應用程式。如今根據 hermes-agent PR #87886，Bot Mode 已捆綁進 Hermes Desktop 並預設開啟，獨立版 repository 已封存，後續開發轉移至主專案內的 apps/desktop/src/plugins/hermes-bots/。此功能隨 Hermes Agent v0.20.3 一起發佈，Hermes Agent 與外掛皆採 MIT 授權，桌面版可免授權費使用。

🧩 **每個 bot 就是一份獨立 profile**

技術上，一個 bot 就是一份 Hermes profile，存放在 ~/.hermes/profiles/<name>/ 底下，config、記憶、技能、憑證與聊天紀錄各自獨立。建立與編輯走的是既有的 profiles.* gateway RPC（list、create、describe、configure），頭像產生則透過 image.generate RPC，可在本地或遠端 gateway 上執行。這代表 Bot Mode 本質上是一層 UI，架在 Hermes 原本就有的能力之上，沒有新增底層機制，維持了系統的簡潔。

Bot 之間的排程任務沿用既有的 Hermes cron job，只是加上 [bot:<name>] <routine> 命名空間，仍會出現在 hermes cron list 裡。Bot 對 bot 的訊息也不是新協議，而是真正的 CLI 交接指令 hermes -p <bot> chat -c "Agent Inbox" -q "..."，訊息會帶有來源標註，每個 bot 的 SOUL.md 檔案負責定義回覆協議。在對話中打 @researcher have a look at this，當前 bot 就會把工作交接出去並回報結果。

🧩 **新增能力：群組與多來源名冊**

New Agent 對話框只需要名稱、標題、描述即可建立，進階選項才會開放完整 profile 設定，也可以直接複製既有 profile、固定 provider 與模型、寫自訂 SOUL.md，或跳過技能設定。in-tree 版本相較最初 beta 新增了兩項能力：Groups 可以把名冊分類到會跨機器同步的標籤區塊；Group chats 則開放二到六個 bot 的共享聊天室，一則訊息會觸發最多三輪成員發言，被 @ 到的 bot 會回應，沒人被 @ 時大家都會回應（也可以選擇簡短回覆或跳過）。另外還支援多來源名冊，把 Settings → Connections 底下所有連線的 bot 一起拉進同一份名冊。

⚠️ **企業採用前要注意的限制**

官方定位很明確：適合獨立開發者、新創與中小型工程團隊立即採用，但企業應把它當成工作站工具而非受管理的基礎設施——沒有管理主控臺、沒有 SSO、沒有中央稽核紀錄，也沒有政策層，受監管的採用者需要自己補上這些控管機制。

🎯 **實務啟示**

若你已經在用 Hermes 做多角色 agent 流程（例如研究員配推理模型、寫手配便宜模型），Bot Mode 把原本靠命名慣例或多開視窗手動管理的分工，變成有名冊、有交接協議、有群組聊天的正式結構，適合拿來搭建 scout、reviewer、publisher 這類交接鏈，但上線前記得自行補齊權限與稽核控管。

🔗 **來源**
- 標題：Nous Research Ships Bot Mode for Hermes Agent, Turning Agent Profiles Into a Roster of Named Bots
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/17/nous-research-hermes-bot-mode/

#NousResearch #HermesAgent #AIAgents #MultiAgent #OpenSource #MITLicense #AgentOrchestration #DeveloperTools #LLM #AIWorkflow
