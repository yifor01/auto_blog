---
title: Even the best AI agents struggle with everyday life
source: TechCrunch AI
url: https://techcrunch.com/2026/11/24/even-the-best-ai-agents-struggle-with-everyday-life/
model: claude-code/sonnet
generated_at: '2026-11-25T01:38:43.193608'
score: 102
---

📌 ShellBench 揭露真相：最強 AI Agent 處理日常瑣事,失敗率仍超過三分之一

TL;DR：新基準 ShellBench 顯示,連 OpenAI、Anthropic、Meta 最頂尖的模型,處理真實生活瑣事時失敗率都超過三分之一。

這幾個月,各家 AI 公司都在賣一個願景:把購物排程、旅行規劃、日常雜事統統交給個人 AI agent 處理。數百萬用戶已經買單。但一份新研究顯示,就連最先進的模型,面對真實生活裡那些雜亂無章的細節,依然力有未逮。

🤔 **一千萬筆真實互動餵出來的基準**

ShellBench 是一個全新的日常 agent 工作基準,由 The OpenClaw Foundation、Parsewave、Hugging Face、Red Hat 與 UC Berkeley 的研究者共同開發,取材自超過一千萬筆匿名化的真實 AI agent 互動紀錄,目的是評估 agent 在人們實際委託的日常工作上表現如何。這份研究出現的時間點正好是 Meta、OpenAI、Anthropic 分別以 Muse、Dots、Claude Duet 搶攻個人 AI 助理市場之際——Meta 曾表示,Muse 在美加地區上線六週內就有超過一千萬人設定使用,其中約四分之一每天都在用。

📊 **連最強的模型,三次重跑都答對的機率也不到一半**

跨所有受測模型,整體有 15.7% 的嘗試至少違反一項安全要求,往往導致非預期的後果。在最高分的模型中,OpenAI 的 GPT-6 Astra 表現最好,但研究者把同一個任務在相同條件下重跑三次後,發現它三次都答對的比例還不到一半——對於理應能無人值守、在背景自主運行的助理來說,這代表使用者可能得反覆重跑才能拿到一個敢信任的結果。另外,大約 10% 原本「表面上做對了」的嘗試,實際上仍違反了至少一項安全標準。

幾個具體任務的數字更直觀:agent 在處理涉及接送小孩下課的情境時,有 79.5% 的比例沒有妥善考慮到這件事;在處理筆電保管紀錄時,有 18.6% 的嘗試未能正確識別並保留一個敏感的銀行上傳權杖(token),等於把不該外流的資訊暴露出去;在另一項發票相關任務中,agent 有 40.3% 的機率會推薦重複或錯誤的付款。

💡 **模型選擇比 harness 選擇更關鍵,但頂尖模型例外**

研究同時測試了不同的 agent harness(控制模型存取資訊、使用工具、採取行動的軟體框架)。整體而言,模型本身的選擇對表現的影響大於 harness 的選擇,但在最頂尖的模型之間,harness 的差異反而變得更重要。舉例來說,OpenAI 的 GPT-6 Astra 在 Pi harness 裡表現勝過 Anthropic 的 Claude Fable 5.2,但換到 Claude Code 這個 harness 裡,表現卻反而較差。Meta 的 Muse Wonder Full 在 Pi 裡拿下 56% 的成功率,但換到 Claude Code 裡只剩 38.1%；Muse Wonder 1.0 在五種受測 harness 下的平均成功率則是 39.7%。值得留意的是,研究者測試的是 OpenAI、Anthropic、Meta 的底層模型,並未在 Muse、Dots、Claude Duet 各自的原生 harness 裡進行測試,因此這些數字未必能代表數百萬消費者實際使用這些產品時的體驗。

⚠️ **「做對」與「安全」是兩條不完全重疊的標準**

ShellBench 刻意把成功任務拆成「有沒有完成要求」與「有沒有符合安全標準」兩個維度來看,而研究顯示這兩者並不必然一致——不少表面上任務完成的嘗試,其實悄悄違反了安全要求,這種落差正是個人助理「無人值守運作」模式下最容易被忽視的風險。

🎯 **給工程師的啟示**

如果你的團隊正在打造或整合個人 AI 助理類產品,ShellBench 的結果提醒我們:評估重點不能只看單次任務是否完成,還要看跨多次重跑的一致性,以及是否有獨立的安全違規檢查機制。選用模型時也別忘了連帶考慮 harness 本身的設計,同一顆模型換個 harness 表現可能差到十幾個百分點。

🔗 **來源**
- 標題：Even the best AI agents struggle with everyday life
- 作者／機構：Rebecca Bellan / TechCrunch AI
- 連結：https://techcrunch.com/2026/11/24/even-the-best-ai-agents-struggle-with-everyday-life/

#ShellBench #AIAgents #AIBenchmark #AgentSafety #OpenAI #Anthropic #Meta #PersonalAI #AIReliability #AgentHarness
