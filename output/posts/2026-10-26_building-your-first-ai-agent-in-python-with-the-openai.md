---
title: Building Your First AI Agent in Python with the OpenAI Agents SDK
source: KDnuggets
url: https://www.kdnuggets.com/building-your-first-ai-agent-in-python-with-the-openai-agents-sdk
model: claude-code/sonnet
generated_at: '2026-10-26T21:58:22.747488'
score: 74
---

📌 用 OpenAI Agents SDK 打造你的第一個 AI Agent

TL;DR：幾十行 Python 就能做出會搜尋、會算數、記得對話的 agent。

寫過 LLM 應用的人都知道那個固定流程：Prompt → Model → Response，問完就結束。但如果你想要模型自己判斷「這題需要先查資料」「這題需要呼叫函式算一下」,再回頭給答案呢？這正是 AI agent 與一般 LLM 應用的分野,而 OpenAI Agents SDK 把這個執行迴圈直接幫你寫好了。

🤔 **Agent 跟 LLM 應用差在哪**

一般 LLM 應用只有「輸入—模型—輸出」一條線。Agent 則多了工具（tool）跟執行迴圈：使用者提問後,agent 會判斷是否需要先採取行動（搜尋網路、呼叫 Python 函式、讀取記憶),再把結果交回模型,直到產生最終答案。SDK 裡的 `Runner` 就是負責跑完這整個迴圈的角色,會自動送出請求、執行工具呼叫、把結果餵回去,直到拿到最終輸出。

🧩 **三行程式碼接上網路搜尋**

安裝很簡單,`uv add openai-agents` 或 `pip install openai-agents`,設好 `OPENAI_API_KEY` 後就能寫：

```python
from agents import Agent, Runner, WebSearchTool

agent = Agent(
    name="Research Assistant",
    instructions="You are a concise research assistant. Use web search when current information is required.",
    tools=[WebSearchTool()],
)

result = Runner.run_sync(agent, "What are the latest developments in Python?")
print(result.final_output)
```

`WebSearchTool()` 是 OpenAI 代管的工具,模型自己決定什麼時候要查最新資訊,不用你手動接搜尋 API。文中範例實測能正確抓到當下的 Python 穩定版本資訊。

🧩 **用 `@tool` decorator 把自家函式變成工具**

真正讓 agent 有用的是能呼叫你自己的程式碼：

```python
from agents.decorators import tool

@tool
def calculate_total(price: float, quantity: int) -> float:
    """Calculate the total cost of an order."""
    return price * quantity
```

把這個函式丟進 `tools=[...]` 清單,SDK 會自動用函式名稱、型別提示（type hints）跟 docstring 生成工具的 schema,模型看得懂該怎麼呼叫,不需要你手寫 JSON schema。文中特別提醒：docstring 要寫清楚,因為模型靠它判斷「這個工具是做什麼的、什麼時候該用」。

🧩 **SQLiteSession 讓 agent 記得你剛才問過什麼**

加入 `SQLiteSession("user_1", "conversations.db")` 並在每次 `Runner.run_sync` 時傳入 `session`,agent 就會自動帶上之前的對話歷史,因此像「最新版本是哪個」這種需要承接上下文的問題也能正確回答。因為是檔案型 SQLite,重啟程式後歷史依然保留；SDK 也支援 Redis、SQLAlchemy、MongoDB 等 session 後端,方便擴展到正式環境。

📊 **四合一的完整範例**

把網路搜尋、自訂工具、持久記憶、基本錯誤處理、持續對話迴圈全部組起來,就是一個完整的小型對話式 agent。SDK 預設啟用 tracing,可以在 OpenAI dashboard 檢視每一步的模型呼叫、工具使用、handoff,對除錯「agent 為什麼選了這個工具」特別有幫助。

🎯 **實務啟示**

這套流程的重點不是打造一個複雜的自主系統,而是「給模型採取行動的能力,並讓 SDK 處理執行迴圈」。有了這個基礎,之後可以逐步加上 MCP server、guardrails、handoff、更多專門工具與多 agent 協作,架構的核心模式不變。

🔗 **來源**
- 標題：Building Your First AI Agent in Python with the OpenAI Agents SDK
- 作者／機構：Abid Ali Awan, KDnuggets
- 連結：https://www.kdnuggets.com/building-your-first-ai-agent-in-python-with-the-openai-agents-sdk

#AIAgent #OpenAI #Python #LLM #AgentsSDK #MCP #SoftwareEngineering #Tutorial #ConversationalAI #DeveloperTools
