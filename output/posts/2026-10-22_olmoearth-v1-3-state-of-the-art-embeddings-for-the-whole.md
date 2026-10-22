---
title: 'OlmoEarth v1.3: State-of-the-art embeddings for the whole planet'
source: HuggingFace Blog
url: https://huggingface.co/blog/allenai/olmoearth-v1-3
model: claude-code/sonnet
generated_at: '2026-10-22T20:46:46.098839'
score: 97
---

📌 Ai2 把整顆地球的衛星影像壓成向量,開源給任何人用

TL;DR：OlmoEarth v1.3 提供全球衛星 embedding,免 GPU 就能在瀏覽器裡追蹤地表變化。

秘魯馬德雷德迪奧斯省的非法採金活動,2017、2018 年一度在坦博帕塔國家保護區緩衝區清除了超過 1,200 公頃的森林,2019 年政府行動一度壓下去,但問題是——它真的停下來了嗎?現在,不需要訓練任何模型,只要拉出兩個年份的 embedding 向量做比較,答案就會自己浮現出來。

🧩 **一年的衛星時間序列,壓成一個 128 維向量**

OlmoEarth v1.3 是 Ai2 推出的最新衛星 embedding 模型。模型讀入一整年的雷達(Sentinel-1)與多光譜(Sentinel-2、Landsat)時間序列資料,為地球上每一個 10 公尺像素產生一個 128 維向量;其中前 64 維也能單獨當作較小的 embedding 使用。架構上,先用 vision transformer 讀取衛星資料,再透過一個 Attention Pooler 把資訊匯聚成每個地塊(patch)的一個向量,最後用一層線性層壓縮成 128 個數字。

過去要用 OlmoEarth,主要途徑是在 OlmoEarth Studio 裡針對每個任務微調模型,再跑過衛星影像產出地圖,這需要 GPU 算力,還要下載、儲存大量影像資料。Embedding 模型把這個流程反過來:衛星資料先被壓縮成可重複使用的特徵向量,之後要做作物地圖、土地覆蓋地圖或變化分析,只需要在 embedding 上訓練一個輕量分類器,就能在本機跑起來。

📊 **27 項評測中拿下 20 項第一,訓練成本卻降了**

Ai2 team 把 OlmoEarth v1.3 的 embedding 拿去和 AlphaEarth Foundations(AEF)、Tessera v2 做對比,涵蓋六大洲的 27 項評測任務。128 維版本在 27 項中拿下 20 項最高分,整體排名第一；64 維版本,尺寸只有一半,仍在 18 項中領先。這次評測也新增了 PLANTEUR,一個針對熱帶農業的作物類型基準,結果顯示 OlmoEarth 的 embedding 在分類器從未見過的地點上泛化能力最好。模型權重、預訓練資料與預訓練程式碼全部公開。

訓練成本方面,OlmoEarth v1.3 是目前最便宜的一代,只用了前代 v1.2 訓練時間的 53%,以及第一代 v1 的 18%,碳排放也分別降到 50% 與 22%。即便如此,它在微調任務上的表現仍與 v1.2 打平,沒有因為省成本而讓精度打折。文中提到,若要重現最終版本的預訓練,大約需要花費 2,720 美元租用 H100 算力。

💡 **從採金活動看 embedding 怎麼當「免訓練」的變化偵測工具**

文章以秘魯坦博帕塔保護區的採金活動為例:比較每個像素在不同年份的向量,完全不需要重新訓練模型。2017 到 2020 年的比較清楚亮出採礦向東南擴張的區域;換成 2020 到 2025 年的比較,訊號明顯轉移——原本擴張的角落安靜下來,但根據 Amazon Conservation 的 MAAP 監測計畫,西北角的部分礦區仍在運作,舊礦區也持續在變化,一部分是林地恢復,一部分是重新開挖。2026 年 8 月,美聯社報導秘魯已派海軍巡邏隊重返保護區,因為檢察官發現採礦活動已侵入坦博帕塔本體。

🎯 **怎麼拿來用:Embeddings Explorer 與 OlmoEarth Studio 分工**

這次發布同時推出了瀏覽器工具 OlmoEarth Embeddings Explorer,把 embedding 渲染成一張 false-color 地圖,可以任意平移、切換年份比對、疊上原始 Sentinel-2 影像核對,也能點選一個地點找出相似區域,或標幾個點直接訓練一個小分類器,結果可匯出成 GeoTIFF,全程不需要帳號或環境設定。過去驗證一個想法常要跑一次微調,動輒數小時;在 Explorer 裡第一次嘗試只要幾秒鐘,整個區域的分析只需要少量標籤,不需要 GPU。

背後的資料庫以 10 公尺解析度儲存,每年約 150 TB,涵蓋陸地與鄰近海岸水域。目前 2025、2024、2023 年已是全球覆蓋,2017 到 2022 年則覆蓋部分國家,未來會持續擴充。每一筆 embedding 都附有來源記錄,每個 20 公里的 tile 與年份都列出所讀取的 Sentinel-1、Sentinel-2、Landsat 場景,並連結回公開資料目錄,方便追溯任何一個像素背後的原始影像。若任務需要特定時間窗、特定模態或解析度,OlmoEarth Studio 仍可針對需求跑同一個模型,整套授權延續 v1 與 v1.2 使用的 OlmoEarth Artifact License。

🔗 **來源**
- 標題：OlmoEarth v1.3: State-of-the-art embeddings for the whole planet
- 作者／機構：Ai2（HuggingFace Blog）
- 連結：https://huggingface.co/blog/allenai/olmoearth-v1-3

#OlmoEarth #SatelliteEmbeddings #GeospatialAI #RemoteSensing #FoundationModels #OpenSource #ClimateAI #Ai2 #EarthObservation #MachineLearning
