---
title: Build a model improvement flywheel with Amazon SageMaker HyperPod Data Capture
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-a-model-improvement-flywheel-with-amazon-sagemaker-hyperpod-data-capture/
model: claude-code/sonnet
generated_at: '2026-11-13T22:54:45.735638'
score: 82
---

📌 用生產流量餵回模型：SageMaker HyperPod 的資料捕捉飛輪

TL;DR：AWS 示範如何用 HyperPod 內建的 Data Capture 抓取生產推論資料，反饋微調修補模型盲區。

模型上線後最怕遇到訓練資料沒蓋到的情況：新產品、新用語、沒見過的輸入格式。離線 benchmark 看不出這些問題，因為它凝固在過去。AWS 用一個家電支援單路由模型的實例，示範了一條完整的「捕捉→分析→標記→微調→重新部署」飛輪。

🤔 **沒有生產推論的紀錄，就找不到模型的盲區**

部署在 Amazon SageMaker HyperPod 上的基礎模型，常會遇到預先整理好的資料集沒覆蓋到的輸入。如果沒有記錄實際的 production inference input/output，團隊就無法偵測 drift、找出失敗模式，更無法用真實互動資料改善模型。SageMaker HyperPod 新推出的 Data Capture，就是內建把線上推論的輸入輸出記錄到 Amazon S3 的功能，官方宣稱延遲影響小，也不影響模型可用性。

🧩 **三個獨立 Tier，外加一套捕捉→分析→標記→微調的管線**

Data Capture 提供三個獨立的 tier：Tier 1 和 Tier 3 都會存完整 payload（兩者同時開啟會重複存兩份），Tier 1 適合 compliance 跟 Model Monitor 用途，Tier 2 只存流量 metadata，Tier 3 則是打算真正拿 payload 去用時才開。這篇文章只用 Tier 3。因為 Tier 3 會存完整 payload，可能含有姓名、地址、訂單編號等個資，官方建議搭配 sampling、AWS KMS 加密（kmsKeyId）、S3 生命週期規則，以及用 Amazon Comprehend 做 PII redaction 來保護資料。

架構上，inference operator 會在 model pod 裡加三個 sidecar：所有經過 NGINX reverse proxy 的請求會被複製一份給 OpenTelemetry collector，批次處理後透過 Mountpoint-S3 volume 寫入 S3，Athena 可以直接讀取這些檔案，不需要額外的 crawler。training operator 則在第二張 GPU 上以 HyperPodPyTorchJob 跑微調，新模型用另一個同樣開著 capture 的 endpoint 部署，整套流程只需要一個 HyperPod cluster。

示範案例是用 Qwen2.5-3B-Instruct 做一個家電支援單路由模型，用 vLLM 的 guided JSON decoding 把每張 ticket 分類成 ProductFridge、ProductWasher、ProductOven、ProductDishwasher、ProductMicrowave 或 catch-all 的 Other 六個類別之一。零售商上線了全新的 Arctis 系列冷氣後，router 沒有對應的分類，只能硬套到最接近的類別，或落入 Other 這個垃圾桶分類，而且它自己說不出「這是個新東西」。捕捉下來的紀錄採 SageMaker data-capture 格式，以 .jsonl 儲存，request 跟 response body 都是 base64 編碼，需要先解碼再轉成 JSON 才能讀。

📊 **Other 類別從 4.8% 暴衝到 36.8%，成為最大分類**

用 Athena 建一張外部表描述 capture 紀錄的外層 JSON，搭配 partition projection 按年月日時對應 S3 的 hourly prefix，不需要 crawler 或手動 ADD PARTITION；再疊一層 view，用 from_utf8(from_base64(...)) 把 payload 解回 JSON 方便查詢。分析結果顯示，Arctis 上線前，Other 類別每分鐘佔比都在 7% 以下；上線那一分鐘跳到 15%，之後持續攀升，最後三分鐘達到 47% 到 65%。累計佔比只到 22.6%，因為它把上線前的大量正常流量平均進去——這正是文章強調「要看每分鐘佔比而非累計佔比來設告警」的原因。把上線前後拆開看，Other 從上線前 400 張 ticket 中的 19 張（4.8%），變成上線後 500 張 ticket 中的 184 張（36.8%），一躍成為最大的分類。

💡 **抓到盲區只是第一步，用 SQL policy 標記再微調才形成閉環**

這個案例說明了離線 benchmark 看不到的分佈漂移，只能從實際 production traffic 裡被看見。接著用一套 SQL policy 把這些被誤判進 Other 的紀錄標記出來，餵給第二張 GPU 做微調，再重新部署一個同樣開著 capture 的新 endpoint，讓這套改善機制可以持續循環，而不是一次性修補。

⚠️ **示範用的是合成資料，且完整 payload 涉及個資處理**

本文採用合成資料集做示範，實際佔比與絕對數字僅反映這次 demo 情境；由於 Tier 3 捕捉的是完整 payload，正式環境導入前需要先做好加密與 PII redaction，才能安心把這些資料用作後續訓練資料。

🎯 **把「捕捉生產流量」當成模型維運的標準配備**

如果你的模型上線後擔心遇到訓練資料沒覆蓋的新情境，可以參考這個模式：開啟 Tier 3 捕捉、用 Athena 做不需額外基礎設施的探索式分析、搭配 SQL policy 做規則式標記，再用第二張 GPU 跑微調並與原模型並行部署，形成持續改善的飛輪，而不是等到離線 benchmark 看不出問題就假設模型沒事。

🔗 來源
- 標題：Build a model improvement flywheel with Amazon SageMaker HyperPod Data Capture
- 作者／機構：Shantanu Tripathi, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/build-a-model-improvement-flywheel-with-amazon-sagemaker-hyperpod-data-capture/

#AWS #SageMaker #HyperPod #MachineLearning #DataCapture #ModelMonitoring #FineTuning #MLOps #vLLM #ProductionAI
