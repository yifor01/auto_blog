---
title: wonderwhy-er/DesktopCommanderMCP
source: GitHub Trending
url: https://github.com/wonderwhy-er/DesktopCommanderMCP
score: 88
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T09:50:10.683155'
---

📌 Desktop Commander MCP：把 AI 編輯、終端指令與檔案管理全收進同一個聊天介面

TL;DR：Desktop Commander MCP 讓開發者在聊天視窗中直接搜尋、編輯檔案、執行長時間終端指令，支援多種 AI 模型，且以本機客戶端訂閱取代 API 付費。

🎣 你是否常在 IDE、終端與 AI 助手之間切換，還要額外管理 API 金額？Desktop Commander MCP 把「聊天」變成完整的開發工作區，從檔案搜尋、即時預覽到遠端指令執行，都可以在同一個對話中完成，讓工作流更流暢。

🤔 為什麼需要「AI 聊天即開發環境」？

- 傳統 AI 編輯器只能在文字層面提供建議，無法直接在本機執行指令或即時預覽檔案變更。  
- 使用 API token 會產生不可預測的成本，尤其在長時間執行或大量檔案編輯時。  
- 開發者常需要同時開啟多個工具（IDE、終端、瀏覽器），切換成本高。

🧩 主要功能與架構概覽

- **多模型支援**：使用者可自行選擇 Claude、GPT‑4.5、Gemini 2.5 或任何支援的模型，完全不受單一服務商限制。  
- **即時檔案預覽**：AI 編輯檔案時，畫面會即時顯示變更的視覺預覽，讓使用者在聊天中直接看到結果。  
- **自訂 MCP 與上下文**：可自行加入自訂的 Model Context Protocol (MCP) 工具，無需編寫額外設定檔，即可擴充功能。  
- **遠端 AI 控制**：支援從 ChatGPT 等前端呼叫 Desktop Commander，實現遠端指令與檔案操作。  
- **長時間指令執行**：內建機制能在聊天介面中啟動、監控與管理長時間的終端指令，避免阻塞對話。  
- **Beta 桌面應用**：提供 macOS 與 Windows 版的 Desktop Commander App，將 MCP 伺服器功能完整搬到本機，體驗更流暢。  
- **未來規劃**：即將加入技能系統、語音輸入、背景排程任務等功能，持續擴大自動化範圍。

📊 安裝與使用快速上手

1. **下載 App**：從官方 GitHub 頁面取得 macOS 或 Windows 安裝檔。  
2. **執行 MCP 伺服器**：安裝後會自動啟動 MCP Filesystem Server，提供檔案搜尋與即時取代功能。  
3. **選擇 AI 模型**：在設定介面輸入欲使用的模型名稱（如 Claude、GPT‑4.5），系統即會以該模型回應指令。  
4. **開始聊天**：在聊天視窗輸入「搜尋 `utils.py` 中的 `parse_json`」或「執行 `npm run build`」等自然語言指令，AI 會自動呼叫 MCP 完成任務，並回傳結果或檔案預覽。  

⚠️ 目前仍在開發中，功能列表包含「Skills 系統」與「背景排程」等尚未完成的專案，使用時請留意官方檔案的 TODO 區段。

🎯 實務啟示

- **降低工具切換成本**：開發者可將日常的檔案搜尋、批次編輯與指令執行全部搬到聊天介面，減少在 IDE、終端與瀏覽器間的來回切換。  
- **成本可控**：因採用本機客戶端訂閱模式，避免了傳統 AI API 按使用量付費的波動，適合長時間或大量檔案操作的團隊。  
- **擴充彈性**：自訂 MCP 讓團隊可以把內部指令碼、CI/CD 工具或測試框架直接掛接到聊天介面，打造專屬的 AI 工作流。  

🔗 來源  
- 標題：wonderwhy-er/DesktopCommanderMCP  
- 作者／機構：wonderwhy-er  
- 連結：https://github.com/wonderwhy-er/DesktopCommanderMCP  

#AI #DesktopCommander #MCP #DeveloperTools #ChatOps #Automation #LLM #GPT4 #Claude #Gemini #Productivity #OpenSource
