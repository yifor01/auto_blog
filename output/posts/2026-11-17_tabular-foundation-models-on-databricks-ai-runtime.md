---
title: Tabular foundation models on Databricks AI Runtime
source: Databricks
url: https://www.databricks.com/blog/tabular-foundation-models-databricks-ai-runtime
model: claude-code/sonnet
generated_at: '2026-11-17T01:10:00.487432'
score: 80
---

📌 表格基礎模型：免訓練預測，但 GPU 帳單誰來付

TL;DR：Tabular Foundation Models 讓表格預測不用再為每個任務重新訓練模型，但企業落地仍要權衡 GPU 推理成本。

信用風險評估、客戶流失預測、需求預測、設備維護——這些最賺錢的機器學習應用，過去都得為每個任務各自開發、訓練、維護一套模型。Databricks 這篇文章整理的 Tabular Foundation Models（TFM）提出另一條路：預訓練好的模型，拿到新資料集就能直接預測，不需要針對該資料集重新訓練。

🤔 **為什麼企業 ML 落地這麼貴**

文章指出，即便 agentic 解法已經在加速這些流程，底層仍然依賴為每個 ML 任務或資料集量身訓練的模型，訓練與重訓練管線並沒有消失。TFM 想拿掉的正是這個依賴：模型預先在大量合成資料上訓練好，不需要在你的資料集上再訓練一次。

🧩 **靠 in-context learning 一次前向推論出答案**

TFM 的推論方式是把已標記的資料列當作上下文，和要預測的列一起傳入模型，transformer 的 attention 機制會把新的一列與這些範例建立關聯，單次前向傳遞就產生預測，這個做法稱為 in-context learning（ICL）。這種零訓練（zero-shot）方式提供了很強的基線，若想再提升準確度，也可以在特定資料集上微調（fine-tune）預訓練權重。

表格資料對 transformer 架構最大的挑戰，在於輸入型態混雜——數值、類別、布林值各自有不同的尺度與意義，不像文字裡的詞或圖片裡的像素那樣統一。社群的解法是開發專門的 tokenizer，把類別和數值特徵都映射進同一個共享的潛在空間。

解決了逐格 tokenization 之後，下一個問題是如何學習列與欄之間的關係。TabPFNv2 是第一個把這件事做到 foundation-model 規模的模型，做法是先對列、再對欄依序套用 attention，捕捉特徵之間的交互與樣本之間的底層關係，但這種密集 attention 的計算成本隨樣本數與特徵數快速增長，擴展性很差。TabICLv1 則採用行壓縮（row-compression）方法，用專門的編碼器把每一列壓縮成僅四個 token，讓跨樣本的 attention 成本大幅降低，同時維持有競爭力的預測表現。這個架構後來被 TabPFNv3、TabFM、KumoTabular 等模型採用並延伸，也是目前 TabArena 等排行榜上名列前茅的幾個模型。

另一個共同特點是訓練資料來源：這些模型主要用合成資料做預訓練，決定模型「開箱即用」表現好壞的關鍵，在於研究者能否生成真正貼近真實世界資料分佈與關係的合成資料，同時模擬缺值、離群值、未觀測特徵等企業資料常見的品質問題。雖然 Structural Causal Models 提供了取樣這類預訓練資料的標準框架，但具體 pipeline 設定因每個 TFM 而異。

📊 **授權條款差異不小，商用前先確認**

文章整理了幾個主要 TFM 的授權狀態：

| 模型 | 授權 | 是否可商用 |
|---|---|---|
| （BSD 3-Clause 授權模型） | BSD 3-Clause | 可商用 |
| TabFM | Non-Commercial License v1.0 | 需與模型創作者另行約定才可商用 |
| TabPFN-3.5 | License v1.0 | 需與模型創作者另行約定才可商用 |
| （Apache-2.0 授權模型） | Apache-2.0 | 可商用 |
| （OpenMDW-1.1 授權模型） | OpenMDW-1.1 | 可商用 |

文章建議，想掌握目前最新技術水準，可參考 TabArena 或 TALENT 這類基準測試，但也提醒企業自身的專有工作負載往往與合成資料或標準 benchmark 差異很大，應該直接拿自家資料評測，而不是只看公開分數。

⚠️ **GPU 記憶體會隨資料規模被吃光**

TFM 推論針對 GPU 最佳化，模型本身小到能塞進單張 GPU，但因為 ICL 的機制要求每次預測都把整個訓練集傳進模型，GPU 記憶體用量會隨著列數與特徵數增長，在企業常見的資料規模下很容易被耗盡。文章指出這會帶來一系列部署上的挑戰，但沒有進一步展開細節。整體而言，比起在 CPU 上跑傳統 XGBoost，TFM 每次預測的 GPU 成本更高，評估時需要把「省下的開發時間」和「持續的推論成本」放在一起權衡。

🎯 **實務啟示**

Databricks 的角度自然是導向自家 AI Runtime：透過 serverless GPU 基礎設施、搭配 Unity Catalog 做治理與版本控管、以及 MLflow 追蹤微調實驗指標，讓 TFM 的實驗與落地可以在資料所在地直接進行，不需要額外搬資料造成資料孤島。即便不用 Databricks，這篇文章給工程師的提醒依然成立：先用自家資料驗證 TFM 的準確度和成本是否划算，而不是只看公開 benchmark 的排名就決定導入。

🔗 **來源**
- 標題：Tabular foundation models on Databricks AI Runtime
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/tabular-foundation-models-databricks-ai-runtime

#TabularFoundationModels #MachineLearning #Databricks #InContextLearning #Transformer #MLOps #GPU #EnterpriseAI #TabPFN #DataScience
