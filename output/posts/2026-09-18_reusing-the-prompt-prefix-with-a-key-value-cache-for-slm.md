---
title: Reusing the Prompt Prefix with a Key-Value Cache for SLM Optimization
source: KDnuggets
url: https://www.kdnuggets.com/reusing-the-prompt-prefix-with-a-key-value-cache-for-slm-optimization
model: claude-code/sonnet
generated_at: '2026-09-18T19:54:21.210965'
score: 87
---

📌 87%的prompt都是重複的，為何還要每次重新計算？

TL;DR：用 KV cache 重複利用靜態 prompt 前綴，可省去 SLM 分類任務中重複的 pre-fill 運算。

如果你的 prompt 裡有 87% 的 token 每次呼叫都長得一模一樣，那這些運算其實不該被重做一遍。這正是 KDnuggets「SLM 最佳化技巧系列」第二篇文章要解決的問題。

🤔 **窄領域自動化的 prompt，其實大多是靜態的**

作者 Matthew Mayo 延續前一篇「限制輸出空間」的系列，這次聚焦在客服工單分類的場景：一段任務指令、分類定義與幾個範例構成 prompt 的大部分內容，每筆工單只新增二、三十個 token。若指令區塊有數百 token，而每筆資料只帶來少量變動，那麼絕大多數的 prompt 其實是逐位元組相同的重複內容，逐次重新編碼並不划算。

🧩 **原理：固定前綴的 key／value 向量不會變**

Transformer 在每一層都會為每個 token 計算 key 與 value 向量，而這些向量只取決於左側（即之前）的 token。這意味著，只要前綴固定，這些 key／value 向量在每次呼叫時都完全相同。只要事先計算一次並保留下來，之後每筆資料的 pre-fill 就只需處理真正變動的那一小段 token。

文章以 Qwen2.5-0.5B-Instruct（float16，透過 Hugging Face Transformers，在配備 24GB RAM、16 核心 Neural Engine 的 M2 MacBook Air 上）作為實測環境，延續前一篇文章的「限制式評分」技巧：由於 prompt 在 assistant turn 開頭就結束，只要各分類標籤的第一個 token 彼此不同，比較各標籤第一個 token 的 logits 即可決定分類結果，因此只需一次前向傳播。

📊 **基準測試：87%的prompt是靜態前綴**

作者手寫 ChatML 格式的 prompt（而非透過 `apply_chat_template()`），以便在已知的 token 邊界處切分前綴與後綴，並用 assertion 驗證切分後編碼結果與整段編碼完全一致，確保切分是「token-clean」的。測試資料為 600 筆工單（三種範例文字各重複 200 次），系統前綴長度為 145 tokens，完整 prompt 長度為 167 tokens，代表整個 prompt 有 87% 是靜態內容。在「每次都重新編碼完整 prompt」的基準做法下，600 筆工單總耗時 184.85 秒，平均每筆 308.1 毫秒。

💡 **導入 DynamicCache：只算一次前綴，重複使用**

接下來的程式碼引入 Hugging Face Transformers 的 `DynamicCache`，將前綴只跑過模型一次、保留下產生的 cache，之後每筆資料只需餵入自己專屬的 token 片段，沿用同一個 model、tokenizer 與 prompt 切分邏輯。這個做法直接對應前面觀察到的問題：87% 的運算原本是重複的，透過快取前綴的 key／value，理論上可以把這部分的計算成本從每筆請求中拿掉，只保留變動的十幾、二十個 token 需要即時編碼。

⚠️ **留意 token 邊界的正確性**

值得注意的是，這個技巧的前提是「前綴／後綴切分必須是 token-clean」——也就是分開編碼前綴與後綴，結果必須與整段一起編碼完全一致，否則快取下來的 key／value 會與模型原本會看到的內容對不上，文章中特別用 assertion 檢查了這一點，這是實作時容易忽略但很關鍵的細節。

🎯 **實務啟示**

如果你的應用場景是窄領域、高重複度的 prompt（例如分類、標籤、路由任務），且前綴佔比高，這類 KV cache 前綴重用的技巧值得優先評估——尤其搭配前一篇文章「限制輸出空間」的單次前向傳播評分法，兩者疊加後理論上能同時省下 decode 與 pre-fill 兩端的運算量。實作時務必先驗證前綴／後綴切分的 token 一致性，避免快取出來的結果與實際 prompt 不符。

🔗 **來源**
- 標題：Reusing the Prompt Prefix with a Key-Value Cache for SLM Optimization
- 作者／機構：Matthew Mayo（KDnuggets）
- 連結：https://www.kdnuggets.com/reusing-the-prompt-prefix-with-a-key-value-cache-for-slm-optimization

#SLM #KVCache #LLMOptimization #Transformers #HuggingFace #Qwen #Inference #MachineLearning #PromptEngineering #ModelServing
