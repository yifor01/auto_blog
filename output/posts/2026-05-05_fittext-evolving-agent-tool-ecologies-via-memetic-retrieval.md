---
title: "FitText: Evolving Agent Tool Ecologies via Memetic Retrieval"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.02411
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-05-05T20:00:49.816425
---

📌 【UCLA 最新研究】動態檢索解決Agent工具語義鴻溝

現有Agent工具檢索多依賴初始單輪查詢，當API規模擴展到4萬個端點時，靜態檢索的平均排名僅8.81。
但新方法將檢索嵌入Agent推理循環後，排名直接壓至2.78，工具調用通過率更提升24個百分點。

🤔 **4萬支API的語義鴻溝，靜態檢索無法跨越**

用戶對任務的描述與工具文檔之間存在顯著語義鴻溝，當API生態擴展至數萬個端點時，僅靠初始查詢的靜態檢索無法彌合這道鴻溝。核心矛盾在於，Agent執行任務過程中對自身需求的認知會持續進化，但對應的工具集卻不會同步更新，導致檢索效果隨API規模擴大急劇下降。

🧪 **無訓練框架，檢索嵌入推理循環與模因演化**

研究提出FitText，這是一個無需訓練（training-free）的框架，核心設計是將檢索動態嵌入Agent的推理循環中，而非僅依賴初始查詢。具體流程包含三個關鍵設計：
1. 生成自然語言偽工具描述作為檢索探針，透過檢索反饋迭代優化這些描述
2. 透過隨機生成探索多樣化的候選描述替代方案
3. 模因演化檢索機制
