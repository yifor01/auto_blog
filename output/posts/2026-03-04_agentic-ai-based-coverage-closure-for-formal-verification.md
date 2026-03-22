---
title: "Agentic AI-based Coverage Closure for Formal Verification"
source: ChatPaper/AI
url: https://arxiv.org/abs/2603.03147
score: 128
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-04T18:56:59.647641
---

📌 【Infineon 最新研究】Agentic AI 讓晶片驗證效率提升 3.2 倍，加速驗證關鍵時刻

IC 設計驗證一直是晶片開發的瓶頸，尤其在正式驗證 (Formal Verification) 階段，如何達成「完整覆蓋」往往決定專案能否如期上線。傳統的窮盡測試法雖然準確，但時間成本高昂，容易在專案時間壓力下無法完成。

🤔 **驗證覆蓋率是關鍵，但傳統方法太慢**

Coverage closure（覆蓋率關閉）是晶片驗證的關鍵指標，代表驗證是否完整。然而，手動分析覆蓋率缺口、設計 formal properties 等工作，需要大量工程師時間，且容易遺漏邊界情況。當專案進入關鍵階段，這往往成為進度瓶頸。

🧪 **Agentic AI 如何自動化驗證流程**

Infineon 與印度理工學院的研究團隊，開發了一套基於 Agentic AI 的工作流程。核心特色包括：

- 使用 LLM 自動分析現有覆蓋率報告，識別缺口
- 生成對應的 formal properties 來填補缺口
- 系統性地迭代驗證，直到達成目標覆蓋率
- 能處理 open-source 與內部設計，適應不同複雜度

 **實驗結果：覆蓋率提升 3.2 倍，驗證效率大增**

研究團隊以多個設計進行測試，結果顯示：

- 平均覆蓋率從 28.4% 提升至 91.2%
- 驗證效率提升 3.2 倍
- 改善程度與設計複雜度正相關

⚡ **為何 Agentic AI 在此應用特別有效**

Agentic AI 不只是單次的 AI 輔助，而是具有目標導向、能自我修正的智能代理。在驗證場景中，這意味著：

- 能理解驗證目標，而非僅回應指令
- 能根據反饋調整策略，持續優化
- 能處理驗證工作的複雜性與不確定性

🎯 **對晶片產業的實務啟示**

這項技術對 IC 設計驗證的影響包括：

- 縮短驗證時程，有助於專案如期交付
- 減少人為疏失，提升驗證完整性
- 讓工程師從繁瑣的覆蓋率分析中解放，專注於關鍵設計決策

⚠️ **研究限制與未來方向**

目前研究仍有以下限制：

- 主要針對 formal verification，對模擬驗證的適用性待評估
- 生成 formal properties 的品質仍需人工審查
- 在極高複雜度的設計上，效果仍有提升空間

🔗 **論文連結**
📝 Agentic AI-based Coverage Closure for Formal Verification
👤 Sivaram Pothireddypalli, Ashish Raman, Deepak Narayan Gadde, Aman Kumar
🏢 Infineon Technologies & Dr. B R Ambedkar National Institute of Technology Jalandhar
🔗 論文：arxiv.org/abs/2603.03147

你認為 Agentic AI 未來還能在晶片設計的哪些環節發揮作用？歡迎討論 👇

#AI #FormalVerification #ICDesign #ChipDesign #AgenticAI #Infineon #MachineLearning #晶片驗證
