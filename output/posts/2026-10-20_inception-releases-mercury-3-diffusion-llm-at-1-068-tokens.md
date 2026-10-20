---
title: Inception Releases Mercury 3 Diffusion LLM at 1,068 Tokens per Second
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/19/inception-mercury-3-diffusion-llm/
model: claude-code/sonnet
generated_at: '2026-10-20T20:47:10.841256'
score: 98
---

📌 Diffusion LLM 衝上 1,068 tokens/秒,品質也追上了

TL;DR:Inception 發布 Mercury 3 diffusion LLM,號稱單秒輸出破千 token,12 項測試中有 8 項贏過 GPT-6 Luna 與 Claude Haiku 5.5。

一般的自回歸(autoregressive)模型寫文字像接力賽,一個 token 等前一個寫完才能生成下一個。Inception 的 Mercury 系列反其道而行:先畫出整個答案的草稿,再用幾輪平行修正逐步精煉每個位置。這次最大的懸念是:模型做大之後,這套 diffusion 路線的速度優勢還撐得住嗎?Inception 給出的答案是肯定的。

🤔 **從草稿到定稿,而非逐字接龍**

Diffusion LLM 的生成邏輯和一般 LLM 不同:它不是一個 token 接一個 token 寫,而是從整段答案的粗略草稿出發,再透過幾次平行修正逐步精煉每個位置。因為減少了序列化的步驟數,同樣的 GPU 上輸出速度自然更快。Mercury 3 是 Inception 第四代 Mercury 模型,接在 Mercury 1(2025 年推出)、Mercury 2、Mercury 2.5(加入可調式推理與 260K context window)之後。

📊 **總參數暴增 40 倍,速度仍維持破千**

根據 Inception 官方數據,Mercury 3 的總參數量是 Mercury 1(mini 版)的 40 倍以上,兩代之間的平均品質分數成長了約 3 倍,而速度依然維持在 1,000 tokens/秒以上,官方在 NVIDIA GPU 上測得 1,068 tokens/秒,context window 達 1M tokens。

在 Inception 自家的基準表(中等設定)中,Mercury 3 在指令遵循與 agentic coding 上拿下最大幅度的領先:IFBench 達 76.84 分,比 GPT-6 Luna 高 15 分;SWE-Bench Atlas 達 51.08 分,遠高於 Luna 的 33.33 與 Haiku 5.5 的 32.26;GPQA Diamond 則是 89.23 分。

不過輸的地方也值得留意:Claude Haiku 5.5 在 DeepSWE v1(51.62 vs 46.31)與 MRCR v2(78.40 vs 75.50)上勝出;GPT-6 Luna 則在 AA-Omniscience-Public(46.94 vs 46.44)與 AA-LCR v1.1(78.30 vs 77.67)小幅領先。長文本檢索與較長的 coding 任務,仍是 Mercury 3 相對弱的地方。

💡 **自報分數,看看就好**

需要提醒的是,以上速度與基準分數都來自 Inception 自家的測試表格,規格與定價則各自取自官方文件;Inception 引用的 4 個早期合作夥伴的說法,也是客戶自述而非獨立評測,解讀時宜保留一分保留。

🎯 **對開發者的實務意義**

Mercury 3 已上架 Inception API Platform、OpenRouter、Baseten 與 Vercel,API 相容 OpenAI 介面,模型字串為 mercury-3,並支援 reasoning_effort 參數。定價方面,官方標價為每 1M input token 0.20 美元、output token 0.70 美元,上市期間五折(0.10 / 0.35 美元),cached input 再打一折,新帳號贈送 1 億 token,企業方案另提供專屬算力、自動擴展與可設定的資料保留政策。對於要蓋 agent、語音機器人或搜尋工具的團隊來說,Mercury 3 是一個「先求快、分數也不差」的選項,值得在延遲敏感的場景納入評估名單。

🔗 **來源**
- 標題:Inception Releases Mercury 3 Diffusion LLM at 1,068 Tokens per Second
- 作者/機構:Jean-marc Mommessin,MarkTechPost
- 連結:https://www.marktechpost.com/2026/10/19/inception-mercury-3-diffusion-llm/

#DiffusionLLM #Inception #Mercury3 #LLM #AIInference #MachineLearning #GenerativeAI #AgenticCoding #LLMBenchmark #AIInfrastructure
