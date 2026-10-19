---
title: Push-based KV transfer to improve TTFT and TPOT for disaggregated inference
  in vLLM
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/push-based-kv-transfer-to-improve-ttft-and-tpot-for-disaggregated-inference-in-vllm/
model: claude-code/sonnet
generated_at: '2026-10-19T21:43:44.773240'
score: 91
---

📌 【AWS】vLLM 換個傳輸方向，TTFT 快上 3 倍

TL;DR：AWS 貢獻給 vLLM 的 push 式 KV 傳輸，把 prefill/decode 分離架構下的首字延遲砍掉一大截。

同一套 RDMA 硬體、同一套 NIXL 傳輸函式庫，光是把「誰主動發起傳輸」這件事反過來，就讓首個 token 的生成時間縮短到原本的三分之一——這正是 AWS 這篇文章要講的 push 式 KV 傳輸。

🤔 **Prefill/decode 分離之後，KV cache 怎麼搬是關鍵**

LLM 推論分成兩個階段：prefill 處理輸入 prompt 並建立 KV cache，decode 則用這份 cache 逐一生成輸出 token。這兩階段的運算、記憶體與擴展特性都不同，因此 prefill-decode（P-D）分離架構會把它們放到不同的 engine 實例上各自擴展。但這麼做也必須先把 KV cache 從 prefill 實例搬到 decode 實例,之後才能開始生成 token，所以傳輸效率直接決定了 time-to-first-token（TTFT）。

vLLM 其中一種搬運方式是透過 NVIDIA Inference Xfer Library（NIXL）connector，在支援 RDMA 的互連（例如 AWS EFA）上搬運 KV block。在支援的機型上，EFA 支援 GPUDirect RDMA 與 Neuron Direct RDMA，讓 NIXL 可以直接在 GPU 或 AWS Trainium 裝置記憶體之間傳輸，不需要先經過主機記憶體。NIXL connector 預設是 pull 模式：prefill 算完 KV cache 後，router 把來源 metadata（包含 prefill 的 block ID）轉交給 decode 實例，decode 實例才配置目的地 block、準備傳輸，再發出 NIXL READ 去拉取資料。這些協調與準備步驟都排在 prefill 完成之後、decode 開始之前依序執行，因此會拉長 TTFT 的關鍵路徑。

🧩 **Push 模式：把準備工作挪到 prefill 進行的同時**

這篇文章介紹的 push 式 NIXL connector，把 prefill 完成後的傳輸協調與準備工作，挪出 TTFT 的關鍵路徑之外。整個協定分三個邏輯步驟：

- **註冊（decode 端）**：decode 實例一旦為某個請求配置好本地 block，就會在同一個 engine step 內，把自己的身分與剛保留好的 block 位置，透過 NIXL notification 傳給 prefill 實例。因為註冊發生在配置當下，connector 在 prefill 完成前就已經知道目的地在哪。
- **交會（prefill 端）**：來自 decode 的註冊與 prefill 本身的完成，可能以任何順序到達，connector 兩種情況都處理得了——誰先到就先等對方,誰後到就觸發傳輸。Connector 依請求 ID 配對,也能正確處理被搶佔或重試的請求。
- **傳輸（prefill 端）**：請求配對成功後，prefill 端會建立（或沿用）跟 decode 端的連線，發出 NIXL WRITE，把 KV block 直接寫進 decode 端已註冊的記憶體裡，並對應到每個目的地的 tensor-parallel rank。兩端可以使用不同的內部 block 排列方式與 block 大小，傳輸時各自做映射。每次 WRITE 都會帶一個完成通知，decode 端要收齊所有預期的通知（每個寫入它的 producer rank 各一個）才會判定 KV 已經收到，進而開始 decode。

這套設計還搭配了一個獨立的背景傳輸執行緒：decode 端的主迴圈負責配置並註冊目的地 block，prefill 端的主迴圈則計算 prompt KV cache，兩者都備妥後，prefill 主迴圈把 KV block 交給背景執行緒處理,自己立刻回去跑模型。背景執行緒負責建立/沿用 NIXL 連線、把 block ID 映射成記憶體描述子、合併相鄰 block 成較大的傳輸區塊，再送出 NIXL WRITE。把這些描述子準備與傳輸送出的工作搬出延遲敏感的主迴圈，是避免拖慢模型執行的關鍵。

兩種模式也有路由上的取捨：pull 模式讓 router 可以等 prefill 完成後再選擇 decode 實例，對負載感知路由與服務品質管理更靈活；push 模式則得提早選定 decode 實例,好讓目的地準備工作能跟 prefill 同時進行，換來的是在相近負載下，prefill 實例可以更早釋放它的 KV block,因為一旦 prompt KV 與目的地註冊都就緒,傳輸就會立刻開始。

📊 **1P1D 實測：TTFT 最高快 3 倍，TPOT 最高快 3 成**

AWS 在以 EFA 連接的 Amazon EC2 P5en 實例上，用 1P1D 部署與 Qwen3-32B 模型做 benchmark，push 模式相較 pull 模式，TTFT 最高快上 3 倍，TPOT（每輸出 token 時間）最高改善 30%，尤其在高請求率下效果更明顯。這套功能最初是在以 EFA 連接的 AWS Trainium 實例叢集上建置與驗證，之後以不綁定特定加速器的方式貢獻回 vLLM，而這次在 EC2 P5en（GPU）叢集上的結果顯示,效益同樣延伸到了 GPU 平臺。文章也特別說明,實際效果會因 workload 與設定不同而有差異。

🎯 **實務啟示**

如果你的服務是以 P-D 分離架構跑 vLLM，而且在高請求率下對 TTFT/TPOT 敏感，push 模式值得評估；但要留意它提早鎖定 decode 實例的路由取捨，可能和你原本依賴 pull 模式做負載感知路由的設計有所衝突。

🔗 **來源**
- 標題：Push-based KV transfer to improve TTFT and TPOT for disaggregated inference in vLLM
- 作者／機構：Sunita Nadampalli, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/push-based-kv-transfer-to-improve-ttft-and-tpot-for-disaggregated-inference-in-vllm/

#vLLM #LLMInference #KVCache #AWS #EFA #NIXL #Disaggregation #Trainium #TTFT #InferenceOptimization
