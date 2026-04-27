---
title: "Show HN: OSS Agent I built topped the TerminalBench on Gemini-3-flash-preview"
source: Hacker News
url: https://github.com/dirac-run/dirac
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-04-27T20:18:58.385536
---

📌 **開源Agent TerminalBench超Google與閉源頂流**

Google官方Agent跑TerminalBench僅得47.8%？
開源方案衝到65.2%，還贏了頂級閉源產品。
更關鍵的是：全程零作弊，代碼完全公開。

🤔 **TerminalBench 2.0作弊亂象頻傳，真實評測亟需透明化**
TerminalBench是針對終端操作Agent能力的權威基準測試，近期調試ML團隊揭露大量針對TerminalBench 2.0的刻意作弊案例（https://debugml.github.io/cheating-agents/），現有公開成績可信度備受質疑。
現有已公開的頂尖成績中，Google官方方案得分47.8%，閉源產品Junie CLI以64.3%位居前列。開發者GodelNumbering基於Gemini-3-flash-preview構建開源Agent Dirac，實測得分65.2%，原本等待官方排行榜收錄，但因維護團隊積壓大量PR，等待8天未獲回應，故公開成果。

🧪 **全程合規運行、開源可複現，零作弊機制**
為回應作弊爭議，作者明確澄清三項關鍵運行細節：
1. 未插入任何agents/skills.md等可能用於作弊的配置文件，全程無任何作弊機制
2. Agent完全按照TerminalBench排行榜的合規要求運行，未修改任何資源限制或超時設置
3. 測試使用的是完全開源版本的Agent，GitHub倉庫（https://github.com/dirac-run/dirac）代碼與運行版本完全一致，可完全復現

💡 **開源Agent 65.2% 登頂，超Google與閉源頂流**
本次測試的關鍵成績對比：
- 開源Agent Dirac（基於Gemini-3-flash-preview）：65.2%
- 頂級閉源產品Junie CLI：64.3%
- Google官方方案：47.8%
開源方案領先閉源頂流0.9個百分點，較Google官方方案高出17.4個百分點，是目前公開可查證的最高成績。

💡 **Harness設計對Agent評測結果影響極大**
作者基於本次實驗與其他同類測試發現，Harness（註：此處指Agent運行的測試框架與調度環境）對最終評測結果的影響遠超預期，這也解釋了同模型底座下不同Agent方案的顯著成績差異。
現階段多數Agent評測僅關注模型能力，往往忽略Harness設計的影響，容易導致評測結果失真。

⚠️ **成績尚未登上官方排行榜，維護積壓待確認**
本次測試成績尚未被TerminalBench官方排行榜收錄，作者已提交HF PR（https://huggingface.co/datasets/harborframework/terminal-ben...），但因維護團隊積壓大量待處理PR，已等待8天未獲回應，成績真實性可透過開源代碼自行復現驗證。

🎯 **Agent評測需重視Harness，開源可複現是信任基礎**
對GenAI工程師與研究者而言，本次案例有三點實務參考價值：
1. 評估Agent真實能力時，除模型本身外，測試Harness、運行環境的設計對結果影響極大，需納入評測的核心考量維度
2. 面對Benchmark作弊爭議，開源代碼、合規運行證明、零作弊聲明是建立結果可信度的核心依據
3. 開源Agent Dirac已完全公開，開發者可自行拉取代碼復現測試結果，驗證實際表現

🔗 **相關連結**
📝 原始來源：Hacker News Show HN
👤 作者：GodelNumbering
💻 開源代碼：https://github.com/dirac-run/dirac
📊 TerminalBench作弊報告：https://debugml.github.io/cheating-agents/
📋 HF PR連結：https://huggingface.co/datasets/harborframework/terminal-ben...

你如何看待TerminalBench的作弊爭議？歡迎分享你的觀察 👇

#AI #Agent #TerminalBench #開源 #Gemini #GenAI #基準測試 #軟體工程
