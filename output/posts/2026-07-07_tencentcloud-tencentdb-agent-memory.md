---
title: TencentCloud/TencentDB-Agent-Memory
source: GitHub Trending
url: https://github.com/TencentCloud/TencentDB-Agent-Memory
score: 96
model: google/gemma-4-31b-it:free
generated_at: '2026-07-07T21:15:14.006672'
---

📌 TencentDB Agent Memory：符號化短期記憶＋分層長期記憶，降低 Token 用量並提升任務成功率  

TL;DR：透過 Symbolic Short‑Term Memory 與 Layered Long‑Term Memory，TencentDB Agent Memory 在 OpenClaw 場景下最多可減少 61.38% Token，用量，同時將 PersonaMem 準確率從 48% 提升至 76%。  

🧩 **符號化短期記憶的核心概念**  
- 代理人在執行工具時會產生大量日誌，若直接保留在對話中會吃掉大量 Token。  
- 本專案將這些日誌「壓縮」為 Mermaid 符號（簡潔的圖形描述），形成 Symbolic Short‑Term Memory。  
- 壓縮後的資訊仍保留關鍵結構，卻大幅降低文字量，減少模型推論時的 Token 開銷。  

🧩 **分層長期記憶的設計理念**  
- 長期記憶不採用單一向量堆疊，而是將斷裂的對話片段整理成「Persona」與「Scene」兩層結構。  
- Persona 代表使用者或角色的固定屬性，Scene 則記錄特定情境下的互動細節。  
- 這種層次化的表示讓代理人在需要回溯時能快速定位相關資訊，避免在長程會話中重複說明 SOP、專案背景等固定內容。  

📊 **效能測試結果（OpenClaw 整合）**  
| 測試專案 | 無 Plugin 成功率 | 使用 Plugin 成功率 | 成功率提升 (相對) | 無 Plugin Token | 使用 Plugin Token | Token 減少率 |
|---|---|---|---|---|---|---|
| WideSearch (短期) | 33% | 50% | +51.52% | 221.31M | 85.64M | **‑61.38%** |
| SWE‑bench (短期) | 58.4% | 64.2% | +9.93% | 3474.1M | 2375.4M | **‑33.09%** |
| AA‑LCR (短期) | 44.0% | 47.5% | +7.95% | 112.0M | 77.3M | **‑30.98%** |
| PersonaMem (長期) | 48% | 76% | +59% | — | — | — |

- 以上資料均為連續長時段會話的測量，非單回合測試。  
- 例如 SWE‑bench 會在同一次會話中執行 50 個連續任務，以模擬真實長程代理人的上下文累積壓力。  

💡 **實務啟示**  
- 若你的 AI 代理人需要頻繁呼叫外部工具或在長時間會話中保持一致性，匯入 Symbolic Short‑Term Memory 可顯著降低 Token 成本。  
- 分層長期記憶的 Persona/Scene 結構適合儲存 SOP、專案說明、輸出格式等「不變」資訊，減少使用者重複說明的負擔。  
- 在 OpenClaw 等需要大量外掛互動的場景下，結合本專案可同時提升成功率與效能，對成本敏感的商業部署特別有價值。  

🔗 來源  
- 標題：TencentCloud/TencentDB-Agent-Memory  
- 作者／機構：TencentCloud  
- 連結：https://github.com/TencentCloud/TencentDB-Agent-Memory  

#AI #AgentMemory #TokenOptimization #LongTermMemory #ShortTermMemory #Mermaid #OpenClaw #TencentCloud #LLM #PromptEngineering  
