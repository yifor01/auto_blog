---
title: 'SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning'
source: arXiv
url: http://arxiv.org/abs/2606.13673v1
score: 98
model: google/gemma-4-31b-it:free
generated_at: '2026-06-13T19:34:30.621403'
---

📌 【新研究】SpatialClaw：讓 VLM 像工程師一樣，用「狀態化程式碼」解決 3D 空間推理

當我們要求 AI 判斷物體在 3D 空間中的位置、相對關係或移動路徑時，目前的 Vision-Language Models (VLMs) 往往表現不佳。雖然透過「工具增強 (Tool-augmented)」引入感知模組能改善問題，但真正的瓶頸其實不在於工具本身，而是在於 AI 呼叫工具的「介面 (Interface)」。

🤔 **工具強大，但「溝通介面」限制了推理能力**

目前的空間推理 Agent 主要採取兩種設計：一種是「單次程式碼執行 (Single-pass code execution)」，AI 必須在沒看到中間結果前就決定所有分析步驟；另一種則是「結構化工具呼叫 (Structured tool-call)」，雖然穩定但缺乏靈活性，難以針對複雜任務自由組合操作。

這導致 AI 在面對開放式、複雜的 3D/4D 空間推理時，缺乏根據中間結果動態調整策略的空間。

🧪 **以 Stateful Python Kernel 作為行動介面**

為了突破這個限制，研究團隊提出了 **SpatialClaw**。這是一個無需額外訓練 (Training-free) 的框架，其核心設計將行動介面重新定義為一個「具備狀態的 Python Kernel」。

具體運作方式如下：
1. **預載環境**：Kernel 中預先載入輸入影像幀以及一套感知 (Perception) 與幾何 (Geometry) 原語 (Primitives)。
2. **迭代執行**：VLM Agent 每一步寫一個可執行的程式碼單元 (Cell)，且每一步的決定都基於之前所有單元的輸出。
3. **動態調整**：Agent 可以靈活地組合感知結果，並根據中間產出的文字描述或視覺觀察，即時調整後續的分析邏輯。

💡 **靈活組合感知結果，準確率提升 11.2%**

研究團隊在 20 個涵蓋靜態與動態 3D/4D 空間推理的基準測試中對 SpatialClaw 進行了評估，結果顯示：

- **性能提升**：平均準確率達到 59.9%，比之前的空間 Agent 提升了 11.2 個百分點。
- **強大的通用性**：在來自兩個不同模型家族的 6 種 VLM Backbone 上均取得一致的提升。
- **零適配成本**：不需要針對特定基準測試或特定模型進行任何微調或適配。

這證明了「將程式碼單元作為迭代介面」能讓 VLM 更有效地操縱幾何工具，將感知結果轉化為正確的空間推理。

⚠️ **框架屬 Training-free，效能依賴 VLM 的程式碼生成能力**

由於 SpatialClaw 是一個 Training-free 框架，其表現高度依賴於底層 VLM 撰寫 Python 程式碼的品質與邏輯能力。雖然在多個模型上表現優異，但對於程式碼能力較弱的小型模型，其潛能可能無法完全釋放。

🎯 **從 Tool-call 轉向 Code-as-Interface 的實務啟示**

對於開發 Agentic VLM 的工程師來說，這項研究提供了一個重要的思考方向：與其設計複雜的 API 定義，不如提供一個具備狀態的執行環境。

- **狀態保存 (Stateful)**：讓 Agent 能在步驟之間傳遞變數與中間結果，而非每次都從零開始。
- **迭代反饋 (Iterative Feedback)**：允許 AI 「先執行、看結果、再修正」，這比一次性生成完整計畫更符合複雜推理的邏輯。
- **組合能力 (Composition)**：透過程式碼的靈活性，讓模型能自由組合基礎原語，而非被侷限在預設的工具路徑中。

🔗 **論文連結**
📝 SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning
👤 Seokju Cho, Ryo Hachiuma, Abhishek Badki, Hang Su, Byung-Kwan Lee
🔗 論文：http://arxiv.org/abs/2606.13673v1

你認為在 Agent 設計中，「結構化 Tool-call」與「程式碼介面」哪一種更適合處理複雜推理？歡迎在評論區討論 👇

#AI #VLM #SpatialReasoning #AgenticAI #ComputerVision #Python #3DReasoning #arXiv
