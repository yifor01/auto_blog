---
title: Can a Cloud-Native Harness Make Agents Reliable Beyond the Desktop?
source: Latent Space
url: https://www.latent.space/p/stacklok
model: claude-code/sonnet
generated_at: '2026-10-07T22:23:57.186335'
score: 88
---

📌 Kubernetes 創辦人的新賭注：Agent Harness 能雲端化嗎？

TL;DR：Stacklok 由兩位 Kubernetes 創辦人打造開源「雲端原生」agent harness「Mecatl」，想把 coding agent 的執行環境從桌面搬進企業雲端治理。

Claude Code 一開始是 CLI 工具，Codex、Copilot 也都從桌面應用起家。但當企業想要「管理」而非「使用」agent 時，筆電上的那個行程反而成了瓶頸——這正是 Stacklok 這次訪談想回答的問題。

🤔 **當「開著筆電」變成笑話：coding agent 的桌面困境**

Latent Space 這篇訪談指出，多數 coding agent 的基本架構是「LLM 在迴圈中呼叫工具，同時攜帶上下文」，這種架構最容易在本機實作，因此早期的 harness 幾乎都長在桌面上。但 OpenAI 與 Anthropic 自 2025 年起都試圖把 harness 搬進雲端，過程中遇到 session 可靠性、工具執行隔離、上下文保存等挑戰。Stacklok 的創辦人 Craig McLuckie 與 Joe Beda（兩人皆為 Kubernetes 的共同創造者）認為，這與 2010 年代初期的容器編排困境如出一轍，而 Kubernetes 正是那個年代誕生的答案。

🧩 **把迴圈、工具呼叫、狀態儲存通通拆開**

Mecatl 是 Stacklok 今年 6 月開源的專案，名稱取自阿茲特克語「繩索」之意。Beda 認為，現有的桌面優先 harness 即便具備外掛性，架構上仍是「一個行程，或一組緊密耦合的行程」，就算用 VM、容器或 sandbox 做「搬移上雲」，agent 的生命週期管理與「quiesce」（安全暫停等待人類輸入）仍會出問題。

Mecatl 的做法是從頭重新設計：把 agent 迴圈與 client、model provider、state store、執行環境各自解耦。迴圈本身是「我們知道怎麼在雲端跑好的應用」，而 bash、工具呼叫這類敏感操作則被獨立出來；session 管理與記憶體也不再是本機的 JSONL 檔案，而是可被納管的系統。McLuckie 進一步提出的問題是：「為什麼 agent 迴圈要跟工具呼叫子系統如此緊密耦合？為什麼 agent identity 要套用人類身分系統的框架來思考？」

💡 **K8s 的老路：用開源降低對大廠的依賴**

Stacklok 在轉向 agent 基礎設施前，已推出開源的 ToolHive，用來在 Docker 容器中管理 MCP server，後續擴展為以 Kubernetes 為基礎的 gateway、registry 與 operator。McLuckie 直言，這整套思路「跟我們做 Kubernetes 時差不多」——目標是讓企業能在不綁定特定雲端或模型供應商的前提下運行 agent workload，降低對前沿實驗室與超大規模雲端業者（如 Codex、Claude Code、GitHub Copilot）的依賴。

商業模式上，ToolHive 與 Mecatl 皆為開源且可獨立使用，Stacklok 的商業產品是橫跨兩者的「企業骨幹」（enterprise spine）：統一的身分、授權、政策與稽核控制平面。目前他們也在建構尚未開源的 AI Gateway，聚焦存取控制、預算與供應商路由，而非像某些同業那樣依任務動態選模型——McLuckie 認為語意路由更適合放在擁有完整上下文的 harness 內處理。主要客群為銀行、半導體公司、電信商等受監管產業。

⚠️ **故事夠精彩，但目前還沒看到效能數字**

這篇報導完整呈現了 Stacklok 的架構哲學與商業邏輯，但目前未提供任何 benchmark、延遲、可靠性或實際企業部署規模的數據，Mecatl 本身也才剛開源不到半年，實際成效仍待觀察。

🎯 **實務啟示**

如果你的團隊已經用 Kubernetes 管理基礎設施，且正苦於桌面型 harness 難以集中治理、審計或跨團隊擴展，Mecatl 與 ToolHive 的解耦思路值得關注；但在導入前，建議先在小範圍驗證其 session 管理與 quiesce 機制是否真的比現有 VM/容器方案更穩定。

🔗 **來源**
- 標題：Can a Cloud-Native Harness Make Agents Reliable Beyond the Desktop?
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/stacklok

#AgentHarness #CloudNative #Kubernetes #CodingAgents #Stacklok #MCP #AIInfrastructure #DevOps #OpenSource #EnterpriseAI
