---
title: 'GLM-5.3 vs. GPT-5.6 Sol on DeepSWE: Cost, Coding, and Routing'
source: Together AI
url: https://www.together.ai/blog/glm-5-3-vs-gpt-5-6-sol-on-deepswe-cost-coding-and-routing
model: claude-code/sonnet
generated_at: '2026-08-22T06:27:58.128791'
score: 76
---

📌 GLM-5.3 vs GPT-5.6 Sol：先跑便宜模型，再升級才是最划算解

TL;DR：Together AI實測顯示，GLM-5.3先跑、失敗才升級Sol，比單用Sol貴模型準13個百分點還便宜21%。

單挑的話，GPT-5.6 Sol小勝GLM-5.3；但如果允許重試，開源挑戰者反過來領先。真正有意思的問題不是誰更強，而是：把兩個模型串起來用，是不是比只用貴的那個更好？

🤔 為什麼要放在一起比

Together AI把GPT-5.6 Sol定位為「精準旗艦」，GLM-5.3則是「持續縮小差距的開源挑戰者」。兩者被拿來在DeepSWE基準上正面對決，這是一個涵蓋多種任務類型與程式語言、用來評估模型軟體工程能力的基準測試。

🧩 測試設計：113個任務、4次試驗、904次rollout

Together AI對DeepSWE全部113個任務各跑了4次試驗，兩個模型合計跑出904次rollout（每邊452次），數據取自官方公開的逐次試驗紀錄。核心比較策略是「級聯」（cascade）：先讓GLM-5.3出手，只有在測試套件判定失敗時才升級交給Sol重跑。

📊 單次對比 vs 允許重試後的對比

| 指標 | GLM-5.3 [max] | GPT-5.6 Sol [max] |
|---|---|---|
| pass@1 | 69.0% | 72.7% |
| pass@2 / pass@4 | 81.1% / 87.6% | 81.0% / 85.8% |
| 平均成本／rollout | $3.99 | $8.37 |
| 每$100可解任務數 | 17 | 9 |
| 平均耗時／步數 | 35分鐘／124步 | 19分鐘／61步 |
| 測試套件回歸失敗率 | 11% | 20% |

單次挑戰Sol以72.7%對69.0%小勝GLM-5.3，差距3.7個百分點；但只要允許兩次嘗試，GLM-5.3就以81.1%追平Sol的81.0%，四次嘗試後更以87.6%反超Sol的85.8%。價格上GLM-5.3便宜2.1倍，同樣花$100，GLM-5.3能解17個任務、Sol只能解9個；但Sol更快更穩，平均19分鐘、61步就能完成一次rollout，遠低於GLM-5.3的35分鐘、124步。失敗模式上，Sol有20%的失敗案例會把原本通過的測試搞壞，GLM-5.3這個比例只有11%，多數失敗屬於「差一點但沒破壞既有基準」的近似未中。

若把GLM-5.3和Sol串成級聯策略，先跑GLM-5.3、測試失敗才交給Sol，最終解決率達到85.9%、平均每題$6.61，比單用Sol的72.7%、$8.37高出13個百分點、還便宜21%，甚至超過一個「完美單次路由器」的理論上限83.8%。

💡 兩個模型真的走不同的路

兩模型在單一任務上的表現相關係數只有0.43，代表它們的錯誤模式明顯不同：兩者合計能覆蓋113個任務中的106個（93.8%），其中GLM-5.3獨力解出9個Sol完全解不出的任務，Sol獨力解出7個GLM-5.3解不出的任務。在語言與領域分布上，Sol在資料建模與序列化（92%）、建置與維運工具鏈（73%）、並行與持久性（72%）、協定一致性（59%）上佔優；GLM-5.3則在查詢與設定語言（88%，全榜最高單項）、語言與執行環境內部機制（83%）、狀態化反應式邏輯（73%）上領先，並在程式分析項目與Sol打平（64比64）。程式語言上，GLM-5.3的JavaScript表現（90%）是全榜最佳，也在Rust上領先（70比60）；Sol則在Python（74比66）、Go（79比76）、TypeScript（66比61）上更強。

⚠️ 這些數字只代表這一次測試

Together AI特別註明，這些數據來自他們自己這次的測試跑分，不同機構公開的GLM-5.3對GPT-5.6 Sol跑分結果可能有出入。另外，Sol的20%回歸失敗率意味著它的輸出不能無條件信任，需要用完整的回歸測試守住。

🎯 給正在做模型路由的工程團隊

如果團隊在打造程式碼修復或自動化工程Agent，這份結果指向一個具體策略：不必二選一，而是把便宜模型當前端、失敗再升級到旗艦模型做二次嘗試，比單押任何一個模型都更划算；已知任務語言時可以進一步分流，JavaScript與Rust交給GLM-5.3、其餘交給Sol；不論用哪個模型，Sol的輸出尤其需要包一層完整回歸測試再接受它的diff。

🔗 來源
- 標題：GLM-5.3 vs. GPT-5.6 Sol on DeepSWE: Cost, Coding, and Routing
- 作者／機構：Together AI
- 連結：https://www.together.ai/blog/glm-5-3-vs-gpt-5-6-sol-on-deepswe-cost-coding-and-routing

#LLM #CodingAgents #GLM #GPT #Benchmark #SoftwareEngineering #CostOptimization #ModelRouting #AIAgents #DeepSWE
