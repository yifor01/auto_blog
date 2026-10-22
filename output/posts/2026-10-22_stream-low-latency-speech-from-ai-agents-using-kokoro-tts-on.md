---
title: Stream low-latency speech from AI agents using Kokoro TTS on Amazon SageMaker
  AI
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/stream-low-latency-speech-from-ai-agents-using-kokoro-tts-on-amazon-sagemaker-ai/
model: claude-code/sonnet
generated_at: '2026-10-22T20:56:53.768015'
score: 87
---

📌 語音代理人少等 5 秒：逐句串流接上 Kokoro-82M TTS

TL;DR：AWS 示範如何讓 TTS 合成跟著 agent 逐句生成同步進行，而不是等完整回覆跑完才開始唸。

🎣 使用者問了語音 agent 一個問題，agent 其實已經在生成答案了，一句話可能只要 600 毫秒就生成完畢，但完整的多段落回覆卻要 5 秒。如果整合方式是等全部文字生成完才送進語音合成，使用者這 5 秒就只能聽到沉默，然後失去耐心、注意力飄走。

🤔 問題出在「等完整回覆」這個假設

這篇 AWS 部落格要解決的，正是文字轉語音（TTS）整合裡常見的這個延遲缺口：agent 產生文字的速度和使用者聽到聲音的時間點，中間隔著「等全部生成完」這一步。解法是讓 Kokoro-82M 這個僅 82M 參數、足以在單張中階 GPU 上便宜運行的 TTS 模型，在 agent 每生成一句話時就立刻開始合成那一句的語音，不等整段回覆結束。

🧩 架構：SageMaker 即時端點 + 雙向 WebSocket + 句子緩衝器

Kokoro-82M 跑在 Amazon SageMaker AI 的即時端點（real-time endpoint）上，使用 ml.g5.xlarge GPU 實例的自訂容器。容器對外開兩個路由：一個是 POST /invocations，針對單筆完整輸入做串流回應；另一個是 WS /invocations-bidirectional-stream，維持一條連線，雙向持續收送多則訊息。

整套部署分兩個 CLI 工具、各自包著自己的 AWS CDK stack：speech-infra deploy 負責把 Kokoro-82M 端點架起來，包含建立 IAM 角色、把模型權重同步進 Amazon S3 的基礎與模型快取 stack，再建構容器映像檔並建立 SageMaker AI 的 model、端點設定與端點本身；agent-infra deploy 則部署承載 Strands agent 的 Amazon Bedrock AgentCore runtime，這個 agent 會呼叫前面架好的端點，因此端點要先部署。

實作上有個容易踩的坑：SageMaker AI 的雙向傳輸會把客戶端送出的每段訊息都包成二進位的 WebSocket frame 送進容器。常見寫法是直接呼叫 Starlette 的 receive_text()，但這個方法讀取 message["text"]，一旦該欄位不存在就丟出 KeyError。因為這個客戶端送出的訊息全都是二進位，這種寫法每次都會失敗，而且常見的通用例外處理會把 str(e) 轉送給客戶端，結果 KeyError('text') 看起來像是「缺了某個欄位」，而不是「訊框格式不對」；端點自己回報的狀態卻一路顯示 InService，因為它確實接受了連線並對每則訊息都「回應」了，只是每次都回應一個錯誤。正確做法是同時明確處理兩種 frame 類型，沒有文字欄位時才把 bytes 當 UTF-8 解碼。

另一個反直覺的地方是：合成完一句的語音後，不該像 HTTP 一樣關閉連線。容器送出這句的音訊與一個 synthesis_complete 控制訊框後，應該回到 receive() 繼續等待同一條、仍開著的 session 上的下一則訊息，只有客戶端明確送出 {"type": "close"} 才關閉。這樣可以在同一條持久 session 上連續送好幾句話，句與句之間沒有重新連線的成本；若每句話都急著關閉連線，等於強迫每句都重新建立連線，抵銷大半的延遲優勢。

