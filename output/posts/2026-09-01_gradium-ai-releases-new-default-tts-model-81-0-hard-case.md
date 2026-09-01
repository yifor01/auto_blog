---
title: 'Gradium AI Releases New Default TTS Model: 81.0% Hard-Case Pass Rate at 216
  ms Time-to-First-Audio'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/31/gradium-ai-releases-new-default-tts-model-81-0-hard-case-pass-rate-at-216-ms-time-to-first-audio/
model: claude-code/sonnet
generated_at: '2026-09-01T10:47:43.551838'
score: 86
---

📌 Gradium 新版 TTS：唸對訂單號比什麼都重要

TL;DR：Gradium 新 TTS 模型硬案例通過率達 81.0%，首字延遲 216ms，即日起直接成為預設模型。

語音 agent 最容易出錯的，往往是通話裡最關鍵的部分：訂單編號、要回撥的電話號碼、對方得抄下來的 email 地址。

🤔 **硬案例才是語音 agent 的真正考驗**

Gradium AI 發表新的 text-to-speech 模型，並在 2026 年 8 月 31 日起將其設為 API 與 Studio 的預設模型，既有的語音（包含自訂複製語音）不需任何遷移即可直接沿用。這次評測聚焦在語音 agent 最容易失敗的場景：唸出拼字、縮寫、英數混合代碼、日期、一般數字、大數字與浮點數，以及 email 地址。

🧩 **500 句、五種語言、十項判準的硬案例評測集**

Gradium 建立了一份 500 句的評測集，並以 CC BY 4.0 授權在 Hugging Face 上開源，內容涵蓋英、德、法、西、葡五種語言，每種語言 100 句、十項判準。其中七項是原子判準（拼字、縮寫、英數 token、日期、一般數字、大數字與浮點數、email），另外三項是複合判準（Orders、IT Ticket、Claims），把多個原子情境疊加成一次真實的 agent 對話輪次。評分方式是由母語者獨立聆聽評分，標準嚴格：只要漏掉一個數字，整句就算不通過。音檔經過響度正規化、播放順序隨機化，評分者每人上限 40 次比較並強制休息。

📊 **通過率與延遲雙雙領先**

在十項判準、五種語言等權重平均下，各模型的硬案例通過率為：

| 模型 | 硬案例通過率 |
|---|---|
| Gradium TTS | 81.0% |
| Cartesia Sonic 3.6 | 75.1% |
| ElevenLabs v3 Conversational | 65.4% |
| Fish Audio S2.1 Pro | 49.5% |
| Inworld TTS 1.5 Max | 46.5% |

所有結果皆於 2026 年 8 月以各模型預設設定產出。在 Coval 的 TTS 基準測試中，Gradium 的首字延遲（time to first audio）為 216ms（P50），比它取代的前一代模型快了 170ms；480 次測試中的 p75–p25 四分位距僅 30ms，是五個模型中最小的。相較之下，Cartesia Sonic 3.6 中位數為 454ms、間距達 165ms（約佔中位數 36%）；Inworld TTS 2 中位數 166ms 是這批模型中最快的；Fish Audio S2.1 Pro 為 291ms，ElevenLabs v3 Conversational 為 329ms。

💡 **不是最快，但失敗率最低且延遲穩定**

文章指出，Gradium 並非這批模型中首字延遲最快的（Inworld TTS 2 更快），它真正的主張是「聯合定位」：在 250ms 以下的首字延遲區間裡，硬案例失敗率最低，且延遲波動幅度也最小。對於實際接聽電話的使用者而言，體驗到的往往是分佈的尾端而非中位數，這也是文章特別強調變異數的原因。

⚠️ **評測由廠商自行設計與發布**

這份評測集雖已開源供外界檢視，但評測設計、標準與執行仍是 Gradium 自行主導，素材中並未提及模型的架構細節。Gradium 也在 Discord 上提供 100 萬點數，徵求完整的硬案例失敗報告。

🎯 **實務啟示**

對於處理報訂單號、回撥電話、email 等需要精準口述資訊的語音 agent 應用，這份開源的硬案例評測集本身就值得拿來檢驗自己現有的 TTS 選型，而不只是看廠商公布的單一分數。

🔗 **來源**
- 標題：Gradium AI Releases New Default TTS Model: 81.0% Hard-Case Pass Rate at 216 ms Time-to-First-Audio
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/31/gradium-ai-releases-new-default-tts-model-81-0-hard-case-pass-rate-at-216-ms-time-to-first-audio/

#Gradium #TTS #TextToSpeech #VoiceAgent #ConversationalAI #SpeechSynthesis #Latency #AIProduct #VoiceAI #Benchmark
