---
title: 'Meet Kyutai REKI: The 2.4B VLA Model Bringing Efficient Memory to Robot Manipulation'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/17/meet-kyutai-reki-the-2-4b-vla-model-bringing-efficient-memory-to-robot-manipulation/
model: claude-code/sonnet
generated_at: '2026-10-18T19:31:10.849827'
score: 107
---

📌 【Kyutai 新作】24億參數 VLA 模型，靠記憶擺脫機器手臂卡頓

TL;DR：Kyutai 釋出 2.4B 參數的開源 VLA 模型 REKI，用一套輕量的暫存器記憶機制大幅降低機器手臂的振盪失敗率。

機器手臂伸到一半忽然在兩個姿勢之間來回擺動，這是許多 vision-language-action（VLA）模型常見的失敗模式。Kyutai 與 Inria、École des Ponts 合作釋出的 REKI，把問題歸因於「感知混淆」（perceptual aliasing），並用一套不太一樣的記憶設計來解決它。

🤔 **多數 VLA 只看「這一幀」，代價很高的記憶方案**

多數 VLA 模型只根據當下這一幀畫面決定動作。先前要加上記憶能力的作法，不外乎把過去幀餵進 vision-language model（VLM）、展開訓練序列，或額外加模組，每一種都會拉高運算成本。REKI 選擇把記憶放進 action expert 內部，而不是放進 VLM。

🧩 **32 個暫存器 token，只看畫面不看動作**

REKI 把 Qwen3.5-2B 當作骨幹，搭配一個 2 億參數的 action expert。這個 expert 透過 flow matching 產生動作區塊，以 10 步 Euler 積分完成；機器人狀態與 flow time 透過 adaptive RMSNorm 注入，每一種機器人狀態格式都配有自己的小型 state MLP。

記憶機制的運作方式：
- 每一幀的動作 token 之前，會放入 32 個學習而來的暫存器（register）token。
- 這些暫存器會 cross-attend 當下這一幀的提示詞與畫面編碼。
- 同時也會 self-attend 之前幀的暫存器，形成跨幀的記憶鏈。
- 暫存器從不讀取動作 token，因此只取決於觀察畫面，與 flow time、機器人狀態無關。
- 每幀只計算一次，並以滾動視窗快取，成本很小。

📊 **RoboTwin 振盪率從 18.6% 降到 4.1%**

| 項目 | 數據 |
|---|---|
| RoboTwin 振盪型失敗（無記憶 → 有記憶） | 18.6% → 4.1% |
| 預訓練帶來的提升（Clean2Rand） | +13.8 分 |
| 預訓練帶來的提升（雜亂場景 clutter） | +30.3 分 |
| 記憶機制帶來的提升（LIBERO-Plus） | +1.5 分 |
| 記憶機制帶來的提升（RoboCasa365） | +5.4 分 |

Kyutai 表示 Clean2Rand 的平均值是依 Qwen-RobotManip 報告 Table 5 的 6 種條件計算而來，該報告也列出 π0.5 在 LIBERO-Plus 上為 84.4 分，可作為對照。REKI 先做一次預訓練，再針對各個 benchmark 分別微調。

💡 **只用公開資料，規模卻比想像中大**

REKI 完全只用公開資料預訓練，混合資料量達 10 億幀，外加 1,220 萬筆 vision-language 樣本。其中真實機器人遙操作資料佔 6.398 億幀，模擬資料 1.939 億幀，第一人稱人類影片 1.709 億幀，來源包含 DROID、BridgeData V2、AgiBot World、EgoDex 與 EgoVerse。Kyutai 刻意保留每個資料集原生的控制慣例，不做動作重映射，預訓練共跑了 20 萬步，使用 32 張 H100。釋出的六個 checkpoint 包含預訓練 base，以及針對 LIBERO、RoboTwin（兩種變體）、RoboCasa365、RoboCasa-GR1 的微調版本。真實機器人部署採用 LeRobot 的 async-inference gRPC 協定，在 UR5 手臂上，REKI 只用每個任務 50 筆示範、微調 3,000 步（約 1 小時）就能上線。

🎯 **實務啟示**

對做機器人學習的工程師而言，REKI 展示了一條便宜的路：與其把記憶塞進 VLM 增加推論成本，不如在 action expert 內部用少量暫存器處理跨幀資訊。模型權重、論文與程式碼都已公開，值得拿來對照自家 VLA 在 out-of-distribution 場景下的表現。

🔗 **來源**
- 標題：Meet Kyutai REKI: The 2.4B VLA Model Bringing Efficient Memory to Robot Manipulation
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/17/meet-kyutai-reki-the-2-4b-vla-model-bringing-efficient-memory-to-robot-manipulation/

#RoboticsAI #VLA #Kyutai #RobotManipulation #OpenSourceAI #FlowMatching #EmbodiedAI #HuggingFace #MachineLearning #AIResearch
