---
title: 'Introducing OlmoEarth embeddings: Custom embedding exports from OlmoEarth
  Studio for downstream analysis'
source: HuggingFace Blog
url: https://huggingface.co/blog/allenai/olmoearth-embeddings
model: claude-code/sonnet
generated_at: '2026-08-13T07:40:52.203893'
score: 66
---

📌 OlmoEarth Embeddings：地球觀測資料也能免訓練直接查詢

TL;DR：OlmoEarth Studio 新增 embedding 匯出功能，讓衛星影像分析不用重新訓練模型就能上手。

不用標記資料、不用微調模型，只靠一個 dot product，就能在整張地圖上找出「長得像這裡」的所有地點。這正是 Allen Institute for AI（Ai2）旗下 OlmoEarth Studio 這次釋出的 embedding 匯出功能想解決的問題。

🤔 **地球觀測模型的門檻，卡在「怎麼用」而不是「準不準」**

OlmoEarth 是 Ai2 開源的地球觀測基礎模型，原始碼與模型權重已隨技術報告一併公開。但對多數團隊而言，直接部署基礎模型做下游任務仍有成本門檻。Embeddings（向量表示）被官方定位為「快速、低成本的切入點」：把每個像素轉成一組數值向量，地表特徵相似的地點在向量空間中距離相近，不同的則相距遙遠，後續可以直接拿來做相似度搜尋、分割、無監督探索等任務。

🧩 **在 Studio 裡設定幾個參數，就能拿到一份向量地圖**

計算 embeddings 的流程與 Studio 裡其他預測任務相同：設定模型、執行、下載結果。可調整的參數包括：

- 感興趣區域：手繪或上傳任意多邊形，Studio 負責影像取得與拼接
- 時間範圍：1 到 12 個月週期，可捕捉季節變化而非只有年度快照
- 編碼器版本：Nano（128 維，140 萬參數）、Tiny（192 維，620 萬參數）、Base（768 維，8900 萬參數）
- 空間解析度：10、20、40、80 公尺
- 影像來源：Sentinel-2 L2A、Sentinel-1 RTC，或兩者並用

輸出格式是 Cloud-Optimized GeoTIFF（COG），每個 embedding 維度對應一個波段，向量以 int8（-127 至 127，-128 保留給 nodata）量化儲存，需要浮點數時可用 olmoearth_pretrain 套件裡的 dequantize_embeddings 還原。由於每次都是即時運算而非查詢預先算好的全域資料庫，輸出結果能精準對應你關心的時空條件。

📊 **四個實際案例：從相似度搜尋到變化偵測**

文章示範的所有案例都使用 OlmoEarth-v1-Tiny（192 維）、40 公尺解析度、Sentinel-2 L2A 合成影像：

- **相似度搜尋**：在加州 Merced 附近選一個查詢點，計算與其他所有像素的餘弦相似度，城市紋理與道路廊道清楚亮起，農業地塊則保持低相似度，模型無需任何標籤就能區分建成地表與農地。換到農業地塊查詢，相似度 0.89 以上全是灌溉農田，接近零的則是機場周邊裸地、乾涸水庫與乾旱牧地。
- **少樣本分割**：在越南金甌（Ca Mau）紅樹林區域，僅標記 60 個像素（每類別 20 個），以 ESA WorldCover 2021 作為標籤來源，訓練一個帶標準化的邏輯迴歸分類器，對整個區域逐像素預測，得到加權 F1 = 0.84 的地表覆蓋圖。標籤數從 30 增加到 300，準確率幾乎沒有變化，顯示大部分工作是 embedding 本身完成的。
- **變化偵測**：分別計算 2023 年 9 月與 2024 年 9 月的月度 embeddings，逐像素比較餘弦距離，加州 Butte County 的 Park Fire 燒毀範圍立即顯現，全程無需標籤或訓練。
- **無監督探索**：對荷蘭 Flevoland 圩田地景做 PCA 降到三維並映射為 RGB 假色影像，規則的農業地塊網格與作物類型、水體、城市區域各自呈現不同色調。

💡 **少量標籤就能訓練出可用分類器，說明了什麼**

金甌案例中，60 個標記像素透過線性分類器（linear probe，基礎模型的標準評估方式）就能還原地表覆蓋邊界。這代表 Tiny 編碼器在預訓練階段，已經把這些生態學上的區分組織進了 192 維空間；作者也提到參數量更大的 Base（768 維）能編碼更豐富的表示。

⚠️ **仍有前提：自訂匯出需要 Studio 存取權**

自訂計算的 embeddings 目前僅限 OlmoEarth Studio 使用者使用，有興趣的團隊需要另外申請存取權；若不想透過 Studio，文中也提供了用公開釋出的 OlmoEarth 模型自行計算 embeddings 的說明連結。

🎯 **實務啟示**

對於需要處理衛星或空拍影像但沒有大量標註資料的團隊，embeddings 是比端到端訓練更快驗證可行性的路徑：先用相似度搜尋或 PCA 假色圖確認模型是否捕捉到你關心的地表特徵，再視需求決定是否要做少樣本分類或進一步微調。

🔗 **來源**
- 標題：Introducing OlmoEarth embeddings: Custom embedding exports from OlmoEarth Studio for downstream analysis
- 作者／機構：Kyle Wiggers, Ai2 Comms（Allen Institute for AI）
- 連結：https://huggingface.co/blog/allenai/olmoearth-embeddings

#OlmoEarth #EarthObservation #FoundationModels #Embeddings #GeospatialAI #RemoteSensing #Ai2 #FewShotLearning #SatelliteImagery #MachineLearning
