---
title: google-antigravity/antigravity-sdk-python
source: GitHub Trending
url: https://github.com/google-antigravity/antigravity-sdk-python
score: 97
model: google/gemma-4-31b-it:free
generated_at: '2026-07-05T19:30:03.823760'
---

📌 Google 推出 Antigravity SDK：將 AI Agent 的執行基礎設施抽象化

TL;DR：提供一套 Python SDK，讓開發者專注於 Agent 行為設計，而非底層執行邏輯。

開發 AI Agent 時，最令人頭痛的往往不是定義 Agent 要做什麼，而是如何處理狀態管理、建立可擴充套件的基礎設施以及管理複雜的 Agentic Loop。Google 這次推出的 Antigravity SDK 正是為了簡化這套流程。

🧩 **將執行基礎設施抽象化，專注於 Agent 行為**

Antigravity SDK 是一個專為 Antigravity 與 Gemini 設計的 Python SDK。其核心理念是提供一個安全、可擴充套件且具備狀態（stateful）的基礎設施層。

透過將「Agent 如何執行」的複雜度進行抽象化，開發者不再需要從零開始建構 Agentic Loop，而能將開發重心轉移到「Agent 應該執行什麼任務」的邏輯設計上。

⚙️ **快速部署與環境設定**

由於該 SDK 依賴於編譯後的執行時二進位檔（compiled runtime binary），因此不能單純透過 Clone 儲存庫來執行，必須透過 PyPI 安裝以獲取對應平臺的 wheel 檔：

`pip install google-antigravity`

**快速啟動流程：**
1. 設定 API 金鑰：`export GEMINI_API_KEY="your_api_key_here"`
2. 執行範例程式：`python ./examples/getting_started/hello_world.py`

💡 **整合 Gemini Enterprise Agent Platform (原 Vertex AI)**

對於企業級使用者，該 SDK 支援與 Gemini Enterprise Agent Platform（原 Vertex AI）整合。開發者只需在 `LocalAgentConfig` 中將 `vertex` 引數設為 `True`，並指定 GCP 專案與位置即可。

**實作範例：**
```python
from google.antigravity import Agent, LocalAgentConfig

config = LocalAgentConfig(
    vertex=True,
    project="your-gcp-project",
    location="us-central1",
)

async with Agent(config) as agent:
    response = await agent.chat("Hello!")
    print(await response.text())
```
*註：使用此模式前，需先透過 `gcloud auth application-default login` 完成本地身分驗證。*

🎯 **實務啟示**

對於 AI 工程師而言，這套 SDK 的價值在於「降低進入門檻」。如果你正打算在 Gemini 生態系中建構具有狀態且需大規模部署的 Agent，使用這套 SDK 可以省去自行設計基礎設施層的時間，快速從原型（Prototype）進入開發階段。

🔗 **來源**
- 標題：google-antigravity/antigravity-sdk-python
- 作者／機構：google-antigravity
- 連結：https://github.com/google-antigravity/antigravity-sdk-python

#AI #AIAgents #Python #Google #Gemini #VertexAI #SDK #SoftwareEngineering #LLM #CloudComputing
