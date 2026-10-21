---
title: 'Claude Mods: Flipping the Harness Inside Out'
source: Latent Space
url: https://www.latent.space/p/claude-mods
model: claude-code/sonnet
generated_at: '2026-10-21T20:59:53.598880'
score: 92
---

📌 Claude Mods：把 Agent Harness 的方向反過來指向人

TL;DR：Claude Mods 讓使用者用程式碼自訂 Claude Code 何時打斷你、給你看什麼,是可程式化的「注意力介面」。

當模型把越來越多的「harness」能力吸收進權重裡,留給人類的那一層會變成什麼?Latent Space 這篇文章給出的答案是:它會變成決定 Agent 何時打斷你、給你看什麼、要你做哪些決策的「注意力介面」(Attention Interface),而 Claude Mods 正是這個介面第一個可以被使用者自己塑形的版本。

🤔 **從「Agent 對機器」到「Agent 對人」**

作者過去幾週用 Claude Mods 把 Claude Code 塑形成符合自己工作流的樣子。他指出,Agent harness 原本是 Agent 與其運行機器之間的介面:使用者下 prompt,Agent 送出指令、編輯檔案、呼叫工具。但現在,harness 正逐漸變成 Agent 與人之間的介面。Claude Mods 讓這個方向反過來:不再只是從 Agent 指向機器,而是從 Agent 指向人類操作者,harness 本身成為與人類注意力互動的介面。作者的判斷是,harness 終將成為一個平臺,讓其他公司在上面建構產品,模型則扮演引擎的角色——就像瀏覽器成為網頁應用程式的平臺一樣。

🧩 **Mod 是什麼：跑在 Claude Code 裡的 TypeScript／JavaScript 中介層**

一個 mod 是 Claude Code 的外掛,由跑在 Claude Code 內部的 TypeScript 或 JavaScript 函式組成,用來自訂 CLI 與桌面版介面的行為與外觀。Mods 會回應特定事件,例如一個 prompt、一次工具呼叫,或是一次介面渲染;它們可以觀察事件、修改渲染方式,或直接取代預設行為來處理事件。換句話說,Claude Mods 是 Agent harness 的中介層(middleware),透過注入程式碼來改變 Claude Code 在執行期的運作與渲染流程。使用者甚至可以要求 Claude 用自然語言描述想要的 mod,由 Claude Code 內建的技能來生成——Claude Code 自帶一個教它如何寫 mod 的技能。

Anthropic 自己已經內建出貨六個 mods,可透過 `/plugin` 指令在 Installed 底下的 Built-in 看到:
- agents-md:把 AGENTS.md 載入為專案指令
- diff:接管 `/diff` 指令並繪製其畫面
- plugin-authoring:提供 Claude 寫 mod 所需的技能
- sec-default:守護組織管理範圍,不受使用者安裝的 mods 影響
- telemetry:發送 Claude Code 與內建 mods 記錄的分析資料
- you-should-know:一個側邊 Agent,在 prompt 上方標註你可能忽略的重要資訊,是唯一預設關閉的一個

多數 mods 在背景默默運作,這意味著 Anthropic 本身有部分 Claude Code 功能就是以 mod 的形式建構的,包括使用者可能根本沒察覺到的部分。

💡 **實例：You Should Know 擋下了一次誤丟工作進度的風險**

作者唯一自己啟用的內建 mod 是 You Should Know。一個真實案例是:他要求 Claude Code 簡化某個個人專案裡冗贊的 UI 文字。主要 Agent 修剪了 Compare 畫面上的文案,安裝新版本,拍下前後對照截圖,看起來一切完成。但 You Should Know 隨後標記出一件事:被編輯的檔案 CompareView.swift 本身已有未提交(uncommitted)的工作,而且另外約 45 個檔案也是如此。如果之後丟棄這次示範性的編輯,連同那些尚未完成的早期工作也會一併被丟掉。它的建議是先 commit 或 stash 這些早期工作。這個 mod 只在某次回合編輯了檔案、執行了指令,或呼叫了 8 次以上工具後才會啟動;在作者展示的畫面中,一次就標記出六項值得注意的資訊。緊接著,一個名為 Next Steps Supervisor 的 mod 會建議下一步動作,以可點擊按鈕的形式,把該指令當成訊息送回 Claude Code。這個 mod 屬於作者自己打造的開源外掛 ModSmith,其中包含數個內建 mod,以及一套讓 Claude 能據此建構彼此協作的新 mod 的範本。

📊 **三家公司,三種「注意力介面」設計哲學**

作者把 Claude Mods 拿來跟另外兩個近期產品對照。OpenAI 在 10 月 7 日隨 GPT-6 推出 ChatGPT 的新介面 Intelligent UI,讓 ChatGPT 不只用文字回答,還能即時生成圖表、地圖、檢核清單、表單,甚至像分帳計算器、儲蓄計算器之類的小工具——這是一種生成式 UI(generative UI)。在 OpenAI 的範例中,ChatGPT 會用多選題式的追問來縮小使用者需求範圍。這也是一種注意力介面,只不過介面是模型逐次從 OpenAI 建好的元件庫裡挑選產生,目前發布時提到的唯一控制項是把視覺效果調低——作者認為這個功能的目標使用者並非工程師。

Cursor 的 PR Routing & Approval 則是從另一端處理同樣的問題:面對的不是一人一答,而是一個團隊和一串越來越多由 Agent 寫出的 pull request,需要有人決定哪些變更值得人類審查。這套系統依程式碼擁有權與提交歷史指派審查者,並能自動核准低風險 PR,判斷依據是風險分數與使用者設定的門檻、Cursor 的 Bugbot 與 Security 審查器的發現,以及存在於 repo 中的政策檔。作者特別注意到一條規則:如果一個 PR 本身修改了核准政策,Agent 不會用那個被修改過的版本來放寬對這個 PR 自己的審查,而是改讀 base branch 裡的政策——這代表 Agent 無法透過改規則來讓自己的 PR 過關。Cursor 的文件也明白指出,這項功能「不能取代完整的程式碼審查」。

三者的差異在於:誰有權設計這個注意力介面。ChatGPT Intelligent UI 是模型在實驗室建好的框架內,逐次回答自行設計介面,零設定但控制權有限;Cursor PR Routing & Approval 是團隊寫政策,由一套固定的審查流程去執行,可配置但互動流程由 Cursor 決定;Claude Mods 則是使用者與 Agent 一起用程式碼,親手打造介面本身。

🎯 **實務啟示**

如果你的團隊已經重度依賴 Claude Code 處理日常工程任務,與其等待官方介面滿足所有需求,不如把 Claude Mods 當成客製化「什麼值得我注意」的工具來投資——像 You Should Know 這種攔截未提交變更的機制,對多人協作、多分支並行的工作流特別實用。對工具鏈設計者而言,這篇文章也提出一個值得思考的方向:當模型能力持續被吸收進權重,團隊與使用者之間的差異化價值,可能會越來越集中在這層「人機介面」的設計自由度上。

🔗 **來源**
- 標題：Claude Mods: Flipping the Harness Inside Out
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/claude-mods

#ClaudeCode #ClaudeMods #AnthropicAI #AgentHarness #AttentionInterface #DeveloperTools #AIAgent #GenerativeUI #Cursor #ChatGPT
