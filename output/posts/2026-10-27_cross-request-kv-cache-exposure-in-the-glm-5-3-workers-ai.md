---
title: Cross-request KV cache exposure in the GLM-5.3 Workers AI model (155 responses)
source: Hacker News
url: https://blog.cloudflare.com/kv-cache-exposure-remediation/
model: claude-code/sonnet
generated_at: '2026-10-27T21:30:02.899566'
score: 99
---

📌 Cloudflare 復盤：GLM-5.3 跨租戶 KV cache 洩漏事故

TL;DR：長 prompt 踩中配置誤差加 SGLang bug，155 筆回應混進了別人的資料。

一個模型配置上的數字不一致，加上一個推理引擎裡「本該報錯卻沒報錯」的路徑，組合起來讓不同客戶的對話內容,出現在了別人的回應裡。Cloudflare 近日公開了這起事故的完整技術復盤。

🤔 **事發經過：8 月 27 日到 9 月 9 日的時間窗**

9 月 8 日，安全研究者 Gadi Evron（來自 Knostic）透過 Cloudflare 的 HackerOne 計畫回報:發給 Workers AI 上的 `@cf/zai-org/glm-5.3`（Z.ai 推出、專為 agentic coding 工作流設計的文字生成模型）的超長 prompt，有時會回傳屬於其他使用者 session 的文字。Cloudflare 隔天上午就重現了問題,並在宣布事故後 40 分鐘內將模型下線。確認問題、部署修正後的配置與修補過的推理引擎,同一天就恢復了服務。

事後統計，問題影響時間是 8 月 27 日到 9 月 9 日，期間只有少數客戶受到影響，總共 155 筆回應受到波及,全部都是發生在長度超過 681,280 token 的 prompt 上。排除 Cloudflare 自己的測試與研究者的測試後，剩下的受影響請求在時間與量級上,符合一般長 context 使用情境,而非有人重複利用這個漏洞,Cloudflare 表示沒有發現任何蓄意利用的證據。已確認 Workers AI 上其他模型都沒有受影響,這份報告也與開源推理引擎 SGLang 的對應說明同步發布,屬於協同揭露。

🧩 **兩個問題疊在一起才會出事**

Workers AI 用 SGLang 以 disaggregated（分離式）架構服務 GLM 5.3:一組 prefill GPU 負責處理 prompt 並生成 KV cache，再透過 RDMA（經由 Mooncake）把 cache 交給一組 decode GPU 負責生成回應。KV cache 本身是 GPU 記憶體裡一塊固定大小分頁的共享池,每個請求被分配到分頁後使用,結束後釋放,但分頁之間不會清零——下一個拿到該分頁的請求,就直接覆寫上去。這是推理引擎追求效能的常見做法,但也意味著分頁的「誰擁有、何時該釋放」完全要靠引擎自己追蹤,而且這個池的大小不是寫在配置檔裡的固定值,是 SGLang 在啟動時,用載完模型權重後剩下的 GPU 記憶體動態算出來的,跟模型宣告的 context length 是兩個完全獨立的數字,沒有任何機制強制兩者一致。

**問題一,配置不一致**:Cloudflare 把 GLM 5.3 部署成 1,048,576 token 的 context window，但 prefill GPU 上的 KV cache 池實際只有 681,280 token 的容量。團隊其實在上線前就知道這個落差，原本預期引擎在處理不了的 prompt 上會回傳錯誤,而長 context 測試時觀察到的是成功的 HTTP 狀態碼與沒有錯誤訊框的串流回應,所以沒把它當成問題。這是測試上的關鍵漏洞:只驗證了 HTTP 回應碼和長 context 下的效能,卻沒有驗證模型輸出內容本身是否連貫正確。

**問題二,SGLang 的 bug**:當 prompt 長度超過 KV 池容量時，SGLang 的 scheduler 會把它內部標記為「拒絕」，並替換成一個只有一個 token 的 placeholder——但引擎沒有中止這個請求並回傳錯誤,而是讓 prefill 正常生成 placeholder prompt 的 KV cache,並把它傳給 decode node。decode node 收到「傳輸完成」的訊息後，誤以為 prefill 已經用完整 prompt 的內容覆寫了之前請求留下的 KV cache,但實際上大部分舊的狀態完全沒被動過。於是 decode node 在生成回應時，attend 到的是還殘留著先前請求資料的過期分頁——這就是超過 681,280 token 的請求,回應裡會混進別人資料的根本原因。

📊 **修復:調大池子,並且讓拒絕路徑真正安全**

Cloudflare 做了兩層修正：

- **配置修正**:把 GLM 5.3 的配置調整成與 GLM 5.2 一致,釋出足夠的 GPU 記憶體,讓 prefill KV 池擴大到約 204 萬 token（大約是 1,048,576 context length 的兩倍）。只要合法 prompt 一定能放進 context window,就一定能放進池子,原本的拒絕路徑根本不會被觸發。
- **引擎修正**:光靠池子夠大並不保險——量化方式、tensor parallelism、CUDA graph 大小,或未來模型版本的任何變動,都可能悄悄改變池子大小。Cloudflare 因此把「帶有待拒絕標記的請求」在 disaggregation 的 admission queue 階段就直接終止並回傳原始錯誤,不讓它進入任何 bootstrap、分配或 KV 傳輸流程,並把這個修法提交上游（PR #38704），同時要求 decode node 驗證「實際傳輸的 token 數」是否等於「原本保留的數量」。其中一部分修法已經在 SGLang main 的 #36988（9 月 6 日合併,原本是為了另一個相關的失敗路徑,但尚未發布正式版本），SGLang 維護者後續也採納 Cloudflare 的做法,合併了 #38935,讓這類請求更早被拒絕。所有修正都經過研究者的重現腳本與 Cloudflare 自己的 canary-marker 測試驗證後,才重新上線模型。

🎯 **對做 LLM 推理服務的工程師的啟示**

這起事故最值得記住的一點是：HTTP 200 加上看起來正常的串流回應,不等於系統真的按預期運作。Cloudflare 在復盤裡坦承,他們當時只驗證了回應碼和效能指標,沒去驗證長 context 下模型輸出的實際內容與連貫性——這正是配置不一致沒被攔下來的原因。如果你的服務也用了分離式 prefill/decode 架構與頁式 KV cache,這份報告提醒你兩件實際可做的事:一是把「KV 池大小」和「模型宣告的 context length」做成啟動時的強制一致性檢查,而不是靠觀察回應碼去推測；二是任何「請求被拒絕」的路徑,都要在真正釋放資源或開始傳輸前就終止,不要讓它悄悄混進正常流程繼續跑下去。

🔗 **來源**
- 標題：Cross-request KV cache exposure in the GLM-5.3 Workers AI model
- 作者／機構：Cloudflare（經 Hacker News 使用者 wondersky 轉發）
- 連結：https://blog.cloudflare.com/kv-cache-exposure-remediation/

#Cloudflare #LLMInference #SGLang #KVCache #AISecurity #TenantIsolation #WorkersAI #GLM #DisaggregatedInference #SecurityIncident
