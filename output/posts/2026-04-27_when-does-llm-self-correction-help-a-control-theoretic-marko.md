---
title: "When Does LLM Self-Correction Help? A Control-Theoretic Markov Diagnostic and Verify-First Intervention"
source: ChatPaper/AI
url: https://arxiv.org/abs/2604.22273
score: 126
model: tencent/hy3-preview:free
generated_at: 2026-04-27T19:39:58.876720
---

📌 【北大&芝大研究】LLM自我修正何时有效？

你以為讓LLM反覆迭代修正答案就能提升準確率？實測7款主流模型後發現：多數模型自我修正後性能反而下降，僅3款模型不受影響。

🤔 **迭代自我修正廣泛用於Agent系統，但效果邊界長期不明確**
目前LLM的迭代自我修正（iterative self-correction）是Agentic系統的核心機制之一，但重複優化究竟會提升還是損害最終表現，始終缺乏可量化的判斷標準。現有實踐多依賴經驗性嘗試，未建立系統性的診斷框架。

🧪 **基於控制論反饋迴路與兩狀態馬可夫模型，實測7模型3數據集**
研究團隊將自我修正框架為控制論（cybernetic）的反饋迴路：同一個LLM同時承擔控制器（controller）與受控對象（plant）的角色，並採用{Correct, Incorrect}的兩狀態馬可夫模型定義可操作的部署診斷規則：僅當ECR/EIR > Acc/(1-Acc)時，才適合進行迭代修正。其中EIR被定義為系統的穩定裕度指標，提示設計則視為輕量級的控制器設計。實驗覆蓋7款主流模型、3個公開數據集（GSM8K、MATH、StrategyQA），並通過verify-first提示消融實驗驗證閾值的可操作性。

📊 **≤0.5%的EIR閾值是自我修正有效與否的分界線**
實驗發現EIR存在
