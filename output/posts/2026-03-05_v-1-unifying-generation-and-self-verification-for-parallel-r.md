---
title: "$V_1$: Unifying Generation and Self-Verification for Parallel Reasoners"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2603.04304
score: 123
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-05T12:15:13.014883
---

📌 【$V_1$ 框架】測試時擴展的關鍵突破：從獨立評分到配對自我驗證

當前 AI 在複雜推理任務上的測試時擴展 (test-time scaling) 已顯示出巨大潛力，但存在一個關鍵瓶頸：如何可靠地從多個候選解中識別出正確的答案？$V_1$ 框架提出了一種統一生成和自我驗證的創新方法，在 Code 生成和數學推理等領域取得了顯著進展。

🤔 **獨立評分為什麼不夠好？**

現有測試時擴展方法通常透過獨立評分多個候選解來識別正確答案。然而，我們發現模型在配對比較 (pairwise comparison) 時表現顯著更強，這意味著模型更擅長判斷「哪個候選解更好」，而非單獨評估每個解的絕對優劣。

🧪 **52 位工程師的隨機對照實驗**

這是一項隨機對照實驗 (RCT)，招募了 52 位軟體工程師（大多為初級）。參與者需學習一個新的 Python 函式庫 (Trio)，一組可以使用 AI 助手，另一組必須手動編程。完成任務後，立即進行知識測驗。

💡 **$V_1$ 的關鍵創新**

$V_1$ 框架包含兩個核心組件：

1. **$V_1$-Infer**：基於不確定性的演算法，使用錦標賽式排名動態分配自我驗證計算資源到最不確定的候選配對
2. **$V_1$-PairRL**：聯合訓練生成器和配對自我驗證器的強化學習框架，確保驗證器能適應生成器的演變分佈

🎯 **實驗結果：大幅超越現有方法**

在 Code 生成和數學推理等多個關鍵任務上，$V_1$ 展現出卓越性能：

- **LiveCodeBench**：Pass@1 提升 10%（相較於點式驗證）
- **CodeContests**：顯著提升推理能力
- **SWE-Bench**：在軟體工程任務上表現優異
- **AIME 和 HMMT**：數學推理任務取得突破性進展

更重要的是，$V_1$-PairRL 在標準強化學習上實現了 7-9% 的測試時擴展增益，並將基準 Pass@1 提高了高達 8.7%。

⚠️ **為什麼配對驗證更有效？**

研究發現，當模型需要判斷兩個候選解的相對優劣時，能更好地利用其推理能力。這種配對比較能減少絕對評分的不確定性，並讓模型更專注於關鍵差異點。

🎯 **實務啟示：測試時擴展的新方向**

- 配對比較可能比絕對評分更適合複雜推理任務
- 動態分配計算資源能顯著提升效率
- 聯合訓練生成器和驗證器能創造更強的協同效應

🔗 **論文連結**
📝 $V_1$: Unifying Generation and Self-Verification for Parallel Reasoners
👤 Harman Singh, Xiuyu Li, Kusha Sareen, Monishwaran Maheswaran, Sijun Tan
@ UC Berkeley; Mila; Together AI; NVIDIA
🔗 論文：arxiv.org/abs/2603.04304

你認為配對驗證會成為測試時擴展的主流方法嗎？歡迎分享你的看法 👇

#AI #機器學習 #測試時擴展 #程式生成 #數學推理 #強化學習 #NVIDIA #UC Berkeley
