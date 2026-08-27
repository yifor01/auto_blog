---
title: 'Bring your own model with Amazon SageMaker AI: Script mode in SDK v3'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/bring-your-own-model-with-amazon-sagemaker-ai-script-mode-in-sdk-v3/
model: claude-code/sonnet
generated_at: '2026-08-27T17:26:01.911276'
score: 95
---

📌 SageMaker SDK v3：把「自帶模型」的工作流程砍掉重練

TL;DR：SageMaker Python SDK v3 用統一的 ModelTrainer／ModelBuilder 取代框架專屬類別，程式碼與容器徹底解耦。

2021 年 AWS 曾發表過一篇介紹 script mode 的文章，讓開發者不必自建 Docker image 就能在 SageMaker 上跑自己的演算法。五年後的今天，SDK v3 把這套工作流程重新設計了一遍，讓「自帶模型」變得更加精簡。

🤔 **問題：框架專屬類別讓程式碼與容器綁得太死**

過去的 SDK 針對不同框架有各自的 estimator 類別，像是 SKLearn、PyTorch、XGBoost，各自維護一套邏輯。v3 版本把這些統一成單一的 ModelTrainer（訓練）與 ModelBuilder（部署），簡化了介面也降低了學習曲線。

🧩 **核心設計：SourceCode 物件把程式碼與容器解耦**

v3 最關鍵的概念是新的 SourceCode 設定物件。它接受一個 source_dir（本機程式碼目錄路徑），搭配一個 command 字串（訓練用）或 entry_script（推論用）。作業啟動時，SageMaker 會把這個目錄同步進容器，你的程式碼在容器內執行，但不需要事先烘進 image 裡。

實務上，你只需要自建一個乾淨的容器映像（或直接用 AWS Deep Learning Container，也可以用第三方 image），這個容器只包含 runtime 與框架函式庫，不含任何訓練程式碼。容器建好一次、推上 Amazon ECR 之後，之後就可以無限次修改訓練程式碼，完全不用再碰 Docker。

🛠️ **兩個端到端範例：從傳統 ML 到多 GPU 生成式 AI**

文章示範了兩種情境。第一個是經典 ML 流程：在 diabetes 資料集上訓練一個 Random Forest 分類器，並部署到即時（real-time）SageMaker endpoint。訓練時把 TRAINING_IMAGE_URI 指向自建容器，部署階段則可以直接用預建的 DJL framework 容器，不一定要自己包一個。過程中也內建了 fully managed MLflow 追蹤選項，只要設定 MLFLOW_ARN 與 MLFLOW_EXPERIMENT_NAME 就能記錄超參數、指標與模型產出物，設為 None 則跳過。

第二個範例規模更大：用 Hugging Face Accelerate 在 4 張 A10G GPU（ml.g5.12xlarge 實例）上，以 LoRA 對 Stable Diffusion 3.5 Medium 做微調。容器內同樣只放 PyTorch、diffusers、transformers、accelerate、PEFT、DeepSpeed 等深度學習堆疊，不含訓練腳本；LoRA 微調邏輯、Accelerate 啟動腳本、recipe 設定檔全部放在 source_dir，於執行期同步進容器。想換 recipe、調整 LoRA rank、換 base model，直接改本機檔案即可，不需要重建容器。

📦 **部署端：ModelBuilder 一次搞定封裝與註冊**

部署階段呼叫 build() 會依照所選 model server（範例中是 DJL Serving）的慣例，把推論 handler 與模型產出物打包在一起，並註冊一個指向推論 image 與 S3 上重新打包產出物的 SageMaker 模型。ModelBuilder 還能自動選擇容器、自動擷取相依套件、從原始框架模型產生序列化程式碼。呼叫 deploy() 就能建立即時 endpoint。若工作負載需要，也可以把多個模型打包在同一個 endpoint 底下，用 inference components 各自獨立分配資源與擴展。

🎯 **實務啟示**

這次更新的價值在於「容器穩定、程式碼可迭代」的分離設計：把容器當成版本控制過的執行環境，訓練或推論邏輯全部放在本機目錄，靠 SourceCode 在執行期同步。對於需要頻繁調整訓練腳本、又不想每次重建 image 的團隊，這能明顯縮短迭代週期，也適用於從傳統 ML 到多 GPU 生成式 AI 微調的各種規模工作負載。

🔗 **來源**
- 標題：Bring your own model with Amazon SageMaker AI: Script mode in SDK v3
- 作者／機構：Bobby Lindsey, AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/bring-your-own-model-with-amazon-sagemaker-ai-script-mode-in-sdk-v3/

#AmazonSageMaker #AWS #MachineLearning #MLOps #ScriptMode #ModelTrainer #ModelBuilder #LoRA #StableDiffusion #DistributedTraining
