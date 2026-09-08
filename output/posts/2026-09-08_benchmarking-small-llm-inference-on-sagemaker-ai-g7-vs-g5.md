---
title: 'Benchmarking small LLM inference on SageMaker AI: G7 vs G5 and G6'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/benchmarking-small-llm-inference-on-sagemaker-ai-g7-vs-g5-and-g6/
model: claude-code/sonnet
generated_at: '2026-09-08T20:18:00.478801'
score: 79
---

📌 NVIDIA Blackwell G7實例上線,SageMaker推論吞吐量勝出六成

TL;DR: AWS實測顯示,新一代G7 GPU實例在30B規模MoE模型推論上,用更少GPU就贏過舊世代吞吐量與延遲。

用一半數量的GPU、更少的總顯存,吞吐量卻能贏過四張GPU的舊世代機型,這是Amazon SageMaker AI最新基準測試給出的結論。

🤔 同一顆模型,換一代GPU能差多少

選擇正確的GPU實例是部署LLM推論最具影響力的決策之一,同一世代的躍進就可能大幅改變延遲、吞吐量與每token成本,但實際增益取決於模型架構、量化格式與工作負載型態。AWS這篇文章用兩個具代表性的30B規模Mixture-of-Experts(MoE)模型,在Amazon SageMaker AI Inference上比較G5、G6、G6e、G7四個GPU實例家族的表現,展示新一代搭載NVIDIA Blackwell GPU的G7實例帶來的吞吐量、延遲與每token成本增益。

🧩 兩組實驗:程式碼模型與推理模型

第一組實驗鎖定企業級程式碼生成、除錯、重構等場景,部署Qwen3-Coder-30B-A3B-Instruct-FP8,透過Amazon SageMaker AI的DJL Large Model Inference(LMI)28.0容器,比較ml.g5.12xlarge(A10G)、ml.g6.12xlarge(L4)、ml.g7.12xlarge(RTX PRO 4500 Blackwell)三種實例。G5與G6組態各配備4張GPU、共96GB顯存,G7則只用2張GPU、共64GB顯存,以此檢驗G7在更少加速器與更少顯存下的表現。工作負載設定為100個請求、並發數4,平均輸入輸出各128 tokens,採非串流模式,透過NVIDIA AIPerf收集延遲與吞吐量指標。

第二組實驗鎖定推理、問答、摘要與agentic工作負載,部署NVIDIA Nemotron-3-Nano-30B-A3B-NVFP4,改用Amazon SageMaker AI Generative AI Inference Recommendations搭配vLLM,自動評估G6、G6e、G7組態並依成本、延遲、吞吐量排序建議。12xlarge組態下,G6提供4張GPU共96GB顯存,G6e提供4張GPU共192GB顯存,G7提供2張GPU共64GB顯存。

文中特別強調NVFP4的重要性:這是NVIDIA隨Blackwell架構推出的4-bit浮點格式,能把模型壓縮到約4 bit/權重且品質損失極小,但目前只有G7原生支援FP4 Tensor Core硬體加速,G5、G6雖然能跑NVFP4權重,卻缺乏硬體加速,這讓G7在MoE部署上佔有結構性優勢。原因在於MoE架構在解碼(生成token)階段主要受限於記憶體頻寬,因為每個token只會啟動一小部分專家層,頻寬越高,inter-token延遲越低、吞吐量越高。

📊 G7吞吐量贏G6六成、贏G5一成三

以下是Qwen3-Coder-30B案例在非串流工作負載下的結果:

| 指標 | G7領先G6 | G7領先G5 |
|---|---|---|
| 輸出吞吐量(391.3 tokens/秒) | 高約60.8% | 高約13.0% |
| 平均請求延遲 | 低約37.6% | 低約10.8% |
| P99延遲 | 低約54.7% | 低約20.2% |

⚠️ 目前只有兩個區域能用

文中提醒,G7目前僅在美國東部(俄亥俄)與美國西部(奧勒岡)區域正式可用,規劃部署前需留意區域限制。

🎯 給正在選型GPU實例的工程師的建議

若正在部署30B規模的MoE模型,且模型已採用FP8或NVFP4量化,G7值得優先納入評估,因為它能用更少的GPU數量達到更高吞吐與更低延遲。文中也展示了兩種評估路徑:已有既有端點時可直接用SageMaker AI benchmark比較延遲、吞吐量與每token成本;若還在選型階段,則可透過Generative AI Inference Recommendations自動化跑基準測試並取得排序建議,不必手動逐一嘗試組態。

🔗 來源
- 標題: Benchmarking small LLM inference on SageMaker AI: G7 vs G5 and G6
- 作者／機構: Mona Mona
- 連結: https://aws.amazon.com/blogs/machine-learning/benchmarking-small-llm-inference-on-sagemaker-ai-g7-vs-g5-and-g6/

#AmazonSageMaker #NVIDIABlackwell #GPUInference #MoE #LLMInference #AWS #vLLM #ModelQuantization #InferenceOptimization #MachineLearning
