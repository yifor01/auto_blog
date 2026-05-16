---
title: "How to Build an MCP Style Routed AI Agent System with Dynamic Tool Exposure Planning, Execution, and Context Injection"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/15/how-to-build-an-mcp-style-routed-ai-agent-system-with-dynamic-tool-exposure-planning-execution-and-context-injection/
score: 85
model: tencent/hy3-preview:free
generated_at: 2026-05-16T19:43:34.104052
---

📌 【MarkTechPost 教學】如何從零打造 MCP 風格的路由 AI Agent？

你是否好奇，讓 AI 代理不只是呼叫工具，而是能夠「依需求動態暴露」適當功能、規劃執行、並把工具輸出注入上下文？這篇來自 MarkTechPost 的逐手教學告訴你該怎麼做。

🤔 **為什麼需要 MCP 風格的路由代理？**  
隨著工具增多（網路搜尋、本地檢索、資料集載入、Python 執行等），單一代理若一次開放全部能力，易產生冗餘與安全風險。MCP（Model‑Control‑Planning）概念提出：先透過路由決策只暴露最小且有效的工具集，再由代理規劃、執行，最後把工具回饋注入上下文合成最終答案。這樣既能提升效率，又能讓系統更具可解釋性與可擴展性。

🧪 **教學實作步驟概覽**  
1. **環境準備**：安裝所需 Python 套件，載入 OpenAI API 金鑰並初始化客戶端。  
2. **結構化 schema 設計**：使用 Pydantic 定義工具規格、工具呼叫、路由決策、規劃輸出與工具結果，統一採用 MCP 風格的資料格式。  
3. **本地知識庫與檢索器**：建立小型文件集（解釋 MCP、動態能力暴露、上下文注入、路由政策、沙盒執行等），以 TF-IDF 實作本地檢索器，返回最相關片段與相似度分數。  
4. **工具伺服器**：實作模組化工具伺服器，對外提供網路搜尋、安全 Python 執行、資料集載入與本地向量檢索，每項能力皆經過結構化 schema 描述。  
5. **混合路由器**：結合啟發式規則與 LLM 推理，依當前任務動態決定應該暴露哪些工具，以達到「最小有效」的能力集。  
6. **代理規劃與執行**：代理先規劃工具使用順序，安全執行每項呼叫，然後將工具輸入注入上下文，最終合成答案。  
7. **實際演示**：透過數個真實任務（例如：網路資訊蒐集＋資料分析、本地檔案檢索＋腳本執行）展示系統如何在規劃、執行與上下文注入之間協同運作。

🔮 **核心展示**  
教學完整展示了從環境設定到端到端執行的完整流程，並提供可直接運行的程式碼片段。讀者可以看到：  
- 工具只有在路由器判斷需要時才會被暴露；  
- 代理能根據規劃結果決定下一步要呼叫哪個工具；  
- 工具執行後的結果會被注入上下文，使後續推論更具依據。  
這些實作展示證明了 MCP 原則（動態能力暴露、路由政策、上下文注入）在實際代理系統中的可行性。

💡 **關鍵洞見**  
- **混合路由的價值**：單靠啟發式規則可能過於死板，單純 LLM 推論則易產生幻覺；兩者結合能在效率與正確性間取得更佳平衡。  
- **上下文注入不是簡單拼接**：教學強調要將工具輸出結構化後，再依任務需求選擇性注入，以避免資訊噪聲。  
- **模組化工具伺服器的擴展性**：新增工具只需定義對應的 schema 並註冊到伺服器，無需改動路由或代理核心邏輯。

⚠️ **教學的限制**  
- 範例依賴 OpenAI API（或相容端點），若換用其他模型可能需要調整提示與參數。  
- 教學著重於實作流程與概念驗證，未提供大規模基準測試或正式效能評估。  
- 作者指出此為「MCP‑style」的實作，雖結合了既有想法（工具路由、上下文注入），但未主張提出全新演算法。  

🎯 **給開發者的實務建議**  
- 若你正在構建需要多工具協作的 AI 代理，可參考此教學先建立一個最小可執行版本（MVP），再逐步加入更複雜的路由政策或沙盒機制。  
- 在實務部署時，記得將工具執行放入沙盒或受限容器，以確保安全。  
- 利用結構化 schema（如 Pydantic）讓工具規格、呼叫與結果具有型別安全，這不僅減少除錯成本，也讓系統更易於未來擴展。  

🔗 **原始教學連結**  
📖 How to Build an MCP Style Routed AI Agent System with Dynamic Tool Exposure Planning, Execution, and Context Injection  
👤 Sana Hassan @ MarkTechPost  
🔗 https://www.marktechpost.com/2026/05/15/how-to-build-an-mcp-style-routed-ai-agent-system-with-dynamic-tool-exposure-planning-execution-and-context-injection/

你有試過讓 AI 代理自行決定要用哪些工具嗎？歡迎在留言區分享你的經驗或問題 👇

#AI #Agent #MCP #ToolRouting #ContextInjection #MarkTechPost #Tutorial #LLM #Python #AIEngineering
