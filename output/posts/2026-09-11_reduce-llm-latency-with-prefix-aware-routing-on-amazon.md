---
title: Reduce LLM latency with prefix-aware routing on Amazon SageMaker Inference
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/reduce-llm-latency-with-prefix-aware-routing-on-amazon-sagemaker-inference/
model: claude-code/sonnet
generated_at: '2026-09-11T19:49:49.472478'
score: 101
---

📌 同一句開場白算了幾千次？SageMaker 用 prefix-aware routing 治好 KV cache 失效

TL;DR：Amazon SageMaker Inference 新增 prefix-aware routing，讓相同 prompt 前綴穩定落在同一臺實例上，TTFT 最高降 77%。

一個客服機器人，每次請求前面都掛著同一段 3,000 token 的政策說明，後面才接使用者真正輸入的 50 個字。vLLM、TensorRT-LLM 這類推論框架早就有 prefix caching 可以快取這段重複的計算，但只要背後是多臺實例組成的 endpoint，隨機路由就會把同樣的前綴這次丟給 A 機、下次丟給 B 機，快取永遠建不起來。

🤔 **Prefix caching 有效，但路由層扯了後腿**

問題不在快取機制本身，而在路由策略。當請求被隨機分散到整個機器叢集，任何單一實例都看不到足夠多次相同前綴的重複請求，KV cache 自然無法穩定命中。

🧩 **讓相同開頭的請求固定走同一臺機器**

Amazon SageMaker Inference 這次推出的 PREFIX_AWARE 路由策略，會檢視每個請求的開頭內容，並把有相同開頭的請求一致地導向同一臺實例，讓那臺機器上的 KV cache 真正被重複使用，開發者不需要自己替請求打標籤或管理 affinity。

這個機制內建兩個保護機制：

- **過載保護**：如果某個前綴太熱門、目標實例已達設定的併發上限，請求會改路由到較不忙碌的實例，犧牲這一次的快取命中換取穩定性。
- **擴縮容時的穩定行為**：新增或移除實例時，多數請求仍會繼續走向原本的實例，只有一小部分流量因為叢集變動而重新分配，快取不會因為擴縮容整批失效。

連同這次新增的 PREFIX_AWARE，SageMaker Inference 的即時 endpoint 現在提供三種路由策略：RANDOM（預設，適合請求彼此無關的通用工作負載）、LEAST_OUTSTANDING_REQUESTS（依在途請求數平均分配，適合處理時間差異大的情境），以及新推出的 PREFIX_AWARE（適合 LLM 工作負載、且序列框架已啟用 prefix caching 的情境）。策略是針對 production variant 設定的，可以透過更新 endpoint 設定直接切換，不需要重新部署模型。

📊 **Llama 3.1 70B 上的實測結果**

以 Llama 3.1 70B Instruct、7 臺 ml.p5.48xlarge、啟用 prefix caching 的 vLLM 進行基準測試，涵蓋單模型 endpoint、inference component endpoint、原生 Invoke API 與 OpenAI 相容 API 共 16 種測試組合，全數以 100% 成功率完成：

| 指標 | 表現 |
|---|---|
| P50 TTFT | 最高降低 77% |
| 吞吐量 | 最高提升 16% |
| KV cache 命中率 | 約 25% 提升到 80% 以上 |
| 路由額外開銷 | 每請求 1.3–1.9 毫秒 |
| 測試中 TTFT 範圍 | 63–280 毫秒 |
| 7 臺實例流量分配 | 每臺 13.3%–15.4%，與理想均分相差在 1% 以內 |

共享前綴越長，效益越明顯：長 context 的工作負載因為有更多計算可以被略過，受益最大；短 context 工作負載也有幫助，只是單次節省的比例相對較小。路由本身帶來的延遲增加微乎其微，且各實例間的流量分配依然均衡，沒有出現熱點。

啟用時只需設定兩個參數：`PrefixLength`（1024–65536，原生 Invoke API 以 request body 的位元組數計算，OpenAI 相容 API 則以擷取出的訊息文字字元數計算，需涵蓋共享前綴再加上足以區分不同工作負載的獨特內容）與 `ConcurrencyThreshold`（1–1024，目標實例的最大在途請求數，超過就觸發過載保護）。模型容器與服務框架完全不需要修改，`InvokeEndpoint`、`InvokeEndpointWithResponseStream` 以及 OpenAI 相容的 Chat Completion API 呼叫方式都維持不變；若不同租戶共用同一份指令但想讓快取情境彼此獨立，原生 API 可設定 `X-Amzn-SageMaker-Prefix-Aware-Id` header，OpenAI API 則可帶入 `prompt_cache_key` 欄位。

🎯 **實務啟示**

RAG 應用（多個使用者針對同一份文件提問）、多輪對話（每輪都帶著完整歷史紀錄）、有長結構化指令的機器人，以及同一檔案內的程式碼補全，都是共享前綴的典型場景。如果你的 LLM 服務已經啟用 prefix caching 卻感覺不到效果，很可能問題出在路由層而非快取機制本身，值得直接把 endpoint 設定切到 PREFIX_AWARE 測試看看。

🔗 **來源**
- 標題：Reduce LLM latency with prefix-aware routing on Amazon SageMaker Inference
- 作者／機構：Kareem Syed-Mohammed
- 連結：https://aws.amazon.com/blogs/machine-learning/reduce-llm-latency-with-prefix-aware-routing-on-amazon-sagemaker-inference/

#AmazonSageMaker #LLMInference #KVCache #PrefixCaching #vLLM #AWS #MLOps #LatencyOptimization #RAG #LLMServing
