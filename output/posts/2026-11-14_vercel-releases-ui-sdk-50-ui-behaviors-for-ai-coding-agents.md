---
title: 'Vercel Releases UI SDK: 50+ UI Behaviors for AI Coding Agents'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/13/vercel-ui-sdk-agent-ui-behaviors/
model: claude-code/sonnet
generated_at: '2026-11-14T21:38:29.540286'
score: 74
---

📌 Vercel UI SDK：把UI行為拆給Coding Agent自己組裝

TL;DR：Vercel開源UI行為庫，讓coding agent自己拼裝出無障礙元件。

如果你請AI agent幫你做一個Select下拉選單，它給你的常常是寫死、沒有鍵盤導航與ARIA屬性的半成品。Vercel Labs想解決的正是這個問題：不是給agent一個做好的元件，而是給它拼積木的材料。

🤔 為什麼不直接給agent一個現成元件？

Vercel UI SDK是一套開源beta版的headless函式庫，提供的是UI「行為」而非做好的元件。官方網站用Select舉例：你不會直接把一個現成的Select元件交給agent，而是給它一個popup、一個selection model，以及typeahead這些行為單元。同一批行為單元，可以拼成autocomplete、combobox，甚至是「目前還沒有人設計過的元件」。

🧩 Primitive、Slot與跨框架的Parts，同一套行為餵5種框架

所有行為都放在@ui-sdk/core這個核心套件，再由各框架的輕量adapter負責渲染。元件的起點是用definePrimitive定義的primitive，裡面宣告state、API與slots；slot再把屬性、事件與行為綁到對應的DOM部件上。README範例示範了一個搜尋欄位，用createFocusRecovery處理焦點回復，裡面的清除按鈕只在有輸入文字時才出現。接著每個框架透過createParts渲染同一份primitive，README強調這些parts在React、Vue、Svelte、Solid、Web Components五種adapter裡都是一樣的，也就是同一份行為定義可以同時服務React跟Svelte專案。目前文件把行為分成10大類，從Focus、Keys到Canvas都有，預先做好的元件則包括Select、Combobox、Date Picker、Menu、Tree與Color Picker。

💡 讓agent在執行時「看懂」頁面

除了開發期的行為拼裝，UI SDK還附上一個執行期的agent橋接：用createAgent()在頁面渲染前建立橋接後，agent可以呼叫agent.snapshot()列出目前頁面上有哪些元件、它們的狀態與可執行的action，再用agent.act()直接執行動作（例如呼叫setValue重新命名一個project）。應用端可以傳入一個allow callback來核准或拒絕agent的動作，change callback也會收到source: "agent"的標記，讓開發者能在agent觸發變更時選擇取消。SDK也支援透過WebMCP把這些工具註冊給相容瀏覽器使用。

📊 一個任務的對照實驗，官方自己說只能當方向參考

Vercel拿自己的agent橋接跟browser tools做了一個project-settings任務的比較：agent要重新命名一個project、更新成員與通知設定，再存檔，兩邊都用Claude Code跑Sonnet，用同樣的任務與system prompt，取3次執行的中位數。但這個比較的樣本只有1個任務，而且browser tools那一邊用的是不同的元件庫，Vercel自己也提醒這些數字只能當方向性參考，官方也沒有公開是哪一個Sonnet版本。

⚠️ 還是0.1.0-beta，且peer依賴版本卡得很新

目前全部6個套件都是0.1.0-beta.1版本，於2026年11月12日發布，採Apache-2.0授權。peer依賴要求也不低：React 19+、Vue 3.5+、Svelte 5.33+、Solid 2.0.0-rc.14+，導入前得先確認專案框架版本跟得上。

🎯 跟React Aria、Zag.js比，差異在agent那一層

把行為跟markup拆開的做法，React Aria的hooks跟Ark UI的Zag.js機制早就在做。UI SDK真正不同的地方，是額外疊上的agent層：npx skills add vercel-labs/ui --skill ui-sdk這個skill、打包好的llms.txt說明文件，以及上面提到的執行期橋接。對正在建立coding agent工作流的團隊來說，這代表可以不用自己重造一套「讓agent讀懂UI狀態並安全執行動作」的機制。

🔗 來源
- 標題：Vercel Releases UI SDK: 50+ UI Behaviors for AI Coding Agents
- 作者／機構：Michal Sutter（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/11/13/vercel-ui-sdk-agent-ui-behaviors/

#Vercel #UISDK #CodingAgents #WebDevelopment #React #Svelte #Vue #OpenSource #AccessibleUI #AIAgents
