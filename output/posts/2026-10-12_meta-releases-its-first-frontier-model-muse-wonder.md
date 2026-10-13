---
title: Meta releases its first frontier model, Muse Wonder
source: TechCrunch AI
url: https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder/
model: claude-code/sonnet
generated_at: '2026-10-12T23:56:03.298426'
score: 91
---

📌 Meta 首個前沿模型登場：Muse Wonder 主打長期記憶而非只拚分數

TL;DR：Meta 發布首款前沿模型 Muse Wonder，效能看齊 Fable 5.1、GPT-6 Astra，強調跨時間記憶能力。

在 OpenAI、Anthropic 輪番推出旗艦模型的這段時間，Meta 一直缺席「前沿模型」這張考卷。這週一，Meta Superintelligence Lab 終於交卷，而交出的答案，重點不是跑分有多高，而是模型「記不記得你」。

🤔 背景：從輕量 Spark 到重量級 Wonder
Meta 先前推出的 Muse Spark 定位是低延遲的輕量模型；這次新發布的 Muse Wonder 與 Muse Wonder Full 則是體量更大、能力更強的版本，在複雜任務（例如 coding）上表現更好。依 Meta 在模型卡中揭露的測試結果，基準分數可與 Fable 5.1、GPT-6 Astra 相提並論。Meta 官方部落格寫道，這兩款模型「標誌著我們在 scaling ladder 上的下一步，也是邁向個人超級智慧的重大一步」。

🧩 兩個版本，不同管道
Wonder 透過 Meta Model API 提供，每百萬 input token 收費 4 美元、output token 20 美元，與 GPT-6 Sol 或 Opus 5.5 的費率大致相當。Wonder Full 則僅開放給 Muse Code 訂閱戶使用，不會透過 API 對外提供。兩款模型同時也會用來驅動 Muse 這個 agent 產品。

💡 重點不是跑分，是「active memory」
Meta 這次特別強調模型保留、整合使用者長期提供資訊的能力，稱之為「active memory」。為了驗證這項能力，Meta 引用了挑戰持續學習（continual learning）與記憶建構框架的 MemoryBench 基準，並宣稱 Muse Wonder 在這項基準上的分數高於 Fable、Opus、Astra。研究科學家 Kavya Kopparapu 在發布影片中表示：「我們投入了大量心力，確保你的模型能在數天、數週、數月甚至更久的時間裡，記住對你重要的事。」

⚠️ 時間點值得留意
這是 Scale AI 創辦人 Alexandr Wang 去年 8 月重整 Meta AI 團隊以來，Meta 首次推出前沿等級模型。在此之前，Meta 只發布過輕量的 Muse Spark 與 Muse agent，並未像 OpenAI、Anthropic 那樣頻繁推出旗艦級模型。這次訓練地點是今年初剛啟用、位於美國俄亥俄州中部的 Meta Prometheus 資料中心。

🎯 實務啟示
對於需要長期維運個人化助理或對話系統的工程團隊而言，Muse Wonder 強調的「active memory」與 MemoryBench 這類評測，提示了一個值得關注的方向：模型能力的比較不該只看單次回答的跑分，也要看它跨會話、跨時間保留與調用資訊的穩定性。若你的產品線也需要長期記憶能力，MemoryBench 的設計思路值得留意。

🔗 來源
- 標題：Meta releases its first frontier model, Muse Wonder
- 作者／機構：Russell Brandom／TechCrunch AI
- 連結：https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder/

#Meta #MuseWonder #LLM #AIAgent #FrontierModel #AIMemory #GenerativeAI #MachineLearning #AIResearch #SuperintelligenceLab
