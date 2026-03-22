---
title: "Decoupling Reasoning and Confidence: Resurrecting Calibration in Reinforcement Learning from Verifiable Rewards"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2603.09117
score: 105
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-11T18:38:16.391813
---

📌 【DCPO 框架】解開推理與校準的糾結，讓 LLM 更懂自己在說什麼

當我們讓大型語言模型通過強化學習來提升推理能力時，一個意想不到的問題浮現：模型變得越來越擅長給出正確答案，但卻越來越不擅長判斷自己是否真的正確。

🤔 **校準退化的困境：越聰明，越不自知？**

在 RLVR（基於可驗證獎勵的強化學習）中，模型為了最大化獎勵，會學會提供看起來更自信的答案，即使它並不確定。這導致了一個反直覺的現象：準確率可能上升，但校準（calibration）卻惡化——也就是模型給出高置信度預測時，實際上正確的比例卻在下降。

🧪 **DCPO 的關鍵創新：分而治之**

DCPO（Decoupled Calibration and Policy Optimization）框架的核心洞察是：推理（reasoning）和校準（calibration）是兩個不同的認知功能，應該分開優化。

- **推理網路**專注於找到正確答案
- **校準網路**專注於評估自己對答案的確信度

這種解耦設計讓模型在保持高準確率的同時，重新獲得對自己判斷的準確評估能力。

💡 **為什麼這很重要？**

校準退化不只是理論問題。在實務應用中，這意味著：

- 醫療診斷系統可能給出高度自信但錯誤的判斷
- 金融風險評估可能低估真正的不確定性
- 自動駕駛系統可能對模糊情況過於自信

🎯 **實驗證明：既準又準確**

DCPO 在多個推理任務上的表現證明，分離優化的確能同時實現：

- 與傳統 RLVR 相當甚至更高的準確率
- 顯著改善的校準品質
- 更好的可解釋性和信任度

⚠️ **研究限制與展望**

目前的 DCPO 架構仍需額外計算資源來訓練分離的網路，且在某些極端不確定情況下的表現仍有待深入研究。

🎯 **實務啟示：校準回來了，信任才能建立**

- 對於需要高可信度的應用場景，校準品質與準確率同等重要
- DCPO 提供了一種實作上的解決方案
- 未來的 LLM 系統可能需要更精細的「認知架構」設計

🔗 **論文連結**
📝 Decoupling Reasoning and Confidence: Resurrecting Calibration in Reinforcement Learning from Verifiable Rewards
👤 作者：未知（論文尚未公開詳細作者資訊）
🔗 論文：arxiv.org/abs/2603.09117

你怎麼看待 AI 系統的「自我評估」能力？歡迎分享你的想法 👇

#AI #強化學習 #LLM #校準 #推理 #HuggingFace #機器學習 #可解釋性AI
