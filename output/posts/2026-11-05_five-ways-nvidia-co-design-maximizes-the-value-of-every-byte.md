---
title: Five Ways NVIDIA Co-Design Maximizes the Value of Every Byte in the AI Factory
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/five-ways-nvidia-co-design-maximizes-the-value-of-every-byte-in-the-ai-factory/
model: claude-code/sonnet
generated_at: '2026-11-05T23:00:10.522173'
score: 99
---

📌 【NVIDIA分享】HBM容量不變,代理式推理吞吐量為何暴增30倍?

TL;DR:NVIDIA靠五層co-design把同樣288GB的HBM榨出30倍產出,關鍵不是加大記憶體,而是讓每個byte都做更多工。

一張GPU規格表容易讓人誤會:從GB300到NVIDIA Rubin,HBM容量維持在288GB沒有變,頻寬則提升到19.2TB/s。但在SemiAnalysis AgentX基準(模擬真實coding agent的工具呼叫延遲與不斷增長的context)上,Vera Rubin NVL72在160 tokens/秒/使用者的互動水準下,吞吐量/MW竟是GB300 NVL72的30倍。容量沒變,為什麼產出差這麼多?答案藏在「每個byte被用得多有效率」。

🤔 **HBM是AI Factory裡最貴也最搶手的資源**

在AI工廠裡,花在冗餘weight副本、閒置session的KV cache,或是重複計算的prefix上的每一個byte,都是沒有被用來產生token的byte。問題已經從「GPU有多少記憶體」變成「每個byte能產出多少有用工作」。NVIDIA把這視為一個橫跨GPU架構、scale-up互連、serving軟體、CPU與儲存系統的co-design問題。

🧩 **NVFP4:用更少位元存下更多智慧**

NVFP4用4-bit的E2M1元素搭配兩層縮放:每16個數值組成的micro-block共享一個FP8(E4M3)縮放因子,外層再疊一個per-tensor的FP32縮放。這讓格式小到能釋放大量HBM,又保有足夠細緻度,不會像naive的4-bit格式那樣損失精度。套用在weight上,NVFP4相較FP16約可縮小3.5倍,相較FP8約可縮小1.8倍,省下來的記憶體正好用在agentic推理最需要的地方:更大的KV cache容量、更大的batch,以及更高的並發量。目前NVFP4已是AA-AgentPerf、SemiAnalysis AgentX、MLPerf Endpoints等開放agentic基準的預設精度,在DeepSeek R1於GB300上的測試中,同等互動性下吞吐量可達FP8基準的4倍。同樣的原理也套用在KV cache本身:NVFP4 KV cache比FP8省下最多50%的快取體積,等於約2倍的context能留在裝置上;在10項DeepSeek-v4-Pro基準測試中,仍能維持超過99%的BF16基準分數。

🧩 **NVLink scale-up網域:把72顆GPU變成一個記憶體池**

MoE模型每個token只啟動一部分參數,但所有expert的weight仍得常駐在某處的HBM裡。如果expert被塞進少數幾顆GPU,每顆GPU就得花大量記憶體存weight,decode時的MoE GroupGEMM也要付出沉重的weight載入成本。NVIDIA TensorRT-LLM的Wide-EP把expert分散到8顆以上的GPU,以DeepSeek-R1的EP64為例,每顆GPU每層只需持有4個expert,也就是全模型14,848個expert block中的232個。這帶來三個好處:容量上,更多HBM留給KV cache、更大batch與更高並發;算術密度上,GroupGEMM核心能讓每個載入的weight被更多token重複利用;平衡上,Expert Parallel Load Balancer(EPLB)會在forward pass之間重新分配冷熱expert,避免某顆GPU記憶體超載而另一顆閒置。但這一切都仰賴scale-up網域讓「遠端的byte幾乎和本地的byte一樣好用」:每個MoE層都會觸發all-to-all的dispatch與combine流量,若沒有高頻寬fabric,這些collective通訊就會把效益吃掉。GB200 NVL72靠130TB/s的NVLink總頻寬吸收這股流量,讓大規模EP(EP32)在100 tokens/秒/使用者下,每GPU輸出token數可達小規模EP(EP8)的1.8倍;GB300 NVL72對比H200 NVL8,則在同樣互動水準下有10倍的token吞吐量/MW。Vera Rubin NVL72延續同樣設計:每顆Rubin GPU最多配備288GB HBM4與3.0TB/s的NVLink 6頻寬,整機約20.7TB HBM4;Rubin還加入inline memory tensor accelerator描述子更新,讓多個expert共用同一份描述子,降低隨expert數量增加而膨脹的metadata負擔。

