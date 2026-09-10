---
title: 'To Infinity and Beyond: ThunderKittens Now on NVIDIA Vera Rubin NVL72!'
source: Together AI
url: https://www.together.ai/blog/to-infinity-and-beyond-thunderkittens-now-on-nvidia-vera-rubin-nvl72
model: claude-code/sonnet
generated_at: '2026-09-10T20:02:51.114923'
score: 95
---

📌 搶先實測 NVIDIA Vera Rubin：ThunderKittens 如何榨出 22 PFLOPS

TL;DR：Together AI 在 Vera Rubin 上優化 ThunderKittens GEMM 核心，逼近算力天花板。

🎣 換一張新的 GPU，理論算力翻倍，實際效能呢？Together AI 的 kernels 團隊把既有的 ThunderKittens NVFP4 GEMM 核心原封不動搬到 NVIDIA Vera Rubin NVL72 上，得到的答案是：只達到 roofline 的 42.1%。

🤔 Rubin 延續 Blackwell 程式設計模型，卻餵不飽新的 Tensor Core

ThunderKittens 是 Together 開發的 GPU kernel 函式庫，先前已針對 NVIDIA Blackwell 架構寫出效能不錯的 GEMM 核心。Blackwell 第五代 Tensor Core 把程式設計模型整個改了一輪：Hopper 的 `wgmma` 指令由整個 warpgroup 集體發出，Blackwell 的 `tcgen05` 指令則改由單一 thread 發出，讓一個小型的 producer warp 就能驅動 Tensor Core；累加器也從暫存器搬進 Tensor Memory，運算元直接從共享記憶體讀取，讓單一 MMA 可以橫跨兩個 SM 上的兩個 CTA。為了在 Blackwell 上打到有競爭力的效能，Together 的 GEMM 核心會啟動 threadblock cluster 讓 CTA pair 透過 TMA multicast 共享運算元（把 HBM 記憶體流量砍半）、把 warp 依角色分工（loader 用 TMA 把 A、B 搬進共享記憶體，單一 MMA warp 驅動 Tensor Core，consumer warpgroup 把算完的累加器從 tensor memory 搬到 HBM），並以 persistent 方式執行，讓一個 tile 的輸入還在串流進來時，前一個 tile 的輸出已經在往外送。

由於 Vera Rubin 保留了 Blackwell 的程式設計模型，這些舊核心可以直接跑，但團隊觀察到 NVFP4 與 FP8 核心分別只達到 roofline 的 42.1% 與 44.4%，還有大量最佳化空間。核心問題是：Rubin 讓 Tensor Core 消耗運算元的速度變成兩倍，但舊核心的資料搬運邏輯跟不上，餵不飽新的 Tensor Core，因此需要讓每個 tile 從晶片上已有的資料裡榨出更多重複使用（reuse）。

🧩 Vera Rubin 帶來的五個關鍵新特性

先看硬體規格對比：

| 項目 | NVIDIA HGX B200 | NVIDIA Vera Rubin NVL72 |
|---|---|---|
| NVFP4 Tensor Core | 9 PFLOPS / GPU | 35 PFLOPS / GPU |
| FP8 Tensor Core | 4.5 PFLOPS / GPU | 17.5 PFLOPS / GPU |
| FP16 / BF16 Tensor Core | 2.25 PFLOPS / GPU | 4 PFLOPS / GPU |
| 記憶體頻寬 | 8 TB/s / GPU | 22 TB/s / GPU |
| SM 數量 | 148 / GPU | 224 / GPU |
| 峰值功耗 | 1000W / GPU | 2300W / GPU |

針對寫出效能夠好的 GEMM，文章特別點出五項新特性：

1. **Tensor Core 一次吃兩倍的 K**：`tcgen05.mma` 每個 step 沿著 K 維度消耗固定 bytes，Blackwell 是 32 bytes，Rubin 可以拉到 64 bytes。MMA 本身耗費的 cycle 數不變，代表同一個指令視窗可以塞進兩倍的工作量。ThunderKittens 用一個新的 template 參數表示：
```
mma_ABt(...);       // Blackwell 預設：32-byte K step
mma_ABt<64>(...);   // Vera Rubin：64-byte K step
```

