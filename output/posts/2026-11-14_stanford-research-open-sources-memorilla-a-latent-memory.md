---
title: Stanford Research Open-Sources Memorilla, a Latent Memory Module for Frozen
  LLMs
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/14/stanford-memorilla-memory-system-16-memory-tokens/
model: claude-code/sonnet
generated_at: '2026-11-14T21:34:42.430738'
score: 100
---

📌 【Stanford新研究】16個記憶Token打敗全文Context

TL;DR：凍結LLM搭配16個記憶token，FactKG分數反而超過塞入全部文件，文件token省108倍。

要讓一個無法再訓練的LLM回答整個文件庫的問題，多數人直覺做法不是把所有東西塞進context，就是用RAG抓最相似的片段。Stanford團隊的新研究走了第三條路：把整個文件集合壓成16個向量。

🤔 **全文context變慢，retrieval又會漏線索**

Full-context prompting隨著歷史變長而愈來愈慢；retrieval只貼最相似的片段，容易漏掉較弱、但其實關鍵的線索。Memorilla想學會「這個問題真正需要知識庫裡的什麼」，而不只是做相似度比對。

🧩 **只練一個記憶模組，凍結的LLM完全不動**

Memorilla是一個記憶模組，把文件集合壓成16個向量，餵給凍結的Qwen3-8B解碼器。整個系統只訓練記憶模組本身，參數量為194,123,776。訓練分三階段：Stage 1用約198萬條Wikipedia paraphrase-reconstruction範例，Stage 2加入約134萬條來自10個QA與摘要資料集的範例，Stage 3在全部8個benchmark上微調。完整流程在4張H100上約需19小時，所有baseline都用同一個凍結的Qwen3-8B比較。

📊 **FactKG贏，但有3個benchmark輸了**

FactKG上，搭配Memorilla的凍結Qwen3-8B拿下84.33%，比把整份文件塞進context的80.43%還高，且用的文件token數少108倍。壓縮效果在NarrativeQA最誇張：16個token取代67,385個文件token，等於4,212倍的壓縮。當作agent記憶使用時，8個記憶token讓Qwen3-4B的TextWorld agent平均成功率從18.6%提升到24.2%。速度方面，1張H100上處理512份文件（約128K tokens）時，Memorilla回答只要0.74秒，全文context則從0.75秒拖到19.9秒，慢27倍，記憶模組本身推理僅約2毫秒。搭配選用的memory cache預先算好cross-attention的keys/values，在1張B200上，100萬份文件時單次問答8.1毫秒，400萬份文件時33毫秒，加上torch.compile後100萬份文件情境可降到5.0毫秒，不過400萬份文件的cache要耗掉80 GiB記憶體。

⚠️ **摘要太短時，壓縮反而沒意義**

Memorilla在3個benchmark上輸了。PubMedQA上只拿59.00%，LLMLingua-2拿69.00%，因為那些摘要總共只有324個token，壓縮本身沒什麼空間可以發揮。MemoRAG則在PersonalizationV4（67.88% vs 66.65%）與NarrativeQA ROUGE-L（20.51 vs 19.31）上領先，但分別用了約690倍與50倍的文件token。

🎯 **想做長期記憶的團隊可以直接拿checkpoint**

程式碼、訓練腳本與checkpoint都以Apache 2.0公開，可用uv在Linux上安裝，呼叫MemoryVLLM.from_pretrained載入（首次會下載約25GB模型）。checkpoint放在memorilla/Memorilla-Qwen3-8B下，分Stage 1/2/3、PV4、PMv2資料夾，必須搭配訓練時使用的decoder。自訂資料需要準備含collection_id、question、answer、documents欄位的parquet檔案。團隊也釋出了PersonalizationV4，包含149個合成使用者、每人200則對話，CC BY 4.0授權。對受限於context window與延遲、又想讓LLM記住大量文件的場景，這提供了介於full-context與RAG之間、壓縮率與可重現性都不錯的選項。

🔗 **來源**
- 標題：Stanford Research Open-Sources Memorilla, a Latent Memory Module for Frozen LLMs
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/14/stanford-memorilla-memory-system-16-memory-tokens/

#LLM #Memorilla #Stanford #MachineLearning #NLP #RAG #OpenSource #AIResearch #ContextWindow #Qwen3
