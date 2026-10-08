---
title: Docker Agent
source: Hacker News
url: https://github.com/docker/docker-agent
model: claude-code/sonnet
generated_at: '2026-10-08T22:18:08.593844'
score: 94
---

📌 Docker 出手做 AI Agent 框架：YAML 寫 agent，HN 熱議破 292 分

TL;DR：docker-agent 用 YAML 宣告多 agent 系統，可像容器映像檔一樣推送分享。

當大家還在用 Python 或 TypeScript 手刻 multi-agent pipeline 時，Docker 直接把「定義 agent」這件事做成了 docker CLI 的一個 plugin，整套設定寫在 YAML 裡，推上 OCI registry 就能像拉 Docker image 一樣分享給別人跑。這個專案在 Hacker News 上已經累積 292 個讚、136 則留言，討論熱度不低。

🤔 **解決什麼問題**

docker-agent 讓使用者不用寫程式碼，就能建立會互相協作的智慧型 agent 來解決複雜問題。它是一個 docker CLI plugin，可以用 `docker agent` 指令直接呼叫，目標是把「打造、執行、分享 AI agent」這件事變成跟操作容器一樣直覺。

🧩 **核心設計：YAML 宣告 agent，工具用 MCP 接**

一個最小可行的 agent 設定看起來像這樣：在 YAML 裡定義 `agents`，指定 `model`（例如 `openai/gpt-5-mini`）、`description`、`instruction`，再透過 `toolsets` 接上工具，例如用 `type: mcp` 搭配 `ref: docker:duckduckgo` 接上一個 MCP server。寫好之後執行 `docker agent run agent.yaml` 就能跑起來。

專案的關鍵特性包括：

- **多 agent 架構**：可以建立一組專職分工的 agent 團隊，彼此自動委派任務。
- **豐富工具生態**：內建工具之外，還能接上任何 MCP server，不管是本機、遠端或是跑在 Docker 裡的都支援。
- **模型無關**：支援 OpenAI、Anthropic、Gemini、AWS Bedrock、Mistral、xAI，以及 Docker 自家的 Docker Model Runner，方便接本地模型。
- **YAML 設定**：宣告式、可版本控管、可分享。
- **進階推理工具**：內建 think、todo、memory 等工具。
- **RAG 支援**：可插拔的檢索機制，支援 BM25、embedding、混合搜尋（hybrid search）與 reranking。
- **打包與分享**：可以把 agent 推送到任何 OCI registry，其他人拉下來就能直接跑。

🎯 **怎麼安裝、怎麼跑**

Docker Desktop 4.63 以上版本已經預先內建 docker-agent plugin，直接執行 `docker agent` 即可使用。也可以用 Homebrew 執行 `brew install docker-agent` 安裝，或從 GitHub Releases 下載二進位檔，並將其連結（symlink）到 `~/.docker/cli-plugins/docker-agent`。使用前需要設定至少一個模型 API 金鑰（例如 `OPENAI_API_KEY`、`ANTHROPIC_API_KEY`），或者改用 Docker Model Runner 跑本地模型。

快速上手的指令包括：`docker agent run` 執行預設 agent、`docker agent run myorg/agent:tag` 直接從 OCI registry 拉下別人分享的 agent 來跑、`docker agent new` 互動式產生新 agent，或是 `docker agent run agent.yaml` 跑自己寫的設定檔。專案本身甚至用自己的工具來開發自己：README 提到他們用 `docker agent run ./golang_developer.yaml` 來開發 docker-agent。

⚠️ **使用前要注意的細節**

docker-agent 預設會收集匿名使用資料以改善工具，官方文件中有獨立的 Telemetry 說明頁面，在意隱私的團隊部署前應該先確認這部分的設定選項。

🎯 **實務啟示**

對已經習慣用 Docker 管理基礎設施的團隊來說，docker-agent 把「建 agent」這件事收斂成跟寫 docker-compose.yml 差不多的心智模型，降低了從零打造 multi-agent 系統的門檻，尤其是 MCP 工具生態與 OCI registry 分享機制，讓 agent 設定檔有機會像容器映像檔一樣被版本化、重複利用。想先試水溫的話，直接用 Homebrew 裝起來跑一個最小 YAML 範例，是最快感受這套工作流的方式。

🔗 **來源**
- 標題：Docker Agent
- 作者／機構：saikatsg（Hacker News 發文者）
- 連結：https://github.com/docker/docker-agent

#Docker #AIAgent #MultiAgent #MCP #YAML #LLM #OpenSource #DevTools #AgentOrchestration #RAG
