---
title: 'Inside NVIDIA’s cuDNN Graph API: Fusion, Autotuning, and Plan Reuse with cuDNN
  Frontend'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/15/inside-nvidias-cudnn-graph-api-fusion-autotuning-and-plan-reuse-with-cudnn-frontend/
model: claude-code/sonnet
generated_at: '2026-09-16T20:24:33.398835'
score: 80
---

📌 跳過框架直接對話 cuDNN：用 Graph API 動手做 kernel 融合與自動調參

TL;DR：一份可在 Colab 跑的教學，示範如何用 cuDNN Frontend 手動搭圖、自選引擎、量化融合與調參帶來的效能差異。

平常呼叫 `torch.nn.functional.conv2d` 時,背後其實是 PyTorch 在幫你決定要用 cuDNN 的哪個引擎執行。這篇教學把這層決策攤開給你看:自己描述運算圖、自己選引擎、自己付出或省下編譯與 launch 的成本。

🧩 統一的五步驟建構流程

教學中的每個 kernel 都用同一套流程處理:先用維度與 strides 宣告 tensor,把運算串接上去,接著跑五步驟的 build pipeline——validate、build operation graph、create execution plans、check support、build plans——最後對一組指標構成的 variant pack 執行運算。全程在單一 Colab GPU 上跑,並拿 PyTorch 的對應運算做為 reference 驗證正確性、同時量測效能代價。

第一步是解決環境問題:讓 cuDNN Frontend 的動態載入器找得到 `libcudnn.so`。做法是先讓 PyTorch 載入它內建的 cuDNN,再手動 preload 對應的共享物件,讓 Frontend 自己的 `dlopen` 可以解析到 process 中已經存在的 library。接著依 GPU 的 compute capability 選擇 bfloat16 或 float16,建立 cuDNN handle,並定義好 tensor 描述、圖建構、workspace 配置與以事件為基礎的 benchmark 等後續共用的輔助函式。

🧩 從單一融合 kernel 到不信任預設引擎

第一個示範圖是 convolution 接 bias add 再接 ReLU,三個運算全部融合成單一 kernel。全程使用 channels_last 排列,因為這正是 cuDNN 的 tensor-core 引擎偏好的 NHWC strides,並明確指定輸出的維度與 strides,確保結果以相同佈局寫回。驗證輸出與 `torch.nn.functional.conv2d` 一致後,再把融合圖拿去跟 PyTorch 分開執行 convolution 與 activation 兩個 kernel 的做法做效能比較。

接著重新搭建同一個 convolution,但這次不採用預設的 heuristic,改為向 heuristic mode A、B、FALLBACK 都索取候選 plan,並用 `build_plan_policy.ALL` 全部編譯出來。逐一走訪每個候選 plan、配置各自需要的 workspace、用 `execute_plan_at_index` 計時,印出每個引擎的吞吐量與 workspace 大小。最快與最慢引擎之間的落差,正是這個練習想凸顯的重點:比起接受預設選擇,自己動手調參到底能換來多少額外效能。

🧩 更完整的 epilogue、attention 與 plan 重用

教學接著搭建一個 batched matmul,並掛上完整的 epilogue:以 host scalar 傳入的 alpha scale、bias add、activation,再加上對結果做 AMAX reduction。把 AMAX 計算塞進同一個 kernel,正是 FP8 訓練會用到的模式,可以在不對輸出多做一次掃描的情況下,順手收集下一步量化所需的 scale factor。跟 PyTorch 的 `baddbmm` + activation + `amax` 這串鏈式呼叫比較後可以看出,加速的來源主要是省掉了 epilogue 之間的記憶體存取,而不是矩陣乘法本身變快。

再來是一個帶 causal mask 的 fused scaled dot-product attention 圖,拿去跟 `torch.nn.functional.scaled_dot_product_attention` 核對,並限定只在 SM80(Ampere 架構)以上執行,因為融合 kernel 需要對應的硬體支援。教學也特別處理了寫法上的相容性問題,因為 cuDNN Frontend 在 1.x 系列版本之間,已經逐漸從 `use_causal_mask` 走向 `diagonal_alignment` 與 bound arguments 的寫法。

最後示範把已經建好的 matmul 圖序列化成 bytes,重新載入到一個全新的圖物件,並透過整數 UID 執行,讓 process 啟動之後可以完全跳過重新編譯的成本。

🧩 貼近生產環境的兩個實務技巧

教學收尾聚焦在兩個生產環境常見的考量。第一個是讓四個只有 batch size 不同的圖共用同一個 kernel cache,分別計時觀察後續 shape 是否能重用已編譯好的 kernel,不必再付一次 JIT 編譯的代價。第二個是把 convolution 的 plan 包進 CUDA graph 裡執行擷取,並把 cuDNN handle 的 stream 設定成 capture stream,讓整段運算進到 graph 裡,藉此量測 replay 到底省下多少每次迭代的 launch overhead。

⚠️ 這套 API 值得投入的場景

整份教學涵蓋的程式碼規模不大,只有一個 convolution、一個 matmul、一個 attention kernel,但涉及的技巧面向很廣。作者指出,這個 API 真正值得投入的地方,是那些框架層級沒有等效寫法的融合、shape 夠「熱」值得花時間自動調參,以及啟動與 launch 成本會主導總開銷的小型 kernel;許多情況下跟 PyTorch 效能打平,其實是因為 PyTorch 底層本來就在呼叫 cuDNN。

🎯 實務啟示

對想要壓榨 GPU 訓練或推論效能的工程師來說,這份教學提供了一套可以直接動手驗證的思路:哪些運算值得手動搭圖融合、如何用同一套程式碼跑過所有候選引擎找出實際最快的選項,以及如何透過 plan 序列化、kernel cache 共用與 CUDA graph 擷取,把編譯與 launch 成本挪出熱路徑。

🔗 來源
- 標題:Inside NVIDIA's cuDNN Graph API: Fusion, Autotuning, and Plan Reuse with cuDNN Frontend
- 作者／機構:Sana Hassan, MarkTechPost
- 連結:https://www.marktechpost.com/2026/09/15/inside-nvidias-cudnn-graph-api-fusion-autotuning-and-plan-reuse-with-cudnn-frontend/

#cuDNN #NVIDIA #GPUOptimization #DeepLearning #KernelFusion #CUDA #Autotuning #Attention #FP8 #MLSystems
