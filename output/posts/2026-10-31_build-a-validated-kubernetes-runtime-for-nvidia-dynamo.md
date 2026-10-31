---
title: Build a Validated Kubernetes Runtime for NVIDIA Dynamo
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/build-a-validated-kubernetes-runtime-for-nvidia-dynamo/
model: claude-code/sonnet
generated_at: '2026-10-31T20:40:50.765873'
score: 75
---

📌 NVIDIA AI Cluster Runtime：把Dynamo部署清單變成可驗證的配方

TL;DR：NVIDIA推出AICR,將Dynamo在Kubernetes上所需的GPU、排程、網路元件打包成已驗證的部署recipe。

部署一個NVIDIA Dynamo的DynamoGraphDeployment看似只是定義vLLM、SGLang或TensorRT-LLM該怎麼在pod裡跑,但這只是冰山頂端。在它底下,你還得回答一連串問題:GPU Operator裝好了嗎,驅動版本跟節點對得上嗎?GPU節點有沒有被正確標記、可被排程器發現?叢集是否透過Dynamic Resource Allocation(DRA)driver曝露GPU?排程器能不能滿足所需的topology與gang scheduling語意?Prometheus能不能收到Dynamo與加速器的指標?這些答對一個都不夠,全部答對才叫production-ready。

🤔 **Dynamo圖之下,還有一整層runtime要搞定**

NVIDIA Dynamo是一個分散式推論框架,負責在多個GPU worker間協調模型服務。把它部署到Kubernetes只是第一步,真正耗時的是上面那串基礎設施依賴——這些工作會把時間從「測試模型行為、服務效能、應用整合」上硬生生搶走。NVIDIA DSX AI Factory Platform整合了一系列技術來幫助生態系設計、建置與運維AI factory,Dynamo是其中之一,而NVIDIA AI Cluster Runtime(AICR)就是用來簡化這整層基礎設施管理的元件:它把Dynamo與其依賴的基礎設施打包成「已驗證的recipe」,每份recipe針對特定環境與workload定義pinned元件版本、相容性限制與驗證檢查。

🧩 **AICR這份recipe裡裝了什麼**

AICR針對Dynamo出貨的recipe,目前搭配dynamo-platform chart 1.4.2版,內含Dynamo operator、Dynamo runtime映像檔,以及nvidia.com/v1beta1的DynamoGraphDeployment CRD(取代舊版v1alpha1)。對照的基礎設施元件包括:GPU驅動層用NVIDIA GPU Operator;GPU探測靠Node Feature Discovery;GPU配置透過DRA Driver for NVIDIA GPUs走Kubernetes原生的DRA;排程由KAI Scheduler負責topology與gang scheduling;多元件serving圖的orchestration交給Grove;節點健康訊號視所選recipe而定,可用NVSentinel與Nodewright;指標收集靠Prometheus stack;若ingress要走Kubernetes原生路徑,則需要agentgateway與Gateway API資源。recipe同時固定元件版本、設定值、node selector、toleration、checksum與驗證預期,讓整套部署可重複執行。值得一提的是,從Dynamo 1.4開始,frontend、worker與選配的GAIE/EPP元件都改用Kubernetes資源互相發現,因此AICR的預設路徑不再使用NATS,dynamo-platform chart也不再預設安裝它,但仍保留為選配項。

Agentic workload會不斷延伸長長的token前綴(系統提示、工具定義、對話歷史、工具結果),若某輪請求落到GPU記憶體裡沒有該前綴的worker上,就必須重新處理中間token。Dynamo透過frontend router或GAIE/EPP整合,把請求導向已經持有相關KV block的worker。它還支援disaggregated serving,把prompt處理(prefill)與token生成(decode)拆開,各自獨立擴展——在AICR預設路徑下,請求走TCP,KV-cache事件走ZMQ,vLLM worker需設定如下:

```
--enable-prefix-caching --kv-transfer-config \
{"enable_kv_cache_events": true, "publisher": "zmq", "endpoint": "tcp://*:5557"}
```

Dynamo的worker runtime會訂閱這個本地vLLM事件源,將事件正規化後重新發布到Dynamo事件平面,供路由決策使用。

🧩 **兩條路由路徑,各有適用場景**

Path 1是Dynamo Frontend router:在DYN_ROUTER_MODE=kv模式下,Frontend對每個請求做tokenize,依prefix overlap與目前負載對候選worker評分,選出worker後透過TCP請求平面派送。這是最小的拓樸,也是目前最成熟、經過production驗證的服務方式,適合應用團隊自己擁有一個model-specific端點,或既有edge proxy只需把流量轉給Dynamo Frontend Service的情境。

Path 2整合Gateway API Inference Extension(GAIE)與Dynamo EPP:agentgateway將HTTPRoute解析到InferencePool,而這個InferencePool由Dynamo operator依據DynamoGraphDeployment建立——selector指定合格的worker pod,endpointPickerRef指向Dynamo EPP Service,gateway再透過GAIE的端點選擇介面呼叫Dynamo EPP。

🎯 **實務啟示**

如果團隊只是想要一個模型對外的最小拓樸,Path 1的Dynamo Frontend router已足夠且最成熟;若基礎設施要求ingress必須是Kubernetes原生的Gateway API,才需要上Path 2並承擔額外的gateway與EPP元件。對於跑agentic workload的團隊,KV-cache事件平面是否正確串接(ZMQ訂閱、Dynamo事件正規化)直接決定了prefix cache命中率,也就是實際的推論成本與延遲,部署前值得用AICR的驗證檢查逐項確認,而不是等上線後才踩坑。

🔗 **來源**
- 標題：Build a Validated Kubernetes Runtime for NVIDIA Dynamo
- 作者／機構：Stefan Schimanski, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/build-a-validated-kubernetes-runtime-for-nvidia-dynamo/

#NVIDIA #Dynamo #Kubernetes #LLMInference #MLOps #GPU #vLLM #KVCache #CloudNative #InferenceOptimization
