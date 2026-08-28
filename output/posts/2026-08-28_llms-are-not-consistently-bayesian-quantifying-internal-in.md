---
title: 'LLMs Are Not (Consistently) Bayesian: Quantifying Internal (In)consistencies
  of LLMs’ Probabilistic Beliefs'
source: Apple ML
url: https://machinelearning.apple.com/research/llms-not-consistently-bayesian
model: claude-code/sonnet
generated_at: '2026-08-28T18:02:47.739732'
score: 92
---

📌 蘋果研究：LLM 的機率信念更新,其實不太貝葉斯

TL;DR：蘋果團隊發現 LLM 更新機率信念時常偏離貝葉斯法則,而偏離的「捷徑」在任務表現上反而更好。

如果一個 AI 系統要在醫療、科學、法律這類沒有標準答案的領域做決策,它得先學會一件事：看到新證據時,該怎麼合理地調整自己的信念。這篇研究要問的是——LLM 真的做得到這件事嗎？

🤔 **沒有單一正解的領域,考驗的是信念更新能力**

論文指出,現代 AI 系統正被部署到醫療、科學、法律等複雜領域,這些場景往往沒有單一正確答案。系統必須能夠表徵並隨新證據更新不確定的信念,才能做出理性決策。研究團隊提出一項新方法：把 LLM 當作「資訊處理規則」來研究,並利用「資訊處理落差」（information processing gap,即模型更新結果與貝葉斯更新之間的偏差）,來量化 LLM 內部信念更新的一致性。

🧩 **評估 LLM 吸收證據的多種方式**

團隊評估了多種 LLM 將證據納入信念更新的方法。其中一些方法會產生（近似）貝葉斯更新,也就是理論上最優的資訊處理方式；另一些則是使用模型學到的啟發式（heuristic）捷徑,而非嚴格遵循貝葉斯法則。

📊 **意外發現：不理性的捷徑,任務表現反而更好**

研究結果顯示,那些非貝葉斯的啟發式更新,在下游任務表現上經常優於精確的貝葉斯更新——儘管後者理論上才是最優的資訊處理方式。作者認為,這說明 LLM 內部對世界的機率模型本身可能是「設定錯誤」（misspecified）的,也就是模型對世界的機率假設本身就不準確,因此嚴格套用貝葉斯法則反而放大了這個錯誤假設帶來的偏差。

💡 **這個落差指標可以當作系統診斷工具**

研究團隊也展示了這項「資訊處理落差」的量測方式,可以用來作為診斷工具,找出以 LLM 為核心的推論系統可能存在的問題。

🎯 **實務啟示**

如果你正在建構依賴 LLM 做不確定性推理或機率判斷的系統（例如結合證據逐步更新信念的診斷輔助、風險評估工具）,不能想當然地假設「讓模型看起來更貝葉斯」就等於更可靠。這篇研究提醒工程師,在部署到高風險領域前,應該實際測量模型的信念更新是否與任務表現一致,而不是只看更新方式在理論上是否「正確」。

🔗 **來源**
- 標題：LLMs Are Not (Consistently) Bayesian: Quantifying Internal (In)consistencies of LLMs' Probabilistic Beliefs
- 作者／機構：Chacha Chen、Matthew Jörke、Adam Goliński、Masha Fedzechkina、Guillermo Sapiro、Sinead Williamson、Nicholas Foti（Apple ML，部分作者來自 Stanford University）
- 連結：https://machinelearning.apple.com/research/llms-not-consistently-bayesian

#AppleML #LLM #BayesianInference #UncertaintyQuantification #MachineLearning #ProbabilisticModeling #AIResearch #ModelEvaluation #DecisionMaking #NLP
