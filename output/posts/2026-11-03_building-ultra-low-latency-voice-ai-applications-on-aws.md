---
title: Building ultra-low-latency voice AI applications on AWS
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/building-ultra-low-latency-voice-ai-applications-on-aws/
model: claude-code/sonnet
generated_at: '2026-11-03T22:35:23.600226'
score: 88
---

📌 Cartesia 用 State Space Model 把語音 AI 延遲壓進百毫秒內

TL;DR：AWS 合作夥伴 Cartesia 以 SSM 架構取代 transformer，讓語音合成與辨識的 first-byte 延遲進入 sub-100ms，並提供兩種 AWS 部署路徑。

人類對話中容許的接話延遲窗口極短，只要 AI 的回覆慢了半拍，整段對話的「人味」就會碎掉。這正是語音 AI 基礎設施最難啃的一塊硬骨頭——而 AWS 這篇文章介紹的 Cartesia，選擇用一套跟主流 transformer 完全不同的架構來解這個問題。

🤔 Transformer 的品質與延遲互相拉扯

傳統以 transformer 為基礎的文字轉語音（TTS）模型，在串流延遲上天生吃虧，因為它們必須先處理完整個序列才能產生輸出。這造成一個根本性的矛盾：想要更高品質，往往就要付出更高延遲的代價。

🧩 SSM 的運作方式與 Cartesia 的兩個模型

State Space Model（SSM）處理序列的方式與 transformer 截然不同。Transformer 靠 attention 機制，把序列中每個元素跟其他所有元素互相比對，運算量會隨序列長度呈平方成長；SSM 則把序列視為一個隨時間連續演化的系統，逐步處理、並往前傳遞一個精簡的內部狀態，這種運算方式可以轉換成電腦能有效率執行的形式，讓長序列的成本維持在低水位。這樣的特性讓 SSM 特別適合即時串流資料，例如語音。

Cartesia 把這個優勢落實成兩個正式產品模型：Sonic 負責文字轉語音（TTS），Ink 負責語音轉文字（STT），兩者都以 sub-100ms 的 first-byte 延遲為目標，同時維持錄音室等級的輸出品質。Sonic 是 Cartesia 的旗艦串流 TTS 模型，適合想用最少維運成本快速上線的團隊，呼叫 API 就能即時收到串流音訊；Ink 則是為對話式 AI 打造的串流語音轉文字模型。

🧩 在 AWS 上的兩種部署路徑

第一種是透過 Amazon SageMaker AI 的託管部署（適用於 Sonic）：Sonic 以 AWS Marketplace 的 model package 形式上架，先訂閱一次取得該 Region 專屬的 model-package ARN，再透過 console 或 SageMaker／Boto3 SDK 用這個 ARN 建立 SageMaker AI endpoint。執行這個流程的 IAM 角色需要 `AmazonSageMakerFullAccess`，訂閱步驟則需要 `aws-marketplace:Subscribe`、`Unsubscribe` 與 `ViewSubscriptions` 權限；部署前要從 model package 的 `SupportedRealtimeInferenceInstanceTypes` 欄位挑選受支援的執行個體類型，額度不足時可能要申請服務配額提升。Endpoint 進入 `InService` 狀態後，就能用 SageMaker Runtime 的 `InvokeEndpointWithResponseStream` API 呼叫並處理回傳的音訊串流。Ink 目前則是透過 Cartesia API 取得，可在 AWS Marketplace 的 Cartesia Voice AI Platform listing 購買。

第二種是在 Amazon EC2 GPU 執行個體上自管部署，適合已有 GPU 基礎設施、網路需求嚴格、或需要與其他服務共置的團隊：先向 Cartesia 取得 Sonic 容器映像檔與授權條款，複製到自己私有的 Amazon ECR repository，讓運算層能用 IAM 範圍內的憑證拉取，不必頻繁對外部 registry 存取。GPU 執行個體方面，G6（L4）與 G6e（L40S）是即時 TTS 的最佳平衡選擇，較舊的 G5（A10G）也能運作。運算層可以用 Amazon ECS（註冊 GPU task definition，設定 GPU resource requirement，前面接 Application Load Balancer）或 Amazon EKS（建立 GPU node group 或 Karpenter provisioner，搭配 EKS GPU 優化 AMI 與 NVIDIA device plugin，以 Deployment 加 Service/Ingress 部署）。為了壓低延遲，建議把推理節點放進 cluster placement group，同一組 replica 集中在單一 Availability Zone，並用 VPC endpoint 存取 ECR/S3；若呼叫端在混合雲或地端環境，建議透過 AWS Direct Connect 或 private Network Load Balancer 終止流量，避開公開網際網路的額外跳點。

若有資料主權、延遲控制或法規遵循的需求，也可以直接把 Cartesia 模型部署進自己 AWS 帳號內的 VPC，推理資料不會離開該帳號範圍。

⚠️ 素材未涵蓋的部分

這篇文章沒有提供 Sonic／Ink 的實測延遲數字（僅說明目標是 sub-100ms）、也沒有提到具體定價，這裡不做臆測，保留從簡。

🎯 實務啟示

對要打造對話式語音產品的工程團隊而言，這提供了兩條清晰路徑：用 SageMaker Marketplace 的 model package 快速上線，或在既有 GPU／K8s 基礎設施上自管部署以取得更細緻的網路與延遲控制。無論選哪一條，cluster placement group、單 AZ 部署與 VPC endpoint 這類網路層優化，看似基礎卻是把延遲壓進對話可接受窗口內的關鍵細節。

🔗 來源
- 標題：Building ultra-low-latency voice AI applications on AWS
- 作者／機構：Nolan Chen／AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/building-ultra-low-latency-voice-ai-applications-on-aws/

#VoiceAI #StateSpaceModels #TextToSpeech #SpeechToText #AWS #SageMaker #Cartesia #ConversationalAI #LowLatency #EdgeInference
