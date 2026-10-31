---
title: I built an AI Tamagotchi before Meta could
source: The Verge AI
url: https://www.theverge.com/gadgets/1013375/muse-charm-gadgets-preview-waveshare-esp32-claude-vibe-code
model: claude-code/sonnet
generated_at: '2026-10-31T20:42:56.704720'
score: 55
---

📌 搶在 Meta 前面，記者用 $50 開發板做出「山寨版」Muse Charm

TL;DR：The Verge 編輯用 Waveshare ESP32 開發板搭配 Claude Code vibe coding，比 Meta Muse Charm 正式上市還早做出類似裝置。

Meta 把 AI 包裝成一張軟萌的小臉，打算在這個耶誕季靠 Muse Charm 讓使用者把「AI 夥伴」掛在身上。但 The Verge 資深編輯 Sean Hollister 說，他家早就有一個「自製版」Muse Charm 了，而且只花了 50 美元。

🤔 **官方認證的開發板，長得就像 Muse Charm**

Hollister 買的不是玩具，而是 Waveshare ESP32-S3 1.75C，一款 1.75 吋觸控螢幕的 push-to-talk AI 裝置開發板。這塊板子被 Meta 官方列為打造「Muse Gadget」的首選硬體之一，因為它能直接用 Meta 開源程式碼與 token 連上 Muse AI 雲端服務。設定過程不算複雜：接上 PC、讓 Claude 讀取 Meta 的 GitHub 專案、再把裝置與 Muse 手機 App 配對即可。

🧩 **裝上去之後，發現一堆沒做完的坑**

但真正可用之前，問題一個接一個冒出來。Muse 一開始會把語音指令誤判成「請轉錄這段音訊」而不是指令；回應速度時快時慢；而且螢幕一次只顯示幾個字，沒有語音播報，也沒有完整對話紀錄可翻看，除非拿出手機上的 Muse App 對照。Meta 原廠的範例也只附上一個「Jolly」人物形象，大多時候只是呆站著；它也不會像 Amazon Echo 或 Google Home 那樣自動偵測智慧家庭裝置。官方雖然附上一個示範程式，展示 Muse Gadget 如何串流手機鏡頭畫面，卻連遠端快門按鈕都沒做，拍照用途相當有限。

💡 **靠 Claude Code 把缺口一個一個補上**

接下來幾輪 Claude Code 的「vibe coding」補完了幾乎所有缺口。Hollister 反覆把裝置接回 PC，直接用自然語言告訴 Claude 他想要什麼：一個可以左右滑動查看完整對話的歷史紀錄頁面；接上 ElevenLabs 免費方案裡最不「掉魂」的英式語音，讓 Muse 的回答能唸出來；修正手機前鏡頭畫面上下顛倒的問題；加上按鈕就能讓手機從遠處拍出高畫質預覽照片；甚至透過藍牙做出低畫質的即時取景畫面，離開家用 Wi-Fi 也能用。

他還讓 Claude 仿照 Meta Connect 展示過的人物形象做出一整批不同的虛擬寵物，並加入類似 Tamagotchi 的小遊戲:寵物需要餵食、玩耍、睡覺、洗澡，後來又加碼做出飢餓、無聊、髒污各四個等級,吃零食會留下碎屑讓寵物變髒,玩太久則會讓牠變累。連裝置外觀像懷錶這件事,Claude 都只花了 15 分鐘就做出一個真的能報時的三針錶面。

⚠️ **程式碼品質未知，信任風險自負**

Hollister 坦言自己完全不會寫程式,無法判斷這些由 Claude 生成的程式碼品質好壞,甚至可能存在嚴重缺陷。他也提到曾有評測者反映 Muse 洩露了自己的住家地址，因此從一開始就把裝置接在訪客 Wi-Fi 上，不敢把它接進家用網路或信箱。

🎯 **這給工程師的提示：硬體裝置的價值在於「可自由改寫」**

這次嘗試讓 Hollister 得出一個結論:一支專用的 AI 口袋裝置真正的價值,不在於 Muse 本身能做什麼,而在於它能被使用者用 AI 輔助工具改寫成任何形狀。這也讓人好奇,正式上市的 Muse Charm 到底會不會開放到這種程度地自由編程,或者真正想動手的人,其實更該直接買開發板。

🔗 **來源**
- 標題：I built an AI Tamagotchi before Meta could
- 作者／機構：Sean Hollister, The Verge
- 連結：https://www.theverge.com/gadgets/1013375/muse-charm-gadgets-preview-waveshare-esp32-claude-vibe-code

#AI #Meta #Anthropic #ClaudeCode #VibeCoding #ESP32 #Wearables #IoT #ConsumerTech #MuseAI
