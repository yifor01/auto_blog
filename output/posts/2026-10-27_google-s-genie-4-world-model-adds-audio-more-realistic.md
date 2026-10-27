---
title: Google’s Genie 4 world model adds audio, more realistic worlds, and real-time
  steering
source: TechCrunch AI
url: https://techcrunch.com/2026/10/27/googles-genie-4-world-model-adds-audio-more-realistic-worlds-and-real-time-steering/
model: claude-code/sonnet
generated_at: '2026-10-27T21:30:02.899117'
score: 103
---

📌 Google DeepMind 發布 Genie 4：世界模型首次加入即時音訊與互動配音

TL;DR：Genie 4 能邊模擬邊接受文字指令即時改場景，還同步生成配樂與對話音訊。

如果一個世界模型除了畫面，連背景音樂、環境音效、甚至角色對話都能即時生成呢？Google DeepMind 週二發布的 Genie 4 研究預覽版，正是把「可互動的世界」又往前推了一步。

🤔 **世界模型賽道正在加速洗牌**

Genie 4 是 Genie 3（一年多前發布）的後繼者，同時也踩在一個競爭愈發激烈的產業節點上：AI 影片新創 Runway 幾個月前剛推出第二代世界模型 GWM Worlds 2，同樣支援動態回應使用者輸入並生成音訊。與此同時，產業整併正在發生：Fei-Fei Li 的 World Labs 正被 AMD 收購，Amazon 在與 Decart 洽談收購，Rivian 也剛併購 Third Dimension，把模擬能力收進自駕測試的內部流程。Genie 4 可以視為 Google 在這個擁擠賽道上保持領先的最新一步。

🧩 **即時音訊、自由編輯、Gemini 當導演**

相比前代，Genie 4 的核心升級在三個方向：

- 更擬真的畫面與互動性：使用者可以在模擬進行中輸入文字 prompt，即時改變場景。
- 即時音訊生成：包括配樂、環境音效，以及與世界互動的對話音訊，且與畫面同步。
- 自由形式編輯：可以即時改變天氣、鏡頭角度，或加入新的人物與物件，場景一致性最長可維持兩分鐘（是前代的兩倍），物理表現與人物的真實感也有提升。

更值得注意的是 Gemini 與 Genie 4 的整合方式：Gemini 扮演「導演」角色，負責規劃步驟並檢查畫面，Genie 則負責實際生成畫面內容。在一項結合 Gemini Robotics 的研究實驗中，Gemini 4 Argon 模型把任務拆解成步驟，再由 Genie 4 即時模擬出來,這為「先在模擬環境測試機器人情境，再搬到真實世界」提供了一種可能路徑。Google 研究總監 Tejas Kulkarni 在簡報中表示：「未來我們會越來越常看到這種混合世界模型——Gemini 負責寫程式碼與文字，Genie 則即時攝取這些內容,在不同抽象層級模擬現實。」

💡 **意外的應用場景：電影前期製作**

官方主打的商業場景是遊戲、互動學習與機器人測試（例如走進一幅歷史畫作，和畫中人物對話那段事件）。但率先拿到測試權限的「trusted testers」反而指出了另一個用法：電影前期構思。Google DeepMind 工程師 Diego Rivas 在簡報中提到：「即時性在需要保持創作『流暢狀態』的場景最有價值,比如構思階段、分鏡階段，任何需要快速試錯的時刻。」他也提到，使用者未來或許能搭配 Google 的 Veo（文字/圖片/影片生成高畫質同步音訊影片的模型，已在影視創作者間逐漸普及）以及多模態模型 Gemini Omni，把這些原型進一步轉成正式素材,不過他也坦言這些能力「還有一段距離」。

⚠️ **仍是早期階段：細節會跑掉、字看不清**

團隊也坦承 Genie 4 還有明顯缺口：模擬時間越長，細節與物件越容易漂移（drift）；音訊準確度與世界中文字的可讀性,目前都還沒有解決方案。Rivas 反覆強調現在談「最終產品體驗長什麼樣」還太早。

🎯 **對工程師的意義**

Genie 4 目前以研究預覽形式提供給 trusted testers，未來幾週會開放給 Google AI Ultra 訂閱者（透過 Project Genie）,以及 Gemini API 與 Google AI Studio 的早期合作夥伴。對做機器人模擬、遊戲原型或互動內容的團隊來說，值得關注的不是畫面好不好看，而是「Gemini 規劃 + Genie 渲染」這種分工模式,這很可能是未來一段時間世界模型產品化的主要架構方向。

🔗 **來源**
- 標題：Google's Genie 4 world model adds audio, more realistic worlds, and real-time steering
- 作者／機構：Rebecca Bellan, TechCrunch AI
- 連結：https://techcrunch.com/2026/10/27/googles-genie-4-world-model-adds-audio-more-realistic-worlds-and-real-time-steering/

#GenieModel #GoogleDeepMind #WorldModel #Gemini #GenerativeAI #AIVideo #Robotics #AIGaming #MultimodalAI #AIResearch
