---
title: "Learning Next Action Predictors from Human-Computer Interaction"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2603.05923
score: 118
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-09T22:21:40.455300
---

# 📌 【Stanford 最新研究】AI 學會從你的螢幕行為預測下一步動作

你每天在電腦或手機上點擊、捲動、切換的每一個動作，都在告訴 AI 你接下來會做什麼。Stanford 團隊提出「Next Action Prediction」技術，讓 AI 能從長期的人機互動歷史中，學會預測你的下一步行為。

🤔 **AI 要真正「主動」服務，必須先學會「預測」**

當前 AI 助手只能被動回應我們的提問，但真正有用的 AI 應該能主動提供幫助。這需要 AI 理解我們的「上下文」— 不只是我們說了什麼，還包括我們看到了什麼、點擊了什麼、使用裝置的模式是什麼。

🧪 **360K 個動作、1,800 小時螢幕時間的學習成果**

研究團隊收集了 20 位使用者一個月內的手機使用數據（1,800 小時螢幕時間），並標註了超過 360,000 個互動動作。他們開發了 LongNAP 模型，能從這些長期互動歷史中學習用戶行為模式。

💡 **LongNAP 的關鍵創新：結合記憶與推理**

LongNAP 使用了兩種學習方式：
- **參數學習**：透過訓練學習通用模式
- **情境學習**：在面對新情境時，能從過去的類似經驗中提取相關資訊

這就像人類面對新問題時，會回想過去類似的經驗來解決當前問題。

🎯 **預測準確率達 17.1%，高度自信時提升至 26%**

使用 LLM 作為評分標準（0-1 相似度），LongNAP 的預測結果：
- 平均情況下，17.1% 的預測與實際行動高度吻合
- 在高度自信的預測中，準確率提升至 26%

這意味著 AI 已經能夠在相當比例的情況下，準確預測用戶的下一步動作。

⚠️ **研究限制與未來挑戰**

- 目前仍需大量標註數據
- 預測準確率仍有提升空間
- 如何處理更複雜、更長期的互動模式

🔗 **論文連結**
📝 Learning Next Action Predictors from Human-Computer Interaction
👤 Omar Shaikh, Valentin Teutschbein, Kanishk Gandhi, Yikun Chi, Nick Haber @ Stanford University; Hasso Plattner Institute; New York University
🔗 論文：arxiv.org/abs/2603.05923

這項研究為未來真正主動的 AI 助手奠定了基礎。你期待 AI 能預測你的下一步動作嗎？歡迎分享你的想法！

#AI #MachineLearning #人機互動 #主動式AI #Stanford #NextActionPrediction #科技前沿
