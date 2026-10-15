---
title: Scale Agentic Coding Workflows with Meta’s Muse Spark Open on NVIDIA GB300
  NVL72
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/scale-agentic-coding-workflows-with-metas-muse-spark-open-on-nvidia-gb300-nvl72/
model: claude-code/sonnet
generated_at: '2026-10-15T20:37:52.405368'
score: 100
---

📌 Meta與NVIDIA聯手:816B程式碼agent模型如何榨乾GB300 NVL72

TL;DR:Meta Muse Spark Open用NVFP4,在GB300 NVL72上衝出單GPU每秒5萬token。

一般的程式碼補全模型只需要處理單次、範圍明確的任務,比如寫一個函式或補一個單元測試。但當agent要做跨檔案重構、在數千個檔案間導航、從失敗的測試中恢復,context window與推理架構就必須徹底不同,這正是Meta Muse Spark Open要解決的問題。

🤔 一般coding模型解決不了的事
一般coding模型針對single-shot completion做最佳化(生成函式、寫單元測試、建議inline修正),擅長處理context小、答案立即出現的離散任務。但agentic coding需要的是能規劃多檔案重構、在數千個檔案間導航、從失敗測試中恢復、並協調subagent的長程、多步驟工作,這對模型提出完全不同的要求。

🧩 816B參數MoE,專為agentic coding打造
Meta推出的Muse Spark Open是一個針對coding最佳化的816B參數mixture-of-experts(MoE)模型,每個token僅啟動42B活躍參數,搭配1M token的context window。它在NVIDIA GB300 NVL72 Blackwell Ultra上訓練,專門針對agentic coding工作流程設計,目標是提升first-attempt準確率、讓tool calling更可靠,並對跨repository的程式碼有更深入的理解。

模型會plan、act、observe、self-correct,支援搭配tool use、輸出評估與迭代修正的多步驟任務執行。它用goal conditioning維持任務方向,並用context compaction在長時間運行的session中保留所需知識。1M token的context window可以容納一整個專案,包括複雜的依賴關係、legacy code與數千個檔案,不需要把任務拆成片段處理。

除了coding,Muse Spark Open還能搜尋網路(包括多模態瀏覽)、為可拆解的任務生成並協調subagent,並具備跨desktop、mobile、browser統一的computer use能力。它會在每個動作前產生獨立的說明文字,讓開發者知道agent正在做什麼、為什麼這麼做。

它的1.8B感知編碼器(perception encoder)能原生處理交錯(interleaved)的文字、圖片、影片畫面與音訊,不需要為每種模態分別建立pipeline,讓模型在單一、統一的推理過程中同時處理所看到、聽到、讀到的內容,這適合涵蓋截圖、圖表、錯誤日誌、影片演示的開發者工作流程。

Sparse MoE路由讓每個token只啟動816B總參數中的42B,透過256個專家中的top-8路由實現,用遠低於同等規模密集模型的服務成本,換取frontier級的agentic能力。

📊 GB300 NVL72上的實測吞吐量
NVFP4是Meta生成、針對NVIDIA Blackwell Ultra最佳化的checkpoint格式,搭配原生FP4 Tensor Core加速,縮小了816B參數的記憶體佔用。每個token搬運的byte數變少,提升了每位使用者的每秒token數;省下的記憶體則能支撐更大的KV cache,讓更多並發的長context session同時運行,帶來更高吞吐量與更低的每token成本。

GB300 NVL72採用rack-scale架構,把72張NVIDIA Blackwell Ultra GPU整合進單一平臺,其NVLink domain讓GPU間通訊達到130 TB/s,消除了專家(expert)流量需要跨越傳統網路架構時產生的瓶頸。對於像Muse Spark Open這種把每個token路由到256個專家中8個的sparse MoE模型來說,這個頻寬直接決定了部署能實現多少理論吞吐量。

在GB300 NVL72上開箱執行agentic workload,Muse Spark Open每GPU可達最高每秒5萬token,每位使用者最高每秒600個token。在四張NVIDIA Blackwell GPU、搭配speculative decode的測試中,同樣實現了每GPU超過5萬token/秒、每位使用者超過600 token/秒的成績,讓AI工廠能以高吞吐量、低延遲的方式在production環境運行大參數模型。

💡 MoE大規模部署的真正瓶頸是頻寬
這個案例說明了sparse MoE模型在大規模部署時,瓶頸往往不是算力,而是GPU之間的通訊頻寬,當token要動態路由到不同專家,專家之間的流量如果必須跨越一般的網路架構,效能很容易被打回原形。GB300 NVL72把72張GPU納入同一個NVLink domain,某種程度上是針對MoE架構量身打造的硬體答案,這也是為什麼官方特別強調頻寬對吞吐量的直接影響。

🎯 實務啟示
NVIDIA為Muse Spark Open提供多種部署路徑:SGLang、vLLM與TensorRT LLM可以直接控制serving設定、平行化方式與batching,TensorRT LLM還額外提供針對NVIDIA GPU調校過的編譯引擎。NVIDIA Dynamo則發布了三者的部署recipe,把prefill與decode分離到各自專屬的GPU池,避免運算密集的prompt處理拖慢token生成速度;其KV cache-aware路由會把請求導向已經持有相關prefix的worker,避免長agentic session中context累積時重複運算。

想針對特定領域微調的團隊,可以用NVIDIA NeMo AutoModel這個PyTorch原生訓練函式庫,它原生支援Hugging Face checkpoint、不需要模型轉換,開箱就能做完整SFT與LoRA微調;要進入大規模生產訓練時,則可以用NVIDIA Megatron Bridge把Hugging Face checkpoint轉換成Megatron格式。現在可以直接從Hugging Face下載Muse Spark Open的NVFP4權重;若要正式上線,NVIDIA NIM把整個設置流程壓縮成一道指令,容器會自動依偵測到的硬體挑選最適合的serving後端與精度。

🔗 來源
- 標題:Scale Agentic Coding Workflows with Meta's Muse Spark Open on NVIDIA GB300 NVL72
- 作者/機構:Tanya Lenz, NVIDIA Developer
- 連結:https://developer.nvidia.com/blog/scale-agentic-coding-workflows-with-metas-muse-spark-open-on-nvidia-gb300-nvl72/

#NVIDIA #Meta #MoE #AgenticCoding #GB300 #BlackwellUltra #NVFP4 #LLM #AIInfrastructure #MachineLearning