2. **Tensor Memory 擴充到 576 欄**：Blackwell 引入的 tensor memory 原本是 128 lane x 512 column x 32-bit 的空間，Rubin 擴充到 576 欄，多出 32 KiB 可用空間；但這些額外欄位只能透過 PTX 9.4 新增的 `.exclusive` qualifier 存取（確保一個 SM 上只有一份存活的 tensor memory 配置），非 exclusive 的配置仍上限 512 欄且必須是 2 的次方。

3. **共享記憶體增加到 328 KiB**：Hopper 與 Blackwell 提供 228 KiB 共享記憶體，Rubin 引入可動態擴增到 328 KiB 的「oversized shared memory」模式，需在 host 端呼叫 `cuFuncSetAttribute` 搭配 `CU_SHARED_MEMORY_MODE_ALLOW_OVERSIZED_SHARED_MEMORY` 設定。

4. **B 側 Collector Buffer**：Blackwell 的 collector buffer 讓下一道 MMA 指令可以直接沿用暫存好的 A tile，不必重新從共享記憶體讀取；Rubin 把這個機制延伸到 B tile（`.collector::b::*`）。透過 FILL／USE／LASTUSE／DISCARD 四種標籤描述每個運算元對 collector buffer 的動作，例如一個 2x2 區塊如果雙邊都做 collector，四道 MMA 的運算元讀取次數可以從八次降到五次。

5. **A 提前釋放**：PTX 9.4 新增 `tcgen05.commit.sync_restrict::shared::read::mma::a` 指令，讓 MMA 一讀完 A 運算元就能提早觸發 barrier，不必等整個 MMA 結束，producer 可以更早開始搬運下一階段的資料。ThunderKittens 對應提供新的 commit 類型：
```
tensor_commit<2>(inputs_finished[stage], mask);   // MMA 完全結束時觸發
tensor_aread_commit<2>(A_finished[slot], mask);   // MMA 讀完 A 就觸發
```

📊 從 88% 天花板出發，目標超越 22 PFLOPS

文章指出，光是把既有 32-byte K step 的編碼直接切換成寬版編碼，效能只有小幅改善，遠不到理論的兩倍；在這個編碼下 Rubin 的 ISA 天花板約 16.8 PFLOPs，而 Together 的 NVFP4 Blackwell GEMM 原封不動搬過來就已經達到 14.7 PFLOPs（天花板的 88%），代表瓶頸不在指令寬度本身，而是資料能不能餵得夠快。作者接下來要做的，是把上述五項特性逐步整合進既有的 Blackwell NVFP4 核心，目標是推到超過 22 PFLOPS，並與 cuBLAS、CuTE DSL 打到有競爭力的水準。

💡 硬體翻倍不等於效能自動翻倍

這篇文章最值得工程師留意的觀察是：算力規格翻倍（NVFP4 從 9 到 35 PFLOPS/GPU）並不會讓既有核心自動獲得對應的加速，記憶體頻寬與晶片上資料重複使用率才是真正的瓶頸。Vera Rubin 把頻寬拉到 22 TB/s，比算力成長的倍數還低，代表新一代 GEMM 核心勢必要更積極地在 tensor memory、共享記憶體與 collector buffer 之間榨出資料重用，而不是單純依賴更寬的指令。

⚠️ 屬於階段性成果

素材本身是系列文章的第一部分，僅完成新特性介紹與問題定位（88% 天花板、需要更多資料重用），完整整合進 GEMM 核心並達成 22 PFLOPS 的具體優化過程留待後續內容說明。

🎯 實務啟示

如果你的團隊維護自家的 GPU kernel，這篇文章提醒了一件事：新硬體上市時，先用既有核心跑一次基準測試找出瓶頸在哪，比急著全面重寫更重要。ThunderKittens 把每個新特性都包成獨立的 API（`mma_ABt<64>`、`tensor_allocator` 的 exclusive 參數、collector 標籤），也示範了如何用漸進式的方式把硬體特性一項項疊加進既有核心，而不必打掉重練。

🔗 來源
- 標題：To Infinity and Beyond: ThunderKittens Now on NVIDIA Vera Rubin NVL72!
- 作者／機構：Together AI
- 連結：https://www.together.ai/blog/to-infinity-and-beyond-thunderkittens-now-on-nvidia-vera-rubin-nvl72

#ThunderKittens #NVIDIA #VeraRubin #GPUKernel #GEMM #NVFP4 #Blackwell #TogetherAI #HighPerformanceComputing #CUDA
