---
title: 'Import AI 469: Science AI; RSI simulator; and Zuck’s technological pessimism'
source: Import AI
url: https://jack-clark.net/2026/08/17/import-ai-469-science-ai-rsi-simulator-and-zucks-technological-pessimism/
model: claude-code/sonnet
generated_at: '2026-08-18T06:30:51.409402'
score: 96
---

📌 AI 能無師自通嗎？70 款隱藏規則遊戲揭曉答案

TL;DR：DiG-bench 用 70 款規則不公開的遊戲測試 AI 的探索與直覺能力，頂尖模型在最難關卡只有 20% 過關率。

人類玩家在這些遊戲裡都能做到 100% 破關，但目前最強的前沿模型，在最難的關卡也只拿下 20% 的成功率。這個落差，揭露了「創造力」這件事在 AI 系統身上，到底卡在哪一關。

🤔 規則不告訴你，你要自己摸索出來

DiG-bench（Discovery in Games）是一套新的 benchmark，由 Thinking About Thinking、牛津大學、普林斯頓大學、阿卜杜拉國王科技大學、瑞士 AI Lab、Inria 與 MIT 的研究者共同打造，作者之一是知名 AI 研究者 Jürgen Schmidhuber。每一款遊戲都是一個獨立的迷你世界，規則與目標同時對玩家隱藏，必須透過互動去挖掘。這與視覺化的 ARC 測驗類似，但 DiG-bench 完全以純文字呈現，遊戲長度也大多控制在能夠塞進目前前沿模型 context window 的範圍內。

這些遊戲全部由人類專家手工打造，且大部分關卡刻意保持私有，避免被拿去訓練 AI 模型；每款遊戲都至少有一位人類玩家破過關，但玩家普遍反映難度不低。遊戲另外提供一個「實驗模式」，讓玩家可以在較寬鬆的步數限制下自由試探環境規則。

🧩 七個難度分級，21 款關卡公開

Benchmark 分成七個難度層級（Tier 1 最簡單，Tier 7 最難），目前公開 21 款遊戲，其餘保留私有。多數遊戲有多個關卡，每一步可採取的行動數量從 2 到 34 種不等。

📊 只有兩個模型踏進了 Tier 7

在整體排行中，Opus 5 與搭配 Claude Code 的 Fable 5 是表現最好的模型，GPT-5.5 緊隨其後。目前只有 Opus 5 與 Fable 5 能在 Tier 7 拿下分數（成功率 0.2，也就是 20%）；Opus 5、GPT-5.5 與 Kimi K3 在配有 Claude Code 這類工具的情況下，能拿下部分 Tier 6 關卡；GLM-5.2 與 Gemini 3.1 Pro 則止步於 Tier 4。作者 Jack Clark 認為，以目前的進展速度推估，AI 系統要在 DiG-bench 上追平人類水準，大概要到 2027 年年中，而那個時間點，遞迴自我改進（recursive self-improvement）相關的討論很可能會真正升溫。

🧩 用一款「文明模擬遊戲」體感遞迴自我改進

同一期電子報也介紹了 Paradigm Research 開發的瀏覽器小遊戲 RSI Simulator，概念類似「給奇點玩的 Cookie Clicker」。玩家在遊戲中扮演經營一間打造 AI 系統的公司，需要在研究人力與算力之間做取捨、決定何時該授權資料等等，藉此培養對「AI 系統一旦具備遞迴自我改進能力後，各種研發要素如何互相牽動」的直覺。Jack Clark 形容這款遊戲不好玩（很難），但這正好呼應了前沿 AI 研發本身的難度。

🧩 一個 27B 模型，監督頂尖模型做科學研究

電子報另外介紹了 AI 新創公司 Inherent 發表的研究：他們訓練了一個名為 Faraday 的 AI 科學家模型，在大型專有前沿模型之上擔任監督角色，提升其做科研的效果。團隊建立了名為 Replica 的資料集，收錄 1990 年至 2026 年間發表的 100 篇機器學習與 AI-for-science 論文，並把其中的關鍵圖表或結果抽掉，轉換成 310 個「複現任務」，讓 AI 系統自主做實驗把缺漏的部分補回來。訓練上，研究團隊用 Claude Opus 4.7 依照 meta-rubric 產生任務專屬的評分標準，再用一個以 Codex 為基礎的 Judge 模型給出整體獎勵與逐輪的信用分配權重，藉此透過改良版的 GRPO 訓練 Faraday。

Faraday 本體是一個 27B 模型，以 OpenAI Codex 作為底層工具、在 Qwen-3.6-27B 之上做後訓練。結果顯示，搭配 Codex 的 Faraday 在部分複現任務上贏過標準的 Opus 4.8 與 GPT-5.5，依照論文自訂的評分標準，在分佈內（in-distribution）的機器學習任務上贏過 73%，在保留（held-out）的 AI-for-science 任務上贏過 60%。

💡 三則消息背後的同一條主線

這三則消息合看，指向的是同一個問題：如何量化 AI 系統「自主發現有用但未被寫下來的資訊」的能力。DiG-bench 的介紹把這件事形容為創造力的前提；Faraday 那篇則指出，AI 系統在這件事上做得越好，就越有理由相信 AI 系統即將具備打造自己的能力。這也是 Jack Clark 認為這類測驗值得持續追蹤的核心原因。

🎯 實務啟示

如果你的工作涉及評估模型的 agentic 或探索能力，DiG-bench 的公開題目與線上遊玩介面（digbench.ai）值得拿來當作壓力測試的補充材料，尤其是它刻意設計成「目前模型解不動」的難度，能幫助你分辨模型是真的具備探索直覺，還是只是背下了常見的解題套路。

🔗 來源
- 標題：Import AI 469: Science AI; RSI simulator; and Zuck's technological pessimism
- 作者／機構：Jack Clark
- 連結：https://jack-clark.net/2026/08/17/import-ai-469-science-ai-rsi-simulator-and-zucks-technological-pessimism/

#AI #Benchmark #DiGbench #RecursiveSelfImprovement #AIResearch #LLM #AgenticAI #ReinforcementLearning #AIScientist #MachineLearning
