---
title: Scaling Agentic AI Factories Through Extreme Co-Design with NVIDIA BlueField
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/scaling-agentic-ai-factories-through-extreme-co-design-with-nvidia-bluefield/
score: 101
model: tencent/hy3:free
generated_at: '2026-07-17T08:06:24.660229'
---

📌 【NVIDIA 開發者部落格】用 BlueField 極致協同設計擴展 Agentic AI 工廠

TL;DR：NVIDIA 以 BlueField-4 DPU 與 DOCA 卸載基礎建設，提升 AI 工廠 GPU 利用率與每瓦代幣數。

Agentic AI 把推理從單次模型呼叫變成跨步驟的分散式工作流，當數十個 agent 同時帶著上下文跑任務，傳統靠主機 CPU 扛網路、儲存與安全的方式，很容易成為拖慢 GPU 的瓶頸。

🤔 **Agentic AI 讓基礎建設負載大幅重組**

一個使用者請求可能觸發多個模型呼叫、工具呼叫、記憶體查詢、政策檢查、儲存存取與網路傳輸，才產出最終回答。隨著並行 agent 數量增加，且上下文跨步驟、使用者、工具、服務與會話流動，基礎建設必須高速移動、保護、檢索與重複使用資料，才能維持 GPU 與 CPU 的產出效率。

🧩 **BlueField 平臺把基礎建設處理搬進專用資料路徑**

NVIDIA BlueField 平臺在 AI 工廠的資料路徑中提供專用且可程式化的基礎建設處理：從主機 CPU 卸載（offload）基礎建設工作、加速資料移動、inline 強制執行政策，並將網路、儲存、安全、遙測與上下文管理隔離處理。

涉及的硬體與軟體元件包含：
- NVIDIA BlueField-4 DPU
- Vera BlueField-4 STX Storage Processor
- DOCA 軟體平臺

BlueField-4 整合最高 800 Gb/s 的 Ethernet 或 InfiniBand、64 核心 NVIDIA Grace CPU、PCIe Gen6，以及高頻寬 LPDDR5X 記憶體。BlueField-4 STX 透過 DOCA Memos 提供 KV cache 管理，支援 AI-native 儲存。DOCA 則提供可程式化軟體基礎，用於上下文重複使用、零信任安全與多租戶生命週期管理，並納入 NVIDIA Vera Rubin 與 DSX 架構。

📊 **宣稱效益：更高利用率與更低單位成本**

README 指出，上述卸載與加速設計可帶來：更高 GPU 利用率、可預測延遲、租戶隔離、更低每代幣成本（cost per token），以及提升的每瓦代幣數（tokens per watt），橫跨整體 AI 工廠。

🎯 **實務啟示**

對建置 Agentic AI 系統的團隊來說，當推理變成多步驟分散式流程，網路與儲存不再是配角。將基礎建設處理從主機 CPU 卸載到 DPU／儲存處理器，並用統一軟體平臺（如 DOCA）管理上下文與安全，是減少瓶頸、壓低營運成本的可行路線。

🔗 **來源**
- 標題：Scaling Agentic AI Factories Through Extreme Co-Design with NVIDIA BlueField
- 作者／機構：Michelle Horton @ NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/scaling-agentic-ai-factories-through-extreme-co-design-with-nvidia-bluefield/

#AgenticAI #AIFactory #NVIDIA #BlueField #DPU #DOCA #Infrastructure #GPU #KVcache #VeraRubin
