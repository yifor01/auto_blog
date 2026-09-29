---
title: 'Anthropic Releases Claude Sonnet 5.5: 70.6% on Terminal-Bench 4.0 at the Same
  $2/$10 Price'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/28/anthropic-releases-claude-sonnet-5-5-70-6-on-terminal-bench-4-0-at-the-same-2-10-price/
model: claude-code/sonnet
generated_at: '2026-09-29T21:40:21.886668'
score: 97
---

📌 Claude Sonnet 5.5：同價，卻靠少用 token 省成本

TL;DR：Anthropic 推出 Claude Sonnet 5.5，價格完全不變，靠 token 效率大幅降低實際使用成本。

當大家都在等旗艦模型漲價或降價的消息時，Anthropic 這次選了第三條路：價格一分不動，把功夫下在「用更少 token 做完同樣的事」。

🤔 定位：Opus 5.5 的快速、低成本搭檔

Claude Sonnet 5.5 是 Claude 5.5 家族的第二個模型，緊接在 Claude Opus 5.5 之後推出。Anthropic 將其定位為更快、更便宜的互補選項，鎖定範圍明確的日常任務、修 bug，以及文件、簡報、試算表這類精修工作。

🧩 規格與部署

Sonnet 5.5 已在 Claude Platform 上以 claude-sonnet-5-5 提供，同時支援 AWS、Google Cloud、Microsoft Azure；它是閉源權重模型，無法自架。規格上具備 100 萬 token context、最多 12.8 萬 token 輸出，知識截止日為 2026 年 6 月。Adaptive thinking 預設開啟，分成 low、medium、high、xhigh、max 五個 effort 等級，且不同介面的預設等級不同：Claude Code 與 Claude 應用程式預設 Medium，Claude Platform 則預設 High。

📊 Benchmark 與一個反直覺結果

官方公布的成績為 Terminal-Bench 4.0 上 70.6%（方法論寫在 Sonnet 5.5 System Card 中，數字皆為 Anthropic 自行提供）。有趣的是，在 FrontierCode 這項測試上，Max 等級的分數反而低於 Xhigh，原因是 Max 更常觸發多代理程式碼審查流程，有時因此造成逾時或超出範圍的修改，被 FrontierCode 扣分。Anthropic 也明確表示，在複雜、開放式任務上 Opus 5.5 仍明顯更強。

💡 價格不變，省的是 token 用量

定價與 Sonnet 5 相同：每百萬 input tokens 2 美元、output tokens 10 美元，cache 讀取 0.20 美元、cache 寫入 2.50 美元（每百萬 tokens），是 Opus 5.5（4/20 美元）的一半。Anthropic 強調這次省下的錢來自 token 使用效率，而非降價。客戶數據支持這個說法：Balyasny Asset Management 每次回答平均用約 12.1 萬 tokens，相較 Sonnet 5 的 49.7 萬 tokens；Base44 平均每次應用程式建置只需 3.6 次迭代，Opus 5 需要 7.7 次；Zendesk 的工單處理速度則快了 20%。

🎯 實務啟示

如果團隊已經在用 Sonnet 5，遷移到 5.5 價格不變，重點應該放在檢查自己的 workload 是否真的受益於 token 效率提升——不同介面的 effort 預設不同，值得確認實際跑的等級是否符合任務複雜度。Anthropic 也提供了 migration guide 與 API migration checker，可用來評估遷移的實際節省幅度；但要注意，真正的成本比例取決於你自己的任務型態，官方數字僅供參考方向。

🔗 來源
- 標題：Anthropic Releases Claude Sonnet 5.5: 70.6% on Terminal-Bench 4.0 at the Same $2/$10 Price
- 作者／機構：Michal Sutter，MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/28/anthropic-releases-claude-sonnet-5-5-70-6-on-terminal-bench-4-0-at-the-same-2-10-price/

#Anthropic #ClaudeAI #LLM #AIAgents #SonnetAI #GenerativeAI #APIPricing #SoftwareEngineering #MachineLearning #AICoding
