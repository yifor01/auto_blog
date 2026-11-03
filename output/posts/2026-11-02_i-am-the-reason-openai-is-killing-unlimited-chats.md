---
title: I Am the Reason OpenAI Is Killing Unlimited Chats
source: Hacker News
url: https://chaosmanage.github.io/i-killed-unlimited-chatgpt/
model: claude-code/sonnet
generated_at: '2026-11-03T00:11:43.293509'
score: 78
---

📌 一個人用MCP隧道，把ChatGPT聊天室變成開發團隊

TL;DR：有人靠MCP連上自己的電腦，用「免費」的ChatGPT對話做完原本要燒Codex額度的開發工作。

當OpenAI宣布要終結無限制的ChatGPT對話時,有一位開發者站出來半開玩笑地說:這或許是我的錯。

🤔 **起點:一個能連上自己電腦的ChatGPT對話**

這一切始於ChatGPT支援自訂MCP(Model Context Protocol)伺服器,加上OpenAI提供的Secure MCP Tunnel。作者發現,透過這個隧道,可以把自己電腦上執行的工具直接暴露給一般的ChatGPT對話使用,而不只是Codex。於是他在自己的Windows筆電和VPS上架了一套統一的MCP伺服器,整合了兩個開源專案:Desktop Commander,讓ChatGPT能讀寫檔案與程式碼、執行終端機指令、跑測試、管理行程;以及CUA(Computer Use Agent),讓ChatGPT能截圖、操作滑鼠、點擊按鈕、檢視視覺元素,測試瀏覽器或桌面應用程式。

🧩 **接上隧道之後,一般對話也能做完整的開發工作**

透過OpenAI的Secure MCP Tunnel,作者用API金鑰驗證連線,把自己的MCP閘道器接上去,不需要額外架設雲端基礎設施。結果是:一般的ChatGPT對話也能檢查repository、修改程式碼、執行指令、除錯、並視覺化驗證修改結果——這些原本是Codex才能做的事。整套方案沒有額外付費的API推論呼叫,全部靠既有的ChatGPT訂閱、開源工具,以及自己原本就有的電腦。

作者後續還自己動手改良了這些開源工具:讓截圖能透過自訂的MCP App檢視器直接顯示在對話裡(而不只是ChatGPT能看到但他看不到的工具結果),也讓工具呼叫結果更容易在對話中閱讀,甚至做了一個監控儀表板,能啟動或停止整個MCP連線、監看伺服器健康狀態、追蹤CPU與記憶體用量,並檢視即時的工具呼叫記錄。

💡 **用GitHub issue當任務佇列,手動搭出多代理人開發流程**

因為一般ChatGPT對話無法自行產生或控制子對話/子代理人,作者得自己手動拼出一套多代理人協作流程:先用較強的推理模型(例如Codex裡的Astra,或ChatGPT裡額度有限的Pro模型)產出詳細的實作計畫,再把計畫拆成一個個範圍明確的GitHub issue,每個issue都附帶足夠的背景、需求與驗收標準,讓另一個AI代理人能獨立接手。接著開啟多個獨立的ChatGPT對話,各自跑Sol 6 High模型,分別指派不同issue,所有對話共享同一套MCP存取權限,能讀取專案、編輯檔案、跑測試、檢查錯誤並反覆迭代到完成。當時Sol High的用量幾乎沒有限制,即使速度比較慢,作者也願意接受,把較稀少的頂級模型額度留給架構設計、困難決策與審查。這套流程並不完美——多個代理人共用同一個檔案系統需要協調,偶爾也需要換上更強的模型介入收尾——但對定義明確的程式任務而言,效果出乎意料地好。

⚠️ **無限對話終究還是被收回了**

OpenAI宣布終結無限制的ChatGPT對話,將其用量與Codex合併計算,作者賴以運作的這套開發流程因此無法再以同樣方式運行。他強調自己並未違反任何規則,只是把ChatGPT對話、MCP支援、安全隧道與自訂工具連接這些OpenAI本就提供的能力用到極致。

🎯 **實務啟示**

這個案例提醒工程師:平臺的「用量限制」設計往往假設使用者只會做平臺預期的事,而MCP這類開放協定一旦把本機工具暴露給對話介面,使用模式很容易超出產品團隊的原始想像——這也是為什麼額度政策需要隨著實際使用型態不斷調整。對正在評估AI輔助開發工具的團隊而言,比起糾結哪個模型更聰明,更該留意的是訂閱方案的額度計算方式是否能撐住自己真正想要的工作流程。

🔗 **來源**
- 標題：I Am the Reason OpenAI Is Killing Unlimited Chats
- 作者／機構：gulmothrowaway
- 連結：https://chaosmanage.github.io/i-killed-unlimited-chatgpt/

#ChatGPT #MCP #ModelContextProtocol #OpenAI #Claude #AIagents #DeveloperTools #Automation #LLM #AIworkflow
