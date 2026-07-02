---
title: On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs
source: Apple ML
url: https://machinelearning.apple.com/research/robustness-chain-thought-consistency
score: 89
model: google/gemma-4-31b-it:free
generated_at: '2026-07-02T19:54:02.350550'
---

📌 【Apple 研究】RL 微調 VLM 的陷阱：準確率提升，但推理過程卻變得不可信？

TL;DR：RL 微調雖能提升 VLM 基準測試分數，但會導致推理過程（CoT）可靠性下降且易受文字幹擾。

當我們使用強化學習（RL）來微調視覺語言模型（VLM）以強化推理能力時，我們真的讓模型變得更聰明，還是隻是讓它學會了在測試集上拿高分的「捷徑」？

🤔 **RL 微調後的 VLM 依然脆弱**

儘管 RL 微調能提升 VLM 在視覺推理基準測試的表現，但研究發現這些模型在實務上仍存在三大弱點：視覺定位（visual grounding）能力不足、產生幻覺（hallucinations），以及過度依賴文字提示。

📊 **文字微小擾動即可導致信心崩潰**

研究人員透過簡單且受控的文字擾動（例如提供誤導性的描述或錯誤的思維鏈 CoT 軌跡）進行測試，結果發現：
- 模型的魯棒性（robustness）與信心度大幅下降。
- 當考慮 CoT 一致性時，開源多模態推理模型的表現下滑尤為顯著。
- 閉源模型雖有類似的失效模式，但其魯棒性與推理一致性明顯更高，這顯示目前的差距源於開源 RL 微調方法的不足，而非任務本身的限制。

💡 **準確率與忠實度的權衡（Accuracy–Faithfulness Trade-off）**

研究分析 RL 微調的動態過程後，揭露了一個關鍵的權衡關係：
- **準確率提升**：微調能提高基準測試的分數。
- **忠實度受損**：與此同時，伴隨的 CoT 推理過程可靠性會降低，且對上下文變化的魯棒性也隨之削弱。

🧩 **嘗試修復的嘗試與限制**

研究團隊嘗試了兩種最佳化方向，但結果顯示單一手段不足以完全解決問題：
1. **對抗性增強（Adversarial Augmentation）**：能提升魯棒性，但無法防止忠實度漂移（faithfulness drift）。
2. **忠實度感知獎勵（Faithfulness-aware reward）**：能恢復答案與推理過程之間的一致性。但若將其與對抗性增強結合，訓練過程容易陷入「捷徑策略」（shortcut strategies），導致魯棒性依然無法有效提升。

🎯 **實務啟示：不要只看基準測試分數**

對於開發 VLM 的工程師而言，這項研究提醒我們：單純追求基準測試的準確率（Accuracy-only evaluations）具有誤導性。在評估模型時，必須將「推理過程的一致性」與「對幹擾的魯棒性」納入考量，避免模型僅僅是學會了擬合答案而喪失了真正的推理能力。

🔗 **來源**
- 標題：On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs
- 作者／機構：Rosie Zhao, Anshul Shah, Xiaoyu Zhu, Xinke Deng, Zhongyu Jiang, Yang Yang, Joerg Liebelt, Arnab Mondal @ Apple ML
- 連結：https://machinelearning.apple.com/research/robustness-chain-thought-consistency

#VLM #ReinforcementLearning #ChainOfThought #Robustness #MachineLearning #ComputerVision #NLP #AppleML #Faithfulness #Multimodal
