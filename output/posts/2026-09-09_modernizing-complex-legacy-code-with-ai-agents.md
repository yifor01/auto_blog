---
title: Modernizing complex legacy code with AI agents.
source: Mistral AI
url: https://mistral.ai/news/legacy-code-modernization/
model: claude-code/sonnet
generated_at: '2026-09-09T19:55:10.492557'
pinned: true
---

📌 【Mistral 實戰案例】AI Agent 搬遷 4 萬行 Fortran 老代碼

TL;DR：Mistral 用結構化 AI Agent workflow，替歐洲能源業者把 4 萬行 Fortran 77 搬到 C++，證明全自主 agent 做不出真正的現代化。

如果把整段程式碼丟給 AI，讓它自己翻譯成新語言，聽起來很誘人，效率也最高。但 Mistral 在這個專案裡試過這條路，結果是「看起來像用 C++ 語法重打一次 Fortran」，不是現代化。真正能上線的版本，反而來自一套刻意設計、還留了人在迴圈裡的工作流程。

🤔 **40 年前的程式碼，連編譯器都幫不了你**

這次的目標是一套物理密集的儲油層模擬器，1977 年標準化的 Fortran 77 寫成，沒有測試套件，也沒有集中的文件。Mistral 指出這個語言的幾個結構性限制：沒有模組、沒有命名空間、沒有結構化型別；狀態存在 COMMON 區塊裡，也就是整個程式共用的全域記憶體；變數型別由第一個字母隱式決定，拼錯變數名稱不會觸發編譯錯誤，只會靜默地生出一個新變數；變數名稱長度上限只有 6 個字元，導致命名相當隱晦。

素材中舉了一個一階 Taylor 展開的例子：Fortran 版本的輸入輸出都是 COMMON 區塊裡的全域變數，IC 之所以是整數，只因為它的名字第一個字母落在 I 到 N 之間。改寫成 C++ 之後，可以用明確型別、物件導向寫法，把回傳值改成真正 return，而不是寫回全域變數。這種結構性差異，加上要整合像 PetSc 這類現代科學計算框架的需求，讓「照著語法翻譯」根本不夠。

🧩 **先蓋驗證機制，再讓 Agent 動手**

在放手讓 agent 上場之前，團隊先解決了一個更根本的問題:如何證明新舊兩套程式碼在數值上是一致的。他們在 Fortran 程式碼裡加了可以匯出狀態的 subroutine，在 C++ 端建立對應的測試框架來載入這些 checkpoint，並寫了 Skill.md 檔案引導 agent 正確使用這套機制。文中示範:在 Fortran 端印出 RHOG 變數的值（該次執行為 42.71834），再用同一個數值作為 C++ 模組測試的參考基準。Mistral 認為這一步應該是任何程式碼現代化專案最先要做的事，因為數值一致是最便宜、最有說服力的「這段模組搬遷完成」的證明。

文件的重建則利用了程序式語言的一個特性:整個程式可以畫成一棵呼叫者-被呼叫者樹。團隊用自製的 parser 產生這棵樹，再用 Vibe CLI 派出上百個 agent 去逐節點寫文件，每個 agent 可以透過文件庫和 Mistral OCR 把相關的 PDF 拉進來，從樹的葉節點開始往上做，每個節點都會開一個 PR 回原始 repo，另有一個以固定排程跑的 reviewer agent 負責找出新開的 PR、審核並在需要時安排修正任務。

真正搬遷程式碼時，Mistral 試了三種做法。第一種是完全放手，一個 agent 負責一個 Fortran subroutine，各自獨立翻譯一週，結果功能可用，但 COMMON 區塊被一對一改成全域 struct，GOTO 控制流也原樣保留，等於「用 C++ 語法重打一次 Fortran」。第二種是給 agent 分工結構:規劃者、coder、tester、程式碼品質審查者一起處理每個模組，品質明顯提升，但遇到程式碼本身複雜度夠高的部分，agent 卡住之後只會反覆嘗試修 bug 然後停滯，沒有人可以介入。最後採用的折衷方案，是人類操作一整套 coder、tester、reviewer agent 的工作流程，逐模組搬遷，保留第二種做法的品質，又加上人類可以在 agent 卡住時介入的檢查點。

最終的結構化流程是:先用呼叫者-被呼叫者樹，配合客戶的儲油層工程師，找出獨立且大小可控的子樹模組（依經驗，控制在一萬行 Fortran 以內）；每個模組依序跑過:產出目標 C++ 架構 → 由儲油層工程師審核 → 通過後拆成任務佇列 → 每個任務跑「規劃 → 實作 → 測試 → 重複」的子流程 → 最後由人類審查 PR，要求修改直到可以合併。

📊 **第一階段:30 萬行裡搬了 4 萬行**

第一個 sprint 覆蓋了核心功能，完成 30 萬行中的 4 萬行。Mistral 特別指出，這套 Fortran 程式碼本身是自成一體、可以獨立執行的，這是一個相對有利的起始條件。

⚠️ **不是每個遺留系統都這麼幸運**

Mistral 明確提到，如果搬遷對象依賴外部系統、沒有可執行的基準版本，或是背後的物理邏輯沒有任何文件記載，會遇到這篇文章沒有討論到的額外挑戰。換言之，這次案例成功的前提，是程式碼本身相對獨立、可執行。

🎯 **實務啟示**

這個案例給想用 AI 處理大型遺留系統的工程師一個明確提醒:先把「怎麼證明搬遷正確」這件事解決掉，再談自動化程度。單純追求 agent 全自主，換來的往往是語法翻譯而非真正的架構現代化；反而是「agent 分工 + 人類檢查點」這種看似沒那麼酷的折衷方案，最後產出的程式碼品質最穩定。

🔗 **來源**
- 標題：Modernizing complex legacy code with AI agents
- 作者／機構：Mistral
- 連結：https://mistral.ai/news/legacy-code-modernization/

#AI #Mistral #LegacyCode #Fortran #CodeModernization #AIAgents #SoftwareEngineering #CodeMigration #ScientificComputing #DeveloperTools
