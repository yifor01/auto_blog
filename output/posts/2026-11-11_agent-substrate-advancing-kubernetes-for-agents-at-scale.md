---
title: 'Agent Substrate: Advancing Kubernetes for Agents at Scale'
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/agent-substrate-advancing-kubernetes-for-agents-at-scale/
model: claude-code/sonnet
generated_at: '2026-11-11T23:41:23.936939'
score: 107
---

📌 【NVIDIA】Agent Substrate捐贈CNCF，解Agent閒置資源之痛

TL;DR：NVIDIA將「Agent Substrate」捐給CNCF Sandbox，讓K8s能用10倍密度跑數百萬個agent。

Agent大部分時間都在「等」——等人類下指令、等工具回結果、等模型回應。但Kubernetes從來不是為「等待」設計的。

🤔 背景：Agent工作負載跟傳統服務不一樣

傳統web服務是少量長駐的instance；agent則是「醒來跑一步，然後等」的模式：跑一個shell指令、改一個檔案、呼叫測試、呼叫LLM，然後可能等幾毫秒也可能等幾分鐘才進到下一步。agent的狀態（檔案系統、行程、工作目錄）必須在步驟之間延續。

問題在於，在K8s上啟動一個compute Pod要經過API server、admission、etcd、scheduler、kubelet、image pull與網路設定，整個過程要花上數秒。這對跑數週的服務沒問題，但對一個要在百毫秒內出現、跑完10毫秒的bash指令就消失、每秒要重複數百次的sandbox而言太慢了。平臺團隊因此被迫二選一：幫每個agent保留一個warm Pod（幾乎全程閒置但仍要付費），或是隨需建立Pod（每一步都要付cold start的代價）。

🧩 Agent Substrate怎麼做

Agent Substrate用K8s來跑一個「ready pods」池，但在上面建了一個獨立的control plane，把大量的actor（agent與其執行環境）對應到這個較小的worker池。當某個actor閒置時，它會被從sandbox（gVisor或microVM）中snapshot出來，釋放worker；當它再被呼叫時，會被還原到任何一個空出來的worker上，記憶體與檔案系統狀態都完整保留。喚醒actor不需要再走一次API server、scheduler、kubelet，而是直接還原到既有的worker。worker pod本身仍是一般的K8s Pod，叢集排程、quota與placement政策照常適用。依NVIDIA所述，這套機制可讓單一worker池服務的agent密度達到標準容器的10倍。

📊 三類驅動需求的場景

- 程式碼助理與agent serving：coding agent在LLM呼叫與自己的環境（clone repo、改檔案、跑build/test）之間來回切換，使用者期待環境在每輪對話之間延續且能即時回應；要支援數千個這類session，不可能每個都配一個warm sandbox。
- RL post-training的agentic環境：具可驗證獎勵的RL要讓GPU trainer與generation server搭配一大群CPU密集的環境（code sandbox、compiler、瀏覽器、模擬器）。sandbox需求會隨rollout批次爆發，訓練規模可從早期的數百個sandbox成長到量產階段的數十萬個；最慢的環境決定trainer何時拿到下一批資料，這條路徑上的cold start會讓GPU閒置。
- 研究用GPU sandbox：研究者的coding agent有時需要GPU不是為了serve模型，而是編譯CUDA code、benchmark kernel或跑數值計算，用完就刪除sandbox。要在組織內支援這種模式，需要大量能快速啟動、公平共享有限GPU池的短命獨立GPU sandbox。

💡 已經上游的工作，以及接下來的方向

目前已公開在Agent Substrate repository中的進展包括：worker全滿時用request parking讓下一個請求排隊等待（而非直接回錯誤），並設上限避免無窮等待；透過K8s Dynamic Resource Allocation（DRA）讓每個container只申請自己需要的裝置，NVIDIA GPU是第一個支援的裝置類型；針對microVM sandbox導入per-container CPU／記憶體限制，避免失控的container拖垮整個sandbox；以及跨「暫停→喚醒」保留GPU sandbox狀態的設計——由裝置廠商描述如何安全暫停裝置、snapshot依賴哪些裝置屬性，Agent Substrate記錄這些屬性並嘗試還原到相符的裝置，若找不到則退回乾淨的cold start。

此外，NVIDIA Dynamo（開源的分散式推論框架）負責協調GPU上的推論排程，Agent Substrate負責管理agent在哪裡執行；兩者之間透過Dynamo router連結，讓agent在工具執行與模型呼叫之間切換時能同步協調延遲與可重用的context。

🎯 實務啟示

如果你的平臺正在為「每個session配一個warm Pod」或「每步cold start」兩難所苦，Agent Substrate提供了第三條路：用checkpoint／restore取代Pod的生生滅滅。對正在做RL post-training或大規模coding agent serving的團隊，這類「control plane疊加在K8s之上」的設計值得納入架構評估，尤其是它仍相容標準的K8s排程與quota機制。

🔗 來源
- 標題：Agent Substrate: Advancing Kubernetes for Agents at Scale
- 作者／機構：Ekin Karabulut, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/agent-substrate-advancing-kubernetes-for-agents-at-scale/

#AgentSubstrate #Kubernetes #CNCF #NVIDIA #AIAgents #ReinforcementLearning #CloudNative #MLOps #GPUComputing #NVIDIADynamo
