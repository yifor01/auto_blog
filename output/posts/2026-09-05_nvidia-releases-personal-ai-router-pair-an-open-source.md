---
title: 'NVIDIA Releases Personal AI Router (PAIR): An Open Source Virtual Inference
  Router that Distributes Local AI Requests Across RTX, DGX Spark, and Mac Nodes'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/04/nvidia-releases-personal-ai-router-pair-an-open-source-virtual-inference-router-that-distributes-local-ai-requests-across-rtx-dgx-spark-and-mac-nodes/
model: claude-code/sonnet
generated_at: '2026-09-05T19:14:22.664496'
score: 89
---

📌 【NVIDIA 開源新工具】PAIR：讓 RTX、DGX Spark、Mac 一起分攤本地推理負載

TL;DR：NVIDIA 開源虛擬推理路由器 PAIR，自動把多 agent 併發請求分派到區域網路內的多臺裝置執行。

一個 agent 派工作，瞬間變成幾十個模型呼叫，全部擠在同一張顯卡的佇列裡排隊，隔壁桌那臺睡著的工作站卻完全沒被叫醒。這正是 NVIDIA 這次要解決的問題。

🤔 多 agent 工作流，把單機推理擠爆

Lead agent 拆解任務、派生 subagent 已經是常態，一個使用者請求瞬間變成數十個獨立的模型呼叫。如果這些呼叫全部打向同一個本地推理引擎，它們會競爭同一批執行槽位，佇列越排越長，而同一個區網裡的另一臺工作站、筆電或 DGX Spark 卻可能完全閒置。NVIDIA Personal AI Router（PAIR）瞄準的就是這個瓶頸。

🧩 不是新引擎，是一層路由代理

PAIR 本身不執行模型推理，Ollama 或 LM Studio 仍在被選中的節點上跑模型。它的角色是虛擬推理路由器：透過 mDNS 自動探索區網內相容的機器，並把獨立的推理請求排程到不同節點上執行。

最關鍵的設計決定，是 PAIR 沒有另外發明一套叢集 API，而是直接代理 agent 工具鏈原本就在說的 Ollama 相容介面與 LM Studio 相容介面，接管這兩個引擎預設使用的埠號（若工具監聽在別的埠，也可以在 PAIR 的引擎設定裡調整代理埠）。GitHub 上的原始碼也額外提供 OpenAI 相容的代理端點。這意味著現有的 agent 工具鏈幾乎不需要修改：agent 決定要做什麼，PAIR 決定在哪裡做。

節點配對透過 mDNS 自動探索，探索失敗時可用 IP 手動加入。信任建立方式是邀請端機器顯示六位數 PIN，受邀端輸入確認，配對完成前所有節點間通訊都被封鎖；配對完成後，節點間流量以產生的憑證透過 mTLS 加密。每個節點各自跑 Ollama 或 LM Studio，PAIR 甚至可以在已配對的機器上安裝引擎、啟動模型下載，省下大部分跨機器設定工作。一個節點只有在所需引擎已啟用、且要求的模型確實存在時才會被視為可用，叢集內各節點的模型不必一致，PAIR 會依模型所在位置路由；同一個 tag 在越多節點上載入，可用的節點池就越大。

排程器在每次請求時會評估五個訊號：節點是否在線且就緒、對應引擎是否啟用、所需模型是否存在、該節點與引擎目前的工作負載、以及目前的 GPU 使用率。要注意的是，這是「工作負載層級」的併發分配，邊界很明確：PAIR 把每個請求指派給單一節點，並在該請求的生命週期內固定在那裡，它不會把多張顯卡的 VRAM 合併成一個更大的加速器，也不會把單一請求切分到多臺機器上執行。

📊 三機分工，平均時間打對折

NVIDIA 的示範把 PAIR 搭配 Hermes Desktop，對一個合成的家庭信箱建立五個 subagent 的工作流，由 Ollama 在每個被選中的節點上執行 Qwen 3.6 35B A3B。單靠一臺 RTX Spark 筆電執行，平均耗時 18 分鐘；換成由 RTX Spark 筆電、DGX Spark、RTX 5090 組成的三機 PAIR 叢集後，平均耗時降到 8 分 48 秒。

⚠️ 部署門檻與限制

PAIR 目前以 v0.1.1 公開 beta 形式提供 Windows、macOS、Linux 的簽名安裝檔，原始碼在 GitHub 上以 Apache 2.0 授權釋出。它完全在本地網路運作，只有下載模型時才需要連上網際網路。支援硬體包含 GeForce RTX 20 系列以上、Turing 世代以後的 RTX PRO 工作站顯卡、DGX Spark，以及 Apple M4 或更新的晶片；Windows、Linux、macOS 節點可以互相配對，涵蓋 x64 與 arm64 架構，不過 Windows on ARM 仍屬實驗性支援。官方驗證的最低配置是 8GB 記憶體、建議 20GB 硬碟空間，其他 Linux 發行版則需要自行從原始碼建置。

🎯 實務啟示

對已經在用 Ollama、LM Studio 起多 agent 工作流的工程師來說，PAIR 的吸引力在於「零改動」：它接管的是既有引擎的相容埠，而不是要求你換一套 API。如果家裡或辦公室已經有閒置的顯卡、Mac 或 DGX Spark，這是一個幾乎零成本把它們拉進推理叢集分攤佇列壓力的方式。但也要認清它的邊界，這是任務級的負載平衡，不是分散式推理，單一巨大請求或需要超大 VRAM 的模型不會因此被「切開」執行。

🔗 來源
- 標題：NVIDIA Releases Personal AI Router (PAIR): An Open Source Virtual Inference Router that Distributes Local AI Requests Across RTX, DGX Spark, and Mac Nodes
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/04/nvidia-releases-personal-ai-router-pair-an-open-source-virtual-inference-router-that-distributes-local-ai-requests-across-rtx-dgx-spark-and-mac-nodes/

#NVIDIA #PAIR #LocalInference #Ollama #LMStudio #DGXSpark #MultiAgent #EdgeAI #OpenSource #InferenceRouting
