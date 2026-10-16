---
title: 'Introducing Reflection Beam: an open-weight model for agentic coding on AWS'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/introducing-reflection-beam-an-open-weight-model-for-agentic-coding-on-aws/
model: claude-code/sonnet
generated_at: '2026-10-16T20:15:08.412868'
score: 83
---

📌 Reflection Beam登陸AWS：501B參數模型兩種部署路徑

TL;DR：Reflection AI的開放權重agentic coding模型Beam已上架AWS SageMaker JumpStart，提供託管端點與HyperPod Kubernetes兩種部署方式。

開放權重的大型agentic coding模型，部署起來往往比下載權重檔麻煩得多。Reflection AI的Beam總參數高達5010億，要真正跑起來需要多GPU、對的checkpoint格式、對的執行環境。AWS這篇文章給出的答案，是兩條明確分流的部署路徑：想要最快上線就用SageMaker JumpStart，想要掌控底層基礎設施就用HyperPod Inference。

🤔 **一個模型，三種checkpoint，不同硬體組合**

Beam是一個sparse mixture-of-experts模型，專為解決軟體問題、修改程式碼、呼叫工具與處理中間結果而設計，總參數501B，每次推論實際啟用23B參數，Reflection官方宣稱其有效context長度可達100萬tokens。權重透過Hugging Face以Apache 2.0授權釋出，提供BF16、FP8、NVFP4三種checkpoint格式，對應不同的記憶體用量與硬體相容性：
- BF16：權重記憶體需求最大，需規劃多節點配置以湊足總GPU記憶體
- FP8：對應ml.p5.48xlarge（NVIDIA H100）或ml.p5e.48xlarge／ml.p5en.48xlarge（H200）
- NVFP4：對應ml.p6-b200.48xlarge（NVIDIA B200）

目前Beam僅在美國東部（維吉尼亞北部）與美國東部（俄亥俄）兩個區域的SageMaker JumpStart上架。

🧩 **兩條部署路徑：全託管 vs. Kubernetes原生控制**

JumpStart即時端點（Real-time Endpoint）路徑把模型、容器與端點打包成一套託管部署流程，是從模型目錄到HTTPS端點最短的路徑。官方提供的範例支援一個variant-aware指令，可切換部署BF16、FP8或NVFP4，省略參數時預設使用NVFP4。

當需要Kubernetes原生的分散式GPU基礎設施控制時，則改用SageMaker HyperPod Inference，可選擇AWS託管的JumpStart容器設定，或是自行用SGLang、vLLM部署。這條路徑需要事先準備好EKS編排的HyperPod叢集、HyperPod Inference Operator及相關add-on，以及VPC、子網路、安全群組等網路設定；若要啟用模型快取，還需要本地NVMe容量。HyperPod的Inference Gateway提供OpenAI相容介面，並能在多個副本間路由請求，同時支援分層KV快取與智慧路由。文章附帶的manifest模板（reflection-beam-jumpstart.yaml、reflection-beam-sglang.yaml、reflection-beam-vllm.yaml）皆可在部署前先行檢視內容。

💡 **先選部署方式，再談基礎設施**

文章給出的判斷準則很清楚：預設先從SageMaker JumpStart開始，除非工作負載需要特定的推論執行環境或設定。JumpStart減少容器整合工作，HyperPod則保留對叢集容量、擴展與可觀測性的控制權。對於需要infrastructure-as-code流程的團隊，HyperPod範例中的JumpStart設定檔正好提供這個切入點；若需要直接掌控serving runtime，則切換到SGLang或vLLM manifest即可，差異只在替換一個設定值。

🎯 **實務啟示**

對已經在AWS上運作的團隊而言，這篇文章的價值在於把「部署一個5000億參數MoE模型」這件原本高門檻的工程工作，拆成清楚可複製的步驟：先確認checkpoint格式對應的instance type，再決定是要全託管端點還是Kubernetes控制權，最後用官方提供的smoke test驗證端點是否正常回應。測試完成後記得刪除資源，避免持續計費。

🔗 **來源**
- 標題：Introducing Reflection Beam: an open-weight model for agentic coding on AWS
- 作者／機構：Clement Perrot
- 連結：https://aws.amazon.com/blogs/machine-learning/introducing-reflection-beam-an-open-weight-model-for-agentic-coding-on-aws/

#ReflectionAI #Beam #AWS #SageMaker #HyperPod #OpenWeightModel #AgenticCoding #MixtureOfExperts #vLLM #SGLang
