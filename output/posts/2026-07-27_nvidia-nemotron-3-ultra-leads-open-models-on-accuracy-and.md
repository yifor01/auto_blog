---
title: NVIDIA Nemotron 3 Ultra Leads Open Models on Accuracy and Efficiency in Agentic
  RTL Coding
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-leads-open-models-on-accuracy-and-efficiency-in-agentic-rtl-coding/
model: tencent/hy3:free
generated_at: '2026-07-27T09:06:43.650871'
score: 113
---

📌 【NVIDIA 研究】Nemotron 3 Ultra 結合 ACE-RTL 代理，大幅提升 RTL 設計的準確度與效率

TL;DR：NVIDIA Nemotron 3 Ultra 搭配 ACE-RTL 代理，在 RTL 任務中達成 97.1% 的通過率，且 Token 消耗降低達 71%。

隨著晶片設計複雜度提升，暫時轉換層（RTL）的開發與驗證已成為工程時間的主要瓶頸。RTL 開發不僅需要專業的硬體知識，更需要精準的推理能力，並需不斷與電子設計自動化（EDA）工具進行反覆互動，因為許多錯誤只有在工具驗證後才會顯現。

🧩 **ACE-RTL 代理與 Nemotron 3 Ultra 的協作模式**

為了應對 RTL 設計對正確性的極高要求，NVIDIA 提出了 ACE-RTL 代理，並結合 Nemotron 3 Ultra 模型，透過以下機制實現高效開發：

- 迭代式工作流：採用「生成 $\rightarrow$ 測試 $\rightarrow$ 反思」（generate-test-reflect）的迭代流程。
- 代理式行為：利用驗證回饋來修正錯誤，這對於依賴精準時序行為（temporal behavior）的 RTL 設計至關重要。
- 專業推理：利用 Nemotron 3 Ultra 的長文本（long-context）與 RTL 專用推理能力。

📊 **在 CVDP 基準測試中取得領先表現**

在綜合 Verilog 設計問題（CVDP）基準測試中，ACE-RTL 搭配 Nemotron 3 Ultra 的表現優於 GLM 5.2 與 Kimi K2.6 等模型：

- 準確度：在九種代理式 RTL 任務類別中，平均通過率達到 97.1%。
- 效率提升：每次迭代使用的 Token 數量減少了高達 71%。

💡 **混合架構與高品質合成數據**

Nemotron 3 Ultra 展現了極高的推論吞吐量與低成本特性，這歸功於其技術設計：

- 混合架構：採用 Mamba-Attention Mixture-of-Experts（混合專家模型）架構。
- 訓練數據：使用經過評分過濾（rubric-filtered）的多元合成 RTL 資料集進行訓練。
- 長文本能力：支援長文本推理，使其成為整合主流 EDA 工具（如 Cadence、Siemens 與 Synopsys）的實務基礎。

🎯 **實務啟示**

對於硬體工程師與 EDA 軟體開發者而言，這代表 AI 代理不再只是單純的程式碼生成器，而是能透過「反思」與「驗證回饋」進行自我修正的開發夥伴，且其高效率的推論特性讓大規模的自動化設計流程變得更具經濟可行性。

🔗 **來源**
- 標題：NVIDIA Nemotron 3 Ultra Leads Open Models on Accuracy and Efficiency in Agentic RTL Coding
- 作者／機構：Nirmal Kumar Juluru, Chenhui Deng, Cunxi Yu, Nathaniel Pinckney and Brucek Khailany @ NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-leads-open-models-on-accuracy-and-efficiency-in-agentic-rtl-coding/

#NVIDIA #Nemotron3Ultra #RTL #EDA #GenerativeAI #AIAgent #Verilog #ChipDesign #MachineLearning #HardwareEngineering
