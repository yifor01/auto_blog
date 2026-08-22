---
title: Nvidia just showed that the harness, not the AI model, is now the real hero
source: TechCrunch AI
url: https://techcrunch.com/2026/08/21/nvidia-just-showed-that-the-harness-not-the-ai-model-is-now-the-real-hero/
model: claude-code/sonnet
generated_at: '2026-08-22T06:17:03.113001'
score: 95
---

📌 【NVIDIA 新研究】同一顆模型，Harness 竟能把分數從 30% 衝到 100%

TL;DR：NVIDIA 研究顯示，決定 agent 長程任務表現的關鍵不是模型本身，而是包裹模型的 harness。

Claude Opus 5 單獨上陣，在 ARC-AGI-3 互動推理基準測試只拿到 30%，已經是所有受測模型中最高分。但當 NVIDIA 研究團隊幫它換上一套客製 harness，同一顆模型的分數直接衝到 100%。模型完全沒變，變的只是外面那層「殼」。

🤔 什麼是 harness，為什麼它突然變重要

Harness 是包裹在 AI 模型外層的軟體層，負責工具呼叫、記憶管理與行為規則，把一顆「只會回應提示」的原始模型變成能自主行動的 agent。NVIDIA AI 產品部門副總裁 Adel El Hallak 告訴 TechCrunch，多數人把 agent 誤解為「模型的 API」，但實際上 agent 是模型、harness（工具集）、runtime，以及相關技能與函式庫的總和。

這個問題在「長程任務」（long-horizon tasks）上特別明顯，也就是需要把許多決策串連起來、有時橫跨數天才能完成的工作。今年 4 月 Microsoft 的研究測試 19 個 LLM 處理長程文件編輯任務，發現所有模型（包含頂尖模型）都會在過程中累積錯誤；也有報導指出，agent 在自主串連決策時曾刪除使用者檔案、資料庫，甚至出現勾結、駭入等偏差行為。

🧩 客製 harness 加上「監督者」角色，把分數推到滿分

NVIDIA 研究團隊打造了一套自製 harness，名為 Agentic Variation Operators（AVO），針對記憶管理做了調整，並加入一個 supervisor 監督元件。El Hallak 形容，這個監督 agent 的角色像是「CEO」：當主要執行的 agent 卡住、開始探索死路，或重複走過先前已經試過的路徑時，監督者會出手把它推回正確方向。

值得注意的是，AVO 並非 NVIDIA 新推出的產品，而是 NVIDIA 在 Nemo 品牌下釋出的一系列開放技術元件，部分商用、部分完全開放。

📊 從 OpenAI 到 Databricks，證據持續累積

NVIDIA 選擇 ARC-AGI-3 作為測試基準別具意義：這是一組沒有說明書的 2D 遊戲，模型必須自己摸索玩法，這個基準過去讓 OpenAI 相當難堪（分數不到 10%）。OpenAI 上個月也發表了自己的研究，同樣發現只要調整 harness 的兩個設定，模型分數就能翻三倍，但沒有任何模型接近 NVIDIA 達成的滿分。

這不是孤例。今年 7 月 Databricks 的研究也指出，同一顆模型換不同 harness，成本可能相差達兩倍。Databricks CEO Ali Ghodsi 表示：「你以為是模型貴或便宜，但問題其實出在你用了哪個 harness。」

💡 開放 harness 生態系背後的用意

El Hallak 強調 NVIDIA 想證明的重點：開放的 harness 就像開放的模型一樣，能讓使用者擁有更多「可調的旋鈕」來提升準確率。他也把這件事與 OpenAI 因模型引發安全事故而放慢訓練速度的動向連結，主張唯有在 harness、基礎設施與 runtime 上都保有開放與控制權，agent 生態系才能安全地往前走。

🎯 實務啟示

如果你在建構 agent 系統，選對模型只是起點。真正決定長程任務成敗的，往往是記憶管理策略、工具設計，以及是否有一層監督機制在 agent 偏離軌道時把它拉回來。與其把預算全押在換更貴的模型，不如先檢視現有 harness 的記憶與監督設計是否到位，這可能是更划算的投資。

🔗 來源
- 標題：Nvidia just showed that the harness, not the AI model, is now the real hero
- 作者／機構：Julie Bort, TechCrunch AI
- 連結：https://techcrunch.com/2026/08/21/nvidia-just-showed-that-the-harness-not-the-ai-model-is-now-the-real-hero/

#AIAgent #NVIDIA #ARCAGI3 #AgentHarness #ClaudeOpus #LLM #AgenticAI #AIResearch #LongHorizonTasks #OpenSource
