---
title: Axiom Math wants to keep AI slop out of mathematics
source: TechCrunch AI
url: https://techcrunch.com/2026/11/05/axiom-math-wants-to-keep-ai-slop-out-of-mathematics/
model: claude-code/sonnet
generated_at: '2026-11-05T23:09:04.879560'
score: 80
---

📌 Axiom Math 砸16萬行以上Lean程式碼,替數學蓋一座不會塌的地基

TL;DR:這家估值16億美元的新創,用AI agent艦隊把7654頁數學巨著Stacks Project全部形式化驗證,想在AI產出證明的速度超過人類驗證速度之前先把地基打牢。

上個月OpenAI一口氣發布719份手稿,宣稱解開了數學界一些最難的問題,但就連用來確認這些結果的電腦檢查本身都可能出錯。如果連「可驗證」這道防線都靠不住,數學是不是也要步入AI垂直內容的後塵?Axiom Math給出的答案不是放慢腳步,而是先把地基做實。

🤔 背景:當證明的產出速度超過驗證速度

Axiom Math由25歲的Carina Hong創辦,她原本在史丹佛讀數學博士,2025年3月中途退學創業,今年3月拿到Menlo Ventures領投的2億美元A輪。公司這次驗證的對象是Stacks Project,一套由哥倫比亞大學數學家Johan de Jong在2005年發起的開放原始碼數學參考庫,內容從大學程度的代數一路累積到代數幾何、幾何與數論最前沿的成果。哥倫比亞大學的Peter Woit曾說這套文獻「沒有什麼能真正相提並論」,並拿它比擬20世紀重建整個數學基礎的Bourbaki叢書。

🧩 方法:讓AI agent自己找任務,逐行檢查1600萬行Lean程式碼

形式化驗證(formal verification)的做法,是把證明改寫成Lean這種程式語言,再由proof assistant逐行檢查邏輯是否成立,通過了才能信任這個證明站得住。Axiom的agent艦隊把Stacks Project約7654頁的內容翻譯成大約1600萬行經過電腦檢查的Lean程式碼。難點在於Stacks裡的定理和定義彼此高度相依,像家族樹一樣一路往前追溯,要在1600萬行規模下維持每一條連結不出錯,團隊一開始並不確定能不能做到。CEO Hong的說法是:「生活中又大又精巧的東西通常兼容不了,但你希望(Stacks裡的)定理彼此一致,不要自相矛盾,定義也不要互相打架。」實作上,團隊只給agent一個鬆散的層級結構,而不是把每個agent該做什麼都寫死,讓它們自己找任務、自己判斷哪些工作可以平行進行。Axiom也訓練了自己的數學模型,Hong表示這是大多數其他驗證新創沒有走的路,一開始靠內部的Lean專家教agent培養人類式的「品味」,後來agent漸漸自己發展出這種判斷力。

📊 結果:填補代數幾何在形式化世界裡的黑洞

Axiom技術團隊成員Ashvin Swaminathan指出,目前已經形式化的數學版圖裡,代數幾何是一塊巨大的黑洞:過去想用Lean檢查代數幾何新成果的研究者幾乎沒有東西可以依靠,「現在他們有了」。這呼應了費爾茲獎得主、UCLA數學家Terence Tao的說法:你手上的形式化證明越多,就能做出越多新的形式化證明。

💡 深入分析:Axiom瞄準的不只是數學家

Axiom把這件事定位成軟體基礎設施問題。開發者長期難以保證程式碼沒有bug或安全漏洞,而這個問題會隨著AI agent寫出更多程式碼而惡化。Swaminathan說:「我們認為數學是適合開始打造這類基礎的領域,而且這種能力是可以轉移的。Agent能讀我們的程式碼、理解它,再在上面蓋新的基礎設施,我們的Lean形式化成果現在就是agent可以往上疊的底層。」Hong的擔心很直接:如果一開始就讓agent在劣質工程決策上「傾倒垂直內容」,之後agent很難再把邊界往外推,所以她公開向所有做coding的公司下戰書,挑戰大家在這個規模上做形式化。

🎯 實務啟示

對工程團隊而言,值得關注的不是這次驗證本身,而是它示範的協作模式:讓agent在鬆散結構下自主找任務、平行作業,再用形式化驗證當作品質把關,這套模式未來很可能被複製到agent自動寫基礎程式碼的場景。如果Lean生態系統真的因此長出一塊可信賴的代數幾何基礎,做相關研究或工具開發的人等於多了一個現成的起點。

🔗 來源
- 標題:Axiom Math wants to keep AI slop out of mathematics
- 作者／機構:Aditya Mehta, TechCrunch AI
- 連結:https://techcrunch.com/2026/11/05/axiom-math-wants-to-keep-ai-slop-out-of-mathematics/

#AxiomMath #FormalVerification #Lean #Mathematics #AIAgents #StacksProject #AlgebraicGeometry #AIResearch #SoftwareVerification #MathAI
