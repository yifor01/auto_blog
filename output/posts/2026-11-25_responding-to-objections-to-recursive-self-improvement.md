---
title: Responding to objections to recursive self-improvement
source: Dwarkesh
url: https://www.dwarkesh.com/p/rsiobjections
model: claude-code/sonnet
generated_at: '2026-11-25T01:47:54.358943'
score: 71
---

📌 Dwarkesh 回應超級智慧質疑：資料才是關鍵

TL;DR：Dwarkesh Patel 逐一回應「2030 超級智慧」爭議，核心論點落在 AI 研究是否能自我產生進步所需的資料。

當一個人說「我預期 2030 年前會出現超級智慧」，最常見的反駁是：你有沒有真正用這些工具做過正事？Dwarkesh Patel 在這篇回應文章裡，先接下了這個略帶挑戰意味的提問，再把討論帶到一個更核心的技術問題：能不能找到可以持續 hill-climb 的指標，以及能不能持續生成讓模型在那些指標上進步的資料。

🤔 **「你有真正的工作嗎」背後的真實爭論**

文章開頭引用讀者 Jim 的留言質疑 Dwarkesh 是否每天真的在用 AI 工作。Dwarkesh 的回應是：他確實每天在用，但他同時也是過去一年半以來，一直在強調當前模型缺乏基本學習能力、因而拖累生產力的人之一。他指出 IT 只佔經濟的 1%，範圍明確的 coding 任務又只是其中一小部分，AI 在多數事情上目前其實還不如人類；但在有大量可驗證代理指標（verifiable proxies）的領域，比如數學與 AI 研究本身，AI 已經達到或超越人類水準。他的推論是：AI 研究方向上不成比例的進展，會壓縮成像 GPT-3 到 GPT-6 之間那樣的能力跨度，而這個跨度未來可能被壓縮進一年之內完成。

🧩 **Cindy Wu 的質疑：定義指標本身就是難題**

Cindy Wu 在 X 上提出的反駁被引用：定義一個不會被 Goodhart 掉、不會被 reward hacking 的指標，需要對應的資料與環境，而這正是做出 AGI 最困難的部分，Dwarkesh 被指「用 AI 會自動產生資料」這句話輕輕帶過了這個難題。

🧩 **拆成兩個子問題：指標存在嗎、資料從哪來**

Dwarkesh 把這個質疑拆成兩部分回應。第一，他認為預訓練在 held-out 語料上的 loss 不只是進度的代理指標，它本身就是預訓練進步的基礎，且高度可驗證；此外還有一批與特定技術路線無關的通用指標，例如 AI 能多快掌握一款從沒見過的電玩、能多快只靠 1700 年以前的資料推導出廣義相對論、能解開多少道開放數學難題。他認為這些突破之所以能在許多不同指標上同時被量測到，是因為智慧本身是通用的，一旦有真正的突破，就會在現實世界的各個面向同時顯現出來，就像 Transformer 原本是為了打敗翻譯任務的 SOTA 而發明,卻同時在 WikiText 的下一個 token 預測、圖像生成等任務上表現優異;推理模型最初只是為了解高中數學與簡單 coding 題而被除錯,如今也被套用到許多不同領域。

🧩 **資料從哪來：Jerry Han 的研究**

第二部分是資料如何被生產出來。Dwarkesh 提到他們與普林斯頓學生 Jerry Han 合作，花費大約數萬到十萬美元等級的 GPU 資源做了一項研究：比較 2019 到 2026 年間的資料語料與架構，看哪一項更能解釋預訓練進步。結果顯示資料對進步的解釋力大於架構，而資料變得更好的方式，主要來自更好的資料過濾方法與更好的合成資料生成方法，而這些都是 ML 研究者在自己的電腦上就能完成的empirical science工作，不需要僱用法律、金融或莎士比亞研究等各領域的專家來手工產出範例，單純透過改變過濾或合成資料的方式,觀察最終模型在數學、法律等任務上的表現變化即可。

💡 **深入分析：為什麼這個論點值得認真對待**

這段對話的關鍵在於，Dwarkesh 並非主張「資料問題不存在」，而是主張資料改善的性質，恰好是 ML 研究者這群「不懂任何特定領域、只懂 ML 研究」的人就能持續完成的工作，這也是他認為 AI 研究本身能被自動化、進而觸發自我加速循環的核心依據。

⚠️ **對話在此處尚未完結**

文章末尾留下一個懸而未決的問題：「能不能把這些 ML 研究者本身自動化？」Dwarkesh 與 Max Farrens 的對談在此處轉向下一個子議題，素材本身並未給出答案。

🎯 **對工程師的意義**

這篇文章提醒工程師在評估「AI 研究自動化」的說法時，應該把注意力放在兩個具體問題上：你信任的能力指標是否真的可驗證、不會被 Goodhart；以及支撐這個指標持續進步的資料改善工作，究竟是需要領域專家的手工知識，還是像文中所說、主要是資料過濾與合成方法上的 ML 研究工作。這會直接影響你對「下一代模型能力會不會突然跳一大步」這類預測該給多少可信度。

🔗 **來源**
- 標題：Responding to objections to recursive self-improvement
- 作者／機構：Dwarkesh Patel
- 連結：https://www.dwarkesh.com/p/rsiobjections

#RecursiveSelfImprovement #AGI #AIResearch #Superintelligence #PretrainingData #SyntheticData #MLResearch #AIAlignment #DwarkeshPatel #AIForecasting
