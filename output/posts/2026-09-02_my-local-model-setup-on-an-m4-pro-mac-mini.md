---
title: My local model setup on an M4 Pro Mac Mini
source: Hacker News
url: https://lws.io/blog/my-local-model-setup/
model: claude-code/sonnet
generated_at: '2026-09-02T10:24:09.505274'
score: 83
---

📌 M4 Pro Mac Mini 跑本地 LLM：一顆 48GB 記憶體怎麼分給兩個模型

TL;DR：作者用 48GB 記憶體的 M4 Pro Mac mini 搭配 oMLX 與 MoE 模型架設全套本地 LLM 系統，取代大部分雲端 API 用量。

雲端 API 的問題不是不好用，而是它是租來的地。定價、額度、甚至背後跑的模型隨時可能被廠商悄悄換掉，而你完全無法控制。這篇 Hacker News 高討論度的文章，記錄了作者如何用一臺桌上型 Mac mini 把大部分日常請求收回自己手上。

🤔 **為什麼要自己跑：租來的地隨時會變卦**

作者提到自己同時繳兩份每月 200 美元的訂閱費，卻常常吃到用量上限，而且明顯感覺到同一個服務在不同時間點給出的品質不一致，有時模型無預警被降級也不會收到通知。除了成本與品質的不可預期，資料隱私也是隱憂：使用者無法確知這些公司拿到資料後會怎麼處理、是否會被用於其他用途甚至外洩，對處理敏感程式碼或客戶資料的人來說,這是一個做了就回不去的決定。作者也提到自己在觀察美國政府如何限制特定模型的推出,這類限制隨時可能因任何理由發生在任何政府身上，一旦依賴的雲端模型被限制，工作流程就得被迫中斷。除此之外，本地部署還有幾個實際好處：成本可預期（硬體加電費之後每次推理都是免費）、沒有網路往返的延遲、離線也能運作，以及不受 API 供應商的用量節流限制。

🧩 **架構：一顆大模型扛推理，一顆小模型扛雜務**

作者的本地技術堆疊包括：作為主力模型、負責需要推理深度任務的 Qwen3.6-35B-A3B-OptiQ-4bit；用於簡單對話、格式化等例行工作的輕量模型 Gemma-4-E4B-it-OptiQ-4bit；推理伺服器 oMLX；以及用 Tailscale 把 Mac mini、iPhone、MacBook 連成一個私有 tailnet。agent 後端 Hermes 跑在 Mac mini 上，MacBook 執行桌面用戶端、手機則透過 Telegram 存取；其他工具還包括 iOS 上的 Apollo（用來做丟即用的簡短對話）、寫程式用的 agent Pi，以及 Mac 上的 Raycast AI。

文中特別解釋了模型命名裡藏的關鍵資訊。以 Qwen3.6-35B-A3B-OptiQ-4bit 為例：Qwen3.6 是模型家族與版本、35B 是所有專家（experts）加總的總參數量、A3B 代表每個 token 實際會啟用的參數量（3B，而不是 35B）、OptiQ-4bit 則是混合精度量化（多數層 4-bit、部分敏感層 8-bit）。這個 A3B 的細節正是關鍵：一個 27B 的密集（dense）模型,每處理一個 token 都要把全部 27B 參數載入運算；但像 Qwen3.6-35B-A3B 這種 MoE（mixture-of-experts）模型，雖然總參數量攤在 256 個專家上有 35B，每個 token 實際只會啟動約 3B，其餘 32B 只是靜靜待在記憶體裡。

📊 **記憶體怎麼分配**

在作者 48GB 的 Mac mini 上，Qwen3.6-35B-A3B 的 4-bit 版本大約佔用 20GB 記憶體，留給 context window、作業系統與其他程式的空間還有 28GB；Gemma-4-E4B 則只佔約 2.4GB，小到足以常駐待命,處理不需要動用 20GB 大模型的簡單任務。作者也拿朋友一臺 16GB 記憶體的 MacBook Air 對照：一個 27B 密集模型的 4-bit 版本大約需要 14GB，幾乎吃光整臺機器扣除作業系統後的所有空間，短暫堪用之後就會開始把資料換頁到 SSD，體驗變得很差。換成 MoE 架構後,同樣是 35B 總參數的模型,因為每個 token 只啟動約 3B,GPU／媒體記憶體的實際負擔更接近一個 6B 密集模型,反而能塞進這臺輕薄筆電。文中也提到,OptiQ 的 4-bit 量化讓這顆 35B-A3B 模型,相較未壓縮的 BF16（16-bit 浮點）版本,在多數基準測試上只掉 1 到 2 分,對換來一半左右的記憶體佔用而言,是划算的取捨。

💡 **判斷一顆模型能不能塞進你的機器**

作者給出一套實用的檢查步驟：先看量化後的檔案大小（4-bit 模型大致等於參數量的 GB 數，例如 35B 參數在 4-bit 下約需 17 到 20GB，視量化方法而定）；再扣掉作業系統的開銷，Apple Silicon 上的 macOS 大約佔 6 到 8GB；接著要為 context window 留出空間，因為每多幾千個 token 就會讓 KV cache 增加數 MB，長對話建議預留 8 到 16GB。對 MoE 模型而言，看總參數量會誤導判斷,真正該看的是「啟用參數量」(active parameters) 這個數字才能反映實際推理時的記憶體需求。只要模型加上 context 的用量,在可用的統一記憶體（unified memory）中還留有 10% 到 15% 的緩衝,就算是安全範圍；太接近滿載就會開始換頁到 SSD。

⚠️ **本地模型不是要取代雲端 API**

作者強調這套本地方案的目標不是完全取代 GPT-5 或 Claude Opus 這類雲端模型,而是接手日常裡不需要動用頂級模型的八成請求，真正需要頂級能力時，雲端模型依然隨時可以呼叫。此外,他也提到換模型的門檻很低：把新模型下載到 ~/models/ 目錄，oMLX 會自動偵測，在 oMLX app 裡選擇或重啟伺服器即可切換，多數步驟也能透過 CLI 從任何裝置 SSH 進 Mac mini 完成。

🎯 **實務啟示**

對於想在消費級硬體上跑本地 LLM 的工程師來說，這篇文章最實用的一點是「別只看參數量,要看啟用參數量」的判斷方法：MoE 架構讓大參數量模型得以塞進中階硬體，是目前在記憶體有限的 Apple Silicon 裝置上取得推理深度與硬體成本平衡的關鍵路徑。用一顆大模型負責深度推理、一顆小模型處理雜務的雙模型分工方式，也是控制本地資源佔用的實用做法。

🔗 **來源**
- 標題：My local model setup on an M4 Pro Mac Mini
- 作者／機構：raybb, Hacker News
- 連結：https://lws.io/blog/my-local-model-setup/

#LocalLLM #MacMini #AppleSilicon #MoE #Quantization #oMLX #EdgeAI #SelfHosted #AIInfrastructure #OnDeviceAI
