---
title: 🗞️Apple AI Taps Qwen, Tencent’s Hy4, and China’s AI Chip Squeeze
source: Recode China AI
url: https://www.recodechinaai.com/p/apple-ai-taps-qwen-tencents-hy4-and
model: claude-code/sonnet
generated_at: '2026-11-08T21:20:59.495360'
score: 63
---

📌 蘋果中國版 Siri 偷測 Qwen，晶片卻兩頭卡關

TL;DR：蘋果開始在中國測試將 Qwen 整合進 Apple Intelligence，同週中國 AI 公司卻在海外租 GPU、買晶片上同時碰壁。

當蘋果忙著把阿里巴巴的 Qwen 塞進 iPhone 的日常操作時，中國的 AI 公司卻連租一批 GPU 都處處受阻。這一週的中國 AI 動態，剛好把「模型能力追上」與「算力拿不到」這兩條故事線同時擺上桌。

🧩 **蘋果開發者測試 Qwen，12 月隨 iOS 27.3 上線**

根據 SCMP 與雷峰網報導，蘋果本週開放開發者測試，計畫搭配 iOS 27.3 於 12 月正式推出。Qwen 會出現在 Siri、Writing Tools 與 Visual Intelligence 之中，使用者可以直接針對一張照片或一份文件提問，不必跳出到另一個聊天機器人 App。這項整合是選擇性開啟（opt-in），使用者可自行決定要把什麼內容送給 Qwen 處理。對阿里巴巴來說，重點不只是模型本身夠不夠強，而是「分發」——即使使用者從未打開 Qwen 的 App，它也已經嵌入日常的 iPhone 工作流程中。

🧩 **騰訊 Hy4 補上視覺與電腦操作，WorkBuddy 當試驗場**

11 月 4 日，騰訊為旗艦模型 Hy4 新增視覺推理與電腦操作（computer use）能力。中國媒體愛範兒的實測中，給 WorkBuddy 一段遊戲錄影，Hy4 便依此建出一個可玩的瀏覽器原型——使用者等於是「秀給 agent 看想要什麼」，而不是純靠文字描述。騰訊也坦承，在部分困難的研究與程式任務上，仍與頂尖的專有系統有差距。這次先開放託管存取，完整權重與系統卡（system card）之後才會公布。

📊 **晶片兩頭卡關：租不到海外 GPU，買不到晶片**

《金融時報》報導，Oracle 因美方官員的擔憂，撤回一筆估計 70 億美元、五年期的交易，原本要讓騰訊在東南亞取得多達 10 萬張 AI 晶片的使用權。CNBC 則報導月之暗面（Moonshot）曾探詢在歐洲租用 Nvidia Blackwell 算力，但這些談判尚未形成簽約租約。彭博則引述消息指出，中國買家在未來四個月、約 700 億美元的 RTX 訂單中，預期只能分到約 1% 的份額。這些數字拼起來,勾勒出一個清楚的現況：模型端的能力正在快速逼近，但算力供應鏈上的瓶頸,不會因為模型做得好就自動解決。

💡 **一週模型放權重：百度、月之暗面、螞蟻、美團同臺**

- 百度發布 ERNIE 5.5 Flash Base，是一個混合專家（MoE）模型，總參數 2800 億、每個 token 啟用 140 億，官方稱微調與推理階段最長可支援百萬 token 的上下文，屬於開發者可自行二次訓練的基礎檢查點。
- 月之暗面本週在 Hugging Face 公開 Kimi K3.1 Pro 的權重，讓開發者有了自架（self-hosting）的選項，這個模型總參數達 2.8 兆。
- 螞蟻集團發布 Ling-3.2-flash，多模態模型，總參數 5600 億、啟用 250 億，官方宣稱的目標場景包括複雜視覺任務、3D 互動與醫療推理。
- 美團發布 LongCat-2.5，原生多模態模型，總參數 1.6 兆、啟用約 480 億,主打需要多步驟、且 agent 得邊做邊檢查視覺輸出的任務（例如程式開發）。

⚠️ **政策訊號仍在醞釀**

中國國家發改委 11 月 3 日表示將加快推進綜合性 AI 立法，並制定涵蓋技術全生命週期的安全標準與倫理規範——這只是立法優先順序的訊號，中國目前尚未有統一的全國性 AI 法。另外六部門則發布鼓勵在養老場景使用具身智能、語言模型、腦機介面與外骨骼的措施，重點在於開發適老化產品與服務，並不代表任何特定設備已獲臨床效果認證或許可。

🎯 **實務啟示**

對工程團隊而言，這週的訊號是：模型能力的追趕速度,比算力取得的速度快得多。如果你的產品規劃依賴海外雲端 GPU 租賃或特定晶片供應,中國案例提醒了「簽約」與「談判中」之間的巨大落差,評估時機時務必區分清楚。而 Qwen 走進 Siri,也再次證明在 LLM 賽局裡,被整合進既有的日常入口,往往比單獨的 App 下載量更有價值。

🔗 **來源**
- 標題：🗞️Apple AI Taps Qwen, Tencent's Hy4, and China's AI Chip Squeeze
- 作者／機構：Tony Peng，Recode China AI
- 連結：https://www.recodechinaai.com/p/apple-ai-taps-qwen-tencents-hy4-and

#AppleIntelligence #Qwen #TencentHy4 #ChinaAI #GPUShortage #MoE #Ernie #KimiK3 #AIAgent #ChipSupplyChain
