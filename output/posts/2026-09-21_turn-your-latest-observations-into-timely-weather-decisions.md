---
title: Turn Your Latest Observations Into Timely Weather Decisions With NVIDIA Earth-2
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/turn-your-latest-observations-into-timely-weather-decisions-with-nvidia-earth-2/
model: claude-code/sonnet
generated_at: '2026-09-21T21:22:24.422367'
score: 75
---

📌 【NVIDIA】用即時觀測資料，讓天氣預報跟上分秒變化

TL;DR：NVIDIA Earth-2 的 AI 資料同化工具讓你把自己的觀測資料塞進擴散模型，即時修正天氣預報。

氣象數值分析（numerical analysis）通常要花上大量運算時間，而且只在固定時段釋出，比如每六小時一次。但風場、太陽能場站的感測器,或雷達，其實隨時都在產生更即時、更貼近在地的資料。問題是：這些資料要怎麼有效餵進既有的預報模型，而不用整套重新訓練？

🤔 **為什麼「等下一次分析」不夠用**

能源公司從風場與太陽能資產蒐集量測資料，緊急應變團隊仰賴雷達與在地感測器，衛星業者則持續觀測地球，這些資料理論上能提供比官方數值分析更早、更貼近特定地區的訊號。但傳統做法要嘛等待固定排程的分析結果，要嘛得重新訓練整個預報模型才能吸收新的觀測型態。NVIDIA Earth-2 提出用 AI 資料同化技術，在不重訓模型的前提下，把這些觀測即時「揉進」既有的擴散式（diffusion）預報或降尺度（downscaling）模型。

🧩 **核心技巧：Score-Based Data Assimilation**

這篇教學介紹的關鍵技術是 Score-Based Data Assimilation（SDA），可用於 CorrDiff、StormCast 這類擴散式 AI 模型。運作原理如下：

- 擴散模型透過一連串的去噪（denoising）步驟，逐步生成高解析度預測。
- SDA 在每一個去噪步驟，都拿當下的中間預測結果去跟你提供的觀測資料比對。
- 根據比對結果微調下一步的去噪方向，把模型往符合觀測的方向「推」。
- 最終輸出仍是機率性的：觀測點附近的不確定性較小，離觀測點越遠、越依賴模型本身的模擬結果，不確定性就越大。

要讓 SDA 運作，需要定義一個「觀測算子」（observation operator），把模型輸出映射成你實際觀測到的量。對溫度、風速這類直接量測，最簡單的算子就是把鄰近網格值內插到觀測位置；作者也提到可以用代理量測，例如用風力發電機的實際發電量，反推當地風速。

SDA 帶來兩個能力：可以持續、更頻繁地更新預報（不受限於官方分析的固定釋出排程），以及可以把自己專屬、地區性或領域特定的觀測資料整合進來。

🧑‍💻 **實際跑一遍：CorrDiff-SDA 與 StormCast-SDA**

教學提供了 Earth2Studio 的程式碼範例。CorrDiff 用於把 0.25 度解析度的天氣場降尺度到 2.2 公里，範例限定在荷蘭與德國西北部的區域，同化 10 公尺風速：

```python
from earth2studio.data import GHCNHourly
from earth2studio.models.da import CorrDiffCosmoEra5SDA

domain = dict(lat_min=50.2, lat_max=53.8, lon_min=4.6, lon_max=10.4)
sda = CorrDiffCosmoEra5SDA.load_model(
    CorrDiffCosmoEra5SDA.load_default_package(),
    assimilate_variables=("u10m", "v10m"),
    resolution="rea2", domain=domain,
    number_of_samples=1, sampler_steps=12, amp=True,
).to("cuda")
```

接著抓取 ERA5 作為低解析度條件輸入，以及 GHCN 的地面站風速觀測，分別跑一次「不加觀測」（prior）與「加觀測」（analysis）的降尺度結果做對照。StormCast 則是同樣的概念用在以 HRRR 初始化、解析度 3 公里的美國中部區域高解析度預報上，藉由 SDA 把最新觀測與尚在等待中的 HRRR 分析結果結合。

📊 **在保留站點上，風速誤差降了 54%**

文中給出一組具體結果：在 CorrDiff-COSMO 的降尺度實驗中，加入 SDA 後，held-out（保留未參與同化）氣象站上的風速 RMSE 降低了 54%。

⚠️ **效果取決於觀測本身的品質**

作者也明確指出，SDA 的效果並非穩賺不賠，會受到幾個因素影響：觀測的數量、空間分布與精確度；預測目標場的特徵長度尺度；以及觀測算子本身的品質與是否「良態」（well-posed）。換句話說，觀測稀疏或算子設計不當,同化帶來的改善會打折扣。

🎯 **實務啟示**

如果你手上已經有專屬的感測資料，例如能源資產周邊的量測站，這套流程提供了一條不需要重新訓練 CorrDiff 或 StormCast、就能把資料用上的路徑。對於需要比官方六小時排程更即時反應的場景（電力調度、緊急應變），SDA 可以當作既有預報管線的一個「後製」步驟插入，重點是先盤點手上觀測資料的空間覆蓋率，再評估是否值得投入建置觀測算子。

🔗 **來源**
- 標題：Turn Your Latest Observations Into Timely Weather Decisions With NVIDIA Earth-2
- 作者／機構：Elizabeth Goodman，NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/turn-your-latest-observations-into-timely-weather-decisions-with-nvidia-earth-2/

#NVIDIA #Earth2 #WeatherAI #DataAssimilation #DiffusionModels #CorrDiff #StormCast #ClimateAI #MachineLearning #Earth2Studio
