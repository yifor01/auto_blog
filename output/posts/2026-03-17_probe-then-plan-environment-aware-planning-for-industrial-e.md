---
title: "Probe-then-Plan: Environment-Aware Planning for Industrial E-commerce Search"
source: ChatPaper/AI
url: https://arxiv.org/abs/2603.15262
score: 105
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-17T18:47:17.682525
---

📌 【JD.com 實戰】Probe-then-Plan：破解 LLM 搜索的「盲目-延遲」困境

當你用 AI 搜尋產品時，系統到底在想什麼？為什麼有時候給你精準結果，有時候卻讓你失望？JD.com 最新研究揭開了工業級 AI 搜索的真實挑戰。

🤔 **LLM 搜索的盲點：不知道庫存，也不知道能不能找到**

你可能不知道，現代 LLM 在搜索時面臨一個根本矛盾：如果只看問題就決定搜索策略，可能根本找不到對應商品（比如建議「藍色連衣裙」但庫存只有紅色）；但如果每次都去檢查庫存再決定，搜索速度會慢到無法接受。

這就是 JD.com 團隊發現的「盲目-延遲」困境：query rewriting 對真實環境一無所知，而深度搜索代理需要多次工具調用，延遲高達幾秒，但工業搜索要求必須在幾百毫秒內響應。

🧪 **Probe-then-Plan：先探再策的解決方案**

JD.com 團隊提出 Environment-Aware Search Planning (EASP)，核心創新是 **Probe-then-Plan 機制**：

1. **Probe（探測）**：先用輕量級檢查快速獲取當前搜索環境的快照（什麼商品在庫、相關性如何）
2. **Plan（策劃）**：基於探測結果，診斷搜索計劃的執行缺口，生成基於現實的搜索策略

這就像先查清楚店裡有什麼貨，再決定怎麼幫顧客找東西，而不是憑空想像。

⚙️ **三階段實現：從理論到部署**

**階段一：離線數據合成**
使用 Teacher Agent 合成多樣化的搜索計劃，這些計劃都經過對真實環境的檢查驗證。

**階段二：規劃器訓練與對準**
- 先用監督學習（SFT）讓規劃器掌握診斷能力
- 再用強化學習（RL）對準商業目標（轉化率）

**階段三：適應性在線服務**
複雜度感知路由機制：只對複雜查詢激活規劃，簡單查詢直接處理，確保資源最佳分配。

 **實驗結果：效果驚人**

- **離線評估**：相關性召回率顯著提升
- **線上 A/B 測試**：在 JD.com 實際部署
  - 有效訂單率 (UCVR) 大幅增長
  - 總營收 (GMV) 實現可觀提升

最重要的是，這套系統已經成功應用於 JD.com 的 AI-Search 系統，證明了其商業可行性。

🎯 **為什麼這很重要**

這不只是學術研究，而是直接解決了工業級 AI 搜索的核心矛盾：

- **實用性高**：直接提升商業指標
- **可擴展性強**：複雜度感知確保效率
- **商業價值大**：已在全站部署

Probe-then-Plan 展示了如何讓 AI 在真實環境中做出更聰明的決策，而不是在真空中空想。

🔗 **論文連結**
📝 Probe-then-Plan: Environment-Aware Planning for Industrial E-commerce Search
👤 Mengxiang Chen, Zhouwei Zhai, Jin Li @ JD.com
🔗 論文：arxiv.org/abs/2603.15262

你有沒有想過，你下次搜商品時，系統可能已經先「看了一眼庫存」再給你推薦？這就是 AI 搜索的進化方向。

#AI #搜尋引擎 #電子商務 #JD.com #LLM #強化學習 #工業級AI
