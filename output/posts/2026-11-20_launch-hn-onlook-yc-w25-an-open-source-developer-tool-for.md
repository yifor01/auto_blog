---
title: 'Launch HN: Onlook (YC W25) – An open-source developer tool for designers'
source: Hacker News
url: https://github.com/onlook-dev/onlook/
model: claude-code/sonnet
generated_at: '2026-11-20T23:20:07.259555'
score: 74
---

📌 Onlook開源發布：讓設計師直接在真實程式碼上畫布作業

TL;DR：YC背景的開源桌面工具,把canvas疊在真實codebase上,讓設計師用現有的Claude Code或Codex直接改程式碼。

工程工具天生是為「收斂」設計的:你要知道自己在哪個branch、上次探索做到哪一步。但設計師的工作方式是「發散」的:看、畫草稿、排列各種變化版本、參考、remix。這道落差,正是Onlook這次重新發布想解決的問題。

🤔 為誰而做:讓設計師能用他們熟悉的方式待在程式碼裡

這是一篇Hacker News上的Launch HN貼文,作者Daniel(D_R_Farrell)是Onlook的創辦人。Onlook是一個桌面應用程式,在你真實的codebase上疊一層canvas,讓你可以用自己原本就在用的agent直接在程式碼裡做設計。根據貼文,專案累計獲得超過25,000名設計師與開發者支持,有100多人貢獻過程式碼,並兩度成為全球trending repo的第一名。團隊這次把整個產品重新打造成一個agentic design tool,並開源出來。

Onlook支援設計師同時開啟多個worktree,在本機跑真實的app,每一次改動都會變成一個可以review或直接丟棄的PR——也就是說,沒有「做完mockup之後還要重新刻一遍」這種重複勞動。

🧩 核心設計理念:canvas疊在真實的webview上

貼文解釋,團隊相信應該有一款開發工具,是按照設計師思考的方式打造的。設計師是透過「看」來思考的:畫草稿、排列變化版本、參考、remix想法,這也是為什麼canvas一直是設計工具的招牌功能。用工程工具做設計最大的痛點,一半來自專案啟動時佔用的心力(我在哪個branch?上次的探索放在哪個頁面?),另一半來自把寫好的程式碼「設計化」呈現所需要的額外工夫(在既有介面上prompt設計工具,或是為了某個特定狀態臨時搭建導覽)。

Onlook的用法是:讓它一次探索大量想法。可以要求它把產品裡的每一條流程都排出來、展示一個元件的每一種狀態,或是針對同一個畫面做出十個不同版本。所有設計結果會並排顯示在一個無限canvas上,每一個frame都是一個真正跑著你app、帶著真實資料的webview,不是mockup,是貨真價實的應用程式本身。團隊形容,做這個editor的過程中,他們意識到這其實可以是一種新型態的設計IDE——agent可以透過調整browser frame的URL,以及在canvas上排列、縮放這些frame,來自行決定如何呈現做好的程式碼。

技術上也遇到具體限制:所有frame共用同一個瀏覽器session,而Chromium對每個host每個session只允許六個連線,十個frame同時打開同一個app就會互相搶連線,團隊必須針對這個限制做規劃,並坦言canvas的效能還有很多要優化的地方。

🧩 怎麼運作:Electron app、git worktree、自家的Artifacts

Onlook是一個Electron應用,可以從GitHub匯入repo或上傳本機資料夾。接下來Onlook會建立一個git worktree、啟動dev server,並讓agent自行處理缺少的依賴套件或其他環境需求——使用者完全不需要打開終端機,agent做的每一件事都是一次正常的git diff,可以直接送到GitHub變成PR。Onlook會在每個frame裡注入一小段腳本,負責畫出選取外框並讀取頁面內容,因此當你點選一個元素並說「把這個改成card排版」,agent能準確知道「這個」指的是哪個元素。

值得注意的是,這次團隊沒有自己做agent:Onlook執行的是使用者自己訂閱的Claude Code或Codex,再把agent吐出的所有內容整理成一份型別化的事件紀錄(typed event log),自行畫出聊天介面的UI。在這之上,他們給agent提供了一批針對設計場景打造的專屬工具,包括在canvas上排列frame、提出建議、針對一個選取範圍生成多個變化版本——這對「agent要自行判斷怎麼把app調整到你需要的狀態」特別有用。

此外,Onlook還有自己的Artifacts功能:這是活在editor裡、但獨立於你的repo之外的快速HTML草稿,沒有網路存取權限,可以跨專案攜帶與編輯,有點類似其他設計工具裡的「元件」概念。使用者可以要求agent把目前的介面轉成一個Artifact,作為另一次探索的參考,或是直接下載成HTML,當作一份可互動的進度匯出檔分享給同事。

⚠️ 定位與限制

貼文也交代了產品的曲折歷史:在這次重新發布之前,團隊先後做過一個web版本(結論是時機太早)和一個Storybook-native版本(團隊自承是個錯誤)。促成這次重做桌面版的原因,是2024年7月那個早期桌面產品在零推廣的情況下,每個月仍持續有數百次下載。

🎯 實務啟示

桌面版editor免費下載,並以Apache-2.0授權開源,團隊表示未來會推出針對團隊的付費雲端產品。對於團隊裡有設計師需要直接碰真實程式碼、又不想讓他們陷入branch管理與終端機操作的場景,Onlook提供了一個把「探索多版本設計」與「讓真實codebase跑起來」結合在一起的具體做法,值得工程團隊評估是否能接進現有的Claude Code或Codex工作流。

🔗 來源
- 標題：Launch HN: Onlook (YC W25) – An open-source developer tool for designers
- 作者／機構：D_R_Farrell, Hacker News
- 連結：https://github.com/onlook-dev/onlook/

#Onlook #OpenSource #DesignTools #ClaudeCode #Codex #Electron #DeveloperTools #YCombinator #AgenticDesign #GitWorktree
