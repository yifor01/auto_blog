---
title: Recursive launches Flint, a laptop coding model it says was largely built by
  AI
source: TechCrunch AI
url: https://techcrunch.com/2026/10/21/recursive-launches-flint-a-laptop-coding-model-it-says-was-largely-built-by-ai/
model: claude-code/sonnet
generated_at: '2026-10-21T20:56:51.986667'
score: 101
---

📌 Recursive 推出 Flint，號稱由 AI 主導打造的筆電編碼模型

TL;DR：成立僅一年的 Recursive 發表開源編碼模型 Flint，開發過程大量仰賴自家 AI 研究系統完成。

一個由 AI 系統參與幾乎每個開發環節、僅用不到四個月打造出來的模型，會是什麼樣子？Recursive 用新發布的 Flint 給出了答案：一個免費、可在筆電上跑的編碼模型，也是「遞歸自我提升」（recursive self-improvement）這個業界爭論已久的概念，首次公開落地的早期測試。

🤔 **AI 做研究、人類來監督**

Recursive 去年成立，目標是打造能自我改進的 AI。公司的自動化研究系統「Eureka Machine」會提出想法、執行實驗並根據結果決定下一步要嘗試什麼。根據公司發布的launch影片，Eureka 幾乎參與了 Flint 開發的每個環節，從 pre-training、post-training 到 inference 都有涉入，讓一個小團隊能在不到四個月內從零打造出這個模型。

遞歸自我提升是 AI 業界最受爭議的想法之一——部分研究者擔心 AI 自我改進的過程可能脫離人類控制。Recursive 目前的版本更為有限：Eureka Machine 是受人類監督的 AI 研究助理，產出的成果是一個小到能塞進筆電的模型。公司今年五月從隱身模式亮相時，已拿到來自 GV、Nvidia、AMD Ventures 等投資方的 6.5 億美元資金，估值達 46.5 億美元，由 Salesforce 前首席科學家 Richard Socher 擔任 CEO。

🧩 **40B 參數的 MoE 模型，只啟用 2.5B**

Flint 採用 mixture-of-experts 架構，總共 40 億...不，是 400 億個參數（40B），但每次只啟用其中 25 億（2.5B）個參數，使其輕量到能在一般筆電上運行，遠小於 Meta 上週發布、需要至少 1TB 記憶體的 Mac 模型 Muse Spark Open（816B 參數）。由於模型運行在使用者自己的電腦上而非雲端伺服器，開發者可以離線使用、保護程式碼隱私，也不用支付依文字處理量計費的雲端服務費用。Flint 以 Apache 2.0 開源授權，免費在 Hugging Face 上提供下載。

📊 **推理速度與跑分雙雙亮眼**

根據 Recursive 的測試，Flint 在搭載 Apple M4 Pro 晶片的 MacBook Pro 上，可達到約每秒 131 個 token，大約是 Google Gemma 4 與 Nvidia Nemotron 3.5 Lightning 等同類模型（每秒 58 到 69 個 token）的兩倍；在 NVIDIA RTX Spark 上則突破每秒 150 個 token。

在 SWE-Bench Verified（衡量 AI 修復真實軟體 bug 能力的基準）上，Flint 的表現優於所有 50B 參數以下的模型；在 Recursive 自家六項測試的平均分數中，只有 Alibaba 的 Qwen3.8 27B 得分高於 Flint。公司坦言 Flint 比付費的大型編碼助手需要更多引導，建議使用者將大型任務拆解成較小的步驟。Wired 記者 Will Knight 在配備 48GB 記憶體的 Mac 上用 Flint 建立了待辦事項 App 與網路研究工具等幾個小程式，發現許多小型編碼模型相較於 Claude 或 Codex 常出錯或速度慢，但 Flint 每次都準確完成他的編碼需求。

💡 **Eureka Machine 具體做了什麼**

Recursive 表示 Eureka 的貢獻包括：設計出更稀疏的模型結構、透過低位元（low-bit）訓練讓 Flint 體積縮小 71% 且幾乎沒有損失品質，以及打造加速底層運算的自訂 kernel。公司並未透露 Eureka 究竟為研究團隊節省了多少時間，但這種依賴 AI 做研究的做法並非孤例——OpenAI 上個月表示，截至 8 月中，其 AI agent 每一個人類研究員的工作日，就能對應記錄 3.1 個工作日的產出。Recursive 今年六月與 Amazon Web Services 簽下的 4.1 億美元運算合約，公司當時就表示重點「不在於headcount，而在於agent count」。

⚠️ **目前仍是「有人看著」的版本**

Recursive 強調 Eureka Machine 目前是由人類監督的研究助理，並非完全自主。公司的長期目標是讓 Eureka 達到完整的遞歸自我提升，但同樣強調過程會由人類監督，並保留在出錯時隨時中止的能力。Recursive 表示，每一代新模型都應該讓 Eureka 成為更好的研究者，進而幫助它更快打造下一代模型。

🎯 **對工程師的啟示**

如果你需要一個能完全離線運行、保護程式碼隱私又不產生 API 帳單的編碼模型，Flint 的體積與速度組合值得實測；但考慮到官方自承需要更細的任務拆解，較適合用在明確定義、可拆解的編碼任務，而非完全取代大型雲端編碼助手。

🔗 **來源**
- 標題：Recursive launches Flint, a laptop coding model it says was largely built by AI
- 作者／機構：Aditya Mehta, TechCrunch
- 連結：https://techcrunch.com/2026/10/21/recursive-launches-flint-a-laptop-coding-model-it-says-was-largely-built-by-ai/

#RecursiveAI #Flint #OpenSourceAI #CodingModel #MixtureOfExperts #RecursiveSelfImprovement #AIResearch #OnDeviceAI #LLM #HuggingFace
