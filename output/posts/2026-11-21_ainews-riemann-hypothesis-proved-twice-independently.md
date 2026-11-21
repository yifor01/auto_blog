---
title: '[AINews] Riemann Hypothesis proved...twice independently'
source: Latent Space
url: https://latent.space/p/ainews-riemann-hypothesis-proved-twice-independently/
model: claude-code/sonnet
generated_at: '2026-11-21T22:15:45.477989'
score: 113
---

📌 【Anthropic 研究員跨界數學】黎曼猜想一天內冒出兩份證明

TL;DR：Anthropic 研究員用 Claude 寫出一份機器驗證的黎曼猜想證明，同一天又有人類獨立交出手寫證明。

數學史上最著名的未解問題，黎曼猜想，困擾了數學家一百六十多年。結果在短短幾個小時內，兩位數學家各自宣稱找到了證明。一份是跟 AI 合作、幾乎沒有人完整讀過的 Lean 程式碼；另一份是純人力耗費十二年、長達 940 頁但外界質疑可能有技術瑕疵的手寫稿。這個對比本身，可能比證明結果更值得工程師停下來想一想。

🤔 **兩份證明幾乎同時出現**

根據 Scientific American 的報導，Anthropic 的數學家 Levent Alpöge 宣布「與 Claude 合作」找到了黎曼猜想的證明，而且這個方法還涵蓋了廣義黎曼猜想（GRH）。幾乎同一時間，Alessandro Masullo 也公開了自己耗費十二年、純人力完成的獨立證明，據報導這份稿件約 940 頁，而且在公開前已經經歷過秘密的人工審查與修訂。

🧩 **Claude 帶他飛到了自己看不懂的地方**

根據 timeline 整理，這項工作從 10 月 6 日展開，20 個步驟中的 8 個在 11 月 15 日完成，最後一條記錄在 11 月 16 日寫下「GRH」。Alpöge 坦言，涉及高階群上自守形式（automorphic forms on higher-rank groups）的部分主要歸功於 Claude，而這正是他自己掌握不多的領域。他形容:「Claude 在終點線前遠遠超越了我。不，Claude 是飛起來的，還跳舞、還閃閃發光。」最終釋出的只有 Lean 程式碼，若要寫成自然語言的完整論述，據估計篇幅會超過 25 萬頁。

📊 **已知的驗證進度，與尚未解開的疑慮**

數學家 Elliot Glazer 確認，形式化後的敘述確實就是 GRH，並表示 Lean 出現 bug 的機率遠低於 1%；若程式碼能順利編譯完成且沒有額外引入公理，證明大機率是對的。但 Artificial Analysis 也提醒，目前兩項 AI 宣稱破解的千禧年問題，包括這份 RH 證明和 OpenAI 九月發布、使用未公開模型的 Navier-Stokes 證明，都仍屬未驗證狀態。後者更是前車之鑑：曾有批評者指出其 Lean 證明與自然語言描述的結果並不吻合。社群對此也出現不同解讀，有人認為這更多顯示我們其實不太清楚數學問題「客觀上」有多難，而不是 AI 展現了全面的超人類能力；也有人將這種做法類比為奧林匹亞式的「硬幹」，只是規模遠遠超出人類的耐力範圍。消息傳出當天，Anthropic 母公司股價下跌約一成。

💡 **看得懂 vs 看不懂，誰才是「敷衍」？**

Alpöge 自己提到一個耐人尋味的矛盾：他說「在還沒完全掌握這整個數學鄰域之前，就向世界提出一個完整的論證」，顯然不適合發表成那種讀者難以理解的大雜燴論文，所以他選擇只公開 Lean 程式碼。這恰好碰上了一個常被提起的準則:「當我們投入的努力少於要求讀者理解所需的努力，那就是 slop。」然而眼前這堆沒人完整讀過的 Lean 程式碼，卻是可驗證為真、且在人類歷史上意義重大的成果。這也呼應了另一個討論方向：一般人使用 agent 的經驗是「強引導弱」，由人類主導方向；但 Alpöge 的經歷恰好相反，他只在早期階段與 Claude 合作，之後就被遠遠拋在後面，變成需要摸索如何監督一個在特定領域已經比自己強的系統。

🎯 **實務啟示**

對工程師而言，這個案例提醒我們：AI 產出的正確性與可理解性正在脫鉤，驗證流程（如 Lean 的形式化檢查）會比「看得懂」更快成為信任的基礎。在設計自己的 AI 輔助工作流時，也該提早思考如何為「AI 懂、人不懂」的中間產物建立可驗證的檢查機制，而不是假設人類永遠能逐行審閱。

🔗 **來源**
- 標題：[AINews] Riemann Hypothesis proved...twice independently
- 作者／機構：Latent Space
- 連結：https://latent.space/p/ainews-riemann-hypothesis-proved-twice-independently/

#RiemannHypothesis #Anthropic #Claude #LeanProver #FormalVerification #Mathlib #AIforMath #MillenniumPrize #MachineLearning #AIResearch
