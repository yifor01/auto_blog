---
title: 'Beyond tree cover: mapping the world’s forest types'
source: Google DeepMind
url: https://deepmind.google/blog/beyond-tree-cover-mapping-the-worlds-forest-types/
model: claude-code/sonnet
generated_at: '2026-10-22T20:41:19.683756'
pinned: true
---

📌 【Google DeepMind 最新研究】AI 畫出全球森林的身分證

TL;DR:10 公尺解析度全球森林分類圖 ForTy,區分天然林、人工林與農林用地,準確率達 90%。

從衛星往下看,百年原始雨林、尤加利人工林和油棕園可能是同一片綠色。但它們儲存的碳量與承載的生物多樣性天差地遠,只看「有沒有樹」遠遠不夠。

🤔 **只看樹冠覆蓋,解決不了法規需求**

Google DeepMind 與 Google Research 指出,多數全球森林地圖只能回答「這裡有沒有樹」,但這對想保護天然林的人來說並不夠用。以歐盟的森林砍伐法規(EUDR)為例,它要求咖啡、可可、棕油等商品不能來自 2020 年後被轉為農地的森林;木製品如家具,也不能來自之後被轉為人工林或種植林的原始林,或轉為種植林的天然再生林。這代表企業與法規制定者需要知道的不只是哪裡有樹,還要知道那是什麼類型的森林,以及砍伐後被什麼取代。DeepMind 去年與世界資源研究所(WRI)、國際應用系統分析研究所(IIASA)聯合發布的 Natural Forests of the World 2020,只能回答「2020 年是否為天然林」這個二元問題。這次發布的 Forest Typology(ForTy)2020 則進一步做出分類,並搭配新的年度時間序列追蹤變化。

🧩 **六種類型,靠 AlphaEarth 嵌入辨認**

ForTy 依據聯合國糧農組織(FAO)的定義,把土地分成六類:原始林(無明顯人為干擾痕跡的原生林)、天然再生林(例如伐木或火災後自然長回的森林)、人工林(人為栽種、長週期管理的森林)、種植林(密集管理、常為單一樹種的快速生長林)、樹木經濟作物與混農林業(種植油棕、橡膠、可可、水果等非木材作物的農地),以及其他土地(草原、農地、城市、水域等)。

訓練這個模型的難點在於,這些分類部分取決於土地「如何被使用」,而非單純外觀。團隊建立了一套大規模森林類型範例資料集,包含約 170 萬個標註地點,來源涵蓋專家調查、國家與區域資料集,以及針對模型容易判斷錯誤地點的重點複查。模型採用專為遙測資料挑戰設計的客製架構,關鍵輸入是 AlphaEarth Foundations embeddings,把每個 10 公尺像素多年的衛星觀測資料壓縮成精簡摘要,藉此捕捉種植紋路、生長週期與採收節奏等細微線索。

📊 **9,000 個驗證點,準確率 90%**

DeepMind 與 IIASA、WRI 合作,在全球隨機選取超過 9,000 個地點進行驗證,每個地點由兩名受訓專家依據高解析影像與多年衛星紀錄判斷實際土地類型。結果顯示,ForTy 有 90% 的機率選出正確的森林類型,有 95% 的機率正確區分森林與非森林用地,表現優於其他全球森林地圖。

值得一提的是,ForTy 不是給出單一是非標籤,而是為每個類別提供機率分數,讓使用者能依區域情境與應用場景調整精確度門檻。例如評估 EUDR 風險的企業可以設定嚴格門檻,只採用模型高度確信的像素以降低法規風險;而估算整體森林面積的研究者則能運用完整的機率分布,取得更全面的景觀圖像。

除了 2020 年的單一時間點地圖,團隊也發布了 2017 至 2025 年的早期時間序列,不只顯示森林在哪裡消失或恢復,還能分辨變化的類型,例如天然林被砍伐後改種成人工林,或是廢棄土地逐漸自然恢復成森林。這點很關鍵,因為天然林被砍伐後重新栽種成人工林時,地表很快又會變綠,一般的樹冠覆蓋地圖偵測不到這種變化,而 ForTy 的時間序列能讓這類隱藏的變化現形。

⚠️ **時間序列仍是早期版本**

DeepMind 表示,這份時間序列目前仍是早期發布版本,團隊將在接下來幾個月與合作夥伴和使用者持續改進。

🎯 **實務啟示**

Forest Typology 2020 地圖與時間序列已在 Google Earth Engine 上以開放授權免費提供。對從事永續供應鏈、ESG 資料分析或地理空間機器學習應用的工程師來說,這是一份已經過驗證且準確率公開的全球土地分類資料,可以直接用來評估供應鏈砍伐風險、協助森林保育資金分配,或作為自建模型的標籤參考。

🔗 **來源**
- 標題:Beyond tree cover: mapping the world's forest types
- 作者/機構:Maxim Neumann and Charlotte Stanton, Google DeepMind
- 連結:https://deepmind.google/blog/beyond-tree-cover-mapping-the-worlds-forest-types/

#GoogleDeepMind #AIforNature #RemoteSensing #Deforestation #ForestTypology #GeospatialAI #ClimateTech #Sustainability #EarthEngine #MachineLearning
