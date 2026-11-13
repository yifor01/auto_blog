---
title: ChatGPT Wallet lets OpenAI’s Dots agents make purchases for you
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/1033425/openai-chatgpt-wallet
model: claude-code/sonnet
generated_at: '2026-11-13T22:56:40.925345'
score: 76
---

📌 OpenAI 推出 ChatGPT Wallet,讓 Dots agent 幫你刷卡

TL;DR：OpenAI 開放 Dots agent 代為購物的錢包功能,每次結帳仍需使用者按指紋確認。

讓 AI agent 自己去逛網站、幫你下單購物,聽起來方便,但前提是你得先放心把付款方式交給它。OpenAI 在 Dots agent 平臺上線後,接著推出了 ChatGPT Wallet,試圖用「每次結帳都要人確認」的機制來解決這個信任問題。

🤔 **從「會逛網站的 agent」到「會付款的 agent」**

OpenAI 今年早些時候推出了 Dots AI agent 平臺,這次則是為這些 agent 加上錢包功能。ChatGPT Wallet 從今天開始,先對美國地區、18 歲以上、使用美國帳單地址,且訂閱 ChatGPT Pro 的使用者開放,支援的卡片包括符合資格的美國發卡 American Express、Chase、Mastercard 與 Visa 卡。

🧩 **每次結帳都要生物辨識確認**

使用方式是先把信用卡加入 ChatGPT Wallet,之後 Dots agent 就可以依照使用者的提示去購買商品,但每次結帳前都會先跟使用者確認。根據 OpenAI 的支援頁面說明,每一筆用 ChatGPT Wallet 完成的購買,都需要經過安全檢查,包括 Face ID 或指紋辨識這類生物辨識驗證,使用者必須核准每一筆從 ChatGPT Wallet 發出的購買。

在卡片資訊的處理上,OpenAI 表示其做法類似 tap to pay、Apple Pay 或 Google Wallet：使用者審核並核准 agent 的購買行為後,系統會用一個付款 token 取代實際的信用卡資訊,因此真正的卡號不會傳給 Dots agent,也不會傳給收款的商家。

💡 **終極目標是讓 agent 完全自主下單**

OpenAI 表示,未來的方向是讓使用者可以把購買行為完全委託給 agent,方法是事先設定明確的參數,例如花費上限、購買類別或時間區段,並預先核准在這些條件內的購買。目前推出的版本仍要求每次都經過人工確認,算是朝這個目標邁出的第一步。

⚠️ **不是每個網站都歡迎 AI agent 購物**

ChatGPT Wallet 不保證在所有地方都能用。部分零售商對 AI agent 的購買行為設有限制,甚至直接封鎖。OpenAI 也提到,今年稍早 Amazon 曾封鎖 Meta 的 Muse agent。要讓 agent 能順利使用 ChatGPT Wallet,OpenAI 表示「網站需要確保 agent 不會被誤判封鎖,付款與風險控管系統也需要能辨識出 agent 發出的合法購買行為」,這代表實際普及程度,很大一部分取決於商家端系統是否願意配合調整。

🎯 **對開發者與產品團隊的觀察點**

這則新聞目前揭露的技術細節有限,主要是產品層面的功能上線,背後的付款 token 化、風險判斷機制等具體實作方式尚未公開。如果你的產品或服務可能被 AI agent 當作購物目標,值得提早評估自己的風控與驗證系統是否能正確識別並放行合法的 agent 購買請求,否則很容易像 Amazon 一樣選擇直接封鎖。

🔗 **來源**
- 標題：ChatGPT Wallet lets OpenAI's Dots agents make purchases for you
- 作者／機構：Stevie Bonifield @ The Verge
- 連結：https://www.theverge.com/ai-artificial-intelligence/1033425/openai-chatgpt-wallet

#OpenAI #ChatGPT #AIAgents #Dots #DigitalWallet #AgenticCommerce #Fintech #AIPayments #ConsumerTech #AutonomousAgents
