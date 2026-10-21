---
title: Solving a 31-year-old grand challenge in mathematics – the KLS conjecture
source: Microsoft Research
url: https://www.microsoft.com/en-us/research/blog/solving-a-31-year-old-grand-challenge-in-mathematics-the-kls-conjecture/
model: claude-code/sonnet
generated_at: '2026-10-21T20:50:49.003623'
score: 111
---

📌 微軟研究院證明31年懸而未解的KLS猜想

TL;DR：KLS猜想被證明成立，為高維抽樣演算法的效率提供了維度無關的理論基礎。

一個1995年提出的猜想，跨越三十一年仍無人能完整證明，直到AI輔助的遞迴式證明方法在2026年10月補上了最後一塊拼圖。

🤔 「平面切一刀」和「隨便切一刀」差多少？

Kannan–Lovász–Simonovits（KLS）猜想問的是：對於一大類高維機率分布，用平面切割去分割這個分布，效果是否幾乎和用任意形狀的切割一樣好？更精確地說，KLS猜想預測兩者的差距不會超過一個通用常數，而且這個常數與維度無關。

這個問題看似抽象，實際上牽動著高維抽樣理論的核心：這些切割的幾何性質，決定了隨機漫步探索一個分布的速度有多快，而隨機漫步正是許多隨機演算法的基礎。Mathematical Sciences Research Institute 曾稱其為「高維凸幾何的核心開放問題」，Simons Institute 則稱它是「凸幾何中最重要的開放問題之一」，Quanta Magazine 形容它「位於統計與電腦科學眾多問題的核心」。在這次證明之前，2026年7月的最佳已知結果雖然縮小了差距，但那個常數仍會隨維度緩慢增長，並非真正維度無關。

🧩 讓100條AI探索路徑，換來一個可遞迴的判準

這次由 Microsoft Research 機器學習與最佳化團隊的 Xinzhi Zhang 與合作者 Zhao Song 完成的證明，過程本身和結論一樣值得關注。研究團隊先用一套結構化、由人類主導的流程，讓多個AI agent平行探索超過100種候選方法，其中許多涉及高階張量的冗長計算，這個過程產出了一個新的數學判準，成為最終證明的基礎。

接著他們發現這個判準可以遞迴套用：每一輪改善過的邊界，可以再餵回同一個論證，產出更緊的邊界。在2026年10月1日版本的論文中，這個方法已經把邊界對維度的依賴降到了迭代對數的量級，這個函數成長極其緩慢，但終究還是隨維度增長，所以還不算完全解決猜想。

最後一步，是把整個遞迴細化過程再整套重複一次，而不只是套用一輪。這個靈感來自作者先前在線性規劃快速演算法上的研究。他們證明了每一階段產生的小誤差，收縮速度快到總和會被一個與維度無關的通用常數所限制。這一步在2026年10月4日版本的論文中完成了整個證明，徹底消除了對維度的依賴。

論文特別強調，這套遞迴方法、重複套用的策略，以及誤差總和有界的證明，都是研究者原創的貢獻；AI工具協助的是探索候選方向、進行詳細推導、準備稿件與執行內部的證明檢查，而研究方向的決定、有潛力想法的篩選、最終論證的組裝與驗證，都由研究者親自完成。

📊 同一天，三組獨立證明和一份Lean驗證同時出現

在作者發布完整證明的同一天，另一組頂尖學者也發布了一份獨立完成的完整證明，而且他們的工作建立在 Microsoft 論文第一版的基礎上，稱其中的判準是「證明中最關鍵的一步」。同一天還出現了第三份依賴相近想法的獨立證明，隨後更有人釋出了一份 Lean 4 形式化驗證，結合了 Microsoft 第一版論文的關鍵判準與額外研究成果。

獨立證明是數學界驗證結果最有力的方式之一，因為它證明這個結論不是建立在單一條推理鏈上。多組獨立方法與形式化驗證接連出現，進一步增強了外界對「這是一個真實的底層原理，而非脆弱的技巧性論證」的信心。

💡 無人引導的AI單獨嘗試，反而沒成功

這項研究同時示範了一種研究方法論的對比。研究團隊另外做了一組對照實驗：用大致相同的總token預算，讓幾個主流AI模型反覆嘗試無人引導地直接解決同一個問題，結果沒有成功。

真正奏效的做法，是一種多agent平行探索、人類逐輪修剪的流程：讓多個agent平行探索一個想法的不同變體，研究者檢視中間結果，淘汰沒有前景的方向，再把最有希望的結果送進下一輪，前後大約經歷了100條研究軌跡才等到關鍵突破。這說明最終的成功，同時依賴AI系統的能力與研究者的數學判斷力，兩者缺一不可。

⚠️ 證明還在簡化，正式版尚未釋出

作者目前正在簡化證明，並將精簡後的版本在Lean中重新驗證，計畫在完成最終審查後一併公開，讓數學與理論電腦科學社群能更容易檢視與延伸這個結果。

🎯 KLS不再是假設，高維抽樣理論可以拿掉條件句

KLS猜想解決後，過去許多假設KLS成立才能推出的結果，現在都可以無條件地成立，這對仰賴隨機漫步取樣效率的演算法設計者是一個紮實的理論基礎。對於正在嘗試用AI加速研究的團隊，這個案例也提供了一個可參考的流程範本：用AI做大規模平行探索與繁瑣推導，但方向判斷與最終驗證仍由人類把關。

🔗 來源
- 標題：Solving a 31-year-old grand challenge in mathematics – the KLS conjecture
- 作者／機構：Microsoft Research — Xinzhi Zhang
- 連結：https://www.microsoft.com/en-us/research/blog/solving-a-31-year-old-grand-challenge-in-mathematics-the-kls-conjecture/

#KLSConjecture #MicrosoftResearch #ConvexGeometry #HighDimensionalSampling #AIforMath #TheoreticalComputerScience #RandomWalk #MachineLearning #Mathematics #ProofVerification
