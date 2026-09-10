---
title: Cognition launches new SWE-2 model, Rivaling Fable 5.1 and GPT-Astra
source: Hacker News
url: https://cognition.com/blog/swe-2
model: claude-code/sonnet
generated_at: '2026-09-10T19:53:27.085087'
score: 105
---

📌 Cognition SWE-2：用一次 RL 訓練跑遍所有成本等級

TL;DR：SWE-2 用單次 RL 訓練同時最佳化多個 effort 等級，逼近 GPT-6 Astra 但成本僅四分之一。

當 coding agent 一個比一個聰明，但也一個比一個貴，Cognition 這次選擇正面處理「智慧與成本」的取捨問題，而不是繼續單純堆參數。

🤔 **成本效能前緣，才是 Coding Agent 的真正戰場**

隨著模型愈來愈聰明也愈來愈貴，成本與效能的取捨在 coding agent 賽道上愈發重要。Cognition 訓練 SWE-2 的目標不只是拉高智慧程度，而是要把整個成本效能取捨的可選範圍一起往外推。SWE-2 是他們最新的 coding 模型，在 FrontierCode 1.1 Main 拿下 50.0%，與 Fable 5.1 差距不到一分，成本卻便宜 64%。

🧩 **多重 Effort 等級，一次 RL 訓練搞定**

SWE-2 是從 Kimi K3（2.8T 參數、已經歷大量 agentic coding RL 訓練）後訓練而來，延續 SWE-1.7 的訓練基礎設施與流程，首次把 RL 規模化到多兆參數等級。關鍵是一套新的 RL 演算法，能在單次訓練中同時訓練所有 effort 等級，推進整條成本效能前緣。

具體做法是採用成本懲罰的 reward 函式：R = S − λ_e × C。其中 S 屬於 {0,1}，代表該次 rollout 是否成功；C 代表 rollout 成本（推論費用與執行時間的綜合指標）；e 代表 effort 等級；λ_e 則依 base model 在該 effort 等級下 Pareto 曲線的斜率調校而來。這個設計是為了讓 RL 目標直接對齊模型在成本效能平面上的位置。此外，團隊也沿用自 SWE-1.6 以來使用的「長度加權 reward baseline」來穩定訓練，並改善了 RL rollout 的排程與線上 draft 模型的解碼吞吐量，搭配 NVFP4/FP8 kernel 與 quantization-aware training，在 base model 參數量幾乎是 SWE-1.7 三倍的情況下，維持相近吞吐量並降低訓練與推論的落差。訓練資料方面則把 RL 環境數量增為三倍，加入 instruction-following 疊加任務，並用先前版本的 SWE-2 checkpoint 建立飛輪機制，持續強化驗證器。

📊 **Benchmark 對照表**

| Benchmark | SWE-2 | Kimi K3 | Grok 4.6 | Fable 5.1 | GPT-5.6 Sol | GPT-6 Astra | SWE-1.7 |
|---|---|---|---|---|---|---|---|
| FrontierCode 1.1 Main | 50.0% | 44.2% | 48.0% | 50.9% | 47.5% | 53.3% | 42.0% |
| DeepSWE 1.1 | 73.0% | 68.5% | 67.5% | 67.4% | 72.7% | 74.1% | 37.7% |
| Terminal-Bench 2.1 | 92.8% | 88.3% | 88.4% | 91.4% | 88.8% | 89.9% | 81.5% |
| Terminal-Bench 4 | 27.3% | 21.5% | 20.3% | 55.8% | 37.3% | 57.9% | 7.6% |

SWE-2 在 FrontierCode 1.1 Main 與 DeepSWE 1.1 上同時勝過 SWE-1.7 與 Grok 4.6，且分數與成本都更好；在其他多個榜單上追平 GPT-5.6 Sol 與 Fable 5/5.1，價格卻只是零頭；與 GPT-6 Astra 相比僅差幾分，成本卻只要四分之一。

💡 **步數少了一半以上，行為也更聰明**

在 FrontierCode 1.1 Main 上，SWE-2 medium 的分數高於 SWE-1.7，平均步數卻少了 58%，成本低了 81%。平均步數：SWE-1.7 為 127 步，SWE-2 medium 53 步、high 80 步、max 98 步。團隊觀察到，效率提升主要來自「更聚焦的探索」：模型能更準確判斷程式庫裡哪些部分真正與任務相關，因此能更快進入實際修改。SWE-2 medium 平均在第 18 步就做出第一次真正的程式碼編輯，相較之下 SWE-1.7 需要 48 步。內部測試也觀察到三個行為特徵：測試覆蓋更完整、能捕捉端到端的迴歸與邊界情況；在遇到路徑受阻時更懂得變通（例如某次需要的 MCP 整合不可用，模型改從既有的 Slack 頻道歷史紀錄重建資料）；面對質疑時會重新推導結論，而不是單純重申，展現出更強的驗證紀律。不同 effort 等級也展現出明顯差異：medium 更快進入行動、適合處理簡單到中等任務；high 與 max 則在複雜任務上會做更多規劃、探索更多程式庫並透過更複雜的驗證管理不確定性。

🎯 **實務啟示**

SWE-2 已在 Devin Desktop 與 CLI 提供，並正在推廣到 Devin Web 與 Fusion。對於評估 coding agent 的團隊，這篇分享提供了一個值得參考的訓練思路：與其為每個成本檔位分別訓練專屬模型，用單一成本懲罰項在同一次 RL 訓練裡覆蓋所有 effort 等級，可能是更省資源、也更能維持模型行為一致性的做法。

🔗 **來源**
- 標題：Cognition launches new SWE-2 model, Rivaling Fable 5.1 and GPT-Astra
- 作者／機構：seelos, Hacker News
- 連結：https://cognition.com/blog/swe-2

#Cognition #DevinAI #CodingAgent #ReinforcementLearning #LLM #AgenticCoding #ParetoFrontier #KimiK3 #AIBenchmark #MachineLearning
