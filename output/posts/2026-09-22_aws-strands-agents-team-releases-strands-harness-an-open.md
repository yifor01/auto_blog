---
title: 'AWS Strands Agents Team Releases Strands Harness: An Open-Source Agent Harness
  With 28% Lower Token Cost at Comparable Accuracy'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/21/aws-strands-agents-team-releases-strands-harness/
model: claude-code/sonnet
generated_at: '2026-09-22T20:21:16.793551'
score: 106
---

📌 AWS開源Strands Harness:同精度下token成本省28%

TL;DR：AWS開源通用Agent Harness「Strands harness」,實測顯示相近準確率下成本比同行低28%。

很多人在Claude Code或Codex裡驗證出一個Agent構想能跑,結果換成自己動手寫的迴圈重建後,效果卻大打折扣。AWS的Strands Agents團隊,這次盯上的正是這個落差。

🤔 **從原型到生產環境的斷層**

Strands harness是一個組裝完成、可直接使用的通用型Agent Harness,可在本地執行,也能部署到雲端服務供應商,提供Python與TypeScript版本,採Apache 2.0授權,一行程式碼即可啟動。根據MarkTechPost報導,團隊隨附的skills檔案能協助你的編碼Agent自動產生AWS、GCP、Azure、Cloudflare與Modal的部署設定。

所謂Harness,指的是圍繞模型運作的整套系統:迴圈邏輯、工具呼叫、上下文管理、記憶與錯誤恢復機制。Strands先前已透過Strands Harness SDK開放這些底層元件,這次的Strands harness則是把它們打包成一組可直接使用的預設組合。它被定位為通用型Agent,而非程式碼編輯專用的coding agent;呼叫create_harness()即可取得一個預先配置好的Agent實例。

📊 **6項基準測試,同精度成本低28%**

Strands Agents團隊使用Terminal-Bench創作者開發的評估框架Harbor,在Amazon EC2上進行分散式基準測試,分數為ALFWorld、ContextBench、GAIA、WebShop、τ²-bench與Terminal-Bench 2.1六項基準的平均值,成本則以每項任務的平均花費計算,對比對象包括Claude Code、Codex、oh-my-pi、OpenCode與DeepSeek Harness。

值得留意的是,DeepSeek Harness整體token效率其實是最高的,比Strands harness再便宜約14%,但每一項基準的分數都較低;圖表註腳說明,正是把DeepSeek Harness納入比較,才把整體節省幅度拉到28%這個數字。圖表中分數最高的點,是在Strands harness上執行Claude Opus 5,接近85%。最清楚的頭對頭比較,則是用Claude Fable 5跑Terminal-Bench 2.1,每個harness各跑89次試驗:相較Claude Code,Strands harness成本低77%,分數還高出7.9分;oh-my-pi以高54%的成本才打平69.7分的準確率;DeepSeek Harness雖然更便宜,分數卻落後10.2分。團隊也提到,另外還有兩個開源harness在成本與準確率上對Claude Code的表現也不錯。

💡 **上下文管理才是關鍵變數**

Strands harness預設就啟用了prompt caching與上下文管理,團隊表示上下文管理的預設規則,是同時驅動token效率與準確率提升的主要原因。這個結論也呼應了近期的HarnessTax研究:該研究比較了Claude Code、Codex CLI與Pi在7個模型上的表現,發現harness的選擇本身對成功率的影響很小,但同一個模型在不同harness下的成本卻可能相差達5倍。Strands研究團隊表示,針對這批基準測試的後續論文即將發布。

🎯 **實務啟示**

安裝方式很直接:`pip install strands-harness`或`npm install @strands-agents/harness`,並可用名稱直接指定模型,或指向本地的Ollama模型。搭配的Strands CLI(`npm install @strands-agents/strands-cli`)可以讓你用純文字描述原型化一個Agent,團隊的示範是要求Agent加入Playwright MCP伺服器並量測部落格文章的影片載入延遲,執行`/export`後就能輸出包含Playwright MCP設定的Python或TypeScript專案壓縮檔。由於Harness本身是一個函式庫依賴,筆電上原型化出來的Agent,理論上就是最終部署到生產環境的那一個,對於想避免「Demo能跑、重寫就掉分」問題的團隊,這個開發流程值得評估。

🔗 **來源**
- 標題：AWS Strands Agents Team Releases Strands Harness: An Open-Source Agent Harness With 28% Lower Token Cost at Comparable Accuracy
- 作者／機構：Asif Razzaq,MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/21/aws-strands-agents-team-releases-strands-harness/

#AWS #AgentHarness #OpenSource #LLMAgents #ContextManagement #ClaudeCode #TokenEfficiency #AIInfrastructure #AgentBenchmark #StrandsAgents
