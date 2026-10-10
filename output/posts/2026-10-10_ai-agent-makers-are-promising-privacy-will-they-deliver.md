---
title: AI agent makers are promising privacy — will they deliver?
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/1009051/privacy-ai-agent-promises-openai-meta-muse-dots
model: claude-code/sonnet
generated_at: '2026-10-10T20:47:30.118211'
score: 63
---

📌 Meta Muse 與 OpenAI Dots 互相喊話「我們更懂隱私」,誰說到做到?

TL;DR：AI agent 大廠紛紛以「比對手更重視隱私」當作賣點,但 Meta Muse 上線後的多起資料外洩與過度蒐集事件,暴露出承諾與實際落差。

當 AI agent 需要存取你的信箱、銀行資訊、聊天記錄才能真正幫上忙,各家廠商打的行銷戰已經不是「誰更聰明」,而是「誰更不會把你的資料搞丟」。The Verge 的報導把這場隱私軍備競賽的落差攤開來看。

🤔 **一場接一場的「我們比對手安全」喊話**

在今年 OpenAI DevDay 上,CEO Sam Altman 發布新 agent 產品 Dots,宣稱公司要「為前沿 AI 的隱私樹立新標準」,會上也多次暗指競爭對手 Meta 的 Muse 未能保護好使用者資料。但諷刺的是,Muse 本身在幾個月前上線時,也是以「比前身 OpenClaw 更安全的替代方案」自我定位,Mark Zuckerberg 當時更直接宣稱 Muse「從一開始就是為隱私與安全而打造」。Meta Superintelligence Labs 產品負責人 Nat Friedman 在 X 上寫道,Muse 的目標就是打造一個「像 OpenClaw,但能做到安全、可規模化到數十億使用者」的產品。

📊 **Muse 的實際表現:資料隔離,但 Meta 自己仍能存取**

根據報導,Muse 的使用者資料被存放在一臺隔離的 Linux 虛擬機上,Zuckerberg 形容為「有獨立瀏覽器、CPU、記憶體與儲存空間的隔離電腦」,公司也表示今年稍後會推出能「以密碼學方式可驗證地阻擋 Meta 自己存取」的機制——但目前 Meta 本身仍能存取這些資料。Muse 上線後迅速登上 App Store 排行榜,根據 Apptopia 數據,在美國短短數週內新增 60 萬名每日活躍使用者,但同時也被研究人員迅速發現一個可被用來完全控制 Muse 的零日漏洞(已修補)。據 404 Media 報導,上線前最後一刻還冒出多起嚴重安全問題,其中一個甚至可能讓使用者存取到 Meta 自家的內部資料庫。此外,Muse 預設允許 Meta 用使用者輸入的內容訓練模型(可手動關閉);一名 Inc. 記者投訴 Muse 在他沒有要求的情況下讀取並上傳了他的私訊;一名 YouTuber 則發現 Muse 透過 Marketplace 把他的地址提供給陌生人——在兩起案例中,Muse 都被形容為「如預期般運作」,只是使用者沒料到它會做到這種程度。Wired 的報導也指出,Muse 會建立「所有朋友與家人的詳細檔案」。

🧩 **OpenAI Dots 想走不同路線,但使用規模也小得多**

OpenAI 這邊,Codex 產品負責人 Alexander Embiricos 在 DevDay 臺上強調公司專注打造「最值得信任、最安全的助理」,Altman 也示範了使用者可以為自己的 Dots 設定規則,例如「單筆消費不得超過某個金額」。OpenAI app 平臺負責人 Glen Coates 則表示,OpenAI 目前情況和 Meta 不同,因為 Meta 已經有一款擁有 12 億使用者的 AI 產品,「推出一個會犯下那種錯誤的東西,是我們會盡力避免的」。針對企業客戶,OpenAI 也提出「更強的資料控制權」框架與零資料保留政策選項(資料完全不留存在 OpenAI 伺服器上)。目前 Dots 還沒有爆出重大隱私事件——不過報導也指出,這或許和它目前僅限每月 100 美元以上訂閱層使用、使用者基數本來就小有關。The Verge 記者 Allison Johnson 也提到,在 Dots 要求輸入銀行資訊以完成任務時,她仍感到不自在(Muse 則是透過 Stripe 整合處理付款)。

💡 **不是所有廠商都選擇打隱私牌**

報導也提到,另一家 agent 廠商 Instinct 曾因服務條款被指過於寬鬆、形同讓公司能無限制存取使用者資料而遭到公開批評,此後該公司似乎已做出調整。整體而言,報導總結出目前 AI 實驗室推廣 agent 給一般大眾的三部曲策略:做得有用、做得可愛讓人卸下心防,再加上隱私承諾——然後寄望這些承諾真的能兌現。

🎯 **對工程師與產品團隊的啟示**

如果你的團隊正在打造或整合 AI agent,這篇報導是一個提醒:隱私文案與實際的資料存取架構之間,中間還有一大段距離要靠工程落實——包括預設行為(opt-in 還是 opt-out)、權限邊界是否真的被尊重,以及上線前的安全測試是否足夠扎實。對使用者而言,「某家公司說自己比對手更重視隱私」本身並不是一個可驗證的保證。

🔗 **來源**
- 標題：AI agent makers are promising privacy — will they deliver?
- 作者／機構：Hayden Field, The Verge AI
- 連結：https://www.theverge.com/ai-artificial-intelligence/1009051/privacy-ai-agent-promises-openai-meta-muse-dots

#AIAgent #Privacy #Meta #OpenAI #Muse #Dots #DataSecurity #TechPolicy #AIethics #BigTech