🧩 **NVIDIA Dynamo:讓每個被快取的byte都派上用場**

KV cache儲存過去token的中間attention計算結果,讓模型重複利用而不必重算,這是一種可被清除、需要時重算的暫時性狀態,但只有在真正被重複使用時才有價值。Agentic工作負載裡其實充滿重複利用的機會:系統提示詞、工具schema、共享文件,以及多步驟任務不斷累積的歷史紀錄。問題是,如果請求被送到一顆沒有保留對應prefix的GPU,或是那段prefix剛被清掉,系統就得重新付出prefill的代價,byte明明存在,只是待在錯的地方。Dynamo這個分散式serving層正是為了補上這個缺口,它把KV cache當成跨整個GPU機群的資源,而不是單顆GPU的副產品,靠三項co-design能力實現:KV-aware路由會追蹤KV block的位置,綜合考量cache-prefix重疊度與worker負載來分配請求;Disaggregated serving讓prefill與decode跑在各自規模的GPU池上,decode GPU可以把HBM全力留給KV cache與batch size;KV Cache Runner(KVCR)則追蹤每個block在GPU、pinned CPU與儲存層(包括本地SSD與掛載的網路檔案系統)之間的位置,搭配NVIDIA Inference Xfer Library(NIXL)進行儲存層傳輸,讓被保存在HBM之外的prefix可以在之後需要時被還原,繼續節省prefill成本;額外的KVCR-Guard功能則能在guard服務與主機都正常運作的前提下,於engine故障時保留已提交的host記憶體快取。

📊 **關鍵數字一覽**

| 技術 | 效果 |
|---|---|
| NVFP4 weight | 比FP16省約3.5倍,比FP8省約1.8倍記憶體 |
| NVFP4 vs FP8吞吐量 | DeepSeek R1於GB300上,同等互動性下最高4倍吞吐量 |
| NVFP4 KV cache | 比FP8省最多50%體積,約2倍context留在裝置,10項基準維持超過99% BF16分數 |
| Wide-EP(DeepSeek-R1, EP64) | 每GPU僅4個expert/層,共232個block(全模型14,848個) |
| GB300 NVL72 vs H200 NVL8 | 100 tokens/秒/使用者下,token吞吐量/MW高達10倍 |
| EP32 vs EP8(GB200 NVL72) | 100 tokens/秒/使用者下,每GPU輸出token數多達1.8倍 |
| Vera Rubin NVL72 vs GB300 NVL72 | AgentX基準,160 tokens/秒/使用者下吞吐量/MW高達30倍 |

🎯 **實務啟示**

這篇文章給做LLM serving基礎設施的工程師一個清楚的訊號:面對記憶體瓶頸,先問「每個byte有沒有被用滿」,再問「要不要加硬體」。精度(NVFP4)、平行策略(Wide-EP)與serving層的快取路由(Dynamo)是三個互補、可以疊加的槳,而且都已經在開放benchmark上被驗證。

🔗 **來源**
- 標題:Five Ways NVIDIA Co-Design Maximizes the Value of Every Byte in the AI Factory
- 作者/機構:Shara Tibken,NVIDIA Developer
- 連結:https://developer.nvidia.com/blog/five-ways-nvidia-co-design-maximizes-the-value-of-every-byte-in-the-ai-factory/

#NVIDIA #HBM #LLMInference #NVFP4 #MoE #TensorRT #Dynamo #AIInfrastructure #GPU #AgenticAI
