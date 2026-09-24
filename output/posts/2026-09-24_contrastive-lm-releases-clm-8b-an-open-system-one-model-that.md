---
title: 'Contrastive-LM Releases CLM-8B: An Open System One Model That Scores Agent
  Actions Up to 9× Faster Than Jev'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/23/contrastive-lm-releases-clm-8b-an-open-system-one-model-that-scores-agent-actions-up-to-9x-faster-than-jev/
model: claude-code/sonnet
generated_at: '2026-09-24T20:38:55.116073'
score: 104
---

📌 CLM-8B：用對比學習取代生成，動作評分快最多 9 倍

TL;DR：Contrastive-LM 開源 CLM-8B，不生成文字、只替候選動作打分數，鎖定 agent 決策場景。

當多數團隊還在把 agent 決策問題塞進「生成一段文字再解析」的框架時，Contrastive-LM 提出了一個完全不同的答案：不生成，只打分。這款名為 CLM-8B 的模型，是他們定義的新類別「Contrastive Language Models（CLM）」中第一個開源成員，主要比較對象是 TypeSafe AI 的專有 System One 模型 Jev（已於 2026 年 9 月 15 日進入限量早期使用）。

🤔 為什麼不用生成式模型做決策評分

Agent 迴圈中常見的任務，例如挑選 best-of-N 解答、路由工具呼叫、回答型別化的決策問題，本質上都是「在一組候選動作中挑一個」。傳統生成式模型要輸出文字再解析成結構化答案，而 Jev 這類 System One 模型已經改成直接回傳帶機率的型別化數值。CLM 瞄準的正是同一個介面：CLM 的 GitHub repo 提供 TypeSafe 相容 API，暴露 3 種問題類型，原本寫給 TypeSafe API 的請求可以直接透過 CLM 的 Python client 重放。

🧩 雙塔對比學習架構

CLM 訓練一個 state encoder 和一個 action encoder，用雙向 InfoNCE loss 學習。每個 encoder 是凍結的 Qwen3-8B backbone，外加一個 2000 萬參數的可訓練投影頭（projection head）。訓練過程把每個狀態向量拉向「實際被採取的動作」，同時推離其他候選動作。推論時，CLM 用狀態向量與動作向量的內積為每個候選打分，再對這些分數做 softmax 得到答案分佈。

這個設計把「狀態」與「動作」解耦：在 agent 迴圈裡，狀態每一步都在變，但動作集合大多固定不變。clm-serve 因此可以像 vLLM 的 KV cache 一樣預留一塊 GPU 記憶體，重複利用已快取的動作向量。官方測試顯示，在 1 張 RTX 4090、3 個候選動作的設定下，重複出現的狀態延遲從 1.7 毫秒降到 0.6 毫秒。Apache-2.0 授權的模型頭僅 75 MB，可在單張 NVIDIA GPU 上以 vLLM 服務 Qwen3-8B encoder 跑起來。

📊 準確率與速度的權衡

在約 10 萬筆保留測試題上，僅做 pre-training 可達 52.1% top-1 準確率；加入 mid-training 後提升到 69.2%；若從一開始就用 hard negatives 訓練，峰值只到 62.4% 後便開始過擬合。

速度面向的關鍵數字：
- 在候選數約 1,000 的情境下，模型卡宣稱 CLM 比 Jev 快 13 倍。
- 9 倍這個數字出自 T-Rex 遊戲測試，其特性是動作在不同狀態間會重複出現。
- CLM 在 T-Rex 與 Super Mario 上與 Jev 打平，但在工具呼叫（tool calling）與 WikiRacing 上落後，不過在每一項任務上速度都更快。

團隊也做了 best-of-N 驗證器（verifier）評測：由生成器產生候選解答，CLM 負責挑選。Opus 5 產生 DeepSWE 候選（best-of-4），Fable 5 產生 Terminal-Bench 2.1 候選（best-of-5），分別在 38 個保留 DeepSWE 任務與 30 個保留 Terminal-Bench 2.1 任務上評測，延遲則在 H100 上量測。團隊將這些結果稱為新的 SOTA 驗證器成績：Jev 在兩項基準上的得分都低於 pass@1，代表用 Jev 挑選反而比隨機取一個樣本還差；CLM 則快了 4.1 倍到 5.7 倍。需要注意的是，這些數字使用的是輕量微調過的模型頭，而非 zero-shot checkpoint，且僅是保留子集結果，並非完整排行榜提交。

⚠️ 侷限

CLM 在工具呼叫與 WikiRacing 這類動作組合較開放、不易重複利用快取的任務上準確率仍落後 Jev；速度優勢也高度依賴「動作集合固定、狀態可快取重用」這個前提是否成立。

🎯 實務啟示

如果你的 agent 系統裡有大量「從固定候選集合中選一個」的子任務，例如工具路由、best-of-N 驗證，CLM 這種對比學習打分架構值得評估——尤其是它開源、單卡可跑，且提供與 TypeSafe API 相容的介面，遷移成本可能不高。但在上線前，建議針對自己的任務分佈重新驗證準確率，不要只看 T-Rex、Super Mario 這類與快取重用高度契合的基準。

🔗 來源
- 標題：Contrastive-LM Releases CLM-8B: An Open System One Model That Scores Agent Actions Up to 9× Faster Than Jev
- 作者／機構：Michal Sutter，MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/23/contrastive-lm-releases-clm-8b-an-open-system-one-model-that-scores-agent-actions-up-to-9x-faster-than-jev/

#ContrastiveLearning #AIAgents #OpenSourceAI #LLM #InfoNCE #ModelServing #vLLM #Qwen3 #AgentEvaluation #MachineLearning