為了把「完整字串」和「逐 token 串流」這兩種輸入形式統一處理，client 端用一個類別正規化文字來源：呼叫 feed() 處理每個新到的文字片段，回傳任何剛完整的句子，並保留還沒結束的片段；在輸入結束時呼叫一次 flush()，釋出即使沒有結尾標點的殘餘文字，避免串流在句號出現前就結束而漏掉最後一句。

📊 三句話循序驗證通過

AWS 團隊針對一個真實運作中的端點，用同一條 session 送入三句話的輸入做驗證，三段音訊都和各自送出的文字內容對得上。不過要注意，這整套流程本質上是「嚴格依序」的循環：接收訊息、合成語音、送出語音、送出 synthesis_complete、再接收下一則訊息，並不是「第二句話的語音在第一句還在傳輸時就已經在生成」。逐句送出換來的延遲收益很明確但有限：只是讓第一句的合成在它一生成出來就立刻開始，不必等整段回覆跑完。對一個首尾生成時間差明顯的多句回覆來說，這就是全部的延遲改善來源。

💡 把音訊傳回瀏覽器：base64/SSE 的隱藏成本

文字串流只解決一半問題，另一半是把合成好的音訊送回前端渲染，通常是瀏覽器。多數 agent／聊天前端已經用 Server-Sent Events（SSE）串流文字，但 SSE 是單向文字協定，不是設計來承載原始二進位內容的。團隊若把語音加進既有 SSE 管線，很自然會想到把音訊 base64 編碼後包進 JSON 事件。AWS 團隊針對 24 段音訊片段實測了這個做法的成本，並用 Amazon Transcribe 確認編碼方式不影響辨識品質，同時比較了 MP3 與 AAC：base64 把每個 payload 膨脹了接近預期的 33%。更隱蔽的成本在於訊框對齊：SSE 事件以空行分隔，但音訊內容是以 MP3 frame 分隔，兩套切分方式未必對得上傳輸層實際切出來的資料塊，在一次實測的回應中，四個邏輯上的 MP3 frame，實際被傳輸層切成六個資料塊，其中兩個在 frame 中段被截斷。如果消費端把每個傳輸塊都當成一個完整單元處理，在正常健康的流量下就會出錯；正確做法是緩衝接收到的 bytes，等找到分隔符號才動作。

另一條路是在模型端這段完全跳過 base64 與 SSE 包裝，改用同一條已經在承載逐句文字輸入的雙向 session，把原始二進位音訊與 JSON 控制訊框多工（multiplex）在一起，用一條規則區分兩者：一個資料塊若無法解析成 JSON 物件，就當作音訊原樣轉送，過程中不需要任何編碼步驟。這裡有個邊界案例要處理：原始 PCM 音訊有可能恰好以 0x7b（也就是 ASCII 的「{」）開頭，和 JSON 物件的開頭字元一樣；但這條規則要求整個資料塊都必須能解析成合法 JSON，而不是只看第一個 byte，PCM 音訊幾乎不可能整塊剛好是合法 JSON，因此不會被誤判。

⚠️ 不是平行合成，收益也有上限

必須說清楚的是，這套做法並沒有讓多句話並行合成，它縮小的只是「等待」這段時間，而不是縫合出真正的並行流水線；如果回覆本身只有一句話，或句與句之間生成時間差很小，這個方案帶來的延遲改善也會跟著變小。

🎯 實務啟示

對正在把 LLM 回覆接上語音輸出的團隊，這篇提供了一個可直接複現的做法：用小模型（82M 參數級）降低推論成本，用雙向 WebSocket session 取代一問一答式的 HTTP 呼叫，用句子緩衝器對齊文字流與語音合成的呼叫時機。如果既有管線是 SSE + base64，這裡列出的「33% 膨脹 + frame 對齊」問題值得在導入語音前先評估是否要改走二進位多工。

🔗 來源
- 標題：Stream low-latency speech from AI agents using Kokoro TTS on Amazon SageMaker AI
- 作者／機構：Joseph Cottingham, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/stream-low-latency-speech-from-ai-agents-using-kokoro-tts-on-amazon-sagemaker-ai/

#TextToSpeech #Kokoro #AmazonSageMaker #VoiceAgent #LowLatency #AWS #AIAgent #WebSocket #StreamingAudio #Bedrock
