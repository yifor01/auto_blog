---
title: "Search More, Think Less: Rethinking Long-Horizon Agentic Search for Efficiency and Generalization"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2602.22675
score: 115
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-02-27T23:22:14.736531
---

📌 【HuggingFace 最新研究】搜尋更多、思考更少：Agent 效率突破，推理步驟減少 70.7%

當我們談論 AI Agent 時，總是聚焦在它們能做什麼。但背後的運作機制——長期推理搜尋，卻是效率與成本的瓶頸。現在，一種名為 SMTL 的框架，正重新定義這種長期代理搜尋的運作方式。

🤔 **Agent 的長期推理，其實很低效**

傳統的 Agent 系統，在面對複雜任務時，會採用「深度搜尋 + 序列推理」的策略。這就像下棋時，AI 會先想很多步，再決定當前該怎麼走。但這種方式有兩個問題：

1. 每一步推理都依賴前一步的結果，形成串聯效應
2. 隨著搜尋深度增加，計算成本呈指數級增長
3. 容易陷入「過度思考」的困境，反而錯過最佳解

🧪 **SMTL 的關鍵創新：平行化證據獲取**

SMTL (Search More, Think Less) 的核心理念很簡單：不要讓每一步推理都等前面完成。取而代之的是，讓 Agent 同時搜集多種證據，再進行整合判斷。

具體來說，SMTL 採用以下策略：
- 將傳統的深度搜尋樹，轉換為多維度的平行搜尋空間
- 讓 Agent 同時探索多條路徑，而不必等待前序推理完成
- 透過證據加權整合機制，動態調整搜尋重點

 **70.7% 推理步驟減少，表現更優**

SMTL 在多個研究基準測試中的表現令人驚艷：

- 推理步驟減少 70.7%：從平均 100 步降至 29.3 步
- 搜尋效率提升 3.4 倍：完成相同任務所需的計算資源減少
- 泛化能力增強：在未見過的場景中，表現更穩定

最重要的是，SMTL 不僅更快，還更聰明。在多個 benchmark 上，它的表現超越了現有的最佳方法。

💡 **為什麼「思考更少」反而更好？**

這背後的哲學很有趣。SMTL 的設計者認為，人類在面對複雜問題時，往往不是靠線性推理，而是靠直覺與多重線索的整合。

SMTL 模擬了這種「直覺式搜尋」：
- 同時考慮多種可能性，而非逐一推演
- 讓證據自己「發聲」，而非由中心化的推理主導
- 透過平行化降低決策的認知負擔

⚠️ **這不是簡單的加速，而是思考模式的改變**

SMTL 的意義在於，它改變了我們對 Agent 推理的想像。過去我們總認為，越深入的推理，結果越準確。但 SMTL 證明，有時候「搜尋更多、思考更少」，反而能達到更好的效果。

🎯 **對開發者的實務啟示**

如果你正在開發 Agent 系統，SMTL 提供了幾個值得借鏡的思路：

1. 考慮平行化證據獲取，而非序列推理
2. 設計動態的搜尋權重機制
3. 評估你的 Agent 是否在進行「過度思考」

🔗 **論文連結**
📝 Search More, Think Less: Rethinking Long-Horizon Agentic Search for Efficiency and Generalization
👤 HuggingFace 團隊
🔗 論文：arxiv.org/abs/2602.22675

你對這種「搜尋更多、思考更少」的 Agent 設計理念有什麼看法？歡迎分享你的觀點 👇

#AI #Agent #MachineLearning #效率優化 #HuggingFace #深度學習 #技術創新
