---
title: Runway’s WorldPrompt and the Engineering of Real-Time Worlds
source: Latent Space
url: https://www.latent.space/p/runway
model: claude-code/sonnet
generated_at: '2026-09-25T20:46:06.258033'
score: 97
---

📌 Runway 公布 WorldPrompt：即時世界模型的工程硬仗

TL;DR：Runway 用 WorldPrompt 讓使用者即時下指令控制生成世界，但誤差累積與記憶體管理仍是硬骨頭。

如果一個遊戲世界不是被寫死的程式碼，而是模型一幀一幀「畫」出來的，那要怎麼在畫面播放的同時接受你的操作指令？這正是 Runway 這次要解決的工程問題。

🤔 **即時世界模型的軍備賽**

Runway 本月推出 GWM Worlds 2 研究預覽版，官方形容這是把「高保真度的影片與音訊生成，轉換成即時互動模擬」。Runway 稱其為「autoregressive diffusion」模型，autoregressive（自迴歸）指的是它如何隨時間生成內容。這波賽道並不冷清，Google DeepMind 的 Genie 3（同樣以 720p、24 fps 生成）、Odyssey-2 Pro，以及 World Labs 的 RTFM（Real-Time Frame Model）都在同一個方向上競爭。Google 也坦言 Genie 3「目前只能支援數分鐘的連續互動，而非長達數小時」，顯示這整個領域仍處於早期階段。Runway 目前估值約 53 億美元，今年 2 月剛完成 3.15 億美元募資，去年 12 月才推出第一版 GWM Worlds。

🧩 **WorldPrompt：不是程式語言，是一種控制層**

WorldPrompt 是 GWM Worlds 2 的新功能，作為 Latent Space 採訪對象、Runway Principal Research Scientist Robin Kahlow 所說，它是一種「控制世界裡所有不同主體」的方式,類似電玩裡的機制,例如讓 NPC 走向玩家並開口說話。使用者可以固定生成世界的某些部分（包括第一幀畫面），再建立一系列帶時間戳記的事件，這些事件甚至可以即時下達。但 Runway CTO Kamil Sindi 強調，WorldPrompt 終究是一種 prompting 機制,而非程式語言,因此不像 Minecraft 或 Roblox 那樣具備腳本能力或狀態控制。Kahlow 也坦言目前「不完美，仍有瑕疵」，指令能否被準確遵循很看動作難度，「移動類的動作相對可靠」。

在生成管線上，共同創辦人暨共同執行長 Anastasis Germanidis 在 Latent Space 的 podcast 中透露，流程從「雙向擴散模型（bidirectional diffusion）」開始，這種模型原本是一次生成整段影片，再被改造成自迴歸式，讓模型可以「一次生成一幀或幾幀畫面」。具體做法是：Runway 先把基礎的音訊影片生成模型微調到能理解 WorldPrompt 格式，接著後訓練成自迴歸生成，最後透過蒸餾方法讓它達到即時速度。Germanidis 提到蒸餾有兩種路徑,把大模型蒸餾成小模型,或是減少擴散步數,例如從 50 個去噪步驟壓縮到 4 個，畫質會有損失但結果可能接近。最終呈現為連續 720p、24 fps 的影片串流，搭配 48,000 Hz 音訊。

| 專案 | 已知特色（依素材） |
|---|---|
| Runway GWM Worlds 2 | 720p、24 fps 影片，48,000 Hz 音訊，具 WorldPrompt 控制層 |
| Google DeepMind Genie 3 | 720p、24 fps 生成，目前僅支援數分鐘連續互動 |
| Odyssey-2 Pro | 素材僅提及名稱，未提供技術細節 |
| World Labs RTFM | 素材僅提及名稱，未提供技術細節 |

💡 **誤差會累積，記憶也不完美**

Germanidis 直言自迴歸模型最大的挑戰是誤差累積:「你把生成出來的畫面餵回模型去生成下一幀，任何微小錯誤都會隨時間累積。」Sindi 補充,「無限生成」帶來另一個難題,要保留哪些上下文、丟棄哪些不重要的內容,否則會把 GPU 記憶體用爆。長期記憶也還是未解問題，Kahlow 直言「模型沒有完美的記憶，這仍是開放的研究課題」。更微妙的是反事實生成（counterfactual generation）的落差：Germanidis 舉例，網路上的足球影片訓練資料，成功進球的畫面遠多於失敗嘗試,因此模型渲染前者會比後者更逼真,「你希望不同的行動選擇,都能生成同樣寫實的結果」,這正是影片模型與世界模型的本質差異。當場景變成多提示、多角色、多場景時，Sindi 也坦承評估因果關係變得困難,Runway 雖有自動化的可驗證測試,但仍建議使用者親自動手測試模型的極限。

🎯 **對工程師的實務啟示**

GWM Worlds 目前沒有結構化狀態可讀取，Kahlow 說「這裡沒有結構化狀態，模型觀察到的就跟你在現實中用攝影機觀察到的一樣」。這意味著下游應用（如機器人模擬測試、大規模 agent 合成資料生成）目前只能靠影片與音訊本身理解世界變化。Germanidis 也提出一個值得關注的方向：未來可能把推理模型用於場景規劃，再把規劃結果傳給負責生成像素的擴散頭（diffusion head）,這對想結合世界模型與 agent 系統的工程師來說是值得追蹤的架構思路。

🔗 **來源**
- 標題：Runway's WorldPrompt and the Engineering of Real-Time Worlds
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/runway

#WorldModels #Runway #GenerativeVideo #AutoregressiveDiffusion #RealTimeAI #AIGaming #DiffusionModels #GenAI #AIResearch #VideoGeneration
