---
title: "Beyond the Grid: Layout-Informed Multi-Vector Retrieval with Parsed Visual Document Representations"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2603.01666
score: 125
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-03T19:50:25.455088
---

📌 【文檔檢索突破】95% 儲存成本砍半，性能還提升！多向量檢索新解法

你用過的 PDF 搜尋工具，真的看懂你的文件嗎？多數系統只讀懂文字，忽略了圖表、表格、欄位間的複雜關係。這是視覺化文件檢索的核心挑戰：如何讓 AI 同時理解「內容」與「排版」？

🤔 **多向量檢索的兩難困境**

當前最強的檢索系統會把文件切成多個向量（embedding），每個段落、圖表、表格都獨立編碼，大幅提升準確度。但問題來了：多向量意味著多倍儲存成本，且現有的優化手段（如向量合併、剪枝、抽象化）不是犧牲準確度，就是忽略排版訊息。

🧪 **ColParse 的創新解法**

香港科大與阿里雲提出 ColParse，核心概念是「用解析器理解排版，只保留必要的向量」。具體來說：

1. 文件解析器先分析版面，找出重要的區域（如標題、表格、圖片區塊）
2. 每個區塊轉成一個「版面感知的向量」
3. 再加上一個全頁級的向量，形成 compact multi-vector 表示

這樣做的好處是：既保留了排版結構，又大幅減少向量數量。

 **95% 儲存成本減少，性能還提升**

ColParse 在多個標準測試集上驗證：
- 儲存需求減少 95% 以上
- 檢索準確度顯著提升
- 支援多種基礎模型

這意味著：同樣的硬體資源，可以處理更多文件；同樣的文件量，檢索速度更快、準確度更高。

🎯 **為何這很重要？**

對於需要處理大量視覺化文件的企業（如法律、金融、學術出版），ColParse 解決了兩個關鍵問題：
- 成本：大幅降低儲存與運算開銷
- 效果：真正理解文件結構，不只是文字堆疊

⚠️ **研究限制與未來方向**

目前 ColParse 仍依賴文件解析器的準確度，複雜排版仍可能帶來挑戰。未來可探索動態調整向量數量、跨語言支援等方向。

🔗 **論文連結**
📝 Beyond the Grid: Layout-Informed Multi-Vector Retrieval with Parsed Visual Document Representations
👤 Yibo Yan, Mingdong Ou, Yi Cao, Xin Zou, Shuliang Liu
📍 HKUST & Alibaba Cloud Computing
🔗 arxiv.org/abs/2603.01666

#AI #文檔檢索 #多模態 #機器學習 #資訊檢索 #文檔解析 #效率優化
