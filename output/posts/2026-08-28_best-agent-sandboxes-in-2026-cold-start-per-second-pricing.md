---
title: 'Best Agent Sandboxes in 2026: Cold Start, Per-Second Pricing, and Network
  Policy Across E2B, Daytona, Modal, Cloudflare, and Vercel'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/27/best-agent-sandboxes-2026-cold-start-pricing-network-policy/
model: claude-code/sonnet
generated_at: '2026-08-28T18:11:42.718793'
score: 77
---

📌 AI Agent 沙箱大評比：冷啟動與計價的真相

TL;DR：五大 Agent 沙箱平臺的計價模型、暫停機制與網路政策落差比你想的大，選錯直接影響成本與安全。

當你的 AI Agent 需要執行程式碼時，它得先有個地方跑。這個「地方」如今已經是一個至少十幾家廠商搶佔的產品類別，但四種互不相容的計費模式，加上各家行銷頁面用不同條件測出來的冷啟動數字，讓「哪個沙箱最快最便宜」變成一個幾乎無法直接比較的問題。

🤔 **廠商的冷啟動數字，其實不是同一種測量**

Daytona 官方頁面宣稱 sandbox 建立時間低於 90 毫秒，E2B 則常被引用為約 150 毫秒，Modal 則宣稱針對預先快取（pre-cached）的容器可以做到次秒級冷啟動。問題是，這些數字都沒有註明併發數、地區、映像檔大小，也沒說清楚計時是從 API 回應開始算，還是從第一個指令真正執行開始算。這種行銷頁面式的比較幾乎沒有參考價值。

🧩 **一個開源的、排程執行的評測基準**

比較有意義的公開資料來自 ComputeSDK 的 sandbox leaderboard，這是一個開源且排程執行的評測工具，衡量的是 Time to Interactive（TTI）：從呼叫 create() 到沙箱內第一個指令成功執行為止的時間。它的方法是在單一 4 vCPU 主機（美國東北維吉尼亞）上，以同一時間併發啟動的方式跑 100 次迭代，最新一輪執行日期是 2026 年 8 月 21 日。

文章特別強調三個評測時要注意的地方：真正該測的任務是你的 Agent 實際會跑的工作，而不是 echo hello 這種空殼指令；一個有意義的測試應該固定跑同一套工作（例如安裝 pandas、讀 CSV、畫圖、回傳 PNG），並分別記錄 TTI 與任務完成時間，因為廠商優化的是前者，使用者在意的是後者；同時要固定地區與映像檔，並公布序列執行與併發執行兩種結果,因為兩者回答的是不同問題。

📊 **計價模型換算：待機成本才是關鍵變數**

文章用一個固定工作模型來換算各家費率：2 vCPU / 4 GiB 的沙箱、執行 1,000 次、不含方案底價與流量費、使用預設地區（Vercel 為 iad1，Cloudflare 標準規格為 2 vCPU / 8 GiB / 16 GB 硬碟）。

在「沙箱開著、模型在思考、什麼都沒在跑」的情境下，Vercel 的 CPU 費用從 $3.20 降到 $2.13，排名從第 4 便宜升到第 3；Cloudflare 的 active-CPU（僅計費實際使用 CPU 的時段）費率則降到 $1.20，等於在這個工作情境下大約便宜了兩倍。這正是 active-CPU 計費模式存在的意義。

反過來，如果 Orchestration 層改成回合之間主動暫停沙箱，而不是讓它一直開著，同樣的工作在每次執行只清醒 30 秒的情境下，E2B 的數字裡包含了約 17 秒的暫停與恢復（pause/resume）額外開銷（以 4 GiB 沙箱計算）。文章指出，暫停機制只有在回合之間的空檔明顯長於這個恢復開銷時才划算。

Fly.io 的閒置偵測器則定義得很明確：只要有進行中的 HTTP 或 API 請求、輸出到 stdout、開著的 TCP 連線，或是一個活躍的任務，就算是「活躍」而會被計費；反之，把輸出重導到檔案就不算活躍,是一個真實可用的省錢手段。

💡 **網路政策的優先順序：規則寫錯方向會出大事**

所有五個平臺現在都能執行完全沒有網際網路存取的沙箱，差別在於規則的優先順序、細緻度,以及政策能否在不重啟的情況下更動。E2B 和 Vercel 的處理方向恰好相反：E2B 中允許規則的優先權高於封鎖規則（同時出現在兩份清單中的 IP 會被允許放行），而 Vercel Sandbox 則是封鎖範圍會覆蓋允許範圍。這意味著,把一套政策從一個平臺原封不動搬到另一個平臺，語意會完全變調。

更隱蔽的問題是，E2B 的文件指出被封鎖的 TCP 連線,從沙箱內部看起來可能像是成功的:防火牆會先接受連線,才決定目的地是否允許,於是 socket 開了但沒有任何封包真正送達。因此驗證流量封鎖時,必須用應用層的回應（例如 HTTP 狀態碼或 TLS 交握）來確認，而不是單靠 connect() 是否成功;只檢查連線錯誤的測試,在沒被真正封鎖的沙箱上也會顯示「通過」。

在憑證管理上,單純封鎖流量只是基本要求,真正的差異在於能否讓沙箱發出「已驗證」的請求,卻從不持有憑證本身。Cloudflare 的作法是在 Workers runtime（沙箱之外）執行 outbound handler,並透過 Workers bindings 附加密鑰,沙箱本身只發出一般請求,並用 ctx.containerId 把憑證按執行實例（instance）隔離。Vercel 則是在流量出口（egress）代發憑證,並用路徑、方法、查詢字串或標頭作為比對條件（matcher）,而且防火牆執行在 microVM 外部的主機層,沙箱內程式碼無法關閉它。E2B 則以公開測試版形式提供逐主機的請求轉換,能在出口代理層注入標頭,包括沙箱本身從未看過的 workload-identity token;Runloop 也提供 Credential Gateway 做不透明的 token 注入。文章的結論很直接:一個被提示注入（prompt injection）攻擊、環境變數裡放著 GitHub token 的 Agent,和一個只能透過持有 token 的代理伺服器存取 GitHub 的 Agent,是完全不同等級的安全事故。

🎯 **實務啟示**

選沙箱平臺前,先用自己 Agent 真正會跑的工作跑一次基準測試,而不是看行銷頁面的冷啟動數字;再確認你的 Orchestration 是讓沙箱一直開著,還是回合之間會暫停,這直接決定該挑計時計費還是 active-CPU 計費的平臺。最後,如果你的 Agent 會處理不可信輸入（例如使用者貼上的文字或第三方回應）,把網路政策與憑證代發機制的優先順序、驗證方式看仔細,比冷啟動速度更該優先考慮。

🔗 **來源**
- 標題：Best Agent Sandboxes in 2026: Cold Start, Per-Second Pricing, and Network Policy Across E2B, Daytona, Modal, Cloudflare, and Vercel
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/27/best-agent-sandboxes-2026-cold-start-pricing-network-policy/

#AIAgents #Sandbox #CloudComputing #E2B #Daytona #Modal #Cloudflare #Vercel #DevOps #InfrastructureEngineering
