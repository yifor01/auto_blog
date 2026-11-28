---
title: Android’s DIY widgets are a bit of vibe-coding fun
source: The Verge AI
url: https://www.theverge.com/tech/1041801/android-intelligence-create-my-widget-gemini
model: claude-code/sonnet
generated_at: '2026-11-28T00:48:40.590563'
score: 48
---

📌 Android的AI小工具：做梗圖很順，做實用功能卡關

TL;DR：Google把vibe coding搬進Android小工具，娛樂性有餘，即時資料整合仍不足。

公車快來了，沒來得及確認時間就錯過，這種煩惱理論上正是「用AI做個小工具」最該解決的場景。結果體驗下來，AI小工具做得出每小時換一句電影臺詞的桌面裝飾，卻做不出一班準時報時的公車動態。

🤔 從I/O發布到Pixel上線

Google在今年春季的I/O大會上公布了用AI生成自訂小工具的功能Create My Widget，屬於Android「Gemini Intelligence」功能套件的一部分。這項功能目前仍處於beta階段，本月才開始在Pixel手機上逐步推送。

《The Verge》作者Allison Johnson在Pixel 11 Pro上實測，發現做出第一個小工具只花了大約20秒：一個每小時顯示一句《Jurassic Park》（原始電影，非續集）臺詞的桌面小工具，點下去會連到Reddit上的r/MovieQuotes討論串。

🧩 本質上是「Gemini捷徑」，不是客製化mini app

作者觀察到，許多透過Create My Widget做出來的小工具，其實是包著小工具外殼的Gemini提示捷徑：點一下小工具，會跳出Gemini介面，經過一段思考時間後給出答案。建立介面會提供幾類範本與分類，偏向較實用的用途，例如習慣追蹤、食譜靈感等。從報導描述可以歸納出幾種固定範本：倒數計時（顯示到某個假日或行事曆事件的倒數）、運動比分（顯示喜愛球隊的近期比分與下一場開賽時間），以及開放式查詢（透過Google搜尋結果產生內容，例如每天換一款三種材料的調酒食譜，或交給Gemini自行判斷）。

📊 四個小工具，兩種體驗落差

作者實測做出幾個小工具：《Jurassic Park》臺詞小工具每小時顯示一句原始電影臺詞，點擊連到Reddit討論串，20秒內完成，體驗良好；下雨提醒小工具下雨時顯示小熊維尼名句「Tut tut, looks like rain」，不下雨則顯示「No rain right now」；走路紀錄小工具原本希望做出視覺化的連續紀錄，結果只做出一個標示「Log Walk」的按鈕，點擊後觸發Gemini把這次散步加進行事曆，Gemini額外建議做成一週打勾清單；至於作者最想要的公車即時到站小工具，她要求列出指定站牌的即時到站時間，結果小工具只顯示「Bus Arrivals」，點擊後由Gemini搜尋到站時間，回覆的是一段描述班次頻率與預估到站時間的文字，而不是一目了然的即時資訊。

💡「一目了然」與「交給Gemini想」的落差

作者原本期待的是可以依自己需求客製化的mini app，但實測下來，這項功能更接近「套版式」體驗：符合既定範本（倒數、比分、搜尋型查詢）的需求做得不錯，但需要即時、結構化資料（像是公車動態）的場景，目前仍只能落到「觸發Gemini生成一段文字回覆」，而非真正讀取即時資料來源並以視覺化方式呈現。

⚠️ 仍在beta，功能邊界明顯

這項功能才剛開始在Pixel機型上推送，仍處於beta階段。從實測結果看，它目前解決的是「好玩」而非「實用」的需求，對於需要即時資料整合的場景（交通動態、感測器數據等）尚未能真正取代原生app。

🎯 對開發者與產品團隊的啟示

這次實測提供了一個清楚的訊號：把LLM包裝成「小工具產生器」，使用者很快能感受到背後是制式範本加Gemini提示，而不是真正能存取結構化即時資料的客製化邏輯。如果要讓這類生成式UI功能真正解決使用者的日常痛點（例如即時交通資訊），背後仍需要串接實際的資料API，而不能只靠LLM生成文字描述來頂替。

🔗 來源
- 標題：Android's DIY widgets are a bit of vibe-coding fun
- 作者／機構：Allison Johnson，The Verge
- 連結：https://www.theverge.com/tech/1041801/android-intelligence-create-my-widget-gemini

#Android #Gemini #VibeCoding #GenerativeUI #GooglePixel #AIWidgets #ConsumerAI #UXDesign #LLMApps #MobileAI
