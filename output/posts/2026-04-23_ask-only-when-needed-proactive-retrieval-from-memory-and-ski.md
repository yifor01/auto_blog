---
title: "Ask Only When Needed: Proactive Retrieval from Memory and Skills for Experience-Driven Lifelong Agents"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2604.20572
score: 113
model: tencent/hy3-preview:free
generated_at: 2026-04-23T19:39:43.396346
---

📌 【上海 AI Lab】讓 AI Agent 學會「只在必要時」檢索經驗

大多數現有的終身學習 Agent 在面對新任務時，往往被動地觸發檢索機制。這就像一個學生不管懂不懂都先翻書，而不是遇到瓶頸時才去思考如何查閱資料。這種「盲目檢索」不僅效率低落，更讓 Agent 錯失了在互動中主動發現知識缺口的機會。

🤔 **被動檢索的痛點：Agent 缺乏「求知慾」**

在長期任務中，Agent 需要不斷累積經驗。然而，現行方法通常只在任務開始或步驟結束後才去查詢記憶庫。這導致 Agent 在互動過程中無法精準識別「我現在缺什麼知識」，也無法根據當下的決策需求去主動獲取最有用的經驗。

🧪 **ProactAgent：將檢索定義為一種「策略動作」**

華東師範大學與上海 AI 實驗室的研究團隊提出了 **ProactAgent** 框架，其核心在於兩大創新：

1.  **ExpOnEvo (經驗增強的在線演化)**：建立結構化的經驗庫，將歷史互動分類為「事實記憶」、「情節記憶」與「行為技能」。這讓檢索不再只是找資料，而是能獲得具體的行動指引。
2.  **ProactRL (主動式強化學習檢索)**：這是技術的靈魂。研究團隊將「檢索」本身視為一個可學習的動作，並透過雙分支過程獎勵（Paired-branch process rewards）來訓練 Agent。簡單來說，系統會比較「檢索後的決策」與「不檢索的決策」哪個更好，從而讓 Agent 學會在能提升任務成功率或效率時才去檢索。

 **SciWorld 成功率 73.5%，檢索開銷大幅降低**

實驗結果顯示，ProactAgent 在 SciWorld 和 AlfWorld 等標準環境中表現出色：
- **SciWorld**：成功率高達 **73.50%**
- **AlfWorld**：達到 **71.28%**
- **StuLife**：表現與專有商業模型相當

更重要的是，這是在「大幅減少檢索開銷」的前提下達成的。Agent 學會了聰明地偷懶，只在關鍵時刻調用記憶。

💡 **從「盲目查詢」到「精準決策」的典範轉移**

這篇論文最值得關注的觀點是：檢索不應是背景作業，而應是決策流程的一部分。透過 ProactRL，Agent 發展出了一種類似人類的「元認知」能力，即判斷自己是否具備解決當前問題的知識，並主動尋求協助。這對於構建高效且具備持續學習能力的互動系統至關重要。

⚠️ **實驗環境與泛化能力的挑戰**

雖然論文展示了優異的數據，但目前實驗主要集中在特定的文字遊戲與模擬環境（SciWorld, AlfWorld）。在更複雜、動態的真實世界場景中，這種主動檢索策略的穩定性仍有待觀察。此外，結構化經驗庫的維護成本與擴展性，也是實務部署時需要考量的因素。

🎯 **實務啟示：打造更聰明的 LLM Agent**

對於正在開發 LLM Agent 的工程師來說，這提供了一個新的優化方向。與其讓 Agent 在每一步都進行昂貴的 RAG（檢索增強生成），不如嘗試引入強化學習來訓練 Agent 的「檢索時機」。這不僅能降低延遲與成本，還能提升 Agent 的自主性。

🔗 **論文連結**
📝 Ask Only When Needed: Proactive Retrieval from Memory and Skills for Experience-Driven Lifelong Agents
👤 Yuxuan Cai, Jie Zhou, Qin Chen, Liang He (East China Normal University; Shanghai AI Laboratory)
🔗 https://arxiv.org/abs/2604.20572

你覺得讓 Agent 學會「主動提問」和「主動檢索」，是實現真正的 AGI 的必經之路嗎？歡迎留言討論 👇

#AI #Agent #ReinforcementLearning #LifelongLearning #上海AI實驗室 #ProactAgent #MachineLearning
