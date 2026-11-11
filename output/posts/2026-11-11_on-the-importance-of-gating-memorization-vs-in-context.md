---
title: 'On the Importance of Gating: Memorization vs. In-Context Learning in State
  Space Models'
source: Apple ML
url: https://machinelearning.apple.com/research/gating-memorization-in-context
model: claude-code/sonnet
generated_at: '2026-11-11T23:53:54.574118'
score: 90
---

📌 SSM 學不會 in-context learning？問題可能出在 gating

TL;DR：Apple 與 Harvard 研究指出，State Space Model 的 gating 機制會讓模型先學會死記硬背，進而拖慢甚至阻礙它學會 in-context learning。

State Space Model（SSM）號稱是 Transformer 的理想替代品：固定記憶體用量、計算複雜度隨序列長度線性成長。但奇怪的是，即便 SSM 在多數任務上表現尚可、計算特性也很誘人,它在需要 in-context learning 與精確檢索的任務上卻始終落後 Transformer，這個差距正是拖慢 SSM 在大規模語言建模中普及的關鍵原因。

🤔 **效能瓶頸從哪裡來**

這篇研究試圖回答一個具體問題：SSM 在 in-context learning 與精確檢索上的落後,究竟是架構本身的根本限制,還是訓練過程中的某種偏差造成的?

🧩 **解剖 gating：先學會死記，才學會現場學習**

作者透過理論與實驗證明，SSM 中普遍存在的 gating 機制,是解釋這個現象成功與失敗兩面的關鍵。具體來說,gating 機制會讓 SSM 優先學會一種「in-weights」的記憶化解法，進而延遲、甚至在某些情況下完全阻止模型收斂到正確的 in-context learning 解法。研究特別指出,這個現象即便在架構本身或記憶容量都沒有根本限制的情況下依然會發生，也就是說，問題不在於模型「能不能」學會 in-context learning，而在於訓練動態本身引導模型先走向了記憶化這條路。

💡 **gating 是雙面刃**

另一方面，研究也發現 gating 對於提升模型在長序列長度上的泛化能力往往是有益的。換言之，同一個機制同時造成了記憶化與 in-context learning 之間的張力，又在長序列泛化上扮演正面角色，這讓 gating 的設計變成一個必須權衡取捨的問題。

⚠️ **理論洞察，但方案仍待後續工作**

目前公開的摘要內容聚焦於診斷問題本身：透過理論與實驗說明 gating 如何同時影響訓練動態與泛化表現，但並未在摘要中給出具體的新架構或修正方案的量化結果。

🎯 **實務啟示**

對於正在評估或設計線性時間序列模型的工程師，這項研究提供了一個重要提醒：如果你的任務高度依賴精確的 in-context 檢索或少樣本學習，帶 gating 的 SSM 在訓練初期可能會優先學到記憶化捷徑，這可能影響 checkpoint 選擇與早停策略；反之，若長序列泛化才是重點，gating 仍是有價值的設計。這篇研究為理解與改進線性時間模型提供了理論基礎，值得後續在 gating schedule 或分階段訓練策略上做更多嘗試。

🔗 **來源**
- 標題：On the Importance of Gating: Memorization vs. In-Context Learning in State Space Models
- 作者／機構：William L. Tong, Aryo Lotfi, Emmanuel Abbe, Kostas Vaggelakos, Vishnu Banna, Etai Littwin, Josh Susskind, Cengiz Pehlevan, Eran Malach（Apple 與 Harvard University 合作研究，刊於 NeurIPS）
- 連結：https://machinelearning.apple.com/research/gating-memorization-in-context

#StateSpaceModels #InContextLearning #Transformers #MachineLearning #AppleML #NeurIPS #SequenceModeling #DeepLearning #Memorization #AIResearch
