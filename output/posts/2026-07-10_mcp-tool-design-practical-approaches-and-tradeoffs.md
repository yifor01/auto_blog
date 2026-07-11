---
title: 'MCP tool design: Practical approaches and tradeoffs'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/mcp-tool-design-practical-approaches-and-tradeoffs/
score: 96
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T08:10:13.056898'
---

📌 【AWS 技術分享】MCP 工具設計：別讓 API 直接暴露給 LLM，小心 context 崩潰

TL;DR：MCP 工具失效通常源於設計而非協議，核心在於平衡「定義膨脹 (Bloat)」與「模型混淆 (Confusion)」。

許多開發團隊在整合 Model Context Protocol (MCP) 時，習慣將現有的 API 原封不動地暴露給 Agent，並寄望 LLM 能自行理解如何呼叫。這種做法在簡單場景可行，但在複雜系統中，往往會導致工具呼叫失敗、引數錯誤，甚至陷入不斷重試的惡性迴圈。

🤔 **工具失效的根源：不是協議問題，而是設計問題**

當 MCP 工具表現不佳時，問題通常出在「工具設計」而非協議本身。直接將 API 對映為工具雖然快速，但忽略了 LLM 與 Agent 系統的運作邏輯。缺乏針對性的設計會導致模型在呼叫時產生錯誤，進而浪費 context 並降低整體效能。

🧩 **兩大核心挑戰：膨脹 (Bloat) 與混淆 (Confusion)**

作者指出，大多數 MCP 工具的失敗可歸結為以下兩個問題：

- **定義膨脹 (Bloat)**：無論工具是否被使用，所有的工具定義在每次呼叫時都會載入到 LLM 的 context 中。當連線多個 MCP 伺服器時，在使用者提出問題前，context 可能就已被大量定義佔滿，導致模型的推理能力下降，降低對話生產力。
- **模型混淆 (Confusion)**：隨著推理能力因膨脹而下降，LLM 更容易做出錯誤選擇，例如呼叫錯誤的工具或填入錯誤引數。而後續的重試（Retries）會進一步增加 context 負擔，加劇膨脹問題。此外，工具間的語義相似度過高、選項過多或命名模糊，都會增加混淆風險。

💡 **上下文工程 (Context Engineering) 的權衡難題**

為了降低「混淆」，常見的解決方案是強化工具描述，加入更清晰的定義、自然語言對映或使用範例。雖然這能幫助模型更精準地選擇工具，但這也帶來了新的矛盾：

**增加描述 $\rightarrow$ 緩解混淆 $\rightarrow$ 增加定義長度 $\rightarrow$ 加劇膨脹 $\rightarrow$ 降低推理能力 $\rightarrow$ 再次導致混淆**

這形成了一個惡性迴圈，導致 Agent 做出非預期選擇，且 context 消耗速度超出預期，使對話 session 迅速失效。

🎯 **實務啟示：將工具設計視為上下文工程**

設計 MCP 工具不應僅是 API 的延伸，而是一場「上下文工程 (Context Engineering)」的實踐。工程師必須精確控制 LLM 在什麼時間點看到什麼資訊，而非一次性提供所有定義。在設計時需在「提供足夠資訊以減少混淆」與「保持精簡以避免膨脹」之間取得平衡，才能確保模型產出更高品質的結果。

🔗 **來源**
- 標題：MCP tool design: Practical approaches and tradeoffs
- 作者／機構：Daniel Wells @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/mcp-tool-design-practical-approaches-and-tradeoffs/

#MCP #LLM #Agent #ContextEngineering #AWS #APIDesign #GenerativeAI #PromptEngineering #SoftwareArchitecture #ModelContextProtocol
