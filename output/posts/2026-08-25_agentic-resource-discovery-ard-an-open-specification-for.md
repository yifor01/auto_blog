---
title: 'Agentic Resource Discovery (ARD): An open specification for agent discovery'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/agentic-resource-discovery-ard-an-open-specification-for-agent-discovery/
model: claude-code/sonnet
generated_at: '2026-08-25T06:31:54.983043'
score: 77
---

📌 AWS 力推的 ARD 規格，想讓 AI Agent 目錄像 DNS 一樣互通

TL;DR：AWS 參與制定的開放規格 ARD，目標是讓不同註冊表的 agent／MCP 資源能跨環境互相發現。

當一個組織裡的 MCP 伺服器、agent、工具越蓋越多，最頭痛的往往不是建立資源，而是「找到」它們。AWS 一篇部落格文章介紹了一套新開放規格 Agentic Resource Discovery（ARD），試圖解決這個跨環境發現的難題。

🤔 **問題：資源散落各處，接一次只能用一次**

隨著組織擴大 AI agent 與工具的使用規模，團隊建立 Model Context Protocol（MCP）伺服器、部署 agent、打造專用工具，但若缺乏中央目錄，這些資源就會彼此孤立。開發者得手動尋找資源、驗證、連接並維護連線，而且針對某個 AI 客戶端設定好的 agent，並不會自動對另一個客戶端可用。這種方式在團隊只接幾個工具時還能應付，但隨著 agent、MCP 伺服器、skill 與 API 數量在公開註冊表與企業私有環境中不斷增加，就難以為繼。

🧩 **AWS Agent Registry 解內部問題，ARD 解跨環境問題**

AWS Agent Registry 是 AWS 提供的集中式目錄，用來管理組織內的 agent、MCP 伺服器、工具、agent skill 與自訂資源，能解決單一 AWS 環境內的發現問題。但文章指出，多數企業並非只在單一環境運作——agent 與工具會分散在多個雲端、地端基礎設施、SaaS 平臺與企業應用中，每個環境都有自己的註冊表、命名慣例與 metadata schema。若每組註冊表之間要互通，就得為每一對註冊表打造客製化連接器。

ARD 想改變這個等式：只要每個註冊表用同一種格式描述資源，並透過共通協定公開發現機制，發布者只需描述一次，使用者就能在任何地方發現。文章將 ARD 的角色類比為 DNS（Domain Name System）——DNS 讓網路間的名稱解析得以互通，ARD 則想讓不同環境的 agent 目錄能夠聯邦化（federate）互通，而不需要逐一簽訂雙邊協議或開發專屬連接器。

📊 **規格現況**

ARD 是一套開放標準，而非產品或單一註冊表，採用 Apache License 2.0 授權，公開於 agenticresourcediscovery.org 及 GitHub。AWS 表示自己在該規格制定過程中提供了回饋意見。

⚠️ **仍在早期階段**

文章本身篇幅不長，並未提供 ARD 的具體資料格式細節、參與制定的其他組織名單，或實際採用案例，屬於規格與方向的初步公告，實作細節有待後續文件補充。

🎯 **實務啟示**

如果你的團隊正在維護多個 MCP 伺服器或 agent，且已經開始感受到「這個工具在 A 平臺能用、在 B 平臺要重新接一次」的痛點，ARD 這類共通描述格式值得關注，未來若能跨註冊表落地，可以省下大量客製化連接器的維護成本。目前建議先追蹤規格演進，暫不急於重構現有的內部目錄架構。

🔗 **來源**
- 標題：Agentic Resource Discovery (ARD): An open specification for agent discovery
- 作者／機構：Jeffrey Damick, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/agentic-resource-discovery-ard-an-open-specification-for-agent-discovery/

#AWS #AgentDiscovery #MCP #OpenStandard #AIAgent #AgentRegistry #Interoperability #CloudAI #DeveloperTools #AgenticAI
