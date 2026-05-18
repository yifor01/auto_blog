---
title: "rohitg00/agentmemory"
source: GitHub Trending
url: https://github.com/rohitg00/agentmemory
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-05-18T20:29:31.486496
---

📌 **AgentMemory：AI 程式記憶，不再重複解釋**  

你厭煩每次都要重新說明需求？這個工具讓你的程式碼AI記住一切。  

🤔 **工具背景：程式輔助AI需要持續記憶**  
隨著 Claude Code、Cursor、Gemini CLI 等 AI 輔助編程工具成為日常，開發者常常要在同一個會話中重複說明同樣的需求或上下文。缺乏長期記憶會導致效率下降與重複溝通的成本。  

🧪 **如何實作：npm 安裝與跨代理連線**  
- 全域安裝：`npm install -g @agentmemory/agentmemory`  
- 啟動記憶伺服器：`agentmemory`（預設監聽 :3111）  
- 連線特定代理：`agentmemory connect claude-code`（同樣支援 codex、cursor、gemini-cli 等）  
- 無需安裝即可體驗：`npx @agentmemory/agentmemory`（首次運行會提示全域安裝）  
專案提供 Quick Start、Benchmarks、vs Competitors、Agents、How It Works、MCP、Viewer、iii Console 等章節，方便開發者快速上手與評估。  

🧠 **核心發現：持續記憶、信心評分與知識圖譜**  
- 建構於 **iii engine**，延伸 Karpathy 的 LLM Wiki 模式。  
- 新增 **confidence scoring**（信心評分）、**lifecycle management**（生命週期管理）與 **knowledge graphs**（知識圖譜）。  
- 採用 **hybrid search**（混合搜尋），讓記憶內容能被快速檢索與更新。  
- 所有支援的代理共用同一記憶伺服器，實現跨工具的知識共享。  

🔍 **深入分析：為何這樣的設計能減少重複解釋**  
傳統的 LLM 互動僅依賴當前 prompt 的上下文，一旦對話切換或會話結束，先前的資訊就會遺失。AgentMemory 把每次互動的結構化知識（程式片段、設計決策、錯誤訊息等）寫入持續存儲的知識圖譜中，並伴隨信心分數標記可靠度。當使用者再次提出相關問題時，系統會先從記憶層檢索高信心的相關節點，減少需重新說明的需求。  

⚠️ **目前限制：早期階段與代理相依性**  
- 專案仍處於早期發布階段，功能與穩定性可能隨版本更新而變動。  
- 記憶功能依賴於目標代理是否支援 hooks、MCP 或 REST API；未支援的工具無法直接受益。  
- 目前未見大規模實務基準數據，效果需由開發者自行驗證。  

🎯 **實務建議：適合想減少重複溝通的開發團隊**  
- 若你的團隊正在使用 Claude Code、Cursor、Gemini CLI 等支援的代理，可先執行 `agentmemory demo` 觀察樣本 session 的回憶效果。  
- 在日常工作流程中，將常用的函式庫使用說明、除錯步驟或架構決策存入記憶，之後直接呼叫即可取得一致的回答。  
- 透過信心評分功能，可辨識哪些記憶仍需驗證，避免過度依賴可能過時的知識。  

🔗 **專案連結**  
📂 **GitHub**：https://github.com/rohitg00/agentmemory  
👤 **作者**：rohitg00  
🏷️ **標籤**：#AI #CodingAgent #Memory #ClaudeCode #Cursor #GeminiCLI #開發工具  

你有試過讓程式碼AI「記住」過去的對話嗎？歡迎在留言區分享你的使用經驗或改進建議 👇
