---
title: 'Gemini 4 Carbon: Our next frontier model'
source: Google DeepMind
url: https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/
model: claude-code/sonnet
generated_at: '2026-10-28T21:46:47.621882'
pinned: true
---

📌 【Google DeepMind 官方發布】Gemini 4 Carbon 登頂 Intelligence Index，資安防禦基準全面刷新

TL;DR：Gemini 4 Carbon 主攻長時任務與資安防禦，多項外部基準創新高，先限量開放給資安防禦人員。

當一個模型可以連續跑上好幾天，只為了揪出大型程式碼庫裡一個深藏的 bug，軟體工程與資安防禦的工作節奏正在被重新定義。

🤔 **接棒 Argon，兩週內再推新旗艦**

Google DeepMind 宣布 Gemini 4 Carbon，是繼兩週前推出的 Gemini 4 Argon 之後的下一代前沿模型，定位為「最強模型，具備頂尖資安能力與長時任務（long horizon）能力」。Carbon 在最新更新的 Artificial Analysis Intelligence Index v5.0 排名第一，得分 59。

🧩 **為持續性 agentic 工作流而生**

Carbon 的設計目標是處理更困難、更長時程的工程問題。素材指出，DeepMind 內部團隊觀察到 Carbon 能連續運作數天，在遇到死路後持續嘗試，完成跨大型程式碼庫與底層系統的複雜多步工程任務，例如追根究柢並修補難以定位的 bug。團隊也針對程式撰寫、agentic 任務、科學任務、全端網站開發與多模態理解等領域進行了調整，網站開發品質提升反映在 WebDev Arena 排名躍升 89 個 Elo 分，來到第 4 名（1768 分）。

📊 **資安防禦三個環節全面領先**

Carbon 在「尋找漏洞、驗證風險、修補根因」這條資安防禦鏈上，取得 DeepMind 所稱的頂尖表現（以下基準均在未加防護機制的狀態下評測）：

| 基準測試 | 評測目標 | Carbon 分數 |
|---|---|---|
| SEC-bench Pro | 自主找出真實軟體中的複雜漏洞 | 88.2% |
| ExploitGym | 驗證漏洞是否可被利用 | 54.8% |
| CWE-bench | 將驗證過的漏洞修補成可運作的程式碼 | 71.0% |

DeepMind 表示，在內部基準上，Carbon 生成安全程式碼的成功率比 Argon 提升超過兩倍；Chrome 團隊回報 Carbon 產生高品質修補程式的表現，比「另一家實驗室的大型前沿模型」高出逾 10 倍；雲端安全平臺 Wiz 也觀察到 Carbon 在網路滲透測試基準上領先，這項能力是 Wiz「Scan for Good」計畫的核心需求。

💡 **對齊與安全性也同步進化**

Carbon 延續 Argon 的多層安全防護架構（模型訓練、即時濫用防禦、prompt injection 防護、思維鏈監控），並在幾個面向上更進一步：在 Terminal-Bench 4.0 上，成功作弊率降到 0.0%，嘗試作弊的比例降到 0.4%，同時整體準確率仍提升；內部實際編程環境中，高嚴重度的「行為偏離」警示減少近 80%；內部測試顯示未經證實的宣稱減少約兩倍，模型遇到資訊不足時會把方法論上的限制直接寫進交付物，而不是編造或含糊帶過；過度行動（overreach）降低 26%，服務不足（under-service）降低 29%；在 Gray Swan 的間接 prompt injection 基準上，Carbon 把攻擊成功率從 Argon 的 0.7% 降到 0.0%，抵禦了所有評測中的攻擊嘗試。

⚠️ **先限量給資安防禦人員，審慎分階段開放**

DeepMind 採取審慎的部署節奏：本週起先開放給一部分資安防禦人員，再透過 Fairwind Program 逐步擴大到更多信任夥伴，同時積極參與美國政府針對發布前模型測試的自願性流程。目前尚未對一般開發者、企業與消費者開放，DeepMind 表示會持續收集回饋並調整防護措施後盡快推出。定價方面，Carbon 延續 Argon 的入門價格，每百萬輸入 token 2 美元、每百萬輸出 token 10 美元，快取輸入 token 則有 95% 折扣。

🎯 **實務啟示**

對安全工程師而言，值得留意的是這些基準分數都是在「未加防護機制」下測得，實際產品體驗可能因 guardrails 而有落差；而分階段開放、優先給防禦方而非直接公開發布的策略，某種程度上反映出廠商對高能力資安模型雙重用途風險的審慎態度。想取得早期存取權的團隊，目前能做的是關注 Fairwind Program 的開放節奏。

🔗 **來源**
- 標題：Gemini 4 Carbon: Our next frontier model
- 作者／機構：Google DeepMind（Koray Kavukcuoglu, SVP, Google DeepMind and Chief AI Architect, Google）
- 連結：https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/

#GoogleDeepMind #Gemini #AI #Cybersecurity #AgenticAI #AISafety #SoftwareEngineering #FrontierModel #LLM #AIResearch
