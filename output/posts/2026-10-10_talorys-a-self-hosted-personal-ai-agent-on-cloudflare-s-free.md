---
title: Talorys – A self-hosted personal AI agent on Cloudflare's free tier
source: Hacker News
url: https://github.com/rociiu/talorys
model: claude-code/sonnet
generated_at: '2026-10-10T20:40:53.341424'
score: 84
---

📌 Talorys：一條指令，在自己的 Cloudflare 帳號裡跑出私人 AI agent

TL;DR：開源專案 Talorys 讓你在 Cloudflare 免費額度內部署專屬 AI 助理，資料全部留在自己帳號裡。

多數 AI 助理產品都要你把對話、記事、行程交給第三方伺服器保管。Talorys 的做法是反過來：你的 Cloudflare 帳號就是整套服務的全部基礎設施，開發者本身連一臺伺服器都不需要經手。

🤔 **解決什麼問題：不想再把個人資料交給別人的伺服器**

Talorys 是一個免費、開源的個人 AI 助理，完全在使用者自己的 Cloudflare 帳號內運作，沒有 Talorys 開發者操作的伺服器、資料庫或帳號系統。README 強調它的設計哲學是「一個人、一個 Cloudflare 帳號、一行指令」，就能擁有自己的 AI agent。它可以聊天、記住重要事項、管理任務／筆記／專案，並依排程執行提醒與自動化流程。

🧩 **架構：全部跑在 Cloudflare 的 Serverless 堆疊上**

根據 README 的架構說明，整個系統的資料流是這樣的：
1. 瀏覽器透過 HTTPS 連到使用者自己的 Cloudflare Pages 網站（React 前端 + `/api` Pages Function）。
2. Pages Function 透過 service binding（而非公開網址）把請求轉給一個私有的 Worker（以 Hono 作為路由框架）。
3. 該 Worker 呼叫 Cloudflare Agents SDK 的 Durable Object（`TalorysAgent`）。
4. Durable Object 內建 SQLite，儲存對話、記憶、任務、筆記、專案、自動化排程、session、設定與使用量；呼叫 Workers AI 的 `@cf/zai-org/glm-4.7-flash` 模型做串流與工具呼叫；排程提醒則交由 Durable Object 的 alarm 機制處理，不需要任何服務常駐在線上。

這個 agent Worker 部署時關閉了 `workers_dev` 與 `preview_urls`，因此沒有公開網址，所有驗證與授權邏輯都在 Worker 端完成，而不是前端；聊天回應則透過 Server-Sent Events 全程串流。整套方案只用到 Cloudflare Pages、Workers、Durable Objects（SQLite）與 Workers AI，這些都在免費方案涵蓋範圍內，不會用到 R2、D1、KV、Vectorize、AI Search 或 Workflows 等付費服務。

🧩 **怎麼用：npx 一行指令部署**

安裝方式是執行 `npx create-talorys@latest`。安裝程式會檢查 Node.js 版本（需 20.18 以上）、確認 Cloudflare 登入狀態（或開啟授權頁面）、讓使用者選擇帳號與 agent 名稱，並設定一個擁有者密碼（本機以 PBKDF2-SHA256 雜湊後，僅以 Cloudflare secret 形式儲存）。接著它會部署私有 Worker（同時建立 SQLite Durable Object）、建立並部署 Pages 專案與 service binding，最後驗證部署是否正常並印出真實的 `*.pages.dev` 網址。安裝資訊會寫入本機的 `talorys/` 目錄（含安裝 id、帳號 id、資源名稱、網址，但不含任何密碼），用於之後的更新。若安裝中途中斷，重新執行同一指令即可接續，不會產生重複資源或刪除既有資料。README 也提供了非互動式安裝的環境變數寫法，方便寫進自動化腳本。日常更新則用 `npx create-talorys@latest update`，密碼與 session 會被保留，資料庫 schema 遷移會自動且在交易中完成。

⚠️ **適用場景與限制**

Talorys 是單使用者設計，沒有多人帳號或團隊協作的概念；若 Workers AI 當日免費額度用盡，聊天功能會顯示明確提示並在每日額度重置後恢復，但任務、筆記、記憶與提醒等核心功能不受影響，因為簡單提醒與每日摘要本來就不會呼叫 AI。README 也提醒，Cloudflare 免費方案的額度（請求數、Durable Object 用量、每日 AI 用量）由 Cloudflare 自行設定且可能變動，因此「免費」並非「無限」；若帳號本身是付費方案，超出額度的部分仍會依方案計費。專案內建可調整的保護機制，包括最大輸出 token 數、最大上下文 token 數、每次請求的工具呼叫與推理步數上限，以及每日 AI 請求與排程 AI 執行次數上限。

🎯 **實務啟示**

對想要「完全掌控自己資料」又不想維運伺服器的工程師，Talorys 提供了一個可快速驗證的範本：用 Durable Object 做狀態持久化、用 alarm 做排程、用 service binding 隔絕公開端點。這個架構模式本身也值得參考，套用到其他需要「免維運、資料自主」的小型 agent 專案上。該專案在 Hacker News 上獲得 206 點與 105 則留言，顯示社群對這種部署模式有相當高的興趣。

🔗 **來源**
- 標題：Talorys – A self-hosted personal AI agent on Cloudflare's free tier
- 作者／機構：rociiu, Hacker News
- 連結：https://github.com/rociiu/talorys

#Cloudflare #OpenSource #AIAgent #SelfHosted #DurableObjects #ServerlessAI #WorkersAI #PersonalAssistant #EdgeComputing #HackerNews
