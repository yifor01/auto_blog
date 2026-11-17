---
title: 'Last year we built megakernels. This year we deleted them: The road to Together
  Compiler'
source: Together AI
url: https://www.together.ai/blog/road-to-together-compiler
model: claude-code/sonnet
generated_at: '2026-11-17T00:56:40.902527'
score: 111
---

📌 Together AI 砍掉 Megakernel：編譯器才是推理最佳化的答案

TL;DR：CUDA Graphs 疊加預設 Inductor kernel 就能達到 98% megakernel 效能，不必手刻單一巨型 kernel。

去年 Together AI 打造出業界最早的 megakernel 之一，把整個模型的 forward pass 塞進一個高度融合的 GPU kernel，跑出破紀錄的速度。今年他們卻把這些 megakernel 刪掉了——因為辛苦幾個月換來的,是「一個模型、一個 batch size、一個客戶」的窄用途成果。

🤔 **Megakernel 跑得快，但難以量產**

AI 推理的場景正變得越來越異質:新模型架構每週都有,流量在不同 batch size 與序列長度間變動,硬體平臺也持續增加。要在所有情境都達到最佳效能,需要能跟上這種變化速度的最佳化框架。Together AI 過去兩年持續探索下一代推理最佳化系統該長什麼樣子,最終推出 Together Compiler——他們稱之為「持續性 AI 推理最佳化框架」。

🧩 **Torch Compile 怎麼運作:三個關鍵元件**

PyTorch 的 nn.Module 這類模組化抽象讓開發速度飛快,卻也犧牲了效能:把模型拆成一連串獨立運算,會帶來不小的啟動開銷,也限制了運算與記憶體搬移重疊的機會。為此,PyTorch 推出 Torch Compile(以 Inductor 為核心引擎),NVIDIA 則推出 CUDA Graphs 來降低 kernel 啟動開銷。Torch Compile 的運作大致分三步:

- **Graph capture**:TorchDynamo 追蹤 Python 執行過程,用「fake tensor」(只帶 shape、dtype、stride 等中繼資料,不實際配置或計算)把張量運算捕捉成一張 FX graph,讓編譯器能在不真正跑 GPU 的情況下推理整個計算流程。
- **運算與 kernel**:Inductor 把這張圖降階成自己的中繼表示,將運算分成 pointwise(如 activation)、reductions(如 summation、softmax)、scans(如 cumulative sum)與 templates(如 GEMM)等類別;部分運算則直接呼叫 cuBLAS 等既有函式庫,以 ExternKernel 表示,對 Inductor 的融合機制而言是不透明的黑盒。
- **融合與最佳化**:Inductor 用貪婪、兩兩配對的演算法決定哪些運算要融合進同一個 kernel。can_fuse() 檢查融合是否合法,score_fusion() 則用記憶體流量節省等啟發式規則排序融合機會,反覆套用有利的融合——但這些決策基於局部啟發式,而非對所有 kernel 分割與執行策略的全域搜尋。

在他們以 Llama 1B 為目標的工作負載上,Inductor 預設可以跑到 669 TPS。

📊 **兩個發現:啟發式規則靠不住,基準測試會騙人**

**發現一:編譯器的啟發式規則無法在所有工作負載下穩定選出最佳實作。** 以 freezing 這個設定旗標為例,它告訴編譯器模型權重在推理過程中不會改變,編譯器便能提前把權重轉成 FP32 做某些最佳化,再轉回原本的低精度格式。團隊發現,在使用矩陣乘矩陣運算的較大 batch size 下,啟用 freezing 能把輸出量提升 10% 到 26%;但在 batch size 為 1、主要是矩陣乘向量運算的情境下,同一個旗標卻造成 49% 的效能衰退——因為 FP32 轉換沒有被還原回矩陣乘向量運算,導致 GPU 得處理更大的 32-bit 權重,而非原本的低精度權重。截至 2026 年第三季,Inductor 已暴露 607 個調校旗標,其中 198 個是過去一年才新增的,而這些旗標之間的效果並非互相獨立:單獨啟用 aggressive_fusion 會讓 Llama 1B 的輸出量降低 6 TPS,但若同時搭配 combo_kernels、benchmark_fusion 與 triton.coalesce_tiling_analysis 這三個旗標,反而能提升 3 TPS。

**發現二:單獨跑最快的 kernel,放進整個推理流程未必最快。** Inductor 的最佳化決策仰賴自己的基準測試機制,而這套機制至少有一種誤導方式是忽略了 kernel 效能其實會受快取行為影響。

💡 **深入分析:應該系統性搜尋,而非猜旗標**

這兩個發現共同指向同一個結論:最佳化旗標之間的互動空間極為龐大且不可預期,靠人工猜測或固定一套配置去套用在所有工作負載上,注定會在某些情境下踩雷。Together AI 由此得出的 takeaway 是,這個空間應該被系統性地搜尋,而不是靠直覺去猜對的旗標組合。

🎯 **實務啟示**

對於自建推理服務的團隊,這篇文章提醒我們:效能調校旗標之間的交互作用遠比表面看起來複雜,啟用同一個旗標在不同 batch size 下可能是提升也可能是重大退步,貿然把「對的設定」寫死在生產環境之前,值得先針對自己實際的工作負載分佈做系統性驗證,而不是全盤複製別人的最佳化配置。

🔗 **來源**
- 標題：Last year we built megakernels. This year we deleted them: The road to Together Compiler
- 作者／機構：Together AI
- 連結：https://www.together.ai/blog/road-to-together-compiler

#TogetherAI #GPUKernel #Megakernel #TorchCompile #Inductor #CUDAGraphs #LLMInference #AICompiler #PerformanceOptimization #DeepLearningSystems
