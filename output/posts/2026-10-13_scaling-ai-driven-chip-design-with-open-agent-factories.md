---
title: Scaling AI-driven chip design with open agent factories
source: IBM Research
url: https://research.ibm.com/blog/open-agent-factories-and-distributed-inference-for-chip-design?utm_medium=rss&utm_source=rss
model: claude-code/sonnet
generated_at: '2026-10-13T22:04:10.835667'
score: 94
---

📌 【IBM Research】開源模型做晶片設計，成本只要專有模型十一分之一

TL;DR：IBM用開源前沿模型組成agent factory最佳化量子錯誤校正晶片，52倍加速只花約26美元推論成本。

一個好演算法離真正的晶片還有很長的路,把演算法轉成高效硬體，需要反覆試驗不同的運算組織、資料搬移與資源配置方式，而這個探索空間大到人類難以窮舉。IBM Research的新研究給出了一個關鍵數字：用開源前沿模型組成的agent factory，只花約26美元的推論成本，就把硬體設計的高層次合成（HLS）估計效能加速了52倍。

🤔 **硬體設計的探索空間太大，而AI agent探索的成本本身就是瓶頸**

High Level Synthesis（HLS）把硬體設計的抽象層級從RTL（register-transfer level）提高到C或C++，但工程師仍必須為迴圈結構、平行化、記憶體組織、資料流與合成指令做無數決策，而這些選擇彼此交互影響,例如同時做更多運算，只有在記憶體系統能供應足夠輸入時才有意義。AI agent能協同探索這個空間：提出架構變更、寫出實作、檢查正確性，並根據合成結果決定下一步要嘗試什麼。問題在於成本,單次搜尋campaign可能耗費數億個token，若要把這套方法套用到許多元件與多輪設計修訂，可能需要上百次這樣的campaign。

🧩 **Agent factory：一個協調者agent，帶著四個平行worker探索硬體設計**

IBM Research Fellow暨首席科學家Ruchir Puri將agent factory描述為「把硬體最佳化變成一個協調過的探索循環：協調者agent在設定好的搜尋預算內，指揮平行的worker agent開發並合成不同的設計方案」。驗證器（verifier）檢查提出的改進是否有效，再依延遲與硬體資源使用量為設計排名，這些結果引導下一輪探索，讓factory能隨著發現更好的設計而逐步修正搜尋方向。

在這次研究中，協調者規劃搜尋並把最佳化假設分配給四個平行的worker agent，worker負責修改decoder實作，正確性檢查與HLS結果則為後續輪次提供回饋。每個設定的搜尋預算都是100個假設。agent探索的變更帶有架構層級的意義：其中一項轉換重新組織了訊息儲存方式，讓合成工具能辨識出獨立的記憶體存取並平行執行更多運算；另一項則把序列式的reduction運算換成樹狀結構，暴露出更多可平行化的運算。

研究用來驗證方法的目標，是Relay-BP,一種用於[[144,12,12]] bivariate bicycle code的量子錯誤校正解碼演算法。量子錯誤校正依賴傳統運算：量測結果提供錯誤線索，decoder必須解讀線索並推斷修正，而且要在實際硬體資源限制內快速完成。Relay-BP的重複訊息傳遞本質上具有平行性，但其基準實作的稀疏圖表示與記憶體存取模式，讓HLS工具難以挖掘出這種平行性，是測試AI驅動硬體探索能力的高難度案例。

📊 **同樣100個假設的搜尋預算，三種設定換到完全不同的成本與加速倍數**

研究團隊在相同的100假設搜尋預算下，比較了三種設定：協調者與worker都用專有前沿模型、協調者與worker都用開源前沿模型，以及協調者用專有模型、worker用開源模型的混合設定。開源模型透過llm-d在地端執行。

| 設定 | 加速倍數 | 推論成本 | 用量 |
|---|---|---|---|
| 全專有模型 | 204x | 299美元 | 約2.16億tokens |
| 全開源模型 | 52x | 26美元 | 約2.41億tokens |

三種設定都找到了經驗證的硬體改進，但取捨方向不同:開源與混合搜尋找到了實用的精簡設計，而專有模型設定更有效地把額外資源轉換成平行度與更低延遲,也就是說，全專有設定達成更高的204倍加速，但成本是全開源設定的11.5倍（299美元對26美元）。值得注意的是，全開源搜尋反而用了更多token（約2.41億，高於全專有設定的約2.16億），它的成本優勢來自服務這些token的經濟性，而不是token用量更省。

💡 **為什麼推論基礎設施本身，會決定agent factory劃不划算**

agent factory反覆回頭參照大量相同的上下文資訊：原始碼、設計限制、先前的修改與合成報告。研究使用開源的分散式推論框架llm-d來支撐這個workload，它的cache-aware routing會把請求導向持有可重複利用上下文的伺服器，同時把prompt處理和token生成拆開，讓系統能分別為兩者配置資源。這解釋了為什麼即使token用量更高，全開源設定的成本仍遠低於全專有設定。

⚠️ **每種設定只跑了一次搜尋，結論是觀察而非通用排名**

研究團隊特別註明，每個設定只在一次搜尋run中被評估，因此這些結果反映的是「觀察到的搜尋過程」，而非建立一個通用的模型排名。報告的成本也只涵蓋模型推論本身，不包含完整硬體開發流程的其他成本。

🎯 **對工程團隊的意義：划算的探索預算，可能比單次最佳設計更重要**

這項研究指出，AI輔助晶片設計的實際價值，不只取決於agent能產出的最佳設計，還取決於一個組織能負擔多少「經過驗證的探索」。模型能力、agent角色分配，以及背後的推論服務基礎設施，共同決定了在真實工程預算內能拿到多少硬體改進。省下的成本，等於可以拿去投入更多輪搜尋，去找更好的設計。

🔗 **來源**
- 標題：Scaling AI-driven chip design with open agent factories
- 作者／機構：IBM Research
- 連結：https://research.ibm.com/blog/open-agent-factories-and-distributed-inference-for-chip-design?utm_medium=rss&utm_source=rss

#IBMResearch #ChipDesign #AIAgents #AgentFactory #QuantumComputing #HighLevelSynthesis #OpenSourceAI #DistributedInference #llmd #HardwareOptimization
