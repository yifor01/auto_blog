---
title: 'SpaceXAI Releases Grok Voice Transcribe 2.0: A Speech-to-Text API Claiming
  2x Accuracy Over 1.0 at $0.10 per Hour'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/18/spacexai-releases-grok-voice-transcribe-2-0/
model: claude-code/sonnet
generated_at: '2026-09-20T19:40:18.664716'
score: 67
---

📌 Grok Voice Transcribe 2.0：電話語音辨識錯誤率砍半的新版 STT API

TL;DR：xAI 旗下 SpaceXAI 推出新版語音轉文字 API，宣稱準確度是舊版兩倍、價格不變，多語言短指令錯誤率降近七成。

噪音電話線、多人搶話、地方口音、唸出來的密碼，這些場景是所有語音辨識系統的惡夢。SpaceXAI 這次沒有推出新模型架構的論文，而是直接把舊產品線的痛點列成清單，交出一份對準這些「難搞音訊」的升級版 API。

🤔 **難處理的不是安靜錄音室，而是真實世界**

Grok Voice Transcribe 2.0 鎖定的正是工程團隊最常抱怨的場景：訊號差的電話、多人同時講話、非標準腔調，以及需要準確辨識的口述帳號密碼等關鍵字。這款模型以批次（batch）與即時串流（real-time streaming）兩種模式提供，透過 Speech to Text API 呼叫，模型 ID 為 `grok-voice-transcribe-2.0`，目前僅以託管 API 形式上線，SpaceXAI 並未釋出開源權重，因此無法自行部署。

🧩 **底層是撐起 Grok Voice 的音訊基礎模型**

2.0 版建立在支撐 Grok Voice 的音訊基礎模型之上。SpaceXAI 表示，Grok Voice 目前每天處理數萬通客服電話，也用於轉錄數百萬小時的影片旁白，並支援 Tesla 車內的 Grok 助理。訓練資料來自這些真實場景中收錄的即時、多語言、含噪音的語音，再經過後訓練（post-training）微調。

📊 **公開榜單第一，內部測試全面優於舊版**

在 Artificial Analysis 的 AA-WER Streaming 公開榜單上，SpaceXAI 表示 2.0 在 32 個串流模型中排名第一；該榜單使用約 8 小時音訊，權重配置為 AA-AgentTalk 佔 50%、VoxPopuli 佔 25%、Earnings22 佔 25%。另外，SpaceXAI 也用 4 組來自正式流量的內部資料集測量字錯誤率（WER），2.0 版在全部 4 組上都優於 1.0 版，其中電話語音（telephony）場景號稱領先所有受測模型——不過這部分屬於廠商自報數據，未經第三方獨立驗證。

多語言辨識被 SpaceXAI 稱為這次最大的進步：模型可自動偵測數十種語言，並在單次辨識中跟上錄音中途的語言切換。以車內短指令這類上下文極少的情境為例，WER 從 20.6% 降到 6.8%，等於減少約 67% 的錯字。文件也列出 25 種語言支援數字、貨幣、單位的書面格式化。批次端點支援單檔最大 500MB、12 種音訊格式；串流則支援 Opus 編碼，頻寬約每秒 4KB，相較 24kHz 原始 PCM 的每秒 48KB 明顯精簡。

價格與 1.0 版相同：批次轉錄每小時音訊 0.10 美元，串流每小時 0.20 美元，換算約每千分鐘 1.67 美元與 3.33 美元，且已內含語者分離（diarization）、時間戳記與關鍵字擷取。

💡 **Atlassian Loom 的實戰案例：從錄音到程式碼**

Atlassian 旗下 Loom 已採用 Grok Voice Transcribe 2.0 轉錄所有影片，並表示比原有方案更準確。SpaceXAI 描述的工作流程是「錄製、轉錄、寫碼」：使用者在 Loom 錄下行動計畫，轉錄文字直接餵給 Cursor 產生程式碼變更。Atlassian Teamwork Collection 資深副總裁 Sanchan Saxena 將這個流程形容為「把情境與程式碼之間的迴路接起來」。

⚠️ **廠商自報數據，且不開放自架**

目前所有效能數字都來自 SpaceXAI 官方公布，尚未見到第三方複現結果；由於未開源權重，企業若要導入只能透過託管 API，無法做私有化部署或客製化微調。

🎯 **實務啟示**

如果你的產品線本來就有電話客服、影片轉錄或車載語音等場景，這次升級的多語言與電話語音改善值得實測評估；而「錄音轉逐字稿→丟給 Coding Agent」這種將語音輸入直接接入開發流程的模式，也提供了一個把非結構化語音資料快速轉為可執行任務的參考架構。

🔗 **來源**
- 標題：SpaceXAI Releases Grok Voice Transcribe 2.0: A Speech-to-Text API Claiming 2x Accuracy Over 1.0 at $0.10 per Hour
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/18/spacexai-releases-grok-voice-transcribe-2-0/

#SpeechToText #GrokVoice #xAI #ASR #VoiceAI #API #Multilingual #AIProduct #SpeechRecognition #DeveloperTools
