---
title: Claude-shaped science
source: Anthropic Research
url: https://www.anthropic.com/research/claude-shaped-science
model: claude-code/sonnet
generated_at: '2026-10-01T21:55:31.204549'
pinned: true
---

📌 【Anthropic 客座文章】放棄跟 Claude 爭論，物理學家反而挖到跨領域金礦

TL;DR：物理學家 Matthew Schwartz 打造開源工具 BootLoops，讓 Claude 找出跨領域都適用的「Claude 型」計算問題。

AI 做科學的新聞標題總是很誘人，但多數學術研究者真正動手用模型時，卻常常感到一種落差：模型很聰明，可是離「像人類科學家一樣工作」還差得遠。這篇 Anthropic 客座文章，就是一位物理學家正面迎擊這個落差之後的紀錄。

🤔 **人類科學家與 LLM 之間的「阻抗不匹配」**

作者 Matthew Schwartz 指出，目前的 LLM 擅長的事情，和科學家實際需要的工作方式並不吻合，他借用物理學的概念稱之為「impedance mismatch」：兩個系統各自運作良好，但彼此銜接不良，導致大部分輸入的東西傳不過去。多數媒體報導的 AI 科學突破集中在數學領域，因為那裡的問題可以被完整陳述、答案也能被絕對驗證，但這不是科學研究的常態。他去年底曾讓 Claude Opus 4.5 擔任研究助理，發現它表現得像一位速度快 20 倍的優秀研究生，但過程很辛苦，他必須逐句修改、把它從無關的方向拉回來、從死胡同中拽出來。

🧩 **不再硬逼 Claude 當合作者，而是找「Claude 型」問題**

這次作者換了做法：不把 Claude 當成他想要的那種合作者，而是去找真正適合 Claude 能力的問題。他鎖定的切入點是散射振幅（scattering amplitudes）計算，這是解讀大型強子對撞機（LHC）數據的理論工具，核心是一種被稱為 Feynman 圖的多維積分，難度高到一個積分可能就是一篇博士論文的份量。過去 20 年間，學界發展出「S-matrix bootstrap」方法：不直接硬算積分，而是用物理約束條件不斷縮小可能答案的範圍（例如先用奇異點把選項縮到 2 萬個、再用對稱性縮到 500 個，一路收斂到唯一解）。更新的「半數值化 bootstrap」則是搭配極高精度（甚至上千位數）的數值計算，在約束不足以完全收斂時，用數字把剩下的係數精確釘死。作者認為這類問題特別適合 agentic AI：需要橫跨數學、物理、程式設計等多領域知識，需要大量寫程式與演算法開發，而且結果可以用兩支腳本互相驗證，門檻低到不管是不是專家都能檢查答案。

於是作者交給 Claude Fable 5 的第一個任務，是把散射振幅領域中分散在 Wolfram Language、C++、Python、Julia，甚至只存在論文裡（完全沒有程式碼）的方法，統一移植到同一套框架，這個過程逐漸發展成一套工具組，作者稱之為 BootLoops，其定位類似 Claude Code、Claude Science 之於 Claude，或是 Codex 之於 GPT 的「harness（任務框架）」。BootLoops 已經開源，可以搭配任何模型使用。

📊 **20 分鐘重現了作者花數週寫出的程式**

作者提到，Claude 用 BootLoops 在約 20 分鐘內重現了他自己論文中的計算結果，而他當初寫那段程式碼卻花了數週。更出乎意料的是，Claude 還主動指出他原本的做法效率不佳，並提出一個他自己並不知道的更好演算法。不過，當作者請 Claude 去尋找 S-matrix bootstrap 能解開的「未解」振幅問題時，卻發現：凡是簡單到這個方法能處理的問題，也簡單到人類早就做過了，也就是說大多數都已經被解決。

💡 **跨領域的「Claude 型問題」：連結到生態學、族群遺傳學等領域**

作者指出，一旦 Claude 擁有了 BootLoops，它持續發現同一種模式：許多領域其實存在一個數學、物理或電腦科學上的既有技巧就能徹底解決的問題，只是該領域沒有人知道這個技巧存在。作者把這類問題稱為「Claude-shaped problems」，並把搜尋範圍從自己熟悉的高能理論物理，延伸到地質學、生物學、經濟學與語言學等領域。由於作者在這些領域沒有專業背景，他找了各領域的專家來判斷 Claude 找到的連結是否真的有意義，結果不少連結最初雖然技術上正確，但在科學上並不特別，於是他與領域專家合作，引導 BootLoops 去回答那些該領域真正關心的問題。

⚠️ **AI 擅長的和科學家需要的，仍有落差**

作者坦言，目前的 Claude 仍無法處理深層的概念性問題，也不是嚴格意義上的「科學家」；它需要被引導去找到適合自己能力的問題，而非被要求像人類研究者一樣思考。同時，絕大多數科學問題並不像數學那樣可以被完整陳述並絕對驗證，這正是目前 agentic AI 在科學應用上普遍存在的侷限。

🎯 **實務啟示**

這篇文章給做 AI 應用的工程師一個很實際的提醒：與其硬逼模型扮演它不擅長的角色，不如反過來盤點它真正擅長的能力組合（例如跨領域知識廣度、程式能力、處理機械式但高複雜度的計算），然後去尋找剛好吻合這組能力的問題。BootLoops 的經驗也顯示，讓模型自由探索、再由領域專家把關篩選方向，可能是目前人機協作科學研究較務實的模式。

🔗 **來源**
- 標題：Claude-shaped science
- 作者／機構：Prof. Matthew Schwartz（客座作者）／Anthropic
- 連結：https://www.anthropic.com/research/claude-shaped-science

#Anthropic #Claude #AIforScience #ScatteringAmplitudes #Bootstrap #AgenticAI #OpenSource #ScientificComputing #PhysicsResearch #LLM
