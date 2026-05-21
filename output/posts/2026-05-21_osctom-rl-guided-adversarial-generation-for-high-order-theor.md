---
title: "OSCToM: RL-Guided Adversarial Generation for High-Order Theory of Mind"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.20423
score: 99
model: tencent/hy3-preview:free
generated_at: 2026-05-21T21:06:42.284341
---

📌 **OSCToM：RL 對抗生成提升高階 Theory of Mind**

你有沒有想過，AI 真的能理解「我想知道你不知道的事」嗎？  
當 AI 需要同時考慮「他人相信什麼」和「自己相信什麼」時，傳統方法幾乎失效。OSCToM 卻讓準則從 0.2% 飆升至 76%。

🤔 **LLM 的 Theory of Mind 在複雜社會情境中仍顯不足**  
現有基準（如 ExploreToM）難以檢測遞迴信念與資訊非對稱，這些正是高階社會推理的核心挑戰。

🧪 **以強化學習導向的對抗性資料生成建模觀察者‑自我衝突**  
OSCToM 結合 RL、擴充領域特定語言（DSL）與組合式 surrogate 模型，專門產生 observer‑self 衝突情境。實驗中，OSCToM‑8B 在所有測試系統中表現最佳：在 FANToM 上優於既有 ExploreToM 結果，於 Hi‑ToM 與 BigToM 保持競爭力；在資訊非對稱的 FANToM 基準上達到 76% 正確率（相較於 ExploreToM 報告的 0.2%），且資料合成效率提升 6×。

💡 **針對性訓練資料讓較小模型也能處理高階認知推論**  
透過 RL 引導的對抗生成，OSCToM 能產出專門針對遞迴信念衝突的訓練樣本，這正是讓較小規模模型在複雜 ToM 任務上取得顯著提升的關鍵。

⚠️ **根據目前公開資訊，未見論文明確列出具體限制**  
摘要與評分理由中未提及樣本 size、實驗環境或潜在適用範圍的限制，因此此處無法提供進一步的限制說明。

🎯 **開放程式碼促進社會推理研究的後續探索**  
專案程式碼已於 GitHub 公開（https://github.com/sharminsrishty/osct），研究者可直接使用 RL‑導向的對抗資料合成框架，進一步提升 LLM 在高階 Theory of Mind 方面的表現。

🔗 **論文連結**  
📝 OSCToM: RL-Guided Adversarial Generation for High-Order Theory of Mind  
👤 Sharmin Sultana Srishty, Kazi Mahathir Rahman, Malaika Parizat Sakkhi, Samia Shahid Prianna, Shaikhul Islam Sinat @ BRAC University  
🔗 論文：https://arxiv.org/abs/2605.20423  
💻 程式碼：https://github.com/sharminsrishty/osct  

#AI #TheoryofMind #LLM #ReinforcementLearning #BRACUniversity #OSCToM #SocialReasoning
