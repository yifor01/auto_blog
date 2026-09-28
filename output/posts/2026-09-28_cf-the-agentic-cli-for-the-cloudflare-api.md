---
title: 'Cf: The Agentic CLI for the Cloudflare API'
source: Hacker News
url: https://blog.cloudflare.com/cloudflare-cf-cli-launch/
model: claude-code/sonnet
generated_at: '2026-09-28T22:43:11.548896'
score: 96
---

📌 Cloudflare 為 Agent 打造全新 CLI：cf 正式登場

TL;DR：Cloudflare 推出 agent 優先設計的 cf CLI，把 Wrangler 的 280 個操作擴展到涵蓋 3,000 多個 API。

一個數字很能說明問題：今年三月，Agent 使用 Wrangler 的比例是四分之一，上週已經衝到 48%，而且 Agent 每天使用的指令種類幾乎是人類的兩倍，用到六個以上指令的機率更是人類的四倍。Cloudflare 觀察到這個趨勢後，沒有選擇在既有的 Wrangler 上疊加功能，而是直接推出一套從頭為 Agent 設計的新 CLI，cf。

🤔 **Wrangler 的天花板：280 個操作 vs. 3,000+ 個 API**

Wrangler 是由各產品團隊各自手工打造指令組合起來的，各團隊在命令設計上缺乏統一標準，於是出現像 `d1 info`、`hyperdrive get`、`workflows describe` 這種用詞不一致的狀況；有些團隊甚至為單一功能寫了數千行客製化程式碼，結果使用率極低。更根本的問題是，Wrangler 累積多年也只涵蓋約 280 個指令路徑，而 Cloudflare 的 API 總共有超過 3,000 個操作，兩者之間有巨大的落差。

🧩 **靠 Forge 直接從 API schema 產生 CLI**

Cloudflare 內部的統一 API 產生管線 Forge 是這次擴張的關鍵：既有的每個 API 都已有 OpenAPI schema 用於產生官方文件與 SDK，只要在 schema 上補上一點額外標註，Forge 就能把它直接轉成 CLI 指令。這讓 cf 能一口氣把涵蓋範圍從 Wrangler 的約 280 個功能，擴展到整個 Cloudflare API 的 3,000 多個操作，理論上能讓 Agent 用同一套工具設定 Worker、部署、監控、用 Cloudflare Access 保護、購買網域、再用 WAF 保護前端，一路串起來。

cf 內建了幾個目前僅少數 CLI 具備的 Agent 導向設計。首先是 `cf cli search`：面對 3,000 條可能的指令路徑，Agent 可以用自然語言描述需求，讓內建的小型搜尋索引根據 API 說明與參數找出對應指令，Agent 第一次執行 `--help` 時系統就會自動告知這個功能的存在。第二是把 JSON 定為預設輸出介面，人類看到的是美化排版，Agent 拿到的是精簡格式以節省 context；相較之下，Wrangler 只有部分指令支援 `--json`，很多指令回傳的是為人類設計的 Unicode 表格，Agent 得額外花時間與 token 去解析。第三是新的設定格式 `cloudflare.config.ts`，以 TypeScript 為基礎，讓 Claude Code、Codex 這類支援 LSP 外掛的 Agent 能直接讀懂設定檔的結構並給出更準確的建議；Cloudflare 內部有些 Wrangler 設定檔透過改用可程式化定義環境（而非逐一複製貼上 env 區塊），從超過 5,000 行壓縮了 40%。這套設定格式也搭配 Vite 成為預設的本地開發伺服器，並附上一套外掛組合。

💡 **推翻重來，反而比漸進升級更乾淨**

Cloudflare 在文中提出一個值得注意的判斷：多年的文件、部落格與第三方教學已經被吸收進 LLM 的訓練資料裡，這對 Wrangler 是資產，但也是包袱，因為任何重大改動都會與模型「學到」的既有行為衝突。相較之下，直接推出一套 Agent 從未見過的新 CLI，搭配設計好的 context 注入與 AGENTS.md 檔案，反而比讓 Agent 去釐清同一工具新舊版本間的差異更簡單。

⚠️ **仍在 Open Beta 階段**

cf 目前以 open beta 形式推出，可透過 `npm i -g cf` 全域安裝並在任何地方執行；新的 TypeScript 設定格式目前從 Workers 開始支援，尚未涵蓋 Cloudflare 全部產品線。

🎯 **實務啟示**

如果團隊已經讓 Agent 自動化操作 Cloudflare 資源，cf 的 `cli search` 與 JSON-first 設計能明顯減少 Agent 摸索指令與解析輸出所花的 token；而 TypeScript 設定格式對於想讓 Agent 安全地編輯基礎設施設定的團隊，也提供了比 TOML、JSONC 更可靠的型別檢查基礎。

🔗 **來源**
- 標題：Cf: The Agentic CLI for the Cloudflare API
- 作者／機構：macleos（Hacker News 提交）
- 連結：https://blog.cloudflare.com/cloudflare-cf-cli-launch/

#Cloudflare #CLI #AgenticAI #DeveloperTools #API #Wrangler #TypeScript #DevOps #AIAgents #CloudInfrastructure
