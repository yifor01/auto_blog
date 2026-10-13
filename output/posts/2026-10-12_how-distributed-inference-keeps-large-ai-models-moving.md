---
title: How distributed inference keeps large AI models moving
source: IBM Research
url: https://research.ibm.com/blog/distributed-inference?utm_medium=rss&utm_source=rss
model: claude-code/sonnet
generated_at: '2026-10-13T00:02:06.039870'
score: 72
---

📌 LLM 推論也需要塔臺調度:IBM 拆解分散式推論六大關鍵技術

TL;DR:當 LLM 要同時服務上萬使用者與 AI agent,光把模型塞進 GPU 還不夠,你需要一層跨伺服器的流量調度機制。

一個模型伺服器把單次推論做得再快,碰到數千個並發請求、agent 突然爆發式呼叫工具再回來、長短任務混雜在一起的場景,照樣會塞車。IBM Research 用「塔臺調度飛機」比喻這個問題:機場不能把每架飛機都丟給第一條空跑道,得同時考慮位置、目的地、機體大小與油量。LLM 推論系統面對的,其實是同一類排程難題。

🤔 問題出在哪:vLLM、SGLang 管得好單機,管不了叢集

像 vLLM、SGLang 這類服務引擎,負責的是「在單一伺服器上有效率地跑模型」。但當請求量放大到需要一整個叢集的 model server,還需要一層更上層的協調角色:決定每個請求該被送到哪一臺伺服器、什麼時候送、要不要先排隊。這正是「分散式推論」(distributed inference)要解決的問題,IBM Research 以開源、Kubernetes-native 的 llm-d 框架為例,拆解了六項技術:prefix-cache-aware routing、KV-cache offloading、flow control、batch inference optimization、prefill/decode disaggregation,以及 wide expert parallelism。

🧩 核心機制:先問「快取在哪」,再問「誰有餘力」

**Prefix-cache-aware routing**:語言模型讀 prompt 時會把中間狀態存進 KV cache。如果下一個請求的開頭文字(例如系統提示、同一份程式碼庫、agent 的歷史步驟)跟之前重複,理論上可以直接重用快取,不必重新計算。但傳統負載平衡器只看「哪臺伺服器比較閒」,不管那臺伺服器有沒有相關快取,結果模型得重新讀一次早就算過的內容。llm-d 的 router 改成同時評分「哪臺伺服器已經持有最多這個 prompt 的 prefix」與「哪臺伺服器有餘力處理」,並提供近似索引與基於實際 token 資料的精確兩種實作方式。

**KV-cache offloading**:快取感知路由要有效,前提是快取還留在記憶體裡。但加速器(GPU)記憶體容量有限,長 prompt、多並發使用者、長時間的 agent session 很快就會把舊快取擠掉,一旦被擠掉,模型就得重新算一次,浪費運算資源。KV-cache offloading 的做法是把不是最急需的快取搬到較大但較慢的層級,例如 CPU 記憶體、本機 SSD 或共享檔案系統,並用一個快取索引追蹤「什麼存在哪」,讓路由層把 offload 出去的資料也納入決策。從 CPU 記憶體讀比從 GPU 記憶體讀慢,但遠比整段重新計算便宜。

素材中提到的 flow control、batch inference optimization、prefill/decode disaggregation、wide expert parallelism 四項,文章列出了名稱與角色定位(分別對應「決定什麼時候該動」「填滿閒置產能但不塞車」「把兩種不同性質的工作拆開處理」「把巨型模型攤開到整個叢集」),但這份摘要未進一步展開細節,此處不做延伸猜測。

📊 實測數據:97% 的可重用快取被抓到了

在 llm-d 團隊的一次示範中,prefix-aware routing 在測試工作負載中捕捉到 97% 的可重用快取機會;另一項示範裡,128 個並發請求下,GPU 記憶體就能供應約 90% 到 92% 的可重用 prefill prefix,CPU offloading 則負責撐住超出 GPU 容量的部分,並在一個長時間、agent 驅動的 benchmark 中維持高吞吐量與低首個 token 延遲。

💡 llm-d 的身世:從五家共同發起者到 CNCF Sandbox

llm-d 於 2025 年 5 月由 IBM Research、Red Hat、Google Cloud、NVIDIA、CoreWeave 共同發起,創始夥伴還包括 AMD、Cisco、Hugging Face、Intel、Lambda、Mistral AI,以及加州大學柏克萊分校與芝加哥大學的學術支持者。IBM Research、Red Hat、Google Cloud 目前仍持續主導其開發。2026 年 3 月,創始成員將 llm-d 捐贈給雲端原生計算基金會(CNCF)作為 sandbox 專案,目標是讓任何模型都能在任何加速器、任何雲端上部署推論堆疊。

🎯 實務啟示

如果你的團隊正在自建 LLM 推論服務,單機引擎選型(vLLM/SGLang)只解決了一半問題;當流量規模跨出單機,prefix-cache-aware routing 與 KV-cache offloading 這類「叢集層」的調度能力,才是決定吞吐量與延遲的關鍵,尤其是 agent 類工作負載因為反覆重用長上下文,從這類最佳化中受益特別明顯。

🔗 來源
- 標題:How distributed inference keeps large AI models moving
- 作者／機構:IBM Research
- 連結:https://research.ibm.com/blog/distributed-inference?utm_medium=rss&utm_source=rss

#LLMInference #DistributedSystems #KVCache #vLLM #SGLang #Kubernetes #MLOps #AIInfrastructure #IBMResearch #llm-d
