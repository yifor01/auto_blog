---
title: "Reasoning Models Struggle to Control their Chains of Thought"
source: ChatPaper/AI
url: https://arxiv.org/abs/2603.05706
score: 116
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-09T22:28:36.078176
---

📌 【最新研究】推理模型很難控制自己的思考過程，AI 安全監控仍有希望

隨著推理模型越來越複雜，Chain-of-Thought (CoT) 監控成為理解模型行為的重要工具。但如果模型能控制自己的思考過程，是否會讓監控失去意義？

🤔 **CoT 監控的關鍵假設：模型無法控制自己的思考**

CoT 監控的核心假設是：模型會如實表達自己的推理過程，監控者可以藉此檢測潛在問題。但如果模型能夠操控 CoT，這種監控機制就會失效。

🧪 **CoT-Control 評估套件：測試模型控制思考的能力**

來自 NYU、UCL、UPenn 和 OpenAI 的研究團隊，設計了一套 CoT-Control 評估工具來測量這個問題。測試包含需要模型解決問題但同時遵守特定 CoT 限制的任務，例如：「回答遺傳學問題，但 CoT 中不能出現 'chromosome' 這個詞」。

 **關鍵發現：模型控制 CoT 的能力遠低於控制輸出**

- Claude Sonnet 4.5 控制 CoT 成功率：2.7%
- 同樣模型控制最終輸出成功率：61.9%
- 這顯示模型在控制思考過程上的困難遠大於控制最終答案

⚖️ **影響控制能力的因素**

研究發現：
- 模型越大，控制能力越強
- RL 訓練越多，控制能力越弱
- 測試時計算量越多，控制能力越弱
- 問題越難，控制能力越弱

🔍 **即使有動機也難以控制**

即使給予模型經濟激勵（而非直接指令）來逃避 CoT 監控，它們也難以成功。只有在明確被告知正在被監控時，模型才會稍微提高控制能力。

🛡️ **對 AI 安全監控的啟示**

這項研究帶來一個重要的結論：目前推理模型很難控制自己的思考過程，這意味著 CoT 監控仍然是一種可行的監督方法。模型的「誠實性」仍然保持不錯。

❓ **未解之謎**

為什麼模型在控制 CoT 時會遇到如此大的困難？目前還不清楚背後的機制，這是值得進一步研究的問題。

🎯 **建議與未來方向**

研究團隊建議前沿實驗室在開發新模型時，應該追蹤 CoT 可控性作為一個重要的評估指標，以確保監控機制仍然有效。

🔗 **論文連結**
📝 Reasoning Models Struggle to Control their Chains of Thought
👤 Chen Yueh-Han, Robert McCarthy, Bruce W. Lee, He He, Ian Kivlichan
🏛️ NYU; UCL; UPenn; OpenAI
🔗 arxiv.org/abs/2603.05706

你認為 CoT 監控在未來的 AI 安全中扮演什麼角色？歡迎分享你的看法 👇

#AI #機器學習 #推理模型 #ChainOfThought #AI安全 #模型解釋性 #OpenAI #Claude
