---
title: '[AINews] Reflection Beam - 501B-A23B American Open Model'
source: Latent Space
url: https://www.latent.space/p/ainews-reflection-beam-501b-a23b
model: claude-code/sonnet
generated_at: '2026-10-06T21:57:57.602283'
score: 88
---

📌 標題: Reflection 推出 Beam：501B 美國自研開放模型能追上中國 SOTA 嗎？

TL;DR: Reflection 發表 23B 啟用參數的 501B MoE 開放模型 Beam，是美國少見的「從零訓練」代表作，但實測效能仍落後中國一線開源模型。

Stealth 超過一年、外界幾乎要放棄期待的 Reflection，這週終於交出成績單——但這份成績單同時也揭露了美國開放模型與中國 SOTA 之間的真實差距。

🤔 背景：等了一年多的「神秘實驗室」終於交卷

Reflection 一年多前就以雄心勃勃的 coding 與 RL 路線圖登場，但之後長期維持 stealth 狀態，外界一度懷疑這間公司是否還會有產品問世。在此期間，整個開放模型生態系並未因此放慢腳步。如今 Reflection 終於發表 Beam，正式宣告自己是一個「有實際產出的新創實驗室」（neolab）。

🧩 架構與訓練規模：23.8T tokens、OCR 管線、萬卡等級 RL

Beam 是一個純文字的 MoE 模型，總參數 501B，啟用參數 23B，鎖定 coding、agentic 與科學任務，並且是從零開始訓練。根據團隊透露，預訓練使用了 23.8T tokens，其中一部分資料來自對數億份 PDF 文件進行 OCR 擷取的管線。後續的 RL/OPD（on-policy distillation）訓練則在 1 萬張 GB300 上穩定跑完，累積超過 1 億次 rollout，涵蓋約 100 萬個任務。完整權重將以 Apache 2.0 授權於本月釋出。

獨立分析者 Elie Bakouch 估計這次預訓練的 BF16 MFU（模型 FLOPs 使用率）僅約 12%，並從架構上判讀為 3:1 交錯排列的全局注意力（global attention）與滑動視窗注意力（sliding-window attention），同時觀察到 Beam 在保留的程式碼困惑度（perplexity）測試上優於 DeepSeek V4。另一位觀察者 Teortaxes 則將 Beam 定性為 DeepSeek V3 的「iso-FLOP 複製品」，並推算其 RL 訓練動用了約 13 億個沙盒環境、四週內最高同時執行 17 萬個。

📊 官方聲稱的成績：SWE-bench Verified 80.9 分

Reflection 公布的關鍵數字包括 SWE-bench Verified 80.9 分，以及相較 GLM 5.2 有 3 到 4 倍的推論效率，整個流程（預訓練加 RL）各花費四週、動用約 1.05 萬張 GB300。背景報導也提到 Reflection 每月在 Colossus 上花費 1.5 億美元運算成本，外加與 Nebius 的 10 億美元合作案，顯示這類「美國自研開放模型」背後的資本投入規模。

💡 定位：接近 GLM 5.2，但仍落後中國一線 SOTA

搶先拿到存取權的 Artificial Analysis 認為，以其展現的智能水準而言，Beam 可能是目前最省 token 的開放模型之一。但多位觀察者，包括 Nathan Lambert，普遍將 Beam 歸類為與 Nvidia、Thinking Machines 同一梯隊的「不錯的美國釋出」，整體水準大致落在 GLM 5.2 附近，部分基準甚至不如 DeepSeek V4.1 Flash，與目前公認的 SOTA（GLM 5.3、Kimi K3、Qwen 3.8 Max、DeepSeek V4.1 Flash）相比仍有明顯差距。

⚠️ 限制：資本投入巨大，但尚未反映在排名上

即便動用了萬卡等級的運算資源與可觀的資本支出，Beam 目前的基準表現仍未能超越中國陣營的頂尖開源模型，MFU 偏低也意味著這套訓練管線在效率上還有最佳化空間。

🎯 實務啟示

對工程師而言，Beam 的重點不在於「打敗 SOTA」，而在於它即將以 Apache 2.0 釋出完整權重並提供 OSS 整合與技術報告，值得在正式開源後實測其宣稱的推論效率與 coding 能力，尤其是其 3:1 混合注意力架構的設計，對於想自建長文本、高吞吐推論服務的團隊會是一個值得研究的公開案例。

🔗 來源
- 標題：[AINews] Reflection Beam - 501B-A23B American Open Model
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-reflection-beam-501b-a23b

#ReflectionAI #OpenWeightModels #MoE #LLM #SWEBench #AIInfrastructure #CodingAgents #GLM #DeepSeek #OpenSourceAI
