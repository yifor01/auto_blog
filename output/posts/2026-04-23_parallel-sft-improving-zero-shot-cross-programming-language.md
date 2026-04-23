---
title: "Parallel-SFT: Improving Zero-Shot Cross-Programming-Language Transfer for Code RL"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2604.20835
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-04-23T19:51:04.795153
---

📌 【Meta & MIT 研究】Parallel-SFT 优化代码跨语言迁移

你以為代碼強化學習（RL）訓練能跨語言泛化？Llama-3.1的實驗結果恰恰相反。
在源編程語言做RL訓練後，模型在目標語言的表現不升反降。
Meta與MIT團隊提出的Parallel-SFT，終於補上了跨語言遷移的短板。

🤔 **跨語言編程技能本應通用，RL訓練卻反而阻礙遷移**
目前大型語言模型在C++、Python等常見編程語言上已展現出色的代碼生成能力，但在低資源編程語言上的表現往往受限于訓練數據不足。理論上，大部分編程技能是跨語言通用的，因此在單一語言上習得的能力理應能遷移到其他語言。

但針對Llama-3.1的測試顯示，在源編程語言上執行代碼生成強化學習（RL，Reinforcement Learning）訓練後，模型在目標編程語言上的表現不僅沒有提升，甚至還可能低於訓練前的水平，這與「技能通用」的預期完全矛盾。

🧪 **SFT階段加入跨語言等效代碼，優化初始化**
研究團隊提出假設，有效的RL跨語言遷移，需要在RL訓練前先完成可泛化的監督微調（SFT，Supervised Fine-Tuning）初始化。基於此提出**並行監督微調（Parallel-SFT）**策略，核心是在SFT階段的數據混合中，加入「並行程序」，也就是功能完全等效、但採用不同編程語言實現的代碼組。

團隊後續在Parallel-SFT初始化後的模型上執行代碼RL訓練，測試其對未見過的目標編程語言的零樣本（無需目標語言額外訓練數據）泛化能力，同時分析模型內部表征的差異。

🔍 **Parallel-SFT 顯著提升RL跨語言泛化能力**
實驗結果驗證了Parallel-SFT的有效性：
1. 普通SFT初始化後執行RL訓練：Llama-3.1在源語言的能力提升，但目標語言表現不升反降；
2. Parallel-SFT初始化後執行RL訓練：模型對未見過的目標編程語言的零樣本泛化能力明顯提升；
3. 內部表征分析顯示，Parallel-SFT讓模型的潛在空間更偏向「功能中心」，不同語言中功能相同的程序在向量空間中聚類更緊密，研究團隊推測這是遷移性提升的核心原因。

💡 **跨語言遷移的核心是功能而非語法**
Parallel-SFT讓模型將功能作為表征的核心維度，而非單一語言的語法特徵，因此跨語言等效程序的特征更接近，RL訓練學到的能力不會被源語言語法限制，可遷移到目標語言。這種全新的SFT範式也為多語言代碼模型的優化提供了新方向。

⚠️ **僅驗證Llama-3.1，即時工具支持有限**
目前研究僅基於Llama-3.1模型完成驗證，其他架構模型的適用性尚未測試；同時該方法的即時工具支持有限，尚未有現成的開源工具或產品級實現可供直接使用。

🎯 **多語言代碼模型SFT階段可加入並行程序**
對於從事多語言代碼模型研發的工程師與研究者，可在SFT階段引入跨語言功能等效的並行程序，無需依賴大量低資源語言的訓練數據，即可讓模型學到通用的編程功能表征，後續RL訓練的跨語言遷移效果也會更好。目前雖然工具支持有限，但方法論邏輯清晰，具備較高的復現價值。

🔗 **論文連結**
📝 論文標題：Parallel-SFT: Improving Zero-Shot Cross-Programming-Language Transfer for Code RL
👤 作者：Zhaofeng Wu, Shiqi Wang, Boya Peng, Anuj Goyal, Melanie Kambadur（Meta Superintelligence Labs；麻省理工學院 MIT）
🔗 論文連結：https://arxiv.org/abs/2604.20835

#AI #機器學習 #代碼生成 #多語言模型 #Meta #MIT #SFT #強化學習 #編程語言遷移 #ParallelSFT
