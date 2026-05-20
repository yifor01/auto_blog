---
title: "rerun-io/rerun"
source: GitHub Trending
url: https://github.com/rerun-io/rerun
score: 101
model: tencent/hy3-preview:free
generated_at: 2026-05-20T21:26:54.083867
---

📌 **rerun-io：統一多模態數據平台**

你有試過將機器人影像、點雲、時間序列、關節狀態一次同步看見嗎？傳統工具常常需要匯出、轉換、延遲。Rerun 宣稱只要兩分鐘，就能把多速率多模態資料直接丟進訓練。

🤔 **多速率多模態資料的統一入口**  
Rerun 設計為實體 AI 的資料層，能夠同時攝取圖像、點雲、變換、時間序列、關節狀態、影像等多種模態，來源涵蓋機器人日誌、人機操作 rig、模擬器與網路影片，支援 MCAP、rrd、LeRobot 等格式。所有資料保留原始速率與時序，避免在不同工具間切換時產生資料對齊問題。

🧪 **Rust 欄塊儲存與即時視覺器的結合**  
底層採用 Rust 開發的欄塊（column‑chunk）儲存，專為多速率實體資料設計，提供高效的壓縮與隨機存取。內建的視覺器可即時渲染所有同步資料，支援時間軸 scrub、側邊比較傳感器，以及觀看電腦視覺管線（SLAM、手部追蹤、動作重定目標）的即時運行。

🚀 **Python / Rust / C++ SDK 快速上手**  
透過 `pip install rerun-sdk`（或對應的 Rust/C++ 套件），開發者僅需兩行程式碼即可初始化與啟動視覺器：

```python
import rerun as rr
rr.init("rerun_example_app")
rr.spawn()
```

這樣就能在瀏覽器中看到第一筆多模態資料，整個流程官方標示為「under 2 minutes」。

🔗 **資料可直接查詢與串流至訓練**  
儲存的欄塊資料支援 DataFrame 或 SQL 查詢，使得原始、中間與衍生資料都能以表格方式取得。同一份資料亦可直接串流至機器學習訓練管線，免除額外的匯出作業與資料快照，降低資料過時的風險。

⚠️ **專注於特定場景，長期穩定性尚待驗證**  
目前的說明著重於機器人與具身 AI 的日誌、視覺化與訓練整合，未提供大規模生產環境的壓力測試或長期穩定性數據。功能與效能的完整評估仍需社群實踐與後續版本驗證。

🎯 **即時整合多模態資料，提升開發迭代速度**  
對於需要同時觀測影像、點雲與控制指令的機器人或視覺系統開發者，Rerun 提供一個不需額外轉換步驟的統一平台。透過即時視覺器與直接查詢功能，工程師可以快速驗證演算法、偵測資料異常，並將同一資料流直接喂訓練模型，縮短從實驗到產品的迴圈。

🔗 **原始碼與文件**  
📂 GitHub：https://github.com/rerun-io/rerun  
📖 快速開始：`pip install rerun-sdk` 並參考 README 中的範例程式碼。  

#Rerun #MultimodalData #Robotics #EmbodiedAI #Rust #SDK #DataVisualization #MachineLearning #OpenSource
