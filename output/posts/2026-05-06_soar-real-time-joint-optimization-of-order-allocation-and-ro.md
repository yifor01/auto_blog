---
title: "SOAR: Real-Time Joint Optimization of Order Allocation and Robot Scheduling in Robotic Mobile Fulfillment Systems"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.03842
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-05-06T20:23:36.906417
---

📌 【北航×极智嘉】SOAR 实时联合优化仓储调度

現有倉儲機器人調度長期面臨兩難：要實時響應動態訂單，就得分拆任務犧牲全局效率；要追求全局最優，又得扛住高昂計算成本，跟不上工業環境變化。

🤔 **RMFS 调度面临实时性与全局最优的两难**
移動機器人倉儲系統（RMFS）透過移動機器人完成自動化庫存運輸，需協調訂單分配與機器人調度提升倉儲效率。但該場景存在嚴格實時約束，且多階段決策強耦合，優化難度極高。
現有方法分為兩類：一類將問題拆為孤立子任務，保證響應速度但犧牲全局最優性；另一類依賴計算昂貴的全局優化模型，無法適應動態工業環境。本論文提出的SOAR框架，正是為了填補這兩類方法之間的缺口。

🧪 **事件驱动MDP + 异构图Transformer的统一DRL框架**
論文提出SOAR，一套統一的深度強化學習（DRL）框架，實現訂單分配與機器人調度的實時聯合優化。核心設計包含以下幾點：
1. 將軟訂單分配作為觀測，把兩個任務轉化為統一流程，形式化為**事件驅動馬爾可夫決策過程（Event-Driven MDP）**，讓智能體可針對非同步系統事件執行同時調度。
2. 採用**異構圖Transformer（Heterogeneous Graph Transformer）**編碼倉庫狀態，並整合分階段領域知識。
3. 加入**獎勵塑形策略**，解決長視距任務中反饋稀疏的問題。

💡 **总完工时间减7.5%，延迟低于100ms**
研究與極智嘉（Geekplus）合作，在合成數據集與真實工業數據集上完成大量實驗，核心結果如下：
- 全局總完工時間（makespan）降低7.5%
- 平均訂單完成時間降低15.4%
- 調度延遲低於100ms，滿足實時性要求
- 完成sim-to-real（模擬到真實）部署驗證，確認框架在生產環境中的實用性與性能提升效果

🔍 **联合优化破解多阶段决策耦合难题**
現有方法的根本缺陷在於未處理好訂單分配與機器人調度的強耦合關係：拆任務會忽略兩者的關聯，全局優化則無法應對動態事件。SOAR的核心創新在於將兩者統一為單一優化流程，透過事件驅動MDP響應非同步系統事件，配合異構圖Transformer捕捉倉庫多主體的複雜狀態，同時融入領域知識降低學習難度，最終實現實時性與全局最優的平衡。

⚠️ **现有公开资讯未提及明确研究限制**
本次提供的論文摘要未明確列出研究限制，讀者可查閱完整論文獲取更多細節。根據現有資訊，框架已在極智嘉的真實工業場景完成驗證，具備工業落地基礎。

🎯 **智慧仓储与多智能体调度开发者可直接参考开源实现**
該框架針對工業場景設計，已在真實生產環境完成驗證，且程式碼完全開源，對智慧倉儲、多智能體排程領域的工程師與研究者具高度參考價值。開發者可基於開源程式碼快速復現實驗，或針對自身場景做適配優化。

🔗 **論文連結**
📝 標題：SOAR: Real-Time Joint Optimization of Order Allocation and Robot Scheduling in Robotic Mobile Fulfillment Systems
👤 作者：Yibang Tang, Yifan Yang, Jingyuan Wang, Junhua Chen, Zhen Zhao
🏫 機構：Beihang University; Geekplus Technology Co., Ltd.
🔗 論文：https://arxiv.org/abs/2605.03842
💻 開源程式碼：https://github.com/200815147/SOAR

#AI #深度强化学习 #智慧仓储 #机器人调度 #北航 #极智嘉 #多智能体 #物流自动化 #工业AI
