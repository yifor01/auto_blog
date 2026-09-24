---
title: Introducing Gemini 3.8 Live with Live Avatar
source: Google DeepMind
url: https://deepmind.google/blog/introducing-gemini-38-live-with-live-avatar/
model: claude-code/sonnet
generated_at: '2026-09-24T20:36:01.585726'
pinned: true
---

📌 【Google DeepMind】Gemini 3.8 Live 加上「即時化身」，讓 AI 客服有臉又會換語言

TL;DR：Gemini 3.8 Live with Live Avatar 把即時對話結合低延遲串流影片，讓企業級 AI 助理有了會說話、會表情的視覺化身。

上週 Gemini 3.8 Live 才剛上線，這週 Google DeepMind 就再加碼：讓這個對話模型「長出一張臉」。Live Avatar 不只是加個動畫貼圖，而是把即時語音對話與近乎即時的影片生成原生耦合在一起，讓 AI 客服或導覽助理第一次可以一邊聽、一邊看、一邊用動態表情跟你說話。

🤔 **對話本來就是多模態的**

Google DeepMind 團隊（由 Research Scientist Shuo-yiin Chang 與 Software Engineer CJ Zheng 代表 Gemini Audio Team 撰文）指出，人類對話天生就仰賴聽、看、說與表情的組合，而過去的 live dialogue 模型只處理了聲音這一層。Live Avatar 的目標，是把這個缺口補上：同步處理視覺與語音輸入，生成更完整的對話體驗，具備精確的嘴型同步（lip-sync）、自然表情與流暢的輪流對話（turn-taking）。這項功能目前已在 Gemini Enterprise 中提供，鎖定客服互動與互動式導覽等企業場景。

🧩 **背景執行工具呼叫，對話不中斷**

Live Avatar 背後仍是 Gemini 的推理能力，其中一個關鍵設計是非同步（asynchronous）的工具呼叫：化身可以在背景觸發工具呼叫、抓取資料，同時持續與使用者對話，不會因為要查資料而讓對話卡住。官方示範的案例是飯店入住報到流程——化身一邊處理複雜的後臺查詢，一邊維持對話不中斷。

🌏 **97 種語言即時切換，嘴型不跑掉**

Live Avatar 內建原生多語言的 speech-to-speech 同步能力，能動態調整嘴型同步與表情，在對話中途切換語言時，可橫跨 97 種語言而不損失影片畫質或出現視覺漂移（visual drift）。對於需要服務多國使用者的企業場景，這代表同一個化身不需要針對每個語系另外訓練或切換模型。

🎨 **可客製化的品牌化身**

除了官方提供的多樣化預設化身庫，企業也可以用一張高品質的參考圖片生成完全動畫化、可即時回應的專屬化身，同時保留參考圖的外觀、品牌風格或角色識別特徵。不過官方說明，客製化化身目前僅開放給企業白名單（allowlisting）使用者。

⚠️ **信任與透明：SynthID 浮水印**

考量到擬真的即時影片可能被濫用於身分冒用或不實資訊，Google DeepMind 表示 Live Avatar 所有輸出都嵌入了 SynthID 這種不可感知的浮水印，直接織入音訊與影片輸出中，協助讓 AI 生成內容保持可被偵測，降低誤導或誤歸屬的風險。完整的安全與負責任部署方法，官方也提供了對應的 model card 供查閱。

🎯 **實務啟示**

對於正在評估企業對話式 AI 的工程團隊，Live Avatar 提供的非同步工具呼叫與多語言即時切換，代表未來設計客服或導覽類 agent 時，可以把「查資料」與「維持對話」解耦成兩條並行邏輯，而不必犧牲互動的流暢度。目前功能已在 Gemini Enterprise 中提供，並有對應 API 文件可供開發者開始整合。

🔗 **來源**
- 標題：Introducing Gemini 3.8 Live with Live Avatar
- 作者／機構：Shuo-yiin Chang, CJ Zheng @ Google DeepMind (Gemini Audio Team)
- 連結：https://deepmind.google/blog/introducing-gemini-38-live-with-live-avatar/

#GoogleDeepMind #Gemini #LiveAvatar #ConversationalAI #MultimodalAI #EnterpriseAI #SynthID #RealTimeVideo #SpeechToSpeech #AIAssistant
