---
title: tirth8205/code-review-graph
source: GitHub Trending
url: https://github.com/tirth8205/code-review-graph
score: 84
model: tencent/hy3:free
generated_at: '2026-07-18T07:38:20.767355'
---

📌 【開源專案】code-review-graph：用結構地圖讓 AI 審 code 不再狂燒 token

TL;DR：建構程式碼結構圖並經由 MCP 提供精準上下文，減少 AI 重讀整個程式庫。

🎣 開場鉤子
AI 程式碼審查工具在 review 任務中，往往反覆重新讀取整個程式碼庫的大半內容。這不只是慢，還在默默燒掉你的 token 配額。

🤔 為什麼 AI 審 code 會浪費 token
README 指出，常見的 AI coding 工具在執行 review 相關任務時，會重複讀取程式碼庫中很大一部分的檔案。作者宣稱 code-review-graph 就是為了解決這個問題而做：讓 AI 助手只讀「真正有關係」的程式碼。

🧩 核心設計：Tree-sitter 建圖 + 增量追蹤 + MCP
這個專案的做法是：
- 用 Tree-sitter 為你的程式碼建立結構化地圖（structural map）
- 增量（incrementally）追蹤程式碼變更，不需要每次全量重解析
- 透過 MCP（Model Context Protocol）把精準上下文送給 AI 助手，讓它只讀必要的部分

支援多語系檔案（英文、簡體中文、日文、韓文、印地語），並提供 Usage、Commands、FAQ、Troubleshooting、GitHub Action 等說明檔案。

🎯 怎麼用：一條指令完成安裝與設定
README 提供的最小可行流程如下：
1. 安裝：`pip install code-review-graph`（或 `pipx install code-review-graph`）
2. 自動配置：`code-review-graph install` → 自動偵測你已安裝的 AI 編碼工具，為每個工具寫入正確的 MCP 配置，並在支援的平臺上安裝原生 hooks/skills，同時把 graph-aware 指令注入平臺規則
3. 建圖：`code-review-graph build` → 解析你的程式碼庫
4. 重啟編輯器或工具讓配置生效

`install` 會自動判斷你是用 `uvx` 還是 `pip` / `pipx` 安裝，產生對應配置。若只想針對單一平臺設定，可加 `--platform` 參數，例如：
- `code-review-graph install --platform codex`（僅配置 Codex）
- `code-review-graph install --platform cursor`（僅配置 Cursor）
- `code-review-graph install --platform claude-code`（僅配置 Claude Code）
- `code-review-graph install --platform gemini-cli`（僅配置 Gemini CLI）
- `code-review-graph install --platform kiro`（僅配置 Kiro）
- `code-review-graph install --platform copilot`（僅配置 Copilot）

🎯 實務啟示
如果你日常用 AI 助手做 code review，且專案程式庫偏大、token 成本明顯，可先試這套工具：一條 `install` 指令就能把 MCP 與平臺設定搞定，不需要手動改配置。讓 AI 拿到結構化上下文，比直接丟整包程式碼更省、更準。

🔗 來源
- 標題：tirth8205/code-review-graph
- 作者／機構：tirth8205
- 連結：https://github.com/tirth8205/code-review-graph

#CodeReview #AICoding #TreeSitter #MCP #TokenEfficiency #GitHub #OpenSource #DeveloperTools #CodebaseMapping #IncrementalParsing
