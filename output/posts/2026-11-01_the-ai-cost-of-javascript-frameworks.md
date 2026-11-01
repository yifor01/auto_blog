---
title: The AI cost of JavaScript frameworks
source: Hacker News
url: https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/
model: claude-code/sonnet
generated_at: '2026-11-01T21:20:49.351769'
score: 82
---

📌 實測 12 種 JS 框架讓 AI 寫同一個網站，花費差了快一倍

TL;DR：用 Opus 5.5 agent 分別以 12 種 JS 框架建同一個 app，花費從 2.67 美元到 4.97 美元不等。

前端圈的框架之爭，長期以來靠的是「感覺」：這個框架「飛快」，那個工具能「supercharge」生產力，卻很少有人真的拿出數據。進入 agentic 時代後，開發者改口說某框架「更適合 agent 寫」，但同樣沒人問過 agent 本人的意見，也沒人附上 benchmark。於是部落客 Nolan Lawson 自己動手做了一個實驗。

🤔 **前端圈又在比「感覺」，這次換成 agent 的感覺**

作者長期觀察到，前端社群的技術選型常常是 vibes-based：React 的虛擬 DOM「很快」之類的說法，多半是先有偏好、後補理由。進入 AI 寫程式的時代，這種論述模式並沒有消失，只是把「開發者的手感」換成了「agent 寫起來比較順」。他好奇這類說法到底有沒有數據支撐，於是設計了一套可重複驗證的測試。

🧩 **用同一份規格，讓 agent 分別用 12 種框架蓋同一棟房子**

實驗設計分成幾步：先用 PokéAPI 設計一個中等複雜度的 Pokémon 查詢應用（含搜尋、篩選等功能，內容偏靜態、互動性不高，比較像 Wikipedia 而非 Figma 或 Gmail）；接著指示 Opus 5.5（high effort）分別用 Next.js、Nuxt、SvelteKit、Astro、Qwik、TanStack Start、SolidStart、React Router、Angular、Hono+htmx、Gracile+Lit 以及原生 Vanilla JS 建同一個 app，並要求各框架使用官方提供的 MCP 或 skill；最後用一套基於 accessibility tree（而非原始 DOM 結構）的 conformance suite 驗收，避免 agent 投機取巧，也因為部分框架用 web components 搭配 shadow DOM，無法硬性規定 HTML 結構。每個框架都跑 5 次取中位數（Angular 因兩次跑出無法測量的結果，部分指標只取 3 次），過程中不告知 agent 之後會被 Lighthouse 測效能與無障礙分數，CSS 方面禁用 Tailwind、Bootstrap 等元件框架，只給一組設計 token。

📊 **花費差了快一倍，SvelteKit、Angular 意外墊底**

以下為 5 次執行的花費中位數（美元，依官方 API 計價）：

| 框架 | 花費中位數（美元） |
|---|---|
| Hono+htmx | 2.67 |
| Astro | 2.76 |
| Nuxt | 2.82 |
| Vanilla | 2.98 |
| Next.js | 3.14 |
| Qwik | 3.27 |
| TanStack Start | 3.54 |
| SolidStart | 3.79 |
| React Router | 3.81 |
| SvelteKit | 4.28 |
| Gracile+Lit | 4.65 |
| Angular | 4.97 |

最便宜的 Hono+htmx 與最貴的 Angular 之間相差近一倍。作者也坦承變異度很大：React Router 的中位數比 Hono+htmx 貴了約 1 美元，但 React Router 最便宜的一次（2.82 美元）仍低於 Hono+htmx 最貴的一次（3.19 美元）。不過幾個規律仍然穩定出現：SvelteKit、Gracile+Lit、Angular 明顯比其他框架貴。作者推測，SvelteKit 的 agent 在每次執行時都會去讀 SvelteKit v3 的 migration guide，可能是因為版本太新、不在 Opus 5.5 的訓練資料裡；Gracile 則是因為 agent 不熟悉這個框架，常常直接 clone 原始碼或去讀 node_modules 裡編譯後的原始碼；Angular 偏貴則與其程式碼總量有關。

💡 **官方 MCP／skill，其實沒多少 agent 真的拿來用**

作者也記錄了各框架的 MCP／skill 實際使用率，結果相當分散：React Router 的 skill 在 5 次執行中都被用到，Hono 的 skill 也是 5/5；但 Nuxt 的 MCP 一次都沒被用過，Next.js 的 skill 檔案只在 1/5 次執行中被讀取、AGENTS.md 只在 2/5 次中被讀取，TanStack Start 的 skill 檔案（藏在 node_modules 裡）也只在 2/5 次中被發現。作者認為這反而讓實驗更貼近真實情境，因為多數「vibe coding」的使用者不會特別去提醒 agent 要用 MCP，甚至根本不知道有這個選項。

⚠️ **這只是一種 app 類型的結果，且 LLM 本身就很隨機**

作者強調這不是一個完美實驗：測試的 app 偏內容型、互動性低，不代表所有應用場景；LLM 輸出本身具有隨機性，有時候某次執行會莫名其妙繞去做其他事、浪費大量 token，這與框架本身無關；Lighthouse 的測量結果也不穩定，例如 Largest Contentful Paint 這次判定某張圖是「最大元素」，下次測又換了另一張。多次執行取中位數有幫助，但無法完全消除這些雜訊。

🎯 **實務啟示**

在用「這個框架對 agent 更友善」當作技術選型理由之前，值得先問一句：有數據嗎？這份實驗至少證明，花費差異確實存在且和框架的「人氣排名」未必一致（SvelteKit、Angular 偏貴，Hono+htmx、Astro 反而便宜）；同時官方 MCP／skill 的採用率參差不齊，不能假設你裝了官方工具 agent 就一定會用。若團隊要評估「AI 友善度」作為框架選型依據，應該像作者一樣用可重複的 conformance suite 去驗收，而不是靠感覺。

🔗 **來源**
- 標題：The AI cost of JavaScript frameworks
- 連結：https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/

#JavaScript #WebDevelopment #AIAgents #Benchmark #React #SvelteKit #NextJS #Frontend #CodingAgents #LLM
