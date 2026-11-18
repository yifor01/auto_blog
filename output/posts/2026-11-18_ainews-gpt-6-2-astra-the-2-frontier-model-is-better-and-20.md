---
title: '[AINews] GPT-6.2 Astra, the #2 Frontier Model is better and 20%-600% cheaper,
  but has mixed reviews; 6.2 Sol likely main workhorse'
source: Latent Space
url: https://latent.space/p/ainews-gpt-6-2-astra-the-2-frontier-model-is-better-and-20-600-cheaper-but-has-mixed-reviews-6-2-sol/
model: claude-code/sonnet
generated_at: '2026-11-18T23:40:16.752947'
score: 96
---

📌 GPT-6.2 Astra 與 Sol 同臺發布:效能提升、成本大降,評價卻兩極

TL;DR:OpenAI 在 Anthropic 掛牌交易前兩天發布 GPT-6.2 Astra 與 Sol,效能進步、價格更親民,但社群反應明顯分裂。

同一天發布兩顆旗艦模型,時間點還卡在對手掛牌交易前兩天——OpenAI 這次的時機選得很微妙。但真正有意思的是後續:這次發布的技術數字相當亮眼,社群的第一波評價卻出現罕見的強烈負面聲音。

🤔 **兩顆模型,兩種定位**

OpenAI 同時推出 GPT-6.2 Astra 與 GPT-6.2 Sol,透過 ChatGPT Work、Codex(Plus、Pro、Enterprise、Edu)以及 API(`gpt-6.2-astra`、`gpt-6.2-sol`)開放。兩者都支援 1M context,輸出上限為 128K token。API 定價上,Astra 為每百萬 token 輸入 $8、快取輸入 $0.40、輸出 $40;Sol 則維持前代定價,輸入 $2、快取輸入 $0.10、輸出 $10。

根據 Artificial Analysis 的測試,Sol 的表現可以追平前一代 Astra,但成本僅約其 15%。在 Intelligence Index 上,新 Astra 拿下 62 分,略落後於 Fable 5.2 的 65 分。換算下來,Anthropic 仍握有「最強模型」頭銜,OpenAI 則拿下「每美元智能密度最高」的位置。

📊 **幾個值得注意的基準表現**

- FrontierMath Erdős:Epoch 驗證 Astra 在 68 題中用 Lean 證出 7 題,此前最佳紀錄是 3 題。
- Epoch Agents' Last Exam 1.1:Astra 在 xhigh 設定下比前代 GPT-6 Astra(max 設定)高出 5.2 分,且成本不到三分之一;比 Fable 5.2 高 5.5 分,成本僅約其 5%。
- GDPval v2:Astra 比前代少用 22% 的輸出 token。
- Mercor 的 OpenWorldEngineer(長時間工程任務):Astra 67.2%,Fable 5.2 54.6%,前代 GPT-6 Astra 44.2%。
- Vals 的多輪 Vibe Code Bench:Astra 排名第一,Sol 排名第三。
- 另外,OpenAI 將 Astra 在「AI 自我提升」這項 Preparedness 指標上評為 High,是該公司首次有外部釋出模型拿到這個等級;Vals 的 RSI-Index 也從 27.07% 升至 29.01%(50% 代表人類參照基準)。

💡 **數字好看,評價卻兩極**

這次發布最特別的地方,是出現了相當強烈的負面網紅評價,甚至促使官方做出回應式說明。Matt Shumer 測試數週後形容這兩顆模型「基本上不堪用」,說自己用 Opus 與 Fable 架設的 agent 會拒絕掉 Astra 產出的多數 subagent 工作成果。Pietro Schirano 則認為自己早期遇到的問題多半出在 harness 配置,而非模型本身;Peter Gostev 拿 Astra 與 Fable 做視覺化程式碼測試時,特別點名 Astra 畫出的 SVG 孔雀圖案有問題。整體看來,部分批評可能有「網紅極端化」的成分,但其中一些關於 RL 訓練痕跡(RL artefacts)明顯且怪異的指摘,看起來是站得住腳的。

🎯 **對工程師的實際影響**

如果你在評估要不要切換到新模型,這次的訊號是:先看任務類型,而非只看 Intelligence Index 總分。Sol 在「準確率打平前代、成本砍到約 15%」這個定位上,對大量常規任務的性價比相當有吸引力;Astra 則在長時間工程任務、數學證明這類高難度場景展現優勢。但鑑於早期回饋顯示 harness 配置差異會明顯影響實際體感,建議先用自己的 harness 跑過一輪再下判斷,不要只看官方或單一評測的分數。

🔗 **來源**
- 標題:[AINews] GPT-6.2 Astra, the #2 Frontier Model is better and 20%-600% cheaper, but has mixed reviews; 6.2 Sol likely main workhorse
- 作者/機構:Latent Space
- 連結:https://latent.space/p/ainews-gpt-6-2-astra-the-2-frontier-model-is-better-and-20-600-cheaper-but-has-mixed-reviews-6-2-sol/

#OpenAI #GPT6 #LLM #AIBenchmark #FrontierModel #AIIndustry #CodingAgent #ArtificialIntelligence #ModelRelease #TechNews
