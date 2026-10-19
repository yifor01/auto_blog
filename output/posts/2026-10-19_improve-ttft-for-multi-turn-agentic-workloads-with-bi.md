---
title: Improve TTFT for multi-turn agentic workloads with bi-directional KV transfer
  in vLLM
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/improve-ttft-for-multi-turn-agentic-workloads-with-bi-directional-kv-transfer-in-vllm/
model: claude-code/sonnet
generated_at: '2026-10-19T21:38:29.313153'
score: 106
---

📌 多輪對話 Agent 的 TTFT 瓶頸：vLLM 雙向 KV Transfer 怎麼解

TL;DR：讓 decode 節點把 KV cache「送回」prefill 節點,多輪 Agent 對話的首token延遲最多降 3.3 倍。

每多一輪對話,Agent 就要把完整歷史重新丟給模型處理一次——這聽起來很浪費,而 AWS 的做法是讓已經算過的 KV cache 別再算第二次。

🤔 **單向 KV 傳輸,在多輪對話裡白白浪費兩次**

多輪 Agentic 工作流程會不斷累積 context：Agent 推理、呼叫工具、整合先前結果,每一輪客戶端都要重送完整對話歷史（系統指令、先前 prompt、工具結果、模型回覆),讓這段持續增長的 context 被重複處理。

在 Prefill-Decode（P-D）分離式架構中,請求會被拆到兩種專職節點：prefill 節點處理 prompt 並建立 KV cache,decode 節點取用這些 KV blocks 來生成回應。但傳統分離式服務只支援單向傳輸,KV cache 只能從 prefill 流向 decode,這對多輪對話造成兩個問題：第一,decode 節點生成回應後,手上同時握有 prompt 與新生成 token 的 KV cache,但下一輪開始時 prefill 節點完全拿不到這些內容,必須重新計算前一輪回應 token 的 KV 投影;第二,只有 decode 節點維護 session 狀態,prefill 節點沒有,導致活躍 session 在 prefill 端更容易被 cache 驅逐——一旦完全 cache miss,prefill 節點就要把整段對話歷史（包含系統指令、過去所有使用者請求、工具結果、模型回覆)全部重新算一次。隨著對話變長,這些重複運算會持續吃掉加速器算力,拉長 time to first token（TTFT）。

🧩 **讓 KV cache 也能「反向」從 decode 流回 prefill**

雙向 KV cache 傳輸的核心概念,是讓 decode 節點在後續輪次把先前算好的 KV 回傳給 prefill 節點,避免共用的 context 被重複計算,並由一個可配置的 KV recompute 門檻值來決定何時觸發回傳。

實作上,團隊擴展了 NVIDIA Inference Xfer Library（NIXL)的 KV connector,讓 prefill 節點也能消費遠端 KV blocks（如同 decode 節點原本消費 prefill 提供的 blocks 一樣)。這並非小改動,因為兩種節點架構本質不同：prefill 節點負責計算新 prompt token 的 KV 表示,能提供完整的 prompt KV blocks;decode 節點沒有能力（或效率)生成完整 KV 表示,只能提供先前已快取的 KV blocks。因此 prefill 與 decode 各自維持自己的角色與 metadata 計算邏輯,但底層實際的 KV 傳輸機制（一次 NIXL READ)對 P→D 與 D→P 兩個方向是共用的。

整套流程可以拆成以下步驟：
1. 路由將請求送到 prefill 節點,prefill 計算 prompt KV 並回傳 block metadata
2. 路由將請求與 metadata 轉給 decode 節點,執行標準 P→D NIXL READ（這是既有流程)
3. decode 節點生成完成後,保留符合條件的 KV blocks,而不是立刻釋放
4. decode 節點在串流回應中回傳這些 block 的 metadata
5. 路由把這份 metadata 快取下來,供下一輪 prefill 請求使用
6. 下一輪請求到來時,prefill 節點先套用本地 cache 命中,再檢查遠端可重用的 KV
7. 當可重用 token 數達到門檻,prefill 排入一次非同步接收,執行 D→P NIXL READ,再只計算剩餘的新增部分

