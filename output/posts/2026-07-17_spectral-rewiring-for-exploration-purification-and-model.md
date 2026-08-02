---
title: Spectral Rewiring for Exploration, Purification, and Model Merging
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.03065
score: 93
model: tencent/hy3:free
generated_at: '2026-07-17T08:11:54.364245'
---

📌 【HuggingFace Papers】用 Spectral Rewiring 只留推理核心，免訓練強化多域能力

TL;DR：SAR 從參數幾何抽取推理有效更新，僅用 0.58% 參數保留 99% 效能並改善融合。

強化學習已成為 LLM 後訓練的標配，但密集的全參數更新反而讓推理能力提早飽和，多域訓練或模型合併時還會互相干擾。問題可能不在「更新了多少」，而在「更新落在哪裡」。

🤔 **全參數更新帶來的兩個部署痛點**

論文指出，RL 後訓練中 dense full-parameter updates 會造成兩個與部署相關的瓶頸：一是推理表現受抑，常反映為 test-time scaling 提早飽和；二是多域訓練或 model merging 時，不同能力互相干擾（interference）。

🧩 **Subspace-Aligned Rewiring：對齊頻譜空間的後製編輯**

作者提出 Subspace-Aligned Rewiring（SAR），一種 post-hoc editing 方法。其核心觀察是：這些更新中對推理真正有效的部分，主要集中在 base model 的 spectral space。SAR 的做法是保留此頻譜核心（spectral core），同時移除正交分量（orthogonal components），藉此濾掉會抑制效能或放大跨域幹擾的殘餘更新方向，而不動用重新訓練。

📊 **只用約 0.58% 參數，保留超過 99% 後訓練效能**

在數個 model families 與不同 scale 上，SAR 僅用約 0.58% 的總參數量就能抽取出緊緻的 reasoning core，並達成以下結果：

- 保留超過 99% 的後訓練效能
- 在數學推理中改善 high-k exploration
- 泛化到 agentic coding：在某 in-house model 上，七個開放基準中有六個獲得提升
- 淨化混合域訓練更新：釋放受抑的 coding 能力，同時維持 math reasoning 與 instruction following
- 支援跨專家 model merging：產生的跨域泛化超越先前 merging baselines，甚至勝過最佳單域專家

💡 **從參數幾何看，推理有效更新可以很稀疏**

SAR 整體說明了一件事：從 parameter geometry 抽取 reasoning-effective updates，可以作為一種 training-free 機制，同時改善推理與多域表現，而不必重新跑訓練流程。

🎯 **實務啟示**

對工程師而言，若手上有 RL 後訓練好的模型卻苦於推理飽和或合併衝突，可嘗試這種後製頻譜重編碼思路：不必重訓，只要鎖定 base model 頻譜核心、濾掉正交雜訊，就有機會用極少參數保住推理增益並減少跨域幹擾。

🔗 **來源**
- 標題：Spectral Rewiring for Exploration, Purification, and Model Merging
- 連結：https://huggingface.co/papers/2607.03065

#SpectralRewiring #SAR #ModelMerging #ReinforcementLearning #LLM #PostTraining #Reasoning #ParameterGeometry #MultiDomain #TrainingFree
