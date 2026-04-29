---
title: "Mistral Medium 3.5"
source: Hacker News
url: https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5
score: 114
model: tencent/hy3-preview:free
generated_at: 2026-04-29T20:07:40.189489
---

📌 【Mistral AI 新作】128B 旗艦模型進軍雲端 Agent，4 卡就能自托管

還在為了跑大型語言模型而堆疊昂貴的顯卡嗎？Mistral AI 最新發布的 Mistral Medium 3.5 試圖證明，128B 的參數量已經能在單一模型上同時搞定指令遵循、推理與長時間編碼，且只需 4 張 GPU 即可自托管。

🤔 **AI Agent 的戰場，正從本地端移向雲端**

過去我們習慣在筆電上跑 Copilot 或本地 Agent，但這限制了運算資源與並行處理的能力。Mistral 這次推出的 Vibe Remote Agents，直接將 Agent 搬上雲端，讓它們能獨立運作、平行處理多個任務，並在完成後主動通知開發者。這意味著開發者可以真正「離開對話」，讓 AI 在背景跑長時間的專案。

🧪 **128B Dense 模型與開放權重的組合**

Mistral Medium 3.5 定位為新的旗艦模型，採用 128B Dense 架構。不同於過往將推理與編碼分開處理的模型，這次將三種能力融合。最關鍵的是，它依然堅持 Open Weights 策略，採用修改過的 MIT License，對於講求數據主權與私有化部署的企業來說，這是一個極具吸引力的選項。

 **4 張 GPU 就能跑的旗艦級效能**

這次發布的最大亮點在於硬體門檻的降低。在雲端 Agent 的架構下，Mistral 強調這個 128B 模型可以在僅需 4 張 GPU 的環境下自托管運行。這解決了許多中小型團隊「想用大模型但跑不動」的痛點，同時在真實世界任務（Real-world performance）中展現了不俗的實力。

💡 **從聊天到工作流：Le Chat 的 Work Mode**

除了模型本身，Mistral 也更新了 Le Chat 的介面。新的 Work Mode (Preview) 將 Agent 能力擴展到更複雜的多步驟任務，如深度研究、資料分析與跨工具操作。結合 Vibe CLI，開發者可以將本地的開發環境「傳送」到雲端，實現無縫的開發體驗。

⚠️ **Preview 階段的觀察重點**

目前 Mistral Medium 3.5 與 Vibe Remote Agents 均處於 Public Preview 階段。此外，雖然號稱 Open Weights，但使用的是 Modified MIT License，具體在商業授權與使用限制上與標準 MIT 有何差異，將是開發者部署前需要釐清的細節。

🎯 **對工程師的實戰建議**

- **自托管優先**：如果你們團隊在意隱私與成本，這是目前少數能在 4 卡環境下運行的 128B 級距模型。
- **異步工作流**：善用 Vibe Remote Agents 處理那些不需要即時回饋的長時程編碼任務，釋放本地資源。
- **關注授權**：在導入產品前，務必確認 Modified MIT License 是否符合你們的閉源商業需求。

🔗 **相關連結**
📝 Mistral Medium 3.5 & Vibe Remote Agents
🏢 Mistral AI
🔗 官方新聞：https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5
💬 Hacker News 討論 (281 points)：https://news.ycombinator.com/item?id=44251831

你們覺得 128B 模型配合 4 卡自托管，會是企業導入 AI 的「甜蜜點」嗎？歡迎在留言區討論 👇

#MistralAI #LLM #OpenWeights #CloudComputing #AIagent #SoftwareEngineering #GenAI #TechNews
