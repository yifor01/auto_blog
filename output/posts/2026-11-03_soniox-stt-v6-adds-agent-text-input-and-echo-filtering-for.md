---
title: Soniox STT v6 Adds Agent Text Input and Echo Filtering for Voice Agents
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/03/soniox-stt-v6-agent-text-input-echo-cancellation/
model: claude-code/sonnet
generated_at: '2026-11-03T22:40:15.844742'
score: 78
---

📌 Soniox STT v6:讓語音辨識「聽懂」Agent 自己在說什麼

TL;DR：Soniox STT v6 讓語音辨識模型同步讀取 agent 的文字,藉此修正短答辨識錯誤並過濾回音。

在語音客服的對話記錄裡,「River Roast」被辨識成「River Road」,「a tow」變成「a tour」——問題不在於使用者說得不清楚,而是辨識模型根本沒看到前面那句問題。Soniox STT v6 想解決的,正是這個被忽略已久的盲點。

🤔 **Cascaded 架構的語音 agent,聽不到自己問了什麼**

在 cascaded(串接式)語音 agent 架構裡,STT 模組通常只聽得到來電者的聲音,完全看不到 agent 自己問了什麼問題。這對短回答的辨識特別不利,因為少了問題的上下文,模型只能憑聲音本身猜測。第二個問題是回音:agent 的語音會透過喇叫電話或筆電漏音回傳,被誤判成使用者的語音,導致 agent 打斷自己說話。

🧩 **一個 flag、一條 WebSocket,把 Agent 的文字餵給辨識模型**

v6 以 `stt-rt-v6`(streaming)與 `stt-async-v6`(檔案)兩種形式發行,支援 60 多種語言。要啟用這個新能力,在 start request 中加入 `"enable_agent_text_input": true` 即可,但目前僅限 `stt-rt-v6`,async 版本不支援。

實際用法是:agent 說話的同時,把它的文字以小型 JSON frame 的形式,透過同一條 WebSocket 與使用者的音訊一起串流送出,格式像這樣:

```
{"type": "agent_text", "text": "...", "end_of_segment": true}
```

時機的掌握很關鍵——這些訊息本身不帶時間戳,模型是依照訊息抵達音訊串流的時間點來定位文字的。Soniox 建議每段文字要在播放前 500 毫秒到 1 秒送出,並依照 TTS 的時間戳來抓節奏。若發生 barge-in(使用者打斷),則要把已播放的部分 flush 掉、送出 `end_of_segment: true`,並捨棄尚未播放的剩餘內容。agent 的文字本身不會出現在最終回傳的逐字稿裡。

開啟 agent text input 後,v6 會利用這份文字,把殘留的 agent 音訊從使用者語音中分離並過濾掉,同時在播放期間持續監聽,讓使用者仍能隨時打斷。Soniox 特別強調,這不是取代聲學回音消除(acoustic echo cancellation,AEC),而是處理「既有 AEC 處理不掉的殘留部分」,所以 AEC 仍應保持開啟。

⚠️ **升級前要注意的格式變化,以及尚未公開的 v6 數字**

升級前有一個格式上的差異需要測試:v6 會把金額寫成「15 dollars and 20 cents」這種唸法,而不是「$15.20」;代碼中的連字號也只有在真的被唸出來時才會出現。

Soniox 目前尚未公開 v6 的準確率或延遲數字,其 benchmark 頁面仍停留在 v5 的資料。在開源的 Pipecat STT benchmark(1,000 筆真實樣本,measure semantic WER 與 time to final segment)上,`stt-rt-v5` 的 semantic WER 為 1.34%,完整正確逐字稿比例 83.3%,中位數 TTFS 為 260 毫秒,P95 延遲 305 毫秒;作為對照,Azure 的平均 WER 最低(1.21%),但中位數延遲高達 1,016 毫秒。這些數字都是 v5 的結果,v6 本身尚未經過這套 benchmark 測試。

💡 **「第一個聽懂 agent 說話的模型」這個說法需要加個註解**

Soniox 稱 v6 是「第一個知道你的語音 agent 在說什麼」的模型,但這個說法需要加上限定條件:AssemblyAI 在今年 7 月發布的 Universal-3.5 Pro Realtime 中,已經把 agent 的回覆餵進串流 STT。兩者真正的差異在於回音處理——Soniox 的文件描述了用這份文字過濾殘留 agent 音訊的機制,而 AssemblyAI 的 context 文件並未描述類似的過濾功能。

v6 可直接替換 v5 使用,只需把模型名稱換成 `stt-rt-v6` 或 `stt-async-v6`。v5 已進入淘汰流程,將於 2026 年 12 月 15 日移除,之後所有 v5 請求都會自動導向 v6。計價採 token 制:streaming 約每小時 0.12 美元,async 約每小時 0.10 美元,agent text 則依輸入文字 token 計費,real-time 每百萬 token 4.00 美元。

🎯 **實務啟示**

對正在建置 cascaded 語音 agent 的團隊,這是個可以直接測試的低成本切換(改模型名稱即可),但升級前務必驗證金額、代碼等格式變化是否影響下游解析邏輯,並留意 v6 準確率/延遲數字尚未公開,仍需自行在自家場景做基準測試。

🔗 **來源**
- 標題：Soniox STT v6 Adds Agent Text Input and Echo Filtering for Voice Agents
- 作者／機構：Michal Sutter(MarkTechPost)
- 連結：https://www.marktechpost.com/2026/11/03/soniox-stt-v6-agent-text-input-echo-cancellation/

#VoiceAI #SpeechToText #STT #VoiceAgent #Soniox #EchoCancellation #ConversationalAI #RealtimeAudio #API #NLP
