---
title: Deploying real-time personalized speech with Qwen3-TTS on Amazon SageMaker
  AI
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/deploying-real-time-personalized-speech-with-qwen3-tts-on-amazon-sagemaker-ai/
model: claude-code/sonnet
generated_at: '2026-09-25T20:54:44.603542'
score: 76
---

📌 用 Qwen3-TTS 在 SageMaker 打造即時語音克隆服務

TL;DR:AWS 展示如何把開源 Qwen3-TTS-12Hz-1.7B-Base 部署到 SageMaker 即時端點,用幾秒鐘參考音檔就能複製聲音並跨語言合成。

只要一段幾秒鐘的錄音和對應逐字稿,模型就能用這個人的聲音唸出任何新文字,甚至換成另一種語言——而且完全不需要重新訓練模型。

🤔 **語音克隆要解決的問題**

Voice cloning 能從一小段參考錄音重現特定說話者的聲音特徵,不必重新訓練模型。文章指出,媒體團隊、教育工作者與應用程式開發者可以用這個能力打造個人化語音體驗、將多語系內容在地化,同時支援無障礙溝通,並在跨語言情境下保留說話者的聲音身份。採用自行架設的公開模型,能自行掌控成本、讓語音資料留在自己的 AWS 環境中,也能依領域需求進一步調整;而透過 Amazon SageMaker AI 部署,基礎設施佈建、健康監控與自動擴縮都交給平臺管理,不需要自己維運底層的 GPU 伺服器。

🧩 **模型與部署架構**

Qwen3-TTS 是阿里雲 Qwen 團隊開發的公開 text-to-speech 模型家族,涵蓋中文、英文、日文、韓文、德文、法文、俄文、葡萄牙文、西班牙文、義大利文共 10 種語言,使用 Qwen3-TTS-Tokenizer-12Hz 語音分詞器,並支援串流生成以因應低延遲的互動情境。本文部署的是 Base 版本 Qwen3-TTS-12Hz-1.7B-Base,只需使用者提供的幾秒鐘音檔即可做語音克隆,也可作為 fine-tuning 的基底;這與另一個 CustomVoice 版本不同,後者是從一組固定的預設語者中生成語音,而非依使用者提供的參考音檔克隆。模型也支援跨語言克隆:可以用一種語言的參考音檔擷取聲音特徵,再用另一種語言生成語音,同時保留原說話者的音色。

在 SageMaker JumpStart 中,Qwen3-TTS-12Hz-1.7B-Base 與 Qwen3-TTS-12Hz-1.7B-CustomVoice、Qwen3-ASR-1.7B 一起提供,直接用 JumpStart 提供的模型檔案與預建服務容器部署,不需要自己撰寫推論處理程式。部署方式是建立一個 JumpStartModel 物件並呼叫 deploy,執行時需要帶入 SageMaker 執行角色的 ARN;端點需要幾分鐘才會進入 InService 狀態,因為容器要把模型載入 GPU。模型內部分成兩個階段在同一張 GPU 上運行:talker 與 code2wav,最終輸出 24 kHz 的音訊。

**GPU 記憶體是部署時最容易出包的地方。** vLLM 會依 gpu_memory_utilization 這個參數預先保留 GPU 記憶體,而 talker 與 code2wav 兩個階段共用同一張 GPU,因此兩者保留量加總必須留在 GPU 容量之內。文章建議兩階段各設為 0.45(0.45+0.45=0.90,留約 10% 緩衝)。容器啟動時,每個階段都會把記憶體用量記錄到 CloudWatch Logs:talker 權重約 3.66 GiB,code2wav 權重約 0.45 GiB,模型權重本身都不大,大部分配額其實變成了 KV cache,也就是暫存 in-flight 請求 token 的工作記憶體。在一張 24GB GPU、0.45 利用率下(約 22GiB 可用),每個階段可用到約 10GiB,兩階段合計仍有餘裕——這也是為什麼 24GB GPU(g6 家族、NVIDIA L4)就足以撐起這顆 1.7B 模型,不需要更大的 GPU。

呼叫端點時,有兩個 JumpStart 容器特有的細節必須注意:參考音檔要先轉成 24 kHz 單聲道 WAV,再編碼成 data:audio/wav;base64,... 格式;呼叫時還要帶上 CustomAttributes 路由參數,請求才能正確打到 text-to-speech 的 handler。回傳的音訊格式由 response_format 控制,文章示範用 "wav",模型會生成 24 kHz 單聲道音訊。單一請求適合處理一句話或一小段文字;較長的內容,例如整篇文章或多行腳本,建議拆成每句或每段各發一次請求,以維持整段語音的一致性。

📊 **如何選擇 instance 與估算容量**

文章建議依三步驟選擇 instance:先確認 JumpStart 是否支援該機型,再檢查帳號的 service quota,最後確認 GPU 記憶體是否放得下模型。對這顆 1.7B 模型而言,24GB GPU(g6 家族、NVIDIA L4)既相符又划算。若要估算可同時服務多少請求,可以查看端點日誌群組(路徑為 /aws/sagemaker/Endpoints/<endpoint-name>)中記錄的 KV cache token 預算。

🎯 **實務啟示**

對想在自己的應用中加入個人化、多語系語音功能又不想自行維運 GPU 基礎設施的工程團隊來說,JumpStart 的預建容器省下了自寫推論處理程式的功夫;而這類「同一張 GPU 跑兩階段模型」的部署,GPU 記憶體配置往往是最容易踩雷的環節,值得先照文章示範的 0.45/0.45 設定在小型 GPU 上驗證是否留有足夠緩衝,再依 CloudWatch 記錄的 KV cache 預算評估要不要擴大 instance 規模。

🔗 **來源**
- 標題:Deploying real-time personalized speech with Qwen3-TTS on Amazon SageMaker AI
- 作者/機構:Suneesh T,AWS Machine Learning Blog
- 連結:https://aws.amazon.com/blogs/machine-learning/deploying-real-time-personalized-speech-with-qwen3-tts-on-amazon-sagemaker-ai/

#TextToSpeech #VoiceCloning #Qwen3TTS #AmazonSageMaker #AWSMachineLearning #SpeechAI #MultilingualAI #vLLM #GenerativeAudio #MLDeployment
