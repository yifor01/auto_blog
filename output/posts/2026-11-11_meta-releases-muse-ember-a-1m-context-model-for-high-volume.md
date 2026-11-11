---
title: Meta Releases Muse Ember, a 1M-Context Model for High-Volume Agent Work
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/09/meta-muse-ember-small-agent-model/
model: claude-code/sonnet
generated_at: '2026-11-11T23:50:25.720440'
score: 100
---

📌 Meta推Muse Ember:百萬context、三分之一成本的agent小模型

TL;DR:Meta新發布Muse Ember,百萬token context的多模態推理模型,專打agent裡的重複性子任務,成本效益看齊Claude Haiku 5.5。

當agent要跑成千上萬次工具呼叫、routing、文件解析這類重複性工作,用大模型跑太貴、小模型又不夠聰明。Meta Superintelligence Labs這次直接針對這個痛點,推出了目前Muse系列裡最小、最有效率的一款模型:Muse Ember。

🤔 背景:agent工作流需要分工,而非一個模型打天下

Meta將Muse Ember定位在工具呼叫、程式碼子任務、routing、資訊擷取與長文件解析這幾類高量、重複的agent子任務上。Meta自己的說法是:Muse Wonder負責規劃,Muse Ember負責跑量。這是Muse品牌第四款模型,排在Spark、Glimmer、Wonder之後,定位在Meta較大模型之下。

🧩 架構:第一個用Muse Wonder Full訓練出來的模型

Muse Ember是Meta第一個使用自家最大模型Muse Wonder Full訓練出來的模型。它原生支援文字、圖片、音訊與影片輸入,一個agent可以直接讀螢幕截圖、圖表、掃描文件或會議錄音,不需要額外接一個專門模型,也能透過螢幕截圖操作桌面應用程式。Context window達到100萬token,足以把整個程式碼庫或一整批文件塞進單次呼叫;輸出上限則到51.2萬token,是另外兩家對手(128K上限)的4倍。

📊 數據:同等分數,成本只要三分之一

依Meta公布、並由Artificial Analysis驗證的資料(皆為max reasoning effort下的結果):

| 模型 | Artificial Analysis Intelligence Index | 每任務成本 |
|---|---|---|
| Muse Ember | 35.8 | $0.136 |
| Claude Haiku 5.5 | 36.2 | $0.411 |
| GPT-6 Luna(最佳設定) | 27.8 | $0.152 |

Artificial Analysis將此總結為「分數打平Haiku,成本只要三分之一」;以Index分數來看,Muse Ember的36分與Claude Haiku 5.5在max effort下的表現相當。

價目表上,Muse Ember每百萬input token收費$0.10、output token收費$0.50,快取輸入則是每百萬token $0.004,這個基礎費率其實與Claude Haiku 5.5、GPT-6 Luna相同。報導指出,既然基礎單價一樣,成本差距只能來自每個任務實際耗用的token量。長文本情境下差距更明顯:Haiku 5.5在輸入超過10萬token後,費率會跳到$0.50與$2.50;GPT-6 Luna則在輸入超過27.2萬token後雙倍計價;而Meta目前未對Muse Ember列出長上下文加價層級。

🎯 實務啟示

對正在用LLM跑高量agent子任務(工具呼叫、routing、擷取、文件解析)的團隊來說,Muse Ember提供了一個分數打平中階模型、成本大幅下降的選項,尤其在長prompt場景下,沒有額外長上下文加價這件事本身就值得納入成本試算。Muse Ember已上架Meta Model API,並整合進Meta的程式碼agent Muse Code,支援Responses API;早期合作測試夥伴包括Box、Cline、Oracle、Cloudflare與You.com,可作為落地參考。

🔗 來源
- 標題:Meta Releases Muse Ember, a 1M-Context Model for High-Volume Agent Work
- 作者/機構:Asif Razzaq / MarkTechPost
- 連結:https://www.marktechpost.com/2026/11/09/meta-muse-ember-small-agent-model/

#Meta #MuseEmber #AIAgents #LLM #MultimodalAI #AgenticAI #MachineLearning #AIInfrastructure #ArtificialIntelligence #GenAI
