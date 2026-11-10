---
title: Introducing Claude Fable 5.2 and Claude Mythos 5.2
source: Anthropic News
url: https://www.anthropic.com/claude-fable-and-mythos-5-2
model: claude-code/sonnet
generated_at: '2026-11-10T00:48:02.374595'
pinned: true
---

📌 Anthropic 發布 Claude Fable 5.2 與 Mythos 5.2，速度更快、價格更低

TL;DR：新一代旗艦模型在程式碼、推理、視覺多項基準全面超越 Opus 5.5，速度提升 30%、單價卻下降。

當一家公司說自家模型在 prerelease 測試中「完成了原本不可行的軟體遷移」「設計出三款可運作的電子裝置」「解開兩個黑洞物理學的開放問題」「用 30 小時形式化證明費馬最後定理」，這份清單本身就值得工程師停下來看一看——這正是 Anthropic 這次發布 Claude Fable 5.2 與 Claude Mythos 5.2 時列出的 prerelease 測試成果。

🤔 **同一顆模型，兩個名字：Fable 面向所有人，Mythos 需要申請**

Fable 與 Mythos 其實是同一個底層模型。差別在於 Fable 內建更嚴格的網路安全與生物安全防護措施，因此可以開放給所有使用者；而 Mythos 則透過 Anthropic 近期擴大的 Life Sciences 與 Cyber Verification Programs，提供給從事網路安全或生醫研究等「有益用途」的組織申請使用。測試者回饋，Fable 5.2 與 Mythos 5.2 的溝通表達比過去版本更清楚，輸出速度比 Fable 5.1／Mythos 5.1 快最多 30%。價格也調降至每百萬 input tokens 8 美元、每百萬 output tokens 40 美元；另外提供可選的 fast mode，生成速度最多再快 2.5 倍，價格為每百萬 input tokens 16 美元、每百萬 output tokens 80 美元。

📊 **幾乎每項基準都領先 Opus 5.5**

Anthropic 公布的基準測試顯示，Fable 5.2 在幾乎所有評測類別都優於自家旗艦日常模型 Opus 5.5：

| 基準測試（類別） | Fable 5.2 | Fable 5.1 | Opus 5.5 |
|---|---|---|---|
| FrontierCode 2.0（Agentic coding, Xhigh） | 49.1% | 32.4% | 45.5% |
| FrontierSWE v2（Agentic coding） | 69.9% | 56.3% | 62.3% |
| AutomationBench（商業流程自動化） | 51.4% | 31.4% | 42.5% |
| BenchCAD 2.1（硬體工程，Max effort） | 83.5 | 44.4 | 65.3 |
| OSWorld 2.1（電腦操作） | 89.3% | 83.5% | 87.2% |
| RoboDojo Sim（機器人） | 64.9% | 27.6% | 39.4% |
| Humanity's Last Exam（含工具） | 74.2% | 65.6% | 67.7% |
| Chartography（視覺圖表辨識） | 73.4% | 44.8% | 64.4% |

其中 FrontierCode 2.0（評估模型的程式碼修改是否會被開源專案維護者合併）特別值得留意：Fable 5.2 在 High effort 下得到 45.3%，幾乎追平 Opus 5.5 在該測試的最佳分數 45.5%，但成本只要後者的一半；在 Xhigh effort 下更拿下 49.1%，是 Anthropic 測試過所有已發布模型中的最高分。

💡 **同樣的分數，更低的成本**

Anthropic 特別強調效率曲線：在預設的 Medium effort 下，Fable 5.2 完成高難度任務所需的 token 數比 Fable 5.1 更少。在 WANDR（Perplexity 設計的大型資料收集 agent 基準）上，Fable 5.2 在 Medium effort 就能追平 Opus 5.5 的最高分，成本只要約 40%；在 Humanity's Last Exam 上，Fable 5.2 在 Low effort 甚至只用不到十分之一的成本就追平 Opus 5.5 的最高分。換句話說，這次升級帶來的不只是分數提升，更是「同樣品質、更低花費」的曲線整體右移。

⚠️ **安全測試：防蒸餾攻擊更強，誤擋更少**

Anthropic 表示針對這次底層模型進行了大量 prerelease 安全測試，開發了能更深入檢視特定風險行為（例如 sandbox escape）的新評測方式。公司判斷模型對齊失準帶來的高風險情境仍然偏低,且在多數對齊指標上表現與近期模型相當或更好。Fable 5.2 的網路安全與生物安全防護力道與 Fable 5.1 相當，但誤擋（不必要的拒絕）更少，同時部署了迄今最強的抗蒸餾攻擊防護。完整細節收錄在 Fable 5.2 與 Mythos 5.2 的 System Card 中。

🎯 **實務啟示：什麼時候該換模型**

Anthropic 的建議是：多數程式開發與知識型任務，先從 Opus 5.5 這個「日常主力」開始，再依任務的複雜度與範疇決定往上切到 Fable／Mythos，或往下切到 Sonnet 5.5／Haiku 5.5。Fable 5.2 也可以被用在兩種特殊角色：作為 Advisor，讓 Haiku、Sonnet 或 Opus 在遇到難題時諮詢它；或作為 Orchestrator，把較簡單的子任務下放給更小的模型執行。對正在設計多模型 agent 架構的團隊而言，這個分層建議本身就是一份可直接參考的路由策略。

🔗 **來源**
- 標題：Introducing Claude Fable 5.2 and Claude Mythos 5.2
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/claude-fable-and-mythos-5-2

#Anthropic #Claude #LLM #AIBenchmark #AgenticCoding #AIAlignment #MachineLearning #AIModel #SoftwareEngineering #AIAgents
