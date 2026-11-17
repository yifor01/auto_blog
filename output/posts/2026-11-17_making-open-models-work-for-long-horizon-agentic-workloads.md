---
title: Making open models work for long-horizon agentic workloads
source: Together AI
url: https://www.together.ai/blog/making-open-models-work-for-long-horizon-agentic-workloads
model: claude-code/sonnet
generated_at: '2026-11-17T00:59:26.133311'
score: 96
---

📌 拆解 Coding Agent 的 Prefix Cache 失效元兇

TL;DR：Together AI 與 Ollama 聯手拆解「agent session 為何越跑越貴」，分別列出 harness 端與 inference engine 端該守住的規則。

每次 coding agent 往前走一步，harness 就會把整段對話，包含 system prompt、所有工具定義、你的請求、讀過的每個檔案、跑過的每個指令，重新完整丟給模型。換回來的往往只是一個幾十個 token 的 tool call。下一步，再把這一切加上新內容重新送一次。如果 GPU 每次都要從零重算這份越來越長的歷史，session 跑得越久就越慢、越貴。

🤔 **Agent 流量的奇特形狀**

這種「輸入序列長（ISL）、輸出序列短（OSL）」的模式是 agentic workload 的特徵。一次請求要經過兩個階段：prefill 一次性平行讀完整個 prompt、產生第一個 token，決定你要等多久才看到回應；decode 則是逐 token 往外吐字，受記憶體頻寬限制，決定輸出的速度。一般聊天兩個階段都會花時間，但 agent 的每一輪幾乎都是 prefill 在吃重，因為輸入是整個 session，輸出通常只是短短的 tool call。

🧩 **Cache 為何說斷就斷**

Prefix caching 的邏輯：引擎會保留前幾輪已經算過的 key/value，下一輪只要處理新增的部分。文章給出一個理想化算式：10 輪對話若不做 cache，要處理 1+2+…+10=55 單位的 prompt；有 cache 的話只要處理 10 單位。到了 100 輪，差距從 5,050 拉大到 100。但這個 cache 有一條硬規則：只會從 prompt 開頭比對到第一個「不同」的 token 為止，之後全部要重算。加在結尾完全免費，改動越靠前面，等於整個 session 的 cache 都要重建。

harness 決定「第一個改動會落在哪裡」，inference engine 決定「下一個請求來時 cache 還在不在」。

🧩 **兩側各自踩過的坑**

在 harness 端，Ollama 透過 `ollama launch` 讓 Claude Code、Codex、Pi 等工具可以接上 DeepSeek-V4.1-Flash、GLM-5.3 等開放模型，但這層轉譜容易無意間破壞 cache：

- **工具延遲載入**：新版 harness 支援 agent 自己搜尋並載入工具定義（例如搜尋「calendar」才載入 `save_calendar`）。理論上把定義放在 prompt 結尾最省 cache，但有些模型的 chat template 不支援在對話中途插入工具定義，一插就出錯，所以能不能這樣做取決於模型本身。
- **system prompt 裡放了會變的東西**：時間戳、git status、agent 目前所在的工作目錄，只要每輪重新渲染,整輪就等於重新讀過一次。固定在 session 內但跨 session 不同的資訊（例如使用者名稱）雖不影響當前 session，卻會讓新 session 無法沿用已經快取好的設定。解法是把這些資訊放進 task message 裡且只放一次，system prompt 全程保持不變。
- **reasoning effort 設定**：以 GLM-5.3-Flash 為例，reasoning effort 不是引擎旁路處理的獨立參數，而是被 chat template 寫進最前面的 system block，比工具列表和對話內容都更靠前。任務跑到一半把 effort 從 low 調成 high，等於從最頂端改動了 prompt,整段歷史的 cache 全部作廢。

🎯 **實務啟示**

建 harness 的人應確保 system prompt 全程不變、易變資訊下放到 task message；工具定義放在尾端前要先確認目標模型的 chat template 是否支援中途插入。做推論服務的人則要確保同一個 session 的請求能穩定路由回已經持有該 cache 的 GPU。這兩件事任何一端沒做好,長 session 的成本都會隨輪數呈平方成長。

🔗 **來源**
- 標題：Making open models work for long-horizon agentic workloads
- 作者／機構：Together AI
- 連結：https://www.together.ai/blog/making-open-models-work-for-long-horizon-agentic-workloads

#PrefixCaching #LLMInference #AgenticAI #CodingAgents #KVCache #TogetherAI #Ollama #OpenModels #LLMOps #GPUEfficiency
