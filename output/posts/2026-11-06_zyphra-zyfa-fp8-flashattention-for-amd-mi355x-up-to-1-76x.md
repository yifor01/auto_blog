---
title: 'Zyphra ZYFA: FP8 FlashAttention for AMD MI355X, Up to 1.76x Faster'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/06/zyphra-zyfa-fp8-flashattention-amd-mi355x/
model: claude-code/sonnet
generated_at: '2026-11-06T22:17:36.494265'
score: 93
---

📌 Zyphra ZYFA：AMD MI355X 上的 FP8 FlashAttention，最高快 1.76 倍

TL;DR：Zyphra 開源 ZYFA，FP8 attention kernel 在 AMD MI355X 上比官方 AITER 快最多 1.76 倍、誤差還更低。

通常「更快」和「更準」是互相拉扯的兩個目標，但 Zyphra 這次公開的 FP8 attention kernel，宣稱在 AMD Instinct MI355X 上同時做到比官方預設 kernel 更快,而且誤差更小。

🤔 **AMD MI355X 上的長上下文 prefill attention，是 ZYFA 要解決的問題**

ZYFA（Zyphra FlashAttention on AMD）是 Zyphra 針對 AMD Instinct MI355X GPU 推出的一組 FP8 與 BF16 prefill attention kernel，定位是長上下文 prefill 用的 FP8 attention 引擎,程式碼以 Apache 2.0 授權開源。它目前驅動著 Zyphra Optimization Engine（ZOE）的 attention 引擎，而 ZOE 正是 Zyphra Cloud 的底層引擎。官方表示，在真實模型 activation 上測試，ZYFA 的 FP8 kernel 比 AMD 官方的預設 kernel 函式庫 AITER 快 1.16 到 1.76 倍；在 head dimension 128 的設定下，FP8 誤差比 AITER 低 62% 到 78%。

🧩 **BF16 用 HIP 手寫，FP8 直接手排組合語言**

實作上，BF16 kernel 以 HIP 撰寫，FP8 kernel 則是由一個 Python 產生器輸出的手排組合語言（hand-scheduled assembly）。關鍵在於：FP8 矩陣運算指令的峰值是 BF16 的兩倍，但 FP8 只能加速 QKᵀ 與 PV 這兩個矩陣乘法，兩者之間的 softmax 仍跑在向量運算單元上，速度在兩種精度下是一樣的。以 32 個 query 對 128 個 key 為例，FP8 矩陣運算需要 1,024 個 cycle，而精確計算的 FP8 softmax 需要 896 個向量 cycle，這意味著 kernel 必須做到幾乎完美的運算重疊，才能讓矩陣運算單元保持忙碌。Zyphra 的 thread trace 顯示，AITER 的矩陣運算單元有 31.7% 的 cycle 是閒置的；由於 MI355X 並不會在硬體層面追蹤矩陣指令的完成狀態,這種重疊必須靠指令順序本身來創造。

團隊因此設計了一個名為「Lean P」的技巧：e4m3 格式的位元模式，當作整數讀取時,每次數值翻倍都會固定增加 8，也就是說 2 的 x 次方大致等於 8x 加上一個常數。利用這個特性,Lean P 只需要 1 次乘加與 1 次整數轉換,就能寫出每個 FP8 機率值,把每個 block 的 softmax 向量 cycle 數從 896 降到 384。配合 2 個 wave 共用一個 SIMD（一個負責發出矩陣指令，另一個計算機率值，兩者互換角色），使用 Lean P 後，矩陣運算單元在穩定狀態下的忙碌率提升到 86%，相較精確計算 P 的 60% 有明顯改善。另外，每 64 個 key 組成的機率 block 會先乘上一個 2 的次方再做捨入，CDNA4 的 scaled matrix instruction 可以免費消去這個係數；ZYFA 還會用額外一次矩陣指令，除以捨入後機率的總和。

📊 **實測結果：最高 1.76 倍，部分 shape 下超過 2 倍 TFLOP/s**

| 測試模型／指標 | ZYFA | AITER |
|---|---|---|
| Mistral-7B（16K，真實 activation） | 1.16x | 基準 |
| Qwen3-8B（16K，真實 activation） | 1.17x | 基準 |
| DeepSeek-V2-Lite（16K，真實 activation） | 1.76x | 基準 |
| Head-dim 128（32K，高斯 benchmark） | 2,672 TFLOP/s | 1,944 TFLOP/s |
| MLA shape（32K，高斯 benchmark） | 2,464 TFLOP/s | 1,237 TFLOP/s |
| Mistral-7B 層（TFLOP/J） | 1.94 | 1.60 |
| Qwen3-8B 層（TFLOP/J） | 1.91 | 1.56 |

值得注意的是，MI355X 的實際時脈會受「有多少 operand 位元翻轉」影響：AITER 允許更多小機率值被歸零或變成 subnormal，位元翻轉較少、時脈因此跑得較高（例如在 Mistral-7B 層上，ZYFA 跑在 1,628MHz，AITER 跑在 2,108MHz），但 ZYFA 整體所需 cycle 數仍然更少，最終還是更快。Zyphra 團隊也因此建議,基準測試應該在真實 activation 與持續穩定時脈下進行，而非單純比較理論峰值。

💡 **誤差也更低：這不只是用精度換速度**

和 fp64 attention 相比，ZYFA 的 FP8 誤差是 AITER 的 0.22 倍（Mistral-7B）與 0.38 倍（Qwen3-8B），整體水準和 Composable Kernel、Triton 相差不到幾個百分點。在完整 Mistral-7B 模型上，與 fp64 的 KL divergence，ZYFA 是 3.4×10⁻³，AITER 是 5.9×10⁻³；ZYFA 的輸出在 7,200 次啟動中更是逐位元（bitwise）一致。官方也指出，全模型 FP8 誤差大部分來自 Q、K、V 的量化本身，對 Q、K 做 Hadamard 旋轉大約能把這部分輸入誤差減半，在 Mistral-7B 上只多花約 0.1% 的 attention 時間。

⚠️ **跨廠商比較要小心,也還沒有 NVIDIA 的數據**

文中強調，這些跨廠商數字來自不同的輸入與時脈設定，Zyphra 並未實際測量 NVIDIA GPU 上的對應表現，因此不宜直接拿來做廠商間的效能定論。

🎯 **實務啟示**

如果你的推論基礎設施跑在 AMD Instinct MI355X 上，且長上下文 prefill 是效能瓶頸，ZYFA 的開源 kernel 值得直接拿來替換 AITER 做基準測試；它背後「用指令排程換取運算單元重疊率」的思路，對自行手刻 kernel 的團隊也是一個值得參考的優化範例。

🔗 **來源**
- 標題：Zyphra ZYFA: FP8 FlashAttention for AMD MI355X, Up to 1.76x Faster
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/06/zyphra-zyfa-fp8-flashattention-amd-mi355x/

#Zyphra #FlashAttention #FP8 #AMD #MI355X #GPUKernel #LLMInference #Quantization #OpenSource #HPC
