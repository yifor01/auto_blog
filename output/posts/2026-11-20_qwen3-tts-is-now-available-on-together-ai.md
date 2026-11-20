---
title: Qwen3 TTS is now available on Together AI
source: Together AI
url: https://www.together.ai/blog/qwen3-tts
model: claude-code/sonnet
generated_at: '2026-11-20T23:25:57.136844'
score: 69
---

📌 Qwen3 TTS 上架 Together AI：97 毫秒出聲的開源語音模型

TL;DR：Qwen 的開源 TTS 模型現可在 Together AI 用 Serverless Inference 或專屬端點呼叫，支援低延遲串流，適合打造語音 agent。

同一句「這下情況不一樣了」，用興奮的語氣念，跟用失望的語氣念,聽在使用者耳裡是完全不同的兩件事。Qwen3 TTS 讓你只靠一句自然語言描述就能決定要哪一種。

🧩 **把「是誰說話」跟「怎麼說」拆開**

Qwen3 TTS 是 Qwen 的開源 text-to-speech 模型，設計上把聲音身分（speaker identity）跟表達方式（delivery）分開處理。你先選定九個預設語音中的一個，這個聲音本身不變，但可以用像「excited and upbeat」這種自然語言指令去調整語氣,也可以切換到不同語言。九個預設語音及其母語與特色：

| 語音 | 母語 | 特色描述 |
|---|---|---|
| aiden | 英語 | 清亮中音的陽光系美式男聲 |
| ryan | 英語 | 節奏感強烈的動感男聲 |
| vivian | 中文 | 明亮帶點個性的年輕女聲 |
| serena | 中文 | 溫暖溫柔的年輕女聲 |
| uncle_fu | 中文 | 低沉醇厚的成熟男聲 |
| dylan | 中文（北京話） | 清亮自然的北京青年男聲 |
| eric | 中文（四川話） | 略帶沙啞明亮的成都活潑男聲 |
| ono_anna | 日語 | 輕快靈巧的日系少女聲 |
| sohee | 韓語 | 情感豐富的溫暖韓語女聲 |

每個語音都能說中、英、日、韓、德、法、俄、葡、西、義共 10 種語言，讓同一個產品切換市場時能維持相同的聲音身分不變。Qwen 官方建議在語音對應的母語下使用，品質最佳，所以切換語言前最好先聽聽實際效果再決定要不要用。

🧩 **怎麼接進來**

最快選語音的方式是用 VoiceFinder（voicefinder.together.ai）：選擇 `Qwen/Qwen3-TTS-12Hz-1.7B` 模型、輸入自己的文字（最多 500 字元），就能試聽各語音唸出同一段文字，並直接取得 Python、TypeScript 或 cURL 的呼叫程式碼。實際呼叫則透過 Together Python SDK（`pip install together`），用 `client.audio.speech.create` 帶入 `model`、`voice`、`language`，以及透過 `extra_body` 傳入 `instructions` 參數描述語氣。要注意 `instructions` 欄位名稱拼錯不會報錯，只會被靜默忽略，是個容易忽略的 debug 陷阱。可用的 `response_format` 是 `wav`、`mp3`、`raw`、`mulaw`，不支援 `opus`、`aac`、`flac`；`sample_rate` 預設 24000，也可設為 8000；不支援詞層級的時間戳記（`alignment=word`）。

🧩 **做語音 agent 要的即時串流**

Together AI 官方提到首個音訊片段最快 97 毫秒內可以送出，並提供兩種串流方式，依文字是否已完整決定：已有完整文字時，用 `stream=True` 搭配 `response_format="raw"`，透過 HTTP 的 server-sent events 接收，每個 `conversation.item.audio_output.delta` 事件帶一段 base64 編碼的 16-bit PCM 音訊；若文字是逐 token 從語言模型產生出來的，則用 WebSocket API，邊產生文字邊 append，等到一句話的文字完整後 commit，伺服器會在收到完整句子後才合成，適合串接即時對話場景。

⚠️ **限制**

素材中僅提及 `Qwen/Qwen3-TTS-12Hz-1.7B` 這一個模型版本，不支援詞層級時間戳記，音訊格式也侵限於 wav/mp3/raw/mulaw。價格為每百萬字元 20 美元，Serverless Inference 與專屬端點皆採此計價。

🎯 **實務啟示**

如果你在做多語言客服語音或語音 agent，Qwen3 TTS 的「聲音身分跟語氣分離」設計,讓產品不用為每種情緒或每個市場重新訓練或換模型，用一句指令跟一個語言碼就能切換。串流 API 的兩種模式也剛好對應兩種常見架構：事先有完整文字稿的批次合成,或是接在 LLM 輸出後面的即時語音對話。

🔗 **來源**
- 標題：Qwen3 TTS is now available on Together AI
- 作者／機構：Together AI
- 連結：https://www.together.ai/blog/qwen3-tts

#Qwen3 #TTS #TogetherAI #VoiceAI #TextToSpeech #OpenSourceAI #SpeechSynthesis #VoiceAgent #RealTimeAI #MultilingualAI
