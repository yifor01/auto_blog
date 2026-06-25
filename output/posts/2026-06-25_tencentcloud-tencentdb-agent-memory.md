---
title: TencentCloud/TencentDB-Agent-Memory
source: GitHub Trending
url: https://github.com/TencentCloud/TencentDB-Agent-Memory
score: 88
model: google/gemma-4-31b-it:free
generated_at: '2026-06-25T20:35:03.969160'
---

📌 【TencentCloud】TencentDB-Agent-Memory：用「符號化」與「分層記憶」解決 Agent Token 爆炸問題

TL;DR：透過符號化短期記憶與分層長期記憶，最高降低 61.38% Token 消耗並提升 51.52% 任務成功率。

在開發長對話 Agent 時，工程師常陷入一個矛盾：為了讓 AI 記得 SOP 和背景，必須餵入大量上下文，但這會導致 Token 消耗激增且雜訊增加，最終導致 Agent 在長程任務中迷失方向。

🧩 **符號化短期記憶與分層長期記憶的設計理念**

TencentDB-Agent-Memory 提出一套記憶管理機制，不再將所有資訊平鋪在 Context 中，而是將記憶拆分為兩種模式：

- **符號化短期記憶（Symbolic Short-term Memory）**：將沉重的工具日誌（Tool Logs）壓縮成精簡的 Mermaid 符號。透過將詳細日誌「符號化」，大幅減少 Token 佔用，同時提升任務成功率。
- **分層長期記憶（Layered Long-term Memory）**：捨棄傳統的扁平向量堆疊（Flat Vector Piles），將碎片化的對話提煉成結構化的「人物誌（Personas）」與「場景（Scenes）」。

📊 **實測資料：大幅降低 Token 成本並提升成功率**

當該記憶模組整合至 OpenClaw 時，在長程對話（Long-horizon sessions）的壓力測試下表現顯著：

| 測試場景 | 成功率 (OpenClaw) | 成功率 (含 Plugin) | 相對提升 ($\Delta$) | 原 Token 消耗 | Plugin 後 Token | 相對減少 ($\Delta$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| WideSearch (短期) | 33% | 50% | +51.52% | 221.31M | 85.64M | -61.38% |
| SWE-bench (短期) | 58.4% | 64.2% | +9.93% | 3474.1M | 2375.4M | -33.09% |
| AA-LCR (短期) | 44.0% | 47.5% | +7.95% | 112.0M | 77.3M | -30.98% |
| PersonaMem (長期) | 48% | 76% | +59% | — | — | — |

值得注意的是，這些資料是在連續長程會話中測得，而非單次對話。例如在 SWE-bench 測試中，每個會話連續執行 50 個任務，用以模擬現實世界中 Agent 面對的上下文累積壓力。

💡 **從「囤積」轉向「提煉」的記憶管理**

該專案的核心觀點在於：記憶的目的不是將所有資訊塞進 AI，而是讓人類不需要重複解釋相同的 SOP、專案背景、工具慣例或輸出格式。透過將碎片資訊結構化，Agent 能更精準地提取有效資訊，而非在海量向量中搜尋。

🎯 **實務啟示**

對於開發複雜 Agent 的工程師，這提供了一個最佳化方向：不要試圖透過增加 Context Window 來解決記憶問題，而應思考如何將「日誌符號化」以及將「對話結構化」，將重複性的背景資訊從動態對話中抽離，轉化為靜態的結構化定義。

🔗 **來源**
- 標題：TencentCloud/TencentDB-Agent-Memory
- 作者／機構：TencentCloud
- 連結：https://github.com/TencentCloud/TencentDB-Agent-Memory

#AI #LLM #Agent #MemoryManagement #TokenOptimization #TencentCloud #OpenClaw #ShortTermMemory #LongTermMemory #SoftwareEngineering
