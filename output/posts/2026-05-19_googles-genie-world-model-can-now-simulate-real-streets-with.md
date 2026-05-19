---
title: "Google’s Genie world model can now simulate real streets with Street View"
source: TechCrunch AI
url: https://techcrunch.com/2026/05/19/googles-genie-world-model-can-now-simulate-real-streets-with-street-view/
score: 107
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:52:24.861207
---

📌 【Google DeepMind】Genie 3 結合 Street View，打造可互動的真實街道模擬  

想像你能在不離開家的情況下，調整倫敦的天氣、看見雪覆蓋的曼哈頓街區——這不再是科幻，而是 Google 最新嘗試的可能性。  

🤔 **真實世界的圖像需要一個能「玩轉」的世界模型**  

長期以來，機器人訓練、城市規劃與沉浸式媒體都面臨同一個瓶頂：如何取得既豐富又可控的虛擬環境？純粹的合成資料往往缺少真實細節；而現有的街景圖像則是靜止的，無法互動或改變天氣、光線等條件。若能把海量的真實街景與具備世界模擬能力的模型結合，就能即時生成可調整的、互動的街道場景。  

🧪 **將 280 億張 Street View 圖像餵給 Genie 3**  

Google 透過多年收集的 Street View 資料——超過 280 億張圖像，覆蓋 110 個國家與七大洲——作為基礎圖像庫。在 Google I/O 2026 上，DeepMind 宣布將這筆龐大的真實影像與其通用世界模型 **Genie 3**（研究預覽版，於去年八月發布）進行整合。根據 DeepMind 開放性團隊的研究科學家 Jack Parker‑Holder 的說法，這樣的結合「對 agent 與 robotics 使用案例以及人類玩耍都很強大」，正是 Genie 從一開始的核心論點。  

🚗 **核心功能：即時生成可調整天氣的互動街景**  

整合後的系統能夠：  
- 使用真實街景作為基礎，生成可自由導航的 3D 街道環境；  
- 即時調整天氣（如陽光、雪落、雨勢）與光線條件；  
- 模擬特殊情境，例如「明天過後」式的極端天氣場景，以檢測機器人在罕見光照下的反應。  

Parker‑Holder 提供了兩個具體例子：  
1. 在倫敦很少見陽光的日子裡，讓機器人先在陽光照射維多利亞式建築的模擬街道中適應，避免真實遇到強光時的感測器衝擊。  
2. 使用者規劃前往紐約的行程，但想先體驗該街區在下雪時的樣子，系統能即時產生對應的雪景街景。  

💡 **為何這樣的結合特別有價值？**  

- **真實細節與可控性並存**：Street View 提供了無與倫比的真實紋理、建築樣式與街景佈局；Genie 3 則提供了世界模型的生成與互動能力，使得使用者不僅能「看」真實街景，更能「玩」它——改變天氣、時間或甚至加入虛擬物體。  
- **對機器人與代理訓練的直接好處**：透過在安全的虛擬環境中重現罕見或危險的天光條件，可減少實體測試的成本與風險，同時提升泛化能力。  
- **擴展至城市規劃與媒體創作**：規劃師可以模擬洪水、暴風雪等極端情境對交通與基礎設施的影響；內容創作者則能快速產出可互動的背景，用於遊戲、虛擬旅遊或電影前期視覺化。  

⚠️ **目前仍屬研究預覽版，公開存取受限**  

- Genie 3 於去年八月僅以研究預覽版發布，尚未開放完整的 API 或公開 demo。  
- 文章未提及任何正式的效能基準、使用者研究或大規模部署結果；因此實際系統的延遲、解析度或在邊緣設備上的可行性仍需後續驗證。  
- 雖然 Street View 資料龐大，但其覆蓋度與更新頻率會隨地區而異，極端或新發展地區的模擬品質可能受限。  

🎯 **對開發者與研究者的實務建議**  

- 若您從事機器人或強化學習研究，可關注 Genie 3 後續的開放版本，嘗試在模擬街景中加入天氣變數作為訓練課程。  
- 城市規劃或模擬公司可評估將此類互動街景作為情境分析的輔助工具，特別是需要快速迭代「什麼如果」場景時。  
- 媒體與遊戲開發團隊則可視為快速生成真實感街景基礎的起點，之後再進行藝術化處理或互動腳本的加入。  

🔗 **參考資訊**  
📝 TechCrunch 報導：Google’s Genie world model can now simulate real streets with Street View  
👤 作者：Rebecca Bellan  
🔗 連結：https://techcrunch.com/2026/05/19/googles-genie-world-model-can-now-simulate-real-streets-with-street-view/  

你認為這種「真實街景＋可調整世界模型」的組合，最適合用在哪些場景？歡迎在留言區分享你的想法 👇  

#GoogleDeepMind #Genie3 #StreetView #WorldModel #Robotics #UrbanPlanning #AI #TechNews
