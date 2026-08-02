---
title: Understanding Reasoning from Pretraining to Post-Training
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.16097
score: 95
model: tencent/hy3:free
generated_at: '2026-07-20T08:52:02.843290'
---

📌 【HuggingFace Papers】用西洋棋當實驗場，看清 Pretraining 如何決定 RL 成效

TL;DR：研究以西洋棋為受控測試平臺，證實 pretraining loss 可預測後續 RL 的推理表現。

強化學習（RL）已成為提升 LLM 複雜推理能力的標準手段，但多數研究把 RL post-training 孤立看待，忽略了它前面還有龐大的 pretraining。兩個根本問題因此懸而未決：pretraining 的模型規模與資料選擇，如何影響 RL 運算的回報？RL 究竟對模型做了什麼？

🤔 **為什麼 LLM 設定下很難回答這兩個問題**

標準 LLM 環境中，pretraining 語料極為龐大且不受控，很難區分某個行為來自 pretraining 還是 RL；此外，跨兩個階段做系統性的 compute sweep 成本高到不切實際。作者因此轉向一個可控的測試平臺。

🧩 **把西洋棋當成完整訓練管線的代理任務**

研究遵循標準 LLM 訓練流程，建立受控實驗：
- Pretraining：從 5M 到 1B 參數的語言模型，在人類西洋棋對局上做 pretraining。
- Supervised Fine-Tuning（SFT）：使用合成推理軌跡（synthetic reasoning traces）進行微調。
- RL：在具可驗證獎勵的西洋棋謎題上執行 RL。

資料流概念上即為：人類棋譜 pretraining → 合成推理軌跡 SFT → 西洋棋謎題 RL（可驗證獎勵）。

📊 **Pretraining Loss 能預測 RL 後的表現**

在此框架下，作者發現：
- 在給定 RL compute 水準下，post-RL 的表現可由 pretraining loss 良好預測。
- RL reward 曲線的斜率，隨 pretraining tokens 增加而近似線性提升。

也就是說，pretraining 階段投入的資料量，直接反映在後續 RL 的學習效率上。

💡 **RL 不是單純把 SFT 政策變尖銳**

除了規模效應，研究觀察到 RL 的作用因題目難度而異：
- 在簡單謎題上，RL 放大 SFT policy 本來就偏好的正確走法。
- 在困難謎題上，RL 浮現出 SFT 下幾乎不存在的正確走法。

這顯示 RL 不只是「 sharpen the SFT policy」，而是有更細緻的機制。

🧩 **數學領域的初步驗證**

作者進一步測試發現是否超越西洋棋：訓練一個 1B 語言模型於數學領域文字，同樣的預測模式出現——pretraining 較久的 checkpoint 在 post-RL 達到更高表現，且在 RL 下進步更快。

⚠️ **研究限制**

素材未提及作者自述的額外侷限，僅能確認實驗以西洋棋為主要受控測試平臺，數學領域僅做轉移驗證，尚非全面證明。

🎯 **實務啟示**

若你正在規劃 LLM 的推理能力訓練，不要把 RL 階段當成獨立槓桿：pretraining 的 loss 與 token 量可能是後續 RL 投報率的先行指標。在資源分配上，先確保 pretraining 品質，再用 RL 針對難題「喚出」模型潛藏能力，可能比盲目加 RL compute 更有效。

🔗 **來源**
- 標題：Understanding Reasoning from Pretraining to Post-Training
- 連結：https://huggingface.co/papers/2607.16097

#LLM #ReinforcementLearning #Pretraining #PostTraining #Reasoning #Chess #SFT #RL #HuggingFacePapers #Scaling
