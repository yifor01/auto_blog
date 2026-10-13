---
title: How Anthropic’s Dynamic Workflows Coordinate Claude Agents
source: Latent Space
url: https://www.latent.space/p/claude-dynamic-workflows
model: claude-code/sonnet
generated_at: '2026-10-12T23:50:37.200255'
score: 94
---

📌 Anthropic新功能「Flows」：讓Claude自己決定怎麼分工

TL;DR：Anthropic在AI Engineer NY發布動態工作流「flows」,讓Claude自主規劃多agent分工,而非由工程師手動配置。

當你手上管理的agent多到每天要審核一堆它們開出的PR,你大概已經變成了那個「人肉瓶頸」。這正是Anthropic在AI Engineer New York 2026工作坊上,拿出新功能dynamic workflows(簡稱「flows」)要解決的問題。

🤔 **從「人工配置」到「Claude自己決定怎麼分」**

這場分享由Anthropic技術人員CJ Avilla與Harrison Stall主講,他們先回顧了Unix由Ken Thompson打造、Linux從Linus Torvalds一人逐步演變成多層可信維護者體系的歷史,想說明的道理是:要讓agent做真正有野心的大型專案,它們也需要類似的組織層級。Avilla提到,很多現在在管理大量agent的人,會開始感覺自己變成瓶頸,「坐在GitHub前審PR、確認一切符合預期」。

Dynamic workflows的概念最早出現在Claude Code裡,叫做「為每個任務配一個harness」,但flows可以跑得比單一agent或固定roster更久。核心轉變在於:過去Claude Managed Agents需要開發者自己設定一個coordinator與一組subagent名單,而flows讓Claude自己決定怎麼拆解與編排工作——由主導agent自己訂計畫,寫出一套編排程式,負責啟動agent、收集結果、管理資訊流動。Stall形容,「在多agent編排的不同階段,它能完成一個個可驗證的獨立工作單元,而你不需要去管理這些環節之間的連接」。Avilla也補充,開發者如果想要,仍可以在agent設定裡傳入預先配置好的專用subagent。這項功能目前開放在Claude Console(開發者透過API存取Claude的介面)中使用。

🧩 **示範案例:股票觀察清單掃描**

現場演示了一個相對簡單的flow:股票觀察清單掃描器。流程分兩階段——先由scan階段把個別股票代號分派給各自擁有獨立context的agent,再由review階段檢視這些發現並產出報告。

💡 **現場Q&A挖出的細節**

幾個聽眾提問頗值得工程師參考:
- Claude怎麼決定需要多少agent,一個簡單的掃描會不會動輒觸發上百個subagent?Stall回答「答案其實是靠evals與較低的預設值」,真正有野心的任務需要明確鼓勵更高的平行化程度才會發生。
- 主導agent跑的時候知道自己有多少預算嗎?Stall說模型執行時並不知道預算,但開發者可以設定session層級的預算上限;他也提到,如果讓模型知道自己的預算,可能會讓agent變得「有點焦慮」,引來現場笑聲。
- 怎麼讓重複執行的flow隨時間變得更便宜、更有效率?除了讓Claude自己檢視產生的成本外,Avilla建議可以搭配另一項研究預覽功能「dreaming」——它會讀取既有的記憶庫與過去的session記錄,產出重新整理過的新記憶庫,合併重複項目、取代過時或互相矛盾的內容,並浮現新的洞見。Avilla形容這是把與該些session相關的記憶庫「結晶化並改善」。
- subagent之間能彼此溝通嗎?Stall說它們共享一個檔案系統,可以透過檔案交換資訊,但開發者無法透過API直接讓一個subagent對另一個發訊息。
- 開發者能看到subagent實際做了什麼嗎?Avilla表示可以透過Claude Console裡的圖形化介面查看,能清楚看到主導agent實際傳給每個subagent的payload,理解整個圖中每一步的轉換。

⚠️ **成本與邊界**

以股票觀察清單這個案例來說,Avilla坦言flows的成本「遠高於」單一agent方案,但在找出所有細節上也「有效得多」。至於股票觀察的flow能不能自己意識到掃描模型不夠好、進而自動調整下次排程,Stall說這目前還沒做進去,但他和Avilla認為hill-climbing與dreaming這類機制,未來可以用來改善這個迴圈。

🎯 **實務啟示**

有聽眾問到flows能否支撐大型科學研究專案,並提及OpenAI近期宣布的Navier–Stokes千禧年難題相關成果,Stall沒有透露Anthropic內部如何計算這類大型科學問題的細節,但表示讓一般使用者也能處理這類問題是他們的目標:「flows基本上是一種對困難問題砸test-time compute的方式,能更快從模型裡擠出更多能力」。對工程團隊來說,這代表未來設計agent系統時,拆分任務、管理agent拓撲的工作,有機會逐漸從人工配置轉移給模型自己判斷——但目前仍需要靠evals與明確提示去控制agent數量與成本,不是丟出需求就能無限擴張的免費午餐。

🔗 **來源**
- 標題：How Anthropic's Dynamic Workflows Coordinate Claude Agents
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/claude-dynamic-workflows

#Anthropic #ClaudeAgents #MultiAgent #AIOrchestration #DynamicWorkflows #AgenticAI #ClaudeCode #LLMOps #AIEngineer #AgentOrchestration
