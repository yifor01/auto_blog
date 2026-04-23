---
title: "Learning to Evolve: A Self-Improving Framework for Multi-Agent Systems via Textual Parameter Graph Optimization"
source: ChatPaper/AI
url: https://arxiv.org/abs/2604.20714
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-04-23T19:49:06.921192
---

📌 【阿里巴巴 Future Living Lab】讓多代理系統學會「自我演化」的新框架

設計多代理系統（MAS）就像在調校一支足球隊，你得決定誰該傳球、誰該射門，還有該用什麼戰術。但現在的問題是，當系統出錯時，大多數的優化工具就像只會調整單一球員跑速的教練，缺乏全局觀，而且教練本身也不會從失敗中學習。

🤔 **Agent Engineering 的痛點：靜態優化與結構黑箱**

目前的多代理系統優化大多依賴「扁平提示調優」（Flat Prompt Tuning）。這種方法將整個系統視為一個黑箱，缺乏對代理間互動結構的感知。更關鍵的是，這些優化器是「靜態」的，它們不會隨著經驗累積而進化，每次遇到新問題都得從零開始。

🧪 **將 MAS 建模為「文本參數圖」(TPG)**

阿里巴巴 Future Living Lab 提出的 TPGO (Textual Parameter Graph Optimization) 框架，核心在於將多代理系統重新定義為一個 **文本參數圖 (Textual Parameter Graph, TPG)**。在這個圖中，代理、工具與工作流程都是可優化的模組化節點。這種結構化的視角，讓系統能精準定位問題發生在哪個節點。

 **從「文本梯度」到「會學習的優化器」**

TPGO 的創新不只在於結構，更在於其反饋機制：
1.  **文本梯度 (Textual Gradients)**：不同於傳統數值梯度，TPGO 利用結構化的自然語言反饋，從執行軌跡中診斷失敗原因並提出修改建議。
2.  **GRAO 元學習策略**：這才是真正的殺手鐧。Group Relative Agent Optimization (GRAO) 讓優化器本身具備了「元學習」能力。它會分析過去優化歷史中的成功與失敗，學習如何更有效地提出更新策略。這意味著，系統不僅在執行任務，還在學習「如何優化自己」。

💡 **自我進化的閉環：優化經驗即資產**

這項研究的關鍵洞察在於，優化過程中的歷史數據不應被丟棄，而應成為系統進化的養分。GRAO 讓 TPGO 隨著時間推移，越來越擅長解決複雜的代理協作問題，實現了從「被動調參」到「主動演化」的跨越。

⚠️ **實作細節與開源資源尚待普及**

雖然概念極具前瞻性，但目前論文中對於具體的實作細節描述仍偏向高層次架構。對於想立即動手嘗試的工程師來說，目前可能缺乏現成的開源程式碼與詳細的部署指南，這是後續落地需要關注的部分。

🎯 **重新定義 Agent Engineering 的未來**

TPGO 展示了多代理系統自動化優化的新路徑。對於開發者而言，這意味著未來我們可能不再需要手動微調每個代理的 Prompt，而是構建一個能自我迭代、自我完善的系統架構。這將大幅降低複雜 AI 工作流的維護成本。

🔗 **論文連結**
📝 Learning to Evolve: A Self-Improving Framework for Multi-Agent Systems via Textual Parameter Graph Optimization
👤 Shan He, Runze Wang, Zhuoyun Du, Huiyu Bai, Zouying Cao @ Future Living Lab of Alibaba
🔗 論文：https://arxiv.org/abs/2604.20714

你認為讓 AI 系統自我優化，最讓你擔心或期待的是什麼？歡迎在留言區討論 👇

#MultiAgentSystem #MAS #Alibaba #LLM #AgentEngineering #自我演化 #AI研究 #未來科技
