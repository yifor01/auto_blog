---
title: "SecAgent: Efficient Mobile GUI Agent with Semantic Context"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.08533
score: 123
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-10T23:55:26.161599
---

# 📌 【SecAgent】Alibaba 推出 3B 參數中文移動 GUI 代理，大幅提升手機自動化效率

隨著手機應用越來越複雜，AI 代理能不能幫你自動完成手機上的各種操作，已經成為一個重要的研究方向。但現有的移動 GUI 代理面臨兩大瓶頸：中文資料太少、記憶歷史太慢。

🤔 **資料不足 vs. 效率瓶頸：移動 GUI 代理的兩大難題**

現有的移動 GUI 代理主要基於英文資料訓練，但中國的手機生態系統有其獨特性。此外，代理需要記住過去的螢幕畫面和操作，這會消耗大量計算資源，影響響應速度。

🧪 **18k 樣本、121k 步驟：SecAgent 的資料與設計**

SecAgent 是阿里巴巴淘寶天貓團隊開發的 3B 參數模型，解決了上述兩個問題：

1. **中文資料集**：18,000 個螢幕畫面對應物件的對齊樣本，121,000 個導航步驟，涵蓋 44 個熱門應用
2. **語義上下文機制**：將歷史畫面和操作濃縮成自然語言摘要，大幅提升效率

🎯 **核心創新：語義上下文機制**

傳統方法需要儲存所有歷史畫面，SecAgent 的創新在於：

- 將多張螢幕截圖和操作轉化為一句話描述
- 例如：「用戶在淘寶搜尋手機殼，點進了某款商品頁面」
- 大幅減少記憶體使用，同時保留關鍵資訊

 **超越同級對手，接近 7B-8B 大模型**

在團隊自建和公開的導航測試中，SecAgent 表現優於參數相近的模型，甚至接近 7B-8B 的大模型。

⚠️ **開源資料集的價值**

除了模型本身，團隊還開源：
- 18k 樣本的中文資料集
- 導航測試基準
- 模型原始碼

這對研究中文移動自動化領域的研究者來說，是非常寶貴的資源。

🎯 **實務啟示：多語言 AI 代理的未來**

- 資料集建設是 AI 模型成功的關鍵
- 效率優化可以讓小模型達到大模型效果
- 開源有助於領域快速進步

🔗 **論文連結**
📝 SecAgent: Efficient Mobile GUI Agent with Semantic Context
👤 Yiping Xie, Song Chen, Jingxuan Xing, Wei Jiang, Zekun Zhu @ Taobao & Tmall Group of Alibaba
🔗 論文：arxiv.org/abs/2603.08533

你覺得中文移動自動化還有哪些應用場景值得探索？歡迎分享你的想法 👇

#AI #MobileAutomation #GUI #Multimodal #Alibaba #中文AI #開源模型
