---
title: Operate Claude Managed Agents inside your security perimeter
source: Claude Blog
url: https://claude.com/resources/articles/self-hosted-claude-managed-agents
model: claude-code/sonnet
generated_at: '2026-11-12T22:51:34.510639'
pinned: true
---

📌 Anthropic 讓企業把 Claude Managed Agents 整套搬進自家機房

TL;DR：self-hosted Claude Managed Agents 開放私有測試，agent 的運作主機、憑證與紀錄都能留在你自己的環境裡。

當 agent 開始無人監督地跑在你的程式碼與內部系統上，修壞掉的 build、測試上線版本、分類警報、清理 bug 待辦清單，「有沒有人盯著每一步」已經不是重點，重點變成系統本身的限制夠不夠嚴密。這正是 Anthropic 這次推出 self-hosted Claude Managed Agents 的出發點。

🤔 **從托管到自架的演進**

Managed Agents 是一組可組合的 API，用來打造並部署自主 agent，提供 agent harness、sandbox、憑證處理與 session 紀錄，讓長時間運行的 agent 能上生產環境。Anthropic 最早以 Anthropic 代管基礎設施的方式推出 Managed Agents，之後針對需要讓程式碼留在自家環境的團隊，加入了 self-hosted sandbox。這次則是進一步開放整個服務都能自架：harness、sandbox、憑證與 session 紀錄全部跑在企業自己的雲端或地端環境中，由企業自行操作 Managed Agents 伺服器、資料庫，以及 agent 執行 shell 與檔案工具的 worker。模型請求可以導向 Anthropic 本身，也可以導向 Amazon Bedrock、Google 的 Agent Platform、Microsoft Foundry，或企業自己的 gateway。如果企業本身已與 Anthropic 簽有 zero data retention（ZDR）協議，這條規則同樣適用於 agent 送往 Claude 的請求，跟一般 Messages API 呼叫一樣。

🧩 **agent 安全設計的四個原則**

Anthropic 說明 Managed Agents 的架構圍繞四項原則，無論是 Anthropic 全代管、企業只自架 sandbox，還是整套自架，都適用：

- 大腦與手分開：harness（大腦）負責呼叫 Claude，sandbox（手）才是 agent 程式碼實際執行的地方，兩者在設計上刻意分離。agent loop、session 紀錄與 vault 中的密鑰都放在 sandbox 之外，因此 agent 不必依賴單一 sandbox 存活一整個 run，sandbox 只在工具真正需要時才啟動。
- 憑證不進 sandbox：vault 的設計就是讓憑證留在 sandbox 外。對於 MCP 工具與支援的 API 呼叫，由 sandbox 外部的 proxy 負責把憑證加進請求；在 self-hosted 架構下，企業也可以把憑證存在自己的密鑰管理系統裡。
- 網路存取可被限制：企業能為每個環境設定允許存取的主機清單，其他主機的請求會被擋掉。例如一個專門修壞掉 build 的 agent，清單可能就只有 git host 與套件庫；若自架 sandbox，則由企業自己的防火牆設定同樣的限制。
- 每個 session 都留下完整紀錄：Managed Agents 會記錄 agent 的每一步，包括呼叫了哪些工具、回傳了什麼，紀錄可透過 OpenTelemetry 匯出，接入企業現有的監控工具，和其他系統的紀錄一起檢視。

⚠️ **目前仍是私有測試階段**

Self-hosted Claude Managed Agents 目前處於 private beta，需要透過 Anthropic 的客戶團隊申請存取權限。

🎯 **實務啟示**

對於已經讓 agent 接觸內部系統、但受限於資料駐留或合規要求無法使用托管服務的團隊，這個方向提供了一條路：先用 Anthropic 全代管快速驗證 agent 的價值，等到授權範圍擴大、風險等級上升時，再逐步把 sandbox、甚至整套服務搬進自己的環境，架構上的四個安全原則不需要重新設計。

🔗 **來源**
- 標題：Operate Claude Managed Agents inside your security perimeter
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/self-hosted-claude-managed-agents

#Anthropic #ClaudeAI #AIAgents #EnterpriseSecurity #SelfHosted #DevOps #MLOps #AgentSecurity #CloudInfrastructure #OpenTelemetry
