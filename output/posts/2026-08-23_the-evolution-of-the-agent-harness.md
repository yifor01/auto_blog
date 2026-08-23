---
title: The Evolution of the Agent Harness
source: Latent Space
url: https://www.latent.space/p/attention-interface
model: claude-code/sonnet
generated_at: '2026-08-23T06:15:48.470767'
score: 78
---

📌 模型追上腳手架的那一刻：Agent Harness 為什麼突然「能用」了

TL;DR：2025年底agent突然變好用，關鍵不是模型單獨躍進，而是模型與harness兩條曲線終於交會。

2025 年聖誕節前後，不少 AI 工程師突然發現手上的 agent「能用了」。連參與發明 Transformer 的 Lukasz Kaiser 都說不清楚確切原因：「harness 變了，加上一點 post-training 的調整，然後新的預訓練模型又出來了……感覺是一次很大的躍進，但很難精確指出是什麼造成的。」

🤔 **Agent Harness 到底是什麼**

Latent Space 這篇文章給出的定義是：agent harness 是模型權重以外，讓 agent 真正能運作的一切——環境、工具、context、guardrails。2022 年 11 月的 ChatGPT 只有下一個 token 預測與一點 RLHF，沒有工具、沒有搜尋、沒有推理，是一個「泡在缸裡的大腦」。Harness 就是讓模型脫離這個缸，跟真實數位資訊空間互動的方式：context 讓它感知、工具讓它行動、記憶與 compaction 讓它保存資訊、permission 與 guardrails 讓它守住邊界。

🧩 **兩條曲線：harness 對模型的要求，vs 模型實際能交付的能力**

文章把 agent 的演進拆成幾個階段，兩條曲線之間的落差，就是 agent 有效性的缺口。

**ReAct，紙上的 harness（2022年10月）**：ReAct 是一種讓模型透過 prompting 進行推理的技巧，定義了「推理→行動→觀察→重複」的 agent loop，但這個迴圈只存在於 prompt 層面，不算真正的模型能力。同年 2 月 Meta 的 Toolformer 已經暗示工具使用其實可以被訓練進模型裡，只是當時還只是個構想。此時兩條曲線都接近零，落差很小。

**AutoGPT / BabyAGI，過早的自主性（2023年春）**：harness 曲線一口氣衝到模型能力曲線前面，把模型當成「自主員工」，但當時的模型還只是脆弱的 next-token 預測器。文章用一個簡單算式說明代價：如果每一步的可靠度是 95%，跑一個 20 步的任務，平均成功率只剩下約 36%。這是落差最大的階段。

**Cursor / Copilot，退回人類在迴圈中（2023-2024年）**：第一批 AI IDE 意識到把太多自主權交給模型的失敗模式，於是把 harness 曲線壓回模型曲線之下——不是把迴圈直接交給模型，而是交給人類，由人類主導、模型加速。早期 Devin 嘗試把自主權交還給模型，Answer.AI 團隊的測試顯示成功率只有約 15%，證明退回人類在迴圈中並非保守，而是當時正確的選擇。2024 年底 o1 這個第一個推理模型出現後，落差第一次反轉，模型能力開始出現盈餘。

**Claude Code，兩條曲線交會（2025年2月）**：2024 年底的反轉創造了一個機會——如果模型已經領先 harness，那麗繼續踩煞車的 harness 就是在浪費能力。Claude Code 放棄 IDE、改用終端機，給模型 bash 與檔案讀寫權限，用 permission rules 取代每次變更都要人工核准。這次 harness 把迴圈重新交還給模型，而模型這次接得住。Claude Code 在六個月內成長到約 10 億美元 ARR。

📊 **harness 差多少，實測數字說話**

Harness-Bench 讓同一個模型跑同樣的 106 個任務、換不同 harness，分數落在 52.4 到 76.2 之間，模型完全沒變，落差卻高達 23.8 分——等於 agent 的一半實力來自 harness。OpenAI 在 ARC-AGI-3 上也觀察到類似結果：只調整 retained reasoning 與 compaction，GPT-5.6 Sol 的分數就從 13.3% 跳到 38.3%。這背後是 RL 已經搬進 harness 內部——OpenAI codex-1 在 2025 年 5 月的發布公告就寫著它是用真實世界的程式碼任務、在多種環境中透過強化學習訓練出來的。

💡 **模型吸收 harness、工程師刪掉被吸收的部分**

當模型在 harness 環境裡被訓練，它開始把 harness 的能力吸收進權重裡，例如學會根據自己的 context window 主動 compaction。一旦能力被吸收，harness 就能卸下對應的鷹架——這是「靠減法生產」。Anthropic 的 Thariq Shihipar 提到團隊最近刪掉了 Claude Code 系統提示詞的 80%。

⚠️ **這是一篇綜合觀點文章，非單一實證研究**

文章引用了多個外部基準（Harness-Bench、ARC-AGI-3）與時間線事件來支撐論點，但整體屬於作者對趨勢的綜合解讀與心智模型整理，讀者應把各項數字視為引用自對應來源，而非本文自行產出的實驗結果。

🎯 **實務啟示**

在設計自己的 agent 系統時，值得對照這個框架問自己：現在給模型的自主權，是踩在「harness 曲線」之上還是之下？如果模型能力已經領先，繼續要求每一步人工核准可能是在浪費能力；反過來，如果貿然放權，也可能重演 AutoGPT 式的複合錯誤。同時要有心理準備，今天手工打造的 harness 邏輯，很可能在下一代模型裡被直接吸收、然後被你自己刪掉。

🔗 **來源**
- 標題：The Evolution of the Agent Harness
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/attention-interface

#AgentHarness #ClaudeCode #AIAgents #LLM #AgenticAI #ReAct #ReinforcementLearning #AIEngineering #ToolUse #FrontierAI
