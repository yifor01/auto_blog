---
title: Deploying Kimi K3 on AWS
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/deploying-kimi-k3-on-aws/
model: tencent/hy3:free
generated_at: '2026-07-31T08:35:57.174532'
score: 109
---

📌 【AWS 技術指南】如何將 2.8 兆參數的開源 MoE 模型 Kimi K3 部署於 AWS

TL;DR：透過 SageMaker HyperPod 或 Amazon EKS，可在 AWS 上自託管首個達到 3 兆級別的開源權重模型 Kimi K3。

隨著模型能力提升至能處理複雜的代理工作流（agentic workflows）與長程程式碼編寫（long-horizon coding），模型規模也隨之膨脹。面對需要專用基礎設施與高端 GPU 算力的兆級參數架構，組織需要能夠在自有基礎設施上進行自託管。

🧩 **Kimi K3：首個達到 3 兆參數等級的開源權重模型**

Moonshot AI 於 2026 年 7 月 27 日發布了 Kimi K3，這是一個擁有 2.8 兆參數的混合專家模型（Mixture of Experts, MoE）。

- **架構設計**：採用差異化架構，包含 Kimi Delta Attention (KDA)、Gated Multi Head Latent Attention (MLA) 以及 Stable LatentMoE 框架。
- **專家分配**：模型將 2.8 兆參數分佈於 896 個專家中，每次 token 僅會啟動 16 個專家。
- **效率提升**：每次前向傳播（forward pass）約啟動 1040 億個參數，相較於前代 Kimi K2，其擴展效率提升了 2.5 倍。
- **資料格式**：權重以 MXFP4 (Microscaling Floating Point 4-bit) 格式發布，在模型品質與記憶體效率之間取得平衡，適合大規模推論部署。

💡 **具備強大推理與工具調用能力**

Kimi K3 在長程程式碼任務、代理工作流與複雜推理方面表現卓越。它支援原生工具調用（tool calling）、結構化輸出（structured output），並具備「持續思考模式」（always-on thinking mode）以解決多步驟問題。

📊 **兩種主流的 AWS 部署路徑**

由於模型規模巨大，部署 Kimi K3 需要使用針對該模型開發的 vLLM day-0 推論容器。目前文章建議透過以下兩種方式進行部署：

- **Amazon SageMaker HyperPod**：適合需要高度管理與大規模訓練/推論環境的場景。
- **Amazon Elastic Kubernetes Service (Amazon EKS)**：適合需要靈活容器化管理與叢集控制的場景。

🎯 **實務啟示**

對於需要處理極高複雜度任務的企業，Kimi K3 的開源權重（可在 Hugging Face 找到 `moonshotai/Kimi-K3`）提供了在自有基礎設施上實現尖端智能的可能性。工程師在部署時，需重點考量 MXFP4 格式帶來的記憶體優勢，並選擇適合的 AWS 推論架構。

🔗 **來源**
- 標題：Deploying Kimi K3 on AWS
- 作者／機構：Vivek Gangasani @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/deploying-kimi-k3-on-aws/

#KimiK3 #MoonshotAI #AWS #SageMaker #EKS #MoE #LLM #OpenWeights #MachineLearning #GenerativeAI
