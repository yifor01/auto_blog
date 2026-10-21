---
title: How Specializing the Vocabulary of SLMs Can Cut Inference Cost by 77% in Real
  Applications
source: HuggingFace Blog
url: https://huggingface.co/blog/Dharma-AI/vocabx-vocabulary-specialization
model: claude-code/sonnet
generated_at: '2026-10-21T20:53:55.518540'
score: 103
---

📌 Dharma-AI 的 VocabX：重新設計詞表，讓小模型推理成本降 77%

TL;DR：依「每個 token 在哪個欄位生成」而非出現頻率重建詞表，實測讓生產環境推理成本降低 77%。

Tokenizer（分詞器）通常被當成 base model 的固定屬性，繼承下來就不再碰。但對一個只服務單一領域的模型來說，它可能是尚未被動過、卻是最大的成本槓桿之一，而且這個選擇在訓練開始之前就已經定型。

🤔 **為通用場景打造的詞表，在單一領域裡變成雙重浪費**

Dharma-AI 在生產環境中運行一套以 Qwen3-4B 微調的葡萄牙語作文評分系統：輸入作文題目、作文本體與參考文本，輸出包含分數與各項能力評語的 JSON 評估結果。這個模型雖然只有 40 億參數、也已針對任務微調過，但它的 tokenizer 仍是 Qwen3-4B 原生版本,為多語言、多領域文本設計。這造成兩種浪費同時存在：第一是「碎片化」,評分器每次回應都重複相同的 JSON 格式、相同的能力名稱、相同的評語用語,這些在領域裡最常重複出現的內容,卻被切成好幾個 token,模型在每一次請求都要為此多付出代價;第二是「過剩」,詞表裡有數萬個這個任務幾乎用不到的詞條（例如中文 token），但模型在每一個生成步驟都要為詞表裡的每一個條目計算一次分數，不管用不用得到。

🧩 **為什麼「寫」比「讀」貴：decode 階段的記憶體頻寬瓶頸**

推理分為兩個階段。Prefill 階段，模型把整段輸入一次性送入網路,每個從 GPU 記憶體讀出的權重會被所有輸入 token 共用,此時的瓶頸是運算量。Decode 階段則是逐個 token 生成回應,每生成一個 token 就要完整跑一次網路,每次讀出的權重只被少數幾個 token 用到，GPU 多數時間在等資料從記憶體送達，瓶頸變成了記憶體頻寬。這個效應在小模型、中等批次規模的場景下最明顯，批次處理能分攤權重讀取的成本，但沒辦法根本解決問題。每個 decode 步驟還要讀取持續增長的 KV cache。在評分器這個案例中,團隊實測一個生成 token 的成本是一個讀取 token 的 7.4 倍,這個比例會隨硬體、批次大小、上下文長度等因素變化，但方向是一致的：生成永遠比讀取貴。

模型最後一層的 LM head 也是成本的一部分：它要把內部狀態轉成每一個可能 token 的分數,因此每個詞表條目都對應一列參數。在 Qwen3-4B 這個規模的模型裡，LM head 矩陣就佔了將近 10% 的參數量，這個比例對大模型來說無傷大雅，但對小模型是沉重負擔。輸入層只需查詢被讀入的那個 token 對應的那一列，但 LM head 在每一次生成時都要讀取並乘上整個矩陣,在本已受限於記憶體頻寬的 decode 階段，每多一列詞條都是額外要搬動的資料,一個幾乎用不到的詞條，成本和一個高頻詞條完全一樣。這也是為什麼「增加 token 數量」有時反而會「拉高帳單」。

🧩 **現有方法的兩個侷限：只看頻率，只動一層**

文獻中已有一些詞表調整方法，如 fast vocabulary transfer（FVT）、multi-word tokenization（MWT）與 Liquid AI 的 in-place BPE（從原始詞表繼續訓練 BPE），它們都能降低碎片化。但 Dharma-AI 測試後發現兩個共同限制：這些方法依「出現頻率」挑選 token，而不是依「成本」,一個在輸入裡出現頻繁的詞,即便它在回應端生成的成本更低，仍會被優先保留;而且它們都只動一層，不是調整分詞方式、就是把片語合併成單一 token，沒有一種方法同時處理兩個層次。評分器裡最大的浪費恰好出在像 JSON 格式這種長、重複的片段，單純的 sub-word 方法只能一塊一塊慢慢合併，效率有限。

🧩 **VocabX 的做法：用成本取代頻率，同時動兩層**

VocabX 把問題換了一個問法：不問一個候選 token 能省下多少次出現，而是問它能省下多少成本與時間。具體做法是把每一個被消除的 token，乘上它所在欄位的「價格」:系統提示詞、使用者訊息，或是模型回應。在評分器案例中,回應端省下一個 token 的價值,是輸入端省下一個 token 的 7.4 倍，詞表的建構就依此權重進行。同時，VocabX 在兩個層次上同步運作：透過 sub-word 合併，用更小、領域專屬的詞表取代原始詞表;再用 macro（巨集）在固定預算內，把整段重複片語直接合併成單一 token。在評分器案例中，輸出層詞表從約 15.2 萬條縮減到約 6.5 萬條。

📊 **同一個 base model、同一份資料、同一套訓練流程，推理成本降 77%**

團隊在不更換 base model（Qwen3-4B）、不更換資料、不更換訓練流程的前提下，單純用 VocabX 重建詞表，實測讓生產環境評分系統的推理成本降低 77%。

⚠️ 文中數字來自 VocabX 論文目前仍在審稿中的版本,正式發表前可能會有調整；7.4 倍的生成/讀取成本比例，也會隨硬體、批次大小、上下文長度等條件變化，並非固定常數。

🎯 **實務啟示**

如果你的團隊把通用 base model 微調成單一領域、單一語言的服務，tokenizer 很可能不該被視為「繼承來就不動」的固定屬性。評估詞表時，不要只看「省了多少 token」，更要看「省在哪個欄位」,decode 端省下的 token 遠比 prefill 端值錢，而 LM head 的大小本身也是一筆持續在付的記憶體頻寬帳單。

🔗 **來源**
- 標題：How Specializing the Vocabulary of SLMs Can Cut Inference Cost by 77% in Real Applications
- 作者／機構：Bernardo França de Aguiar、Gabriel Pimenta de Freitas Cardoso、Bruno Duarte、Francisco de Almeida Rocha Alves（Dharma-AI），HuggingFace Blog
- 連結：https://huggingface.co/blog/Dharma-AI/vocabx-vocabulary-specialization

#LLM #Tokenization #InferenceOptimization #SLM #CostOptimization #Qwen #HuggingFace #MachineLearning #NLP #EdgeAI
