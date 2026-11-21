---
title: Lean verification of the Riemann Hypothesis
source: Hacker News
url: https://leanprover-community.github.io/blog/posts/riemann-hypothesis/
model: claude-code/sonnet
generated_at: '2026-11-21T22:15:45.478182'
score: 102
---

📌 【Lean 社群官方認證】1700 萬行程式碼，黎曼猜想過關了

TL;DR：Lean 與 Mathlib 社群正式發聲明，宣稱已完整驗證 Alpöge 的黎曼猜想證明，過程詳述了四項判定標準。

一份號稱證明了黎曼猜想的程式庫，裡面裝了 1700 萬行 Lean 程式碼，沒有一個人類完整讀過它。這聽起來像是信任危機的起點，但 Lean 和 Mathlib 社群用一套四項標準加上多個獨立檢查器，把這件事變成了一個可以逐條核對的工程問題。

🤔 **一份沒人讀完的證明，要怎麼讓人信？**

2026 年 11 月 20 日，Levent Alpöge 釋出了一份以 Lean 函式庫形式呈現的黎曼猜想證明，程式碼規模達到 1700 萬行。隔天，Lean 和 Mathlib 社群聯合發出聲明，並獲得 Lean FRO 與 Mathlib Initiative 背書，宣布對這份證明的正確性有完全信心。這份聲明的重點不是「相信」，而是逐一列出判定依據。

🧩 **四項標準，缺一不可**

聲明引用了 Xena Project 部落格先前提出的四項驗證標準，並說明全部都已滿足:
1. 黎曼猜想的敘述本身是正確的——這個敘述已被納入 Mathlib 的 `RiemannHypothesis`，並經過 Lean 與數論專家仔細審核。
2. 程式庫能正確編譯——截至聲明發出時，已有數十人回報成功編譯這份程式碼，並重現出相同的原始證明輸出檔，過程中沒有編譯錯誤或建置失敗。
3. 程式碼證明的是「正確的那個敘述」——社群額外新增了一份只匯入 Mathlib、單獨隔離出黎曼猜想敘述的檔案，並用兩套獨立工具（comparator 與 con-leche–compare）比對，確認 Alpöge 程式庫中證明的定理，與 Mathlib 既有的黎曼猜想敘述完全一致。
4. Lean 證明本身是有效的——匯出的原始證明，已經過多個檢查器驗證，包括 Lean 官方的 kernel、con-leche 與 con-ron 檢查器，以及第三方用不同程式語言獨立實作的多個檢查器。

📊 **連檢查器本身都要被驗證**

聲明特別提到，con-leche 與 con-ron 這兩個檢查器都附帶一份「相對於集合論」的正式證明，證明它們不可能接受一個假的證明，這是為了回應一種疑慮：如果 Lean 的邏輯系統本身有漏洞，證明是否可能利用這個漏洞。這些檢查都是針對證明的一份「惰性匯出檔」（inert export）進行，刻意讓它脫離 Lean 證明原始碼中假想的惡意程式碼可能觸及的範圍。更詳細的總覽文件則放在 MIT 的 GRH 專頁上。這篇聲明在 Hacker News 上獲得 686 點、547 則留言，顯示工程與數學社群對此事的關注程度。

💡 **信任的基礎，從「讀懂」換成「可驗證」**

這份聲明體現出形式化驗證社群一套成熟的思路:當證明規模大到沒有人能完整閱讀，正確性的保證就必須轉移到「多個獨立、彼此不信任的檢查器都能得出同一個結論」。這跟傳統數學靠同行評審「讀懂並認可」的模式有本質上的不同，卻可能是未來處理超大規模、AI 輔助產出的證明時唯一可行的路。

🎯 **實務啟示**

對工程師來說，這是一個觀察形式化方法（formal methods）如何在真實高風險場景中落地的活教材：用多重獨立檢查器交叉驗證、把「信任」拆解成可自動化的具體判定項目，這套思路同樣適用於審查 AI 產出的程式碼或系統設計，而不只是數學證明。

🔗 **來源**
- 標題：Lean verification of the Riemann Hypothesis
- 作者／機構：g-b-r（Hacker News 轉貼，原文為 Lean 與 Mathlib 社群聯合聲明）
- 連結：https://leanprover-community.github.io/blog/posts/riemann-hypothesis/

#LeanProver #Mathlib #FormalVerification #RiemannHypothesis #ProofAssistant #TheoremProving #FormalMethods #OpenSource #MathCommunity #SoftwareVerification
