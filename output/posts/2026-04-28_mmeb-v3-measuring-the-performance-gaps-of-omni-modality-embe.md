---
title: "MMEB-V3: Measuring the Performance Gaps of Omni-Modality Embedding Models"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2604.23321
score: 118
model: tencent/hy3-preview:free
generated_at: 2026-04-28T20:10:09.387990
---

📌 【Google AI Research 等機構聯合發表】全模態嵌入模型評測：指令失效與檢索偏差

現有的多模態嵌入模型號稱能理解文本、圖像、視頻和音頻，但當你明確指定「幫我找一段音頻」時，它真的能準確鎖定目標模態嗎？最新研究顯示，目前的頂尖模型在處理全模態檢索時，往往無法可靠地執行指令中的模態約束，甚至會出現嚴重的「模態混淆」。

🤔 **現有評測只覆蓋部分模態，全模態學習難以系統評估**

隨著 AI 從單模態走向能同時處理文本、圖像、視頻、音頻的 Omni-Modality（全模態），現有的評測基準卻嚴重滯後。大多數 Benchmark 仍局限於雙模態（如圖文檢索），這導致我們無法診斷模型在真正全模態語義空間中的表現，特別是在 Agent 場景下的應用能力。

🧪 **MMEB-V3 與 OmniSET：覆蓋四大模態的系統性診斷**

由寧波東方理工大學、上海交大、Google AI Research 等機構組成的團隊提出了 MMEB-V3 基準測試。不同於以往，它涵蓋了文本、圖像、視頻、音頻以及 Agent 場景。為了精確區分「語義相似」與「模態效應」，研究團隊還構建了 OmniSET（全模態語義等價元組），讓語義相同的實例以不同模態呈現，從而進行細粒度的錯誤分析。

 **模型常檢索錯模態、跨模態檢索不對稱、指令引導效果不彰**

實驗揭露了當前全模態嵌入模型的三大核心缺陷：

1.  **模態檢索失敗**：模型經常無法檢索到指令中指定的目標模態，容易混淆不同模態的表徵。
2.  **跨模態不對稱性**：跨模態檢索存在高度不對稱，且結果往往被「查詢模態（Query Modality）」的特徵所主導，而非真正的語義。
3.  **指令對齊失效**：透過指令（Instruction）引導的嵌入偏移，要麼強度不足，要麼與目標模態錯位，無法可靠地改善檢索精確度。

💡 **指令無法可靠約束模態，模型缺乏模態感知檢索能力**

這些結果指出一個關鍵問題：目前的模型架構和訓練方法，尚未真正學會「模態感知」。當用戶下達「找一段關於貓叫的音頻」這類指令時，模型可能只是因為文本語義相似就返回了圖片，而無法理解「音頻」這個模態約束的強制性。這對於需要精確模態控制的 Agent 應用來說是一大隱患。

⚠️ **基準測試的覆蓋範圍與真實場景仍有差距**

雖然 MMEB-V3 大幅擴展了評測維度，但全模態學習的複雜度極高，真實世界中的模態交互（如長視頻與複雜音頻的對應）可能比基準測試更為複雜。此外，OmniSET 的構建依賴特定方法，其泛化性仍需在更多模型架構上驗證。

🎯 **全模態評測框架為模型改進提供診斷工具**

對於從事多模態模型訓練與評估的團隊，這項研究提供了明確的改進方向：
- **強化模態約束**：在訓練目標中加入更強的模態對齊損失，確保模型能區分「語義相同」但「模態不同」的實例。
- **診斷優先**：在開發全模態模型時，應利用此類細粒度 Benchmark 診斷模型是否存在 Query 偏差。
- **指令微調**：重新審視 Instruction Tuning 在全模態場景下的設計，確保指令能真正引導嵌入空間的偏移。

🔗 **論文連結**
📝 MMEB-V3: Measuring the Performance Gaps of Omni-Modality Embedding Models
👤 Haohang Huang, Xuan Lu, Mingyi Su, Xuan Zhang, Ziyan Jiang 等
🏛️ Eastern Institute of Technology, Ningbo; Shanghai Jiao Tong University; Google AI Research; University of Waterloo; NUS; UCSB; Netmind.ai
🔗 論文：https://arxiv.org/abs/2604.23321

你認為目前的多模態模型（如 Gemini 或 GPT-4o）在區分「圖片中的貓」和「貓的叫聲」時，表現如何？歡迎分享你的觀察 👇

#MultimodalAI #EmbeddingModels #GoogleAI #機器學習 #資訊檢索 #全模態 #MMEB #模型評測
