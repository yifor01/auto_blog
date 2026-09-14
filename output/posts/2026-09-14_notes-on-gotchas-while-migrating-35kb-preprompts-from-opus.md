---
title: Notes on gotchas while migrating 35kb preprompts from Opus to self-hosted Ollama
source: Hacker News
url: https://patrickmccanna.net/notes-on-migrating-large-prompts-away-from-anthropic-openai-to-self-hosted-llms/
model: claude-code/sonnet
generated_at: '2026-09-14T21:16:29.154157'
score: 60
---

📌 把35KB的prompt從Opus搬到自架Ollama，會發生什麼事

TL;DR：作者實測把大型preprompt搬到自架LLM，發現上下文窗口才是真正的天花板。

如果你曾經把一份在雲端API上跑得順暢的prompt，原封不動丟進自架的open weight模型，卻看著agent陷入無限迴圈重複讀檔、重寫已完成的工作，這篇筆記可能會讓你會心一笑，也可能讓你倒吸一口氣。

🤔 為什麼要自架

作者的出發點是資料主權的疑慮：他認為agent session的逐字記錄，其實是使用者解題思路與直覺的濃縮，價值可能高於一般個資本身。文章提到近期一起與Navier-Stokes解法有關的爭議事件（連結至The Verge報導），並以此質疑前沿供應商是否可能在未充分揭露的情況下，利用使用者的推理過程訓練模型。基於這個顧慮，作者認為唯一能驗證隱私邊界的做法，是把推論搬到自己掌控的硬體上執行；不過這部分屬於作者個人立場與推測，並非文章證實的事實。

🧩 35KB的prompt，在自架環境裡直接「爆表」

真正有價值的是接下來的實測筆記。作者的硬體是一臺配備128GB記憶體的AMD Ryzen AI MAX+ 395，其中32GB分給host OS，其餘全部用於推論，透過Ollama跑本地模型。他觀察到：

- 在前沿API上跑得乾淨俐落的prompt，搬到自架模型上直接「散架」：agent在重複的tool call之間空轉，反覆重讀已經讀過的檔案，甚至重寫已完成的工作。
- 問題根源不是模型體積太小，而是自架系統的上下文窗口天生較小。作者的系統上限是65k tokens，一份35KB的prompt本身就先吃掉整體上下文窗口的14%。
- 隨著prompt疊加session歷史，上下文很快被填滿，模型開始對自己剛下的指令「重新懷疑」，觸發不必要的tool call與重複讀檔，有時甚至在給出第一個回應之前，上下文就已經飽和。

作者用一個比喻形容這種狀態：帶著大型preprompt在小上下文窗口裡運作，就像每90秒就重新投胎一次的人，只能執行最後一道指令，完全不記得前面15個要求。

⚠️ 這篇筆記的侷限

文章也夾雜大量對前沿供應商動機與網路安全策略的批評與推測，例如質疑OpenAI、Anthropic的安全防護是「表演」、抱怨safety filter阻礙防禦端的漏洞研究等，這些屬於作者個人觀點與立場陳述，並未附上可查核的證據，讀者宜與後段的技術實測分開看待。此外，文章提到嘗試使用「abliterated」（移除安全對齊限制）的27B開放權重模型以避開資安相關的拒答，這同樣是作者自述的實驗方向，其可行性與風險文章本身尚未給出結論。

🎯 對工程師的實務啟示

如果你打算把大型preprompt從雲端API搬到自架的小上下文模型，先假設「一模一樣搬過去」大機率不可行。作者接下來提出的方向是「Single Objective Prompting（單一目標提示）」，也就是把大而全的preprompt拆解成聚焦單一任務的精簡指令，避免在有限的上下文窗口裡塞入模型根本消化不了的資訊量。這對任何在有限VRAM／記憶體環境下跑agent的人，都是值得優先驗證的假設。

🔗 來源
- 標題：Notes on gotchas while migrating 35kb preprompts from Opus to self-hosted Ollama
- 作者／機構：0o_MrPatrick_o0
- 連結：https://patrickmccanna.net/notes-on-migrating-large-prompts-away-from-anthropic-openai-to-self-hosted-llms/

#LLM #Ollama #SelfHosted #PromptEngineering #OpenWeights #AIInfrastructure #ContextWindow #LocalLLM #AIAgents #DataPrivacy
