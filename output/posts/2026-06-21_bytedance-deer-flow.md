---
title: bytedance/deer-flow
source: GitHub Trending
url: https://github.com/bytedance/deer-flow
score: 122
model: google/gemma-4-31b-it:free
generated_at: '2026-06-21T19:47:15.944445'
---

📌 【ByteDance 開源】DeerFlow 2.0：整合子代理與沙箱的 Super Agent 框架

TL;DR：ByteDance 推出的開源 Super Agent 框架，透過協調子代理、記憶體與沙箱實現複雜任務自動化。

當 LLM 從單純的對話轉向執行複雜任務時，單一模型往往難以處理長路徑的推理與執行。ByteDance 這次推出的 DeerFlow 試圖透過一個「超級代理（Super Agent）」的架構，將研究流程模組化，讓 AI 能像人類研究員一樣進行深度探索。

🧩 **協調子代理與沙箱的 Super Agent 架構**

DeerFlow (Deep Exploration and Efficient Research Flow) 的核心設計在於它不只是一個單一的 Agent，而是一個「框架 (Harness)」，其運作邏輯包含：

- **子代理協調 (Sub-agents Orchestration)**：將複雜任務拆解並由多個子代理協同完成。
- **記憶體與沙箱 (Memory & Sandboxes)**：提供記憶體儲存與沙箱環境，確保執行過程的可控性與連續性。
- **可擴展技能 (Extensible Skills)**：透過可擴展的技能集，讓 Agent 能執行多樣化的操作。

💡 **2.0 版本採取完全重寫，與 v1 毫無關聯**

值得開發者注意，DeerFlow 2.0 是一個從零開始的全新重寫版本 (Ground-up rewrite)，與 v1 版本沒有共用任何程式碼。原有的 Deep Research 框架目前維護在 1.x 分支，而所有的主開發進度已全面移至 2.0。

🛠️ **工程實作與整合建議**

對於想要部署 DeerFlow 的工程師，README 提供了以下技術路徑：

- **推薦模型**：作者強烈建議使用 Doubao-Seed-2.0-Code、DeepSeek v3.2 以及 Kimi 2.5 來驅動框架。
- **部署選項**：支援 Docker（推薦方式）或本地開發環境部署。
- **外部整合**：
    - **搜尋與爬蟲**：整合了由 BytePlus 開發的智慧搜尋與爬蟲工具集 InfoQuest。
    - **追蹤與監控**：支援 LangSmith 與 Langfuse 進行 Tracing 追蹤。
    - **擴展能力**：支援 MCP Server 與 IM Channels 整合。

🎯 **實務啟示**

對於開發 AI Agent 的工程師來說，DeerFlow 的設計體現了目前「深度研究 (Deep Research)」的趨勢：不再依賴單一 Prompt，而是建立一套包含「記憶體 $\rightarrow$ 技能 $\rightarrow$ 沙箱執行 $\rightarrow$ 監控」的完整管線。如果你需要構建能執行實際操作而非僅是生成文字的 Agent，研究其子代理協調機制與沙箱整合方式具有很高的參考價值。

🔗 **來源**
- 標題：bytedance/deer-flow
- 作者／機構：ByteDance
- 連結：https://github.com/bytedance/deer-flow

#ByteDance #OpenSource #AIagent #SuperAgent #DeepResearch #LLM #Docker #LangSmith #DeepSeek #MCP
