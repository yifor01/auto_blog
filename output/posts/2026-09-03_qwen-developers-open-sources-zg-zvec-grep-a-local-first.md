---
title: 'Qwen Developers Open-Sources zg (zvec-grep): A Local-First Search Layer Unifying
  ripgrep, BM25, and Vector Search'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/02/qwen-developers-open-sources-zg-zvec-grep-a-local-first-search-layer-unifying-ripgrep-bm25-and-vector-search/
model: claude-code/sonnet
generated_at: '2026-09-03T20:09:42.228257'
score: 106
---

📌 【Qwen開源】zg：把ripgrep、BM25、向量搜尋合而為一的coding agent搜尋層

TL;DR：Qwen團隊開源本地優先的zg搜尋工具，一套介面同時支援關鍵字比對與語意搜尋，實測可減少過半工具呼叫次數。

coding agent最耗token的環節，往往不是寫程式，而是「找程式碼」。當目標是用自然語言描述的行為時，關鍵字比對常常落空，agent只能用猜測詞彙、整檔閱讀的方式拼湊上下文，每一次摸索都是額外的tool call、token與時間成本。Qwen Developer團隊開源的zg（zvec-grep），想把這段摸索過程直接省掉。

🤔 **背景：agent找程式碼為什麼慢**

已知symbol名稱時，ripgrep能精準命中；但當目標是一段行為描述而非確切字串，關鍵字搜尋往往找不到，agent只能反覆試錯。zg把語意搜尋、BM25與ripgrep收在同一個介面之下，供人類與agent共用。專案掛在zvec-ai這個GitHub組織下，採Apache 2.0授權。

🧩 **架構：一個介面，四種搜尋路徑**

zg對整個workspace建立一次索引後，提供多種查詢方式：預設的hybrid模式結合意圖理解與關鍵字錨點；`--fts`走BM25排序的精確詞比對；`--vector`做概念相似度比對，不做關鍵字排序；`--rg`則是窮舉式的literal／regex比對，完全不需要索引，這在repo還沒建索引時特別有用。索引存放於`<root>/.zvec-grep/`，`.git`與`.zvec-grep`永遠被排除，加上常見的依賴、build、cache、log目錄與repo自身的ignore規則。重新執行`zg index`是增量更新，但若要換embedding模型，必須明確加上`--rebuild`，因為不同模型的向量空間即使維度相同也彼此不相容。每筆索引結果都會標註新鮮度狀態`fresh`或`possibly_stale`，讓agent可以直接採用「夠好」的結果，不必先做一次額外的狀態檢查。

🧩 **給agent用：刻意收斂到兩個工具**

`zg install`會偵測機器上安裝的Codex、Claude Code、Cursor、OpenCode，並自動接上本地MCP整合。伺服器透過Streamable HTTP MCP運作，只在loopback位址`http://127.0.0.1:7999/mcp`提供服務，可選擇加上bearer認證。預設的agent工具集刻意只有兩個：`zvec_grep_search`用於已知意圖但不知道確切字串的情境，`zvec_grep_rg`用於已知symbol、路徑或regex的情境；索引的建立與刪除等生命週期管理則留在CLI層，不交給agent操作。另外還有一組六個工具的相容組合（含索引建立、刪除、狀態查詢、伺服器狀態），需要透過`zg server --mcp-toolset full`主動開啟，文件明訂agent不得在使用者不知情的情況下靜默建立、重建或刪除永久索引。輸出格式也是刻意精簡：結果依檔案分組並附上行號區間，預設不顯示索引來源預覽，也會擋掉會改變輸出格式的ripgrep參數（如`--json`、`--count`、`-l`、`--vimgrep`），確保回傳格式維持緊湊。

🧩 **模型選擇與資安考量**

內建目錄提供10個本地模型與3個Qwen遠端端點（文章指出，發布文提到11個本地模型，與目前文件的10個有出入）。預設模型`local/potion-code-16m-v2`是Model2Vec的static模型，256維輸出、8,192 token輸入上限，因為採用靜態向量查找，換GPU並不會加速。較重的本地選項包括`jina-embeddings-v2-base-code`、`embeddinggemma-300m`、`qwen3-embedding-0.6b`；遠端選項則有輸入上限128,000 token的`qwen/qwen3.7-text-embedding`，以及多模態的`qwen/qwen3-vl-embedding`。使用遠端模型需要額外授權：設定好provider憑證並不代表可以傳資料出去，必須用`--allow-remote`針對單一指令授權，或透過`zg auth grant`簽署整個workspace的授權，並可用`zg auth revoke`撤銷。

📊 **官方測試數據**

評測數字目前出現在發布文而非repo本身，repo的benchmarks章節仍是佔位文字。兩組測試都是A/B配對測試，固定agent、模型、prompt、runtime與任務，zg這組只多了預先建好的索引、MCP工具與使用引導，索引建置本身的成本不計入結果。20題SWE-QA-Bench抽樣顯示，工具呼叫次數減少超過一半，輸入token減少接近一半，Judge分數提升1.50分；80題BrowseComp-Plus抽樣顯示，準確率從98.67%升到99.00%，輸入token減少37.56%，工具呼叫減少43.52%，agent耗時減少38.58%。另外，替Django repo（3,457個檔案）建索引，在Apple M4 Pro上據稱能在30秒內完成。

⚠️ **限制**

20題與80題的樣本數都不算大，數據也來自廠商自己的測試，獨立複現會是下一步驗證的重點。

🎯 **實務啟示**

如果你正在打造coding agent或內部檢索工具鏈，zg的價值在於不用重新發明搜尋層：透過npm安裝、預設不需要GPU、Apache 2.0授權可商用。它把agent工具集刻意收斂到兩個MCP tool、索引生命週期留給人類CLI操作的設計，本身就值得在自家agent工具設計時參考。

🔗 **來源**
- 標題：Qwen Developers Open-Sources zg (zvec-grep): A Local-First Search Layer Unifying ripgrep, BM25, and Vector Search
- 作者／機構：Michal Sutter，MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/02/qwen-developers-open-sources-zg-zvec-grep-a-local-first-search-layer-unifying-ripgrep-bm25-and-vector-search/

#Qwen #OpenSource #CodingAgents #MCP #SemanticSearch #BM25 #ripgrep #DeveloperTools #VectorSearch #AIAgents
