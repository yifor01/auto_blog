---
title: "A New NVIDIA Research Shows Speculative Decoding in NeMo RL Achieves 1.8× Rollout Generation Speedup at 8B and Projects 2.5× End-to-End Speedup at 235B"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/01/a-new-nvidia-research-shows-speculative-decoding-in-nemo-rl-achieves-1-8x-rollout-generation-speedup-at-8b-and-projects-2-5x-end-to-end-speedup-at-235b/
score: 113
model: tencent/hy3-preview:free
generated_at: 2026-05-02T19:12:27.606098
---

📌 【NVIDIA 研究】推測解碼助 NeMo RL 訓練最高加速 2.5 倍

做數學推理、程式碼生成等可驗證任務的 RL 後訓練時，你是否常看著進度條乾等？
數據顯示，rollout 生成就佔了整個訓練步驟 65-72% 的時間，是最大瓶頸。
但 NVIDIA 團隊把原本只用於推理加速的推測解碼，直接整合進 RL 訓練迴圈，還保證目標模型的輸出分佈完全不變。

🤔 **RL 後訓練的最大瓶
