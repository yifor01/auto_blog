---
title: 'Nace AI Open-Sources Drex 1.5: A 9B Decision Model That Scores Options, Not
  Text'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/09/nace-ai-open-sources-drex-1-5-a-9b-decision-model-that-scores-options-not-text/
model: claude-code/sonnet
generated_at: '2026-10-10T20:40:53.341160'
score: 99
---

📌 【Nace.AI 開源】Drex 1.5：9B 決策模型不寫文字，只對選項打分數

TL;DR：Drex 1.5 是開源的 9B 決策模型，單次 forward pass 就能在固定選項中給出機率，可直接替換商用的 Jev。

當所有人都在比拼 LLM 寫文章、寫程式碼有多流暢時，Nace.AI 選擇做一件反直覺的事：讓模型完全不生成文字，只負責在你給定的選項裡打分數。

🤔 **這不是聊天模型，是決策層**

Drex 1.5 讀取一個 state（文字或 JSON）加上多個具名問題，對每個問題回傳固定選項的機率分布。它支援三種問題型態：choice（多選一）、noul（是非題）與 ordinal score（順序分數）。因為不採樣 token，temperature 和 top_p 這類參數完全不適用，模型也只能回答你提供的選項，不會自由發揮。它對外服務 POST /v1/systemone API，與催生這個類別的closed model「Jev」（由 TypeSafe 開發）用的是同一套請求格式，Nace 表示現有的 Jev 客戶端只要改幾個環境變數就能切換過來。

🧩 **架構：蒸餾骨幹 + 獨立指標頭**

Drex 1.5 的 backbone 是 MiMo-V2.6-Distill-Qwen-9B，由 Qwen 3.5 9B 蒸餾而來，共 32 層，採用混合 attention：每 1 層全注意力搭配 3 層 linear attention。模型另外接了一個獨立的 pointer head（head.pt），直接從 backbone 的隱藏狀態為每個選項打分。每個問題只需要對「state + 該問題」跑一次 forward pass；在 llama.cpp 實作中，state 只編碼一次，可在多個問題間共用，節省重複運算。Nace 表示訓練資料來自各項 Decision Index benchmark 的官方訓練切分，評測則只用 held-out 切分。

📊 **排行榜數字：與 Jev、Nimble 幾乎打平**

在公開的 Decision Index 0.3.1（37 項 benchmark，經機率校正）上，Drex 自測拿到 58.08 分，是 10B 參數以下最高分，且與 Jev、Nimble 同在 0.9 分的誤差帶內，在 37 項 benchmark 中贏 Jev 20 項。細項上 Drex 的 Tools 類別最強（75.0），Knowledge 與 Reasoning 最弱（44.6）。在較舊的 Decision Index 0.2.1 上，Drex 拿 58.28 分、Jev 為 57.91 分。在 JevBench 的 231 道公開題目上，Drex 拿 86.2%、Jev 拿 87.0%，兩者在難題子集都是 73.9%。在 8 款 OpenSpiel 遊戲的正面對決中，Drex 以 122 勝 47 和 87 負（勝率 56.8%）贏過 Jev。長文件是 Drex 的強項：若把同樣的請求截斷到 8K tokens，準確率會掉到 76.5% 與 78%，顯示長上下文確實有加成。部署方面，Nace 在 AWS g5.2xlarge（A10G 24GB）上測試 bf16 與 Q8_0，答案一致；Q8_0 的 GGUF 版本在 Apple M5 Pro 的 Metal 與 CPU 上也給出相同結果。官方還提供 Drex agent skill，可接入 Claude Code、Codex、Cursor、OpenCode、Hermes Agent、Gemini CLI 與 GitHub Copilot。

⚠️ **知識類任務是明顯弱點**

Drex 1.5 終究不是通用模型，無法生成文字、程式碼或任何解釋。在知識密集型測試上差距明顯：GPQA Diamond 只有 45.4%，對比 Jev 的 78.6%；MMLU-Pro 為 58.7%，對比 Jev 的 82.7%。由於訓練資料來自 benchmark 的官方訓練切分，模型在熟悉的決策類型上表現較好，換到全新領域的效果仍是未知數。本地部署若要用 Ollama 或 llama.cpp，需要 Nace 自己維護的 fork，而非主線版本。權重採用 RAIL-M 授權並附帶使用限制，商用前務必確認條款。

🎯 **實務啟示**

如果你的 agent 流程裡有大量「從固定選項中選一個」的環節（路由、審核、分類、遊戲決策），Drex 1.5 提供了一個開源且可本機部署的替代方案，API 相容於 Jev，遷移成本低；但知識類推理仍建議搭配一般 LLM 做第二層判斷。

🔗 **來源**
- 標題：Nace AI Open-Sources Drex 1.5: A 9B Decision Model That Scores Options, Not Text
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/09/nace-ai-open-sources-drex-1-5-a-9b-decision-model-that-scores-options-not-text/

#DecisionModel #OpenSource #Qwen #AgentTools #LLM #HuggingFace #OpenRouter #MachineLearning #AIInfrastructure #NaceAI