協調這整套流程需要一個具備 KV-cache 感知能力的路由：它是客戶端、prefill、decode 之間一個輕量、有狀態的控制平面,維護一份從客戶端提供的 conversation_id 到 decode 端 kv_transfer_params 的記憶體內映射,只儲存 block 位置的 metadata,而非 KV 張量本身,且這份 metadata 是從回應串流中取得,不需要另外查詢 decode 節點。第一輪對話時 cache 查詢會 miss,走標準 P→D 流程,路由同時從回應串流中存下 decode 的 metadata;後續輪次路由用 conversation_id 取出 metadata,讓 prefill 重用 decode 端的 KV,生成完成後再更新 metadata 供下一輪使用。

decode 節點平常在生成完成後會立刻釋放請求的 blocks,但在雙向傳輸模式下,會依照可配置的存活時間（decoder_kv_blocks_ttl,預設 480 秒)保留這些 blocks,並公開其位置與到期時間。只要下一輪對話在 TTL 到期前抵達,prefill 就能重用這份 KV;超過時限則退回標準 prefill 流程。由於這個 TTL 是固定值、不會被續期,部署時需要依照預期的輪次間隔來調整,以平衡 KV 重用效益與加速器記憶體佔用。

另外,KV 重用不保證永遠比本地重算快——如果可重用的 prefix 很短,跨節點互連與協調的額外開銷甚至可能超過直接重算的時間。這由 kv_recompute_threshold 這個設定值控制,預設為 64 tokens：待計算的 token 數低於門檻就本地重算,達到或超過門檻才向 decode 節點拉取 KV,實務上需依模型運算時間、KV 大小與互連效能來調整。

📊 **在 EC2 P5en 上實測：TTFT 最高降 3.3 倍**

團隊在使用 AWS EFA（低延遲 RDMA 網路)互連的 Amazon EC2 P5en 實例上,以 1P1D 部署架構分別測試 Qwen3-32B 與 zai-org/GLM-5-FP8 兩個模型的多輪對話。結果顯示雙向 KV 傳輸讓 TTFT 最多降低 1.6 倍（Qwen3-32B)與 3.3 倍（GLM-5-FP8),文中強調實際結果會因工作負載與配置而有差異。這套機制最初是在用 EFA 互連的 AWS Trainium 實例叢集上開發與驗證,並以加速器無關（accelerator-agnostic)的形式貢獻回 vLLM,文中展示的 GPU 實測結果證明同樣的效益也能延伸到 GPU 平臺。EFA 支援 GPUDirect RDMA 與 Neuron Direct RDMA,可以讓 KV blocks 直接在 prefill 與 decode 節點的 GPU 或 Trainium 裝置記憶體之間搬移。

⚠️ **下一步：讓 decode 端的釋放時機更聰明**

目前 TTL 是固定計時,團隊提到一個自然的改進方向是把心跳續期（heartbeat-renewed)租約機制延伸到 decode 端,讓 decode 節點能在對話真正閒置時就回收 blocks,而不是死等固定計時器到期。

🎯 **實務啟示**

vLLM 已經內建 connector 端的雙向 KV 傳輸支援,vLLM GitHub 也提供了範例 proxy 可供改寫成自己的路由邏輯。如果你的服務是多輪 Agent 對話、且用的是 P-D 分離式部署,這套機制值得評估——特別要記得依照自己的對話節奏去調整 decoder_kv_blocks_ttl 與 kv_recompute_threshold 兩個參數,否則可能拿不到預期的 TTFT 改善,甚至因為短 prefix 重用而得不償失。

🔗 **來源**
- 標題：Improve TTFT for multi-turn agentic workloads with bi-directional KV transfer in vLLM
- 作者：Sunita Nadampalli @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/improve-ttft-for-multi-turn-agentic-workloads-with-bi-directional-kv-transfer-in-vllm/

#vLLM #KVCache #LLMInference #AIAgents #AWS #Trainium #GPU #TTFT #InferenceOptimization #MultiTurnConversation
