---
title: '[AINews] Meta Muse Wonder & Wonder Full: MSL’s Claude 5.5-tier Frontier Model'
source: Latent Space
url: https://www.latent.space/p/ainews-meta-muse-wonder-and-wonder
model: claude-code/sonnet
generated_at: '2026-10-13T22:11:41.855642'
score: 85
---

📌 【Meta】14個月衝上frontier：Muse Wonder評測數字總彙整

TL;DR：MSL推出第二代Muse Wonder家族，多項agentic與coding評測逼近甚至追平Claude、GPT頂規模型。

從「重建基礎」到「推進frontier」，Meta Superintelligence Labs（MSL）只花了14個月，就讓一個新成立的研究室交出能跟Opus 5.5、Fable 5掰手腕的成績單——這速度本身就是這則新聞最大的亮點。

🤔 **一個14個月的研究室，補上了自己的模型家族命名**

MSL在今年4月發表第一代Muse Spark，這次推出的Muse Wonder（代號「Watermelon」）是第二代家族，補齊了Meta自己的模型分層命名，對應OpenAI的Sol/Terra/Luna與Anthropic的Opus/Sonnet/Haiku。發布前，Meta內部員工在社群上以西瓜表情預告，暗示這次規模不小。

🧩 **兩個模型、兩種存取管道，外洩定價$4/$20 per M tokens**

這次共兩款：Muse Wonder（快速版frontier模型）與Muse Wonder Full（完整版）。Wonder可透過Meta Model API與Muse Code使用，Full只開放給Muse Code訂閱用戶，且最高推理層級「Wonder Full」僅限Power/Maximum Usage方案。社群流出的定價為每百萬token輸入$4、輸出$20、快取輸入$0.20，context window達1M。官方主打三項能力：Active Memory（記住跨日、跨週、跨月的互動）、Active Focus（卡關也能持續推進任務）、以及金融與法律領域的domain expertise（官方稱在health領域也「表現強勁」）。訓練上延續了Spark發布後持續擴大的pretraining與RL規模；安全面則聲稱針對adversarial instruction的穩健性與個人隱私資訊的謹慎處理做了訓練，但沒有引用詳細的system card。發布當天還出現Muse Code配額異常消耗過快的bug，官方在同一天修復並重置了所有用戶的配額。

📊 **第三方評測：Intelligence Index逼近Opus 5.5，coding評測追平Claude Code**

第三方機構Artificial Analysis的Intelligence Index v4.3顯示，Wonder Full（max）拿56分、Wonder（max）52分，上一代Spark 1.3（max）為48分，目前仍由Opus 5.5以58分領先；而Spark 1.3到Wonder的發布間距僅6週。agentic向的GDPval-AA v2.1 Elo從1681上升到1857；在10項指標中，Wonder Full於6項排進前三，其中GDP.pdf與CritPt拿下第一（皆33%），AA-Briefcase、AutomationBench-AA（71%）與SciCode（63%）排第三。非Full版的Wonder進步也不小：Terminal-Bench從33%升到52%，AutomationBench從58%升到68%。輸出token用量方面，兩款模型平均約54k，比Spark 1.3的60k少了約一成，對照Gemini 4 Argon的62k、Fable 5.1的78k、GPT-6.1 Sol的38k與GPT-6 Astra的27k；輸入token用量則是Full 6.44M、Wonder 7.69M。每個index任務的成本，Wonder為$4.52，對照表中Fable 5.1為$7.63、Opus 5.5為$5.98、Sonnet 5.5為$5.46、Astra為$3.26、Argon為$1.99、Sol為$0.72、Spark 1.3為$1.60；Wonder Full因未公布token價格，無法算出對應成本。

在Coding Agents Index上，Wonder Full搭配Muse Code拿下68分，與Claude Code+Sonnet 5.5（68分）打平，領先Opus 5.5（66分）；Wonder本身63分，上一代Spark 1.3為54分。另一項私有測試ProofBench，Wonder Full拿下94/100，遠超Spark 1.3的58分（頭部模型落在99至100分）；Terminal-Bench 4的分數較上一代翻倍以上，與Fable 5.1並列第4，且在Terminal-Bench上少用約30%輸出token、ProofBench少用約40%、Vibe Code Bench則以一半步驟就拿到同樣分數。Wonder本身在Vals Index排第10，較上一代提升7.9分，平均每個任務耗時約37分鐘（Full為57分鐘），Terminal-Bench 4提升38.9分，且少用約20%token。

Meta自己公布的headline數字則包括：SWE-Marathon上Wonder Full拿57.5%（Opus 5.5為46.3%、Astra為42.5%）；DeepSWE v1.1拿79.0%（Opus為74.2%、Astra為74.1%）；Harvey LAB拿13.1分（Astra為8.6分）；MemoryBench拿85.5分（Opus為81.5分）。

💡 **刻意秀出的「ID vs OOD」對比，是用來反駁benchmaxxing的證據**

Meta特別公開了模型在「有做過post-training的任務」與「沒做過post-training的任務」上的表現對比，以及相對Spark 1.3的out-of-distribution增益，用來證明這不是單純針對特定基準硬刷分數，業內有人稱這是「big model smell」。合作夥伴方面也有人指出，token效率是這次最大亮點，在自家的網路安全基準上零拒絕率（且Wonder在這項上甚至高於Full），並認為MSL在alignment上有實質進展；但同一批回饋也提到，模型在科學發現的直覺判斷上仍偏弱，相關的RSI Index結果尚未公布。

⚠️ **熱鬧背後的缺口**

安全聲稱沒有對應的詳細system card；Wonder Full至今沒有公開的token計費，無法獨立核算成本；多數評測細節來自社群貼文與合作夥伴的非正式回饋，而非統一的第三方審核文件；發布當天的配額bug也顯示上線流程還不穩定。

🎯 **實務啟示**

如果要把Wonder系列納入自家agent pipeline的候選名單，Coding Agents Index與Claude Code+Sonnet 5.5打平這點值得實測驗證；同時輸出token用量（Wonder約54k，對照Fable 5.1的78k）是另一個容易被忽略但直接影響成本的比較維度，評估時建議把token效率和單任務成本一起放進評分表。

🔗 **來源**
- 標題：[AINews] Meta Muse Wonder & Wonder Full: MSL's Claude 5.5-tier Frontier Model
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-meta-muse-wonder-and-wonder

#Meta #MSL #MuseWonder #FrontierModel #AgenticAI #LLMBenchmark #ArtificialAnalysis #CodingAgents #AIIndustry #MachineLearning
