---
title: "Agentic-imodels: Evolving agentic interpretability tools via autoresearch"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.03808
score: 121
model: tencent/hy3-preview:free
generated_at: 2026-05-06T20:07:14.058440
---

📌 【Microsoft Research 最新研究】Agentic-imodels：演化 AI 代理專用可解釋工具

當前絕大多數數據科學工具都標榜「人類可解釋」，但負責執行數據工作的 AI 代理根本無法有效理解這些工具。
微軟最新研究顯示，換用專為代理設計的可解釋工具後，Copilot CLI、Claude Code 等系統的效能最高提升 73%。

🤔 **AI 代理主導數據科學工作，現有工具卻僅針對人類設計**
Agentic Data Science (ADS) 系統正快速發展，已能自主完成數據分析、模型擬合與結果解讀，未來絕大多數數據科學工作都可能由 AI 代理完成。但當前 ADS 系統使用的統計工具，都是設計給人類解讀的，並未考慮 AI 代理的理解需求，形成關鍵的工具缺口。

🧪 **Agentic-imodels 自動研究迴圈，定義 LLM 可評估的代理可解釋性指標**
本研究提出 Agentic-imodels，這是一個代理式自動研究迴圈，能演化專為 AI 代理設計的可解釋數據科學工具。具體而言，團隊開發了一套相容 scikit-learn 的表格數據回歸器庫，同時優化兩項指標：一是傳統預測效能，二是全新的 LLM 代理可解釋性指標。該指標透過一系列 LLM 評分的測試，檢驗擬合後模型的字串表示是否具備「可模擬性」：即 LLM 能否僅透過讀取模型的字串輸出，就正確回答關於模型行為的問題。

 **演化模型雙升預測效能與代理可解釋性，下游任務效能最高漲 73%**
實驗結果顯示，演化後的模型同時提升了預測效能與代理端可解釋性，且能泛化到全新數據集與新的可解釋性測試。更關鍵的是，這些演化模型能優化下游端到端 ADS 系統表現：在 BLADE 基準測試中，Copilot CLI、Claude Code、Codex 的效能最高提升 73%。

 **從「人類可解釋」到「代理可模擬」，解鎖 ADS 效能瓶頸**
傳統可解釋性工具以人類認知為核心，但 AI 代理的理解邏輯與人類不同，人類可讀的模型輸出對代理來說可能資訊不足。本研究提出的「可模擬性」指標，直接對齊代理（LLM）的理解能力，搭配自動研究迴圈持續演化工具，才突破了過去 ADS 系統的效能
