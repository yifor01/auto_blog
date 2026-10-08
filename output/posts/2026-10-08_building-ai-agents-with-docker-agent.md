---
title: Building AI Agents with Docker Agent
source: KDnuggets
url: https://www.kdnuggets.com/building-ai-agents-with-docker-agent
model: claude-code/sonnet
generated_at: '2026-10-08T22:23:41.002904'
score: 91
---

📌 Docker Agent:用YAML把AI Agent打包成「容器」

TL;DR：Docker推出開源CLI工具Docker Agent，讓AI agent像容器一樣用YAML定義、版本控管、透過OCI registry分發。

Docker靠「打包一次、到處執行」這個理念建立起地位，現在它把同樣的邏輯搬到AI agent身上：不用寫程式碼，用一份declarative設定檔描述agent，透過CLI外掛執行，再用你本來就在用的OCI registry來分發。

🤔 **AI agent能不能像容器映像檔一樣被定義、版本化、分享？**

這是Docker Agent要填補的空缺。它是一個Apache 2.0授權的開源CLI外掛，由Docker Engineering團隊開發，安裝後以`docker agent`指令執行，標語直接寫明目標：「run AI agents like containers」。根據文章，這個專案在pkg.go.dev上的Go module紀錄顯示，最早的標籤版本可追溯到2026年3月，成長速度很快，目前已累積超過3,300個GitHub星數與近10,000次commit。文章也提到，這並非憑空出現，而是Docker在2025年陸續鋪墊的成果：先是讓Docker Compose支援agent與AI模型，接著推出Docker Model Runner讓使用者能在本機跑模型而不需雲端API key，Docker Agent則是這些基礎落地成的獨立工具。

🧩 **YAML定義agent，provider不綁定，支援多agent協作**

Docker Agent的設計理念有幾個重點：agent用YAML（或HCL）定義而非寫程式碼，門檻因此降低；它是provider-agnostic的，支援OpenAI、Anthropic、Gemini、AWS Bedrock、Mistral、xAI以及透過Docker Model Runner執行的本機模型，設定檔不會被綁死在單一供應商上；它支援真正的多agent協作（multi-agent orchestration），可以組出一群各自專精的agent互相委派工作；工具生態系包含內建工具，以及任何MCP伺服器，可以在本機、遠端，或是獨立的Docker容器中執行以取得隔離性；最後，呼應容器的類比，做好的agent可以推送到、或從任何OCI相容的registry拉取，用的正是Docker映像檔原本就在用的那套分發機制。

💡 **三步驟上手：安裝、設定模型、寫第一個agent**

文章給出完整的手把手教學。安裝有三條路：Docker Desktop 4.63以上版本已內建外掛，直接執行`docker agent`即可；透過Homebrew執行`brew install docker-agent`安裝二進位檔，可用`docker-agent`指令執行，或將其symlink到`~/.docker/cli-plugins/docker-agent`以改用`docker agent`這種呼叫形式；也可以直接從GitHub Releases下載二進位檔，再用同樣方式建立symlink。模型設定則有兩個選項：設定雲端供應商的API key作為環境變數（如`ANTHROPIC_API_KEY`），或完全不用雲端key，透過Docker Model Runner在本機跑模型。安裝完成後可用`docker agent --help`確認。

最小可行的agent只需要一份YAML檔，裡面定義`root`這個進入點agent（每份設定檔都必須有名為`root`的agent），指定`model`（格式為provider/模型名稱，如`anthropic/claude-sonnet-4-5`）、`description`（簡短描述，當設定檔中有多個agent時尤其重要）、`instruction`（也就是system prompt，用白話描述agent的行為）、以及`toolsets`（agent可用的能力清單，例如`filesystem`賦予讀寫檔案權限、`shell`允許執行指令、`think`讓agent在行動前有結構化的推理空間，對原生推理能力較弱的模型特別有用）。寫好之後可用`docker agent run agent.yaml`進入互動式對話，或用`docker agent run --exec agent.yaml "任務描述"`以非互動方式單次執行，適合用在腳本或CI中。

若要讓agent接上外部能力，文章特別點出MCP的使用建議：將MCP伺服器跑在獨立的Docker容器中，而不是當成本機裸執行的process。設定檔裡只要在`mcp`工具型別的`ref`欄位加上`docker:`前綴（如`docker:duckduckgo`），就會讓該MCP伺服器在自己的容器中執行；文章強調這是官方建議的用法，因為預設就具備安全性與隔離性，而不是把系統存取權信任給一個任意的本機process。此外還有`memory`工具型別，可以在指定路徑建立持久化儲存，讓agent能跨對話回憶重要發現。

文章最後示範了一個多agent團隊的完整案例：一個內容研究團隊，由`root`協調者將主題委派給`researcher`進行網路搜尋，再將研究結果交給`writer`產出報告。協調者在設定中透過`sub_agents: [researcher, writer]`宣告可委派的下游agent，`researcher`則搭配`docker:duckduckgo`這個MCP工具與`memory`持久化儲存來完成任務。

⚠️ 文章聚焦在安裝與實作步驟，並未提及Docker Agent在效能、穩定性或與其他agent框架（如LangGraph、AutoGen）相比的優劣，這部分留白。

🎯 **實務啟示**

如果你的團隊已經熟悉Docker生態系的映像檔、registry與CI流程，Docker Agent的價值在於把這整套熟悉的分發與版本控管機制直接套用到AI agent上，尤其是用容器隔離MCP伺服器這個細節，值得在設計agent工具呼叫的安全邊界時參考。

🔗 **來源**
- 標題：Building AI Agents with Docker Agent
- 作者／機構：Shittu Olumide, KDnuggets
- 連結：https://www.kdnuggets.com/building-ai-agents-with-docker-agent

#DockerAgent #AIAgents #MCP #MultiAgent #OpenSource #DevTools #LLM #Containerization #CLI #AgentOrchestration
