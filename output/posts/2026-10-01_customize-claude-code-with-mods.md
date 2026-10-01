---
title: Customize Claude Code with mods
source: Claude Blog
url: https://claude.com/blog/claude-code-mods
model: claude-code/sonnet
generated_at: '2026-10-01T21:57:22.349094'
pinned: true
---

📌 Claude Code 推出 mods：用 TypeScript 客製化你的 AI 編碼工具

TL;DR：Anthropic 推出 mods，讓開發者用幾行 TypeScript 改寫 Claude Code 的行為與介面，甚至不用等官方出新功能。

如果你覺得 Claude Code 某個內建功能不合用，以前只能等官方更新；現在你可以自己動手改，甚至請 Claude Code 自己寫一個 mod 來改自己。

🤔 **為什麼需要 mods**

開發者一直要求對 Claude Code 有更多掌控權，而不必等 Anthropic 出新功能。Hooks（鉤子）曾部分滿足這個需求，但 hooks 無法重寫事件、畫新的 UI，或取代既有功能，mods 可以做到這些事。Anthropic 表示，在正式推出前已先在 GitHub 公開設計草案收集開發者意見。

🧩 **運作原理：掛在事件上的 TypeScript 函式**

Claude Code 每做一個動作都會送出一個事件（event），例如呼叫工具、要求權限，或繪製畫面的一部分。mod 就是掛在某個事件上的函式，可以選擇在事件「之前」執行、「之後」執行、「取代」事件本身，或「包住」事件（前後都執行一段程式碼）。

用一個函式，mod 能做到的事包括：
- 在 prompt 送進模型前重寫它
- 封鎖、重寫或重試某次工具呼叫
- 核准或拒絕一次權限請求
- 在 Claude 讀取工具輸出前，把裡面的機密資訊遮蔽掉

mod 也能改變畫面本身：編輯或取代 Claude Code 畫出的介面元件（像是工具結果或 Claude 提出的問題），還能加上按鈕與輸入欄，讓其他 mod 對這些互動做出回應。目前 mod 可以把目標設定為終端機、桌面版 App，或兩者同時套用。當多個 mod 掛在同一個事件上時，會依載入順序依序執行：最先載入的 mod 最先看到事件，也最後看到結果，這讓不同作者寫的 mod 可以彼此疊加使用。

甚至可以讓 Claude Code 自己改自己：只要請 Claude 寫一個 mod，它就能寫出對應的 TypeScript、安裝它，並在目前的 session 中熱重載（hot reload）。

🧩 **內建功能也開始陸續換成 mods**

舉例來說，內建的 `/diff` 功能現在本身就是一個 mod，所以可以在 `/plugin` 裡把它關掉，或換成自己寫的版本。Anthropic 表示，未來會把更多內建功能陸續改寫成 mods，讓 Claude Code 能縮減成一個精簡的核心，再由使用者自行加回想要的功能。

💡 **團隊與企業端的管控機制**

因為 mods 是包在 plugin 裡發行，既有的 plugin 管控機制同樣適用。Team／Enterprise 方案中，擁有者可在管理後臺允許或封鎖 plugin marketplace；在 Claude API 或第三方 API 方案中，則由管理者把 managed settings 推送到使用者的機器上。

在 Team／Enterprise 方案，以及任何套用了 managed settings 的機器上，一個名為 `sec-default`（安全預設）的內建 mod 會最先載入，用來阻止使用者自行安裝的 mod 做出高風險行為，例如覆寫權限的拒絕規則；其原始碼可供查看，確認它實際限制了哪些行為。管理者如果想讓自己的 mod 優先載入，需記得把 `sec-default` 加進清單，才能保留它的限制效果。

團隊也能用 mods 打造自己的控制與功能，例如：在對話旁顯示 CI/CD pipeline 狀態的面板、要求任何觸及 production 設定的指令都需先確認的安全護欄，以及由最先載入的 mod 記錄其他所有 mod 呼叫行為的稽核紀錄。

⚠️ **沒有沙箱隔離，只裝信任的來源**

mods 擁有與 Claude Code 本身相同的機器存取權限，並未被沙箱隔離。官方明確提醒：只應該安裝來自信任來源的 mod，就像在電腦上安裝其他任何程式一樣謹慎。

🎯 **客製化與安全治理可以並存**

對重度使用 Claude Code 的工程師，mods 把過去只能靠 hooks 做局部調整的範圍，擴大到改寫 prompt、攔截工具呼叫、客製化 UI 等更深層的行為；而企業情境下 `sec-default` 與 managed settings 的設計，說明「開放客製化」與「集中治理」可以同時成立，這是導入團隊協作前值得先摸清楚的兩端。

🔗 **來源**
- 標題：Customize Claude Code with mods
- 作者／機構：Anthropic
- 連結：https://claude.com/blog/claude-code-mods

#ClaudeCode #Anthropic #AI #DeveloperTools #TypeScript #AIAgents #SoftwareEngineering #DevEx #Plugins #CLI
