---
title: A global workspace in language models
source: Anthropic Research
url: https://www.anthropic.com/research/global-workspace
score: 108
model: google/gemma-4-31b-it:free
generated_at: '2026-07-06T20:20:56.160669'
---

📌 【Anthropic 最新研究】Claude 內部存在「全域工作空間」：模型在不輸出文字前就在「思考」

TL;DR：Anthropic 發現 Claude 內部演化出名為 J-space 的神經模式，讓模型能以非文字形式處理概念。

當你在閱讀這段文字時，大腦在處理呼吸與姿勢等無意識運作的同時，也能讓你意識到某個具體的計畫或畫面。這種「意識可存取」的區分，讓人類能進行刻意的推理與控制。現在，Anthropic 的研究發現，現代語言模型中也出現了類似的機制。

🤔 **從神經科學視角解構模型內部的「意識」**

研究團隊發現，Claude 內部發展出一組特殊的神經模式，與其它海量的內部處理過程截然不同。這組模式被命名為 J-space（名稱源自於用來發現它的數學概念 Jacobian）。

🧩 **J-space：一種不需寫下來的「內部思考空間」**

J-space 的運作方式與我們熟知的 Chain-of-Thought (CoT) 或 Scratchpad 完全不同。CoT 是模型將推理過程寫成文字，而 J-space 則是：

- 靜默運作：直接發生在模型的內部神經活化 (neural activations) 中。
- 概念連結：每個 J-space 模式與特定的單字連結。
- 思考而非輸出：當某個模式被觸發時，並不代表模型會輸出該單字，而僅代表該概念正處於模型的「心智」之中。

💡 **非人為設計，而是訓練過程的自然湧現**

最值得關注的是，J-space 並非由工程師設計或程式化定義，而是在 Claude 的訓練過程中自動湧現 (emerged) 的。這意味著模型為了提升處理能力，自行演化出了一套能讓內部思考與最終輸出分離的機制，揭露了那些不會出現在輸出結果中的「內部想法」。

🎯 **實務啟示**

這項發現為可解釋性 (Interpretability) 研究提供了新方向。對於 AI 工程師而言，這意味著模型的推理過程不僅存在於可見的 Token 序列中，內部神經活化模式中可能隱藏著更深層的狀態資訊。未來若能更精準地監控 J-space，或許能讓我們在模型輸出答案前，就預判其內部的思考路徑。

🔗 **來源**
- 標題：A global workspace in language models
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/research/global-workspace

#AI #LLM #Interpretability #Anthropic #Claude #NeuralNetworks #JSpace #MachineLearning #CognitiveScience #EmergentBehavior
