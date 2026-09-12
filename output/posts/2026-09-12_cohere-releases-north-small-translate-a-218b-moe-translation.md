---
title: 'Cohere Releases North Small Translate: A 218B MoE Translation Model That Scores
  83.6 on WMT26 Across 50 Languages'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/10/cohere-releases-north-small-translate-a-218b-moe-translation-model-that-scores-83-6-on-wmt26-across-50-languages/
model: claude-code/sonnet
generated_at: '2026-09-12T19:29:20.402396'
score: 88
---

📌 Cohere 開放翻譯模型：218B MoE 只啟用 25B 參數

TL;DR：Cohere 發布開放權重翻譯模型 North Small Translate,WMT26 平均 83.6 分,標榜比同級模型便宜數十倍。

2017 年那篇《Attention Is All You Need》,靠著 WMT14 英德、英法翻譯任務證明了 Transformer 的威力。九年後,Cohere 帶著一個專門為翻譯打造的模型,重新回到了這個最初的問題。

🤔 **翻譯,被 Cohere 定位成「主權」問題**

North Small Translate 是 Cohere 與 Cohere Labs 共同發布的開放權重機器翻譯模型,也是 North 系列的第一個成員,接續先前的 Tiny Aya 與 Command A Translate。Cohere 在發布貼文中把翻譯框定為一個攸關組織能否保持主權的問題:無法與全球溝通的組織,就無法維持主權。模型的開發過程與語言服務商 RWS 合作,由其 Language Weaver 團隊的科學家與語言專家協助把關真實世界的翻譯品質。

🧩 **decoder-only 稀疏 MoE,支援 50 種語言**

North Small Translate 是一個 decoder-only 的稀疏 MoE Transformer,總參數 218B,每個 token 實際啟用約 25B 參數,換算下來大約只有 11.5% 的權重會被啟用。也就是說,單次運算的算力消耗跟著 25B 走,但要跑起來仍得把全部 218B 參數載進記憶體。它涵蓋 50 種語言,從阿爾巴尼亞語到越南語都在支援範圍內。除了標準版之外,還有一個 Agentic 版本,會跑多輪流程,自己找出並修正翻譯錯誤。

📊 **跟 DeepL、Google Translate、Gemma 比一輪**

Cohere 在自家 WMT26 評測中,North Small Translate 平均分數為 83.6,官方表示這個成績超越 DeepL、Google Translate,也贏過 GLM 5.2 與 Mistral Large 3 等開放模型。

| 項目 | North Small Translate | 對照組 |
|---|---|---|
| WMT26 全語言平均 | 83.6 | — |
| 歐洲語言(標準版) | 82.17 | Gemma 4 31B：72.73 |
| 南亞語言 | 86.16 | Gemma 4 31B：88.04 |
| 吞吐量(低併發) | 112 tokens/秒 | Gemma 4 31B：81 tokens/秒 |
| 吞吐量(高併發) | 39 tokens/秒 | Gemma 4 31B：30 tokens/秒 |
| 長文件翻譯(2 章節/1 次呼叫,xCOMET-XL) | 48.9 | Google Translate：21.3；Gemma 4 31B：19.4 |
| 每工作成本 | $0.000676(平均 661 token,得分 80.1) | Gemini 3.1 Pro Preview(high)：$0.038928；Qwen 3.5 397B A17B：$0.004525；Command A+：$0.005158 |

Cohere 表示這代表吞吐量最多提升 1.4 倍,而在長文件翻譯與整體成本上的優勢更為明顯,推理成本比 Gemini 3.1 Pro Preview(high)便宜約 58 倍。

⚠️ **數字是誰跑出來的,要看清楚**

上述所有分數都是 Cohere 自己跑出來的結果,並以 GPT-5.6-Sol 作為評分裁判,在獨立的第三方 WMT26 結果出爐之前,應該當作廠商自報數據看待。值得注意的是,在南亞語言這一項,Gemma 4 31B 的表現反而略勝 North Small Translate 一籌(88.04 對 86.16)。

🎯 **實務啟示**

如果你的場景是大量文件或長篇內容翻譯,且對單次呼叫成本敏感,North Small Translate 在 Cohere 自己的測試裡展現出明顯的成本優勢,值得列入評估清單。想試用可以直接透過 Cohere Chat V2 API,免費用到達速率限制為止;若需要合規自架,Cohere 也釋出了與正式環境相同的 3 個 checkpoint,支援非商業自架或商業授權部署。

🔗 **來源**
- 標題：Cohere Releases North Small Translate: A 218B MoE Translation Model That Scores 83.6 on WMT26 Across 50 Languages
- 作者／機構：Asif Razzaq，MarkTechPost（模型由 Cohere 與 Cohere Labs 發布,與 RWS 合作）
- 連結：https://www.marktechpost.com/2026/09/10/cohere-releases-north-small-translate-a-218b-moe-translation-model-that-scores-83-6-on-wmt26-across-50-languages/

#Cohere #MachineTranslation #MoE #OpenWeightModels #WMT26 #NLProc #LLM #Multilingual #AIInfrastructure #TranslationAI
