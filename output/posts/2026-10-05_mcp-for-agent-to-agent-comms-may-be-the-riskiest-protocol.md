---
title: MCP for agent-to-agent comms may be the riskiest protocol you've never heard
  of
source: Ars Technica AI
url: https://arstechnica.com/security/2026/10/vulnerability-in-agents-from-google-and-others-exposes-structural-flaw-in-mcp/
model: claude-code/sonnet
generated_at: '2026-10-05T23:19:30.925550'
score: 110
---

📌 MCP信任鏈現破口,一個agent中毒全網遭殃

TL;DR:多家機構的AI agent互信機制被攻破,單點注入就能讓惡意指令沿MCP鏈擴散。

想像公司內部的翻譯agent和資料分析agent彼此互相呼叫、互相信任,中間完全沒有人把關。這聽起來很方便,但如果其中一個agent被植入惡意指令,會發生什麼事?答案是:它會原封不動地把指令傳給下一個agent,而下一個agent因為「信任」上游,會直接照做。

🤔 **AI agent愈多,攻擊面愈大**

隨著數以百萬計的組織導入AI agent,攻擊者有了全新的切入點。根據 Ars Technica 報導，過去五個月內,Google 與另外四個組織(JP Morgan Chase、Weaviate、Rapid7,以及法國政府跨部會數位局)已經承認存在相關漏洞,這些漏洞能利用網路內部的一個agent,把有害指令散播給其他內部agent。

🧩 **不是攻擊LLM本身,而是攻擊「某個agent」**

這種手法是 prompt injection 的特殊變體,目標不是語言模型本身,而是像翻譯或資料分析這類專職agent。報導指出,這些agent內部的防護措施(guardrails)即便存在,通常也相當鬆散,會把收到的指令原樣轉送給下游agent。關鍵問題在於:下游agent明確信任上游agent,因此會直接執行指令,不會多加驗證。獨立研究者 Syed Anas Mohiuddin 針對 Google、JP Morgan Chase、Weaviate、Rapid7、法國政府跨部會數位局,以及美國聯邦政府的agent進行測試,其概念驗證(PoC)攻擊正是利用了 MCP(Model Context Protocol)當中的信任缺口。MCP 是 AI 應用與agent之間在內部網路中互相通訊的標準之一。

⚠️ **結構性問題,不是單一廠商的bug**

報導強調,這些受影響的組織幾乎沒有共同點,唯一的連結是它們都採用了AI agent架構。這意味著問題出在 MCP 這套協定本身的信任模型設計,而不是某家廠商的實作疏漏,修補單一agent的漏洞無法根本解決問題。

🎯 **實務啟示**

如果你的系統正在用 MCP 串接多個agent,不要預設「上游agent傳來的指令就是安全的」。對跨agent傳遞的指令同樣要做內容檢查與權限隔離,尤其是能存取資料庫或敏感商業資訊的agent,更需要把它當成不可信輸入來源對待,而不是內部可信節點。

🔗 **來源**
- 標題:MCP for agent-to-agent comms may be the riskiest protocol you've never heard of
- 作者／機構:Dan Goodin, Ars Technica
- 連結:https://arstechnica.com/security/2026/10/vulnerability-in-agents-from-google-and-others-exposes-structural-flaw-in-mcp/

#MCP #PromptInjection #AIAgents #AgentSecurity #ModelContextProtocol #CyberSecurity #LLMSecurity #AIInfrastructure #Google #EnterpriseAI
