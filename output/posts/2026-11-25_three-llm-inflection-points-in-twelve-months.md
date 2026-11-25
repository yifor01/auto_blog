---
title: Three LLM inflection points in twelve months
source: Simon Willison
url: https://simonwillison.net/2026/Nov/24/llm-inflection-points/
model: claude-code/sonnet
generated_at: '2026-11-25T01:45:12.985116'
score: 82
---

📌 一年內三次質變：LLM與coding agent的三個拐點

TL;DR：Simon Willison回顧過去12個月LLM與coding agent的三次能力拐點。

2026年11月24日，正好是Claude Opus 4.5發布滿一年的日子。Simon Willison在這篇文章裡回頭看，認為這個模型是他使用Claude Code以來第一個「預設輸出通常就是對的」的模型，而這只是他歸納出的三個拐點之一。

🤔 **拐點一：coding agent從「偶爾好用」變成「預設可信」**

在Opus 4.5之前，作者並沒有把Claude Code當成每天依賴的工具，因為結果不夠可靠，常常得自己動手修正，稱不上明顯的加速器。Claude Code當時已經推出9個月（與Claude 3.7 Sonnet同日於2025年2月24日發布），但要等到Opus 4.5，作者才感覺到大多數日常遇到的coding問題，模型可以直接給出正確答案，而且明顯比自己動手解題更快。同一個月，OpenAI發布GPT-5.1 Instant、GPT-5.1 Thinking、GPT-5.1-Codex與GPT-5.1-Codex-Max，對Codex這個coding agent帶來類似的效果，讓它也變得可靠好用。作者提到，這個時間點恰逢12月假期，許多人（包括他自己）趁假期把玩這些新工具，到了1月就已經把它們用在真正的工作上。

🧩 **拐點二：「Fable class」模型，給目標、給工具，接下來讓它自己想辦法**

今年4月，Anthropic宣布的Claude Mythos因為具備更強的網路安全能力，不只能找到漏洞，還能想辦法利用漏洞，而被認為「太危險而不釋出」。6月，一個被收斂過的版本以Claude Fable 5之名問世：它會解決大多數問題，但會主動擋下使用者把它用在安全攻擊相關的用途上。發布後短短三天，美國政府便以出口管制為由把這個模型收回，直到7月1日才解禁。

作者把這類模型稱為「Fable class」：給定目標與適當的工具，模型會自己想辦法達成，不需要一步步手把手指示。他舉了兩個例子：6月時請Fable處理Safari的一個顯示錯誤，它主動架了一套基於pyobjc-framework-Quartz的螢幕截圖機制，外加一個支援CORS的localhost記錄伺服器來協助除錯；最近一次則是他讓Opus 5.5與Fable 5.2存取房間裡五支WebAudio麥克風，兩個模型合力把一個惱人的神秘嗶嗶聲來源定位到誤差約40公分以內。作者目前把Claude Fable 5、5.1、5.2與Claude Opus 5.5都歸類為Fable class（他稱Opus 5.5是「平價版Fable」），並認為GPT-6 Astra同樣達到這個水準，新發布的Gemini 4 Neon也可能算進去。他表示這類模型現在已經是他對前沿模型的基本期待。

💡 **拐點三：模型突然學會了3D建模，也學會了「什麼叫好玩」**

過去四個月，前沿LLM在3D建模上突然變得很強，用Blender或寫Three.js程式碼，就能生成幾乎任何描述物件的可信模型。作者最早在Claude Fable 5上注意到這個現象，到Opus 5.5、GPT-5.6 Sol、GPT-6 Astra，再到最新的Gemini 4系列，這個能力明顯加速。他舉了Gemini 4 Neon的例子：只靠文字描述與OpenStreetMap地圖資料，就生成了一段「yonkers變身大型機甲、踩過Manhattan、Queens與Brooklyn」的Three.js動畫。作者認為，3D空間感對把視覺LLM用在機器人任務上相當關鍵，但他不確定這是實驗室刻意聚焦3D建模的結果，還是反過來的因果關係。

另一條線索來自遊戲設計。8月時，作者讓Fable 5做了一個浣熊搶劫題材的小遊戲，3D畫面看起來像遊戲，但玩起來很糟；GPT-5.6 Sol Ultra做得好一些，但遊戲本身玩90秒後還是很無聊，他當時還頗為安心，覺得「設計出好玩的遊戲」似乎仍是人類獨有的能力，甚至在9月的一場演講裡用這個例子安慰聽眾。後來他只對Claude Opus 5.5說了一句「這遊戲還不夠好玩，讓它變得更好玩」，結果真的奏效：他做的那款類似《終極動員令》的RTS遊戲，在Opus花了12小時試玩與重新調整平衡後，從無聊變得相當耐玩。Opus 5.5（2026年9月22日發布）是作者用過的第一個「看起來理解什麼叫好玩」的模型。此後他參加的兩場研討會上，都有人展示用類似方法做出來、真正稱得上是完整遊戲的作品；獨立遊戲圈甚至因為AI協作編程這件事爆發了一場文化戰爭，不少人稱《GTA VI》是「最後一款生成式AI之前的大作」。

⚠️ **Fable 5.2算不算第四個拐點？作者自己也還沒下定論**

作者坦言，他還無法判斷Fable 5.2究竟是一個新的拐點，還是單純的漸進式進步。他提到自己最近用這個模型處理了許多拖了好幾年、一直沒解決（或一直在拖延）的難題，過去三週內，Datasette專案接連推出1.0a42、1.0a43、1.0a44版本，LLM專案也接連推出0.37、0.37.1、0.37.2、0.37.3、0.38版本，一口氣塞進大量修正、功能與改進。如果這真的算是一個拐點，作者認為關鍵特徵會是：只要你能想清楚並描述一個軟體，Fable就能把它做出來。

🎯 **實務啟示**

作者的結論很直接：過去一年軟體開發的樣貌已經徹底改變，他不認為自己會再回去手動輸入大部分程式碼。對工程團隊而言，這篇回顧提供的參考框架是：評估一個新模型時，除了看基準測試分數，也可以用「預設輸出是否可信」「能否主動規劃並調用工具解決問題」「能否處理空間與美感這類主觀判斷」這三條線索，去判斷它是否真正跨過了能力門檻，而不只是漸進式的分數提升。

🔗 **來源**
- 標題：Three LLM inflection points in twelve months
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Nov/24/llm-inflection-points/

#LLM #ClaudeCode #CodingAgents #AIEngineering #Anthropic #OpenAI #Gemini #AIAssistedCoding #SoftwareDevelopment #AgenticAI
