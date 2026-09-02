---
title: 'Researchers from Princeton, Ant Group and Stanford Introduce AQuA: A Two-Part
  Agentic Framework for Autonomous Factor Discovery and Model Development in Quantitative
  Finance'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/01/aqua-a-two-part-agentic-framework-for-autonomous-factor-discovery/
model: claude-code/sonnet
generated_at: '2026-09-02T10:08:32.875499'
score: 90
---

📌 Princeton、Ant Group、Stanford 提出 AQuA：讓量化研究 Agent 不再靠洩漏資料贏基準

TL;DR：AQuA 把評估器鎖在自我迭代之外，避免研究型 Agent 用資料洩漏灌水績效。

會自己寫實驗的量化研究 Agent，有個容易被忽略的風險：一個其實有資料洩漏問題、卻在回測上表現亮眼的特徵，會被系統當成「成功案例」存下來，並在後續迭代中不斷被複製放大。光靠 prompt 層級的指示或另一個 Agent 當審查者並沒有用，因為寫程式的 Agent 跟審查的 Agent，往往有一樣的盲點。

🤔 **問題出在哪：Agent 既是選手也是裁判**

量化研究本來就容易被微小的方法論錯誤搞出「好看但不可複現」的回測結果，這個現象在 Bailey 等人的研究中已被記錄。當 Agent 自己寫實驗時，情況更糟：一個有洩漏問題的特徵一旦被存成先例，遞迴迭代會像放大真正的發現一樣，把未被察覺的 bug 也一起放大。反覆存取固定的 holdout 集合會造成適應性過度配適（adaptive overfitting），已有研究觀察到 LLM Agent 會鑽研究目標與評估器設計不夠嚴謹的漏洞。換句話說，prompt 層級的指示與模型互審，本質上都不是一道真正的完整性防線。

🧩 **不對稱自由：Agent 可以自由探索，但評估器不能被碰**

AQuA 由兩個獨立系統組成，一個在加密貨幣市場上做符號化 alpha 因子挖掘，另一個在美股上做時間序列模型開發，兩者不共用 Agent、記憶、候選空間或研究狀態。核心設計理念是「不對稱自由」：在每次迭代開始前，就先固定好資料切分方式、特徵與標籤定義、以及評估器本身，Agent 只被允許輸出一個受限的因子表達式，或是單一組態的差異修改（config diff）。也就是說，Agent 可以在自己的 DSL 內自由探索，但評估器本身完全在這個可調整的範圍之外，讓可能造成洩漏的動作從一開始就不存在。

Part I 是一條六個 Agent 組成的流程：Data Steward、Visual Analyst、Idea Miner、Factor Evaluator、Backtest Engineer 與 Research Librarian，全部由一個 AI Manager 統一調度，Agent 之間不會互相呼叫，每一次交接都要經過 Manager，確保整條流程可被稽核。一個因子在被組裝成標準化的 formulaic-alpha 運算子之前，必須先以「可證偽的提案」形式提出，包含假說、機制、預期方向與證偽條件。由於每個時間序列運算子只讀取過去的滑動視窗、每個橫斷面運算子只讀取當下時間點，因果性在組合運算下能維持封閉。系統內跑三種回饋迴圈：回測內的方向校準、單一 run 內基於證偽結果的信念更新，以及跨 run 的記憶機制，用來引導下一輪搜尋方向。

Part II 的任務是預測每支股票未來 30 分鐘的報酬，訓練資料為 2010 至 2019 年，2020 年完全設為隔離區間不被觸碰，2021 至 2025 年則是完全未被使用過的測試資料，模型選擇只使用訓練窗末端切出的內部驗證區段。這裡的一個「假說」就是架構、損失函數、取樣器或最佳化器上的單一組態差異，一個差異對應一個變體，確保變體之間可比較。預測模型是個混合架構：多尺度一維卷積前端、可配置的骨幹網路（涵蓋 LSTM、Mamba 與 attention，實際回報結果採用 attention 版本）、一個橫跨整個股票池做混合的橫斷面階段、閘控融合，以及逐股票的池化輸出層。

📊 **結果：因子挖掘與模型開發都優於各自的基準線**

在加密貨幣五分鐘頻率市場上，AQuA Part I 的組合驗證 Spearman IC 在 20 輪研究迭代中攀升到約 0.190：

| 方法 | 驗證 IC |
|---|---|
| AQuA（組合） | 0.190 |
| AlphaMemo（改編版） | 0.171 |
| AlphaGen（改編版） | 0.151 |
| LSTM | 0.137 |
| LightGBM | 0.106 |
| Alpha158-style 基準 | 0.075 |

值得注意的是，單一因子的 IC 只有 0.026 至 0.037，論文強調這代表整套研究流程本身的價值，而非單一因子表達式的貢獻。

Part II 在美股盤中資料上的逐股票原始 IC 比較：

| 模型 | 原始 IC |
|---|---|
| 混合模型 | 0.0843 |
| GRU | 0.0613 |
| LSTM | 0.0535 |
| xLSTM | 0.0434 |
| LightGBM | 0.0397 |
| Ridge | 0.0251 |

混合模型比最佳基準高出絕對值 0.0230，相對提升 37.5%。研究團隊也發現沒有任何單一價量特徵能單獨扛起訊號，最強的單一特徵（5 分鐘報酬）僅 −0.031，Ridge 組合後也只有 +0.025，逐股票 R² 為 1.20%。

把逐股票預測轉成美元中性的門檻多空組合、雙邊交易成本設為 2 個基點後，做產業中性化調整可將樣本外 Sharpe 拉高到 +2.15（訓練與樣本外數值幾乎相等）；疊加一個因果的波動率目標調整後進一步提升到 +2.50；即使改用完全因果、每個參數都只用過去資料選定的 walk-forward 方式，仍能達到 +2.00。2021 至 2025 逐年 Sharpe 分別為 +1.7、+3.5、+1.9、+1.8、+2.7，即使在 2022 年的下跌行情中依然維持正值。

⚠️ **兩套系統的 IC 不能直接互相比較**

論文明確指出，Part I 與 Part II 使用不同的 IC 計算慣例，兩者的數字不應該被拿來直接對照，這一點在解讀結果時要特別留意。

🎯 **實務啟示**

對於任何讓 LLM Agent 自主設計實驗、自動迭代研究流程的系統來說，AQuA 的「不對稱自由」是個值得參考的設計模式：與其事後靠人工審查抓資料洩漏，不如在架構層面就讓評估器與資料切分固定在 Agent 的可調整範圍之外，讓 Agent 的自由度只存在於受限的假說空間內，而非整個實驗流程。

🔗 **來源**
- 標題：Researchers from Princeton, Ant Group and Stanford Introduce AQuA: A Two-Part Agentic Framework for Autonomous Factor Discovery and Model Development in Quantitative Finance
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/01/aqua-a-two-part-agentic-framework-for-autonomous-factor-discovery/

#QuantitativeFinance #AIAgents #AlgorithmicTrading #LLMAgents #MachineLearning #FinTech #AIResearch #Princeton #StanfordAI #AntGroup
