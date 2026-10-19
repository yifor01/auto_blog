---
title: Laplace Intelligence red-teams robots and self-driving cars before they hit
  the real world
source: TechCrunch AI
url: https://techcrunch.com/2026/10/19/laplace-intelligence-red-teams-robots-and-self-driving-cars-before-they-hit-the-real-world/
model: claude-code/sonnet
generated_at: '2026-10-19T21:46:44.900881'
score: 76
---

📌 用AI測試AI:Laplace Intelligence在模擬中「撞爛」自駕車與機器人

TL;DR:這家新創用模擬環境加AI agent，在機器人與自駕車部署前主動設計邊緣案例找出失敗點。

「想像一下，如果類似的事情發生在實體世界。」Laplace Intelligence的CEO Howie Sun,用OpenAI與Hugging Face之間曾發生的事件當作警示——當AI agent從電腦走進實體世界，失控的代價不再只是當機，而可能是真實世界的事故。

🤔 **AI agent正在走出電腦,但沒人想讓它在現實世界裡失敗**

Sun告訴TechCrunch,隨著AI agent從純軟體走向機器人、自駕車等實體場域，確保這些「physical AI」安全的唯一辦法，是讓AI去測試AI。Ann Arbor的Laplace Intelligence做的正是這件事:為機器人與自駕車打造自動化紅隊測試（red-teaming）——刻意嘗試讓系統失敗，藉此在部署前找出問題並修正。Sun表示，公司的目標是「幫助企業在部署前發現並修正問題,並隨時間建立一套客戶、保險公司與監管機構都能信任的共同證據基礎」。

🧩 **核心:用NVIDIA Cosmos重建的高擬真模擬,加上主動找破綻的AI agent**

Laplace的核心是一套從真實世界重建的高擬真模擬環境，搭配不斷探測弱點與失敗點的AI agent。這套模擬環境是NVIDIA的AI世界模擬平臺Cosmos的後訓練（post-trained）版本，並以真實世界資料為基礎——可以重建從亞利桑那州高速公路到巴黎行人穿越道的任何場景。模擬方式是混合多種真實世界資訊:例如用一張Google街景圖作為參考，生成整條街道,再結合真實地圖資料，確保生成的環境符合真實比例，而不是隨機產生。開發者可以用語言prompt即時修改場景設定，比如加入下午時段的車流。Sun也提到，Laplace會從TomTom等導航服務商拉取即時交通與壅塞資訊。

這套模擬不只環境是模擬的，其他行動者的行為也是。在一次演示中，Sun指示測試用的agent車輛切入對向車道，而原本會被撞上的那輛車主動避開——這正是這套系統被稱為「互動式模擬環境」的原因:所有角色都在對彼此的行動做出反應，更像是一個有互動參與者的世界模型，而不是單純的場景重播。

💡 **真正的差異化:讓AI自己設計邊緣案例,把人推出決策迴圈**

文章指出，Laplace真正的獨特賣點，是用來自動設計corner case（可能讓AI系統出錯的罕見棘手場景）的AI agent，把人進一步推出測試迴圈之外。Sun表示，這些agent「可以從新聞、警方事故報告等各種資訊來源取材，主動挑戰自駕車與其他physical AI」。目前自駕車業者多半是用錄下的真實行車紀錄轉成模擬，或是靠人力想出新的邊緣案例來訓練AI應對；雖然已有像自駕卡車公司Waabi這類業者開始用AI生成邊緣案例，但Sun認為，當通用型機器人開始進入真實世界時，這項技術的需求會更加明顯——因為「通用機器人的資料更少，沒有人知道真實世界裡的邊緣案例會是什麼樣子」。

📊 **已有實際營收,競爭對手是估值150億美元的Applied Intuition**

Sun與共同創辦人、首席科學家Henry Liu在密西根大學成立Laplace，至今約一年。Sun過去八年都在學界研究如何在模擬中挑戰自駕AI，並於2023年與當時的博士指導教授Liu共同發表一篇登上《Nature》封面的相關論文，之後開始收到自駕車公司的合作邀約，促使他把研究轉為產品。文章指出，Laplace目前已經有營收,甚至有小幅盈利，主要客戶來自自駕車領域,包括德州自駕卡車公司Bot Auto與一家日本大型汽車製造商；同時也與NVIDIA、T-Mobile合作，在加州聖荷西進行一項免費的智慧城市試點，提供高階交通營運資訊，並正在與開發倉儲用人形機器人的夥伴展開早期合作。目前多數合約是專案制，公司正朝經常性收入轉型。該領域的主要競爭對手是估值達150億美元、累計募資12億美元的Applied Intuition。

🎯 **實務啟示**

對從事機器人或自駕系統安全測試的工程團隊而言，Laplace的案例點出一個趨勢:邊緣案例的設計本身，正從「人力發想加錄影重播」轉向「AI主動生成並即時互動反應」。如果你的測試管線仍高度依賴錄製好的真實行車資料，值得思考如何引入能根據新聞、事故報告等外部資訊主動生成新場景的機制，而不是被動等待資料累積。

🔗 **來源**
- 標題：Laplace Intelligence red-teams robots and self-driving cars before they hit the real world
- 作者／機構：Rebecca Bellan, TechCrunch
- 連結：https://techcrunch.com/2026/10/19/laplace-intelligence-red-teams-robots-and-self-driving-cars-before-they-hit-the-real-world/

#AutonomousVehicles #Robotics #RedTeaming #PhysicalAI #AISafety #SimulationTesting #NVIDIA #SelfDrivingCars #StartupBattlefield #AIAgents
