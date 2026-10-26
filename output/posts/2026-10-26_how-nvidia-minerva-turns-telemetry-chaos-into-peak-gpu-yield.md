---
title: How NVIDIA Minerva Turns Telemetry Chaos Into Peak GPU Yield
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/how-nvidia-minerva-turns-telemetry-chaos-into-peak-gpu-yield/
model: claude-code/sonnet
generated_at: '2026-10-26T21:52:50.147086'
score: 81
---

📌 當一萬張GPU的健康訊號分散在三個團隊手上

TL;DR：NVIDIA Minerva用知識圖譜整合telemetry,把分散的異常訊號拼成單一可追查的事件。

一張GPU溫度高了幾度,一臺NVMe只在長時間滿載時掉速,一個switch發出一陣pause-frame風暴——單獨看,每個現象都「正常」;湊在一起,就是拖垮整個訓練任務的元兇。

🤔 同步訓練的致命弱點:最慢的那一個拖累所有人

AI Factory是極端複雜的運作環境:數十萬張GPU、NVIDIA Spectrum-X Ethernet構成的scale-out/scale-across/scale-in網路,加上NVLink的scale-up fabric、分散式排程器,以及可能跑上數週的訓練任務,全部必須像同一套生產系統一樣協同運作,即便telemetry分別掌握在不同團隊手上。在同步分散式訓練中,任務的進度取決於最慢的那個rank,一張狀態不佳的GPU、一個介面或一臺儲存裝置,就足以浪費大量健康資源的運算時間。

更麻煩的是,真正傷害良率(yield)的故障通常很微妙,不會跨越任何固定的告警門檻。傳統規則式監控假設「已知指標越過已知門檻=已知問題」,面對這種「灰色故障(gray failure)」——元件仍可用,問題只在滿載或與同儕比較時才顯現——規則式告警不是漏判就是誤報過多,把決策壓力全部丟給值班工程師。加上規模放大效應,一個實體故障可能同時產生介面錯誤、RX pause frame、壅塞指標與GPU使用率變化等一堆看似無關的警報,網路團隊看介面計數器,運算團隊看節點與GPU健康度,ML團隊看step time變化,三方畫面都「準確」,卻看不到彼此之間的因果關係,追查往往變成一連串的dashboard搜尋與跨團隊交接。

🧩 用動態知識圖譜把基礎設施和任務綁在一起

NVIDIA Minerva是針對AI factory拓樸與工作負載設計的AI-native AIOps平臺。它從GPU、Spectrum-X與NVLink交換器、SuperNIC、DPU、儲存裝置、NCCL與排程器等全層級收集telemetry,透過auto-discovery建立起一個會隨環境即時更新的動態知識圖譜,把基礎設施、排程器與工作負載的關係串連起來,範圍可以橫跨多個資料中心,也能從全廠視角一路鑽到單一介面。這個拓樸圖讓調查路徑可以雙向進行:從一個異常介面出發,可以追到它所屬的節點、服務的fabric路徑,以及目前placement在上面的任務;從一個任務ID出發,也可以反過來追蹤GPU、host、NIC、switch與log證據。

在偵測層,Minerva每小時處理數十億筆metric與log資料點,結合supervised與unsupervised機器學習模型。Supervised模型辨識已知的關鍵錯誤模式並附上對應的修復建議;unsupervised模型則學習每個硬體或邏輯元件的「正常」樣態,拿來跟同儕比較——例如某張GPU溫度在規格內,但明顯比同批次下跑同樣負載的其他GPU熱,這種異常單獨看不出來,比較之後就會浮現。Log方面則結合NLP異常偵測(找出未見過的模式)與已知錯誤的監督式比對,偵測結果還能回饋給排程器,在另一個任務落到故障節點之前,或在checkpoint之間的安全時間點把節點drain掉。

📊 把事件風暴收斂成單一事件

Minerva的關聯引擎利用知識圖譜判斷哪些事件共享同一條依賴路徑,把本來會觸發多個告警的下游症狀收斂成同一個事件,連同受影響的拓樸與工作負載一起呈現。NVIDIA的測試顯示,在它支援的情境下,通知事件與工單數量有顯著下降(官方未提供具體量化數字)。平臺內建一個名為Sherlock的AI agent,基於即時telemetry與知識圖譜運作,運維人員可以直接用自然語言問「某個任務在某段時間為什麼變慢」「哪些元件狀態改變了」「其他節點是否共享同一個故障域」,Sherlock會附上支持證據並給出修復建議,也提供MCP server供外部agentic工具串接,讓資歷較淺的工程師也能走到過去需要資深專家才能得出的根因分析。

⚠️ 留意之處

NVIDIA目前公開的「顯著減少工單」是自家測試結果,沒有附上具體百分比,實際效果仍需在自己的環境中驗證;此外,知識圖譜與異常偵測的準確度,很大程度依賴telemetry覆蓋的完整度與跨團隊資料的即時性,導入前的資料整合工作量不應低估。

🎯 實務啟示

如果你的團隊正苦於GPU叢集故障排查需要在多個dashboard與多個團隊之間來回拉鋸,Minerva示範的思路值得借鏡:關鍵不是再多一個監控儀表板,而是把「基礎設施拓樸」與「正在跑的任務」綁在同一張即時圖譜上,讓關聯與根因分析能從同一份證據出發,而不是各自表述。

🔗 來源
- 標題：How NVIDIA Minerva Turns Telemetry Chaos Into Peak GPU Yield
- 作者／機構：Elizabeth Goodman, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/how-nvidia-minerva-turns-telemetry-chaos-into-peak-gpu-yield/

#AIOps #NVIDIA #GPUCluster #DistributedTraining #Observability #KnowledgeGraph #MLOps #DataCenter #AIInfrastructure #AnomalyDetection
