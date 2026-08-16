---
title: 'Fine-Tuning Tool-Calling LLMs: A Complete Guide Using XYZ-Aquila-SFT and Qwen3'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/15/fine-tuning-tool-calling-llms-a-complete-guide-using-xyz-aquila-sft-and-qwen3/
model: nvidia/nemotron-3-ultra-550b-a55b:free
generated_at: '2026-08-16T06:08:17.975877'
score: 99
---

📌 手把手實作 Tool-Calling LLM 微調：用 XYZ-Aquila-SFT 與 Qwen3 打造完整 SFT 流程

TL;DR：MarkTechPost 釋出端到端教學，從資料流式處理、ChatML 渲染、LoRA 微調 Qwen3-0.6B 到教師強制評估，一次打通 Tool-Calling SFT 全鏈路。

隨著 LLM 從「聊天」走向「執行工具」，如何把多輪工具呼叫軌跡轉成可訓練的監督微調資料，成為工程師必修課。這篇教學不只講概念，直接把資料解析、格式轉換、遮罩損失、LoRA 訓練、基線比較全串起來，且在 Colab 等消費級 GPU 就能跑通。

🧩 **從原始資料到結構化軌跡**

教學以 XYZ-Aquila-SFT 資料集為例，示範如何以流式方式讀取、檢查 Schema，並逐筆拆解多輪對話中的 JSON 工具呼叫、推理區塊、觀察結果與內嵌工具定義。關鍵步驟包含：
- 定義巢狀安全的解析工具，提取 tool calls、reasoning、observation、embedded schemas
- 將每筆原始列轉為結構化軌跡物件，並驗證解析出的工具呼叫數量與資料集宣稱值一致
- 統計全語料層級指標：工具呼叫分佈、訊息深度、軌跡大小、工具使用頻率，並輸出視覺化分佈圖

🧩 **ChatML 格式化與僅監督 Assistant Token**

為了讓 Qwen 系列模型正確學習工具呼叫格式，教學手動將每條軌跡渲染為 ChatML，並保留所有推理內容，僅對 Assistant 產生的 Token 計算損失。具體做法：
- 提取內嵌工具定義並重構為結構化格式，驗證轉換後能還原原始系統訊息
- 依序處理每個訊息角色，套用 Qwen 相容的 ChatML 模板
- 建立自訂 PyTorch Dataset 與 Collator，完成 Tokenization、序列長度截斷策略、Train/Eval 切分與 Padding DataLoader 準備

🧩 **教師強制評估探針與基線測量**

在訓練前後都能公平比較，教學設計了教師強制評估機制：
- 在包含工具呼叫的 Assistant 輪次前截斷軌跡，構建評估探針
- 載入 Qwen3-0.6B 基礎模型，先測量基線工具呼叫效能
- 掛載 LoRA Adapter，啟用梯度累積、混合精度、Gradient Checkpointing、梯度裁剪與 Cosine LR Scheduler 進行微調

📊 **訓練後評估與成果匯出**

微調完成後，同樣用教師強制探針評估適配後模型，並與基線比較指標。最終輸出成果包含：
- 訓練好的 LoRA Adapter 權重與 Tokenizer
- 每條解析後軌跡的結構化 JSONL（含 messages、tool schemas、questions、answers）
- 語料統計報告 JSON（語料規模、工具頻率、軌跡統計、監督 Token 比例、評估結果）

🎯 **實務啟示**

這條流程示範了「資料理解 → 格式對齊 → 高效微調 → 可復現評估」的標準化範本。對想自行訓練 Agentic LLM 的團隊，可直接參考：
- 如何保留 Reasoning 內容並只監督 Assistant 輸出
- 如何用 LoRA 在小顯存環境驗證 Tool-Calling 能力提升
- 如何產出可複用的資料集制品與評估基準，支援後續擴展至更大模型或不同序列長度策略

🔗 **來源**
- 標題：Fine-Tuning Tool-Calling LLMs: A Complete Guide Using XYZ-Aquila-SFT and Qwen3
- 作者／機構：Sana Hassan @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/15/fine-tuning-tool-calling-llms-a-complete-guide-using-xyz-aquila-sft-and-qwen3/

#LLM #FineTuning #ToolCalling #Qwen3 #LoRA #SFT #HuggingFace #PyTorch #AgenticAI #MarkTechPost
