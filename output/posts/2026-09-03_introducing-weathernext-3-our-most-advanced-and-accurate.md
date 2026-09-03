---
title: Introducing WeatherNext 3, our most advanced and accurate global weather AI
  model
source: Google DeepMind
url: https://deepmind.google/blog/introducing-weathernext-3-our-most-advanced-and-accurate-global-weather-ai-model/
model: claude-code/sonnet
generated_at: '2026-09-03T20:02:30.243099'
pinned: true
---

📌 【Google DeepMind】WeatherNext 3：用即時衛星取代六小時延遲預報

TL;DR：新一代天氣 AI 改用即時衛星資料，每小時更新，解析度提升 5 倍。

🎣 手機上顯示的降雨機率，很可能是基於六小時前的觀測資料算出來的。傳統數值天氣預報（NWP）仰賴超級電腦跑物理模擬，這個延遲讓快速變化的降雨、氣溫預測長期不夠精準。Google DeepMind 與 Google Research 發表 WeatherNext 3，試圖用完全不同的資料來源解決這個問題。

🤔 為什麼舊方法追不上天氣的變化速度
多數 AI 天氣模型（包括前代 WeatherNext 2）都是拿 NWP 模型的輸出當訓練資料，等於是在物理模擬的基礎上再學一層。但 NWP 本身有六小時資料延遲，對降雨、地表溫度這類變化快的變數容易產生偏差；而氣溫、濕度這種在幾公里內就可能劇烈變動的變數，傳統模型也因為訓練資料本身解析度不足而難以掌握地形細節。

🧩 直接吃即時衛星資料的 FGN 架構
WeatherNext 3 的核心改變，是讓模型不只學歷史再分析資料，還直接攝入即時、全球地球同步衛星的資料鑲嵌（mosaic），與歷史分析資料一起餵進單一、彈性的 Functional Generative Network（FGN）mesh transformer。這個架構同時輸出密集網格場、離散颱風路徑，以及站點層級的稀疏座標預測。解析度方面，氣溫、濕度等地表變數可達 5 公里、其他地表變數 10 公里、風速等大氣變數則為 25 公里，相較 WeatherNext 2 固定在 25 公里網格、每 6 小時更新一次的規格，整體畫面清晰度提升約 5 倍，且每小時就能產生一次新預報。

📊 英國氣溫圖：從模糊色塊到看得出地形
官方以英國 2 公尺氣溫預報為例，WeatherNext 2 在 25 公里解析度下呈現的是模糊、過度平滑的色塊，而 WeatherNext 3 在 5 公里原生解析度下能明確描繪地形細節。根據獨立即時評測機構 Brightband 的評比，WeatherNext 3 是目前最先進、最準確的全球天氣模型。

💡 站點資料補上偏鄉的空白
除了衛星，WeatherNext 3 也直接在稀疏的地面氣象站觀測資料上訓練，讓模型能在 5 公里網格上納入地形等區域細節。這對拉丁美洲、非洲、亞太等過去因區域模型運算成本過高而長期缺乏高解析度預報的地區特別關鍵。模型還新增了針對再生能源設計的變數：渦輪機高度（約 100 公尺）的風速預測，以及高解析度雲量與日照輻射量，讓電網調度與再生能源業者能更準確估算發電量、對接用電需求。

🎯 對工程師來說，這代表什麼
WeatherNext 3 已整合進 Search、Gemini、Maps、Google Maps Platform 與 Cloud。開發者不需要自己訓練天氣模型，就能透過 Google Cloud 直接呼叫這些每小時更新、5 公里解析度的預報資料，接入農業、物流、能源排程等下游應用。

🔗 來源
- 標題：Introducing WeatherNext 3, our most advanced and accurate global weather AI model
- 作者／機構：Google DeepMind
- 連結：https://deepmind.google/blog/introducing-weathernext-3-our-most-advanced-and-accurate-global-weather-ai-model/

#WeatherNext3 #GoogleDeepMind #WeatherAI #ClimateAI #Forecasting #GeospatialAI #RenewableEnergy #MachineLearning #SatelliteData #GoogleCloud
