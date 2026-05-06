---
title: "A Benchmark for Interactive World Models with a Unified Action Generation Framework"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.03941
score: 118
model: tencent/hy3-preview:free
generated_at: 2026-05-06T20:08:55.730902
---

📌 iWorld-Bench互動世界模型評測基準

你還在比較世界模型生成的影片夠不夠逼真嗎？
真正要落地AGI，能不能和物理世界互動才是核心能力。
現有評測卻幾乎都忽略了這塊，清華團隊剛補上了缺口。

🤔 **現有世界模型評測缺互動標準，卡住AGI發展**

AGI的核心是需要能自適應學習與交互的智能體，而互動式世界模型是支撐感知、推理、行動的可擴展環境，是具身智能、機器人等前沿領域的關鍵基礎。但現有研究一直缺乏大規模數據集與統一基準，來評估世界模型的物理互動能力，導致不同模型的能力難以橫向比較，研究方向也缺乏明確指引。

🧪 **330k影片片段、4.9k測試樣本，覆蓋多場景互動任務**

為解決上述缺口，清華大學、東北大學、華南理工大學的研究團隊提出iWorld-Bench，這是一套專門針對互動式世界模型的訓練與測試基準。團隊首先構建了包含33萬個影片片段的多樣化數據集，篩選出2100個覆蓋不同視角、天氣、場景的高質量樣本；針對現有世界模型互動模態不統一的問題，團隊提出統一動作生成框架（Action Generation Framework），設計6種任務類型，最終生成4900個測試樣本，聯合評估模型的視覺生成、軌跡跟隨、記憶三大類能力，同時覆蓋距離感知、記憶等互動相關指標。

💡 **評測14款主流世界模型，找出互動能力關鍵短板**

團隊基於iWorld-Bench評測了14款具代表性的世界模型，明確識別出當前模型在互動能力上的關鍵限制，並公開了iWorld-Bench模型排行榜。評測結果可為後續研究提供明確的優化方向，也讓開發者能快速對比不同模型的互動能力差異。

⚠️ **現有公開資料未提及具體研究限制**

本次釋出的論文摘要與公開資訊中，未明確列舉研究侷限。團隊已將iWorld-Bench排行榜公開於http://iWorld-Bench.com，後續可關注數據集擴展與更多模型評測結果的更新。

🎯 **開發者可基於統一框架橫向對比模型能力**

對於GenAI研究者與工程師，iWorld-Bench提供了統一的動作生成框架與標準化測試集，可直接用於評測自研世界模型的互動能力，也可參考公開排行榜對比14款主流模型的優劣勢。尤其是從事具身智能、機器人世界模型、互動式生成模型的研究團隊，可基於該基準快速驗證模型在距離感知、記憶、軌跡跟隨等核心能力上的表現。

🔗 **論文連結**
📝 論文標題：A Benchmark for Interactive World Models with a Unified Action Generation Framework
👤 作者：Jianjie Fang, Yingshan Lei, Qin Wan, Ziyou Wang, Yuchao Huang
🏫 機構：清華大學、東北大學、華南理工大學
📚 來源：Computer Vision and Pattern Recognition (arXiv:2605.03941)
🔗 論文：https://arxiv.org/abs/2605.03941
🌐 排行榜：http://iWorld-Bench.com

#世界模型 #AGI #具身智能 #生成式AI #計算機視覺 #清華大學 #iWorldBench #AI研究
