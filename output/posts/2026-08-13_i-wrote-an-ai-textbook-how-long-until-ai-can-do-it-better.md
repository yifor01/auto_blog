---
title: I wrote an AI textbook — how long until AI can do it better?
source: Interconnects
url: https://www.interconnects.ai/p/i-wrote-an-ai-textbook-how-long-until
model: claude-code/sonnet
generated_at: '2026-08-13T07:36:05.709769'
score: 86
---

📌 寫完一本 AI 教科書才發現：LLM 的長篇寫作沒有真的變強

TL;DR：模型在程式與數學上已近超人類，但整理知識、寫出一整章連貫技術文字仍卡關。

程式與數學能力這幾年從普通進步到接近超人類，但如果你請同一個模型寫完一整章教科書，你會發現它還是那個東拼西湊、邏輯斷裂的老樣子——這正是 Nathan Lambert 寫完一本後訓練（post-training）教科書後最意外的觀察。

🤔 **一本教科書，兩年的落差**

Lambert 剛完成《Reinforcement Learning from Human Feedback》一書的寫作，過程中大量借助 LLM：整理 LaTeX 公式排版、做大量的 copyediting、用 TikZ 或 Python 產生圖表。他坦言在 2024 年時，一度以為 2026 年出版非虛構書籍會顯得「有點笨」，因為當時預期模型進步速度會把這類解釋性文字徹底輾壓。結果是，今日最被稱讚寫作能力的模型，反而是 GPT-4.5 與 Kimi K2 這類相對「老」的模型，而同一批模型在程式和數學上早已脫胎換骨。

🧩 **創意寫作 vs. 非虛構寫作，是兩件事**

文章區分了兩種寫作批評：一種針對高個人風格、有觀點、需要「透過文字窺見思考過程」的創意寫作（例如部落格），這類批評近年反而在增加，因為模型越工具化，離「有靈魂的表達」越遠；另一種是非虛構、說明性寫作，過去被視為 LLM 最實用的能力之一（填充文案），理論上應該隨模型智慧提升而自然變好。但 Lambert 的實測經驗顯示，這一項能力幾乎是原地踏步。

💡 **問題出在「組織」，不是「造句」**

他觀察到，模型擅長檢查或產生「一個單位」的內容：一句話、一條公式、一張圖，但在把多個單位串成一整段連貫論述時，會出現一種「複合誤差」：修飾得太刻意、產生無謂的概念錯誤、整體組織鬆散。他把這種能力拆解為兩種角色的對照：GPT-5.5 Pro 在校對整份 200-300 頁書稿 PDF 時，能挑出深藏的細微錯字；Claude 系列則更擅長編輯建議，對任務的心智模型理解更好、更能幫作者打破寫作卡關。兩者都停留在「逐點檢查」層次，而非重組整體敘事的能力。他也提到，RLVR（可驗證獎勵的強化學習）在數學與程式領域已幾乎解決了複合誤差問題，但寫作領域至今缺乏對等的訓練訊號與資料，這正是進度停滯的核心原因。

⚠️ **這對「AI 解決開放科學問題」的期待是警訊**

Lambert 認為，如果模型連整理、精彩呈現已經確立的既有科學知識都做不好，這應該被視為它們獨立解決開放性重大科學問題之前的必要前提。在 Anthropic 同期發布 Claude 在黎曼猜想（Riemann Hypothesis）上取得進展的消息背景下，他仍主張科學問題的廣度遠超過目前模型的實際覆蓋範圍，組織知識本質上是一種「壓縮」，而壓縮正是產生洞見的必要條件；今日的 LLM 在長篇非虛構寫作上反而是在增加熵，這種狀態難以無限疊加自我改善。

🎯 **實務啟示：把 LLM 當編輯，而非作者**

Lambert 分享了實際做法：他把編輯的提問以特定分隔符號嵌入 LaTeX 原始檔，讓 Claude Code 逐一定位每則註解、印出前後文，判斷是單純錯字還是需要更細緻處理，再由他撰寫或請 Claude 提供修改建議。他坦承書中不到 1% 的技術說明句子直接來自 AI，且僅在身為專家判斷「這句話正是讀者需要的」時才保留。與此對照，他在自己的部落格 Interconnects 上堅持「絕不使用 AI 產出的內容」，因為高個人風格的寫作本身就是目的，而不只是填空的手段。對工程師而言，這提示了一個更務實的協作模式：用 LLM 做逐句校對、抓錯字、給編輯建議，但整體敘事的組織與判斷，仍需要人類專家把關。

🔗 **來源**
- 標題：I wrote an AI textbook — how long until AI can do it better?
- 作者／機構：Nathan Lambert（Interconnects）
- 連結：https://www.interconnects.ai/p/i-wrote-an-ai-textbook-how-long-until

#LLM #AIWriting #NonFictionWriting #RLHF #RLVR #AIResearch #ClaudeAI #GPT #Interconnects #AIAssistedWriting
