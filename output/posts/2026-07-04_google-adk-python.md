---
title: google/adk-python
source: GitHub Trending
url: https://github.com/google/adk-python
score: 103
model: google/gemma-4-31b-it:free
generated_at: '2026-07-04T19:22:36.672792'
---

📌 【Google 開源】ADK 2.0：以 Code-First 為核心的 AI Agent 開發框架

TL;DR：Google 推出的 Python 框架，透過圖形化工作流與結構化任務委派，強化 AI Agent 的控制力與部署能力。

在 AI Agent 的開發過程中，如何在靈活性與可控性之間取得平衡？許多開發者面臨的問題是：純 Prompt 驅動的 Agent 過於隨機，而硬編碼的流程又太僵化。Google 釋出的 ADK (Agent Development Kit) 2.0 試圖透過「Code-First」的設計理念，讓工程師能精準定義 Agent 的行為與執行路徑。

🧩 **以圖形化執行引擎定義複雜工作流**

ADK 2.0 引入了 Workflow Runtime，將 Agent 的執行邏輯轉化為基於圖 (Graph-based) 的執行引擎。這讓開發者能建構確定性的執行流程，並支援以下進階功能：
- 路由 (Routing) 與 扇入/扇出 (Fan-out/Fan-in)
- 迴圈 (Loops) 與 重試機制 (Retry)
- 狀態管理 (State management) 與 動態節點 (Dynamic nodes)
- 人機協作 (Human-in-the-loop) 以及 巢狀工作流 (Nested workflows)

🧩 **結構化的 Agent 任務委派機制**

除了工作流，ADK 2.0 的 Task API 讓 Agent 之間的協作變得更結構化，支援多樣化的委派模式：
- 多輪對話任務模式 (Multi-turn task mode)
- 單輪受控輸出 (Single-turn controlled output)
- 混合委派模式 (Mixed delegation patterns)
- 允許將 Task Agents 直接作為工作流中的節點使用，並整合人機協作機制。

🚀 **快速上手與核心組成**

ADK 應用主要由兩個核心類別組成：`Agent`（定義 AI 的指令、工具與行為）與 `Workflow`（編排 Agent 與任務的圖形化流程）。

安裝方式簡單，僅需 Python 3.10+ 環境：
```bash
pip install google-adk
# 若需安裝擴充整合
pip install "google-adk[extensions]"
```

範例程式碼片段顯示，開發者可以快速定義 Agent：
```python
from google.adk import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.5-flash",
    instruction="You are a helpful assistant. Greet t..."
)
```

⚠️ **版本升級注意：1.x 與 2.0 的不相容性**

本次 2.0 版本包含重大變更 (Breaking Changes)，涉及 Agent API、事件模型 (Event model) 與 Session 結構 (Session schema)。
- ADK 2.0 產生的 Session 可由 ADK 1.28+ 讀取（多餘欄位會被忽略）。
- 但 2.0 的 Session 與更早期的 1.x 版本完全不相容。

🎯 **實務啟示**

對於需要高度可控性的企業級 Agent 應用，ADK 2.0 提供的圖形化工作流能有效降低 LLM 的隨機性。工程師可以將複雜的業務邏輯定義在 Workflow 中，而將具體執行交給 Agent，實現「邏輯確定，執行靈活」的開發模式。

🔗 **來源**
- 標題：google/adk-python
- 作者／機構：Google
- 連結：https://github.com/google/adk-python

#AI #Agent #Google #Python #LLM #Gemini #Workflow #OpenSource #SoftwareEngineering #AI_Agents
