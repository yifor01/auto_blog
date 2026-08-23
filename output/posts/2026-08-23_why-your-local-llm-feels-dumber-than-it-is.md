---
title: Why your local LLM feels dumber than it is
source: Hacker News
url: https://forum.level1techs.com/t/why-your-local-llm-feels-dumber-than-it-is/253917
model: claude-code/sonnet
generated_at: '2026-08-23T06:12:19.913862'
score: 94
---

📌 本地 LLM 為何比雲端笨？答案可能藏在 Attention Backend 裡

TL;DR：同一份 BF16 權重只換 vLLM 的 attention backend,長 context 後段就開始出現 token 分歧。

同一組權重、同一張 GPU,只換掉 vLLM 底層選用的 attention backend,模型在十萬 token 的長對話後半段就開始選出不同的下一個字。這篇 level1techs 論壇的技術實驗,試圖回答一個很多人有感、卻很少人量化過的問題:為什麼你本機跑的模型,「感覺」比官方 demo 笨。

🤔 你的「參考實作」跟你的本機環境,根本是兩套系統

作者把發布模型、提供官方 benchmark 數據並自行託管的實驗室稱為「reference implementation」。這些實驗室的硬體和軟體都與一般使用者的環境相去甚遠。每一套跑 LLM 的硬體與軟體組合,彼此都有些微差異:家用主機常混用不同世代的 GPU,而不同 GPU 的指令集,即使套用完全相同的權重,計算下一個 token 的方式也不會完全相同。作者以自己拉下來的 vLLM nightly container 為例,裡面就有 734 個套件(其中 252 個是透過 uv/pip 安裝的 Python 套件)——也就是 734 套各自帶著自己 bug 與非文件化行為的程式碼,你的實作路徑注定與別人不同。

作者也提醒,評估這個落差不能只靠把溫度調到零、貼三句測試提示詞就下結論。zero-shot 測試不能代表大多數 agentic 任務,需要長 context 的工具呼叫與領域知識評測,才能找出自己這套環境相對於同一份權重的其他實作,弱點究竟在哪。

🧩 從 logits 到 KL Divergence:量化「感覺不對」

文中先鋪陳基礎概念:logits 是模型對每個候選下一個 token 的分數,經正規化為機率分布,再通過設定好的 sampler,最後由 detokenizer 轉回文字。取樣參數(如溫度、top-p)通常寫在模型的 model card 上,設定錯誤會造成明顯異常——例如溫度設太低,正是某些 Qwen 模型卡在 THINK 輸出裡跳不出來的原因之一。

當下一個 token 的機率變化夠大,輸出路徑就可能整個岔開,這正是「感覺哪裡怪怪的」的起點。這時可以用 KL Divergence(KLD)量化:把輸出 logits 轉成機率分布,測量它離某個選定基準分布有多遠。KLD 越低代表越接近基準,但不代表「更聰明」,而且 KLD 是有方向性的,兩個分布誰在前誰在後會影響結果。作者也提醒:如果 HF 上某個量化模型卡宣稱極低的 KLD,卻沒有揭露參考 checkpoint、完整執行環境、評測文本、校準資料、context 長度、取樣位置、KL 方向、詞彙截斷方式與聚合方法,這個數字就無法被解讀。

📊 Test 1:只換 attention backend,長 context 後段就開始分歧

第一組實驗鎖定 prefill(提示詞處理)階段可選用的 attention backend——這會同時影響速度與精確度,且不同 GPU 家族/SM 運算能力需要不同的 CUDA kernel。實驗以 Qwen3.6-27B 的官方 BF16 checkpoint,在 RTX PRO 6000 Blackwell GPU 上以 tensor parallelism 1 執行,KV cache 為 BF16、不做任何權重/activation/KV-cache 量化,使用 pinned nightly vLLM build、eager execution,關閉 CUDA graphs、prefix caching 與 MTP,採 2k-token chunked prefill。Qwen3.6-27B 是稠密而非 MoE 模型,但屬於混合架構:64 層中每 3 層 Gated DeltaNet/linear-attention 就接 1 層 full-attention,只有這 16 層 full-attention 會用到可選的 attention backend,Gated DeltaNet 路徑維持不變。

測試用的 workload 是「Prompt 2」——一段來自真實 Turnstone lab 工作流、包含多次工具呼叫與真實產出物的約十萬 token context,刻意選來貼近本地 agent 的實際使用情境,而非合成的 needle-in-haystack 測試,也因此不曾出現在任何公開 benchmark 或訓練資料集中,沒有人能針對它做過 benchmax 或量化校準。

vLLM 中可選的三種 full attention backend 分別是 FlashAttention 2、FlashInfer 與 Triton Attention,實驗中唯一更動的變數就是 backend,其餘軟硬體堆疊維持不變;作者另外做了同 backend、跨 GPU 的重複性對照。量測方式是每 32 個提示詞 token 就以 BF16 擷取一次完整詞彙表的 logits,KLD 等分布比較則事後以 FP64 從儲存的 logits 計算。Top-1 一致性指的是最高 logit 的 token(greedy argmax)是否相同,三個 backend 都對照同一份「強制」的 token 歷史來評估,並不讓某次選擇的分歧去改變後續歷史,以維持比較的可控性。結果顯示:在提示詞前面數千個 token,三種 backend 選出的下一個 token 完全一致;但到了較長 context 的後段,backend 之間開始出現分歧。

⚠️ 這只是第一個實驗,還沒回答「分歧會不會搞砸任務」

作者特別強調,這個 Test 1 的設計是「強制對照」——刻意不讓某次 token 分歧影響後續生成,所以能看到的只是數學上的分歧程度,還無法回答一個未受控的生成會分岔多遠,或某次工具呼叫是否真的會因此失敗。作者表示這部分留給後續的 Test 2。

🎯 實務啟示

如果你的本地部署「感覺比官方 demo 笨」,問題未必出在權重或量化精度,也可能藏在 attention backend、sampler 設定這類容易被忽略的推論堆疊細節裡。在下判斷前,先確認自己用的溫度、top-p 是否與 model card 一致,並用貼近真實 agentic 工作流(而非合成短提示)的長 context 測試去比較不同 backend,而不是只看單一 benchmark 分數。

🔗 來源
- 標題：Why your local LLM feels dumber than it is
- 作者／機構：felineflock, level1techs 論壇（Hacker News 討論,265 points, 86 comments）
- 連結：https://forum.level1techs.com/t/why-your-local-llm-feels-dumber-than-it-is/253917

#LLM #LocalLLM #vLLM #Inference #Quantization #AttentionMechanism #KLDivergence #MachineLearning #GPU #AIInfrastructure
