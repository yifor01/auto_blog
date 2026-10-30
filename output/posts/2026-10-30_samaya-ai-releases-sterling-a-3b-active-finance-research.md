---
title: 'Samaya AI Releases Sterling: A 3B-Active Finance Research Agent Model that
  Beats Claude Fable 5.1 on FrontierFinance at 11x Lower Cost'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/30/samaya-sterling-post-trained-finance-research-model-frontierfinance/
model: claude-code/sonnet
generated_at: '2026-10-30T21:36:01.037783'
score: 102
---

📌 Samaya Sterling:3B 活躍參數的金融研究 agent,成本只要對手的十一分之一

TL;DR:小模型配精簡 harness,在金融研究基準上以 1/11 成本打贏 Claude Fable 5.1。

一個只有 3B 活躍參數的模型,在專門設計來考驗金融研究能力的基準上,贏過了 Claude Fable 5.1,而且每道題的花費只要對手的不到一成。這不是模型規模的勝利,而是「模型 + harness 共同訓練」的勝利。

🤔 **問題:怎麼讓小模型在狹窄領域裡打贏大模型**

Samaya AI 發布了 Samaya Sterling,一個針對 agentic 金融研究任務「後訓練」(post-trained)的模型,底層架構是 NVIDIA 的 Nemotron 3.5 Lightning,一個 30B 的 mixture-of-experts 模型,實際活躍參數僅 3B。在 Samaya 自建的 FrontierFinance 基準上,Sterling 拿下 58.9% 的分數,高於 Claude Fable 5.1 的 55.9%;而每道題的成本,Sterling 只要 0.61 美元,Fable 5.1 則要 6.89 美元。根據 Maithra Raghu 在 X 上的公告,這個專案最初只是一個 2 人團隊研究 agentic 編排效率的嘗試。

🧩 **把精力花在 harness 的瘦身,而不只是模型本身**

Sterling 是 Nemotron 3.5 Lightning 經 LoRA 後訓練而成的版本,職責是作為金融研究 agent:規劃研究路徑、呼叫金融工具、蒐集證據,再把發現交給一個獨立的報告撰寫模型。Samaya 團隊把原本給大模型用的生產級金融 harness 拿來適配小模型,具體做法包括:從系統提示與工具描述中拿掉詳細的指導文字、合併工具以縮短提示長度。此外還引入兩個輔助模型管理上下文:一個「condenser」負責壓縮冗長的工具回傳結果,一個「compactor」負責在對話軌跡變長時持續總結。再加上一個「研究預算」限制 agent 能工作多久,之後才由報告撰寫模型根據已蒐集的內容作答。

訓練使用 LoRA,在 Thinking Machines Lab 的訓練 API「Tinker」上進行,共分 4 個階段完成。

📊 **每個訓練階段都有進步,高努力模式再往上衝一段**

FrontierFinance 基準由 220 道公開查詢組成,對照專家撰寫的評分標準,評分方式是 3 個模型組成的評審小組(judge panel)。Samaya 團隊表示基準題目沒有被用於訓練,checkpoint 的選擇則依據 100 道內部驗證題目。

四個訓練階段(加上 base)的分數依序是 42.5%(base)、51.4%、54.8%、57.5%、58.9%,呈穩定遞增;過程中模型的「中位數工具呼叫次數」也從 3 次上升到 17 次,顯示模型逐漸學會做更深入、更多步的研究。

在標準模式下,Sterling 以 0.61 美元、282 秒拿下 58.9%;Fable 5.1 則以 6.89 美元、268 秒拿下 55.9%。有趣的是,Samaya 自家的「高努力」系統本身反而比 Sterling 低了 2.9 個百分點,成本卻要 1.81 美元。而當 Sterling 本身也切換到高努力模式,分數可以推進到 60.6%,成本 1.83 美元、耗時 372 秒;在題目難度最高的那三分之一子集上,分數從 31.8% 一舉提升到 45.2%。

值得注意的成本結構:Sterling 模型本身每道題只要 0.04 美元,剩下的 0.61 美元大部分花在工具呼叫與輔助模型上。文中也提醒,FrontierFinance 所有欄位的數字皆來自 Samaya 自家部落格,屬於自我報告的結果。

💡 **小模型 + 精簡 harness 的具體配方**

對開發者而言,這個案例給出的啟示相當具體:與其一味追求更大的底層模型,不如把 harness 本身(系統提示、工具描述、上下文管理策略)跟著小模型一起共同設計與訓練。當任務領域夠狹窄(這裡是金融研究),精簡後的提示加上針對性的 LoRA 後訓練,可以讓一個活躍參數僅 3B 的模型,在特定基準上超越通用型的大模型,同時把成本壓低一個量級以上。

⚠️ **侷限**

這些數字全部來自 Samaya 自建、自評的 FrontierFinance 基準,且由廠商自行報告,尚缺乏第三方的獨立驗證;分數優勢(58.9% 對 55.9%)雖然明確,但差距本身不算巨大,在不同任務分佈下是否能維持同等優勢,仍待更多外部測試檢驗。

🎯 **實務啟示**

如果你的團隊正在為某個垂直領域(金融、法務、醫療等)打造 agent,這個案例提供了一條可行路徑:先把生產環境裡給大模型用的 harness 做瘦身(精簡系統提示、合併工具、加入上下文壓縮的輔助模型),再用 LoRA 對一個相對小的開源或半開源模型做分階段後訓練。狹窄領域裡,「協同設計模型與 harness」可能比單純換更大的底層模型更划算。

🔗 **來源**
- 標題:Samaya AI Releases Sterling: A 3B-Active Finance Research Agent Model that Beats Claude Fable 5.1 on FrontierFinance at 11x Lower Cost
- 作者/機構:Asif Razzaq(MarkTechPost);模型由 Samaya AI 發布
- 連結:https://www.marktechpost.com/2026/10/30/samaya-sterling-post-trained-finance-research-model-frontierfinance/

#SamayaAI #Sterling #FinanceAI #AgenticAI #LoRA #Nemotron #MixtureOfExperts #LLMBenchmark #CostEfficiency #FinancialResearch
