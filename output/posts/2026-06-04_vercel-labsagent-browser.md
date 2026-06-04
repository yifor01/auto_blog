---
title: vercel-labs/agent-browser
source: GitHub Trending
url: https://github.com/vercel-labs/agent-browser
score: 98
model: tencent/hy3-preview:free
generated_at: '2026-06-04T20:47:10.800966'
---

**Vercel Labs 發布 agent-browser**  
你有沒試過讓 AI 自己操作瀏覽器？現在只要一行指令，就能呼叫一個用 Rust 寫成的瀏覽器自動化工具。  
但它與現有的 Playwright、Puppeteer 有什麼不同？

🤔 **專為 AI Agent 工作流而生**  
AI 需要程式化地開啟頁面、填寫表單、截圖或執行腳本。傳統的瀏覽器自動化庫雖功能完整，但在 agent 場景中常需要額外封裝才能獲得乾淨的 CLI 介面。vercel-labs 團隊直接以 Rust 實作了一個可執行二進位的 CLI，目標是讓開發者在腳本或 CI 中一行指令即可啟動受控瀏覽器。

🧪 **安裝與使用方式多元**  
- **npm 全域安裝**：`npm install -g agent-browser`，隨後 `agent-browser install` 會自動下載 Chrome for Testing。  
- **Homebrew (macOS)**：`brew install agent-browser`，同樣執行 `agent-browser install` 取得瀏覽器。  
- **Cargo (Rust)**：`cargo install agent-browser`，再執行 `agent-browser install`。  
- **原始碼編譯**：需 Node.js 24+、pnpm 11+ 與 Rust，透過 `pnpm install`、`pnpm build` 與 `pnpm build:native` 完成編譯，最後 `pnpm link --global` 讓指令全域可用。  
所有安裝路徑在首次執行 `agent-browser install` 時會處理 Chrome 的下載與相依性，Linux 系統可加上 `--with-deps` 參數自動安裝所需的系統函式庫。

🚀 **核心特色：原生 Rust 二進位 + 零設定 Chrome**  
- 以 Rust 編譯得到的原生二進位，啟動速度與資源佔用優於基於 Node.js 的套件。  
- 內建偵測機制：若已安裝 Chrome、Brave、Playwright 或 Puppeteer，會自動複用；否則會從 Chrome for Testing 取得專用於自動化的版本。  
- 作為 CLI，可以直接在 `package.json` scripts 中呼叫，或在任何 Shell 脚本中使用，適合 CI/CD、本地腳本或 agent 框架的直接調用。

🔍 **與既有方案的比較觀察**  
功能上與 Playwright、Puppeteer 大致相同，都提供頁面導航、元素互動、截圖等能力。agent-browser 的差異在於：  
1. **交付形式**：提供單一可執行檔，減少版本鎖定與套件衝突的困難。  
2. **安裝流程**：一條 `agent-browser install` 指令即完成瀏覽器取得，免除手動指定執行檔路徑。  
3. **語言生態**：以 Rust 寫成，適合已經在 Rust 工具鏈中的專案；同時仍支援 npm、Homebrew、Cargo 等多種安裝管道，降低跨語言採用門檻。

⚠️ **目前已知的限制**  
- 文件僅說明了基本安裝與使用方式，未提供效能基準或與特定版本的 Playwright/Puppeteer 的詳細對照數據。  
- 專注於 Chrome 系列瀏覽器，Firefox 或 Safari 的支援情況未在說明中提及。  
- 作為新專案，社區生態（插件、範例、中文文件）仍在建置中，可能需要自行適配某些進階功能。

🎯 **實務建議**  
- 若你正在構建需要瀏覽器互動的 AI agent（例如自動化測試、資料爬取、網頁操作示範），可先嘗試全域安裝後在腳本中使用 `agent-browser run <your-script>` 來快速驗證流程。  
- 對於已經投入 Playwright 或 Puppeteer 的專案，可將 agent-browser 作為備用方案評估其啟動時間與部署簡單度是否符合你的 CI 需求。  
- 關注專案的 Release 與 Issue，以了解未來是否會擴充多瀏覽器支援或提供更細微的設定選項。

🔗 **資源連結**  
📂 GitHub：https://github.com/vercel-labs/agent-browser  
📦 npm：`npm install agent-browser`  
🍺 Homebrew：`brew install agent-browser`  
🦀 Cargo：`cargo install agent-browser`  

你有試過用這種方式讓 AI 操作瀏覽器嗎？歡迎在留言區分享你的使用經驗或遇到的挑戰 👇

#VercelLabs #agent-browser #Rust #瀏覽器自動化 #AIagent #CLI #開發工具
