---
title: The Open Source AI Stack
source: Together AI
url: https://www.together.ai/blog/the-open-source-ai-stack
model: claude-code/sonnet
generated_at: '2026-09-09T20:05:03.896853'
score: 84
---

📌 開源 AI 開發堆疊:用 MIGHT 框架拆解你該怎麼選模型

TL;DR:Together AI 提出 MIGHT 框架,把開源模型的開發堆疊拆成五層,幫工程師搞懂該怎麼選模型、選工具。

如果你已經會用 Claude Code,其實你離用開源模型並不遠。這是 Together AI 這篇文章想傳達的核心觀察:換成開源模型,不需要學會訓練模型、買一整排 GPU,或變成機器學習專家,從應用開發者的角度看,堆疊結構其實出乎意料地熟悉。

🤔 開源模型追上來了,問題變成怎麼組合堆疊

文章指出,隨著開源模型品質逼近閉源模型,越來越多開發者與組織想轉向開源,以獲得更多所有權、控制權與成本優勢。由於堆疊裡的每一層彼此獨立,這也讓開發者能自由組合適合自己開發流程的技術選擇,並在新模型推出時,以幾分鐘而非重建整個工作流的代價去嘗試它。

🧩 MIGHT 堆疊的五層

- Model:負責解讀請求、決定該做什麼的智慧層,也就是推理與決策的核心。
- Inference:模型實際執行的基礎設施與推論供應商。
- Gateways and routers:決定哪個模型或供應商處理特定請求的路由層,平衡成本、速度與能力。
- Harness:管理對話、讓模型能存取工具、並連接到你的程式碼庫的應用程式。
- Tools(Skills and MCP):告訴模型如何完成特定任務的知識,包含讓模型與 harness 取得相關 context 的機制。

文章特別提到,多數領先的開源模型現在都是 Mixture-of-Experts(MoE)架構,內含許多專精的「專家」子網路,但每次生成 token 時只啟用其中一小部分,因此能在擁有龐大參數量的同時,只需較少的運算資源。

📊 大模型與小模型:不是誰更好,而是誰更適合

文章以 Kimi K3 作為大模型範例,總參數 1.8T、啟用參數 104B。這類模型適合處理模糊或界定不清的任務,例如重構既有的驗證系統、將程式碼庫升級到新框架、審查 pull request,或釐清資料庫為何突然變慢——這些任務需要同時追蹤多項限制條件,並在長對話中維持跨檔案的一致性。

小模型的代表是 GLM 5.3 Flash,總參數 320B、啟用參數 18B,相較 Kimi K3 小約 6 倍、成本便宜約 20 倍。文章指出,只要任務界定明確、範圍狹窄,小模型的表現能與大模型相當,例如:讓函式多接受一個選項、幫某個檔案寫測試、解釋特定錯誤、審查一個 50 行函式是否有 bug,或重新命名 API 並更新所有呼叫端。這類任務不需要模型建立對整個程式碼庫的深入理解,小模型的優勢在於明顯更快、更便宜,能讓迭代速度更快,也能放心重複執行而不必擔心成本。

💡 把模型當工具箱,而非排行榜上的冠軍

文章提醒,不要把太多時間花在排行榜上找「單一最強模型」,因為 benchmark 把大量行為壓縮成一個分數,而實際工作內容通常更具體;排名稍低的模型,也可能特別擅長你每天在做的那類程式工作。建議的做法是從幾個大小不同的模型開始實際使用,逐漸培養對「哪些任務該交給哪種規模模型」的判斷力。The Open Frontier、Artificial Analysis 等排行榜可作為初步篩選參考;文中提到目前最受歡迎的開源模型包括 GLM 5.3 Flash、DeepSeek V4 Flash、Kimi K3 與 MiniMax M3。

🎯 實務啟示

由於堆疊各層彼此獨立,工程團隊可以先固定住 Harness 與 Tools 層,單獨替換 Model 層做 A/B 測試,降低導入開源模型的門檻。對於範圍明確、重複性高的工作(寫測試、重新命名、解釋錯誤),優先評估用小模型處理以節省成本與延遲;只有在面對模糊、跨檔案、需要多步推理的任務時,才動用大型模型,這樣的分工方式比單純追逐排行榜分數更貼近實際開發需求。

🔗 來源
- 標題:The Open Source AI Stack
- 作者/機構:Together AI
- 連結:https://www.together.ai/blog/the-open-source-ai-stack

#OpenSourceAI #LLM #MixtureOfExperts #KimiK3 #GLM #AIStack #AgenticCoding #DeveloperTools #ModelSelection #TogetherAI
