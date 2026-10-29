---
title: 'Prime Intellect Releases Prime Mega MoE: Trainable Fused MoE Kernel, 3.11x
  Faster Forward Pass'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/29/prime-intellect-prime-mega-moe-fused-moe-kernel-training/
model: claude-code/sonnet
generated_at: '2026-10-29T21:57:12.931926'
score: 105
---

📌 Prime Intellect 補上 MoE 訓練缺的那塊:反向傳播加速 3.11 倍

TL;DR:Prime Intellect 為 DeepSeek 的 Mega MoE kernel 補上反向傳播,讓 MoE 訓練步驟最高快 55%。

DeepSeek 在今年 4 月把 Mega MoE kernel 加進 DeepGEMM 函式庫時,只做了前向傳播——這意味著這顆快速 kernel 只能用在推理,訓練時 GPU 依然得在搬資料與等通訊之間反覆空轉。Prime Intellect 這次補的,正是那塊缺失的反向傳播。

🤔 MoE 訓練裡,GPU 到底在等什麼

在 MoE 模型中,每個 token 只會被送到一小部分的 expert,而這些 expert 分散在不同 GPU 上。於是每一層都要把 token 送出去、在對應 GPU 上做 expert 運算、再把結果送回來,而這套流程在前向與反向傳播都要各跑一次。在一般做法裡,這些步驟是分開執行的:GPU 先排序 token,等傳輸層把資料送達,再開始運算,算完後再把結果送回去、繼續等——這些等待就是白白浪費的 GPU 閒置時間。

🧩 一顆 kernel 融合所有步驟,現在反向也能重疊

DeepSeek 的 Mega MoE 把這整條鏈用一次 kernel 呼叫取代:融合 expert-parallel dispatch、兩層 expert 線性層、SwiGLU 與 combine 步驟。當一組 token 還在傳輸途中,kernel 就先對已經到達的另一組 token 做運算,並透過 GPU-only 的 scratch buffer 跳過中間張量的搬動——但這顆 kernel 原本只實作了前向傳播。

Prime Intellect 寫出了缺的反向 kernel,同樣採用重疊式設計,支援 BF16、MXFP8(限 Blackwell)與 blockwise FP8(限 Hopper)三種資料型別。prime-rl 的設定檔還額外提供 fp8_bwd 模式,讓前向用 BF16、反向用 FP8。

📊 完整訓練步驟最快 55%,但反向的加速幅度本來就比前向小

以下數字皆為 Prime Intellect 自行回報,測試環境為 8×H200 節點、FP8、16,384 token 序列,並開啟完整 activation checkpointing,每項結果取第 6 到第 20 步的平均值。

相較 TorchTitan,30B 模型的吞吐量從每 GPU 每秒 5,337 tokens 提升到 7,886 tokens;235B 模型則從 1,094 提升到 1,697。prime-rl 自身的基準則是用 torch all-to-all 搭配 DeepGEMM FP8 expert 組合。在單一 MoE 層的測試中(1 節點、8×H200、EP=8、128 個 expert、top-8、隨機路由),呈現出一致的模式:前向傳播的加速幅度遠大於反向傳播。官方宣傳的「最高 3.11 倍」,指的其實只是前向傳播部分。

⚠️ 不同基準之間不能直接比較

TorchTitan 本身宣稱的 41% 加速,是在完全不同的設定下測出來的(B200、671B 模型、BF16 基準),與 Prime Intellect 這裡的測試條件並不相同,兩者數字不應直接拿來類比。

🎯 實務啟示

對正在訓練 MoE 模型的團隊,Prime Mega MoE 是個可以直接接上 prime-rl 的 dispatch backend:只要在設定檔的 [trainer.model.moe.dispatch] 下將 type 設為 "mega_moe",並從 bf16、mxfp8、fp8、fp8_bwd 中選擇精度即可啟用,訓練用的 kernel 以 prime-kernels 提供的預編譯 DeepGEMM wheel 形式發佈(官方標準版 DeepGEMM 並未內建)。對於本來就在用 Qwen3 MoE 架構訓練的團隊,這類基礎設施層級的最佳化,直接換算成可觀的 GPU 工時節省。

🔗 來源
- 標題:Prime Intellect Releases Prime Mega MoE: Trainable Fused MoE Kernel, 3.11x Faster Forward Pass
- 作者/機構:Asif Razzaq,MarkTechPost
- 連結:https://www.marktechpost.com/2026/10/29/prime-intellect-prime-mega-moe-fused-moe-kernel-training/

#MoE #GPUOptimization #DeepGEMM #PrimeIntellect #DeepSeek #LLMTraining #Kernel #DistributedTraining #OpenSource #MachineLearning
