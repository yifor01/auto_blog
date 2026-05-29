---
title: "ryoppippi/ccusage"
source: GitHub Trending
url: https://github.com/ryoppippi/ccusage
score: 101
model: tencent/hy3-preview:free
generated_at: 2026-05-29T21:00:15.711409
---

📌 **ccusage：AI 編程助手用量統計**

你有沒好奇，每天用 AI 編程助手真的花了多少錢？  
當 Copilot、Claude Code、Gemini CLI 等工具成為日常，token 消費與成本卻往往看不見、摸不著。

🤔 **開發者需要一個統一的使用量視圖**  
各家 coding agent CLI 都有自己的使用紀錄，但分散在不同目錄、格式不一，難以快速彙總出每日、每週、每月的 token 消費與估算費用。缺乏這樣的可觀測性，會讓團隊在預算控制與成本優化時盲目操作。

🧪 **從本地資料讀取、多來源支援的 CLI 工具**  
ccusage 直接讀取各支援 coding agent CLI 在本機產生的使用紀錄，無需額外伺服器或雲端服務。目前支援的來源包括：Claude Code、Codex、OpenCode、Amp、Droid、Codebuff、Hermes Agent、pi‑agent、Goose、OpenClaw、Kilo、Kimi、Qwen、GitHub Copilot CLI、Gemini CLI 等。  
使用方式極簡：  
- `bunx ccusage`　　顯示所有偵測到來源的每日報表（預設）  
- `bunx ccusage daily / weekly / monthly / session`　　依時間切分彙總  
- 亦可透過 `nix run github:ryoppippi/ccusage -- daily`、`pnpm dlx ccusage`、`npx ccusage@latest` 等方式快速啟動，甚至提供離線預覽版本的安裝指令。

💡 **即時取得成本洞察，無需改變現有工作流程**  
因為 ccusage 只讀取本地已有的使用紀錄，對現有的 coding agent CLI 沒有任何侵入性。開發者可以在終端機直接查看：  
- 某一天的總 token 數與估算花費  
- 各來源的佔比（例如 Claude Code 佔 45%、Copliot 佔 30%）  
- 每週或每月的趨勢變化  
這些資訊有助於快速判斷哪些助手使用頻率最高、哪些時段成本突升，進而做出訂閱調整或使用策略的決策。

⚠️ **僅限於已有本地紀錄，無法產生未追蹤的使用資料**  
ccusage 的依賴點是各 coding agent CLI 必須在本機留下使用日誌。若某工具未將 token 使用寫入檔案，或使用者已清除該紀錄，ccusage 無法從中抓取資料。此外，工具目前不提供雲端匯總或即時推播功能，所有報表均基於本地檔案的掃描結果。

🎯 **適合需要成本可視化的個人開發者與團隊**  
- 若你正在評估多個 AI 編程助手的費用效益，可直接比較各來源的 token 用量。  
- 團隊領導可將 ccusage 加入 CI/CD 或開機腳本，產出定期使用報告作為成本控制的參考。  
- 因為安裝與使用皆指令列式，幾乎不需要額外設定，適合快速試驗與長期監控。

🔗 **專案連結**  
🛠️ github.com/ryoppippi/ccusage  
📖 文件與使用範例見專案 README  

你是否已經開始監控 AI 編程助手的花費？歡迎在留言區分享你的觀察與使用經驗 👇

#AI #CodingAssistant #TokenUsage #CostMonitoring #GitHubTrending #ccusage #開發工具 #LLM #開源專案
