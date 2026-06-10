---
title: "Rethinking Exploration in RLVR: From Entropy Regularization to Refinement via Bidirectional Entropy Modulation"
source: arXiv
url: http://arxiv.org/abs/2604.04894v1
score: 106
model: gpt-4o-free
generated_at: 2026-04-07T13:45:07.929178
---

📌 RLVR 探索瓶頸破局：非對稱熵調控機制

在 RLVR 訓練中加入熵正則化本來是為了防止模型過早收斂，但實證顯示，盲目提高探索率反而可能破壞 LLM 的邏輯推理鏈。為什麼增加隨機性，有時會讓解題能力不升反降？

🤔 **盲目追求探索多樣性，反而會破壞推理解題模式**

Reinforcement Learning with Verifiable Rewards (RLVR) 已成為提升大型語言模型數學與程式推理能力的核心訓練框架。然而實務上常遭遇「探索受限」(restricted exploration)：策略函數極快收斂到少數幾組解法，迅速喪失尋找更優路徑的潛力。

業界慣用熵正則化 (Entropy Regularization) 來強迫模型保持輸出多樣性，但這招在大語言模型上往往水土不服。超參數極度敏感，且帶來的效能提升非常有限。核心矛盾在於：傳統方法將所有「不確定性」視為等價的探索資源，卻忽略了推理任務中，隨機性其實是一把雙面刃。

🧪 **將策略熵拆解為「資訊」與「雜訊」，設計 AsymGRPO**

研究團隊重新審視策略熵與探索的關係，透過推導組相對優勢估計 (group-relative advantage estimation) 的參數化形式與分析熵動態，提出關鍵概念分解：策略熵並非單一維度，而應被拆解為「資訊熵」(informative entropy) 與「雜訊熵」(spurious entropy)。前者負責保留多樣且有效的解題路徑，後者則會直接侵蝕模型既有的推理模式。

基於此洞察，團隊提出 AsymGRPO 框架。其核心設計在於「非對稱調控」：明確解耦正負樣本 (positive/negative rollouts) 的熵控制機制，讓訓練管線能獨立決定何時該保留探索空間、何時該壓制無效隨機性。

📊 **非對稱調控正負 Rollout，性能顯著超越強基線**

實驗結果顯示，AsymGRPO 在多個推理基準測試上，穩定超越現有的強基線方法。該框架不僅有效緩解了探索崩潰問題，大幅降低對熵正則化超參數的依賴度，更展現出與現有熵正則化技術協同運作的潛力。這證明將「熵精煉」(entropy refinement) 從隱式機制轉為顯式控制，能帶來更穩健的訓練動態與更高效的探索利用率。

💡 **探索不是「越多越好」，而是「該留的留、該壓的壓」**

為什麼傳統熵最大化會失效？LLM 的解題過程高度依賴結構化的邏輯鏈。當我們無差別地獎勵高熵行為時，模型很容易學到「亂湊答案」的捷徑，這就是雜訊熵泛濫的代價。AsymGRPO 的理論價值在於，它還原了 group-relative advantage 在背後其實已隱含熵精煉的邏輯：在正樣本（答對/高分）上維持資訊熵以鼓勵多元解法；在負樣本（答錯/低分）上主動壓制雜訊熵，避免錯誤模式被強化。這種雙向調控機制，精準對應了推理模型訓練中「保多樣性」與「防退化」的權衡需求。

⚠️ **依賴組相對估計架構，長期訓練動態與泛化性待驗證**

本研究框架建立在 group-relative advantage estimation 之上，其理論推導與 AsymGRPO 的設計高度依賴此類採樣與評分機制。若換用其他優勢估計方法，非對稱調控的移植成本仍需評估。此外，論文中未詳細說明在極大參數量模型上的擴展性、長期訓練是否會產生新的收斂偏差，以及該方法在非可驗證獎勵（如開放式對話或創意生成）任務中的泛化表現。

🎯 **RLHF/GRPO 管線優化方向：從「加噪」轉向「濾熵」**

對於正在實作 GRPO 或 PPO 進行推理微調的工程團隊，建議調整思維：與其微調單一的全域熵係數，不如嘗試區分正負 rollouts 的更新策略。在實作層面，可監控生成分佈的熵值分佈而非僅看平均值，並考慮在負樣本的反向傳播中引入更強的熵懲罰或梯度截斷。AsymGRPO 的架構也顯示，現有的探索正則化並非過時，而是需要與非對稱優勢估計結合，才能發揮協同效應。

🔗 **論文連結**
📝 Rethinking Exploration in RLVR: From Entropy Regularization to Refinement via Bidirectional Entropy Modulation
👤 Hengrui Gu, Xiaotian Han, Yujing Bian, Kaixiong Zhou
🔗 arXiv：http://arxiv.org/abs/2604.04894v1

你在實作 GRPO/PPO 時，如何平衡探索 (Exploration) 與收斂穩定性？歡迎分享你的調參經驗 👇

#AI #LLM #RLVR #GRPO #強化學習 #推理模型 #機器學習研究 #AsymGRPO
