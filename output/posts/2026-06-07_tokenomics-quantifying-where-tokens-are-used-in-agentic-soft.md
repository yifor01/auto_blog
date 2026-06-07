---
title: 'Tokenomics: Quantifying Where Tokens Are Used in Agentic Software Engineering'
source: Hacker News
url: https://arxiv.org/abs/2601.14470
score: 99
model: google/gemma-4-31b-it:free
generated_at: '2026-06-07T19:32:36.570938'
---

📌 **【Tokenomics 研究】Agent 寫 Code 到底花多少錢？量化分析 LLM 多代理系統的 Token 消耗**

當我們談論 AI Agent 自動化軟體工程時，討論的焦點通常是「它能寫多少行 Code」或「通過多少測試」，但對於企業管理者與工程師最頭痛的問題——「這到底要花多少 Token？」卻鮮少有系統性的量化分析。

如果你打算將 LLM-MA (Multi-Agent) 系統導入生產環境，不能僅靠感覺估算預算，因為 Agent 的迭代循環可能會讓成本在不知不覺中呈指數級增長。

🤔 **自動化很美好，但成本不可預測是最大的痛點**

目前的 LLM 多代理系統（如 ChatDev）已經能處理從需求分析、程式碼生成到測試的複雜任務。然而，這類系統的運作效率與資源消耗一直處於「黑盒」狀態。由於成本不可預測且環境影響未知，許多企業在實際部署時會猶豫：究竟是模型太貴，還是工作流設計太冗贅？

🧪 **以 ChatDev 框架與 GPT-5 推理模型進行實測**

研究團隊為了量化這個問題，設計了一套標準化的評估框架。他們分析了 30 個軟體開發任務的執行軌跡 (Execution Traces)，並將開發流程拆解為六個關鍵階段：
- 設計 (Design)
- 編碼 (Coding)
- 程式碼補完 (Code Completion)
- 程式碼審查 (Code Review)
- 測試 (Testing)
- 文件撰寫 (Documentation)

透過這種映射方式，研究者能精準追蹤在每個階段中，輸入 (Input)、輸出 (Output) 以及推理 (Reasoning) Token 的具體分佈情況。

📊 **初步發現：迭代式的 Code Review 是 Token 消耗的大戶**

研究的初步結果指出，在整個軟體開發生命週期 (SDLC) 中，**「程式碼審查 (Code Review)」階段的 Token 消耗量最為顯著**。

這揭示了一個關鍵洞察：Agent 之間的反覆對話、審核與修正的迭代過程，其資源消耗遠高於單純的程式碼生成。這意味著，提升 Agent 的「一次性審查準確度」比單純提升生成速度，更能有效降低整體運作成本。

💡 **從「能執行」轉向「成本效益優化」**

這項研究將焦點從「功能實現」移向了「資源量化」。對於開發 Agentic Workflow 的工程師來說，這提供了重要的實務啟示：
1. **精準預算編列**：不再是概算，而是能根據開發階段（如 Design vs. Testing）來預估 Token 分佈。
2. **瓶頸分析**：既然 Code Review 是消耗大戶，優化該階段的 Prompt 或引入更輕量的小模型進行初步審核，可能是降低成本的突破口。
3. **推理成本考量**：隨著推理模型 (Reasoning Models) 的普及，量化 Reasoning Token 的消耗將成為評估系統效能的新指標。

⚠️ **初步研究階段，樣本數與模型單一**

需要注意的是，這目前屬於初步發現 (Preliminary findings)，分析樣本為 30 個開發任務，且僅使用單一的 GPT-5 推理模型。不同規模的專案或不同模型（如 Claude 或 DeepSeek）的 Token 消耗模式可能會有所差異。

🎯 **開發 Agent 時，請關注「迭代循環」的成本**

如果你正在構建 AI Agent 系統，建議在設計工作流時，特別關注那些「反覆對話」的環節。減少不必要的迭代，或為高消耗階段設計更高效的過濾機制，將比單純優化單一 Prompt 更有成效。

🔗 **論文連結**
📝 Tokenomics: Quantifying Where Tokens Are Used in Agentic Software Engineering
👤 Mohamad Salim, Jasmine Latendresse, SayedHassan Khatoonabadi, Emad Shihab
🔗 論文：https://arxiv.org/abs/2601.14470

你目前在開發 AI Agent 時，最令你驚訝的 Token 消耗環節在哪裡？歡迎在評論區分享你的經驗 👇

#AI #LLM #Tokenomics #SoftwareEngineering #ChatDev #GPT5 #AgenticWorkflow #軟體工程
