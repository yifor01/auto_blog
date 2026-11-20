---
title: 'The War Against Slop and an Emerging Weapon to Fight it: Formal Verification'
source: Latent Space
url: https://latent.space/p/formal-verification/
model: claude-code/sonnet
generated_at: '2026-11-20T23:20:07.259386'
score: 89
---

📌 當AI程式碼開始「摻水」，形式驗證成了新戰場

TL;DR：AI寫code量暴增後，formal verification正從學術工具變成對抗slop與資安風險的量產防線。

測試能抓到bug,但測試永遠無法回答一個問題：「我是不是漏掉了最後一個？」這正是formal verification（形式驗證）和傳統測試、AI自我批評最本質的差異,也是這篇報導想講清楚的核心。

🤔 Slop時代,「驗證」兩個字被用得太輕

2026年AI產業的年度詞是「slop」，指LLM產出的低品質內容。隨著越來越多程式碼由AI生成,避免slop成了工程師的日常課題。報導指出,目前已有多家公司以formal verification作為解方,包括Harmonic、Theorem、Axiom Math,以及新進場的&Truth（唸作「and truth」）。

Latent Space採訪了&Truth共同創辦人兼共同CEO Clark Barrett。他同時是史丹佛大學的Corbel Professor（Research），也是cvc5的共同創造者——cvc5是一套廣泛用於satisfiability modulo theories（SMT）的自動推理引擎,Barrett提到它現在被Amazon大量採用,例如在Amazon的agentic開發環境Kiro中用於規格分析與測試生成,「它從實驗室裡的一個好點子,變成現在在Amazon的生產線上每天被呼叫數十億次」。

被問到AI coding agent公司口中的「驗證」（跑測試、自我批評、讓另一個模型來評判）距離真正的驗證還有多遠時,Barrett的回答很直接：「主要差別就在於,你怎麼知道自己做完了。用測試、patching、scanning這些既有工具,它們都很好,能抓出一大堆問題,但你永遠無法確定——我是找出了全部的問題,還是還有一個漏網之魚躲在我的工具抓不到的地方?」

🧩 Lean：讓AI寫證明、讓機器檢查證明

&Truth的第一個工具&Atlas,被形容為「世界開源程式碼的地圖,從C語言程式碼開始」。&Truth的技術基礎是Lean,一套開源程式語言與proof assistant（證明輔助工具）。他們的做法是結合AI與自動推理技術來構造證明,再交由Lean檢查。Barrett形容:「Lean做的事就是檢查你有沒有犯錯,你可以把它想成一個非常精密的數學檢查器。」

Lean目前也是前沿模型挑戰高難度數學題的常用工具:報導提到,本週GPT-6.2 Astra產出了Vals認為是「Smoktunowicz's Gap Theorem的第一個Lean證明」,Vals還補充Anthropic曾用Lean將費馬最後定理（Fermat's Last Theorem）形式化,項目達1,300萬行程式碼。更新的消息是,據報Anthropic的數學家Levent Alpöge聲稱利用Claude證明了167年歷史的黎曼猜想（Riemann hypothesis）,並將證明以Lean程式碼的形式發布。

&Truth想在Lean之上打造一臺「verification machine」,目標是讀懂任何語言的程式碼,證明它是否滿足明確陳述的需求,並讓人類不必逐行閱讀就能信任它。

🏢 不只是防守:Axiom、Harmonic、Theorem各有側重

Axiom Math用formal verification為其數學推理系統的訓練提供正確性回饋,證明嘗試的結果會回頭改善未來的模型。該公司CEO Carina Hong此前受訪時強調:「formal verification對我們來說不只是清掉愚蠢的錯誤和幻覺,而是在放大聰明——是在走向super-intelligence。」Axiom的AxiomProver負責生成Lean證明,配套工具AXLE則用於探索、驗證與操作這些證明。

Harmonic的Aristotle被稱為「automated theorem prover」,官網描述其運作方式是「AI寫證明,Lean逐步檢查每一步,所以結果永遠不依賴於AI本身是對的」。

資安則是另一條重要戰線。Barrett提到&Truth一個很有力的應用情境,是掃過世界上所有的C語言程式碼(無論開源還是閉源),確保它們記憶體安全,一旦發現不安全的地方就能明確指出問題所在,要求修正。Theorem也把資安列為重點,官網寫道:「驗證是唯一在對手持續擴大規模時仍然有效的防線。」Theorem與Anthropic合作發表的部落格文章〈LLMs are making formal software verification feasible at a much larger scale〉中提到一個令人振奮的細節:在一組36個小型驗證任務上,Opus 5.5用比Opus 5少約40%的token,就達到50%的解題率——顯示formal verification雖然目前仍很耗token,但效率正在隨著模型在長驗證任務上訓練而持續改善。

💡 從vibe-coding走向veri-coding

&Truth官網提出一個說法:開發者將從「vibe-coding」走向「veri-coding」,也就是把驗證層納入日常工作流程的一部分。Barrett解釋:「如果你把verification machine接到agent上,你還是可以說『嘿,我要你做這個』。可能要花一點工夫跟agent把規格(specification)釐清,但接下來agent就能在底層跟formal工具協作,你幾乎看不出差別,只是你的程式碼第一次跑就會是對的。」換句話說,開發者的時間會更多地花在撰寫與審查規格上,而不是寫程式碼或review程式碼本身。

🎯 實務啟示

對工程師而言,這篇報導點出一個值得關注的訊號:當agent team可以直接照你的指令把東西做出來,人類開發者需要一種方式去檢查交付結果是否正確,而formal verification正是目前最被寄予厚望的路線之一。如果你的團隊已經在用cvc5、Lean或類似工具,或是正在評估Harmonic、Theorem、Axiom Math、&Truth這類產品,這是一個值得持續追蹤、而非一次性嘗鮮的方向。

🔗 來源
- 標題：The War Against Slop and an Emerging Weapon to Fight it: Formal Verification
- 作者／機構：Latent Space
- 連結：https://latent.space/p/formal-verification/

#FormalVerification #Lean #AICoding #SMTSolver #Anthropic #SoftwareSecurity #AISlop #TheoremProving #cvc5 #AgenticCoding
