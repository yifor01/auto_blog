---
title: Are AI labs pelicanmaxxing?
source: Hacker News
url: https://dylancastillo.co/posts/pelicanmaxxing.html
model: tencent/hy3:free
generated_at: '2026-07-23T08:23:07.131865'
score: 81
---

這篇內容屬於「產業新聞／部落格報導」，因為其來源為個人部落格與社群討論，而非正式研究論文或開源專案。

📌 【趣味實驗】AI 實驗室會為了「鵜鶘騎單車」而針對性最佳化嗎？

TL;DR：研究者透過擴展經典的「鵜鶘騎單車」測試，探討 AI 模型是否存在針對特定 Prompt 的過度最佳化現象。

🎣 **一個從玩笑變成業界標準的非正式 Benchmark**

在過去幾年裡，Simon Willison 習慣用同一個指令測試所有主流 LLM 的表現：「Generate an SVG of a pelican riding a bicycle」（生成一張鵜鶘騎單車的 SVG 影像）。這個原本帶有戲謔性質的測試，如今已成為 AI 界最著名的非正式基準測試（informal benchmark）之一，甚至經常出現在 Hacker News 討論熱潮中。

🤔 **當金錢與效能掛鉤，模型會「投機取巧」嗎？**

隨著模型競爭進入白熱化，當動輒數十億甚至數兆美元的資金與市場佔有率掛鉤時，如果一個強大的測試結果能說服使用者，AI 實驗室是否有動機針對這類經典 Prompt 進行「Pelicanmaxxing」（針對鵜鶘測試進行最佳化）？為了驗證這個猜想，研究者進行了一場小型實驗。

🧩 **實驗設計：從單一動物擴展到多樣化組合**

為了測試模型是否只是「背下了」原本的指令，研究者建構了一個包含 8 種動物與 6 種交通工具的矩陣，總共產生 48 個指令組合：

- **動物清單**：鵜鶘 (pelican)、火烈鳥 (flamingo)、鷺鷥 (heron)、水獺 (otter)、浣熊 (raccoon)、羚羊 (antelope)、鯨魚 (whale)、貓 (cat)。
- **交通工具清單**：腳踏車 (bicycle)、獨輪車 (unicycle)、滑板 (skateboard)、滑板車 (scooter)、飛機 (plane)、船 (boat)。

研究者採用了與原指令幾乎完全相同的句構，僅更換動物與交通工具，並刻意選擇了與原指令（鵜鶘＋腳踏車）在相似度與難度上各異的組合。

📊 **實驗方法與分析**

研究者針對七個前沿模型（frontier models）生成了 1,008 個 SVG 檔案，並使用一個 LLM 作為裁判進行評分，最後利用 Claude Fable 5 進行資料分析。

⚠️ **實驗侷限性**

作者在文中也提到，動物與交通工具的選擇過程並非極度嚴謹，且實驗規模相對較小，僅作為初步探索。

🎯 **實務啟示**

這項研究提醒開發者，當我們依賴非正式的「梗測試」來評估模型能力時，必須意識到模型可能存在的過度最佳化（overfitting）風險。對於工程師而言，建立更具泛化能力且難以被「投機」的測試集，對於評估模型真實能力至關重要。

🔗 **來源**
- 標題：Are AI labs pelicanmaxxing?
- 作者／機構：dcastm
- 連結：https://dylancastillo.co/posts/pelicanmaxxing.html

#AI #LLM #Benchmark #SVG #MachineLearning #AIResearch #HackerNews #GenerativeAI #PromptEngineering #ArtificialIntelligence
