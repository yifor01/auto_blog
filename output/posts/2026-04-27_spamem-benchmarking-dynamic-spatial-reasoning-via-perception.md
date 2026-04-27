---
title: "SpaMEM: Benchmarking Dynamic Spatial Reasoning via Perception-Memory Integration in Embodied Environments"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.22409
score: 114
model: tencent/hy3-preview:free
generated_at: 2026-04-27T19:56:41.302203
---

📌 SpaMEM：具身空間推理診斷基準

你以為多模態大模型已經搞定空間推理了？
現有模型在靜態看圖答題表現優異，但放到具身環境長時交互，連剛才移動的物體位置都無法持續追蹤。

🤔 **靜態視覺推理成熟，具身長程空間一致性仍是痛點**
多模態大語言模型（MLLMs）近年在靜態視覺-空間推理任務上已有顯著進展，但一旦進入具身場景，環境持續變化、智能體需從自我中心觀察不斷修正空間信念，現有模型往往無法維持長程空間連貫性。這個問題對具身智能、AI Agent的落地至關重要，家庭服務機器人、人形機器人等應用都需要可靠的長時空間記憶能力，卻始終缺乏針對性的評測基準。

🧪 **千套程序生成房屋、千萬級多模態圖像
