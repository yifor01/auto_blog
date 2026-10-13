---
title: Self-Compacting Language Model Agents
source: Apple ML
url: https://machinelearning.apple.com/research/self-compacting-language-agents
model: claude-code/sonnet
generated_at: '2026-10-12T23:46:59.438703'
score: 99
---

📌 【Apple ML 新研究】讓 Agent 自己決定什麼時候該「斷捨離」上下文

TL;DR：SELFCOMPACT 讓模型自行判斷壓縮時機，無需微調就比固定間隔摘要更省 token、效果更好。

🎣 Agent 跑得越久，思維鏈與工具呼叫堆得越高，裡面混雜的過時內容不只佔位置，還會反過來錯誤地「錨定」接下來的生成，直到整個 context window 被撐爆。

🤔 **固定間隔壓縮，壓到一半正在推導的地方**

現有的 agent scaffold 大多用固定間隔壓縮來緩解這個問題：context 累積到某個 token 門檻就觸發摘要。但這種觸發機制完全不理會任務軌跡（trajectory）的結構，可能在推導過程還沒走完、或搜尋還在進行中時，就把中間結果硬生生丟掉。

🧩 **工具加規則：兩者缺一不可**

研究團隊提出 SELFCOMPACT，一個把「何時壓縮、如何壓縮」交給模型自己判斷的 scaffold。它在推論時搭配兩個元件：一是壓縮工具，模型可以主動呼叫它來摘要目前累積的 context；二是一套輕量規則（rubric），明確指出什麼時候該觸發壓縮（某個子任務已解決、軌跡正在收斂），以及什麼時候該壓住不要壓縮（正在進行中的推導、或卡住的時候）。

論文強調兩者缺一不可：只給壓縮工具，不同的開源模型使用狀況參差不齊，常常在沒幫助的時機呼叫、或根本不呼叫；只給規則，模型知道該怎麼判斷卻沒有動手壓縮的能力。把工具與規則搭配在一起，就能在完全不需要微調、不需要額外監督訊號的情況下，讓模型做出有效的自適應壓縮。

📊 **在 6 個 benchmark、7 個模型上驗證**

研究團隊在六個 benchmark（涵蓋競賽數學與 agentic search）、七個模型上做了實證評估。結果顯示 SELFCOMPACT 在效果上達到甚至超越固定間隔摘要，但 token 成本只是一小部分：相較於完全不做摘要的基準，在數學任務上最多提升 18.1 分，在 agentic search 任務上提升 5 到 9 分，同時每題成本降低 30% 到 70%。

💡 **模型其實不太清楚自己的 context「壞掉」了**

研究團隊指出一個「元認知缺口」（meta-cognitive gap）：如果不給任何提示，模型本身並不能穩定判斷自己的 context 什麼時候開始失效，但補上一套輕量規則就能補足這個缺口。這重新定義了「何時該壓縮」這件事——它可以是 scaffold 層面就能提供的能力，不必靠訓練才能具備。

🎯 **實務啟示**

對正在打造長時間運作的 agent scaffold（例如 coding agent、deep research agent）的團隊來說，SELFCOMPACT 指出壓縮邏輯值得放進 scaffold 的規則或 prompt 層，而不一定要靠昂貴的微調解決。如果目前的 agent 系統還在用單純的固定間隔摘要，這是一個值得嘗試的替換方向。

🔗 **來源**
- 標題：Self-Compacting Language Model Agents
- 作者／機構：Tianjian Li, Jingyu Zhang, William Jurayj, Xi Wang, Chuanyang Jin, Mehrdad Farajtabar, Eric Nalisnick, Daniel Khashabi（多位作者來自 Johns Hopkins University，發表於 Apple ML，NeurIPS 2026）
- 連結：https://machinelearning.apple.com/research/self-compacting-language-agents

#LLMAgents #ContextWindow #PromptEngineering #AppleML #NeurIPS2026 #AgenticAI #Summarization #InferenceTime #ToolUse #MetaCognition
