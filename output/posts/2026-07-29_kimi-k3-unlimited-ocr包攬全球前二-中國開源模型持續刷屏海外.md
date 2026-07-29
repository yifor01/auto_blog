---
title: Kimi K3、Unlimited OCR包攬全球前二，中國開源模型持續刷屏海外
source: 量子位
url: https://www.qbitai.com/2026/07/461949.html
model: tencent/hy3:free
generated_at: '2026-07-29T08:35:31.587479'
score: 81
---

📌 【中國開源雙子星】Kimi K3 與 Unlimited OCR 包攬 Hugging Face 全球趨勢榜前二

TL;DR：Kimi K3 與百度 Unlimited OCR 登頂 Hugging Face，展現中國模型從「釋出關注」轉向「持續採用」。

中國 AI 開源模型近期在海外社群展現強大影響力，月之暗面（Moonshot AI）與百度推出的兩款模型，不僅迅速登頂 Hugging Face 趨勢榜，更在技術層面解決了長文件解析的長期痛點。

🚀 **Kimi K3 迅速登頂 Hugging Face 趨勢榜**

7 月 27 日，月之暗面正式開源 Kimi K3 完整模型權重。該模型釋出後，在幾十分鐘內便迅速登頂 Hugging Face 趨勢榜，並刷新了該平臺的增長紀錄。

🧩 **Unlimited OCR 透過技術突破實現四榜第一**

與 Kimi K3 同步熱議的還有百度的 Unlimited OCR。該專案展現了極高的開發者黏著度：
- **GitHub 表現**：5 天內 Star 突破 1 萬，首發即登頂 GitHub Daily Trending 總榜與 Python 榜。
- **Hugging Face 表現**：包攬全球模型總趨勢榜與多模態模型趨勢榜。
- **長期熱度**：在釋出一個月後，獲得 AI 科學家楊立昆轉發，熱度再次攀升，重回 Hugging Face 全球模型總趨勢榜第一。截至目前，其 GitHub Star 已突破 1.97 萬，Hugging Face 下載量達 265 萬。

💡 **解決長文件解析的記憶體與速度瓶頸**

Unlimited OCR 受到開發者青睞的核心原因，在於它解決了長文件（如書籍、論文、報告）解析的工程痛點。

🤔 **傳統 OCR 的挑戰**
過去處理長文件時，通常需要採用「逐頁解析 + 結果拼接」的方案。隨著輸出內容不斷增長，解碼階段的 KV Cache 會持續膨脹，導致推理速度下降與視訊記憶體（VRAM）成本大幅增加。

🧩 **Reference Sliding Window Attention (R-SWA) 機制**
為了應對上述問題，百度提出了 R-SWA 機制，其設計理念類似人類閱讀長文件時的工作方式：
1. **持續關注**：始終保持對原始文件內容的關注。
2. **工作記憶**：僅保留最近一段生成內容作為「工作記憶」，而非無限累積所有歷史資訊。
3. **恆定成本**：透過此設計，模型能在一次前向推理中連續完成數十頁文件解析，並將解碼階段的 KV Cache 控制在恆定規模，使計算成本與記憶體佔用不會隨輸出長度持續增長。

🎯 **從「釋出關注」邁向「持續採用」**

Unlimited OCR 的表現顯示，中國 AI 開源正從單純的「釋出即關注」轉向「持續被採用」。這不僅是模型效能的領先，更代表其技術方案能實際解決開發者在長程推理與記憶管理上的實際需求，從而沉澱為全球開發者生態的影響力。

🔗 **來源**
- 標題：Kimi K3、Unlimited OCR包攬全球前二，中國開源模型持續刷屏海外
- 連結：https://www.qbitai.com/2026/07/461949.html

#AI #OpenSource #HuggingFace #KimiK3 #UnlimitedOCR #Baidu #MachineLearning #OCR #LLM #ComputerVision
