---
title: "vercel-labs/agent-browser"
source: GitHub Trending
url: https://github.com/vercel-labs/agent-browser
score: 101
model: tencent/hy3-preview:free
generated_at: 2026-04-23T20:03:59.351963
---

📌 【Vercel Labs 推出】agent‑browser：讓 AI Agent 直接「開車」上網的 Rust CLI  

你以為 AI 只能在本地跑文字模型？現在只要一行指令，就能讓生成式 AI 直接在 Chrome 裡點、滑、抓資料——完全不需要自己寫 Selenium 或 Playwright！  

🤔 **AI 想上網卻被瀏覽器卡住？**  
傳統的瀏覽器自動化往往需要繁雜的 Node.js 生態、額外的驅動程式，且效能不佳。Vercel Labs 把 Rust 的原生速度與 Chrome‑for‑Testing 的官方渠道結合，打造出「agent‑browser」這把「AI 上網」的鑰匙。  

🧪 **一鍵安裝、即刻使用**  
- **全局安裝（推薦）**：`npm install -g agent-browser` → `agent-browser install`（首次自動下載 Chrome for Testing）  
- **專案本地**：`npm install agent-browser` → 於 `package.json` script 中調用  
- **macOS Homebrew**：`brew install agent-browser`  
- **Rust Cargo**：`cargo install agent-browser`  
- **從原始碼編譯**：`git clone … && pnpm install && pnpm build && pnpm link --global`  

> **注意**：在 Linux 上可加上 `--with-deps` 讓指令自動安裝系統依賴，升級則用 `agent-browser upgrade`，工具會自動偵測你是 npm、Homebrew 還是 Cargo 安裝方式。  

💡 **核心功能一覽**  
- **原生 Rust 執行檔**：啟動即秒回應，遠超 Node.js 版的 Puppeteer/Playwright。  
- **自動下載官方測試版 Chrome**：避免版本不匹配的煩惱，已支援 Chrome、Brave、Playwright、Puppeteer 的現有安裝偵測。  
- **CLI 即插即用**：可在 `package.json` scripts、CI/CD pipeline，甚至直接在終端機呼叫，讓 AI Agent 只要輸入「在 https://example.com 點擊 #login」就能完成。  
- **跨平台支援**：macOS、Linux、Windows（透過 npm / Cargo）皆可安裝。  

⚠️ **目前的限制**  
- 只支援 Chrome for Testing（官方自動化頻道），若需要其他瀏覽器仍須自行配置。  
- 仍在 early‑stage，文件以安裝指令為主，缺乏完整的 API 範例或高階腳本範例。  
- 需要 Rust 環境才能從原始碼編譯，對非 Rust 開發者稍有門檻。  

🎯 **實務建議：把 AI Agent 當成「自動化腳本生成器」**  
1. **快速原型**：在開發生成式 AI 服務時，先用 `agent-browser` 讓模型直接抓取網頁資訊或填寫表單，省去自行寫 Selenium。  
2. **CI/CD 整合**：將 `agent-browser` 加入測試流程，讓 AI 驗證網站變更（例如驗證 SEO、A/B 測試結果）自動化。  
3. **成本控制**：相較於雲端瀏覽器服務，使用本機 Chrome for Testing 完全免付費，適合資源受限的開發團隊。  

🔗 **原始專案**  
📝 **repo**：vercel-labs/agent-browser  
👤 **作者**：Vercel Labs  
🔗 **GitHub**：https://github.com/vercel-labs/agent-browser  

🚀 你的 AI 代理人已經準備好「上網」了嗎？快試試看，然後在留言告訴我它幫你完成了什麼任務！  

#AI #Agent #BrowserAutomation #Rust #VercelLabs #CLI #ChromeForTesting #DevOps #生成式AI #自動化 #開源工具
