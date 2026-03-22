---
title: "Google is using old news reports and AI to predict flash floods"
source: TechCrunch AI
url: https://techcrunch.com/2026/03/12/google-is-using-old-news-reports-and-ai-to-predict-flash-floods/
score: 107
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-12T19:15:16.004737
---

📌 **Google 用舊新聞＋AI 破解閃電洪水預測難題，全球 150 國上線**

閃電洪水是全球最致命的天災之一，每年奪走超過 5,000 條人命。但這種災害來得又快又急，傳統天氣預報系統很難準確預測。Google 想出一個出人意表的解法：用 AI 讀舊新聞。

🤔 **AI 讀新聞，找到隱藏的洪水資料庫**

閃電洪水之所以難以預測，是因為它們發生得太快、範圍太小，無法像氣溫或河川水位那樣被全面監測。這造成資料缺口，讓最先進的深度學習模型也無法發揮。

Google 研究團隊的解法是：用 Gemini（Google 的巨型語言模型）掃描全球 500 萬篇新聞報導，從中篩選出 260 萬起不同洪水事件，轉換成帶有地理標記的時間序列資料，稱為「Groundsource」。

這是 Google 首次將語言模型應用於這類工作，產品經理 Gila Loike 表示。這套系統已於週四公開研究成果與資料集。

🧪 **LSTM 模型結合天氣預報，預測閃電洪水風險**

有了 Groundsource 作為真實世界的基準資料，研究團隊訓練了一個基於長短期記憶（LSTM）神經網路的模型。這個模型會吸收全球天氣預報資料，計算特定區域發生閃電洪水的機率。

Google 的閃電洪水預測模型現在已在 150 個國家的 Flood Hub 平台上顯示城市區域的風險，並與全球緊急救援機構分享資料。

南部非洲發展共同體的緊急應變官員 António José Beleza 表示，在測試這套預測模型後，他的組織能更快回應洪水災情。

⚠️ **低解析度、不如美國官方系統精準**

這套模型仍有限制。首先，它的解析度相當低，只能在 20 平方公里的區域內識別風險。而且不如美國國家氣象局的洪水警報系統精準，部分原因是 Google 的模型沒有納入當地雷達資料。

🎯 **用 AI 連接歷史與未來，災害預報進入新階段**

這項研究展示了如何用 AI 將非結構化的歷史資料（新聞報導）轉化為有價值的預測工具。對全球許多天氣監測能力較弱的地區來說，這套方法可能提供關鍵的預警時間。

🔗 **論文連結**
📝 Using News Reports and AI to Predict Flash Floods
👤 Google Research 團隊
🔗 研究：尚未在 arXiv 上公開（Flood Hub 平台資料）

你覺得用新聞資料訓練災害預測模型還能應用在哪些領域？歡迎分享你的想法 👇

#AI #機器學習 #自然語言處理 #災害預防 #Google #FloodHub #LSTM #Gemini
