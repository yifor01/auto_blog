---
title: 'Together Compiler: Continual Compilation for AI inference'
source: Together AI
url: https://www.together.ai/blog/together-compiler-continual-compilation-for-ai-inference
model: claude-code/sonnet
generated_at: '2026-11-04T22:47:12.598531'
score: 112
---

📌 Together AI 推出連續編譯器，推理吞吐量最高衝高 2.6 倍

TL;DR：Together Compiler 用高吞吐 agent 持續重新編譯推理引擎，24 小時內追上新模型與新流量模式。

如果你覺得「把一個模型調到最佳效能」已經夠難，那 Together AI 面對的問題是：同時要幫數千種模型、數千種客戶流量、好幾代硬體都調到最佳。而且這個目標還會隨時間漂移。

🤔 **推理工作負載沒有穩定態可言**

Together AI 在文章開頭點出一個反直覺的事實：Transformer 問世已經約 11 年，照理說架構應該趨於統一，但 OpenRouter 上前十大開源 LLM 竟然沒有兩個用同樣的架構。硬體端也一樣分裂，H100、B200、B300、NVL72、Groq 等平臺各自需要不同的最佳化策略。再加上流量本身的變數：Together 每天服務數兆 token，不同地區用戶的 prompt 長度可以差到 1.4 倍（97k vs 70k tokens），新模型上線兩週後 prompt 長度會因為使用者轉向 agentic 工作流而暴增 80%，流量的突發性（burstiness）也會讓 prompt 長度瞬間翻倍、快取命中率下滑。人工或傳統機器學習編譯器的固定規則，顯然跟不上這種多維度、持續變化的最佳化空間。

🧩 **用「持久化引擎」取代重啟，讓 Agent 實驗速度暴增**

Together Compiler（簡稱 TKCC）的核心想法是讓 agent 持續產生最佳化想法並測試，而不是依賴人工規則。但作者指出,現有 agentic 推理最佳化系統的瓶頸在實驗速度：每次測試新想法都要重新啟動 vLLM、SGLang 或 TRT-LLM 之類的推理引擎,而引擎啟動動輒數十分鐘。

TKCC 的解法是「持久化引擎」（persistent engines）：引擎只啟動一次,之後可以熱重載（hot-reload）任何候選的 forward pass,完全不需要重啟。文中附上的實測表格顯示差異有多懸殊,從流程初始化、權重載入、KV-cache 調整、JIT kernel 暖機到 autotuning,整套流程原本需要 467 秒才能開始服務,TKCC 壓到只要 9.0 秒。為了讓持久化引擎持續有新想法可測,TKCC 同時派出多個 agent,透過訊息板（message board）互相溝通、平行化各自的實驗。

為了兼顧「測量速度」與「測量準確度」的取捨,TKCC 設計了兩層引擎:「快引擎」只載入少數層,用於快速迭代與低變異的計時;「慢引擎」載入完整層數,用來驗證最佳化策略在真實資料分布下是否依然有效。這一點特別重要,因為像 MoE 或稀疏注意力這類資料依賴型（data-dependent）的架構,最佳化策略的勝負會隨輸入資料分布改變,用隨機資料測試很容易選錯方向。

此外,TKCC 還設計了一套自訂成本模型,結合硬體規格、微基準測試與實際量測到的 forward pass 結果,用分層量測策略快速篩選出張量平行、專家平行等平行化策略的候選空間,而不是單純依賴硬體規格或微基準做判斷。

📊 **24 小時內,吞吐量最高衝高 2.6 倍**

在 SemiAnalysis 的 InferenceX AgentX 基準上,TKCC 從各推理引擎與硬體平臺目前最佳的開源配置出發,最終在所有測試情境中都刷新效能上限,最高達到 2.6 倍的 TPS 提升。在低延遲情境（batch size 1）下,TKCC 在 MiniMax M3.1-Flash 上達到 1111 TPS、在 DeepSeek v4.1-Flash 上達到 1205 TPS,雙雙創下該基準的新紀錄;這兩項結果是改用 TKCC 自家的成本模型挑選平行化配置,而非沿用 InferenceX 原本的配置所得出。在被人工專家與傳統機器學習編譯器高度最佳化過的「MegaKernel」場景(Llama 1B、batch size 1)上,TKCC 相較現有開源 megakernel 仍能再快 1.7 倍,且優勢在序列長度增加時依然維持。文章也提到,這一切效能提升的基礎,是 TKCC 相較基準 agentic 最佳化系統有 252 倍的實驗吞吐量。值得一提的是,TKCC 並不只侷限於語言模型推理,文中提到它也能延伸到天氣模擬、PDE、時間序列與生物學等領域的程式碼。

🎯 **實務啟示**

對建置推理服務的工程團隊而言,TKCC 的啟示是把「效能最佳化」本身也變成一個持續運行的系統,而不是模型上線前做一次性調參。如果你的服務也面對多模型、多硬體、多客戶流量型態的組合爆炸,「持久化引擎 + 分層測量 + 持續重編譯」這套思路,比單靠人工規則或一次性 AutoTuning 更能跟上真實世界的流量漂移。

🔗 **來源**
- 標題：Together Compiler: Continual Compilation for AI inference
- 作者／機構：Together AI
- 連結：https://www.together.ai/blog/together-compiler-continual-compilation-for-ai-inference

#TogetherAI #AIInference #LLMOptimization #GPU #Megakernel #MoE #InferenceEngine #AIAgents #MachineLearningSystems #Compilers
