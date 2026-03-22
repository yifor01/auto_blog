---
title: "Confidence-Calibrated Small-Large Language Model Collaboration for Cost-Efficient Reasoning"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2603.03752
score: 123
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-05T12:15:54.268008
---

# 📌 【AWS & 清華大學最新研究】用小模型省 20% 成本，推理能力還不減

大型語言模型 (LLM) 的推理能力確實強大，但每個 token 幾塊錢的 API 費用，讓企業望而卻步。有沒有可能讓小模型先試試看，真的不行的時候再找大模型幫忙？

🤔 **小模型先上，真的不行的時候才找大模型**

AWS 與清華大學團隊發現，在複雜推理任務中，小模型 (SLM) 雖然能力不如大模型 (LLM)，但如果能準確判斷「自己不會」，就能把大模型的工作量減少 20% 以上。

他們設計了 COllaborative REAsoner (COREA) 系統，核心概念很簡單：
1. 先讓小模型回答問題，並輸出一個「信心分數」
2. 信心分數低於門檻的問題，才交給大模型處理
3. 透過強化學習訓練小模型，讓它的信心分數更準確

🧪 **21.5% 成本降低，推理能力只掉 2%**

實驗在多個數學和非數學推理資料集上測試，結果顯示：
- 成本降低：21.5% (數學) / 16.8% (非數學)
- 準確度下降：小於 2 個百分點
- 適用模型：Llama、Qwen、Baichuan 等多種 backbone

💡 **關鍵在於「信心校準」**

COREA 的創新在於透過額外的信心校準獎勵 (confidence calibration reward)，用強化學習訓練小模型，讓它不僅答案準確，還能準確判斷「我該不該回答這個問題」。

⚠️ **仍有侷限**

- 信心門檻需要根據任務微調
- 對極端困難問題仍需依賴大模型
- 訓練過程需要額外的計算資源

🎯 **對開發者的實際意義**

如果你在生產環境中使用 LLM API：
- 可節省 15-20% 的推理成本
- 適用於對成本敏感的商業應用
- 提供了一種混合使用 SLM/LLM 的架構範例

🔗 **論文連結**
📝 Confidence-Calibrated Small-Large Language Model Collaboration for Cost-Efficient Reasoning
👤 Chuang Zhang, Zizhen Zhu, Yihao Wei, Bing Tian, Junyi Liu
🏢 Amazon Web Services, Tsinghua University
🔗 arxiv.org/abs/2603.03752

你有用過類似的小模型先行、大模型後援的架構嗎？歡迎分享你的經驗 👇

#AI #推理 #成本優化 #強化學習 #AWS #清華大學 #LLM #SLM
