---
title: Can Safeworld convince people that GenAI robots won’t hurt them?
source: TechCrunch AI
url: https://techcrunch.com/2026/10/05/can-safeworld-convince-people-that-gen-ai-robots-wont-hurt-them/
model: claude-code/sonnet
generated_at: '2026-10-05T23:31:36.009653'
score: 68
---

📌 【CMU 安全實驗室出手】給生成式 AI 機器人做「碰撞測試」的新創

TL;DR：Safeworld 用模擬測試評估機器人的生成式 AI 控制系統安不安全,獲 1200 萬美元種子輪。

當機器人的「大腦」從傳統演算法換成生成式 AI 模型,工程師面臨一個新難題：這套系統的行為不再是可預測的 if-else,而是機率性的輸出。如果你家裡或工廠裡的人形機器人,其決策核心本質上是「猜」出來的,你要怎麼確保它不會撞到人?

🤔 **生成式 AI 讓機器人變聰明,也變得難以驗證**

卡內基梅隆大學（Carnegie Mellon University）Safe AI Lab 主任 Ding Zhao,與資深新創高層 Kyle Wong、機器學習工程師 Simo Rachidi 共同創立 Safeworld,正是為了解決這個問題。Zhao 指出,挑戰分兩層:第一是如何為機率性的生成式 AI 系統做風險評估（underwrite the risk）；第二是「信任」問題，而要讓機器人真正被部署,這兩者缺一不可。這個情境類似 Tesla、Wayve 等自動駕駛公司要處理的「長尾邊緣案例」,但 Zhao 認為機器人更棘手,因為它們活動在非結構化環境中,而且每個場域（工廠、倉庫、家庭）的安全標準都不一樣。

🧩 **把工廠的轉角搬進 Genesis 或 MuJoCo**

Safeworld 的做法是把真實場景「數位化」。舉例來說,Wong 提到工廠裡常見的痛點是「視線死角的轉角」:機器人需要多快的速度、多短的停止距離,才能確保不會撞上一位可能正抱著箱子、看不到機器人的工人?為了回答這類問題,Safeworld 會在 Genesis 或 MuJoCo 這類模擬環境中重建該場域的數位版本,放入由機器人真實軟體驅動的模擬體,再跑上千次「人類模型遇上機器人」的情境,包括人突然跌倒、絆倒等難以在現實中反覆重現的意外狀況。

📊 **1200 萬美元種子輪,拉到業界實際客戶**

這輪種子輪募得超過 1200 萬美元,由 Shine Capital 與 a16z Speedrun 領投,Box Group、Carnegie Mellon University Endowment、Innovation Endeavors、SV Angel 等跟投。a16z Speedrun 合夥人 Jonathan Lai 表示,建立產業安全標準要趁機器人還在設計與部署階段的現在進行,等到家用機器人真的撞到小孩造成事故,就太晚了。目前已有實際合作對象:Gritt Robotics 的 CTO Vishal Dugar,他們正在開發協助工人在大型太陽能廠安裝光伏板的機器人 AI 大腦,並與 Safeworld 合作建立安全模擬。Dugar 坦言,他們的系統很難用數學公式「形式化證明」安全性,必須靠經驗性（empirically）的大量場景測試來驗證,因為現場的人類姿態、衣著、身形、動作變化太多樣。

💡 **第三方驗證的價值,可能比技術本身更關鍵**

Safeworld 的模擬測試能力,其實跟許多機器人公司內部已經在做的事情有相似之處。但創辦團隊的論點是:即便技術上重疊,機器人製造商仍會需要一個「第三方」來背書,原因之一是同業之間不會把各自的安全測試細節互相分享,而中立的驗證者能扮演「安全案例」（safety case）的中介角色。Zhao 更直言,真正該擔心的不是展示間裡那臺表現完美的 demo 機器人,而是大規模部署後,面對從未操作過機器人的一般使用者時的真實狀況。

⚠️ **商業模式仍在摸索,技術成熟度待觀察**

目前 Safeworld 仍在決定產品形態：要做成讓外部客戶自行使用的平臺,還是以服務（services）形式交付?這也反映出整個「生成式 AI 驅動機器人」賽道還處於早期階段,安全評估的方法論和標準尚未定型。

🎯 **給工程師的啟示：把安全評估當成 CI/CD 的一環**

對正在開發機器人控制系統的工程師來說,這個案例提醒一件事:當控制核心換成機率性的生成式 AI,傳統的單元測試與規則驗證已經不夠,需要像自動駕駛產業那樣建立「情境庫＋大規模模擬」的測試基礎設施,並且越早把安全驗證納入開發流程,越能避免後期出現難以挽回的真實世界事故。

🔗 **來源**
- 標題：Can Safeworld convince people that GenAI robots won't hurt them?
- 作者／機構：Tim Fernholz, TechCrunch AI
- 連結：https://techcrunch.com/2026/10/05/can-safeworld-convince-people-that-gen-ai-robots-wont-hurt-them/

#GenerativeAI #RobotSafety #Robotics #AISafety #SimulationTesting #StartupFunding #CarnegieMellon #HumanRobotInteraction #AgenticAI #EdgeCaseTesting
