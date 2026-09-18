---
title: Qwen3.8-LiveTranslate：知其人，傳其義
source: Qwen
url: https://qwen.ai/blog?id=qwen3.8-livetranslate
model: claude-code/sonnet
generated_at: '2026-09-18T19:42:26.958546'
pinned: true
---

📌 Qwen3.8-LiveTranslate：即時同傳延遲砍到2.3秒

TL;DR：Qwen3.8-LiveTranslate改用Interleave架構做同步口譯，延遲更低，還能分辨誰在說話。

同步口譯最怕兩件事：講者臨時交替發言、術語脫離上下文被譯錯。Qwen最新的即時同傳模型想同時處理這兩個問題，而且延遲比前代更快。

🤔 **同傳不只求快，還要保留「誰在說話」的資訊**

即時同傳追求的不只是翻得快，更要聽得清、譯得準。文中指出，團隊希望同傳不只傳遞語言本身，也能保留交流中人物與上下文資訊，因此在支援60種語言的基礎上，Qwen3.8-LiveTranslate新增了三項能力：即時說話人分離、原文譯文同幀同出，以及長上下文消歧。

🧩 **Interleave架構＋Thinker-Talker雙模組**

本代模型把同傳重構為「音訊-文字交織」的單一資料流，已聽的音訊與已產出的譯文都能快取複用，字均延遲（LAAL）從上一代的2.8秒降至2.3秒。架構上，Qwen3.8-LiveTranslate採用基於Hybrid MoE（混合專家）的Thinker–Talker雙模組設計，以Interleave方式串接串流理解、文字輸出與語音生成：Thinker把影片、音訊、原文與譯文依時序交替編排進同一條因果序列，端到端輸出，讓理解與翻譯在單一序列內完成；Talker則結合譯文與原始音訊，把譯文合成為保留原說話人音色的語音。

在多人交替發言的場景中，模型會區分不同說話人與各自的發言內容，讓譯文語音更穩定地保留原說話人的音色；原文與譯文同步呈現、雙語對齊，兼顧即時理解與原文核對，也為後續字幕、內容整理與檢索功能打底；長上下文消歧則結合前文與歷史語境，緩解專有名詞、代名詞在複雜場景下的歧義。

📊 **多說話人與多語言評測雙雙勝出**

在涵蓋14個語向的多說話人長音訊評測集Omnilingua-MSpeaker上，Qwen3.8-LiveTranslate在翻譯的忠實度、流暢度、簡潔度，以及說話人分離錯誤率（DER，Diarization Error Rate）四個維度上，都優於目前業界主流的即時同傳系統。在公開的FLEURS音訊測試集上，團隊評測了70個語向的即時同傳表現，Qwen3.8-LiveTranslate在翻譯品質、字均延遲、語音辨識準確率與語音合成品質四個維度，均領先上一代與當前主流即時同傳系統。支援語種方面，輸入音訊與輸出文字涵蓋60種語言，輸出語音則支援29種語言。

💡 **用API串起麥克風到喇叭的完整同傳鏈路**

文中提供了透過DashScope API呼叫的完整即時同傳客戶端範例：擷取麥克風音訊、以WebSocket串流傳送至服務端，再接收並播放譯文語音。新增的說話人分離與原文譯文同步輸出能力，都是透過會話設定（session.update）開啟；服務端在回傳譯文的同時，也會一併給出說話人標識與來源語言原文，不需要額外呼叫ASR介面。session設定中還能注入熱詞語料（corpus.phrases），針對專有名詞與行業術語提升辨識與翻譯準確率，這對需要處理大量專業術語的會議、法律、醫療口譯場景會是實用細節。

⚠️ **公開資訊未涵蓋的部分**

文中並未提供各語向品質是否均衡、模型參數規模或部署硬體需求等細節，實際導入前仍需針對目標語向與場景自行驗證。

🎯 **系統設計上的參考價值**

對開發即時語音應用的工程師來說，Interleave架構把「聽」與「譯」放進同一條因果序列處理，是值得參考的系統設計方向；而透過session配置就能切換文字/語音輸出模式、開啟說話人分離與熱詞注入，也代表這類API的整合成本相對低，適合直接串接到會議轉譯、直播字幕等場景中快速驗證。

🔗 **來源**
- 標題：Qwen3.8-LiveTranslate：知其人，傳其義
- 作者／機構：Alibaba
- 連結：https://qwen.ai/blog?id=qwen3.8-livetranslate

#Qwen #LiveTranslation #SpeechAI #MoE #RealTimeTranslation #SpeechRecognition #MultilingualAI #Alibaba #VoiceCloning #AIInterpretation
