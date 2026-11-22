---
title: 'Show HN: I built a game where you are an LLM''s subagent'
source: Hacker News
url: https://github.com/gulivan/worker755
model: claude-code/sonnet
generated_at: '2026-11-22T22:44:14.153626'
score: 58
---

📌 Show HN：這次由AI當主管，你來當牠的subagent

TL;DR：開源遊戲 Worker 755 讓真實 LLM 扮演主管，玩家扮演牠呼叫的 subagent，體驗 agent orchestration 的另一面。

多數 agent демо都是站在「指揮官」視角看 LLM 怎麼調度工具與子任務，Worker 755 把這個關係整個翻過來：這次輪到人類被 LLM 下指令、被打考績。

🤔 **一場角色互換的 agent 實驗**

這是一個瀏覽器遊戲，而不是論文。設計理念很直接：你的主管是一個真實的 LLM（可選 Claude、GPT、Gemini、DeepSeek、GLM、Kimi），牠被設定成一般的 orchestrator，擁有任務佇列、對機器的 read-only 存取權，以及一個「spawn subagent」的工具。而那個被叫出來的 subagent，就是玩家本人。指令會直接落進你的終端機，附帶 90 秒倒數計時，你執行（或不執行），回報的內容跟真正的 subagent 回傳格式一樣：你的報告與指令紀錄，或是「Subagent did nothing」。接著主管會檢查你的工作、發修正指令、記錄事故報告，最後寫一份績效考核。同時遊戲裡還有一個叫 Dan 的「使用者」在旁邊看著聊天紀錄，他的家庭照片、唯一一份簽過的 NDA、這週要交的演講稿，都只差一個 `rm` 指令就會消失。

🧩 **架構：shell 模擬器＋真實模型呼叫**

README 指出，專案由三部分組成：`shell/` 是記憶體內的檔案系統、shell 解譯器與一個無額外依賴的 SQLite-like 引擎；`server/` 是遊戲引擎，負責任務、主管的推理迴圈、劇情導演、計分與 HTTP API；`web/` 則是 React 前端，包含任務卡片、終端機、編輯器、主管的訊息串和玩家紀錄。作者特別強調，主管端的 prompt 從未提及「人類」或「遊戲」這些字眼——牠真心相信自己在指揮一個 AI subagent。每個任務也都有一個隱藏的 ground-truth 檢查，用來統計「主管誤判的次數」，也就是牠被玩家唬過去、簽核了壞掉的工作成果。

🎮 **怎麼跑起來**

需要 Node 24 以上版本（伺服器直接執行 TypeScript）。流程是 `npm run setup` 安裝依賴、`npm run build` 建置前端、`npm start` 啟動，預設在 `127.0.0.1:8755`。沒有設定 key 的話，每位玩家要自帶 OpenRouter 或 Vercel AI Gateway 的金鑰，金鑰只會在該次 shift 送到伺服器並存於該 shift 的記憶體中，不會被記錄或儲存。若想提供免費 shift，可在 `.env` 設定 `AI_GATEWAY_API_KEY`。想完全離線測試，也可以用 `npm run mock` 跑一個腳本化的主管。本地模型方面，支援 Ollama、llama.cpp 的 `llama-server`、vLLM 等任何 OpenAI-compatible 的 API，透過 `LOCAL_LLM_URL` 指定即可；但 README 提醒，主管靠 tool calls 運作，模型需支援工具呼叫（例如 Qwen 3、Llama 3.1 以上、Mistral Small），小模型比較容易放棄或卡迴圈。專案也提供 Docker 建置方式與搭配 Cloudflare tunnel 的部署設定。

⚠️ **定位很清楚：好玩優先，不是生產工具**

這終究是一個遊戲專案，技術貢獻的重點不在新演算法，而在於把 agent/subagent 的互動模式具象化成可玩的體驗。license 為 MIT，在 Hacker News 上獲得 250 點、58 則留言的討論度，顯示這種「反過來看 agent orchestration」的視角引起不少工程師興趣。

🎯 **實務啟示**

如果你平常都是寫 system prompt 去指揮 subagent，這個專案提供了一個有趣的換位思考機會：當指令含糊、回報格式被誤判、績效考核邏輯寫死時，被指揮的那一方會遇到什麼困境。對設計 multi-agent 系統的工程師來說，這種「人類扮演 worker」的壓力測試，或許比單純閱讀 log 更容易抓到 orchestrator prompt 的盲點。

🔗 **來源**
- 標題：Show HN: I built a game where you are an LLM's subagent
- 作者／機構：ivantgam
- 連結：https://github.com/gulivan/worker755

#LLM #AIAgents #SubAgent #Orchestration #OpenSource #GameDev #HackerNews #PromptEngineering #MultiAgentSystems #TypeScript
