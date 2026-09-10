---
title: Deploying Qwen3.8-2.4T-A95B on Amazon SageMaker HyperPod with vLLM
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/deploying-qwen3-8-2-4t-a95b-on-amazon-sagemaker-hyperpod-with-vllm/
model: claude-code/sonnet
generated_at: '2026-09-10T19:58:02.898402'
score: 101
---

📌 開源首見:2.4T 參數 Qwen3.8 如何用 vLLM 上線

TL;DR:Qwen 首度開源 Max 等級模型,教你用 vLLM 在 SageMaker HyperPod 部署上線。

🎣 當你聽到「2.4 兆參數」時,第一個念頭大概是「這種規模的模型一般團隊根本養不起」。但 Alibaba 的 Qwen 團隊在 2026 年 8 月 12 日把 Qwen3.8-2.4T-A95B 的權重公開釋出,這是 Qwen-Max 等級模型第一次以開源權重形式問世。AWS 這篇文章示範了如何把這隻巨獸實際搬上 Amazon SageMaker HyperPod,用 vLLM 撐起一個 OpenAI 相容的推論端點。

🤔 背景:為什麼開源權重重要

開源權重讓企業能把資料留在自己的基礎設施內、依需求客製推論行為,且不必為大規模使用支付逐 token 的 API 費用。但代價是維運複雜度:這種規模的模型需要專門設計的 GPU 基礎設施與最佳化的服務堆疊才扛得住。本文是 AWS「部署開源兆參數模型」系列的第二篇,第一篇處理的是 Kimi K3。

🧩 架構重點:混合式 attention 與細粒度 MoE

Qwen3.8-2.4T-A95B 總參數 2.4 兆,每個 token 僅啟動約 950 億參數,原生 context 長度達 262K tokens,可延伸至 1M。關鍵在於它的混合 attention 設計:92 層中有 69 層是 Gated DeltaNet(線性 attention,搭配固定大小的 recurrent state),另外 23 層是 Gated Attention(完整的二次方 attention,負責高保真度的 token 互動)。這種 3:1 的比例讓運算量與記憶體用量在 context 逼近 1M tokens 時仍維持在可控範圍,對於會在多輪對話中不斷累積工具輸出、程式碼與推理軌跡的 agentic 工作負載尤其重要。

MoE 部分採細粒度設計,把容量分散到 512 個小型 expert,而非少數幾個大型 expert,藉此提升路由效率與專精程度。由於每次前向傳播只啟動約 950 億參數,實際服務成本跟著啟動參數走,而非整個 2.4 兆參數規模。

Qwen3.8 針對 agentic 執行場景設計,包括多步驟寫程式、自主工具呼叫、長時程規劃與複雜研究工作流,並內建 reasoning_effort 參數(low / medium / high),讓開發者依請求需求在推理深度與運算成本間取捨:困難的多步驟問題可以調高,高吞吐量任務則調低。開源權重以標準 Transformers 格式發布在 Hugging Face,社群量化版本包含 MXFP4 與 NVFP4(W4A4),可把模型壓縮到約 1.2 TB,足以塞進單一 8 GPU、搭載 B300 Blackwell Ultra 的節點。

📊 官方基準數據:研究與終端寫程式表現亮眼

根據 vendor 的基準測試結果,Qwen3.8-2.4T-A95 在研究工作流(PaperBench 93.0)、指令遵循(IFBench 82.8)與終端寫程式(86.6)上表現突出,多數類別與頂尖前沿模型相當,但在較困難的 repository 層級任務(SWE-bench Pro)與一般工具使用(Toolathlon)上仍有進步空間。對於評估自架替代方案取代專有 API 的團隊而言,這些結果讓 Qwen3.8-2.4T-A95 成為 coding agent 與研究 pipeline 的可信選項。

🧩 上線架構:SageMaker HyperPod 負責「怎麼跑」

