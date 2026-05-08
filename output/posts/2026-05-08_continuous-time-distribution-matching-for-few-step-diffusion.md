---
title: "Continuous-Time Distribution Matching for Few-Step Diffusion Distillation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.06376
score: 124
model: tencent/hy3-preview:free
generated_at: 2026-05-08T19:52:25.857171
---

📌 【阿里/南开/吉大】连续时间分布匹配优化扩散蒸馏

少步擴散生成圖像總有偽影、過度平滑？
現有主流DMD蒸餾方法往往得加GAN才能救畫質。
這篇新框架直接從根源解決問題，不用額外輔助模組。

🤔 **離散時間蒸餾的先天缺陷，讓少步生成得靠GAN補畫質**
擴散模型生成質量頂尖但推理速度慢，step蒸餾是目前最主流的加速範式，其中分布匹配蒸餾（DMD）與一致性蒸餾是兩大代表路線。一致性蒸餾透過強制整個PF-ODE採樣軌跡的自一致性，將軌跡導向乾淨數據流形；但基礎版DMD僅依賴少數預定義離散時間步的稀疏監督，加上反向KL散度的模式尋求（mode-seeking）特性，容易產生視覺偽影、輸出過度平滑，往往得額外加入GAN、獎勵模型等複雜輔助模組才能恢復畫質，大幅增加訓練成本與複雜度。

🧪 **首次將DMD從離散錨點遷移到連續優化**
南開大學、阿里巴巴集團、吉林大學的團隊提出連續時間分布匹配（CDM），是首個將DMD框架從離散錨點遷移到連續優化的嘗試，核心包含兩項連續時間設計：
1. 將固定的離散調度替換為動態連續隨
