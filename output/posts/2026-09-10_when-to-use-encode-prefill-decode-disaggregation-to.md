---
title: When to Use Encode-Prefill-Decode Disaggregation to Accelerate Multimodal Model
  Serving
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/
model: claude-code/sonnet
generated_at: '2026-09-10T19:58:02.898645'
score: 99
---

📌 圖片吃滿 GPU?EPD 分離讓多模態推論快 5 倍

TL;DR:NVIDIA Dynamo 用 EPD 分離加速多模態推論,最高 5 倍 TTFT。

🎣 當一個請求裡塞了十張圖片,你的 LLM 推論伺服器到底在忙什麼?答案往往不是你以為的「生成 token」,而是視覺編碼,這段隱藏在 prefill 之前的工序,可能拖垮整條推論管線的延遲。NVIDIA 這篇文章介紹了 encode-prefill-decode(EPD)分離技術,說明何時該用、何時不該用。

🤔 背景:多模態請求在 prefill 前多了一道工序

一個多模態請求必須先前處理媒體、跑過 vision transformer(ViT)產生 embedding,才能開始 LLM 的 prefill。在傳統的 aggregated serving 中,vision encoding、LLM prefill 與 decode 共用同一個 worker、同一個排程網域,當媒體處理只佔工作負載的一小部分時,這種簡單設計運作良好。但隨著請求包含的圖片或影片增加,vision encoding 可能耗時數百毫秒以上。由於 encoder 與 LLM 的運算共用同一顆 GPU,媒體密集的請求會延遲自己的 prefill,還會跟同時進行的 prefill、decode 工作互相搶資源。在混合流量下,即使是純文字請求,也可能被迫排在多模態請求後面等待,即使它們根本不需要 vision encoding。

🧩 三種 encoder 佈署拓撲

NVIDIA Dynamo 是一個開源的分散式推論框架,支援把 encoder 與 PD(prefill+decode)worker 角色拆開,但不固定硬體佈署位置。Encoder worker 產生 vision embedding,PD worker 消費這些 embedding 並執行 LLM,兩者透過 NVIDIA Inference Transfer Library(NIXL)傳遞資料,讓兩個階段可以獨立批次處理、獨立排程、獨立擴縮。

文章比較了三種拓撲:
- Aggregated:每顆 GPU 跑一個 aggregated worker,排程器把 vision encoding、LLM prefill、decode 全部當成同一個請求生命週期的一部分管理。
- Colocated encoder:每顆 GPU 跑一個或多個 encoder worker,搭配一個 PD worker,worker 共享 GPU 運算資源,但維持各自獨立的 request queue 與 batching。在同質叢集上,Colocated Encoder 通常是較佳選擇,因為 vision encoder 相對 LLM 而言是輕量工作,把整顆同等級 GPU 保留給 encoder 會讓大半運算力閒置。
- Disaggregated encoder:當叢集裡有一種更便宜、更適合 encoder 工作的低階 GPU 層,而主力 GPU 層專門服務 PD worker 時,這個拓撲最有吸引力。NVIDIA 的測試環境用兩顆 RTX 6000D GPU 跑 encoder worker、四顆 GB200 GPU 跑 PD worker,把較輕量的 encoder 工作留在 RTX GPU 上,把運算與記憶體需求更高的 LLM 工作留給 GB200。文章特別指出,同質 GPU 的 disaggregated 佈署一律表現不如 colocated encoder,因此分析中未納入這種組合。

💡 決定 EPD 效益的四個因素

| 因素 | 為何重要 | 何時能帶來效益 |
|---|---|---|
| 輸入媒體量 | 媒體越重,visual token 越多,encoder 工作量越大 | 多張圖片、高解析度圖片或影片輸入,產生大量 visual token |
| 輸出序列長度(OSL) | OSL 越長,整體延遲越偏向 decode 階段;TTFT 的增益仍在,但 E2E 增益會縮小 | 短 OSL 時 E2E 增益維持;長 OSL 時 E2E 增益被侵蝕 |
| 模型大小/精度 | ViT 運算量大致固定,LLM 運算量會隨啟動參數變少、精度降低而下降,小型、MoE、量化模型的 ViT 對 LLM 運算比例更高 | 較小、MoE、較低精度的模型受益更多,大型稠密模型受益較少 |
| 混合流量(文字+多模態) | 混合的 prefill batch 會讓文字請求被迫等待 ViT;EPD 把 encoder 工作隔離開,文字請求不必再等 encoder | 多模態流量重、又混雜對延遲敏感的文字請求時效益最明顯 |

📊 實測:十張圖片的請求,TTFT 降了近六成

測試環境用 Qwen3.5 122B A10B NVFP4(精度消融實驗除外),四顆 GB200 GPU(加上 disaggregated 設定中額外的 RTX 6000D GPU)。Aggregated 設定為每顆 GB200 跑一個 TP1 aggregated worker;Colocated EPD 為每顆 GB200 跑兩個 encoder worker 加一個 PD worker;Disaggregated EPD 則用 RTX 節點當 encoder 層、GB200 當 PD 層。Vision embedding 透過 NIXL over UCX RC/TCP Ethernet 傳輸,測得峰值頻寬 20 Gbps,goodput 的 SLO 門檻設定為 inter-token latency(ITL)低於 100 毫秒。

在一個模擬中等偏重視覺負載的測試請求中(每個請求 10 張圖片、每張圖片上限 256 tokens、OSL 1024),結果顯示:Colocated encoder 讓 TTFT 下降 58%,Disaggregated(異質 GPU)設定則下降 50%。由於 OSL 高達 1024,decode 時間並不會因為 encoder 分離而縮短,所以 E2E 延遲的改善相對溫和。但真正的亮點在 goodput:異質 GPU 層在同樣的延遲 SLO 下,可服務的流量比 aggregated 設定多出 70%,原因是 encoder 容量的增加完全沒有動用到 GB200 的運算預算。

🎯 實務啟示:先看你的流量吃不吃 visual token 與短輸出

如果你的服務主要處理短輸出、圖片密集或影片輸入的請求,並且使用量化 MoE 模型,EPD 分離值得認真評估,尤其是在有異質 GPU 資源可用時,把 encoder 移到便宜的 GPU 層能在不動用主力 GPU 預算的情況下大幅提升 goodput。但若你的服務以長輸出為主,或模型本身是大型稠密模型,EPD 帶來的 E2E 延遲改善會相對有限,評估前建議先量測自己流量中 visual token 佔比與 OSL 分布。

🔗 來源
- 標題:When to Use Encode-Prefill-Decode Disaggregation to Accelerate Multimodal Model Serving
- 作者/機構:Tanya Lenz, NVIDIA Developer Blog
- 連結:https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/

#NVIDIA #Dynamo #MultimodalAI #LLMInference #VisionTransformer #InferenceOptimization #MoE #GPUComputing #TTFT #AIInfrastructure
