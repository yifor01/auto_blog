---
title: Bend – a language that blocks AI mistakes via proof and runs on GPUs
source: Hacker News
url: https://bend-lang.com/
model: claude-code/sonnet
generated_at: '2026-09-18T19:47:11.499080'
score: 99
---

📌 Bend:用數學證明擋住AI寫壞的程式碼,還能自動跑上GPU

TL;DR:開源語言Bend把型別檢查變成證明檢查,讓AI Agent每改一行都能被即時驗證,同時原生支援CPU/GPU平行運算。

如果AI已經能自己寫程式碼、自己開PR,你要怎麼確定它沒有偷偷改壞一條你從沒讀過的邏輯?Bend給出的答案很直接:別讀程式碼,要求它提供證明。

🤔 後AGI時代,我們需要的是「無歧義」的溝通方式

Bend官網開宗明義提出一個設定:在人類逐漸不再自己寫程式碼與讀程式碼的世界裡,仍然需要一種沒有歧義的方式告訴AI「我要什麼」。自然語言做不到這件事,但law(規則)可以讓意圖變得精確,而proof(證明)則能驗證AI是否真的照著你的意圖實作。Bend想解決的,就是把這兩件事和一個夠快的編譯器綁在一起。

🧩 型別檢查器就是證明檢查器,還能自動鋪滿GPU核心

Bend編譯為原生程式碼,單核心執行速度接近C語言;同一份binary也能跑在16核心或GPU上,最高比單核心快上百倍。它的型別檢查器本質上是像Lean、Rocq那樣的證明檢查器,一般中型程式碼庫的證明檢查可能要花上數分鐘,但Bend最多只需要一秒,這讓AI Agent可以在每一次修改後都即時檢查。平行化也不需要開發者手動處理:把工作拆成兩半,Bend會自動把呼叫分散到找得到的每一個核心上,再把結果合併回來,不需要執行緒、鎖或自行撰寫kernel。官網展示了一個pow2函式在4096個GPU核心上執行的例子。

最核心的機制是LAWS.bend:開發者在這個檔案裡宣告「規則」,此後任何AI都無法交出違反這些規則的一行程式碼。官網用一個遊戲示範:要求Claude讓遊戲棋盤能夠環繞(wrap around),在沒有LAWS.bend的情況下,這個修改引入的bug就直接上線了;有了LAWS.bend,AI必須反覆重試,直到它真正建好邊界並證明這條規則成立為止。官網將LAWS.bend形容為「由證明背書的AGENTS.md」,也就是說「不要犯錯」這句話,現在變成了可以被型別系統檢查的東西。Bend的核心理論有兩篇論文支撐:BendTT是一套affine dependent type theory(仿射依賴型別理論),構成Bend的型別系統核心;BendRT則是跑在CPU與GPU上的平行執行期(runtime),也就是虛擬機本身。

⚠️ 專案仍在早期,目前建議只用在後端

官方明確表示Bend仍在快速演進中,會有bug,遇到問題歡迎回報issue。目前建議的使用場景是後端,作業系統支援Linux與macOS。完整語言說明收錄在GUIDE.md,也可以透過`bend guide`指令直接印出。

🎯 實務啟示

如果你的團隊已經在用AI Agent大量自動生成程式碼,Bend提出的思路值得參考:與其事後花時間審查AI寫的每一行,不如把不能違反的不變量寫成可被機器驗證的規則,讓AI自己反覆重試直到通過證明,而不是依賴人工Review去抓漏。

🔗 來源
- 標題:Bend – a language that blocks AI mistakes via proof and runs on GPUs
- 連結:https://bend-lang.com/

#Bend #ProgrammingLanguages #FormalVerification #TypeTheory #GPUComputing #AIAgent #DependentTypes #OpenSource #CUDA #SoftwareCorrectness
