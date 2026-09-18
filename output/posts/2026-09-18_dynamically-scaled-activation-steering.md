---
title: Dynamically Scaled Activation Steering
source: Apple ML
url: https://machinelearning.apple.com/research/dynamically-scaled-activation-steering
model: claude-code/sonnet
generated_at: '2026-09-18T19:52:25.439611'
score: 91
---

📌 【Apple ML研究】不是每次生成都需要steering，那該何時介入？

TL;DR：DSAS讓activation steering依輸入動態調整強度，在毒性抑制與效能間取得更好平衡。

多數activation steering方法有個共同盲點：不管輸入內容是否真的需要介入，一律套用同樣強度的干預。這樣做的代價是,當模型本來就不會說出有害內容時，steering反而在拖累它原本該有的表現。Apple ML的這篇研究,想解決的正是「何時該介入」與「該怎麼介入」被綁在一起的問題。

🤔 **均勻施加的steering，會在不需要時傷害效能**

Activation steering已經成為引導生成模型行為（例如緩解毒性內容）的有力方法，但論文指出，現有方法大多對所有輸入一視同仁地套用相同的干預強度。問題在於：當某個輸入本來就不會觸發不良行為時，這種「一律介入」的做法會不必要地拉低模型的效能與可用性。

🧩 **DSAS：把「何時steer」和「怎麼steer」拆開來決定**

作者提出Dynamically Scaled Activation Steering（DSAS），這是一個method-agnostic（方法無關）的steering框架，核心想法是把「什麼時候該進行干預」與「用什麼方式進行干預」這兩個決策解耦。DSAS會在跨層與跨輸入的維度上，自適應地調節既有steering轉換的強度，只在偵測到有不良行為傾向時才強力介入。在生成階段，DSAS會計算與上下文相關的縮放係數（context-dependent scaling factors），用它來動態調整任何steering方法的介入強度。論文也說明了DSAS可以與steering函式一起進行端到端（end-to-end）的聯合最佳化，而不只是作為外掛在既有方法之上運作。

📊 **在毒性抑制與跨模態驗證上都改善了Pareto front**

論文指出，當DSAS與現有steering方法結合時，相較於單純套用steering方法，能持續改善Pareto front，在毒性抑制與效能（utility）維持之間取得更好的權衡——也就是在同等程度的毒性抑制下，模型能保留更多原本的能力，反之亦然。為了證明DSAS的通用性，作者也將其套用到文字生成圖片（text-to-image）的diffusion模型上，展示了自適應steering如何用來調節特定概念的生成強度。此外，論文特別強調DSAS帶來的運算負擔極小，同時還提升了可解釋性：它能具體指出哪些token需要被steering、以及需要多大的調整幅度，這讓steering的介入過程不再是黑箱操作。

⚠️ **論文本身未提供的部分**

素材中並未給出具體的實驗數值（如毒性抑制分數、utility指標的實際數字，或與哪些baseline方法的直接比較數據），因此這部分的效果幅度仍待查閱論文全文確認。作者表示程式碼將於GitHub上開源，但截稿時尚未提供實際連結。

🎯 **實務啟示**

如果你的團隊在生產環境中已經在用activation steering做內容安全控制，DSAS這類「按需介入」的思路值得關注：與其對每個輸入都套用固定強度的干預（犧牲一部分模型能力換取安全性），更精細的做法是先判斷這次生成是否真的有風險，再決定介入力道。這對於既要維持安全防線、又不想犧牲模型正常能力的場景（例如客服機器人、創作輔助工具）會是更務實的權衡方式，而且由於DSAS宣稱method-agnostic，理論上可以直接套用在團隊現有的steering pipeline上，不需要重新設計整套機制。

🔗 **來源**
- 標題：Dynamically Scaled Activation Steering
- 作者／機構：Alex Ferrando de las Morenas、Xavier Suau Cuadros、Jordi Gonzàlez Sabaté、Pau Rodríguez Lopez
- 連結：https://machinelearning.apple.com/research/dynamically-scaled-activation-steering

#ActivationSteering #AppleML #Interpretability #LLMSafety #ToxicityMitigation #DiffusionModels #TMLR #AIAlignment #MachineLearning #ModelSteering
