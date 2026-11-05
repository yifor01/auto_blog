---
title: 'Together AI Releases Together Compiler: Agents Make Inference Up to 2.6x Faster'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/05/together-ai-together-compiler-continual-compilation-ai-inference/
model: claude-code/sonnet
generated_at: '2026-11-05T22:56:20.202139'
score: 102
---

📌 推理引擎不該調一次就定型，Together AI 讓 Agent 持續重寫 Kernel

TL;DR：Together Compiler 用 coding agent 持續重寫推理 forward pass，在真實流量下比現有最佳開源配置快最多2.6倍。

一個 kernel 在上線那天測得再快，三天後流量分佈一變，它可能就是全場最慢的那一個。Together AI 的新系統，索性把「調優」做成一個永不停止的迴圈。

🤔 **流量永遠在漂移，隨機資料會騙人**

Together AI 團隊觀察到，生產環境的流量形狀從不穩定：同一模型在不同國家的 prompt 長度，一地約97K token，另一地僅70K token；某客戶的 P90 輸入長度在3天內從18K漲到33K token。更麻煩的是，用隨機資料調優 kernel 會得出誤導性結論——隨機輸入比真實流量多啟用13%到38%的 MoE 專家，一個 agent 寫出的 top-k kernel 在隨機資料上僅耗時20微秒，換成70K上下文的真實資料卻要62毫秒。

🧩 **持久引擎 + 兩級測量，繞開重啟成本**

Together Compiler（TKCC）是一套持續編譯迴圈：輸入伺服器啟動命令、流量輪廓與硬體配置，agent 提出更快的 forward pass 候選方案，一個持久化引擎負責測量每個候選，勝出的程式碼被直接推上線。當流量再次漂移，迴圈重新啟動。

多數 agent 調優迴圈的做法是每次實驗都重啟 vLLM、SGLang 或 TensorRT-LLM——研究團隊測得 MiniMax M3.1 Flash 在 TensorRT-LLM 上的冷啟動要761秒。Together Compiler 則只啟動引擎一次：agent 透過 RPC 送出候選 forward pass，伺服器直接換掉 forward 函式指標並重新擷取 CUDA graph。

系統設有兩級測量：快速層用12層做初篩，慢速層用60層在真實分佈上確認增益。兩級組合測試的候選數量是單一慢速層的8.1倍（1,354 比 168），還多找到一個快7.2%的方案。團隊報告的 agent 實驗吞吐量，是重啟引擎基線的252倍。

📊 **數字說話：成本模型、知識庫反而幫倒忙**

一個成本模型會在 agent 開始之前，先依 spec-sheet 數據、微基準測試與實測 forward pass，外加實測到的 MoE 專家負載不均與請求長度差異，對 tensor/expert/data/context parallel 等排布方式排序。在 Kimi K3 上，它找到一個 TPS 提升達24%的生產排布。

有趣的是，給 agent 一份人工整理的專家知識庫，12小時後反而讓加速效果降低25%到31%；只被要求「盡可能快」的樸素 agent，表現反超遵循專家策略的版本——10輪試驗後整體分數是6.2倍對4.9倍。自訂日誌結構曾吃掉多達43%的工具呼叫，因此 Together AI 現在直接給 agent 引擎原始碼，而非中間表示。

在 SemiAnalysis InferenceX 的 AgentX 工作負載上，Together Compiler 比現有最佳開源配置快最多2.6倍 TPS，每項設定在至多2個節點上跑不到24小時。在 MiniMax 案例中，成本模型選擇了 TP8 而非基線的 TP4，讓每張 GPU 在記憶體受限的 decode 階段權重流量減半。在 Llama 1B、batch size 1 的場景，它比 Hazy Research megakernels、Mirage 與 CUDA-graph 基線快最多1.7倍；在8個科學模型上也取得1.5到6.4倍加速，且輸出位元級一致。用 Claude Code 搭配 /goal 則達到1.2到4.4倍，但在 AIFS-ENS 2.0 上失敗。

🎯 **實務啟示**

對維運大規模推理服務的團隊，這個案例點出一個容易被忽視的坑：用合成/隨機資料做的 kernel benchmark 可能完全不代表真實流量下的表現。與其追求「調一次用到老」，不如把調優做成能持續接收真實流量回饋的迴圈；同時，先用成本模型排序並行策略、再讓 agent 動手，看起來比直接丟給 agent 更穩健。

🔗 **來源**
- 標題：Together AI Releases Together Compiler: Agents Make Inference Up to 2.6x Faster
- 作者／機構：Asif Razzaq / MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/05/together-ai-together-compiler-continual-compilation-ai-inference/

#LLMInference #AIAgents #KernelOptimization #MoE #TogetherAI #GPUOptimization #CUDAGraphs #InferenceOptimization #MLSystems #AgenticAI
