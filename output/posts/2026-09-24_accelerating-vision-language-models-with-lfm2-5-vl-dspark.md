---
title: Accelerating vision-language models with LFM2.5-VL-DSpark
source: HuggingFace Blog
url: https://huggingface.co/blog/LiquidAI/lfm2-5-vl-dspark
model: claude-code/sonnet
generated_at: '2026-09-24T20:38:55.116202'
score: 103
---

📌 LFM2.5-VL-DSpark：VLM 推測解碼實測最高加速 3.13 倍

TL;DR：Liquid AI 釋出 VLM 專用推測解碼草稿模型，多推論框架即測即用且不損輸出品質。

推測解碼（speculative decoding）在純文字 LLM 上已證明能大幅加速，但視覺語言模型（VLM）多了一個影像編碼與大量視覺 token 的前置流程，這個技巧還適用嗎？Liquid AI 針對自家 LFM2.5-VL-3B 給出了實測答案。

🤔 VLM 的推測解碼要解決什麼問題

繼日前推出文字版 LFM2.5-DSpark 草稿模型後，Liquid AI 這次釋出實驗性的 LFM2.5-VL-3B 專用 DSpark 草稿模型，用少量記憶體換取更大的解碼加速，且不改變輸出品質。官方數字：on-device 解碼加速最高 3.13 倍、H100 上最高 2.66 倍，端到端加速最高分別達 2.62 倍與 2.27 倍；草稿模型只增加 2.8 億參數，相當於 3B 目標模型多 8.9% 的體積。

🧩 沿用文字草稿的推測解碼算法，只是輸入模態變了

視覺草稿模型（vision drafter）沿用與文字版 LFM2.5-DSpark 草稿模型相同的架構：擷取目標模型在固定幾層（tapped layers）的隱藏狀態，以此為條件草擬一個包含 k 個候選 token 的區塊。關鍵在於，影像 patch 與文字 token 會在進入這些層之前先被投影到同一個共享表示空間，因此草稿模型看到的隱藏狀態向量維度一致，不論輸入是圖還是文字，推論演算法因此與文字模型完全相同，不需要額外設計。

訓練上沿用 DSpark 配方，使用依預期服務工作負載加權過的視覺語言 SFT 資料混合集。團隊針對 3、4、5 層做了消融實驗，最終選定 4 層、block size 為 9 的純 attention 草稿模型架構；在最終資料混合上訓練 10 個 epoch，並在每個 epoch 後量測接受率（acceptance rate），結果隨訓練 token 增加而提升，直到報酬遞減。推論時建議依硬體選擇 block size 8 或 9。

模型組成細節（參數量）：

| 元件 | 參數量 |
|---|---|
| Decoder stack（4 層） | 193.0M |
| Hidden-state projection | 21.0M |
| Markov head | 65.5M |
| Norms + confidence head | 6.4k |
| 總計 | 279.5M |

📊 六項視覺任務的實測加速

團隊依循 MMSpec benchmark，在 general VQA、text VQA、image captioning、chart VQA、複雜推理、多輪對話等六種視覺任務上量測 on-device 與 GPU 推論表現，block size 統一為 8：
- MLX on M5 Max：解碼依任務提升 2.30 倍到 3.13 倍，端到端提升 1.56 倍到 2.62 倍。
- llama.cpp on M3 Ultra：解碼提升 1.57 倍到 2.14 倍，端到端提升 1.30 倍到 1.77 倍。
- H100：解碼最高提升 2.66 倍，端到端提升 1.64 倍到 2.27 倍。

⚠️ 邊緣裝置上的加速上限：Amdahl's law

推測解碼只加速「解碼」階段，不加速視覺編碼與 prefill。VLM 的 prefill 比純文字模型更重：影像要先經過視覺編碼器，語言主幹接著要處理數百個視覺 token 加上文字提示。邊緣裝置算力遠低於資料中心 GPU，prefill 在整體延遲中的佔比因此更高（M5 的每核心 GPU 神經加速器能部分縮小這個差距）。這正是 Amdahl's law 的體現：當 prefill、視覺編碼這類無法被加速的部分佔比高時，即使解碼加速再大，端到端的整體收益也會被壓縮。

🧩 怎麼用

三個推論框架都已日內支援：

SGLang（需支援 DSpark 的 build，PR #40651）：
```
python -m sglang.launch_server \
  --model-path LiquidAI/LFM2.5-VL-3B \
  --speculative-algorithm DSPARK \
  --speculative-draft-model-path LiquidAI/LFM2.5-VL-3B-DSpark \
  --speculative-draft-attention-backend flashinfer \
  --speculative-dspark-block-size 9 \
  --disable-radix-cache
```
接著查詢 OpenAI 相容端點 http://localhost:30000/v1，block size 會從草稿模型的 config.json 讀取；拿掉三個 `--speculative-*` 參數即是基準版本。

llama.cpp（需對應 build，PR #29339）與 MLX-VLM（需對應 build，PR #2280）也各自提供對應指令，細節可參考原文。

值得注意的是，推測解碼是精確（exact）的：目標模型會驗證每個被提議的 token，貪婪解碼下的輸出與單獨使用目標模型完全一致，每次回應的計時資訊會回報 draft_n 與 draft_n_accepted。

🎯 實務啟示

模型與草稿模型皆以 Safetensors 與 GGUF 格式開源在 Hugging Face 上，權重可自由下載、微調、部署。若你的 VLM 服務瓶頸主要在解碼階段（例如多輪對話、長輸出的場景），這類草稿模型是值得優先嘗試的低成本加速手段；但若場景是短輸出、長 prompt（例如單次描述一張高解析度圖），別忘了 Amdahl's law 提醒的天花板，實際效益要看 prefill 佔比而定。

🔗 來源
- 標題：Accelerating vision-language models with LFM2.5-VL-DSpark
- 作者／機構：Liquid AI
- 連結：https://huggingface.co/blog/LiquidAI/lfm2-5-vl-dspark

#SpeculativeDecoding #VLM #EdgeAI #LiquidAI #LLMInference #SGLang #llamacpp #MLX #OpenWeights #ModelOptimization
