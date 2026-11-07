---
title: 'Buoyant Releases Kinference: An Open Source Inference Control Plane for Kubernetes
  and vLLM'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/07/buoyant-kinference-open-source-inference-control-plane-kubernetes-vllm/
model: claude-code/sonnet
generated_at: '2026-11-07T20:59:25.398624'
score: 91
---

📌 Buoyant 開源 Kinference：把 K8s＋vLLM 揉成一個多租戶推理平臺

TL;DR：開源控制平面加上 KV-cache 感知路由，尖峰 goodput 比純隨機負載平衡高達 7 倍以上。

當一家公司要同時對內部多個團隊提供好幾個開源權重模型的推論服務，「每個 vLLM pod 後面排一條 Kubernetes Service」很快就會變成瓶頸：誰先搶到誰先跑，快取命中率看運氣，也沒有任何按租戶計費或限流的機制。Linkerd 背後的公司 Buoyant，針對這個痛點推出了開源專案 Kinference。

🤔 vLLM 管資料面，Kinference 管決策面

Kinference 是一個架在 vLLM 工作節點前面的推理控制平面（inference control plane）。按照 Buoyant 官方 FAQ 的說法：vLLM 是資料平面，Kinference 是控制平面。它在同一層裡處理路由政策、token 速率限制、KV-cache 感知的負載平衡，以及每租戶的指標蒐集，目標客群是需要把多個開放權重模型提供給多個內部用戶的開發團隊。專案採 Apache 2.0 授權，目前版本為 v0.1.0-alpha.7。

🧩 兩個元件、五個 CRD、一個預測指標

Kinference 的架構分成兩部分：一個流量閘道（traffic gateway），以及一個推理處理器（inference handler）。README 指出，處理器對外暴露 gRPC 介面，接收請求後回傳應該送往的端點，以及可能被改寫過的請求內容；它與像 Buoyant Gateway 這樣的 proxy 搭配使用。

Kinference 會監看 vLLM 的 KV-cache 事件與引擎指標，目前採用 NVIDIA 的 dynamo-kv-router crate 來處理這些快取事件。所有設定都放在五個 CRD 裡：GatewayBackend、InferencePolicy、InferencePool、InferenceProvider、InferenceWorkerSet。

推理政策（inference policy）是宣告式規則，決定每個請求該怎麼路由或直接拒絕，規則可以依租戶、請求的模型、GPU pool 的狀態、甚至語意標籤來比對。官網列出的範例政策涵蓋五種模式，而大多數規則最終都會收斂成同一個目標：minimize: PredictedTTFT。也就是說，Kinference 會根據快取重疊程度與佇列長度，預測每個候選端點的首 token 時間（TTFT），再挑出最划算的那個。這些政策本身可以放進 git 做版本控管，並用 kinfctl CLI 離線驗證。

📊 shared-prefix 場景下，尖峰 goodput 高了 7.4 倍

Buoyant 公布了一份對比純 Kubernetes 負載平衡的 benchmark。測試中每個對照組使用 3 個 vLLM 0.31.0 pod，每個 pod 配一張 L40S GPU，模型是 Qwen3.8-27B-FP8，壓測工具為 GuideLLM 0.8.1。基準線是一個 ClusterIP Service，也就是 kube-proxy 對每條連線隨機挑一個 pod 的作法。

結果顯示：在未滿載情況下，shared-prefix 場景的中位數端到端延遲下降 45%，multiturn 場景下降 32%；在控制流量測試中，p95 TTFT 從 21.46 秒降到 12.33 秒，Buoyant 將此歸功於具佇列感知的負載平衡。在容量測試（衡量符合 TTFT SLO 的每分鐘請求數，也就是 goodput）中，shared-prefix 場景的尖峰 goodput 從 14.0 req/min 提升到 103.0 req/min，約 7.4 倍；multiturn 場景從 23.8 提升到 82.7 req/min，約 3.5 倍。作為基準線的 Service，在任何測試的併發量下都沒有達到 SLO。

💡 這份數字怎麼看待

這些數字是 Buoyant 自行量測並公布的，比較的基準是「隨機路由」，而不是 llm-d 或 NVIDIA Dynamo 這類本身就具備快取感知能力的路由器。Buoyant 自己也提到，測試用的 SLO（8 秒與 4 秒）比較適合離線的 agent 工作流，不是即時聊天場景。換句話說，這份 benchmark 證明的是「比完全不做快取感知路由好很多」，而不是「比業界最強的快取感知路由器更快」。

⚠️ 它的強項是治理，不是刷榜效能

照 Buoyant 自己的定位，Kinference 的差異化角度在於治理層面：政策管理、模型別名、provider fallback、按租戶的用量統計，這些是 llm-d 與 Dynamo 目前沒有主打的部分；反過來說，在純推論效能、disaggregation、引擎覆蓋範圍上，llm-d 與 Dynamo 仍是領先者。想導入的團隊，得先確認自己缺的是「治理與多租戶管理」還是「極限吞吐效能」。

🎯 實務啟示

照官方的 Getting Started 指南，安裝只需五步：裝 Gateway API v1.5.1 的 CRD、裝 Buoyant gateway 的 Helm chart、再裝 Kinference 的 Helm chart。Kinference 本身內建 Prometheus 指標與 Grafana 儀表板，指標涵蓋 TTFT、ITL（inter-token latency）、端到端延遲，以及按租戶拆分的快取命中／未命中 token 數。對已經在用 vLLM 跑多租戶服務、但苦於沒有統一路由政策與計費依據的團隊，這是一個可以直接拿 Helm chart 落地評估的方向。

🔗 來源
- 標題：Buoyant Releases Kinference: An Open Source Inference Control Plane for Kubernetes and vLLM
- 作者／機構：Michal Sutter／MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/07/buoyant-kinference-open-source-inference-control-plane-kubernetes-vllm/

#Kinference #vLLM #Kubernetes #LLMOps #InferenceOptimization #OpenSource #Buoyant #KVCache #MultiTenant #MLInfra
