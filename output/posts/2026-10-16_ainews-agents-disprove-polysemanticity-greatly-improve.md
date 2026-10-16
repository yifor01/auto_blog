---
title: '[AINews] Agents disprove Polysemanticity; greatly improve Interpretability
  & Alignment'
source: Latent Space
url: https://www.latent.space/p/ainews-agents-disprove-polysemanticity
model: claude-code/sonnet
generated_at: '2026-10-16T20:12:47.807427'
score: 94
---

📌 Goodfire 研究員翻案：多義性神經元其實沒那麼難懂

TL;DR：Goodfire 研究員主張多數「多義性」神經元可被 agentic 分析重新解讀，可解釋性卡關的程度被高估了。

可解釋性領域長期有一個揮之不去的夢魘：神經網路裡的神經元常常同時代表好幾個不相關的概念，糾成一團人類難以拆解的「結」，這就是所謂的 polysemanticity（多義性）與 superposition（疊加）。如果大部分神經元都長這樣，那「看懂模型在想什麼」幾乎是不可能的任務。但 Goodfire 的研究員 Nick Cammarata 最近丟出一個挑戰這個共識的說法。

🤔 **多義性曾被當作可解釋性的天花板**

Cammarata 回顧自己 2023 年在 OpenAI 做自動化可解釋性（automated interpretability）研究時的結果：當時只有約 2% 的神經元被判定為「可讀」，其餘絕大多數都被歸類為難以理解的多義性神經元。這個數字在過去幾年成為業界普遍引用的悲觀基準，暗示著模型越大、越難被人類理解。

💡 **用 agent 重新檢查，多數「結」其實能解開**

Cammarata 在新文章中提出他目前的工作假設：「Neural Networks Are Already Clean」。他的論點是，許多過去被標記為多義性、疊加糾結的著名案例，其實是被誤讀了。當進一步用 agentic 分析去檢視這些神經元時，許多原本看起來糾纏不清的「結」會被解開，變得可以理解。他主張，在規模一路到數兆參數的模型中，多數神經元其實是「乾淨」、可被解讀的，而不是像過去認為的那樣普遍混亂。

這個說法得到一些關注，包括 tszzl 等人將其稱為一個重要的時刻。摘要也提到，這延續了 Goodfire 去年與 Anthropic 一起觀察到的「可解釋性方法隨規模擴大而受益」（bitter-lesson scaling）的脈絡。

⚠️ **這仍是一篇論述性文章，不是可直接複現的論文**

目前能看到的資訊來自新聞彙編對這篇文章的轉述，並非原始論文或完整方法細節：沒有具體的評測資料集、沒有可複現的實驗設置，也沒有明確的「乾淨神經元」比例數字（只有 2023 年那篇舊研究的 2% 作為對照）。換句話說，這是一個值得關注的工作假設與論述方向，但其穩健性仍有待同行與社群的進一步檢視。

🎯 **對從事可解釋性工作的工程師而言**

如果你曾因為「多義性無法解決」而放棄深入分析模型內部表徵，這篇文章提示的方向是：先別急著下結論，試著用更強的 agentic 工具重新檢視那些「看起來糾結」的神經元，有些可能比想像中更容易拆解。但在看到具體可複現的方法與資料之前，仍應保持審慎。

🔗 **來源**
- 標題：[AINews] Agents disprove Polysemanticity; greatly improve Interpretability & Alignment
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-agents-disprove-polysemanticity

#Interpretability #AIAlignment #Polysemanticity #Superposition #Goodfire #MechanisticInterpretability #AgenticAI #AISafety #NeuralNetworks #MachineLearning
