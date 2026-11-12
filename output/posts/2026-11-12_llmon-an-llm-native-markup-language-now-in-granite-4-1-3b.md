---
title: 'LLMON: An LLM-Native Markup Language, now in Granite 4.1 3B and 8B'
source: HuggingFace Blog
url: https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite
model: claude-code/sonnet
generated_at: '2026-11-12T22:56:07.871587'
score: 105
---

📌 IBM 推出 LLMON：讓 LLM「看懂」context 結構的標記語言

TL;DR：LLMON 用保留 token 分隔指令與資料，讓 prompt injection 攻擊近乎失效。

當你把一份不受信任的文件塞進 context，要求模型「照裡面的指示做」時，模型其實分不清那是文件內容還是給它的新指令，因為引號、冒號、大括號對它來說，跟文件裡出現的同一個符號是同一個 token。這正是多數 LLM 容易被 prompt injection 攻破的根本原因之一。

🤔 context 裡塞滿東西，但結構全靠模型自己猜

LLM 的 context 裡混雜著 system prompt、過去的對話輪次、作用在檢索文件上的指令、工具回應、使用者資料、輸出限制與推理鏈。這些結構多數時候是隱性的，或被編碼成像 JSON 這種「為 parser 設計、不是為 LLM 設計」的格式。IBM 團隊指出，模型的 tokenizer 並不受 JSON 語法約束，引號、冒號這類結構字元跟一般文字用的是同一套詞彙，括號的巢狀深度更要靠數 bracket 來推算，而 transformer 在長距離計數上本來就比較弱。結構不明確，除了讓小模型特別容易出錯，也給了攻擊者藏 prompt injection 的空間。

🧩 用保留 token 把指令和資料綁在一起

LLMON（LLM Object Notation，發音像「lemon」）是一種類 XML 的標記語言，但結構分隔符是保留的特殊 token，不是一般字元，因此結構和內容各自使用詞彙表中不同的部分。每個語意完整的區塊都用有意義的標籤包起來，並透過唯一 ID 互相指向，讓某條指令可以精確綁定到它該作用的資料上，概念上類似程式語言裡函式呼叫時傳入參數。

舉例來說，一個同時帶有 instruction、data、requirement 的使用者輪次，經過 LLMON 的 chat template 轉換後，會被拆成多個各自有 ID 的區塊，再由一個 exec 區塊宣告「執行這條指令，作用在這份資料上，受這些限制約束，結果寫進這個 assistant 區塊」。這比一般 chat template 把所有內容壓扁成一段文字、讓模型自己猜哪段是任務哪段是限制條件，多了一層明確的結構。

IBM 同時發布兩個實驗性的預覽模型：granite-4.1-3b-LLMON-preview 與 granite-4.1-8b-LLMON-preview，皆由 Granite 4.1 base model 訓練而來，並開源了對應的 GitHub 工具庫，內含 LLMON 的轉換工具與範例。既有的 JSON pipeline 可以用官方提供的轉換工具，無損轉成 LLMON 再轉回來。這套機制已經在 Mellea 中原生支援，呼叫 LLM 時會自動把訊息 LLMONize。

📊 對抗 prompt injection 的效果

團隊在 OPI 這個把惡意指令藏在經典 NLP 任務資料中的 benchmark 上做了測試，比較 LLMON 預覽模型與多個開源、閉源模型。結果顯示，非 LLMON 模型幾乎都以高機率被劫持，執行了藏在資料裡的指令，而 LLMON 幾乎讓這個問題歸零：相較測試中表現最好的前沿模型，LLMON 多擋下 47% 的攻擊，相較表現最好的開源模型則多擋下 95%。團隊表示在 ASB 與 StruQ 這兩個基準上也觀察到類似趨勢。

⚠️ 目前驗證的是靜態攻擊

IBM 團隊特別註明，這些 benchmark 測試的是模型對「靜態」indirect prompt injection 的防禦能力，目前公開的結果還沒有涵蓋更動態、會針對防禦機制調整的攻擊手法。

🎯 實務啟示

如果你的 agent pipeline 需要讀取不受信任的檢索文件或工具回應，與其繼續用 JSON 硬塞進 prompt 期待模型遵守格式，LLMON 提供了一個把指令與資料顯式切開的替代方案，尤其值得在資安敏感的 RAG 或 agent 應用中評估導入，或直接透過 Mellea 取得這層保護而不必重寫既有程式碼。

🔗 來源
- 標題：LLMON: An LLM-Native Markup Language, now in Granite 4.1 3B and 8B
- 作者／機構：IBM Granite 團隊（Abraham Daniels, Basel Shbita, Chad DeLuca, Dan Gutfreund, Michael Hind, Shub A）
- 連結：https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite

#LLMON #PromptInjection #IBMGranite #LLMSecurity #AIAgents #RAG #Tokenization #OpenSource #HuggingFace #AIInfrastructure
