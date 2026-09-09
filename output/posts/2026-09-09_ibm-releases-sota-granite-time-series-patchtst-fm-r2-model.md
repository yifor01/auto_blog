---
title: IBM releases SOTA Granite Time Series PatchTST-FM-r2 model with commercial-friendly
  license
source: HuggingFace Blog
url: https://huggingface.co/blog/ibm-research/ibm-releases-sota-granite-time-series
model: claude-code/sonnet
generated_at: '2026-09-09T20:01:24.913490'
score: 89
---

📌 IBM新時間序列模型:商用授權下的zero-shot預測冠軍

TL;DR：IBM推出385M參數的Granite PatchTST-FM-r2,在GIFT-Eval上是permissive授權下表現最好的zero-shot預測模型。

企業做需求預測、能源負載或流量預測時,長期得為每個資料集各自訓練一個模型。時間序列基礎模型想解決的正是這個痛點:一個預訓練模型,直接zero-shot套用到沒看過的資料集上。IBM這次釋出的Granite Time Series PatchTST-FM-r2,想證明的是「zero-shot預測」與「商用友善授權」可以同時兼顧。

🤔 **為什麼zero-shot表現是第一關**

一個基礎模型真正有用的前提,是它能泛化到訓練時沒見過的時間序列上,因此IBM團隊優先檢視的就是zero-shot表現。GIFT-Eval是一套涵蓋多種預測情境的綜合基準,若只看zero-shot、可複現、且未受測試資料洩漏影響的模型類別,PatchTST-FM-r2在CRPS與MASE兩項指標上都排名第二,同時是所有permissive商用友善授權模型中表現最好的一個。即使把允許使用GIFT-Eval訓練資料做預訓練的「pretrained」模型也一併納入比較,PatchTST-FM-r2依然名列前茅:CRPS排第3、MASE排第4,並且贏過包括Chronos-2、Timer-S1與多個Toto變體在內的幾個規模更大的競爭模型。

🧩 **架構關鍵:從Transformer層換成Conformer區塊**

PatchTST-FM-r2延續了PatchTST家族以patch為表示單位的做法,但把內部架構做了改版。前一代r1的區塊是「多頭自注意力 + 前饋網路」,r2則換成源自語音處理領域的Conformer風格區塊:兩層half-step前饋網路包夾住多頭自注意力與一層時間卷積(temporal convolution)。這樣的設計讓模型同時擁有兩種互補機制——自注意力負責捕捉patch之間的長距離關係,卷積則提供對局部時間結構的歸納偏誤(inductive bias)。從真實資料(ETTh1資料集)畫出的attention圖也能觀察到差異:傳統Transformer的注意力大多集中在對角線附近(局部關係),而Conformer版本則呈現更多遠離對角線的長距離關注,因為短距離的部分已交給卷積層處理。骨幹中的卷積層採用交替的kernel大小(重複{5, 5, 3, 3}模式)。

其他架構調整還包括:採用50%重疊的patch搭配Hamming窗加權,並以overlap-and-add方式做預測,以平滑patch邊界、提升準確度;新增了穩定性用的正規化;區塊數也從20層擴增到30層。整體參數量約385M,支援長達8,192步的context,並透過99-quantile的預測頭同時輸出點預測與機率分佈,讓使用者能取得完整的不確定性區間。

📊 **關鍵數據**

- 在僅限zero-shot、可複現、無測試洩漏的GIFT-Eval類別中:幾何平均CRPS為0.467(排名僅次於TimesFM-3,是permissive授權模型中的第一名);幾何平均MASE為0.6846
- 納入允許使用基準訓練資料的pretrained模型比較後:CRPS排名第3、MASE排名第4,且勝過Chronos-2、Timer-S1與Toto等多個變體

💡 **授權才是這次真正的差異化賣點**

在一眾時間序列基礎模型中,PatchTST-FM-r2真正的獨特之處,或許不只是排名數字,而是它同時採用Apache-2.0與OpenMDW 1.0雙授權(使用者可任選其一),而且模型權重、架構、推論pipeline與重現基準結果所需的程式碼全數公開。對於需要在商用產品中部署、又在意授權風險的企業而言,這種「效能夠好、授權夠乾淨、可重現」的組合,比起單純堆疊排行榜名次更具實際意義。

🎯 **實務啟示**

如果你的團隊正在評估時間序列基礎模型,PatchTST-FM-r2值得列入候選名單的理由很明確:zero-shot表現在permissive授權模型中排名第一,且提供完整可重現的程式碼與權重,能直接拿來對需求、價格、能源負載、流量或telemetry等場景做初步預測,再視情況決定是否需要進一步微調。素材也提到Granite Time Series系列可透過Confluent產品用於串流場景的生產環境,對已經有事件串流基礎設施的團隊而言是額外的整合切入點。

🔗 **來源**
- 標題：IBM releases SOTA Granite Time Series PatchTST-FM-r2 model with commercial-friendly license
- 作者／機構：Roman Vaculin、Wesley M. Gifford、Jiri Navratil、Chandra Reddy、Ayhan Sebin(IBM Research)
- 連結：https://huggingface.co/blog/ibm-research/ibm-releases-sota-granite-time-series

#IBM #GraniteTimeSeries #PatchTST #TimeSeriesForecasting #ZeroShot #FoundationModel #GIFTEval #OpenSourceAI #ApacheLicense #Forecasting
