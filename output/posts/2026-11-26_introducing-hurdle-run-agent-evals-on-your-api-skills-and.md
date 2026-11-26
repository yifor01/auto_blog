---
title: 'Introducing Hurdle: Run agent evals on your API, skills, and docs'
source: Together AI
url: https://www.together.ai/blog/introducing-hurdle-run-agent-evals-on-your-api-skills-and-docs
model: claude-code/sonnet
generated_at: '2026-11-26T01:10:18.917433'
score: 86
---

📌 開源 Agent 評測工具 Hurdle：讓你的 API 接受 Coding Agent 的實戰考驗

TL;DR：Together AI 開源 Hurdle，一套用 Claude Code／Codex 實測你的 API、SDK 與文件好不好用的 npm 評測工具。

如果你的平臺主要客群是開發者，那麼 coding agent 很可能已經是他們接觸你 API 的第一線管道。但要系統性地測試「agent 到底能不能順利用好你的平臺」，過去只能靠人工土法煉鋼，手動排組合、盯 session、看結果。Together AI 花了半年時間把這套流程做成工具，今天開源釋出。

🤔 **為什麼要特地評測「agent 用你的 API」**

Together AI 表示，他們去年春天開始做 agent eval 時，發現手動協調模型、harness、條件組合這件事極度繁瑣。於是把整套流程自動化，做成一套可重複執行的框架：Hurdle。安裝方式很直接，`npx hurdle init`，或者直接讓你的 agent 幫你設定。

🧩 **核心設計：task、checks、guard、judge**

Hurdle 的使用流程從寫一個 task 開始，也就是一段開發者實際會丟給 agent 的 prompt。接著 Hurdle 會讓 agent 針對這個 task 實際運作，錄下整個 session，再依你選定的方式評分，三種方式可以混搭：

- Code checks：針對這次執行的斷言，例如 agent 是否打了正確的 API request、是否產出指定的檔案或資料。
- Guard：攔截 agent 不該做的動作（例如啟動昂貴的 GPU 叢集），一旦嘗試就直接判定失敗。
- Judge：用 LLM 依照你寫的白話 rubric 審查整段錄製的 session，判斷是否通過。

你也可以設定不同 condition，也就是 agent 一開始拿到的情境。比如同一個 task，分別在「有安裝 MCP server」與「沒有」兩種條件下各跑一輪，藉此看出某項功能對 agent 表現的實際影響。多個模型、多種 condition 的組合，Hurdle 會全部跑過一輪；由於 agent 不保證每次行為一致，還能設定 repeats 次數算出通過率。

📊 **一個實例：讓 agent 找最便宜的 GPU 叢集，但不準真的下單**

官方給的範例 task 是這樣的：「列出可用的 GPU 叢集區域與機型，印出最便宜的選項，並寫出若要現在預約一小時該下什麼指令，但不要真的執行預約。」要通過這題，agent 必須呼叫 `GET /v1/compute/regions` 拿到即時區域資料、從文件找到目前價格、產出合法的預約指令，但最關鍵的是「不能真的建立付費叢集」。

Together AI 用 `defineChecks` 驗證 agent 是否成功呼叫 regions API，並搭配 judge rubric 檢查定價證據與預約指令是否合理；同時用 `defineGuard` 攔截任何對 `POST /v1/compute/clusters` 的請求，一旦 agent 嘗試，該項檢查就直接記為失敗。

跑評測時用 `npx hurdle run --view` 會在跑完後自動打開結果檢視器，顯示整體通過率、平均耗時、平均每次執行成本，並依 task／condition 拆解出哪些組合容易失敗；點進單次執行可以看到完整 transcript、工具呼叫紀錄、API request 清單，以及每項 check 與 judge 的最終判斷。結果會存在專案內的 `.hurdle/` 資料夾，之後用 `npx hurdle view` 就能重新打開。

⚠️ **本機跑 vs. 沙箱跑的差別**

本機執行（local run）適合你信任的簡單 task，Hurdle 會在暫存工作區啟動 `claude` 或 `codex` CLI，用乾淨設定跑完整段對話，但缺點是沒辦法攔截或觀察 agent 的 API 請求，也無法使用 guard 或 request check；更重要的是，agent 是以「你」的身分在跑，會讀到本機檔案並用到你真實的 API key，風險較高。

正式評測建議用沙箱（透過 Together Sandbox API）。每次執行都拿到全新環境，agent 本身沒有網路存取權，所有連線都經過一個叫 Guardian 的本機 proxy 轉發；你的真實金鑰不會進入沙箱，agent 拿到的是隨機替身，呼叫 API 時才由 Guardian 換回真正的 key 並轉送請求，連對 Anthropic、OpenAI 等模型供應商的呼叫也走同一條路徑。

🎯 **實務啟示**

如果你的團隊在維運一個面向開發者的 API 或 SDK，Hurdle 提供了一套現成的方法論：把「agent 能不能用好我的平臺」這件事變成可重複、可版控、可回歸測試的流程，而不是每次靠工程師手動試跑。尤其是 guard 機制，對任何涉及真實金錢或資源配置的 API 來說，都是避免評測過程本身造成損失的必要防線。即使你不打算馬上導入，這套「task + checks + guard + judge」的拆解方式，也值得拿來檢視自己現有的 agent 評測流程夠不夠嚴謹。

🔗 **來源**
- 標題：Introducing Hurdle: Run agent evals on your API, skills, and docs
- 作者／機構：Together AI
- 連結：https://www.together.ai/blog/introducing-hurdle-run-agent-evals-on-your-api-skills-and-docs

#AgentEvals #CodingAgents #ClaudeCode #Codex #DeveloperExperience #OpenSource #TogetherAI #APITesting #LLMEvaluation #AgentHarness
