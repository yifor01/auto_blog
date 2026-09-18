---
title: PrismML hopes its tiny LLM will change how we all use AI
source: TechCrunch AI
url: https://techcrunch.com/2026/09/17/prismml-hopes-its-tiny-llm-could-change-how-we-all-use-ai/
model: claude-code/sonnet
generated_at: '2026-09-18T19:54:21.210875'
score: 89
---

📌 27B模型壓成5.9GB，PrismML押注「小模型也能推理」

TL;DR：Caltech 團隊新創 PrismML 用「三元權重」把 Qwen3.8 27B 壓縮到 5.9GB，效能保留 98%。

一個模型要多小，才能塞進手機還維持推理能力？新創公司 PrismML 給出的答案是：把一個 16-bit 的權重，簡化成只有三種取值。

🤔 **押注「能推理的模型不必大」**

PrismML 由 Caltech 研究團隊創立，執行長 Babak Hassibi 是 Caltech 教授、壓縮技術專家，公司目前完成 2,225 萬美元種子輪，投資方包括 Khosla Ventures、Cerberus Capital 與 Caltech，顧問陣容則有 Databricks 共同創辦人、Berkeley Sky Computing Lab 主任 Ion Stoica。公司目標明確：做出小到能塞進 PC 甚至高階智慧型手機的推理模型（reasoning LLM）。TechCrunch 報導甚至傳出 PrismML 正與 Apple 洽談，Hassibi 對此不予置評。

🧩 **三元權重：把16bit壓成三個數字**

本週四發布的 Bonsai 2 27B，是將 Alibaba 開源模型 Qwen3.8 27B 壓縮到 5.9GB，記憶體用量較原始模型減少 9 到 10 倍。壓縮方式稱為「ternary（三元）」權重：一般模型每個權重需要 16 bit 儲存，PrismML 的做法則將其簡化為 +1、−1 或 0 三種數值，大幅縮減每個權重需要儲存的資訊量，模型體積因此大幅下降。

📊 **從95%到98%：壓縮不等於效能全失**

Hassibi 表示，Bonsai 2 在整體 benchmark 分數上達到原始 Qwen 模型的 98%，較今年 3 月發布的第一代 Bonsai（95%）進一步提升。第一代 Bonsai 至今下載次數已超過 1,100 萬次，PrismML 更小型的模型系列則另外累積 260 萬次下載。至於能否達到 100% 的 benchmark 對齊，Hassibi 認為壓縮多少都會帶來一定影響，但他也指出，未壓縮的 LLM 本身在實際任務上就不是完全準確，2% 的分數落差未必會顯著影響實際使用體驗；此外，模型跑在什麼樣的 harness（周邊軟體）裡，對準確度的影響同樣重大。

💡 **下一步：把同樣的壓縮技術用在數百億參數模型上**

PrismML 表示下一批模型預計在未來幾個月內發布，規模將達到數百億參數等級。Hassibi 認為模型愈大，反而愈容易在壓縮後保留原有智慧——因為更大的模型有更多「空間」可供壓縮，因此對大型模型來說更容易接近 100% 的效能保留。Stoica 則從應用角度補充，這類技術讓進階模型得以直接跑在使用者裝置上，「智慧就在你的指尖，而且免費，因為它跑在你已經買下的裝置上；同時也更私密，因為資料不需要送上雲端。」

⚠️ **同場競爭者不只一家**

報導提到，LLM 壓縮並非 PrismML 獨有的賽道，西班牙 Donostia International Physics Center 教授創立的 Multiverse Computing 也在做類似的事，且募資規模更大；PrismML 的差異化訴求在於壓縮後效能損失極小。

🎯 **實務啟示**

對工程師而言，「三元權重壓縮」代表的是推理成本結構的潛在轉變：若像 Bonsai 2 這樣 9–10 倍的記憶體縮減能維持近乎原始效能，意味著原本只能跑在雲端 GPU 上的模型，未來有機會直接部署在邊緣裝置或消費級硬體上，值得持續關注其 Hugging Face 頁面公開的壓縮細節與後續數百億參數模型的驗證結果。

🔗 **來源**
- 標題：PrismML hopes its tiny LLM will change how we all use AI
- 作者／機構：Julie Bort（TechCrunch AI）
- 連結：https://techcrunch.com/2026/09/17/prismml-hopes-its-tiny-llm-could-change-how-we-all-use-ai/

#LLM #ModelCompression #EdgeAI #OnDeviceAI #SmallLanguageModels #Qwen #AIStartup #Caltech #TernaryQuantization #AIHardware
