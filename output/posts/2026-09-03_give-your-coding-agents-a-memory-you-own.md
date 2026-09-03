---
title: Give Your Coding Agents a Memory You Own
source: HuggingFace Blog
url: https://huggingface.co/blog/funes
model: claude-code/sonnet
generated_at: '2026-09-03T20:15:55.266119'
score: 98
---

📌 funes開源:讓Coding Agent擁有一份你自己保管的記憶

TL;DR:Hugging Face開源funes,把Claude Code、Codex等coding agent的session紀錄變成可檢索、可溯源的長期記憶,一行指令就能加進現有工作流。

換機器工作、依任務切換不同coding agent,是不少工程師的日常,但代價是每個新agent、每個新session都把你的專案當陌生人,「上週為什麼放棄streaming parser」這種推理過程,session一結束就消失了。

🤔 Agent trace是潛在記憶,但不是可用記憶

今年稍早已經有文章指出,coding agent在搜尋程式碼、嘗試方案、遇到錯誤、改變方向的過程中,其實留下了一份記錄不只「改了什麼」、還記錄「為什麼改」的詳細trace。問題是,這些session log終究只是archive,你沒辦法在一萬個turn裡grep出「為什麼那時候改了方向」。要讓agent在工作時真正用上這些trace,還需要索引、檢索、排序與精確的來源標註,這正是funes要補上的一塊。

🧩 一個binary,本機索引,可選擇性上雲

funes是單一binary,預設的inference後端不依賴任何ML runtime,embedding與reranking都在本機執行。底層有一條決定性pipeline:把每種支援的agent trace解析成統一的turn-and-block結構,分塊、用一個pin住版本的本機模型做embedding,寫入本機的Lance dataset。查詢時,funes結合vector搜尋與BM25搜尋,融合兩者的排序結果,再用cross-encoder重新排序候選,依照時間新近程度加權,並附帶鄰近的段落作為上下文。

這個設計帶來三個特性:第一,Claude Code、Codex、pi、Hermes四種agent都寫入同一種資料形狀,recall可以橫跨它們的歷史紀錄,並且每一筆結果都標明是哪個agent產生的;第二,原始證據不會在寫入時被摘要成一句「結論」,任何一筆結果都能追溯回產生它的那個turn;第三,recall預設是本機運作,不需要帳號或Hub repository,雲端模型不會處理你的session內容,embedding與reranking都在本機完成,真正的推理仍由你的coding agent負責。

如果想讓記憶跨機器、跨團隊,可以在加入agent時綁定一個Hugging Face dataset(預設private),例如`funes add codex acme/funes-memory`。之後funes會持續在本機索引每個turn,並在session邊界把記憶發布上去,別臺機器執行同樣的指令就能接上同一份記憶。在資料離開本機之前,credential已經在索引階段被redact,發布時還會再掃描一次並攔截疑似secret的內容。

🧩 怎麼用:一行指令加進agent,一句話直接問記憶

安裝方式是`curl -fsSL https://huggingface.co/buckets/huggingface/funes/resolve/install.sh | sh`,接著用`funes add claude`(或`codex`、`pi`、`hermes`)一次建立索引、賦予agent recall與get工具,並安裝自動化流程持續索引每個完成的turn,新資料是增量索引,不會重新embedding整段歷史。如果只是想單次提問而不想改動agent設定,可以用`funes ask claude "上次我們對streaming parser做了什麼決定"`,它會檢索段落、交給coding agent,回傳一個附帶來源出處的答案;如果檢索不到支持答案的段落,agent會直接說沒找到,而不是硬湊一個回答。

📊 長session的第三條路:recall vs compaction vs handoff

長時間的調查會讓session膨脹到「每個turn維護context的成本比實際做事還高」,常見的兩種解法是讓agent自動compaction、繼續往下做,或者手寫一份handoff重新開一個session。funes團隊用一個叫handoff-vs-recall的benchmark,拿兩個「答案必須依賴session先驗知識才能重建」的任務比較這三種方式:compaction是多數agent的預設做法,但在benchmark裡結果不穩定,兩個任務只答對一個,原因是摘要壓縮時把關鍵發現壓沒了。recall回傳的是原始段落而非摘要,因此發現不需要撐過一次摘要壓縮。

⚠️ 素材未提供的部分

文中沒有給出recall與handoff在該benchmark中的具體分數,只描述了compaction的失敗模式與相對表現;funes目前明確支援的agent是Claude Code、Codex、pi與Hermes,其他agent的相容性素材未提及。

🎯 實務啟示

如果你經常跨機器、跨agent接續同一個專案,或者團隊需要讓新成員快速接上過去幾個月的決策脈絡,funes提供的思路是把easily過時的CLAUDE.md,換成一份可持續累積、可搜尋、可溯源的實際session歷史,而不是一份需要有人手動維護的文件。

🔗 來源
- 標題:Give Your Coding Agents a Memory You Own
- 作者/機構:David Corvoysier(dacorvo) / Hugging Face
- 連結:https://huggingface.co/blog/funes

#CodingAgent #DeveloperTools #HuggingFace #LLM #RAG #AgentMemory #OpenSource #ClaudeCode #DevProductivity #SoftwareEngineering