部署 2.4T 參數模型不只是 GPU 夠不夠的問題,還牽涉模型下載、容器排程、健康監控、自動擴縮與節點故障處理,全部要在無人介入下完成。SageMaker HyperPod 的 EKS-orchestrated 叢集以 Amazon EKS 作為控制平面,你仍保有完整的 Kubernetes 生態(kubectl、Helm charts、CRD),AWS 則負責底層基礎設施生命週期,包括網路、儲存、GPU 驅動安裝與 NVIDIA device plugin。

HyperPod Inference Operator 提供單一 CRD——InferenceEndpointConfig,可宣告式指定模型、容器映像檔、GPU 資源請求與 vLLM 啟動參數。ml.p6-b300.48xlarge(8x NVIDIA B300 Blackwell Ultra GPU)這款機型需透過 Flexible Training Plan 取得保留容量,不會與 on-demand 資源池搶用,也沒有冷啟動容量風險。HyperPod 會持續監控節點健康狀態並自動更換故障節點,對 24/7 運行的推論服務來說,大幅減少人工偵測與復原的維運負擔。

📊 記憶體算法:NVFP4 量化如何讓 2.4T 塞進單節點

以 BF16 精度計算,Qwen3.8 的 2.4 兆參數光是權重就需要約 4.8 TB 記憶體,超過單一 8-GPU 節點的容量。改用 NVFP4(W4A4)量化後,每個參數壓縮到約 4 bits,權重總量降到約 1.2 TB,可以舒服地放進 p6-b300 實例約 2.1 TB 的聚合 GPU 記憶體內,還留有空間給 KV-cache 與 activation。混合 attention 架構在此是關鍵優勢:69 層 DeltaNet 維持固定大小的 recurrent state,不會隨 context 增長,只有 23 層完整 attention 會讓記憶體用量隨 context 成長。作為參考,NVIDIA 在 GB300 NVL72(FP8、72 顆 GPU)上的 Day-0 基準測試達到每 GPU 每秒超過 4K tokens、每使用者每秒超過 350 tokens;單一 8-GPU p6-b300 節點搭配 NVFP4 的聚合吞吐量會按比例降低,但仍適合中等併發量的生產推論工作負載。

💡 vLLM 關鍵配置:reasoning、tool calling 與 MTP 投機解碼

文章提供的 vllm serve 配置包含三個重點旗標:
- --reasoning-parser qwen3:從模型輸出的 <think>...</think> 區塊中擷取推理內容。
- --enable-auto-tool-choice 搭配 --tool-call-parser qwen3:啟用 OpenAI 相容的 function calling。
- --speculative-config '{"method":"mtp","num_speculative_tokens":1}':啟用 Qwen3.8 內建 draft head 的 Multi-Token Prediction(MTP)投機解碼。

完整的部署 manifest 與腳本已公開在 AWS 提供的 GitHub repository 中,部署流程涵蓋叢集佈建、套用 InferenceEndpointConfig 到監控部署進度等階段,模型下載本身就需要一定時間。

🎯 實務啟示:量化與投機解碼是榨乾單節點吞吐量的關鍵

對於已經在用 SageMaker HyperPod 或考慮自架 frontier-class 模型的團隊,這篇文章示範了一條完整路徑:從取得保留 GPU 容量、用宣告式 CRD 管理部署,到利用 NVFP4 量化與 MTP 投機解碼壓榨單節點吞吐量。如果你的 agentic workload 需要長 context 與高工具使用密度,Qwen3.8 的混合 attention 設計值得列入自架選項評估清單。

🔗 來源
- 標題:Deploying Qwen3.8-2.4T-A95B on Amazon SageMaker HyperPod with vLLM
- 作者/機構:Dmitry Soldatkin, AWS ML Blog
- 連結:https://aws.amazon.com/blogs/machine-learning/deploying-qwen3-8-2-4t-a95b-on-amazon-sagemaker-hyperpod-with-vllm/

#Qwen #vLLM #SageMakerHyperPod #LLMInference #MoE #OpenWeights #NVFP4 #SpeculativeDecoding #AgenticAI #AWS
