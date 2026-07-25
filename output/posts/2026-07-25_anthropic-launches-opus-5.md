---
title: Anthropic launches Opus 5
source: TechCrunch AI
url: https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/
model: tencent/hy3:free
generated_at: '2026-07-25T07:53:26.541773'
score: 58
---

這是一篇針對產業新聞型別的技術部落格文章。

📌 【Anthropic 重磅更新】Opus 5 正式發布：效能超越 Fable 5 且限制更少

TL;DR：Anthropic 推出 Opus 5，具備更強的自我驗證與迭代能力，且安全性限制較前代更輕量。

Anthropic 於週五推出了其重量級模型的新版本——Opus 5。這不僅是該系列模型的最新迭代，更在多項基準測試中展現出超越 Fable 5 的強大實力。

🧩 **效能更強且更具成本效益**

雖然 Opus 5 的規模比 Fable 5 小，但其具備以下優勢：
- **成本更低**：相較於 Fable 5，使用成本更低廉。
- **限制更少**：減少了開發者最在意的限制問題，使其在多數使用場景中更具優勢。
- **自我迭代能力**：Anthropic 強調 Opus 5 在「驗證工作」與「重複迭代以達成目標」的能力上有顯著進步。例如，在面對不完整的提示詞 (prompt) 時，Opus 5 能自行撰寫出完整的電腦視覺 (computer vision) 流程。

📊 **安全性與隱私權的平衡演進**

在安全性設計上，Opus 5 採取了更精準且輕量化的策略：
- **隱私保護**：不同於 Fable 與 Mythos 適用 30 天資料保留政策 (data retention policy)，Opus 5 不受此政策限制，這對重視隱私的使用者至關重要。
- **更低的誤判率**：預計 Opus 5 的安全分類器 (classifiers) 觸發頻率會比 Fable 5 低 85%，減少了對開發者的幹擾。
- **差異化安全規範**：針對網路安全任務仍保有防護措施。例如，Opus 5 禁止用於掃描二進位檔 (software binary) 的漏洞，但允許進行原始碼 (source code) 的漏洞搜尋，因為後者更符合防禦性用途。

💡 **新增 Automatic Fallbacks 解決模型拒絕問題**

為了降低安全機制對使用體驗的衝擊，Anthropic 推出了一項名為 Automatic Fallbacks 的測試版功能。當使用者的提示詞觸發安全分類器時，系統會自動將請求路由 (route) 到效能較低的模型，以確保流程不被中斷。

⚠️ **產品更新時程密集**

Opus 5 的發布時程極快，僅在 5 月 28 日推出 Opus 4.8 兩個月後便正式亮相。隨著 Mythos 5、Fable 5 與 Sonnet 5 於六月陸續推出，目前僅剩輕量級的 Haiku 模型尚未升級至第 5 系列。

🔗 **來源**
- 標題：Anthropic launches Opus 5
- 作者／機構：Russell Brandom @ TechCrunch AI
- 連結：https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/

#AI #Anthropic #Opus5 #LLM #MachineLearning #TechNews #ArtificialIntelligence #Fable5 #ComputerVision #AIModels
