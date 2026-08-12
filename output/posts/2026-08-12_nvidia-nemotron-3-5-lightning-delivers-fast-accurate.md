---
title: NVIDIA Nemotron 3.5 Lightning Delivers Fast, Accurate Specialized Task Execution
  for Long-Running Agents
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/
model: claude-code/sonnet
generated_at: '2026-08-12T07:29:35.279370'
score: 98
---

📌 【NVIDIA】別讓前沿模型處理每一次 git pull:Nemotron 3.5 Lightning 專攻 Agent 執行層

TL;DR:Nemotron 3.5 Lightning 是專為長時間運作 agent 高頻執行任務設計的開源 30B MoE 模型。

長時間運作的 AI agent,大多數時間並不是在「思考」,而是在執行:呼叫工具、驗證結果、把任務分派給子 agent。如果每一步都動用前沿級推理模型,成本與延遲都會被拖垮。NVIDIA 這次針對的正是這一層。

🤔 **解決什麼問題:agent 的「執行層」需要專屬模型**

NVIDIA Developer 部落格指出,開發者正愈來愈常用「一組模型」而非單一模型來建構應用:像 Nemotron 3 Ultra 這樣的前沿推理模型負責協調與複雜規劃,較小、較有效率的模型則負責高頻的執行層工作。Nemotron 3.5 Lightning 就是為這個執行層打造的模型,設計上鎖定 OpenClaw、Hermes Agent 這類 agent harness,並由開源的 NVIDIA NemoClaw 安全與管理堆疊支援,用於運行常駐運作的 AI agent。

🧩 **核心架構:30B MoE、3B 活躍參數,加上投機解碼**

Nemotron 3.5 Lightning 是一個可客製化的開源 30B 混合專家(MoE)模型,活躍參數只有 3B。MoE 的原理是用一個路由器(router)把每個 token 只送進眾多專家中的少數幾個,因此每個 token 實際運算只用到一小部分參數,等於用小模型的運算成本,取得較大密集模型的容量。

作為 Nemotron 3 家族中最小的成員,Lightning 沿用了家族中已驗證過的多項技術:訓練階段就內建多 token 預測(multi-token prediction, MTP),與 Nemotron 3 Super、Ultra 相同做法,並額外提供 DFlash 與 DSpark 兩個草稿模型(draft model),讓推理最佳化能涵蓋更廣的服務情境。模型也針對主流 agent harness 做了訓練,讓 agent 在高頻任務中的呼叫更準確、延遲更低。

🧩 **怎麼用:開箱即可客製,並用 NeMo Switchyard 做路由**

與 Nemotron 系列每次發布相同,Lightning 的權重、訓練資料與訓練配方都以 OpenMDW-1.1 授權盡可能開放釋出。開發者可以用 NeMo Automodel 與 NeMo Megatron Bridge 做 LoRA 或全參數 SFT 微調,也可以用 NeMo RL 與 NeMo Gym 執行強化學習與環境化評估。這次發布同時附上 Nemotron-RL Agentic Terminal Pivot,一個用來訓練部分程式碼 agent 能力的開源 agentic 強化學習資料集。

模型也提供 NVFP4 與 BF16 兩種格式的檢查點,NVFP4 使用與 Nemotron 3 Ultra 相同的專屬核心,可在 NVIDIA Blackwell、Hopper、Ampere 架構的 GPU 上運行,同一份檔案能同時服務資料中心與桌上型 DGX Spark。

任務路由則交給新發布的 NVIDIA NeMo Switchyard 函式庫負責,它能把 Lightning 曝露為路由目標之一,與其他開放或封閉模型並列,讓規劃類任務往上路由給前沿模型、執行類任務往下路由給 Lightning,確保 token 花在對的地方。

📊 **準確度與速度的權衡曲線**

在整合九項評測(涵蓋 agentic 任務、程式設計、科學推理與一般智力)的 Artificial Analysis Intelligence Index 上,Nemotron 3.5 Lightning 在同量級模型中取得準確度與輸出速度雙贏的 Pareto frontier,輸出速度最高可達同量級模型的 4 倍。在 PinchBench 上,Lightning 以 86% 準確率完成 1 萬個任務,速度比準確率相近的 Qwen3.6 35B 快 30%。NVIDIA 也與 EXO Labs 合作測試模型在 DGX Spark 上的表現,結果顯示 Lightning 在 EXO Labs 的 local.ai 排行榜上同樣落在同量級開源模型的 Pareto frontier 上。

⚠️ **定位:執行層專用,不是取代前沿模型**

Lightning 明確被定位為「執行層」模型,而非取代 Nemotron 3 Ultra 這類負責複雜規劃與協調的前沿模型。它可以在 NVIDIA Jetson、GeForce RTX 5090、DGX Spark 等本地裝置運行,也支援 LM Studio、llama.cpp、Ollama、Unsloth 等主流工具鏈,適合作為多模型系統中負責高頻、低延遲工作的那一環,而不是單獨扛起整個 agent 系統的智慧。

🎯 **對工程師的啟示**

如果你的 agent 系統把大量 token 花在驗證工具輸出、格式化結果、執行常規呼叫這類重複性高的步驟上,把這些工作從前沿模型卸載到 Lightning 這類執行層模型,再搭配 NeMo Switchyard 做路由,是一個值得評估的成本與延遲最佳化方向。開放的權重與訓練配方,也讓團隊可以針對自己的 harness 再做進一步微調。

🔗 **來源**
- 標題:NVIDIA Nemotron 3.5 Lightning Delivers Fast, Accurate Specialized Task Execution for Long-Running Agents
- 作者／機構:Tanya Lenz, NVIDIA Developer
- 連結:https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/

#NVIDIA #Nemotron #MoE #AIAgent #OpenModel #SpeculativeDecoding #NeMoSwitchyard #DGXSpark #LLMRouting #AgenticAI
