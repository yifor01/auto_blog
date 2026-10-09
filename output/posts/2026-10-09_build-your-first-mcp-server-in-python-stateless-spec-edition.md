---
title: Build Your First MCP Server in Python (Stateless Spec Edition)
source: KDnuggets
url: https://www.kdnuggets.com/build-your-first-mcp-server-in-python-stateless-spec-edition
model: claude-code/sonnet
generated_at: '2026-10-09T21:58:09.592931'
score: 93
---

📌 MCP 規範轉無狀態，Python 兩個檔案就能起一個伺服器

TL;DR：2026-07-28 版 MCP 規範拿掉了 session 機制，搭配 Python SDK v2 的 MCPServer API，寫 function 就能生出完整的工具、資源與 prompt 伺服器。

以前要串接 MCP，第一步永遠是處理 session：建立連線、維護 `Mcp-Session-Id`，確保每個請求都綁在正確的上下文裡。現在這一步直接消失了。

🤔 **為什麼突然不用管 session 了**

今年夏天發布的 2026-07-28 MCP 規範把協定核心改成了「無狀態」：客戶端不再需要先建立協定 session 才能發請求,伺服器端的一般請求也不再依賴 `Mcp-Session-Id`。這個改動的直接好處是 MCP 伺服器可以直接架在一般的 HTTP 基礎設施後面做水平擴充，不用額外處理 session 親和性（session affinity）的問題。同時，官方 Python SDK 也進到 v2 穩定版，提供了更高階的 `MCPServer` API，讓開發者用一般的 Python function 定義 tool、resource、prompt，不用自己寫 JSON Schema。

🧩 **一個 function 加一個 decorator，就是一個 MCP 介面**

教學示範建了一個小型「開發者知識庫」伺服器，暴露三個 MCP 原語：工具 `search_kb(query, limit)`、資源 `kb://articles`、prompt 模板 `draft_support_reply(customer_message)`。整支伺服器完全沒有使用者 session 狀態，每個請求都自帶所有需要的資訊,正好示範了新的無狀態模型。

核心設計理念很直白：

```python
from mcp.server import MCPServer

mcp = MCPServer(
    "Developer Support KB",
    instructions=(
        "Use the knowledge-base tools to answer support questions. "
        "Prefer retrieved KB information over guessing."
    ),
)
```

`MCPServer` 是目前 SDK 推薦給大多數場景使用的高階介面；SDK 另外保留了一個低階的 `Server` class，留給需要精確控制 schema、協定 metadata 或自訂方法的情境。

工具的定義完全靠型別提示（type hints）推導出來：

```python
@mcp.tool()
def search_kb(query: str, limit: int = 3) -> list[dict[str, str]]:
    """Search the support knowledge base."""
    ...
```

沒有手寫 JSON Schema、沒有手寫參數解析器。`query: str` 與 `limit: int = 3` 直接被 SDK 轉成 MCP 的 input schema，預設值讓參數在 schema 裡變成可選。換句話說，函式的簽章本身就是介面定義。

資源與工具的分工也很清楚：資源像是 GET，用來把資料讀進上下文；工具像是 POST，用來執行動作。

```python
@mcp.resource("kb://articles")
def list_articles() -> str:
    """Return the available knowledge-base articles."""
    ...
```

Prompt 則是給使用者或 host 主動呼叫的範本：

```python
@mcp.prompt()
def draft_support_reply(customer_message: str) -> str:
    """Create a prompt for drafting a concise support response."""
    ...
```

三者共用同一套 decorator 風格的伺服器介面，是這套 SDK 讀起來特別「平易近人」的原因。

💻 **從零到可連線只需要幾行指令**

專案建立用 `uv`：

```
mkdir first-mcp-server
cd first-mcp-server
uv init
uv add "mcp[cli]"
```

或用 pip 安裝 `mcp[cli]`（官方建議裝 CLI extra，因為它附帶開發指令與 MCP Inspector 工作流）。整個專案可以小到只有 `server.py` 和 `client.py` 兩個檔案，不需要額外框架樣板。寫完上述三個原語後，伺服器最後用：

```python
if __name__ == "__main__":
    mcp.run("streamable-http")
```

跑在 Streamable HTTP 上，就是一個可被外部連線的完整 MCP 應用。SDK 要求 Python 3.10 以上版本。

🎯 **實務啟示**

如果你的團隊已經在用 MCP 串接內部工具或知識庫，這次規範轉向無狀態是個很好的時機重新檢視架構：不用再為每個客戶端維護 session 生命週期，可以直接用一般的 HTTP 負載平衡與多副本部署來擴充 MCP 伺服器。而 Python SDK 的 decorator 模式也意味著，既有的業務函式只要補上型別提示，幾乎可以直接變成 MCP 工具，門檻比想像中低。

🔗 **來源**
- 標題：Build Your First MCP Server in Python (Stateless Spec Edition)
- 作者／機構：Kanwal Mehreen, KDnuggets
- 連結：https://www.kdnuggets.com/build-your-first-mcp-server-in-python-stateless-spec-edition

#MCP #Python #LLM #AIAgent #API #OpenProtocol #DeveloperTools #StreamableHTTP #SDK #AIEngineering
