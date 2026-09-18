---
title: Best Open-Source Agent Harnesses for Local LLMs in 2026
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/18/best-open-source-agent-harnesses-for-local-llms-in-2026/
model: claude-code/sonnet
generated_at: '2026-09-18T19:54:21.210781'
score: 90
---

📌 2026年本地LLM代理框架怎麼選？11款開源Harness實測盤點

TL;DR：MarkTechPost 依授權、本地執行文件完整度與維護狀態，評比 11 款開源 agent harness，本地部署前必讀。

「模型」只是 agent 的一半，另一半是「harness」：負責跑工具、管狀態、控權限、把結果餵回模型。當你把模型換成跑在自己機器上的本地 LLM，這個差異會被放大——因為本地模型的 context window 通常較小、tool calling 能力也較弱，harness 設計上的任何缺陷都會被直接暴露出來。

🤔 **為什麼本地部署更吃 harness 的設計**

MarkTechPost 這篇整理，於 2026 年 9 月 18 日直接從各專案 GitHub 讀取事實，依 OSI 核可授權、是否記載本地執行方式、維護狀態與安全控管四項標準排名 11 款工具。文中特別點出兩個容易被忽略的前置動作：一是拉高 context window，Ollama 官方文件指出預設值依 VRAM 而定（24 GiB 以下為 4k、24–48 GiB 為 32k、48 GiB 以上才到 256k），但 agent／coding 類工具建議至少要有 64,000 tokens，一行指令 `OLLAMA_CONTEXT_LENGTH=64000 ollama serve` 即可調整；二是要挑選支援 tool calling 的模型，Goose 文件說明不支援 tool calling 的模型只能做純聊天，llama.cpp 則要靠 `--jinja` 參數才能啟用相容的 chat template。

🧩 **各家 harness 的定位差異**

- **OpenCode**：文件記載 Ollama、LM Studio、llama.cpp 的 llama-server 三條本地路徑，均透過 `@ai-sdk/openai-compatible` 搭配本地 baseURL，宣稱總計支援 75 家以上 provider；內建 build（完整權限）與 plan（唯讀、執行 bash 前需詢問）兩種 agent。
- **Pi**：走極簡路線，README 只給模型四個工具——read、write、edit、bash，刻意不做 MCP、子代理、plan mode 與權限彈窗，這些功能改用 TypeScript 擴展補上；原生支援 llama.cpp 的 router server，可用 `/llama` 管理多個 GGUF 模型。值得注意的是 Pi 沒有內建權限系統，直接沿用使用者權限執行，README 建議搭配 Docker 或 micro-VM 隔離。舊網址 badlogic/pi-mono 已轉址至 earendil-works/pi，Earendil 於 2026 年 4 月收購 Pi，創作者 Mario Zechner 也加入該公司；據 The Pragmatic Engineer 報導，Pi 是 OpenClaw 的技術基礎。
- **Goose**：文件記載的本地執行環境最多，涵蓋 Ollama、LM Studio、Docker Model Runner、Ramalama、Atomic Chat，vLLM 與 KServe 則透過 OpenAI 相容介面串接。治理面也是亮點：Linux Foundation 於 2025 年 12 月 9 日成立 Agentic AI Foundation，Block 將 goose 捐贈進去，專案現位於 aaif-goose/goose，以 Rust 撰寫，README 宣稱擁有 70 個以上 MCP 擴展。
- **Cline**：本地指南建議務必開啟「Use Compact Prompt」，並搭配專注型任務與定期開新 session；預設每次檔案編輯與指令執行都需人工核准，也可切換自動核准，並以 Plan／Act 模式分離策略與執行。要注意的是，其 JetBrains 外掛並未開源，只有 VS Code 擴展、CLI 與 SDK 採用 Apache-2.0 授權。
- **OpenHands**：本地指南最具體，建議 Qwen3.6-35B-A3B 作為首選本地模型（截至 2026 年 5 月 21 日），量化版本至少需 24GB VRAM，或 64GB 統一記憶體的 Apple Silicon Mac；context length 建議至少 22,000、理想為 32,768，並直接點名 Ollama 4,096 的預設值連 system prompt 都放不下。Linux 使用者要注意 LM Studio 預設只綁定 127.0.0.1，容器化的 OpenHands 需開啟「Serve on Local Network」才能連上。
- **Aider**：以 whole／diff 兩種 edit format 因應 tool calling 較弱的模型，並在每次請求附上程式碼庫的符號地圖；其 Ollama 文件特別警告 Ollama 會靜默捨棄超出 context window 的內容，因此 Aider 會依請求動態調整視窗大小並預留 8k tokens 給回覆。維護狀態是隱憂，PyPI 顯示 0.86.2 版發布於 2026 年 2 月 12 日，前一版則停留在 2025 年 8 月。
- **Codex CLI**：Apache-2.0 授權，內建 ollama（11434 埠）與 lmstudio（1234 埠）兩個本地 provider，`codex --oss` 預設使用 gpt-oss:20b；硬性限制是只支援 Responses API（`/v1/responses`），原始碼會拒絕 `wire_api = "chat"`，本地伺服器必須提供對應端點。
- **Qwen Code**：README 列出 OpenAI、Anthropic、Gemini、Qwen 四種協定，本地模型指向 Ollama 與 vLLM；專案源自 Google Gemini CLI v0.8.2，在 v0.1 後停止同步上游。
- **Kilo**：README 說明 Kilo CLI 是 OpenCode 的 fork，最早則源自 2025 年的 Roo fork，2026 年 4 月 2 日推出重建版 VS Code 擴展；本地模型文件涵蓋 Ollama、LM Studio、Atomic Chat，並提醒本地模型通常缺乏 prompt caching 與 computer use 能力。
- **Hermes Agent**：Nous Research 出品的通用型 agent，而非程式碼工具，README 描述一套能從經驗中生成技能的學習迴圈，Ollama 頁面指出內建 70 個以上技能與跨 session 記憶，並支援 Telegram、Discord、Slack、WhatsApp、Signal、Email 等訊息閘道。
- **OpenClaw**：本清單中星數最高的專案，Ollama 將其描述為透過中央閘道橋接訊息服務與 AI agent 的個人助理，本地模型建議至少 64k context window；首次啟動會顯示安全提示，說明工具存取的風險，因為它會連接使用者的訊息帳號。

🎯 **實務啟示**

部署本地 agent harness 前，先確認三件事：context window 是否拉到至少 64k、模型是否真的支援 tool calling、記憶體規劃是否誠實對應模型量級（Cline 文件建議 16–32GB RAM 配小型量化模型、32–64GB 配中型 coding 模型、64GB 以上才上大模型）。若目標是純 coding 場景，OpenCode 或 Aider 的文件最務實；若要做容器化長任務，OpenHands 的硬體指引最直接；若在意治理與長期維護，Goose 掛在 Linux Foundation 底下相對穩健。

🔗 **來源**
- 標題：Best Open-Source Agent Harnesses for Local LLMs in 2026
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/09/18/best-open-source-agent-harnesses-for-local-llms-in-2026/

#OpenSource #LLM #AIAgent #LocalLLM #Ollama #LLMOps #DeveloperTools #ToolCalling #AgentHarness #EdgeAI
