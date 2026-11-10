---
title: 'What Frontier Labs Buy: A Data Deep Dive with Handshake AI — Garrett Lord
  & Team'
source: Latent Space
url: https://latent.space/p/handshake/
model: claude-code/sonnet
generated_at: '2026-11-10T01:06:18.464545'
score: 82
---

📌 Frontier Labs砸10億美元買的，其實是這種資料

TL;DR：Handshake AI一年內把資料訓練業務做到10億美元年化營收,Latent Space深度訪談拆解RL訓練環境怎麼設計。

短短一年,一家專門提供「人類專家資料」的公司,把營收衝到10億美元的毛年化規模。這集Latent Space的深度訪談,直接把產線攤開給聽眾看。

🤔 frontier labs到底在買什麼

這是Latent Space第一次與AI資料公司做深度對談。Handshake的AI訓練業務在大約一年內,從上線衝到10億美元毛年化營收（gross annualized revenue）。因為Handshake的業務橫跨科學、工程、研究、金融等多個領域,節目特別串連了Latent Space旗下多位主持人共同製作,分段呈現Finance、Bio、Coding三個現場示範,外加Alignment（安全對齊）收尾,主持與來賓包括創辦人Garrett Lord、Sahil Bhaiwala、Nishant Ranka、Nick Magazine、Jonas Mueller、Collin Schweiker、Steve Kelling等人。

🧩 三個示範：金融試算表、腦組織切片、Coding環境

Finance環節裡,在模擬投資銀行情境Project Falcon中,Agent要從銀行信件裡找出自己的任務指派,判斷哪些檔案才是真正規範這筆交易的依據,再交出一份工作表。節目示範了一個典型錯誤:客戶信件裡提到一筆既有商譽(goodwill)數字,Agent把它直接帶進Python程式碼裡做了減法運算。問題不在於它不懂稅務處理,直接問它反而能講清楚規則,而在於它沒意識到眼前這段程式碼正是該套用這條規則的地方。

Bio環節由Nick Magazine與Jonas Mueller展示VIALS,這是Handshake用來評測模型解讀科學影像能力的基準。節目現場把9張腦腫瘤組織切片放上螢幕,請模型判斷哪兩張的血管壞死（vessel necrosis）程度最嚴重,正確答案是H和I,而模型選出了H、I,卻多加了一個G。

Coding環節由Steve Kelling與Nishant Ranka主持,在一個模擬的檔案存取任務中,團隊檢查的不只是Agent最後回答了什麼,而是它實際讀取了哪些檔案、有沒有核對副本,以及事後對shell history做了什麼。單看最終回覆的逐字稿,會漏掉大部分真正需要評估的行為細節。

📊 節目也提到另一筆已公開的案例Project Osprey,完整追蹤一筆交易從客戶信件到最終評分決策的全過程,並有ATLAS-Finance這個橫跨模擬銀行信箱、文件、財務模型的基準供外部探索,涵蓋的討論主題還包括frontier labs怎麼採購資料、如何評估新資料集、如何用開源模型測試資料品質、以及rubrics評分與專家判斷之間的落差。

💡 錯誤往往不是不懂規則,而是不知道規則該套用在哪

這幾個示範有個共同點:無論是財務減法算錯、組織切片多選一張,還是程式碼讀寫軌跡,問題往往不是模型「不知道規則」,而是不知道規則要套用在眼前這個具體情境。這類錯誤比單純的知識缺口更難靠放大模型規模解決,也正是Handshake建構這些RL訓練環境與評測基準的著力點。

⚠️ 材料中沒有提供這些評測項目的具體分數或對比baseline數字,僅呈現節目描述的案例與錯誤模式,實際量化表現需參照Handshake自家公開的基準資料。

🎯 實務啟示

對正在設計agent評測或RL訓練環境的工程師而言,這場對談提供了一個具體提醒:只看模型最終輸出容易高估能力,真正有鑒別力的評測要追蹤工具呼叫軌跡、中間決策與副作用,像是改了哪個檔案、動了哪段shell history,這些才是分辨「模型懂不懂」與「模型會不會用」的關鍵。

🔗 來源
- 標題：What Frontier Labs Buy: A Data Deep Dive with Handshake AI — Garrett Lord & Team
- 作者／機構：Latent Space
- 連結：https://latent.space/p/handshake/

#AITrainingData #RLHF #FrontierLabs #HandshakeAI #DataLabeling #AIEvaluation #AgenticAI #MachineLearning #LLM #AIBenchmark
