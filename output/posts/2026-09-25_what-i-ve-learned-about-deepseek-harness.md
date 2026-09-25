---
title: What I’ve Learned About DeepSeek Harness
source: KDnuggets
url: https://www.kdnuggets.com/what-ive-learned-about-deepseek-harness
model: claude-code/sonnet
generated_at: '2026-09-25T20:43:48.816234'
score: 111
---

📌 【DeepSeek開源】連Agent迴圈都能換的插件式Runtime dsh

TL;DR：DeepSeek開源agent runtime dsh，把模型、工具、迴圈全做成可替換插件。

一個標榜「developer preview」、README裡還寫著「將會有破壞相容性的變更」的專案，十天內拿下超過18萬顆星、2萬次fork，這樣的速度連AI工具圈都少見。它靠的不是「更好用的coding agent」這麼簡單的理由。

🤔 **DeepSeek又一次選擇開放基礎設施**

2026年8月13日，DeepSeek悄悄開源了一個agent runtime，稱為DeepSeek Harness，CLI名稱是dsh。上線後反應一點都不安靜：第一個12小時衝到約5萬星，28小時來到約9.2萬星，十天內突破18.6萬星、超過2萬次fork。

這不是DeepSeek第一次選擇開放基礎設施而非築起圍牆花園。2025年1月，DeepSeek-R1成為第一個來自美國以外實驗室、採MIT授權的開放前沿推理模型，訓練成本遠低於同等級的西方模型，重設了外界對「誰有能力開放釋出前沿AI」的預期。Harness讀起來像是同樣的精神往堆疊上層延伸：這次開放的不只是權重，而是整套agent基礎設施，且與公告同時發布，而非提前預告。

🧩 **核心架構：每一層都是插件，連推理迴圈也不例外**

DeepSeek反覆強調的核心主張是：agent的每一層都是插件，模型adapter、工具註冊表(tool registry)、session log、沙箱(sandbox)、UI，甚至agent迴圈本身都不例外。它建構在Cordis這個插件框架之上，Cordis在被DeepSeek採用之前，已經在Koishi聊天機器人專案裡穩定運作四年，並非為這次發布臨時打造。這個設計還有一篇論文作學術背書：《A Programming Paradigm for Spatiotemporal Composability》。

幾個值得留意的技術細節：它是model-agnostic設計，跨越約40家供應商，甚至可以把sub-agent整個委派給競爭對手的agent，不被鎖定在DeepSeek自家模型上；沙箱是真正的作業系統層級隔離，而非軟性約定，Linux上用bwrap(Bubblewrap，Flatpak應用使用的同一種沙箱機制)搭配Landlock，macOS上用蘋果自家的Seatbelt沙箱框架，Windows上用受限的ACL token，預設為fail-closed而非fail-open；session log是append-only，並由runtime強制執行一條規則：只要模型看過的內容，就一定會被記錄，不存在「靜默上下文」。

README自己也很坦白地寫著「developer preview」與「將會有破壞相容性的變更」，對一個這麼受矚目的專案來說相當罕見。簡單說，這還不是一個能直接對著repository跑起來用的coding agent，而是組裝coding agent所需要的機件。

🧩 **實測：152個可各自替換的插件**

作者實際跑了一次。由於是以npm套件形式發佈，可以直接用`npx --yes @deepseek-ai/dsh --version`安裝，回傳版本號0.1.5-rc.2，與GitHub releases頁面的版本紀錄相符，確認這是真實可運作的安裝。

help輸出顯示指令包括`web`(啟動web profile，等同`--profile web`)與`plugin`(把剩餘參數轉發給該profile目錄下的pnpm，管理插件)。此外還有`headless`、`tui`、`rescue`等不同profile，各自只是一組不同的已掛載插件堆疊。`dsh plugin add`把安裝新能力當成一次普通的套件安裝，而非另外設計一套特殊機制。

最具體的發現來自`--dump-default-config`這個flag，它會在profile啟動前印出完整組成的插件樹。對預設web profile執行後，印出了152個各自獨立命名、可各自替換的插件，從側邊欄、聊天視窗，到approval提示、sub-agent面板、排程UI(內建但預設`disabled: true`)，全都是各自獨立、有自己id的可安裝套件，多數工具會把這些都當成同一個巨石式前端來處理。

作者也試了在沒有設定model key的情況下跑一次性的headless模式：`npx --yes @deepseek-ai/dsh --profile headless "say hello"`，結果立刻失敗，並回傳清楚具體的錯誤訊息：`MISSING_CREDENTIAL: llm-deepseek: no API key for provider route "deepseek-official"`，直接告訴使用者該設定哪個環境變數，或web UI的Models頁面會把金鑰存在哪裡。

💡 **連推理迴圈都能換，是真正的架構差異**

作者認為最與眾不同的地方，不在插件數量，而在於「agent迴圈本身就是一個插件」。在Codex CLI這類工具裡，要改變核心推理迴圈的行為，得去改一個編譯好的Rust binary；在dsh裡，迴圈就活在一個普通的套件裡，可以像換UI面板一樣直接從設定檔換掉。這是真正的架構差異，而不只是「extensible」的另一種說法，也是為什麼專門在做agent基礎設施的開發者會特別關注它。不過這不代表它已經適合廣泛推薦：一份獨立的插件目錄在第一次快照時只收錄了94個插件、分四個類別，生態仍在起步。

⚠️ **限制**

專案本身反覆聲明這是developer preview，且會有破壞相容性的變更；如果目標是明天早上就要拿來取代Claude Code或Codex當日常coding agent，它還沒準備好，而且專案自己也不假裝已經準備好了。

🎯 **實務啟示**

如果你是在做agent基礎設施，或是想在不fork任何東西的情況下換掉session store或沙箱後端，這個架構現在就值得認真研究，它是真的在跑，不是空氣專案。但如果只是想找一個明天就能取代現有coding agent的日常工具，現在還不是時候。

🔗 **來源**
- 標題：What I've Learned About DeepSeek Harness
- 作者／機構：Shittu Olumide, KDnuggets
- 連結：https://www.kdnuggets.com/what-ive-learned-about-deepseek-harness

#DeepSeek #AgentRuntime #OpenSource #PluginArchitecture #AIAgents #DeveloperTools #CLI #Cordis #AIInfrastructure #CodingAgent
