---
title: Elsewhere
source: Simon Willison
url: https://simonwillison.net/elsewhere/
model: claude-code/sonnet
generated_at: '2026-10-10T20:47:30.118031'
score: 70
---

📌 Simon Willison 更新 ttok：確認 GPT-6 與 GPT-5 共用同一套 Tokenizer

TL;DR：ttok 升級到 1.0 並預設改用 GPT-5/6 的 tokenizer，同時作者也動手做了一個對應 OpenAI 新 Decisions API 的外掛工具。

OpenAI 到目前都沒正式公告 GPT-6 是否沿用 GPT-5 家族的 tokenizer，社群甚至為此開了一張「生氣的 issue」。開發者工具作者 Simon Willison 沒有等官方回應,而是直接用升級自己的 CLI 工具來驗證答案。

🧩 **ttok 0.4 → 1.0:一個小 bug 換來的版本躍進**

ttok 是 Simon Willison 維護的 token 計算 CLI 工具,底層用 OpenAI 開源的 tiktoken 函式庫。這個工具已經兩年沒更新,這次重啟是因為他跑 `uv tool upgrade ttok` 後發現新版本預設竟然還在用 GPT-4 的 tokenizer——對一個早該預設 GPT-5/6 的工具來說明顯不合理。他把「切換預設 tokenizer」當作出 1.0 正式版的理由,順手修掉一個 Click 警告、更新了 CI,還加上 `--list-models` 指令列出可用模型。透過 `uvx` 執行,任何人都能直接對一份檔案算 token 數,不需要額外安裝環境。

📊 **證據:七個 GPT-6 模型,31 組測資,結果一致**

至於 GPT-6 是否真的沿用 GPT-5 的 tokenizer,Simon 引用了開發者 William Liu 的一份 commit 實驗結果作為佐證:全部七個 GPT 模型(5.5、5.6 的 Sol/Terra/Luna,以及 6 的 Astra/Sol/Luna)在 31 個測試樣本上,都回報出完全一致的 44,794 個 token,彼此沒有任何落差。換句話說,GPT-6 在這份語料上並未帶來輸入計數上的變化,這也是 Simon 決定把 ttok 預設 tokenizer 切過去的依據。

🧩 **順手做了一個 OpenAI Decisions API 外掛**

OpenAI 在上週 DevDay 發布了「Jev 風格」的新 Decisions API。由於 Simon 已經有一個對接 Jev 的 `llm-typesafe` 外掛,他讓 GPT-6 Astra 讀完 OpenAI 的新文件後,仿照同樣模式建出 `llm-openai-decisions` 外掛。兩者在 API 設計上相當接近:都支援是非題、選項題、評分題三種問題類型,計價方式也都只對輸入收費、輸出免費——OpenAI 是每百萬 input token 收 10 美分,Jev 則是 4.2 美分。差異在於 OpenAI 新推出的 `gpt-6-luna` 決策模型除了文字外,還支援圖片輸入。

💡 **順帶一提:為什麼 embedding 模型該保持開放權重**

這份筆記也收錄了 Simon 對 Google EmbeddingGemma 2 採用 Apache 2.0 授權的肯定。他的論點很直接:embedding 模型的使用場景通常是一次性算出成千上萬、甚至百萬筆向量後長期儲存比對,如果模型是封閉、僅限託管的版本,一旦供應商停止提供該模型,使用者仍得花錢把所有舊向量重新算一次。他並不要求自己得親自 host 模型,而是希望「即使付費用託管服務,也能確保供應商停止服務時自己或其他業者能接手跑開放權重版本」。

🎯 **對工程師的實務啟示**

Token 計算、tokenizer 版本切換聽起來是小事,但直接牽動計費、上下文長度估算與遷移成本——這正是 ttok 這類小工具存在的價值。而 embedding 模型的授權選擇,則提醒工程團隊在導入第三方向量服務前,務必評估「供應商抽梯子」的長期風險。

🔗 **來源**
- 標題：Elsewhere
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/elsewhere/

#OpenAI #GPT6 #Tokenizer #LLM #DeveloperTools #EmbeddingGemma #OpenSource #AITooling #tiktoken #APIDesign
