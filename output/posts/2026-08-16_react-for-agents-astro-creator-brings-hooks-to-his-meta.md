---
title: 'React for Agents: Astro Creator Brings Hooks to his Meta-Harness, Flue'
source: Latent Space
url: https://www.latent.space/p/flue-2
model: claude-code/sonnet
generated_at: '2026-08-16T06:07:53.687986'
score: 93
---

📌 Astro 之父打造 Flue 2：把 React Hooks 搬進 Agent 框架

TL;DR：Astro 創辦人 Fred Schott 推出 Flue 2，用 React 風格的 Agent Hooks 讓 agent 能在執行時動態改變自己。

Agent 開發框架還處在早期階段，而這次的關鍵轉折是：Flue 的創辦人一度以為自己在打造「Agent 版的 Astro」，後來才意識到，真正該做的其實是「Agent 版的 React」。

🤔 Agent 框架還在「jQuery 時代」，Flue 想當 React

Vercel 的 eve 與 Fred Schott 的 Flue 都在今年推出，被視為 agent 開發框架的早期範本。Schott 正是 web 框架 Astro 的創辦人，這也促成他的公司在今年 1 月被 Cloudflare 收購。他剛發布 Flue 2，是第一個穩定版本，核心基礎是 React 風格的「Agent Hooks」。Sierra CEO、同時也是 OpenAI 董事長 Bret Taylor 先前曾提到，業界「還在摸索誰是 reactive agents，陪審團還沒有結論……我們還處在 agent 的 jQuery 時代，而不是 React 時代」，這篇報導正是延續這個討論脈絡。

🧩 Agent 是一個函式，每個回合都重新渲染

在 Flue 裡，一個 agent 被表示成一個 JavaScript 函式，這個函式會「在每個回合重新渲染」，也就是在每次呼叫模型之前都重新執行一次。Hooks 以 TypeScript 撰寫，Flue 2 內建 16 個 hooks，包括 useSkill()、useTool()、useSubagent()，開發者也可以自行加入自訂 hooks。根據 Flue 2 的發布文章，這些 hooks「讓你打造能管理自身狀態、監聽 agent 生命週期事件，甚至在執行時動態附加不同資源與能力的動態 agent」。Schott 表示，這對打造「真正的客服機器人、真正的分流機器人」是必要的，因為這類 agent 沒辦法事先完全設定好，必須即時根據使用者需求或情境調整自己，例如一個客服 agent 可能要先驗證使用者身份，才能動態掛載帳戶管理工具。

Flue 的核心概念之一是 harness：agent 必須處在一個能取得完成任務所需情境與能力的環境裡。Schott 的說法是，「不是你和你的程式碼驅動 LLM、用腳本告訴它該做什麼，而是把 agent 放進這個 harness，讓它自己驅動自己去解決問題」。Flue 建構在開源、極簡的 harness 專案 Pi 之上，Flue 2 的 hosted agent 則改用開源建構工具 Vite 打造，Schott 把 Pi 在 Flue 中扮演的角色，類比為 Vite 之於 Astro 的基礎地位。

💡 從「五個檔案五條路由」到「整家公司就是一個 Agent」

Schott 對框架設計的想法演變得很快。今年 5 月初發布的 Flue 1，直接把 web 框架的 file-based routing 概念搬了過來，設想把五個 agent 放進五個檔案，對應五條路由。但 Flue 的早期使用者，尤其是較大型的客戶，反饋的模式是：他們整家公司就是一個 agent，根本不在乎路由。這個回饋讓 Schott 把重心轉向 composability（可組合性），也把他重新帶回 React 的思路，這也是 Flue 2 API 更接近 React、而非 Astro 或 Next.js 那套 routing 概念的原因。

Schott 認為 eve 是 Flue 最直接的競爭對手，兩者幾乎同時出現，也都把 harness 當作內建的核心設計。相對地，他把 Vercel AI SDK、Cloudflare Agents SDK，以及由打造 Gatsby 團隊開發的 Mastra，歸類為「OG agent 框架」——這些框架誕生時並未把 harness 當作核心概念，如今雖然也在補上 harness，但屬於後加的功能，而非 Flue、eve 從一開始就內建的設計。對於 Databricks 的 Omnigent、具備自我改進能力的 Exo harness 這類「meta-harness」討論，Schott 認為業界對這個詞本身還沒有共識；他也玩過 Exo，覺得很有意思，但認為用一套 API 橫跨所有 harness 反而會讓 Flue 的定位變得模糊，因為框架與 harness 在 Flue 裡是緊密綁在一起的。

值得一提的是，Flue 專案最初只是 Astro 程式庫裡的一個 issue 分流系統，一開始是一個由 LLM 驅動的腳本或工作流程，用來審閱 issue，後來逐漸具備在程式庫中執行動作的能力，才從單純的自動化，演變成想把「Claude Code 的體驗」headless 化、可託管、可雲端執行的野心，harness 作為核心概念的想法也是在這個階段成形。

主機可攜性（host portability）是 Flue 的核心原則之一。儘管 Schott 能借助僱主 Cloudflare 的工具與基礎設施，他強調 Flue 是「給每一種 host 使用的開源框架」，並希望保持這一點；他也提到 Vercel 已經展示過 Flue agent 同樣能部署在 Vercel 上。至於 LangChain 新推出的 Managed Deep Agents 這類託管 agent 平臺，Schott 表示目前管理型 agent 產品並不在 Flue 的路線圖上。

🎯 實務啟示

如果你正在打造需要即時調整能力的 agent 產品，例如客服或分流機器人，Flue 2 的 Hooks 模式提供了一個具體參考：用可組合的 hooks 管理狀態與動態掛載工具，而不是把所有邏輯寫死在事前設定裡。更大的訊號是，agent 框架正從「routing 優先」轉向「harness 優先」的設計哲學，這對評估要採用哪套框架、或是否該在既有 SDK 上補一層 harness，都是值得納入考量的判斷依據。

🔗 來源
- 標題：React for Agents: Astro Creator Brings Hooks to his Meta-Harness, Flue
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/flue-2

#AgentFramework #ReactForAgents #Flue #Astro #Cloudflare #AIAgents #DeveloperTools #OpenSource #AgentHooks #TypeScript
