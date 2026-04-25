---
title: "MemoriLabs/Memori"
source: GitHub Trending
url: https://github.com/MemoriLabs/Memori
score: 99
model: tencent/hy3-preview:free
generated_at: 2026-04-25T19:13:04.303819
---

📌 **【MemoriLabs 新專案】不只記對話，這套框架記住 Agent 的「行為」**

還在為 AI Agent 的短期記憶漏接、長期記憶難以整合而苦惱嗎？大多數記憶系統只專注於處理對話文字，卻忽略了 Agent 在後端「做了什麼」。MemoriLabs 最新在 GitHub Trending 亮相的開源專案，試圖改變這個現狀。

🤔 **從「說什麼」到「做什麼」，記憶定義的典範轉移**

過去我們設計 Agent 記憶時，往往只關注 Chat History。但一個成熟的 Agent 在基礎設施中執行的操作、調用的 API、以及產生的副作用（Side effects），才是構成其長期智慧的關鍵。Memori 的核心邏輯很簡單：Memory from what agents do, not just what they say。這意味著它捕捉的是 Agent 的行為軌跡，而不僅僅是語言碎片。

🛠️ **零配置與框架無關，工程師的即插即用體驗**

這項工具的設計哲學是「無侵入性」。根據其架構描述，Memori 是 LLM、Datastore 和 Framework 無關的（Agnostic）。它不強迫你重寫架構，而是直接接入你現有的軟體與基礎設施。

對於開發者來說，最誘人的是其「Zero config」的雲端版本。只要設定 API Key，幾分鐘內就能開始構建。目前官方已提供 TypeScript 與 Python 雙語 SDK，降低了落地的門檻。

🧪 **自動化背景持久化，讓 Context 管理變透明**

看看這段 TypeScript 的 Quickstart 範例，你會發現開發者幾乎不需要手動處理記憶的讀寫：

```typescript
const mem = new Memori().llm.register(client).attribution('user_123', 'support_agent');

// 第一次對話，Memori 在背景自動持久化
await client.chat.completions.create({
  model: 'gpt-4o-mini',
  messages: [{ role: 'user', content: 'My favorite color is blue.' }],
});

// 第二次對話，Memori 自動召回背景資訊
const response = await client.chat.completions.create({
  model: 'gpt-4o-mini',
  messages: [{ role: 'user', content: "What's my favorite color?" }],
});
// 系統會自動 recall 並理解你的偏好顏色是藍色
```

這種將記憶層與 LLM 呼叫解耦的設計，讓開發者能專注於業務邏輯，而不必耗費心力在 Context Window 的管理上。

✨ **行為驅動記憶對多 Agent 系統的實質影響**

在多 Agent 協作的場景中，Agent A 的行為結果往往需要成為 Agent B 的上下文。Memori 提出的「行為記憶」架構，能有效解決跨 Agent 的狀態同步問題。當記憶不再只是文字，而是結構化的行為數據，Agent 的長期演化才真正成為可能。

⚠️ **早期階段，生態系整合待觀察**

目前該專案雖然已在 GitHub Trending 上獲得關注，但作為一個新興工具，其在大規模生產環境下的穩定性、對非 OpenAI 模型的支援細節，以及具體的效能開銷，仍需社群進一步驗證。

🎯 **如果你正在構建長期運作的 Agent，值得一試**

對於正在評估 Agent 記憶方案的架構師，Memori 提供了一個輕量且靈活的選項。特別是當你的系統已經有既有的 LLM 或資料庫選擇時，這種「無關性」的設計能省去大量的遷移成本。

🔗 **專案連結**
📝 Memori: Memory from what agents do
👤 MemoriLabs
🔗 GitHub: https://github.com/MemoriLabs/Memori
📚 文件: memorilabs.ai/docs/memori-cloud/

你覺得 Agent 的記憶應該基於對話還是行為？歡迎在留言區分享你的架構設計思路 👇

#AI #Agent #LLM #MemoryArchitecture #OpenSource #MemoriLabs #軟體工程 #GitHubTrending
