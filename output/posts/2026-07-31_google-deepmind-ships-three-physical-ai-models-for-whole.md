---
title: Google DeepMind Ships Three Physical AI Models For Whole Body Control, Dexterity
  And Multi Robot Collaboration
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/30/google-deepmind-gemini-robotics-2-whole-body-control-dexterity-multi-robot-collaboration/
model: tencent/hy3:free
generated_at: '2026-07-31T08:37:01.756260'
score: 107
---

📌 【Google DeepMind】Gemini Robotics 2 登場：從桌面操作跨越至全身控制與靈巧操作

TL;DR：Gemini Robotics 2 透過 VLA 與 ER 模型結合，實現從全身控制到多機器人協作的智能進化。

🤔 **打破預設程式與遠端操控的侷限**

目前的機器人多半依賴預設程式或遠端操控來執行狹窄且重複的任務，面對不可預測的環境時缺乏適應力，且技能難以在不同機器人主體間轉換。Google DeepMind 提出的 Gemini Robotics 2 正是為了同時解決這三大限制。

🧩 **三層次模型架構：從高層推理到底層動作執行**

Gemini Robotics 2 作為視覺—語言—動作 (VLA) 模型，能將視覺與語言輸入轉換為馬達控制指令，涵蓋從雙腳到指尖的全身控制，以及多指靈巧手或平行夾持器的操作。其系統設計採用了專業的分工模式：

1. **Gemini Robotics ER 2 (具身推理模型)**：
   作為高層大腦，基於 Gemini 3.5 Flash 開發。它能理解物理世界、與人類溝通，並規劃持續數分鐘的多步驟任務。
   - 輸入：交錯的文字、圖像、影片與音訊。
   - 規格：上下文視窗 (context window) 高達 128k，可輸出 64k tokens 的文字。

2. **Gemini Robotics 2 (核心 VLA 模型)**：
   負責執行具體的馬達控制，將高層規劃轉化為動作。

3. **Gemini Robotics On-Device 2 (裝置端 VLA 模型)**：
   針對機器人本地執行進行最佳化的高效能模型，基於 Gemini Robotics 1.5 技術與 Google 的裝置端 Gemma 模型開發。
   - 輸入：文字、圖像與機器人本體感覺 (proprioception) 的數值。
   - 輸出：機器人動作的數值。

💡 **開發者如何整合：將 VLA 作為工具使用**

在系統設計中，ER 2 會負責規劃並追蹤任務，隨後將馬達執行權交給被宣告為「工具」的 VLA 模型。開發者可以註冊低階控制介面（例如 VLA 模型或導航 API）作為可呼叫工具，並直接將多模態的影片、音訊或文字串流傳入模型中。

📊 **從桌面操作演進至全身控制**

與前代僅能控制機器人上半身進行桌面任務的 Gemini Robotics 模型不同，新一代模型將能力範圍擴展至全身控制與多機器人團隊合作，實現更完整的具身智能。

🎯 **實務啟示**

對於機器人工程師而言，這種將「高層推理 (ER)」與「底層控制 (VLA)」解耦的架構，提供了更具擴展性的開發模式，讓機器人能處理更複雜的時序任務，並能在本地端與雲端之間取得效能與反應速度的最佳平衡。

🔗 **來源**
- 標題：Google DeepMind Ships Three Physical AI Models For Whole Body Control, Dexterity And Multi Robot Collaboration
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/30/google-deepmind-gemini-robotics-2-whole-body-control-dexterity-multi-robot-collaboration/

#GoogleDeepMind #GeminiRobotics #VLA #EmbodiedAI #Robotics #MachineLearning #AI #Humanoid #MultiRobotCollaboration #ComputerVision
