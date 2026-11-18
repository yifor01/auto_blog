---
title: Amazon SageMaker AI real-time endpoints now support KV cache aware routing
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-real-time-endpoints-now-support-kv-cache-aware-routing/
model: claude-code/sonnet
generated_at: '2026-11-18T23:42:37.690441'
score: 95
---

📌 KV 快取感知路由：讓多輪對話真正命中快取

TL;DR：Amazon SageMaker AI 新增 KV-aware routing，依實際快取狀態動態選擇實例，p50 首字延遲最高降 97%。

多輪對話、長系統提示詞、RAG 這類場景有個共同痛點：同一串 prompt 前綴反覆出現，但路由如果猜錯實例，GPU 就得把已經算過的東西再算一次。SageMaker AI 這次補上的 KV-aware routing，直接讓路由器「看見」每臺實例真正快取了什麼，而不是憑猜測行事。

🤔 Prefix-aware routing 的兩個盲點

SageMaker AI 先前推出的 prefix-aware routing，做法是把請求開頭的文字（到你設定的 PrefixLength 為止）做雜湊，再把開頭相同的請求導到同一臺實例。這個方法完全靠請求本身推測快取位置，看不到實例實際上快取了什麼，因此在兩種情況下會失準：一是實例的 GPU 記憶體滿了會淘汰舊的快取項目,但路由器並不知道,仍把相符的請求導去一個早已「冷掉」的實例；二是多輪對話剛開始時,每一輪都會讓對話變長,只要請求長度還沒超過 PrefixLength,每一輪雜湊出來的內容就不同,下一輪很可能被導到跟前面幾輪不同的實例,直到對話長度超過 PrefixLength 才會穩定落在同一臺機器上。

🧩 三個部件：回報、索引、路由決策

KV-aware routing 由三部分組成。首先，模型容器透過環境變數 SM_VLLM_KV_EVENTS_CONFIG 開啟事件回報，每次儲存或淘汰快取項目時都會發出一則 KV 快取事件。其次，SageMaker AI 用這些事件維護一份「管理式快取索引」，索引裡只存著單向、截斷過的雜湊值,對應到持有該內容的實例或推論元件副本——不會儲存 prompt 原文、token ID、請求內容或 KV 張量本身。第三，每個請求進來時,端點會先 tokenize prompt 並查詢索引,索引回傳哪些實例持有這段 prompt 的部分快取、持有多少,端點再綜合「快取命中長度」與「目前忙碌程度」挑選最合適的實例；如果命中最多的那臺正忙,就導去次佳且空閒的實例。由於索引是依 token 而非固定位元組數比對,多輪對話的歷史即使持續變長,仍能完整比對命中。

如果查詢速度太慢、沒有任何有用的比對結果,或所有候選實例都忙,請求會自動回退到 load-aware routing(等同 LEAST_OUTSTANDING_REQUESTS 策略),請求依然會被服務,只是少了快取命中的加速效果。索引也會隨機群變化：縮編時移除已下線實例的項目；擴編或更新置換實例時,新實例的快取是空的,短時間內延遲可能偏高。KV-aware routing 需要至少兩個實例(或兩個推論元件副本)才能發揮效果,單一實例時每個請求都只能去那一臺,這個設定就不起作用。

📊 Llama 3.1 70B 實測：p50 TTFT 最高降 97%

AWS 在七臺 ml.p5.48xlarge 實例上以 Llama 3.1 70B Instruct 做了 30 分鐘測試,模擬 20 或 100 位使用者進行多輪對話與文件問答,prompt 長度最高到約 64,000 tokens。在長 prompt、高負載的情境下,相較於隨機路由,KV-aware routing 把 p50 首字延遲(TTFT)最多降低 97%,吞吐量最高提升 234%,KV 快取命中率從 3–48% 提升到 80–93%。即便在較低負載下,長 prompt 依然有收益；短 prompt 因為本身可省下的 prefill 計算量較少,增益最小。

🎯 實務啟示

要啟用這個功能,只需兩步：在模型容器加上一個環境變數讓它回報快取內容,並在端點設定把 RoutingStrategy 設為 KV_AWARE,呼叫端的 API 完全不用改。對於已經在跑 prefix-aware routing、卻發現多輪對話前幾輪仍常常「冷啟動」或快取常態性被擠掉的團隊,這是一個不需要改動應用層程式碼就能直接升級路由精準度的選項；但記得它只在多實例、負載夠大、prompt 夠長時才有明顯優勢,流量很小或 prompt 很短的場景不必強求導入。

🔗 來源
- 標題：Amazon SageMaker AI real-time endpoints now support KV cache aware routing
- 作者／機構：Dmitry Soldatkin，AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-real-time-endpoints-now-support-kv-cache-aware-routing/

#AWS #SageMaker #LLMInference #KVCache #Routing #MLOps #GenerativeAI #vLLM #ModelServing #Latency
