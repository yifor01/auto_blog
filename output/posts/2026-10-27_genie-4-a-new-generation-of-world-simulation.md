---
title: 'Genie 4: A new generation of world simulation'
source: Google DeepMind
url: https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/
model: claude-code/sonnet
generated_at: '2026-10-27T21:26:53.364774'
pinned: true
---

📌 Google DeepMind 發布 Genie 4，能即時生成有聲音的世界

TL;DR：DeepMind 推出新一代世界模型 Genie 4，建立在 Gemini 家族之上，可即時模擬畫面、聲音與人物互動。

你打字輸入「下雨」，畫面裡的世界就開始下雨，還能聽到雨聲——這是 Google DeepMind 最新世界模型 Genie 4 的即時展示內容。

🤔 模擬世界，是通往 AGI 的必經之路

DeepMind 在文章中表示，理解並模擬世界是建構 AGI 的關鍵一環。Genie 4 的目標，是建立安全、可無限變化的模擬環境，應用範圍從為機器人與 agent 打造訓練環境，到解鎖全新的互動式體驗。

🧩 架構：站在 Gemini 家族的肩膀上

Genie 4 是 natively multimodal 的模型，能同步生成類似音樂的音訊、環境噪音與互動式對話。文章指出，這個模型整合並延伸了 Gemini 家族的能力：Gemini Omni 負責把模擬錨定在真實世界的外觀與行為上，其他 Gemini 模型則提供維持模擬連貫性與延續性所需的複雜推理。只要設定好一個起始事件，Genie 4 就會模擬接下來發生的一切：世界如何回應、聽起來如何、裡面的人物如何移動、反應與說話。

目前 Genie 4 以研究預覽（research preview）形式，優先推送給受信任的測試者，DeepMind 正在收集回饋，之後才會逐步開放給消費者與開發者，第一批將是 Google AI Ultra 訂閱者（透過 Project Genie）以及 Gemini API 與 Google AI Studio 的早期合作夥伴。

📊 四項核心能力中的兩大亮點

文章展示了 Genie 4 推進的多項能力，其中兩點特別具體：

- 即時塑形：使用者可用標準鍵盤操作導航與鏡頭，並用文字提示即時修改模擬內容，例如改變天氣、移動鏡頭，或加入新的人物或物件，Gemini 會依場景脈絡自動調整提示內容；在使用者輸入之間，Gemini 也會持續監控並引導場景，維持世界的連貫發展。
- 物理與人物動作的真實感：Genie 4 建立在更進階的物理理解之上，能模擬空氣動力學、碰撞等真實世界物理場景。文章稱「最戲劇化的躍進」在於人物模擬：角色能自然移動、對環境做出有機反應，並可在即時互動中被持續引導操控。

⚠️ 目前僅限受信任測試者，尚未對外開放

截至發布時，Genie 4 仍處於受限的研究預覽階段，一般消費者與開發者還拿不到，需要先加入 Project Genie 的候補名單等候後續開放。

🎯 實務啟示

對於開發機器人或 agent 訓練環境的工程師，這類世界模型提供了一種用自然語言快速生成多樣化模擬場景的可能性，值得留意候補名單開放後能否串接進既有的強化學習或 agent 訓練 pipeline；對互動內容與遊戲團隊而言，即時文字操控場景生成的能力，也值得關注其 API 形式開放後的實際可用性。

🔗 來源
- 標題：Genie 4: A new generation of world simulation
- 作者／機構：Google DeepMind（Raia Hadsell、Diego Rivas、Hang Qi）
- 連結：https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/

#GoogleDeepMind #Genie4 #WorldModel #Gemini #GenerativeAI #Robotics #AgentTraining #Multimodal #AGI #AIResearch
