---
title: Introducing Amazon SageMaker HyperPod Inference Gateway
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/introducing-amazon-sagemaker-hyperpod-inference-gateway/
model: claude-code/sonnet
generated_at: '2026-09-18T19:52:25.439445'
score: 93
---

📌 首token延遲最多降82%，SageMaker新增GPU感知推論閘道

TL;DR：HyperPod Inference Gateway用GPU即時訊號路由推論請求，零改動應用程式碼即可裝上。

一個聊天機器人使用者原本要等4.4秒才看到第一個字，換上新的路由層後縮短到800毫秒以內。造成這種差距的元兇，往往不是模型本身，而是Kubernetes預設的round-robin或least-connections負載平衡演算法——它們對GPU內部發生的事完全沒有可見性。

🤔 **問題不在模型，在路由演算法看不見GPU裡發生什麼**

當叢集裡有些pod的KV cache已經飽和、有些正在跑到一半的長文本生成、還有些已經把你需要的LoRA adapter載入記憶體時，傳統round-robin依然會盲目地把請求平均分配。結果就是請求堆積在忙碌的pod後面，閒置容量卻沒被用到；流量突發時首token延遲飆到4秒以上；GPU利用率高低不均、難以預測；團隊只能靠過度佈署GPU來補償——這等於花錢養著沒在做有用工作的GPU。

🧩 **兩層架構：叢集內智慧路由 + 跨叢集全域協調**

Amazon SageMaker HyperPod Inference Gateway是一個Kubernetes原生的GPU感知路由系統，以單一EKS managed addon（amazon-sagemaker-hyperpod-inference）的形式部署在既有HyperPod基礎架構上。

第一層（Tier 1）建構在開源的Gateway API Inference Extension之上，包含三個核心元件：一個高效能L7 proxy負責終止進入的HTTPS流量，並為每個叢集對外暴露單一私有端點；它會檢查每個OpenAI相容請求的body，抽出model欄位，路由到正確的模型池，天生支援一個閘道服務多個模型；而真正的智慧層則是EPP（Endpoint Picker），它持續消費每個模型伺服pod回報的即時Prometheus指標，用一套加權評分演算法選出最適合的後端——每個評分項都可設定權重，因此你可以依工作負載特性（延遲敏感的對話 vs. 吞吐量優先的批次任務）調整路由行為，其中包括會識別哪些pod已經把特定LoRA adapter載入記憶體的LoRA Affinity Scorer，以及找出共享prompt前綴命中率的Prefix Cache Hit Rate Scorer。第二層（Tier 2）則疊加在Tier 1之上，提供跨叢集、跨區域的協調能力：跨叢集容錯移轉、全域流量限速，以及成本感知的流量調度。

部署方式很單純：安裝addon、建立一個宣告式的InferenceGatewayConfig自訂資源定義模型與路由行為，再幫既有的模型伺服deployment加上標籤讓閘道能發現它們。閘道對外暴露的是標準OpenAI相容端點，現有的client程式碼完全不用改。若同一叢集上跑多個模型，Body-Based Router會依請求body中的model欄位自動路由到對應模型池,不需要在應用程式裡寫任何路由邏輯；若是共享base model、掛載多個LoRA adapter，閘道會優先把請求導向已經載入該adapter的pod，避免昂貴的adapter swap延遲，若沒有pod已載入，則導向可用容量最多、能最快載入完成的pod。

📊 **三種真實場景下的benchmark：8B到235B模型**

團隊在p5.48xlarge（H100）與g5（A10G）機型上，針對8B到235B參數的四款模型做測試，流量都經過內部Application Load Balancer，貼近真實生產路徑，測試客戶端與模型伺服端各自運行在獨立node group以避免資源互相干擾，且全程使用閘道的預設路由設定，不做任何額外調校。三個場景分別呈現差異：混合GPU世代時，較小記憶體的機型會在round-robin下率先飽和，而其他機型明明還能負荷，閘道能即時偵測這種不均並調整；突發流量下，單一副本會在忙碌與閒置間反覆震盪，round-robin無法平滑這種延遲尖峰,閘道則能把請求導向有餘裕的pod；多輪對話、文件問答等共享prompt前綴的場景中，Prefix Cache Hit Rate評分器會把請求導向已經快取該前綴的pod，避免重複計算。

⚠️ **均勻叢集、穩定流量下,增益有限**

三個場景呈現一致的規律：叢集偏離「均勻」的程度越大，閘道帶來的增益就越明顯。反過來說，在完全均勻的GPU叢集、流量穩定的情況下，各副本的利用率本就接近一致,此時閘道的表現與round-robin相當——也就是說,這不是萬能的效能加速器,而是針對生產環境中真實常見的「異質硬體、突發流量、共享前綴」三種痛點設計的解法。目前Tier 1（單叢集路由）已在支援inference add-on的區域上線，Tier 2的跨叢集協調則是進一步擴充。

🎯 **實務啟示**

如果你的LLM推論叢集混雜著不同代的GPU、承受著突發流量，或工作負載中有大量共享prompt前綴（如多輪對話、RAG檢索）,這個addon值得一試——因為它不需要sidecar、不需要service mesh、也不需要改動應用程式碼，裝上去幾分鐘內就能觀察到首token延遲的變化，比起重新設計整套路由架構,風險與成本都低得多。

🔗 **來源**
- 標題：Introducing Amazon SageMaker HyperPod Inference Gateway
- 作者／機構：Vinay Arora
- 連結：https://aws.amazon.com/blogs/machine-learning/introducing-amazon-sagemaker-hyperpod-inference-gateway/

#AWS #SageMaker #Kubernetes #LLMInference #GPU #LoadBalancing #MLOps #EKS #InferenceOptimization #CloudComputing
