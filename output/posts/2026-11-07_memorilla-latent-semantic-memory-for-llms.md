---
title: 'Memorilla: Latent Semantic Memory for LLMs'
source: Hacker News
url: https://arxiv.org/abs/2610.21375
model: claude-code/sonnet
generated_at: '2026-11-07T20:59:25.398707'
score: 90
---

📌 16 個記憶 token，讓凍結 LLM 在 FactKG 上贏過全文輸入

TL;DR：Memorilla 用固定 16 個 query-dependent 記憶 token，打敗 Mem0 與 MemoRAG 多項基準。

把整段使用者對話歷史、整本書的章節，或是 agent 一路走來的所有行動記錄，硬塞進 LLM 的 context window，不只貴，還常常把模型越餵越笨。來自 Adibvafa Fallahpour、Jure Leskovec 等七位作者的新論文 Memorilla，提出了另一條路：不塞進 context，而是把整個文件集合濃縮成固定數量的「記憶 token」。

🤔 凍結模型的記憶困境：資訊要放進 context，但 context 很貴

論文指出，記憶機制讓 LLM 能用到參數之外的資訊，例如過去的使用者對話、長文件，或是 agent 先前的行動記錄。但對一個凍結的（frozen）LLM 來說，它能存取到多少累積知識，完全取決於記憶系統塞進 context window 裡的內容。現有系統的難題在於：既要從整個文件集合裡，針對每一次查詢蒐集並組合出相關資訊，又要讓模型的 context 保持精簡，這兩者本身就互相拉扯。

🧩 文件先編碼一次，查詢時只生成 16 個記憶 token

Memorilla 的作法，是先把文件集合（例如使用者的聊天記錄、書的章節）各自編碼一次，存成可重複使用的 embedding。之後面對每一次查詢，它會學習去檢索並把「與這次查詢相關」的資訊，放進 LLM 輸入的 embedding 空間裡，表現形式就是固定數量、query-dependent 的「記憶 token」。論文的實驗只用了 16 個記憶 token，就在多個基準測試上勝過 Mem0 與 MemoRAG 這類既有的記憶系統基準。

📊 FactKG 準確率贏過全文輸入，token 用量卻少 108 倍

Memorilla 在橫跨個人化、長文件問答、知識密集型問答的八個基準測試中，五個拿下最佳表現（對比的基準線包含 Mem0 與 MemoRAG）。在 FactKG 這個基準上，Memorilla 達到 84.33% 準確率，高於直接把全文塞進 context 的 80.43%，而代表原始文件所用的 token 數量，少了 108 倍。

論文也在 TextWorld 環境裡測試了 agent 場景：隨著 agent 走的步數增加，文件數量（也就是 agent 過去的行動記錄）也持續增加，這正好對應持續學習（continual learning）的情境。結果顯示，用 Memorilla 的 agent，比起把整段歷史都放進 context 做 in-context learning 的作法，更不容易在已經探索過的房間裡來回打轉，平均成功率也從 18.6% 提升到 24.2%。

⚠️ 八個基準裡還有三個沒拿到最佳

論文摘要明確寫的是「五個基準測試中表現最佳」，也就是說在另外三個基準上，Memorilla 並未勝過所有對比基準線。這點說明它的優勢並非全面壓倒性，而是在特定類型任務（例如需要精準檢索事實的場景）上效果更明顯。

🎯 實務啟示

對於要幫 agent 或聊天系統做長期記憶的工程師，Memorilla 示範的思路值得參考：不是把歷史對話全部塞進 prompt，也不是單純做傳統 RAG 式的文字檢索，而是把文件先編碼成可重複使用的向量，查詢時再學習生成一組固定長度的記憶 token 直接注入模型的輸入 embedding 空間。這種做法同時緩解了 context 長度與檢索品質的拉扯問題，尤其適合 agent 行動記錄持續累積、必須邊做邊學的場景。

🔗 來源
- 標題：Memorilla: Latent Semantic Memory for LLMs
- 作者／機構：Adibvafa Fallahpour, Parsa Idehpour, Vignesh Kothapalli, Nikita Mounier, Shirley Wu, Shayan Pardis, Jure Leskovec
- 連結：https://arxiv.org/abs/2610.21375

#LLM #Memory #Memorilla #RAG #ContinualLearning #AgenticAI #MachineLearning #NLP #ContextWindow #ArtificialIntelligence
