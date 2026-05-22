---
title: "microsoft/agent-governance-toolkit"
source: GitHub Trending
url: https://github.com/microsoft/agent-governance-toolkit
score: 139
model: tencent/hy3-preview:free
generated_at: 2026-05-22T20:17:35.104972
---

📌 **微軟 Agent Governance Toolkit：零違規的 AI 執行管控**

你以為 AI 安全只要加個提示就夠了？實測顯示提示式安全有 26.67% 違規率，而這套工具卻做到 0%。

🤔 **隨著 AI 代理應用爆發，安全管控成為瓶頸**  
LangChain、CrewAI、AutoGen 等框架讓 AI 能自主呼叫工具、存取資源、與其他代理互訊。但若只靠「請遵守規則」的提示，模型仍有可能違反政策，導致安全風險與合規問題。

🧪 **多語言運行時政策執行層**  
Agent Governance Toolkit（AGT）在應用層插入一個決定性的 Policy Check：每一次工具呼叫、資源存取或代理間訊息都會在執行前根據 policy.yaml（或等效設定）進行允許/拒斥判斷，並即時寫入審計日誌。該檢查延遲 < 0.1 ms，支援 Python、TypeScript、.NET、Rust、Go 五種語言的 SDK。

🔍 **核心發現：紅隊測試中違規率驟降至零**  
- 提示式安全（「請遵守規則」）：在紅隊測試中 policy violation rate 為 **26.67%**  
- AGT 的應用層執行：同樣測試下 violation rate 為 **0.00%**  

這意味著，只要把政策寫入 AGT 的檢查點，理論上不會出現任何未經授權的工具呼叫或資源存取。

💡 **為何執行層能徹底阻斷違規？**  
- **決定性**：政策檢查發生在模型輸出之前，不依賴模型的自願遵守。  
- **可審計**：每次決策都會產生不可變的 audit log，便於事後追蹤與合規審查。  
- **低延遲**：<0.1 ms 的開銷幾乎不影響使用者體驗。  

⚠️ **目前為 Public Preview，可能在 GA 前有破壞性變更**  
- 需要特定版本依賴（Python 3.10+、Node.js 18+、.NET 8+、Go 1.25+、Rust 1.70+）  
- 文件標註「may have breaking changes before GA」，生產環境部署前請閱讀 changelog。  
- 未提供長期穩定性或大規模負載測試數據，僅基於紅隊測試的政策違規率給出。

🎯 **實務啟示：兩行程式碼即可獲得強制政策管控**  
```python
from agentmesh.governance import govern
safe_tool = govern(my_tool, policy="policy.yaml")   # 每次呼叫都會被檢查、記錄、執行
```
同樣方式適用於 TypeScript、.NET、Rust、Go，且已預先適配 LangChain、CrewAI、AutoGen、OpenAI Agents、Google ADK、Semantic Kernel、AWS Bedrock 以及 20+ 其他框架。工程師只需在專案中加入對應 SDK，定義 policy.yaml，即可獲得「執行時政策強制」的安全保證，無需再依賴脆弱的提示式安全。

🔗 **資源連結**  
- GitHub Repo：https://github.com/microsoft/agent-governance-toolkit  
- 文件 (Docs)：同 repo 中的 Docs 目錄  
- Quick Start：同 repo 中的 🚀 Quick Start  
- PyPI 包：`agent-governance-toolkit[full]`  
- Changelog：同 repo 中的 📝 Changelog  

你的 AI 代理是否仍在依賴「請遵守規則」的提示？試著把政策搬到執行層看看，或許能讓違規率歸零。歡迎在留言區分享你的實作經驗或疑問 👇

#AI #AgentGovernance #Microsoft #LangChain #CrewAutoGen #安全管控 #開發工具 #PyPI #TypeScript #DotNet #Rust #Go
