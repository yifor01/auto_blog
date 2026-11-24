---
title: 'Import AI 482: Huawei kernel benchmarks; airborne drone detection; and a national
  lab’s AI science benchmark'
source: Import AI
url: https://jack-clark.net/2026/11/23/import-ai-482-huawei-kernel-benchmarks-airborne-drone-detection-and-a-national-labs-ai-science-benchmark/
model: claude-code/sonnet
generated_at: '2026-11-24T03:37:01.255916'
score: 90
---

📌 出口管制逼出來的解法：深圳研究院發布華為Ascend晶片核心優化基準AscendGYM

TL;DR：AscendGYM是針對華為Ascend NPU的核心優化基準，用來評測AI agent改善晶片效能的能力。

美國出口管制擋住了中國取得前沿西方半導體的路，逼得中國企業只能在手上既有的華為Ascend晶片上想辦法榨出更多效能。最新發布的AscendGYM，就是要讓AI agent自己上場，幫忙把這些晶片的核心運算（kernel）效能一步步優化上去。

🤔 **背景：被出口管制逼出來的自我優化需求**

深圳合作區研究院（Shenzhen Loop Area Institute）這個中國研究機構打造並發布了AscendGYM，一套「針對Ascend NPU的核心優化基準」。其目標是讓AI更容易為華為的Ascend晶片開發客製化kernel，這對於無法取得前沿西方晶片、被迫轉向華為硬體的中國組織而言格外重要。

🧩 **AscendGYM要回答的核心問題**

AscendGYM設計者希望這套工具能回答：「給定一個正確的kernel實作，特定agent能否在可接受預算內進一步提升其在目標workload上的效能，同時維持正確性？」為此，AscendGYM從三個維度評估：跨案例的適用性（cross-case applicability）、針對特定shape與場景能達到的最佳效能（shape specialization），以及取得這些效能提升所需付出的優化成本（optimization efficiency）。工具內建名為AscendForge的評測環境，提供編譯、正確性檢查、效能測量與回饋的統一介面。

📊 **測試結果：Opus 5拿下最佳成績，Claude Code是最強舞臺**

研究團隊在Claude Code、Codex、OpenCode三種agent harness下測試不同模型的表現：

| 排名 | 模型 |
|---|---|
| 1 | Opus 5 |
| 2 | GPT-5.6 |
| 3 | GLM-5.3 |

其中Claude Code整體拿到最高的絕對分數，GLM-5.3在Claude Code裡表現不錯，而GPT-5.6則在Codex裡表現較好；另外Opus 5相對更耗費token，GPT-5.6的token使用效率更高。

💡 **為何重要：中國版「自我改進」的關鍵拼圖**

AI系統要能自我改進（recursive self-improvement, RSI），前提是要能開發並優化自己訓練與推理所依賴的軟體。像AscendGYM這樣的基準，將成為中國快速提升自身運算基礎效率的重要工具，也直接關係到出口管制格局下，中國晶片能否透過軟體層面的優化縮小與西方晶片的效能差距。

🎯 **對工程師的實務啟示**

AscendForge「編譯、正確性檢查、效能測量、回饋」四件套的統一介面設計，以及跨案例適用性、shape特化、優化成本三個維度並重的評分思路，都是設計kernel optimization agent評測框架時值得參考的模式，不只限於Ascend晶片，也能套用在其他硬體平臺的agent化效能優化評測上。

🔗 **來源**
- 標題：Import AI 482: Huawei kernel benchmarks; airborne drone detection; and a national lab's AI science benchmark
- 作者／機構：Jack Clark, Import AI
- 連結：https://jack-clark.net/2026/11/23/import-ai-482-huawei-kernel-benchmarks-airborne-drone-detection-and-a-national-labs-ai-science-benchmark/

#Huawei #AscendNPU #AIAgents #KernelOptimization #SemiconductorAI #ChipDesign #ExportControls #LLMAgents #AIBenchmark #RSI
