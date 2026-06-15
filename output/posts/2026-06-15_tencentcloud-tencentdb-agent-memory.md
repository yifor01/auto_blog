---
title: TencentCloud/TencentDB-Agent-Memory
source: GitHub Trending
url: https://github.com/TencentCloud/TencentDB-Agent-Memory
score: 98
model: google/gemma-4-31b-it:free
generated_at: '2026-06-15T21:14:47.265014'
---

📌 【TencentCloud 最新開源】不再讓 AI 遺忘：符號化記憶與分層結構，大幅降低 Token 消耗

你是否發現 AI Agent 在處理長程任務時，會因為對話過長而「記憶混亂」，或者你必須反覆向它解釋相同的 SOP、專案背景與輸出格式？

目前的 RAG 或簡單的向量儲存（Vector Store）往往將記憶視為「扁平的資料堆疊」，導致 Token 消耗劇增且檢索精準度下降。TencentCloud 提出的 TencentDB-Agent-Memory 試圖改變這個現狀：記憶不應該是單純的囤積，而應該是精準的提取。

🤔 **記憶的痛點：重複解釋 SOP 與 Token 的浪費**

在實際應用中，開發者經常發現 Agent 在長時間交互後，會忘記之前的工具約定或專案背景，導致我們必須不斷重複同樣的指令。這種「認知重複」不僅降低效率，更讓 Token 成本在長程 session 中呈指數級增長。

🧪 **核心設計：符號化短期記憶 + 分層長期記憶**

TencentDB-Agent-Memory 捨棄了傳統的全量儲存，採用了一套更像人類思考的記憶結構：

1. **符號化短期記憶 (Symbolic Short-term Memory)**：
將沉重的工具日誌（Tool Logs）壓縮成精簡的 Mermaid 符號。透過將複雜過程「符號化」，在保留關鍵邏輯的同時，大幅削減輸入的 Token 數量。

2. **分層長期記憶 (Layered Long-term Memory)**：
不再將對話碎片化地丟進向量資料庫，而是將碎片資訊蒸餾（Distill）成結構化的「人格 (Personas)」與「場景 (Scenes)」。這種結構化儲存讓 AI 能更精準地定位身份與環境，而非在海量向量中盲目搜尋。

📊 **實測數據：Token 降低 61%，成功率提升 51%**

團隊將此記憶模組整合至 OpenClaw 並在長程任務（Long-horizon sessions）中進行壓力測試，結果相當顯著：

- **WideSearch 任務**：成功率從 33% 提升至 50% (相對提升 51.52%)，且 Token 消耗從 221.31M 降至 85.64M (降低 61.38%)。
- **SWE-bench 任務**：在連續 50 個任務的壓力測試下，成功率提升至 64.2%，Token 消耗降低 33.09%。
- **PersonaMem 準確率**：從 48% 大幅提升至 76%。

值得注意的是，這些數據是在「連續長程對話」而非單次問答中測得，這更貼近現實中 AI Agent 處理複雜專案的實際壓力場景。

💡 **從「資料堆疊」轉向「結構化蒸餾」**

這項研究的核心洞察在於：高效的記憶不在於「記得所有細節」，而在於「如何壓縮細節」。
短期記憶透過「符號化」減少冗餘，長期記憶透過「分層化」建立結構。這種設計讓 Agent 能在維持上下文理解力的前提下，顯著降低推理成本，並在長程交互中保持一致的行為模式。

⚠️ **目前僅提供 Benchmark 數據，實際部署效果視模型而定**

雖然量化數據亮眼，但實際效果仍會受到底層 LLM 處理符號化資訊（如 Mermaid 符號）能力的影響。不同模型對這種壓縮格式的理解程度可能有所差異，實作時需針對特定模型進行調優。

🎯 **工程實踐：開發長程 Agent 的優化方向**

對於正在開發 AI Agent 的工程師，這套方案提供了兩個可落地的優化方向：
- **嘗試將 Log 結構化**：不要直接將所有 Tool Output 餵回 LLM，嘗試將其轉換為簡潔的狀態符號。
- **建立 Persona 配置文件**：將用戶偏好與場景設定從對話紀錄中抽離，轉化為結構化的 Persona 模組，而非依賴 RAG 檢索。

🔗 **專案連結**
📝 TencentDB-Agent-Memory
👤 TencentCloud
🔗 GitHub：https://github.com/TencentCloud/TencentDB-Agent-Memory
(支援 TypeScript 實作，可快速上手)

你目前在開發 Agent 時，是如何處理長程記憶與 Token 成本平衡的？歡迎在評論區分享你的實作經驗 👇

#AI #LLM #Agent #TencentCloud #MemoryManagement #TokenOptimization #TypeScript #OpenSource
