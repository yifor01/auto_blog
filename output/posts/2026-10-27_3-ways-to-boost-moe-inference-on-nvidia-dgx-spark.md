---
title: 3 Ways to Boost MoE Inference on NVIDIA DGX Spark
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/3-ways-to-boost-moe-inference-on-nvidia-dgx-spark/
model: claude-code/sonnet
generated_at: '2026-10-27T21:30:02.899442'
score: 103
---

📌 NVIDIA 實測：三招讓 DGX Spark 上的 MoE 推理快近 3 倍

TL;DR：MoE kernel 替換、LM head 量化、投機解碼疊加後，decode 吞吐量提升 185%。

同一張 GPU、同一個模型，光靠換個 kernel、量化一層權重、再加投機解碼，吞吐量就能從 36 tok/s 衝到 103 tok/s。NVIDIA 工程團隊用 Ling-3.0-flash 在 DGX Spark 上做了一次完整拆解，而其中最有意思的,是一個把優化效果「完全吃掉」的隱藏 bug。

🤔 **先定位瓶頸：decode 是記憶體頻寬問題**

團隊對 Inclusion AI 的 Ling-3.0-flash 做 batch-size-1 的 profiling，發現 decoding 階段是 memory-bound,讀取模型權重主導了執行時間。兩個運算最吃頻寬：mixture-of-experts（MoE）運算,以及輸出層的 vocabulary 投影（LM head）。這指向兩個優化方向:減少每個 decode step 的權重讀取量，以及讓每輪驗證多生成一些 token。

測試模型是 Ling-3.0-flash-fp4：124B 總參數、每個 token 啟用 5.1B 參數的 MoE 模型，共 42 層（35 層 Kimi Delta Attention 線性注意力 + 7 層 multi-head latent attention）。每個 MoE 層會把 token 路由到 512 個 routed experts 中的 8 個，再加 1 個共享專家。模型原生支援 256K context window,可擴展到 1M token，並可依任務切換是否啟用 reasoning。

基線配置依官方 cookbook 的 W4A8 設定：FlashInfer 的 MXFP4 MoE kernel、NVIDIA CUTLASS dense GEMM，加上 `--enable-fp32-lm-head`。LM head 要把 2,560 維的 hidden state 投影到 157,184 詞彙的 vocabulary。

🧩 **招式一：換掉 MoE kernel 後端**

第一招是把 MoE 的執行後端從 `flashinfer_mxfp4` 換成 `humming`（一個透過 `humming-kernels` pip 套件發行的獨立 kernel library）。Humming 用 NVIDIA CUDA Runtime Compilation（NVRTC）,針對實際的 M/N/K 維度、資料型別與 GPU 架構,在執行時動態生成並編譯 CUBIN,再快取到 `~/.humming/cache`。這讓 kernel 能針對 Ling-3.0-flash 的形狀（包括偏窄的 moe_intermediate_size=768）特化,編譯粒度也更細:單個 kernel 幾秒內完成，相比之下 FlashInfer CUTLASS 路徑用 ninja 編譯 97 個 target,要花上幾十分鐘。

🧩 **招式二：LM head 動態 FP8 量化**

Checkpoint 中 LM head 原本以 BF16 儲存，且被列在 `modules_to_not_convert` 裡,載入時不會被量化。但它的 vocabulary GEMM 是 157,184 × 2,560，每生成一個 token 就要整塊讀一次,在頻寬瓶頸下是個高價值的壓縮目標。第二招只在建構 LM head 時套用動態 FP8 量化,模型其他部分仍沿用 checkpoint 原本的 FP8/MXFP4 設定，讀取量直接減半。啟用方式是設定 `SGLANG_ENABLE_FP8_LM_HEAD=1`，但這與基線的 `--enable-fp32-lm-head`（輸出 FP32 logits、走較慢的 vocab-GEMM 路徑）互斥，不能同時開。

🧩 **招式三：NEXTN 投機解碼，一次驗證多個 token**

前兩招降低每個 decode step 的成本，第三招則是減少 decode step 的數量。Ling-3.0-flash 內建一個 NEXTN 預測層（`num_nextn_predict_layers: 1`），可以直接拿來當 draft model,不需要額外訓練或下載。實測配置用 3 個 draft step 搭配 4-token 驗證視窗:每一輪 draft 依序預測 3 個 token，target 一次驗證 4 個位置，接受正確的前綴。

這招的收益取決於兩個數字:accept length（每輪平均接受的 token 數）與驗證成本比（一次驗證相對一次正常 decode 的成本），實測約為 2.26。有意思的是，驗證成本的主要來源不是 attention（batch size 1 下 KV 讀取量相對於權重讀取很小），而是 MoE 專家活化:正常 decode 一次只活化 8 個專家，驗證一次處理 4 個 token,最多可能活化到 32 個專家。

📊 **疊加效果：單項 +9.3%，三招疊加 +185.1%**

| 配置 | TPOT | Decode 吞吐量 | 相對基線 |
|---|---|---|---|
| 基線 | 27.71 ms | 36.09 tok/s | — |
| + Humming MoE 後端 | 25.35 ms | 39.45 tok/s | +9.3% |
| + 線上 FP8 LM head | 22.76 ms | 43.94 tok/s | +21.7% |
| + MTP（NEXTN，3 steps / 4 draft tokens） | 9.72 ms | 102.88 tok/s | +185.1% |

（測試條件:32K input token、2K output token、batch size 1 的合成工作負載。疊加 MTP 後 accept length 達到每輪 3.90 個 token。）

⚠️ **一個會讓優化「反而變慢」的整合陷阱**

文章特別點出一個踩雷點:當線上 FP8 LM head 量化與 MTP 同時啟用時，draft model 必須與 target 共享整個 LM head 模組,而不能只共享權重張量。原始的 Ling NEXTN 實作並未開放這個介面——沒有它,系統會悄悄 fallback:draft 收到的是 FP8 權重,卻把它當成 BF16 解讀,導致 accept length 掉到 1.00，吞吐量甚至比完全不做任何優化還低。解法是透過正確介面共享完整的 LM head 模組，才能恢復正常的接受率。團隊也提醒，這組合成測試使用重複性較高的輸出與簡單抽樣,系統性地高估了投機解碼的收益;他們另外用全部 1,319 道 GSM8K 題目做了嚴格的 end-to-end 比較（five-shot、temperature 0.6、top_p 0.95、啟用 CoT），所有變數除了這三項優化外都保持一致,但文中並未給出具體的 end-to-end 分數。

🎯 **實務啟示**

如果你的 MoE 模型在單請求場景下吃緊在頻寬而非算力，這三招的順序值得參考:先用專用 kernel 砍 MoE 讀取成本，再量化 LM head 這種「每個 token 都要整塊讀」的層，最後才疊投機解碼。但疊加優化前務必確認元件之間真的共享了正確的狀態（像這裡的 LM head 模組），否則合成 benchmark 看起來很美,實際部署卻可能比什麼都不做更慢。

🔗 **來源**
- 標題：3 Ways to Boost MoE Inference on NVIDIA DGX Spark
- 作者／機構：Yang Liu, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/3-ways-to-boost-moe-inference-on-nvidia-dgx-spark/

#MoE #LLMInference #NVIDIA #DGXSpark #SpeculativeDecoding #Quantization #SGLang #FP8 #InferenceOptimization #AIInfrastructure
