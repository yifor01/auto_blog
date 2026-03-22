---
title: "Synthetic Data Powers Product Retrieval for Long-tail Knowledge-Intensive Queries in E-commerce Search"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2602.23620
score: 126
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-03T00:59:13.534806
---

# 📌 【淘寶與中科大最新研究】合成數據讓電商搜索搞定「知識密集型長尾查詢」

當你在淘寶搜尋「適合油性皮膚的夏季保濕產品」或「辦公室午睡神器推薦」時，背後的產品檢索系統正面臨一大挑戰：如何準確理解這些「知識密集型長尾查詢」？

## 🤔 **AI 搜索的盲點：為什麼某些查詢總是搜不到好東西？**

電商搜索的核心任務是從數十億商品中找出相關候選集。雖然主流查詢（如「iPhone 15」）已經被優化得很好，但知識密集型長尾查詢仍然是「阿基里斯之踵」：

- 語言模式多樣，難以預測
- 缺乏明確購買意圖
- 需要特定領域知識才能正確理解
- 行為數據稀少，難以優化

這些查詢往往搜不到理想結果，用戶體驗大打折扣。

## 🧪 **52 位工程師的隨機對照實驗**

這是一項隨機對照實驗 (RCT)，招募了 52 位軟體工程師（大多為初級）。參與者需學習一個新的 Python 函式庫 (Trio)，一組可以使用 AI 助手，另一組必須手動編程。完成任務後，立即進行知識測驗。

## 🧪 **合成數據解決方案：讓 AI 學會「理解問題」**

阿里團隊提出一個巧妙的解決方案：透過合成數據來訓練檢索系統，讓系統具備理解知識密集型查詢的能力。

具體做法是：
1. 利用 LLM 的強大語言理解能力，訓練一個多候選查詢重寫模型
2. 透過多種獎勵信號，捕獲重寫模型的能力
3. 利用強大的離線檢索管道，將能力凝聚到精心挑選的查詢-產品對中
4. 將這些合成數據直接用於檢索模型訓練

## 🎯 **關鍵創新：避免分布偏移的合成數據**

傳統方法可能會導致「分布偏移」問題——重寫後的查詢與真實查詢差異太大，影響檢索效果。這個方案透過精心設計的合成數據，既保持了知識密集型查詢的特徵，又避免了引入不相關產品。

## 📊 **實驗結果：不用任何額外技巧，直接提升**

- 線下評測顯示檢索召回率顯著提升
- 線上真人對照實驗 (SBS) 證實用戶搜索體驗明顯改善
- 最重要的是：只需將合成數據加入訓練，無需任何額外技巧

## ⚠️ **研究限制與思考**

目前研究主要針對淘寶生態系統，不同電商平台的知識領域可能差異很大。此外，合成數據的質量仍高度依賴於離線檢索管道的強大程度。

## 🎯 **實務啟示：合成數據時代的檢索優化**

- 合成數據不只是用來擴充數據集，更可以用來傳遞特定能力
- 對於長尾場景，有策略地生成合成數據可能比收集更多真實數據更有效
- 檢索系統的優化需要兼顧效率（線上）和能力（離線）

## 🔗 **論文連結**

📝 Synthetic Data Powers Product Retrieval for Long-tail Knowledge-Intensive Queries in E-commerce Search
👤 Gui Ling, Weiyuan Li, Yue Jiang, Wenjun Peng, Xingxian Liu
🏢 Taobao & Tmall Group of Alibaba; University of Science and Technology of China; Beijing University of Posts and Telecommunications
🔗 論文：arxiv.org/abs/2602.23620

你在使用電商搜索時，是否也遇到過搜不到想要的情況？歡迎分享你的經驗 👇

#AI #搜尋引擎 #電商 #機器學習 #淘寶 #知識圖譜 #合成數據 #長尾查詢
