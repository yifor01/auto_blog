---
title: 'NVIDIA Releases Alpamayo 2 Super: A 34B Open Vision-Language-Action Model
  for Robotaxis and Autonomous Driving Under OpenMDW-1.1'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/05/nvidia-alpamayo-2-super-open-vla-model-autonomous-driving/
model: tencent/hy3:free
generated_at: '2026-08-06T08:28:52.876620'
score: 105
---

📌 【NVIDIA 重磅發佈】34B VLA 模型 Alpamayo 2 Super：專為自動駕駛「長尾事件」設計

TL;DR：NVIDIA 推出 34B VLA 模型，結合 VLM 與 Diffusion Decoder，能輸出路徑與因果解釋，且開放商用。

面對自動駕駛中最棘手的「長尾事件」（Long-tail events）——即那些罕見且涉及多個代理人（multi-agent）的複雜情境，傳統的「偵測與預測」技術架構往往難以應對。NVIDIA 此次推出的 Alpamayo 2 Super，正是為了填補這項技術空白而生。

🧩 **32B VLM 結合 2.3B Diffusion Decoder 的強大架構**

Alpamayo 2 Super 是一個擁有 34B 參數的視覺-語言-動作（Vision-Language-Action, VLA）模型，其核心設計包含：
- **主幹網路**：採用 32B 的視覺語言模型（VLM）骨幹，基於 NVIDIA Cosmos 3 Super Reasoner 並經過強化學習（reinforcement learning）後訓練。
- **動作解碼器**：使用 2.3B 的擴散模型（diffusion-based）作為 Action Decoder。
- **輸入資訊**：模型接收多鏡頭 RGB 影片、文字指令以及包含時間戳的自我運動（egomotion）歷史紀錄。
- **輸出內容**：僅需單次處理全方位環視相機影片，即可同時輸出：
  1. 規劃路徑（Planned trajectory）
  2. 該路徑的因果解釋（Causal explanation）
  3. 元動作（Meta-action，如讓路或變換車道）

📊 **效能表現：在 LingoQA 評測中排名第一**

在多項關鍵指標上，Alpamayo 2 Super 展現了極強的競爭力：
- **LingoQA 評測**：Lingo-Judge 分數為 79.2，在近 40 個模型中排名第一。
- **對比測試**：
  - 領先 Qwen2.5-VL 72B 17.0 分。
  - 領先 Gemini 2.5 Pro 15.1 分。
  - 領先 GPT-4o 23.3 分。
- **規劃能力**：
  - 在 AlpaSim 閉迴路評估中，取得 1.50 ± 0.13 的分數。
  - 在 PhysicalAI-AV 開放迴路評估中，6.4 秒的 minADE₆ 為 0.911m。

💡 **透過因果鏈（CoC）提升安全性與標記效率**

該模型最引人注目的技術突破在於其「因果鏈」（Chain-of-Causation, CoC）技術。訓練資料中包含約 370 萬條結構化的因果解釋軌跡，這讓開發者能將「觀察到的情境」與「選擇的動作」直接關聯起來。

這不僅能與 NVIDIA Halos 安全驗證工作流整合，也符合 ISO/PAS 8800 的 AI 安全標準。此外，在實際應用中，NVIDIA 利用此模型作為自有車隊數據的自動標記工具（autolabeler），成功將標記週期從「數月」縮短至「數天」。

⚠️ **開放商用授權：OpenMDW-1.1**

與以往僅供研究使用的模型不同，Alpamayo 2 Super 採用 OpenMDW-1.1 許可證（Linux Foundation 針對開源模型發佈的寬鬆授權），並提供 Apache 2.0 授權的原始碼。這意味著開發者從第一天起就可以對其進行微調（fine-tuning）、開發衍生模型並進行商業分發。

🎯 **實務啟示**

對於自動駕駛與機器人工程師而言，Alpamayo 2 Super 的出現標誌著從單純的「感知-決策」轉向「感知-推理-動作」的一體化趨勢。其具備的因果解釋能力，解決了自動駕駛模型長期存在的「黑箱」問題，為安全性驗證與大規模數據自動標記提供了新的解決方案。

🔗 **來源**
- 標題：NVIDIA Releases Alpamayo 2 Super: A 34B Open Vision-Language-Action Model for Robotaxis and Autonomous Driving Under OpenMDW-1.1
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/05/nvidia-alpamayo-2-super-open-vla-model-autonomous-driving/

#NVIDIA #Alpamayo2Super #VLA #AutonomousDriving #Robotaxis #MachineLearning #ComputerVision #OpenSource #AI #DeepLearning
