---
title: 'SUFLECA: Scaling Up Feature Learning for CAD-to-image Alignment'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.15058
score: 103
model: tencent/hy3:free
generated_at: '2026-07-18T07:32:21.875268'
---

📌 【HuggingFace Papers】SUFLECA：用幾何特徵擴大學習規模，零射 CAD 對齊超越全監督

TL;DR：SUFLECA 以弱監督 NOC 特徵學習達成零射 CAD 對齊，在 ScanNet25k 首度勝過全監督方法。

從單張 RGB 影像估算物體的 9D pose（旋轉、平移、各向異性縮放），一直是機器人與擴增實境落地的關鍵難題。但現有零射（zero-shot）方法仰賴視覺基礎模型做外觀匹配，一旦遇到遮擋或 sim-to-real 領域偏移，對應關係就明顯退化。

🤔 **外觀驅動匹配在遮擋與域偏移下會失效**

CAD-to-image alignment 的目標是從單張 RGB 圖估出物體的 9D pose。近期 zero-shot 方法用 visual foundation models 把影像區域匹配到 CAD 模型，但對應點多半是 appearance-driven，在 occlusion 或模擬到真實的域差下品質下滑。

🧩 **兩大貢獻：擴大幾何特徵學習 + 幾何一致匹配**

SUFLECA（Scaling Up Feature Learning for CAD Alignment）是一個弱監督（weakly-supervised）框架，用於 zero-shot CAD 對齊，包含兩個核心設計：

- 透過 Normalized Object Coordinates（NOCs）監督，從預訓練視覺表徵擴大 geometry-grounded feature learning，使用橫跨 12 個真實與合成資料集、共 674K 張影像，學出緊緻且具幾何感知的特徵，可跨域泛化。
- 提出 geometrically consistent matching 演算法，建立可靠的 CAD-to-image 一對一對應點。

兩者結合後，每個物體例項可在 sub-second 內完成精準對齊，且不需迭代式 pose refinement。

📊 **ScanNet25k 上精度與效率雙贏**

在 ScanNet25k 基準上，SUFLECA 達到 33.4% / 42.3% 的 category / instance accuracy：

- 較最強的 zero-shot baseline 高出 10.3 / 12.2 個百分點，且運算 footprint 更小。
- 在該基準上首次超越 fully supervised 方法。

🎯 **實務啟示**

對機器人與 AR 工程師而言，SUFLECA 展示了用弱監督幾何特徵取代厚重外觀匹配、並免迭代最佳化的路徑：在遮擋與域偏移場景下，優先考慮 geometry-aware 的特徵學習與一致匹配，有機會用更低運算成本拿到可部署的零射對齊能力。作者也已開源程式碼（github.com/snt-arg/SUFLECA）。

🔗 **來源**
- 標題：SUFLECA: Scaling Up Feature Learning for CAD-to-image Alignment
- 連結：https://huggingface.co/papers/2607.15058

#CADAlignment #ZeroShot #PoseEstimation #NOC #GeometryAware #FeatureLearning #Robotics #AugmentedReality #ScanNet25k #SUFLECA
