---
title: Kimi K3、Unlimited OCR包攬全球前二，中國開源模型持續刷屏海外
source: 量子位
url: https://www.qbitai.com/2026/07/461949.html
model: tencent/hy3:free
generated_at: '2026-07-29T14:12:13.339996'
score: 92
---

📌 【中國開源雙子星】Kimi K3 與 Unlimited OCR 包攬 Hugging Face 全球趨勢榜前二

TL;DR：Kimi K3 與 Unlimited OCR 登頂 Hugging Face，展示中國開源模型從「熱度」轉向「持續採用」的影響力。

中國 AI 開源模型正持續引發全球開發者的關注，近期月之暗面（Moonshot AI）與百度推出的兩款開源模型，不僅在短時間內衝上 Hugging Face 趨勢榜首，更在海外社群展現了極高的開發者黏著度。

🧩 **Kimi K3 與 Unlimited OCR 雙雙登頂**

在 7 月底的開源浪潮中，兩款模型展現了現象級的爆發力：

* **Kimi K3**：月之暗面正式開源完整模型權重，釋出後幾十分鐘內便迅速登頂 Hugging Face 總趨勢榜，刷新了該平臺的增長紀錄。
* **Unlimited OCR**：百度開源模型，不僅首發即登頂 GitHub Daily Trending 與 Python 榜，更在 5 天內 GitHub Star 突破 1 萬，實現 GitHub 與 Hugging Face 四榜第一。

📊 **從「釋出即關注」邁向「持續被採用」**

與一般開源專案在熱度回落後便逐漸沉寂不同，Unlimited OCR 展現了極強的生命力。在釋出一個月後，因獲得 AI 科學家楊立昆（Yann LeCun）轉發，其熱度再度攀升，重新回歸 Hugging Face 全球模型總趨勢榜第一。

截至目前，Unlimited OCR 的數據表現如下：
* **GitHub Star**：突破 1.97 萬
* **HuggingFace 下載量**：達 265 萬

💡 **解決長文件解析痛點：Reference Sliding Window Attention**

Unlimited OCR 之所以受到開發者青睞，關鍵在於它解決了長文件解析（如書籍、論文、報告）的工程難題。

🤔 **傳統方案的限制**
過去的 OCR 模型在處理長文件時，通常採用「逐頁解析 + 結果拼接」的工程方案。隨著輸出內容增加，解碼階段的 KV Cache 會持續膨脹，導致推理速度下降與視訊記憶體（VRAM）成本大幅增加。

🧩 **R-SWA 機制：模擬人類閱讀模式**
百度提出了 **Reference Sliding Window Attention (R-SWA)** 機制，其設計理念類似人類閱讀與抄錄：
1. **持續關注**：始終保持對原始文件內容的關注。
2. **工作記憶**：僅保留最近一段生成內容作為「工作記憶」，而非無限累積所有歷史資訊。

這種設計讓模型能在一次前向推理中，連續完成數十頁文件的解析，實現從第一頁到最後一頁的連貫輸出，並將解解碼階段的 KV Cache 控制在恆定規模，使計算成本與記憶體佔用不會隨輸出長度持續增長。

🎯 **實務啟示**

Unlimited OCR 的突破不僅提升了 OCR 的效率，更為大模型處理長程推理與記憶管理提供了新思路：不再單純依賴擴展上下文視窗（Context Window），而是透過更高效的注意力機制來實現長期任務處理。這對於需要處理大量非結構化長文件的 AI 應用場景，具有極高的實作價值。

🔗 **來源**
- 標題：Kimi K3、Unlimited OCR包攬全球前二，中國開源模型持續刷屏海外
- 連結：https://www.qbitai.com/2026/07/461949.html

#AI #OpenSource #HuggingFace #GitHub #KimiK3 #UnlimitedOCR #MachineLearning #OCR #DeepLearning #ArtificialIntelligence
