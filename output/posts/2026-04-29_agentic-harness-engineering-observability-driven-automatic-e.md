---
title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2604.25850
score: 123
model: tencent/hy3-preview:free
generated_at: 2026-04-29T19:48:20.718145
---

📌 【復旦/北大研究】Harness 自動進化，讓 Coding Agent 效能提升 10%

你還在手工調整 Agent 的 Prompt 和工具定義嗎？當大家都在研究如何讓模型更聰明時，這篇來自復旦大學與北京大學的論文指出，決定 Coding Agent 成敗的關鍵其實是「Harness」（執行框架）。更驚人的是，他們證明了這個框架可以透過「可觀測性」全自動演化，且效能直接超越人類設計的版本。

🤔 **Harness 決定成敗，但手工調整已到極限**

在 Coding Agent 的開發中，Harness 定義了模型如何與程式庫、工具和執行環境互動。過去，這些 Harness 多由人工設計，但隨著 Agent 軌跡（Trajectory）動輒數百萬 Token，加上評估訊號稀疏且雜訊多，傳統的試錯（Trial-and-Error）方式已經很難再提升效能。如何讓 Harness 的演進不再只是黑箱操作，成為這篇論文試圖解決的核心痛點。

🧪 **三層可觀測性架構，將編輯轉化為可驗證合約**

研究團隊提出了 **Agentic Harness Engineering (AHE)** 框架，核心在於為工程循環的三個階段（編輯、檢視、決策）分別注入可觀測性：

1. **元件可觀測性**：將所有可編輯的 Harness 元件轉化為檔案級別的表示，讓動作空間明確且可回溯。
2. **經驗可觀測性**：將數百萬 Token 的原始軌跡蒸餾成結構化的「證據語料庫」，讓演化中的 Agent 能真正消化這些經驗。
3. **決策可觀測性**：每一次編輯都必須伴隨一個「自我預測」，並在下一輪任務中驗證結果。

這種設計將每一次修改變成了具備「可偽證性」的合約，讓系統能自主演化，而不會陷入無效的亂試。

 **自動演化效能突破 77%，超越人類設計**

在 Terminal-Bench 2 的實驗中，經過 10 次 AHE 迭代：
- 效能從基準的 **69.7%** 提升至 **77.0%**。
- 成功超越了人類精心設計的 Harness (Codex-CLI 的 71.9%)。
- 甚至擊敗了現有的自演化基準 (ACE 與 TF-GRPO)。

💡 **進化出的不是調參技巧，而是通用工程經驗**

這項研究最值得關注的發現是「遷移性」。研究團隊將演化後的 Harness 凍結後直接套用：
- 在 **SWE-bench-verified** 上，成功率達到頂尖水準，且消耗的 Token 比原始版本減少了 **12%**。
- 在 **Terminal-Bench 2** 上，跨模型家族（三種不同模型）測試時，效能額外提升了 **5.1 到 10.1 個百分點**。

這證明了 AHE 演化出的不是針對特定基準的過擬合，而是具備通用性的工程經驗。

⚠️ **複雜度與計算成本的權衡**

雖然 AHE 實現了自動化，但架構本身引入了額外的可觀測性層（如軌跡蒸餾與合約驗證），這意味著在初期設定與迭代過程中，對計算資源與日誌系統的要求較高。此外，目前的驗證主要集中在 Coding 場景，其他類型 Agent 的泛化能力尚待觀察。

🎯 **工程化 Agent 的下一步：擁抱可觀測性**

對於正在構建生產級 Agent 的開發者來說，這篇論文提供了一個明確的實踐方向：
- 不要只關注模型本身，Harness 的設計品質是隱形的天花板。
- 建立「決策可觀測性」，讓每一次修改都有據可查，有預測可驗證。
- 透過結構化的經驗回饋，讓 Agent 框架具備自我進化的能力。

🔗 **論文連結**
📝 Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses
👤 Jiahang Lin, Shichun Liu, Chengjun Pan, Lizhi Lin, Shihan Dou
🏫 Fudan University; Peking University; Shanghai Qiji Zhifeng Co., Ltd
🔗 https://arxiv.org/abs/2604.25850

你覺得 Agent 的框架自動演化，會是下一個技術爆發點嗎？歡迎在留言區討論 👇

#AI #Agent #CodingAgent #MachineLearning #NLP #軟體工程 #復旦大學 #北京大學 #自動化
