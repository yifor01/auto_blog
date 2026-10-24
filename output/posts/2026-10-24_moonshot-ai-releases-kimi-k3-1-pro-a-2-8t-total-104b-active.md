---
title: 'Moonshot AI Releases Kimi K3.1 Pro: A 2.8T Total/104B Active Params (MoE)
  Model with 1M Context'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/23/moonshot-ai-kimi-k3-1-pro-open-weight-model/
model: claude-code/sonnet
generated_at: '2026-10-24T19:34:39.874050'
score: 102
---

📌 Moonshot AI Kimi K3.1 Pro：3T 級模型,權重 11 月才開放

TL;DR：Kimi K3.1 Pro 號稱逼近頂尖 proprietary 模型,API 已上線,但「開放權重」要等到 11 月。

一個標榜「open-weight」的模型,權重卻還沒放出來——這正是 Kimi K3.1 Pro 眼下的狀態,官方說法是預計 2026 年 11 月釋出。

🤔 K3.1 系列的第一棒

Kimi K3.1 Pro 是 Moonshot AI K3.1 系列首款模型,官方標示為 2.8T 總參數、104B active 參數的 MoE 模型,context window 達到 1M tokens。Moonshot 團隊把它拿來對標最強的 proprietary 模型,涵蓋 coding、agentic 與 knowledge 類 benchmark,對開發者而言的吸引力是比 K3 更便宜的 API 定價。

🧩 在 K3 基礎上,砸更多後訓練運算量做聯合 RL

K3.1 Pro 是 Kimi K3 的後訓練版本,用了遠大於 K3 的 post-training 運算量,跨數百個下游領域進行聯合強化學習。為此,Moonshot 團隊最佳化了 RL framework、長文本推理、沙箱基礎設施與 rollout 排程。基礎的 K3 架構採用 Kimi Delta Attention（KDA）與 Attention Residuals（AttnRes）,透過 Stable LatentMoE 框架,每次從 896 個專家中啟用 16 個。API 可接受文字、圖片與影片輸入。此外 Moonshot 也同步推出 Kimi K3.1 Pro Highspeed,官方部落格稱其速度為一般版本的 2 到 3 倍。

📊 為了安全移除 cyber 資料,分數因此下降

以下數字皆由 Moonshot 自報,多在 max reasoning effort、主要搭配 Claude Code harness 的設定下測得。針對開放權重版本,Moonshot 在 mid-training 與 RL 階段移除了與 cyber 相關的資料。在內部的 xdev-bench-hard 測試上,未經過濾的 checkpoint 在 pass@3 下解出 90.5%,而正式發行的 K3.1 Pro 只解出 81.0%。Moonshot 表示,在 offensive cyber 類任務上,K3.1 Pro 仍落後於 frontier 等級的 proprietary 模型。

部署與定價：模型目前已上線 Kimi.ai、Kimi Work、Kimi Code 以及 Kimi API,API ID 為 `kimi-k3.1-pro` 與 `kimi-k3.1-pro-highspeed`,端點相容 OpenAI 格式。K3.1 Pro 定價為輸入每百萬 tokens 2 美元、輸出 10 美元,cache 命中降到 0.2 美元;Highspeed 版本則是輸入 4 美元、輸出 20 美元。相較之下,K3 原本的定價是輸入 3 美元、輸出 15 美元。

⚠️ 權重未到位,評估只能先靠 API

所有 benchmark 數字都是 Moonshot 自報,尚未有第三方驗證;真正的「開放權重」要等到 2026 年 11 月,現階段只能透過 API 使用,無法自建部署;移除 cyber 相關訓練資料也意味著模型在特定任務類型上的能力被刻意收斂。

🎯 實務啟示

如果你的應用需要超長 context（1M tokens）加上多模態輸入與 agentic/coding 能力,現在可以先用 API 評估效果與定價是否划算,等 11 月權重真正釋出後再評估自建部署的可行性;定價比 K3 更低,值得先納入 agent routing 的候選清單觀察。

🔗 來源
- 標題：Moonshot AI Releases Kimi K3.1 Pro: A 2.8T Total/104B Active Params (MoE) Model with 1M Context
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/10/23/moonshot-ai-kimi-k3-1-pro-open-weight-model/

#MoonshotAI #KimiK3 #MoE #LLM #LongContext #OpenWeightModel #AgenticAI #CodingAssistant #AIInfrastructure #ReinforcementLearning
