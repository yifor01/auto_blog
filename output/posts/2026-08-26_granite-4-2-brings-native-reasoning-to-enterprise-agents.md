---
title: Granite 4.2 brings native reasoning to enterprise agents
source: IBM Research
url: https://research.ibm.com/blog/introducing-granite-4-2?utm_medium=rss&utm_source=rss
model: claude-code/sonnet
generated_at: '2026-08-26T06:26:54.553236'
score: 94
---

📌 IBM Granite 4.2：企業級 Agent 模型內建「先想再做」的推理能力

TL;DR：Granite 4.2 加入原生 reasoning 與工具呼叫能力，鎖定企業多步驟 agentic workflow。

當 LLM 從「回答問題」進化到「執行任務」，一個模型在動手前是否能先想清楚，決定了企業敢不敢把它接進生產流程。IBM 這次把賭注押在「thinking」這件事上。

🤔 企業任務不是一問一答

企業場景裡的任務往往模糊、涉及多個步驟：模型必須理解不明確的指令、擷取正確資訊、選對工具、依正確順序執行,還要驗證結果是否正確。IBM 認為，reasoning 能力正是讓模型在這條路徑上走得更穩的關鍵，它讓 Granite 4.2 在呼叫工具前先評估該用哪個應用、以什麼順序執行，而非盲目執行。基於 Granite 4.2 打造的軟體工程 agent，可以在程式碼庫中導覽、處理多步驟開發任務，並在終端機環境中運作。

🧩 從 SFT 到多階段強化學習

Granite 4.2 提供 3B、8B、30B 三種參數規模，採用 dense 架構，支援雲端、地端與邊緣部署，並以 Apache 2.0 授權釋出，企業可自由下載、fine-tuning 並投入生產,不受授權限制。

這一代模型建立在 Granite 4.0 基礎模型之上，訓練流程從監督式微調（supervised fine-tuning）開始，接著進入多階段強化學習（RL）。第一階段稱為「foundational RL」，套用於所有 Granite 4.2 模型，強化數學、科學、程式撰寫、推理與工具呼叫能力，結合可驗證獎勵（verifiable rewards）與 reward-model 評估，同時學習準確性與更高層次的品質信號。8B 與 30B 模型接著會再進入一個專屬的「agentic RL」階段,聚焦軟體工程、終端機程式撰寫與搜尋導向的工作流程，再搭配 RLHF（reinforcement learning from human feedback）對齊。

另外兩項技術也影響了這代模型的程式撰寫與推理表現：模型使用 IBM 自家 CodeAlchemy pipeline 產生的 1 兆 token 合成程式碼進行訓練；同時導入一個稱為 mid-training 的中介訓練步驟，據稱能進一步釋放模型的推理能力。模型也加入了 speculative decoding 層，能在服務更多使用者的同時加快文字輸出速度，藉此改善推理體驗並降低企業的維運成本。IBM 團隊也與 Hirundo 合作，運用其 machine unlearning 技術，在不需要完整重新訓練模型的情況下，針對性減少訓練後模型產生不良輸出的情形。

📊 470M 參數的邊緣語音模型

同一波發布中，IBM 也推出兩款語音模型：Granite Speech 5.0 Turbo CTC 與 5.0 Turbo CTC NC。相較於前一代 4.1 模型，這是一次結構上的跳躍，因此團隊將其獨立命名。兩款模型僅 470 百萬參數，是 Granite 家族中最小的模型之一，適合部署在筆電、手機等邊緣裝置。它們採用 CTC（connectionist temporal classification）技術，能有效率地把音訊對應到文字，並直接從原始音訊與文字中學習，擅長串流音訊、快速轉錄。與過去的 Granite Speech 模型不同，這兩款模型沒有 LLM backbone，因此模型體積極小，同時在 ASR（自動語音辨識）任務上維持效率。

IBM 研究團隊指出，目前 Hugging Face Open ASR leaderboard 上速度最快的模型處理吞吐量（RTFx）約在 6,000 左右，而在他們的測試中，Granite Speech 5.0 Turbo CTC 在單張 H200 GPU 上達到約 12,600，能在一秒內轉錄三小時的語音紀錄，適合即時字幕、語音應用開發，或大規模的客服中心語音分析。團隊同時釋出一個以受限使用資料訓練的非商用（NC）版本。

💡 進化而非革命，但方向務實

從技術路線來看，Granite 4.2 是延續 Granite 4.0 基礎、透過訓練流程優化帶來的漸進式升級，而非架構上的重新設計。但對企業使用者而言，這種務實的疊代反而更有價值：三種尺寸讓小模型負責高吞吐量的日常 agentic 任務、大模型保留給複雜推理與程式撰寫，Apache 2.0 授權也降低了導入門檻。

🎯 實務啟示

若團隊正在評估 agent 導向的企業 LLM，Granite 4.2 的分層設計（3B/8B/30B）與 Apache 2.0 授權，值得納入 fine-tuning 或私有部署的候選清單；語音團隊則可關注 Granite Speech 5.0 Turbo CTC 在即時轉錄與大規模語音分析上的效率優勢。模型已可於 Hugging Face、Ollama 與 GitHub 下載。

🔗 來源
- 標題：Granite 4.2 brings native reasoning to enterprise agents
- 作者／機構：IBM（IBM Research）
- 連結：https://research.ibm.com/blog/introducing-granite-4-2?utm_medium=rss&utm_source=rss

#IBM #GraniteLLM #EnterpriseAI #AIAgents #ReasoningModels #ToolCalling #OpenSourceLLM #SpeechAI #ReinforcementLearning #ASR
