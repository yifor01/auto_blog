---
title: Accelerating Mamba-2 with High-Performance Forward Pass Kernels in NVIDIA CUDA
  Tile
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/accelerating-mamba-2-with-high-performance-forward-pass-kernels-in-nvidia-cuda-tile/
model: claude-code/sonnet
generated_at: '2026-10-19T21:43:44.773338'
score: 90
---

📌 【NVIDIA × Jane Street】用 cuTile 加速 Mamba-2 前向傳遞

TL;DR：Jane Street 工程師用 NVIDIA 新 DSL cuTile 實作 Mamba-2，靠三個客製化 kernel 把序列模型推上 Tensor Core。

Attention 訓練快、推論卻隨序列長度線性變貴；RNN 推論成本固定、訓練卻難以平行化。Mamba-2 想在這兩者之間找到平衡點，而 Jane Street 的機器學習工程師選擇用 NVIDIA 的新工具 cuTile 來實作它的前向傳遞，並與 NVIDIA 合作最佳化出三個核心 kernel。

🤔 **序列建模的運算取捨**

傳統的 softmax attention 靠矩陣乘法與 Tensor Core 加速，訓練很快，但推論時運算量與記憶體需求會隨序列長度線性增加。RNN 則相反：固定大小的運算與記憶體佔用，但訓練過程緩慢且難以平行化。Mamba-2 這類架構想兼顧兩者：它像 RNN 一樣擁有固定大小的隱藏狀態與遞迴更新，但這個遞迴更新可以用分塊（chunkwise）的方式,透過 Tensor Core 有效率地計算。

🧩 **核心遞迴式與分塊計算**

Mamba-2 的核心遞迴可以寫成：h(t) = exp(A·dt(t))·h(t-1) + dt(t)·B(t)·x(t)，輸出則是 y(t) = c(t)ᵀ·h(t) + D·x(t)。其中 x(t)、dt(t)、B(t)、c(t) 是這一層在第 t 個 token 的輸入（類似 attention 裡的 query/key/value 經過投影而來），h(t) 是跨 token 傳遞、大小固定的隱藏狀態——但它不是像 RNN 那樣的向量，而是一個矩陣,因此能帶有更多表示能力。dt(t) 是每個 head 一個純量，代表狀態要更新多少,所有 dt 值皆為負,所以當 dt(t) 為 0 時狀態維持不變；x(t) 的角色類似 attention 中的 value，B(t) 類似 key，c(t) 則類似用來把狀態混合成輸出的 query；A、D 則是模型學到的參數。

直接照遞迴式逐步計算（for-loop）很適合推論階段，但訓練與 prefill 需要更快的做法。文章推導出,只要先把一個 chunk 內所有 token 的 b(t) 疊成矩陣 B、x(t) 疊成矩陣 X，就能用一次矩陣乘法 B·Xᵀ 直接跳算到這個 chunk 結尾的隱藏狀態,不必逐步展開中間的每個狀態。輸出的計算同理也能重新表達成 Tensor Core 友善的矩陣乘法,只是需要加上一個類似 causal attention 的三角遮罩,把「未來」的項目蓋掉。若再把衰減項（exp(a(t))）放回來，透過把運算搬到 log 空間、用累積和取代連續乘法，依然能維持矩陣乘法的形式,只要在乘法前先把 B（或 X）的每一列乘上對應的指數項即可。由於所有 a(t) 皆為負值,這個累積和之差必為負,代表式子裡出現的指數值都不會超過 1，確保了數值穩定性。

這整套計算最終拆成三個 kernel：`chunk_cumsum` 負責計算每個 chunk 內 a(t) 的累積和；`fwd_pass_state` 利用前述的跳算公式，算出每個 chunk 開頭的隱藏狀態；`compute_out` 則用每個 chunk 算好的起始隱藏狀態，算出該 chunk 的輸出。

🧩 **cuTile：用 Python 寫 tile 級 GPU kernel**

NVIDIA CUDA Tile（cuTile）是一套基於 Python 的 DSL 與平行程式設計模型，把 thread 與 warp 層級的排程細節抽象到 tile 層級的高階原語背後，讓開發者可以用 Python 寫 GPU kernel，同時讓編譯器最佳化自動對應到 Tensor Core 等進階硬體功能。Jane Street 作為 cuTile 的早期採用者,把 Mamba-2 用 cuTile 實作出來,並與 NVIDIA 合作最佳化這幾個 kernel。

⚠️ **使用門檻**

要使用 cuTile,需先符合 cuTile Python Quickstart 指南列出的環境需求，文章中的 kernel 實作皆以 `import cuda.tile as ct` 的方式引入。

🎯 **實務啟示**

對想自己動手寫 GPU kernel、但又不想深入 thread/warp 排程細節的團隊，cuTile 提供了一條用 Python 寫 tile 級 kernel、同時吃到 Tensor Core 加速的路徑；而 Mamba-2 這套「用跳算公式避免逐步展開」的技巧，也是實作其他線性遞迴型序列模型時值得參考的通用招式。

🔗 **來源**
- 標題：Accelerating Mamba-2 with High-Performance Forward Pass Kernels in NVIDIA CUDA Tile
- 作者／機構：Tanya Lenz, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/accelerating-mamba-2-with-high-performance-forward-pass-kernels-in-nvidia-cuda-tile/

#NVIDIA #Mamba2 #CUDA #cuTile #JaneStreet #TensorCores #SequenceModeling #GPUKernel #StateSpaceModel #DeepLearning
