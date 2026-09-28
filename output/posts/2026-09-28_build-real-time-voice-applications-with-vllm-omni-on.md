---
title: Build real-time voice applications with vLLM-Omni on SageMaker AI – Part 1
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-real-time-voice-applications-with-vllm-omni-on-sagemaker-ai-part-1/
model: claude-code/sonnet
generated_at: '2026-09-28T22:44:54.541346'
score: 89
---

📌 讓 TTS 模型邊生成邊講話：用 vLLM-Omni 在 SageMaker 上部署即時語音

TL;DR：AWS 示範用 vLLM-Omni DLC 在 SageMaker AI 部署 Qwen3-TTS，讓文字轉語音在生成完成前就能開始播放。

語音助理、無障礙工具、客服系統最怕的就是「使用者講完話後陷入長時間沉默」。這篇 AWS 教學示範了怎麼透過一條持續開啟的雙向連線，把文字串流進模型、把語音串流出來，讓聲音在模型還沒把整句話生成完之前就開始播放。

🤔 **文字生成模型的框架，不夠用在語音上**

這是一篇部署教學而非論文，聚焦的問題是：一般的文字生成 serving 框架難以直接處理語音、影像這類多階段、多模態的生成流程。vLLM-Omni 專案把 vLLM 從純文字生成擴展到能處理或生成文字、音訊、影像與影片的模型，內建異質 pipeline 抽象層，可以協調包含 autoregressive 與 diffusion 階段的多階段模型工作流程，並提供串流輸出與 OpenAI 相容 API。AWS 則把追蹤中的 vLLM-Omni 版本打包進 AWS 映像檔，做成 vLLM-Omni DLC（Deep Learning Container），額外加上給 SageMaker AI 用的路由 middleware。這篇文章是系列文的第一篇，聚焦即時語音串流；第二篇會把同一個 DLC 家族用在影像與影片生成上。

🧩 **雙向串流的資料流怎麼走**

SageMaker 的雙向串流透過 HTTP/2 傳輸的全雙工 WebSocket 實現：客戶端連到 SageMaker Runtime endpoint 的 8443 埠，SageMaker 的 inference sidecar 再把連線轉發到容器內 vLLM-Omni 原生的 WebSocket 路由。範例使用的是 vLLM-Omni 暴露出的原生路由之一 `v1/audio/speech/stream`。客戶端傳送 session 設定與文字事件，Qwen3-TTS 則透過同一條連線回傳音訊生命週期事件與 24 kHz PCM 音訊區塊。

這篇教學可以視為前一篇文章（把麥克風音訊串流進 Voxtral-Mini-4B Realtime STT 模型做語音辨識）的輸出端補完：前一篇處理「語音進、文字出」，這一篇處理「文字進、語音出」，兩者組合起來就是一條完整的語音對話管線，只是兩個 endpoint 之間的對話邏輯編排不在這篇範疇內。

部署時，endpoint 設定使用了 SageMaker instance pool：為同一個 production variant 定義一份依優先順序排列的相容機型清單，範例中依序是 ml.g6.xlarge、ml.g6e.xlarge、ml.g5.xlarge、ml.g4dn.xlarge。SageMaker 只會實際佈署其中一臺，而不是每個機型都各開一臺，但建立 endpoint 時會驗證清單中每一個機型的配額，因此需要為列出的所有機型都準備好額度；同時要注意的是，若 SageMaker 選用了不同機型，實際的時薪成本也會跟著變動,可以用 `--instance-types` 把 pool 限縮在符合配額、價格與效能需求的機型上。

📊 **怎麼跑起來**

完整範例放在 repo 的 `03-features/bidirectional-streaming-vLLM-Omni` 路徑下，clone 後即可拿到部署腳本、共用的串流傳輸層與 Gradio 客戶端。教學以美國東部（維吉尼亞北部）區域示範，DLC 映像檔 URI 與 runtime endpoint 都由 `AWS_REGION` 建構；呼叫模型的路徑要省略開頭的斜線，因為 SageMaker 會在轉發前自動補上。等 endpoint 狀態變成 `InService`（第一次部署會因為要下載 DLC 映像檔與模型檔案而花較長時間）後，打開 `http://127.0.0.1:6006` 就能透過 Gradio 介面測試，Gradio 的音訊元件會即時播放收到的每個 24 kHz PCM 區塊,狀態欄位則會顯示已接收的區塊數與音訊總位元組數（`--share` 選項會建立公開連結，非必要建議保持關閉）。測試完成後務必確認清理指令有回報 endpoint、endpoint 設定與模型都已刪除，因為正在運行的 GPU endpoint 會持續計費。

🎯 **實務啟示**

如果你正在打造需要低延遲語音回應的應用（語音助理、互動式教學、客服機器人），這個範例提供了一條相對現成的路徑：不需要自己處理 streaming 架構、WebSocket 轉發與多模態模型的 serving 細節，直接沿用 AWS 提供的 DLC 與範例程式碼,搭配前一篇 STT 範例，就能拼出一條「聽 → 想 → 說」的即時語音管線雛形。

🔗 **來源**
- 標題：Build real-time voice applications with vLLM-Omni on SageMaker AI – Part 1
- 作者／機構：Yadan Wei @ AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/build-real-time-voice-applications-with-vllm-omni-on-sagemaker-ai-part-1/

#AWS #SageMaker #vLLM #TextToSpeech #VoiceAI #Streaming #Qwen3 #MachineLearning #MLOps #RealTimeAI
