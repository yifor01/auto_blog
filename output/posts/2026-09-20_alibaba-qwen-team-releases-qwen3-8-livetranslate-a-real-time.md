---
title: 'Alibaba Qwen Team Releases Qwen3.8-LiveTranslate: A Real-Time Interpretation
  Model That Cuts Average Lag to 2.3 Seconds Across 60 Languages'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/19/alibaba-qwen-team-releases-qwen3-8-livetranslate/
model: claude-code/sonnet
generated_at: '2026-09-20T19:32:12.422635'
score: 101
---

📌 阿里 Qwen 團隊發布同步口譯模型，平均延遲砍到2.3秒

TL;DR：Qwen3.8-LiveTranslate 用新的 Interleave 架構邊聽邊譯，60種語言即時互通，已上線 API。

同步口譯向來是個矛盾的任務：等得越久，模型看到的上下文越完整；講得越快，聽者等待的時間越短。阿里 Qwen 團隊這次交出的答案，是把這個兩難重新設計了一次。

🤔 **同步口譯的老問題：等待與延遲的拔河**

Qwen 團隊發布 Qwen3.8-LiveTranslate，這是新一代即時同步口譯模型，能一邊聽取即時語音（可選搭配視訊畫面），一邊在說話者仍在講話時就同步輸出翻譯文字與語音。衡量這類系統的關鍵指標是 LAAL（Length-Adaptive Average Lagging），用來計算翻譯內容平均落後原始語音多少時間，同時避免系統靠「過度生成內容」灌水分數。

🧩 **核心是一套新的 Interleave 架構**

Qwen 團隊表示，此模型是 Qwen3.8-LiveTranslate-Flash 的即時版本，建構在 Qwen-Omni 技術堆疊、大規模多模態資料、跨語言與跨模態對齊，以及視覺增強能力之上。Flash 版本本身也支援離線的音訊與影片翻譯。

模型可理解60種語言，其中29種能以語音加文字形式輸出，其餘31種則僅輸出文字。支援語音輸出的語言包括中文、英文、阿拉伯文、德文、法文、西班牙文、日文、韓文、印地文等。輸入端接受音訊與可選的圖片，官方文件建議每秒最多傳送2張圖片；嘴型、手勢、螢幕上的文字等視覺線索，能在嘈雜環境或語意模糊時提供輔助判斷。此外系統支援「熱詞」設定，可將來源語言的特定詞彙對應到固定的目標翻譯，文件建議熱詞數量上限為1,000個。這代表模型並非單純的語音辨識加翻譯串接，而是把說話者分離（real-time speaker diarization）、雙語同步顯示、長上下文消歧義等能力整合進同一套推理流程。

📊 **延遲降1成8，但別忽略配額與價格**

Qwen 團隊報告 LAAL 從2.8秒降至2.3秒，約降低18%的平均延遲，同時提升忠實度、流暢度與簡潔度。開發者可透過 WebSocket Realtime API 串接，模型 ID 為 qwen3.8-livetranslate-flash-realtime，預設的分段判斷方式為 speaker_detection，音訊輸入預設為16kHz PCM、輸出為24kHz PCM，預設語音為 Tina。session.output_modalities 可設定為純文字或文字加語音，且務必在關閉連線前送出 session.finish，否則最後一段翻譯內容會遺失。

情境成本方面，音訊輸入每秒消耗7個 token，音訊輸出每秒消耗12.5個 token；一小時的語音輸入加輸出，在新加坡節點約需1.54美元（尚未計入文字與圖片 token）。文件也列出北京節點每百萬 token 的定價分別為5.653、0.466、14.133、22.613美元，較新加坡節點更低。上下文視窗為53,248個 token（輸入49,152、輸出4,096），預設速率限制為每分鐘10次請求、10萬個 token。

⚠️ **目前還不支援的功能**

Model Studio 文件明確列出目前不支援 function calling、structured outputs、batch inference 與 fine-tuning，這代表現階段它比較適合做即時口譯這類垂直場景，而非泛用的 agent 後端。

🎯 **實務啟示**

對於需要跨語言即時溝通的產品（視訊會議、直播字幕、客服系統）而言，這次更新是漸進式但可直接落地的改良：延遲降低、支援視覺線索與熱詞設定，都是實際部署時會在意的細節。若要整合，需留意 token 計費方式與速率限制，並確保正確處理 session 生命週期以避免漏字。

🔗 **來源**
- 標題：Alibaba Qwen Team Releases Qwen3.8-LiveTranslate: A Real-Time Interpretation Model That Cuts Average Lag to 2.3 Seconds Across 60 Languages
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/19/alibaba-qwen-team-releases-qwen3-8-livetranslate/

#Qwen #Alibaba #RealTimeTranslation #SimultaneousInterpretation #SpeechAI #MultimodalAI #WebSocketAPI #LLM #QwenOmni #AIProductRelease
