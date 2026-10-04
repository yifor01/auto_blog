---
title: 'Aleph Alpha Releases Kolibri: A 78.1B Open-Weight English-German MoE Model
  With Only 3.46B Active Parameters'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/04/aleph-alpha-releases-kolibri-a-78-1b-open-weight-english-german-moe-model-with-only-3-46b-active-parameters/
model: claude-code/sonnet
generated_at: '2026-10-04T20:14:55.885401'
score: 95
---

📌【Aleph Alpha】歐洲主權 MoE 模型，780 億參數僅啟用 3.46B

TL;DR：Kolibri 是為德國、歐盟監管產業打造的雙語 MoE 開源模型，技術報告細節完整。

當多數大模型競相比拼參數規模時，Aleph Alpha 選了另一條路：把 780 億參數的模型做成每個 token 只啟用 3.46B（4.4%），目標不是刷榜，而是讓公務機關、工業與航太等受監管產業能在自己的基礎設施上合規部署。

🤔 **為合規而生的設計目標**

Kolibri（代號 Kolibri-1）由德國團隊從頭到尾自建，涵蓋資料、架構、訓練基礎設施、後訓練與評估整條管線，訓練機房設在德國與芬蘭。設計目標對準歐盟《通用人工智慧行為準則》（GPAI Code of Practice）、《AI 法案》與 GDPR，Aleph Alpha 本身是該行為準則的簽署方，資料流程在訓練前會先去識別化個資。模型以 Apache 2.0 授權開源在 Hugging Face。

🧩 **MoE 架構：384 個 expert，只挑 6 個加 1 個常駐**

Kolibri 疊了 50 層 transformer block，模型寬度 2,560。每個 MoE 層用 sigmoid router 對全部 384 個 routed expert 評分，每個 token 送去 top 6 個，再加上恆定啟動的 1 個 shared expert；負載平衡靠 Exact Quantile Balancing 與 Load-Error Injection 兩個機制處理。

Attention 採用 grouped-query attention，48 個 query head 配 4 個 KV head。每 5 層裡有 1 層用不帶位置編碼的 full attention，其餘 40 層改用滑動視窗 attention（只看前 512 個 token）搭配 RoPE。因為大部分層的 KV cache 是固定大小，只有 10 層會隨 context 長度增長，Aleph Alpha 團隊表示在相同運算量下，這種混合架構能支援比純 full attention 模型長 4 倍的序列。

Tokenizer 用 UniBPE（用 Unigram loss 評分每次合併，而非傳統 BPE 的頻率），128,000 詞彙量。在德文文本上達到 4.90 bytes/token，相比 GPT-5 tokenizer 的 4.35，等於在德文網頁文本上省下 11.2% 的 token 數；英文則是 4.58 對 GPT-5 的 4.67。

📊 **訓練規模與基準表現**

預訓練在 768 張 NVIDIA B200 上跑了 20T token，接著是 65,536 序列長度下的 3.44T mid-training token，再用 201B token 在 262,144 序列長度做長 context 訓練。Aleph Alpha 另外加入超過 2T 從網路蒐集或合成生成的德文 token。後訓練結合 SFT（混合 MergeMix）與超過 120 萬筆內部任務的強化學習，並用 Merlin-Arthur 協定訓練模型在檢索內容不足以支撐答案時主動拒答。

英文基準上，Kolibri 在 GPQA Diamond 拿下 84.3、AIME 2025 為 96.9、AIME 2026 為 96.0，英文 agentic 平均 63.4 與 Qwen3.5 35B-A3B 打平；但在 BFCL v4 落後，61.4 對 Qwen3.5 的 70.5。相較於稠密模型 Qwen3.8 27B（英文 80.2、德文 79.9 整體更高），Kolibri 整體分數較低，但 Qwen3.8 27B 每個 token 啟用的參數量大約是 Kolibri 的 8 倍。對比自家上一代 Kolibri Origin，新版每張 GPU 的解碼產出量約快 2.7 倍，英文分數高出 21.4 分。

⚠️ **代價所在**

啟用參數少帶來的效率提升是有代價的：Kolibri 在 agentic 工具呼叫（BFCL v4）上明顯落後 Qwen3.5，整體分數也不及稠密的 Qwen3.8 27B，只是後者需要燒掉多倍的啟用參數量才能做到。

部署上，FP8 checkpoint 約 78GB，可在單張 B200、B300 或 H200，或兩張 H100 SXM5 上透過 vLLM 搭配專用的 Kolibri reasoning 與 tool-call parser 運行。預設 context 為 262,144 token，要開到完整 1,048,576 token 需加上 `--max-model-len 1048576` 並覆寫 `max_position_embeddings`；推理強度（reasoning effort）可透過 `chat_template_kwargs` 設定，官方建議的取樣參數是 temperature 1.0、top-p 0.97、top-k 128。

🎯 **實務啟示**

如果你的場景剛好落在歐盟監管紅線內（公部門、工業、航太等），Kolibri 提供了一條「架構、訓練、評估全透明、權重可自架」的路線,不必把資料送去境外 API。若場景不涉及合規考量,純比較推理成本與分數,稠密模型或 Qwen3.5 系列在某些任務上仍可能是更直接的選擇。

🔗 **來源**
- 標題：Aleph Alpha Releases Kolibri: A 78.1B Open-Weight English-German MoE Model With Only 3.46B Active Parameters
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/04/aleph-alpha-releases-kolibri-a-78-1b-open-weight-english-german-moe-model-with-only-3-46b-active-parameters/

#AlephAlpha #Kolibri #MoE #OpenWeight #SovereignAI #EUAIAct #LLM #GQA #vLLM #Tokenizer
