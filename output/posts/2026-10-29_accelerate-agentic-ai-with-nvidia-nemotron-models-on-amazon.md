---
title: Accelerate agentic AI with NVIDIA Nemotron models on Amazon EKS and SageMaker
  HyperPod EKS
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/accelerate-agentic-ai-with-nvidia-nemotron-models-on-amazon-eks-and-sagemaker-hyperpod-eks/
model: claude-code/sonnet
generated_at: '2026-10-29T22:07:09.597825'
score: 90
---

📌 【NVIDIA】Nemotron 3.5 Super VL：120B MoE模型如何部署上雲

TL;DR：NVIDIA開源多模態agentic模型Nemotron 3.5 Super VL，AWS公開在EKS與SageMaker HyperPod EKS上的完整部署與壓測方法。

一個能同時讀懂文件、影片與程式碼的120B模型，真正燒GPU運算的卻只有12B參數，這是怎麼辦到的？

🤔 **一個模型同時服務文字與視覺任務**

Agentic AI工作流程常常需要同時處理文字推理與視覺理解，分開維護兩個模型成本高昂。Nemotron 3.5 Super VL是從Nemotron 3 Ultra蒸餾出的開放模型，加入既有的Nemotron 3 Nano、Nano Omni、Super、Ultra與Nemotron 3.5 Lightning家族，讓一個模型同時服務文字與視覺任務。NVIDIA公開了權重、訓練資料集與post-training recipes，使用者可以針對特定領域workload自行客製，並在自己掌控的基礎設施上運行。

🧩 **Hybrid Mamba-Transformer MoE架構**

模型採用hybrid Mamba-Transformer MoE架構，交錯排列Mamba-2、attention與expert layers。Sparse routing讓每個token只啟動120B參數中的12B，計算量接近小型模型，但GPU記憶體仍需容納完整權重。Mamba-2層在生成過程中維持固定大小的state，不像KV cache會隨序列長度增長，讓長context的成本更可控。模型還搭載recursively shared的Multi-Token Prediction（MTP）head，支援原生speculative decoding。

📊 **Hermes Bench 63.44%，agent評測87.05%**

根據NVIDIA technical report，Nemotron 3.5 Super VL在Hermes Bench拿下63.44%，在LangChain agent evaluations拿下87.05%，在CharXiv圖表推理基準上則是80.8%。模型整合了NVIDIA reference implementations、cookbooks與Agent Toolkit，可接入主流開放agent框架與orchestration系統。

💡 **從NCCL驗證到concurrency sweep的部署實測**

AWS的aws-do-eks專案提供了在標準Amazon EKS、EKS Auto Mode與SageMaker HyperPod EKS上部署的參考實作，三種orchestrator共用同一套Kubernetes manifest。架構上，Amazon ECR存放container image，共享的Amazon FSx for Lustre volume存放模型權重，Elastic Fabric Adapter（EFA）連接GPU節點。NVIDIA Dynamo可以把服務架構設計成單節點aggregated，或prefill/decode拆到不同節點的disaggregated模式，對於視覺語言模型，image/video encoding階段甚至可以再拆到獨立節點。這套架構已在p6-b200.48xlarge（8張NVIDIA B200）與p5en.48xlarge（8張NVIDIA H200）上驗證過。

部署前可先用NCCL all-reduce micro-benchmark驗證叢集與網路，確認所有GPU都有負載、所有EFA adapter都有流量；之後用NVIDIA的aiperf工具量測TTFT（time to first token）、ITL（inter-token latency）與TPS（tokens per second）。在不同並發量下做concurrency sweep，可以畫出latency budget的水平線（例如TTFT低於600毫秒、ITL低於每token 100毫秒），找出單一副本在SLO內能撐住的最大吞吐量，再用目標TPS除以單副本吞吐量，就能算出需要部署多少組prefill-decode pair。文中提到的範例顯示aggregated與disaggregated部署的TTFT有差異，但ITL相近，單副本在SLO下約可撐到每秒320 tokens。

⚠️ **重量級基礎設施需求**

這套方案仰賴EFA、FSx for Lustre與多節點GPU叢集等基礎設施，面向的是平臺或infra團隊的規模化部署，不是單機就能跑起來的輕量方案。

🎯 **capacity planning可以照著這套方法走**

如果團隊要部署大型MoE多模態模型，aws-do-eks的「NCCL驗證＋aiperf concurrency sweep」是一套可重複的方法論：先確認叢集網路沒問題，再用sweep找出SLO下的真實吞吐量上限，每次換精度、TP/PP配置或aggregated/disaggregated策略後重跑一次，就能直接看出哪個方向的曲線更划算，而不是憑感覺猜GPU數量。

🔗 **來源**
- 標題：Accelerate agentic AI with NVIDIA Nemotron models on Amazon EKS and SageMaker HyperPod EKS
- 作者／機構：Alex Iankoulski，AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/accelerate-agentic-ai-with-nvidia-nemotron-models-on-amazon-eks-and-sagemaker-hyperpod-eks/

#NVIDIA #Nemotron #MoE #AgenticAI #AmazonEKS #SageMaker #MultimodalAI #vLLM #GPUInference #AWS
