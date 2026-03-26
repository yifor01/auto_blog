---
title: "Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2603.24472
score: 113
model: gpt-4o-free
generated_at: 2026-03-26T19:38:35.061562
---

📌 【Microsoft Research 最新研究】為什麼 Self-Distillation 會讓 LLM 的推理能力退化？

Self-distillation 一直被視為提升大型語言模型 (LLMs) 表現的有效方法，但最新研究顯示，這個方法可能在數學推理場景中適得其反。不僅答案長度縮短，性能甚至大幅滑落——這背後的原因，與模型「表達不確定性」的能力被壓抑有關。

🤔 **自蒸餾有時有用，但對「不確定性」的抑制是個問題**

Self-distillation，簡單來說就是讓模型在訓練後學習「自己生成的答案」，以優化推理路徑並提升準確性。然而，Microsoft Research 與 KAIST、首爾大學的研究團隊發現，這種方法會抑制模型表達「不確定性」的能力，尤其是在數學推理中表現得尤為明顯。

這種抑制對於模型處理未知問題（Out-Of-Distribution, OOD）時非常不利，因為無法表達不確定性就無法靈活調整推理過程，導致性能顯著下降。

🧪 **多模型實驗揭示性能下降高達 40%**

研究團隊使用了三種 LLM 模型進行對比測試：Qwen3-8B、DeepSeek-Distill-Qwen-7B 和 Olmo3-7B-Instruct。在數學推理相關任務中，應用 self-distillation 的模型性能下降高達 40%。

更重要的是，這種下降與模型的「推理上下文豐富程度」和「任務覆蓋範圍」相關。當教師模型（Teacher Model）被設定為依賴豐富的上下文信息時，模型會更傾向壓抑不確定性表達，導致在未見過的問題中表現尤其不佳。

💡 **不確定性：推理中的「潤滑劑」**

研究揭示了一個關鍵洞察：對於 LLM 來說，「不確定性」不僅是推理過程中的自然現象，更是一種重要的能力。適當表達不確定性讓模型可以在推理過程中靈活地調整，特別是在面對 OOD 任務時。

這項研究提醒我們，優化推理行為不應僅僅著眼於生成正確答案的能力，而是要關注模型如何處理未知情境的表現。換句話說，提升模型的「適應性」和「健壯性」比單純縮短推理路徑來得更重要。

⚠️ **研究限制：僅針對數學推理，其他領域尚需驗證**

值得注意的是，這項研究的發現主要針對數學推理場景，其他應用領域（如自然語言理解或生成）是否存在類似效應，尚需進一步研究。此外，實驗的性能下降與具體模型的架構細節也可能有關，這些都需要在未來的工作中進一步探討。

🎯 **實務建議：在數學推理場景中謹慎使用 Self-Distillation**

- 如果目標是優化數學推理性能，應謹慎評估 self-distillation 的應用。
- 強化模型對不確定性的表達能力，可能是提升 OOD 表現的重要方向。
- 開發者應根據任務需求，調整 post-training 優化的策略，避免過度壓抑模型的靈活性。

🔗 **論文連結**
📝 Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?
👤 Jeonghye Kim, Xufang Luo, Minbeom Kim, Sangmook Lee, Dohyung Kim
🏢 Microsoft Research; KAIST; Seoul National University
🔗 論文： https://arxiv.org/abs/2603.24472

你認為 LLM 在推理過程中應該如何平衡效率與靈活性？歡迎留言分享你的觀點！👇

#AI #LLM #SelfDistillation #推理能力 #數學推理 #MicrosoftResearch #KAIST #SeoulNationalUniversity #機器學習
