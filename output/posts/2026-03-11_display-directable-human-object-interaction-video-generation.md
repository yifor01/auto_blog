---
title: "DISPLAY: Directable Human-Object Interaction Video Generation via Sparse Motion Guidance and Multi-Task Auxiliary"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.09883
score: 103
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-11T18:39:49.250585
---

📌 【百度最新研究】HOI 影片生成突破：只用手腕座標和物體框，就能控制人與物互動

HOI（Human-Object Interaction，人與物互動）影片生成一直是 AI 影像領域的難題。現有方法要麼依賴密集控制訊號，要麼需要模板影片，要麼得精心設計文字提示，靈活性差，也很難處理新穎物體。百度研究團隊最新提出 DISPLAY 框架，用「手腕座標 + 物體框」這種極度稀疏的訊號，就能生成高保真、可控制的 HOI 影片。

🤔 **稀疏控制的挑戰：人與物失衡，物理一致性難保**

HOI 生成面臨的核心問題是：人體和物體的表徵不對稱，導致生成的互動缺乏物理一致性。傳統方法要麼給出密集的關節座標，要麼提供完整的物體模型，這不僅限制了泛化能力，也讓控制變得複雜。

🧪 **DISPLAY 架構：稀疏動作引導 + 物體壓力注意力機制**

DISPLAY 的關鍵創新在於：

- **稀疏動作引導**：只用手腕關節座標和物體的無向邊界框作為控制訊號
- **物體壓力注意力機制**：在稀疏條件下提升物體的穩定性
- **多任務輔助訓練策略**：透過專門的資料整理流程，讓模型同時受益於可靠的 HOI 樣本和輔助任務

🎯 **技術突破：輕量化控制方案的工程價值**

這種輕量化的控制方案解決了 HOI 生成中的兩大問題：

1. 降低了控制訊號的複雜度，讓用戶能直觀地控制互動
2. 改善了人體和物體表徵的失衡，提升了物理一致性

 **全面實驗驗證：多樣任務的高保真生成**

實驗結果顯示，DISPLAY 在多種 HOI 生成任務上都取得了高保真、可控制的效果。這證明了稀疏控制方案的可行性，也展示了物體壓力注意力機制和多任務輔助訓練策略的有效性。

⚠️ **資料限制與未來方向**

研究團隊也指出，HOI 資料的高品質樣本仍然稀缺，這也是他們開發多任務輔助訓練策略的重要動機。未來可以探索更複雜的互動場景，以及進一步提升泛化能力。

🎯 **實務啟示：HOI 生成技術的應用前景**

DISPLAY 的技術突破為 HOI 生成應用打開了新的可能性，特別是在需要直觀控制和處理新穎物體的場景中。這項技術可能應用於虛擬試穿、教育訓練模擬、電影特效製作等領域。

🔗 **論文連結**
📝 DISPLAY: Directable Human-Object Interaction Video Generation via Sparse Motion Guidance and Multi-Task Auxiliary
👤 Jiazhi Guan, Quanwei Yang, Luying Huang, Junhao Liang, Borong Liang @ Baidu Inc.
🔗 論文：arxiv.org/abs/2603.09883
🔗 專案頁面：mumuwei.github.io/DISPLAY/

#AI #ComputerVision #HOI #VideoGeneration #Baidu #機器學習 #深度學習

你對這種只用手腕座標就能控制 HOI 影片生成的方式有什麼想法？歡迎分享你的觀點 👇
