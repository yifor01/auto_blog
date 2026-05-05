---
title: "bytedance/deer-flow"
source: GitHub Trending
url: https://github.com/bytedance/deer-flow
score: 133
model: tencent/hy3-preview:free
generated_at: 2026-05-05T19:35:26.265321
---

📌 【ByteDance 開源】DeerFlow 2.0：GitHub 衝上 #1 的 Super Agent 統合引擎

才宣佈 v2.0 上線，DeerFlow 就在 2 月底拿下 GitHub Trending 全站第一。這不是一次普通的功能更新，而是一次從零重寫的架構轉換：過去 Deep Research 框架的代碼已全數移至 1.x 分支，2.0 分支徹底捨棄舊碼，以 sub-agents、memory 與 sandboxes 為核心，重新編排成可擴充的 skill orchestration 層。

🤔 **從 Deep Research 到 Super Agent，架構邊界正在溶解**

過去幾年，長文本研究與多步驟推理任務往往依賴單一強大模型或靜態 RAG 流程；但當任務長度與工具依賴同時擴張，單體智能的邊際效益快速遞減。DeerFlow 的出現，正對應了這個轉折點：當「研究流程」本身需要被持續拆解、修正與重組時，工程架構必須先於模型能力升級。

🧪 **從零重寫的 2.0 分支，將 sub-agents、memory 與 sandboxes 統一為可擴充技能**

DeerFlow 2.0 捨棄 v1.x 既有代碼，以模組化方式重構執行環境。核心組件包含：

- Sub-agents：可動態啟動與回收的執行單位，負責特定研究階段（如檢索、驗證、摘要）  
- Memory：跨回合的狀態儲存與檢索機制，支持長期上下文維護  
- Sandboxes：隔離執行環境，避免污染與提升安全性  
- Skills：外掛式能力包，協調上述組件完成複合任務  

此外，專案強調與現有觀測與部署生態的整合，提供 Docker 快速部署、進階沙盒模式、MCP Server、IM 通道接入，以及 LangSmith 與 Langfuse 的雙 tracing 支持。

🐇 **在 GitHub 衝上 #1 的背後，是具體可落地的長期研究解法**

DeerFlow 並非停留在原型展示，而是直接提供：

- 單行 Agent 啟動流程與配置範本  
- 區分開發與量產的部署選項（Docker 與本地模式）  
- 對話平台與即時通道整合方案  
- 與 InfoQuest（BytePlus 開發的搜尋與爬蟲工具集）原生集成  

官方亦針對中國大陸開發者提供本地化接入建議，並推薦搭配 Doubao-Seed-2.0-Code、DeepSeek v3.2 與 Kimi 2.5 等模型運行完整流程。

🔍 **可擴充的 skill orchestration，才是多 Agent 系統的可維護性關鍵**

DeerFlow 的設計選擇揭示了一個清晰觀點：當系統需要長期與多工具互動時，決定性不應只交給模型提示詞，而是透過明確的 skill 介面與狀態機制進行調度。這種「模型負責推理，框架負責流程」的切分，有助於降低除錯成本、限制錯誤傳播範圍，並讓迭代更接近傳統軟體工程經驗。

⚠️ **從零重寫意味生態斷裂，長期穩定性仍需時間檢驗**

- v2.0 與 v1.x 代碼不互通，現有用戶需遷移或維護雙分支  
- 廣泛依賴外部模型與工具服務，跨區域穩定性受基礎設施影響  
- 多 Agent 調度在極長時間軸下的 memory 衰減與 drift 問題，尚未公開長期壓測數據  

🎯 **想跑通長期研究任務，先看技能拆分是否合理**

- 優先將「研究步驟」拆解為可測試的 skill，而非依賴端到端提示  
- 在沙盒中執行不可信代碼與外部呼叫，避免牽連主流程  
- 搭配 tracing 工具持續觀察調度路徑與 token 消耗，及早發現瓶頸  

🔗 **論文連結與開源資源**  
📦 Project: bytedance/deer-flow  
🌐 Repository: https://github.com/bytedance/deer-flow  
📄 Official Website & Demos: https://deer-flow.com  

你目前的多 Agent 架構是如何解決流程調度與長期記憶問題的？歡迎分享實戰經驗與踩坑筆記 👇

#ByteDance #DeerFlow #MultiAgent #OpenSource #AIResearch #LangChain #SoftwareArchitecture
