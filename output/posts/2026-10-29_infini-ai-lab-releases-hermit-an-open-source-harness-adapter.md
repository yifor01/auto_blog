---
title: Infini-AI-Lab Releases Hermit, an Open-Source Harness Adapter Framework for
  AI Agents
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/29/infini-ai-lab-hermit-harness-adapter-framework/
model: claude-code/sonnet
generated_at: '2026-10-29T21:57:12.931638'
score: 108
---

📌 不微調模型,改練「外掛的 Harness」:Hermit 開源框架

TL;DR:Hermit 讓 Codex、Claude Code 等 agent 的模型與 harness 都凍結不動,只訓練一個外部適配層。

微調模型要資料、要算力,改 harness 原始碼又容易破壞原本調校好的元件互動——如果兩條路都不好走,Infini-AI-Lab 給出的第三條路是:讓模型和 harness 原封不動,只訓練一個掛在外面的「適配層」。

🤔 Harness Adapter 是什麼

Infini-AI-Lab 於 2026 年 10 月 25 日發布 Hermit v0.1.0,由 CMU 博士後研究員 Haizhong Zheng 於 10 月 27 日在 X 上公布。Hermit 的核心概念是 harness adapter:一種可訓練的外部 harness,運作方式像是一個「內建訓練能力的插件」。LoRA 之類的 model adapter 用來適配模型本身,而 harness adapter 適配的是既有的 agent——它可以包含指令、skill、記憶、工具、可執行程式碼,甚至 agent 之間的協調邏輯,大到整個 repository 都算。每個 adapter 都有規格,說明哪些部分可學習、更新如何被檢查,而基礎模型與 harness 本身始終不變。

Infini-AI-Lab 給出三個設計理由:許多 harness 本身是閉源的;即便是開源 harness,直接修改也容易破壞原本細調好的元件互動;而一個學習出來的 adapter 可以在相容的模型與 harness 之間搬動。

🧩 RL 式的訓練迴圈,每個版本都進 git tree

Hermit 用的是 RL 風格的訓練迴圈:Trainer 讓目前版本的 adapter 帶著 acting agent 跑一批任務,Judge 替輸出打分,Evolver 讀取軌跡與回饋後提出新版 adapter,Trainer 再對照規格檢查並將其提交為下一版本。每一版 adapter 都存在 git tree 裡,可以檢視、回滾或直接部署任何版本。需要沙箱執行的 Learner 程式,要求 Linux 搭配 bubblewrap。

目前已內建 5 種演化方法:GEPA、SkillOpt、MetaWorld Model(MWM)、Harness² 與 Continual Harness;ACE 與 ReHarness 則列為即將推出。使用者也可以自行撰寫 Evolver。

📊 三個 benchmark,MWM 與 Harness² 的表現最搶眼

以下數字皆為 Infini-AI-Lab 自述,且全部以 GLM 5.3 Flash 作為 acting model:

- OfficeQA(172 題美國財政部公報相關問題,以 exact match 評分):GEPA 與 SkillOpt 在 50 題上訓練後凍結測試;Continual Harness 與 Harness² 則在串流測試集一次的過程中持續學習。Harness² 相較參考基準提升 7.6 分,95% 信賴區間為 +1.7 到 +13.4。
- CL-Bench(database、poker,取自 Continual Learning Bench 論文的有狀態環境):在 database exploration 任務上,MWM 達到 0.795 準確率,相較 in-context baseline 的 0.580;在 exploitable poker 上,MWM 每手贏 3.08 個大盲注,優於 in-context learning 的 2.51。
- ServeLearnBench(624 筆零售客服請求,政策隱藏且會變動):MWM 在隱藏政策測試中拿到 45.3 分,leaderboard 上最佳的學習方法 Continual Harness 拿 28.7 分,而直接拿到政策的 oracle 則是 89.2 分。

💡 一套工具串起訓練到部署

安裝可透過 pip install hermit-harness,或直接 clone repo 取得範例。CLI 涵蓋 check、train、eval、deploy、convert 五個指令,模型以 <backend>/<model id> 格式指定,支援 Fireworks、OpenAI、Anthropic、DeepSeek、vLLM、SGLang、Ollama 等後端。hermit deploy 會寫出可供 Codex、Claude Code 或 Pi 使用的 workspace,hermit convert 則能把訓練好的 adapter 匯出成 Codex、Claude Code、Pi 或 Hermes 的原生插件。官方範例中,一個訓練完成的 Lean 協作 adapter 可以協調 5 個 Codex agent 共同證明同一條定理。

⚠️ 數字皆取自專案範例 README

上述 benchmark 結果來自 repo 內各範例的 README,為專案方自行回報的數據,尚未見第三方獨立覆核。

🎯 實務啟示

如果團隊已經在用 Codex 或 Claude Code 這類現成 agent,但想讓它適應特定任務(例如固定的客服政策、特定程式碼庫慣例),Hermit 提供了一個不需微調底層模型、也不需要 fork harness 原始碼的路徑,且每個版本都可追溯、可回滾,適合想在生產環境中謹慎迭代 agent 行為的場景。

🔗 來源
- 標題:Infini-AI-Lab Releases Hermit, an Open-Source Harness Adapter Framework for AI Agents
- 作者/機構:Asif Razzaq,MarkTechPost
- 連結:https://www.marktechpost.com/2026/10/29/infini-ai-lab-hermit-harness-adapter-framework/

#AIAgents #OpenSource #HarnessAdapter #Hermit #ReinforcementLearning #CodingAgents #ClaudeCode #Codex #AgentFramework #MachineLearning
