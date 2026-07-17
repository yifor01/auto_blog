---
title: 'VideoChat3: Fully Open Video MLLM for Efficient and Generalist Video Understanding'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.14935
score: 93
model: tencent/hy3:free
generated_at: '2026-07-17T08:11:24.763715'
---

📌 【HuggingFace Papers】VideoChat3：4B 引數全開源影片 MLLM 兼顧效率與泛化

TL;DR：VideoChat3 以全開源與 I3D-ViT 設計，用 4B 引數超越同級開源影片模型。

現有的開源影片理解模型，常常只能在特定領域奏效，要不就是運算成本太高，要不就是訓練程式碼或資料集不公開。這讓想在真實場景落地、或自行改進模型的工程師卡在中途。

🤔 **開源影片 MLLM 的三道牆**

摘要指出，當前開源模型主要有三個限制：難以跨多樣影片型別泛化、只能在特定領域有效；高運算需求拖累效率與可擴充性；多數僅部分開源，訓練程式碼、策略或資料集未釋出，阻礙重現與社群發展。

🧩 **雙軸設計：效率與有效性並進**

VideoChat3 被定位為 fully open、efficient、generalist 的影片中心 MLLM（Multimodal Large Language Model），透過兩個互補設計推進影片理解：

- 效率面：提出 Inflated 3D Vision Transformer（I3D-ViT）與 Adaptive Frame Resolution for Streaming Video Perception，用於串流影片感知，實現高效的時空表示，降低訓練與推論時處理影片輸入的成本。
- 有效性面：開發可擴充的影片資料合成管線，整理出三個多元高品質訓練資料集：VideoChat3-Academic2M、VideoChat3-LV116K、VideoChat3-OL617K，分別涵蓋一般、長影片與串流影片場景，提升跨領域泛化能力。

將上述設計整合後，模型在廣泛泛化與運算效率之間取得少見的平衡。

📊 **4B 引數超越同級開源模型**

在一般、長影片與串流基準上的實驗顯示，VideoChat3 僅用 4B 引數，便在同等或更大引數量的先前開源模型之上，且具更高效率。摘要未提供具體基準名稱與分數，僅宣告此結果。

🎯 **全開源對實務的價值**

對工程師而言，訓練程式碼、策略與三套資料集若皆可用，代表能直接重現、微調或擴充管線；I3D-ViT 與自適應幀解析度也提供在有限 GPU 記憶體下處理串流影片的實作參考。

🔗 **來源**
- 標題：VideoChat3: Fully Open Video MLLM for Efficient and Generalist Video Understanding
- 連結：https://huggingface.co/papers/2607.14935

#VideoMLLM #VideoChat3 #OpenSource #VideoUnderstanding #I3DViT #Multimodal #LLM #Efficiency #DatasetSynthesis #StreamingVideo
