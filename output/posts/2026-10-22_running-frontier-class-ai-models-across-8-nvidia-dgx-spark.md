---
title: Running Frontier-Class AI Models Across 8 NVIDIA DGX Spark Nodes
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/running-frontier-class-ai-models-across-8-nvidia-dgx-spark-nodes/
model: claude-code/sonnet
generated_at: '2026-10-22T20:52:29.218196'
score: 89
---

📌 8 臺 DGX Spark 併起來，統一記憶體衝上 1TB 跑旗艦模型

TL;DR：8 節點 DGX Spark 叢集記憶體上探 1TB，可服務 753B 模型。

單臺DGX Spark有128GB統一記憶體,四臺是512GB,但有些前沿模型連512GB都塞不進去。把節點數衝到8臺,這個門檻一次跨過去。

🤔 不再只是跑單一模型

AI開發者現在不只是跑單一個模型,而是平行協調多個模型、串接推論呼叫,並嘗試需要數百GB記憶體的前沿級架構。DGX Spark原本就是要把AI開發帶到桌面上,NVIDIA在GTC Berlin宣布正式支援8節點DGX Spark叢集,把統一記憶體擴展到1TB,打開了跑frontier-class模型、multi-agent workload,以及近乎線性擴展pre-training的門,而且全部都在本地執行。NVIDIA Sync讓組叢集變簡單,其中的Cluster Assistant負責處理設定和裝置管理;NVIDIA Sync對8節點叢集的支援將在年底前推出。

🧩 記憶體怎麼疊出來的

單臺DGX Spark提供128GB統一記憶體,4節點達到512GB,8節點達到1TB。這個容量讓原本在4節點系統上根本跑不起來的一類模型變得可行,包括Z.ai的完整GLM 5.3(753B)模型。NVIDIA實測把GLM 5.3 Flash跑在8節點叢集上,生成速度約80 tokens/秒,適合對一個frontier級mixture-of-experts模型做互動式本地開發。完整的GLM 5.3(753B) checkpoint可以跑在8x128GB的叢集上,是少數能在本地端服務起來的最大型開源模型之一。

📊 GLM 5.3 在 8 節點叢集上的實測數字

| Concurrency | Prefill 總TPS | Prefill 單使用者TPS | Decode 總TPS | Decode 單使用者TPS |
|---|---|---|---|---|
| 1 | 1,600 | 1,600 | 31 | 31 |
| 4 | 1,600 | 750 | 51 | 21 |
| 8 | 1,600 | 473 | 67 | 18 |

模型為nvidia/GLM-5.3-NVFP4,NVFP4量化下約470GB,以MTP3在concurrency 1、4、8下測量,prefill以8K input sequence length量測。

🧩 換一套 collective 通訊後端：RoCEnante

Tensor-parallel推論有不少時間花在all-reduce之類的collective操作上。NVIDIA在switch連接的叢集上評估了一套Spark最佳化的collective後端RoCEnante,針對tensor-parallel decode典型的小訊息、低concurrency、節點數不多的模式降低collective延遲。做法是all-to-all交換後接本地reduce:每個rank把輸入分享給每個其他rank,再各自在本地加總,由單一GPU kernel協調整個過程。好處是通訊步驟更少,ring all-reduce要在相鄰rank間跑多輪轉發,這種方式則直接跟所有peer交換,省掉轉發鏈;代價是資料搬移量更大,每個rank要把完整輸入送給每個peer並自己reduce所有輸入,訊息或節點數變多時這個額外流量的代價會變貴,此時ring all-reduce的頻寬效率就愈有吸引力。

