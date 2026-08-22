---
title: NVIDIA AVO Reaches 100% on ARC-AGI-3, Demonstrating a Frontier-Level General-Purpose
  Architecture for Long-Horizon Autonomous Agents
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/nvidia-avo-reaches-100-on-arc-agi-3-demonstrating-a-frontier-level-general-purpose-architecture-for-long-horizon-autonomous-agents/
model: claude-code/sonnet
generated_at: '2026-08-22T06:12:56.087507'
score: 105
---

📌 【NVIDIA 研究】AVO 在 ARC-AGI-3 拿下滿分,關鍵不是模型是架構

TL;DR:NVIDIA 的長時程代理架構 AVO,在 ARC-AGI-3 公開測試集達到 100.00 RHAE,顯示 agent harness 的設計可能比模型本身更決定成敗。

一個前沿語言模型只是 AI 代理的其中一個零件。真正決定代理能不能在長時間、多步驟任務中穩定運作的,是模型周圍那層系統,也就是所謂的 harness:它負責模型如何接收上下文、使用工具、維持狀態、回應回饋、從失敗中恢復,並在長時間任務中持續推進。

🤔 打造能撐過長時程任務的代理架構

NVIDIA 的研究專案 Agentic Variation Operators（AVO）正是為了解決這個問題:如何打造一個通用的代理架構,讓前沿模型能可靠地完成延伸、多步驟的任務。AVO 最初被用於高難度的軟體工程與 GPU 核心最佳化任務,這類任務要求代理不只是產生程式碼,而是要檢視既有實作、形成假設、進行修改、執行硬體層級的測試、解讀回饋,並反覆修正方向。

🧩 持久記憶與監督者:讓進度不因單一 context 而中斷

AVO 是一個通用的程式碼代理系統,能檢視與編輯程式碼、執行指令、查閱文件,並透過實際執行驗證自己的成果,其特色在於能維持長時間的自主運作。在 GPU 核心最佳化的應用中,AVO 取代了傳統演化搜尋系統裡預先定義的變異步驟,改由自主代理決定下一個候選方案要檢視什麼、修改什麼、測試什麼、提交什麼。

架構中有兩個關鍵機制:持久記憶會延續先前的實作、評估結果、編譯器與效能分析器輸出,以及累積的推理過程,讓代理能從目前狀態接續,而不必每次重新建構搜尋;監督者則監看整體搜尋軌跡是否停滯或陷入重複的無效循環,並在需要時把主代理導向其他策略。

📊 七天跑出 40 個核心版本,再到 ARC-AGI-3 拿下滿分

在 attention 核心研究中,AVO 連續運作七天,探索超過 500 個最佳化方向,產出 40 個提交的核心版本。在 NVIDIA DGX B200 系統上,最終的 multihead attention 核心在評測配置中比 cuDNN 快最多 3.5%,比 FlashAttention-4 快最多 10.5%。代理隨後只花了大約 30 分鐘的自主工作,就把演化出的核心調整套用到 grouped-query attention。

團隊接著把同一套 AVO 架構接上完全不同的挑戰:互動式推理基準 ARC-AGI-3。在這個基準中,代理進入陌生環境,沒有說明、沒有明訂規則、也沒有明確目標。AVO 在公開測試集的全部 25 個環境中達到 100.00 的 RHAE（Relative Human Action Efficiency,結合任務完成度與相對人類基準的每關動作效率）分數,完成了全部 183 個關卡。

💡 換了領域,核心迴圈沒有變

GPU 核心最佳化與 ARC-AGI-3 表面上差異很大,一個涉及原始碼、編譯器、效能分析器與吞吐量,另一個則是要在陌生互動環境中推斷可用動作的效果、發掘目標並有效率地行動。但底層的運算模式其實相似:代理都必須從不完整的證據建立假設、透過外部介面採取行動、觀察後果、保留有用的狀態、修正對問題的理解、從錯誤假設中恢復,並在長時程中持續推進。領域變了,回饋管道變了,但核心的代理迴圈沒有變。

團隊在建構 ARC-AGI-3 系統時,沒有採用 Tycho 所探討的明確程式化世界模型建構方式,而是採用 VISTA 所描述的直接互動設計原則,並獨立重新實作任務介面。VISTA 的主要設定是透過 Claude Code 使用 Claude Opus 5,或透過 Codex 使用 GPT-5.6 Sol 來實例化 harness,而 NVIDIA 的系統使用的是自家的 AVO 架構,具備持久記憶、監督者與自己的執行迴圈；觀察介面也不同,VISTA 主要使用 512x512 的 PNG 渲染畫面,同時也探索文字網格表示法。

🎯 評估模型和評估代理是兩件事

這個結果點出一個更廣的道理:評估一個模型不等於評估一個代理。模型能力固然重要,但真正決定這份能力能否轉化為持續自主進展的,是模型周圍的系統設計。對正在打造 agentic 系統的工程師來說,值得思考的重點或許不是換更強的模型,而是投資在持久記憶、監督機制這類讓進度得以延續的系統層設計。

🔗 來源
- 標題：NVIDIA AVO Reaches 100% on ARC-AGI-3, Demonstrating a Frontier-Level General-Purpose Architecture for Long-Horizon Autonomous Agents
- 作者／機構：Tanya Lenz, NVIDIA
- 連結：https://developer.nvidia.com/blog/nvidia-avo-reaches-100-on-arc-agi-3-demonstrating-a-frontier-level-general-purpose-architecture-for-long-horizon-autonomous-agents/

#NVIDIA #AVO #ARCAGI3 #AIAgents #LongHorizonAgents #AgenticAI #GPUKernel #AutonomousAgents #AIArchitecture #AgentHarness
