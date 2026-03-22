---
title: "Dual-Modality Multi-Stage Adversarial Safety Training: Robustifying Multimodal Web Agents Against Cross-Modal Attacks"
source: ChatPaper/AI
url: https://arxiv.org/abs/2603.04364
score: 128
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-05T12:12:26.009770
---

📌 【UC Berkeley & Google 最新研究】AI 網頁代理的安全漏洞：圖文合攻的對抗攻擊

隨著多模態網頁代理（Multimodal Web Agents）逐漸應用於自動化網頁操作，一個關鍵的安全問題浮現：當攻擊者同時操縱視覺和文字兩個通道時，AI 代理的防禦能力為何？

🤔 **圖文合攻的對抗攻擊：AI 代理的隱藏漏洞**

傳統的 AI 安全研究多聚焦於單一模態（如文字或圖像）。但多模態網頁代理同時處理**螢幕截圖**和**無障礙樹**（accessibility trees）兩種輸入，這創造了一個獨特的攻擊面：攻擊者可以同時污染視覺和文字兩個通道，讓 AI 代理接收一致但具有欺騙性的訊息。

🧪 **MiniWob++ 實驗揭露關鍵弱點**

研究團隊在 MiniWob++ 網頁代理測試平台上進行對抗攻擊實驗，發現**包含視覺成分的攻擊遠比純文字注入更有效**。這揭示了當前以文字為中心的 VLM（Vision-Language Model）安全訓練存在關鍵缺口。

💡 **DMAST：三階段對抗訓練框架**

為了解決這個問題，研究團隊提出 **Dual-Modality Multi-Stage Adversarial Safety Training (DMAST)**，將代理與攻擊者的互動形式化為**雙人零和馬可夫博弈**（two-player zero-sum Markov game），並透過三階段共訓：

1. **模仿學習**（Imitation Learning）：從強大的教師模型學習基礎能力
2. **監督微調**（Supervised Fine-Tuning）：使用創新的「零確認策略」（zero-acknowledgment strategy），在對抗性干擾下培養任務導向的推理能力
3. **對抗性強化學習**（Adversarial Reinforcement Learning）：透過 Group Relative Policy Optimization (GRPO) 自我對弈持續進化

 **性能突破：防禦 + 效率雙提升**

DMAST 在**未見過的任務**上展現卓越表現：
- 大幅降低對抗性風險
- 同時將任務完成效率**翻倍**
- 顯著優於現有的訓練型和提示型防禦方法

這證明了 DMAST 能實現真正的**共同進化進步**（co-evolutionary progress），並具備對複雜、未見過環境的穩健泛化能力。

⚠️ **研究限制與未來方向**

雖然 DMAST 展現強大潛力，研究團隊承認仍有挑戰：
- 對抗攻擊的生成策略仍有優化空間
- 在更複雜的真實網頁環境中的表現需進一步驗證
- 計算資源需求較高

🎯 **實務啟示：多模態 AI 安全的新標準**

這項研究為多模態 AI 系統的安全設計提供了重要參考：
- 安全訓練必須考慮**多模態攻擊面**
- 對抗訓練應該**同步演化**攻擊與防禦策略
- 任務導向的推理能力是抵禦對抗攻擊的關鍵

🔗 **論文連結**
📝 Dual-Modality Multi-Stage Adversarial Safety Training: Robustifying Multimodal Web Agents Against Cross-Modal Attacks
👤 Haoyu Liu, Dingcheng Li, Lukas Rutishauser, Zeyu Zheng (UC Berkeley; Google; Google Deepmind)
🔗 arxiv.org/abs/2603.04364

隨著多模態 AI 代理越來越多地應用於自動化網頁操作，這項研究提醒我們：真正的安全，需要考慮所有可能的攻擊通道。

#AI安全 #多模態學習 #對抗訓練 #網頁代理 #UC Berkeley #Google #DeepMind #VisionLanguageModel #機器學習 #人工智慧
