---
title: Chinese frontier AI models carry the fingerprint of export-controlled GPUs
source: Hacker News
url: https://unemploymentlabs.com/checkpoint-forensics
model: claude-code/sonnet
generated_at: '2026-11-13T22:47:57.183339'
score: 97
---

📌 權重裡的硬體指紋：鑑識報告稱多家中國大模型已用上受管制的Blackwell GPU

TL;DR：一份鑑識報告透過分析公開權重的數值特徵，推斷DeepSeek、Moonshot AI等四家中國實驗室已用NVIDIA Blackwell GPU訓練最新模型。

出口管制卡住的是晶片的合法銷售通路,但卡不住的是權重本身留下的痕跡。這份由Will DePue撰寫、11月12日發布的鑑識報告主張，不需要洩密或內部消息,只靠公開發布的模型權重本身,就能回推訓練時用的是哪一代NVIDIA硬體。

🤔 **問題：如何在沒有內部資料的情況下判斷訓練硬體**

美國官員與媒體此前已多次指稱DeepSeek、Moonshot AI使用Blackwell晶片,但始終沒有公開技術證據。這份報告嘗試用純技術手段補上這塊空白：從模型已公開的權重中,還原出模型初始化時殘留的數值痕跡,再反推哪種硬體組態與初始設定能重現這些痕跡。

🧩 **方法：從初始化痕跡回推硬體世代**

報告的核心邏輯是,不同世代的NVIDIA晶片在硬體層級的處理器核心數（streaming multiprocessors, SM）不同——B200/B300是148個SM，GB200/GB300是152個SM——這類硬體特徵會以某種方式反映在模型初始化階段留下的數值模式裡。作者在約6兆種種子與硬體組態的搜尋空間中比對,並對DeepSeek-V4-Flash與Kimi K3兩個模型額外在實體Blackwell晶片上做了驗證。報告也指出,配置特殊的AMD硬體（同樣受出口管制）是唯一已知的替代解釋,但已在DeepSeek-V4-Flash上排除,並認為在其他五個模型上也「非常不可能」。

📊 **六個模型讀出Blackwell指紋,訓練規模達數千張GPU**

| 實驗室 | 模型 | 發布時間 | 判讀晶片 |
|---|---|---|---|
| DeepSeek | DeepSeek-V3 | 2024年12月 | NVIDIA Hopper（廠商自述H800） |
| DeepSeek | DeepSeek-V4-Flash | 2026年4月 | NVIDIA Blackwell B200/B300 |
| DeepSeek | DeepSeek-V4-Pro | 2026年4月 | NVIDIA Blackwell GB200/GB300 |
| Moonshot AI | Kimi K2 / K2.5 | 2025年7月／2026年1月 | NVIDIA Hopper |
| Moonshot AI | Kimi K3 / K3.1-Pro | 2026年7月／11月 | NVIDIA Blackwell GB200/GB300 |
| MiniMax | MiniMax-M2.7 | 2026年4月 | NVIDIA Hopper |
| MiniMax | MiniMax-M3 | 2026年6月 | NVIDIA Blackwell B200/B300 |
| Ant Group | Ling-3.0-flash / 3.1-flash | 2026年8月／10月 | Hopper → Blackwell |

報告指出,這些判讀結果遠非隨機吻合可以解釋：在約6兆種組合的搜尋空間裡,僅靠機率產生的最強吻合預期也只會達到約8個標準差（sigma），而六個模型的最強證據落在49到1,385個標準差之間，最弱的單項測試也有20個標準差。作者也用24個已公開硬體資訊的模型做交叉驗證,結果全部與官方說法一致，包括NVIDIA自家Nemotron-3 Ultra的152個SM讀數,與其技術報告中提到的GB200相符。

按模型規模與訓練資料量估算,報告推測Kimi K3與DeepSeek-V4-Pro這兩個最大的訓練任務,各需要約4,500張與3,000張Blackwell GPU、跑上兩到三個月，五個訓練任務合計約需1.2萬張Blackwell GPU，若以約每張7萬美元估算（參照《華爾街日報》報導字節跳動在馬來西亞部署3.6萬張Blackwell的費用換算),單一最大叢集成本約落在2億至3億美元,五者合計超過5億美元。

⚠️ **報告自己承認的不確定性**

作者坦言,這套估算仰賴幾個無法從權重直接確認的假設：各實驗室實際的GPU使用效率（MFU）從未公開，訓練token數除DeepSeek自報數字外都是作者自行推估的方法尚未公開細節,訓練時長也沒有任何實驗室對外說明，且前提是訓練全程都使用初始化權重時的那套硬體。報告同時明確指出,這些技術證據只能證明「有能力接觸到先進運算硬體」,無法證明晶片的實際所在地、取得管道，或是否真的違反出口管制。值得注意的是,報告也發現並非所有中國實驗室都已切換到Blackwell：阿里（Qwen）、智譜（GLM）、騰訊、小米與StepFun的最新模型讀數仍是Hopper世代,美團則聲稱LongCat-2.0完全在「AI ASIC超級節點」上訓練,且在其釋出的權重中未發現任何NVIDIA指紋。

🎯 **對關注AI地緣格局的工程師意味著什麼**

這份報告展示了一種新型的、不依賴內部洩密的技術稽核手段——用模型自身的權重做「出生證明鑑識」。對於長期關注算力管制有效性與中美AI產業賽局的工程師和研究者,這提供了一個可公開驗證、可複現的方法論樣本,而不只是又一輪缺乏證據的輿論指控。

🔗 **來源**
- 標題：Chinese frontier AI models carry the fingerprint of export-controlled GPUs
- 作者／機構：Will DePue
- 連結：https://unemploymentlabs.com/checkpoint-forensics

#NVIDIA #Blackwell #ExportControls #DeepSeek #MoonshotAI #MiniMax #AntGroup #AIHardware #ModelForensics #GeopoliticsOfAI
