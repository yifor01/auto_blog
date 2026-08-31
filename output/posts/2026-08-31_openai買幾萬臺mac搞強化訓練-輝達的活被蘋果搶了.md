---
title: OpenAI買幾萬臺Mac搞強化訓練！輝達的活被蘋果搶了
source: 量子位
url: https://www.qbitai.com/2026/08/481759.html
model: claude-code/sonnet
generated_at: '2026-08-31T12:12:55.878608'
score: 49
---

📌 輝達GPU搞不定的活，蘋果Mac mini接下了？

TL;DR：OpenAI、Anthropic傳出大量採購Mac mini與Mac Studio訓練「電腦操作Agent」，統一記憶體成關鍵優勢。

輝達GPU缺貨、Google TPU產能吃緊，這些是AI圈熟悉的劇本。但如果告訴你，有一種AI訓練任務連這兩家都搞不定，最後靠的是消費級的Mac mini，你會相信嗎？

🤔 **幾萬臺沒螢幕沒鍵盤的Mac，都去哪了**

根據The Information的消息，OpenAI已購入數以萬計的Mac mini與Mac Studio，且指定不要一體式的MacBook，專挑這兩款桌上型機種。量子位報導指出，不只OpenAI，Anthropic也透過AWS租用Mac mini執行類似任務。這些機器被用來訓練「computer-use agent」（電腦操作智慧體），也就是能自主操作電腦、編輯與測試程式碼、整理郵箱、總結文件等多步驟任務的AI系統，訓練方式正是強化學習。

這股需求也直接反映在蘋果財報上：最近一季Mac銷售額年增近29%，達到103億美元，成長速度超越iPhone、iPad等其他所有產品線，成為蘋果成長最快的業務。6月23日，蘋果總部還罕見舉辦了一場面向企業客戶的「Business at the Park」活動，迪士尼、福特高管，以及Anthropic共同創辦人Jared Kaplan都出席，Mac mini是整場活動的焦點。

🧩 **關鍵不是快，是記憶體架構不一樣**

量子位報導解釋，輝達GPU的視訊記憶體與系統記憶體是分開的，資料在兩者間傳輸會形成瓶頸；蘋果M系列晶片則採用單一共享記憶體池，CPU與GPU可直接存取同一塊記憶體，在處理AI工作負載時具備效能優勢。此外，Mac mini與Mac Studio配備專門散熱系統，長時間運行複雜AI任務不會因過熱而降頻，這對動輒需要連續數小時甚至數天的強化學習訓練來說相當重要。蘋果也在推廣開源專案EXO Labs，可將多臺Mac組成叢集，在本地執行萬億參數等級的模型；甫發布的新款Mac Studio也特別強調叢集能力。

💡 **輝達已經盯上了，蘋果卻還沒準備好**

報導提到，一位曾與輝達高管討論競爭情勢的知情人士透露，輝達已將蘋果視為本地AI領域最大的競爭對手，去年底發布外型與Mac mini相近的AI桌上型電腦DGX Spark，直攻這塊市場。而蘋果自己面臨的現實問題是供應跟不上——AI資料中心對記憶體晶片的巨大需求引發全產業歷史性短缺，高配版Mac mini與Mac Studio已缺貨數月。蘋果前AI產品企業行銷經理Todd Dailey透露，過去一年已有企業因Mac供應受限轉而尋找替代方案，DGX Spark是最常被提及、且目前有現貨的選項；他也提到蘋果在企業AI市場的爆紅完全是意外，公司內部並沒有專門面向企業客戶的工程團隊或開發者關係人員。

⚠️ **傳聞居多，蘋果自己也還沒想清楚怎麼接**

蘋果上一次販售伺服器產品，是2011年停產的Xserve，基於Mac的伺服器作業系統也已於2022年停止開發。即使已有前OpenAI基礎設施員工創辦Mount Thor這類基於蘋果硬體的雲端運算公司，蘋果自己用M系列晶片打造的伺服器目前也僅供內部Private Cloud Compute服務使用，對於企業客戶詢問能否購買使用權，蘋果目前一律拒絕。整起事件目前仍以業界傳聞與單一媒體報導為主，具體採購規模、合約條件等細節尚未獲蘋果、OpenAI或Anthropic正式證實。

🎯 **對工程師的啟示**

如果你的團隊正在評估computer-use agent或需要長時間強化學習訓練的工作負載，統一記憶體架構帶來的資料搬移優勢值得放進硬體選型的考量清單——但供應短缺與缺乏企業級支援，也代表這條路線目前還不是穩定的量產選項。

🔗 **來源**
- 標題：OpenAI買幾萬臺Mac搞強化訓練！輝達的活被蘋果搶了
- 作者／機構：夢晨，量子位
- 連結：https://www.qbitai.com/2026/08/481759.html

#AI #Apple #OpenAI #Anthropic #ReinforcementLearning #MacStudio #MacMini #UnifiedMemory #AIInfrastructure #Nvidia