在switch拓樸、使用Qwen3.8-27B-NVFP4(關閉speculative decoding)的測試中,8個Spark節點搭配RoCEnante達到4.43倍加速,沒有RoCEnante則是3.05倍,相當於擴展效率提升45%。實務上在NVFP4下4節點的prefill和decode分別快約5%和21%,在非量化模型的8節點下decode快約18%。這套後端已併入FlashInfer,啟動測試失敗時會透明回退到NCCL,且只適用switch連接的拓樸,因為它依賴每個節點間的直接point-to-point交換,並非要取代NCCL,隨著叢集規模和concurrency增加,NCCL仍是預設且更好的選擇。原始的one-shot all-reduce作法由社群貢獻者Jason Cook/el8提出。

📊 從 1 到 8 節點的擴展曲線

| 節點數 | 拓樸 | Prefill(TPS) | Prefill倍數 | Decode(TPS) | Decode倍數 |
|---|---|---|---|---|---|
| 1 | — | 2,635 | 1.00x | 11.86 | 1.00x |
| 2 | 直連 | 3,285 | 1.25x | 21.71 | 1.84x |
| 4 | 實體環形 | 4,446 | 1.69x | 32.82 | 2.77x |
| 4 | Switch(RoCEnante) | 4,556 | 1.73x | 36.34 | 3.06x |
| 8 | 實體環形 | 4,962 | 1.88x | 40.11 | 3.38x |
| 8 | Switch(RoCEnante) | 5,105 | 1.94x | 52.58 | 4.43x |

以dense模型NVIDIA/Qwen3.8-27B NVFP4、關閉speculative decoding/MTP測量,用llama-benchy、8192 tokens input sequence length、256 tokens output sequence length、concurrency 1;倍數相對同精度下的單臺Spark計算。兩個現象值得注意:decode throughput隨節點數明顯擴展,從單節點約12 TPS一路到8節點約52 TPS;另外最適合的拓樸要看工作負載,實體環形在單一模型切分到所有節點時decode表現優異,但一旦要把叢集切成獨立分組,或工作負載需要節點間直接any-to-any連接,就得改用switch。

💡 不是每個叢集都需要 switch

DGX Spark節點可以直接用實體環形接線,成本更低、設定更簡單,對愛好者和小型部署很有吸引力。在4節點部署內,NCCL預設採用ring-based演算法做tensor-parallel通訊,讓switchless環形正好貼合流量模式,用較低花費拿到不錯的throughput。但規模擴大或需求變specialized時情況會變:要擴到8節點或把叢集切成兩組各4臺,環形拓樸表達不出這種切分,需要switch;像MPI-based clustering這類依賴point-to-point模式的傳統HPC工作負載也需要switch,環形會付出額外的hop代價;前面提到的最佳化collective後端只支援switch配置,因為它需要每個節點間的直接point-to-point連接。簡單來說,想要最簡單、最低成本的4節點推論機,選switchless環形;需要擴到8節點、切分叢集,或跑環形無法服務的通訊模式,就選switch。

🎯 多模型協調：NVIDIA NeMo Switchyard

不是每個請求都需要用上最大的模型。在共享的8節點叢集上,把簡單請求導向小而快的模型、把大模型留給難題,可以拿到明顯更高的整體throughput。NVIDIA NeMo Switchyard讓這件事變得實際可行:一個輕量分類器檢查每個請求或session,把它導向適當的模型池,再由load balancer把流量分散到各個replica上。

🎯 實務啟示：如果本地已經有多臺DGX Spark,8節點叢集把統一記憶體門檻推到1TB,值得評估的是工作負載更看重單一超大模型的decode throughput(選實體環形),還是需要切分叢集或多模型協調的彈性(選switch搭配RoCEnante和Switchyard)。

🔗 來源
- 標題：Running Frontier-Class AI Models Across 8 NVIDIA DGX Spark Nodes
- 作者／機構：Shara Tibken, NVIDIA Developer Blog
- 連結：https://developer.nvidia.com/blog/running-frontier-class-ai-models-across-8-nvidia-dgx-spark-nodes/

#NVIDIA #DGXSpark #GTCBerlin #AIInfrastructure #LLMInference #GPUCluster #EdgeComputing #MixtureOfExperts #AIHardware #DistributedComputing
