---
title: Batching by Length Instead of Looping Item by Item for SLM Optimization
source: KDnuggets
url: https://www.kdnuggets.com/batching-by-length-instead-of-looping-item-by-item-for-slm-optimization
model: claude-code/sonnet
generated_at: '2026-09-25T20:54:44.603335'
score: 81
---

📌 別再逐筆跑 SLM 推論:依長度分批能省下多少浪費的運算?

TL;DR:KDnuggets 系列文章實測顯示,小模型逐筆推論在 CPU 上嚴重浪費記憶體頻寬,而 padding 到全域最長長度更會白算好幾倍 token。

同一顆 0.5B 模型跑 600 張長短不一的工單分類,如果每一批都把所有句子補齊到資料集裡最長的 449 tokens,光是 padding 就會讓你多算 3.7 倍不必要的 token——這是這個 SLM 最佳化系列第三篇、也是最後一篇要處理的問題。

🤔 **逐筆推論為何是整條管線裡最大的浪費**

前兩篇文章分別談了限制輸出空間、以及用 key-value cache 重用 prompt 前綴,這篇則聚焦「依長度分批」而非逐筆跑迴圈。文章指出,在 batch size 為 1 的情況下,小模型是受記憶體頻寬限制而非算力限制:硬體必須把全部權重從記憶體讀出來只為服務一個序列,接著馬上重來一次服務下一個,運算單元大部分時間都在閒置。這件事在 GPU 上成立,在 CPU 上更明顯——而 0.5B 這種規模的模型,實務上最常就是跑在 CPU 上。批次處理能把「讀一次權重」的成本攤提到多筆序列上,但最直接的實作方式又會引入新的浪費:同一批裡的序列必須補齊(padding)到相同長度。真實世界的文字長度分布通常有長尾,如果資料集裡最長的項目有幾百個 token、中位數卻遠低於一百,把每個批次都補到全域最大值,代表大部分算力都花在 padding 上。

🧩 **解法:先依 token 長度排序,再分批**

文章延續系列第一篇的支援單分類情境(用 Qwen2.5-0.5B-Instruct,透過 Hugging Face Transformers 在配備 16 核心 Neural Engine、24GB RAM 的 M2 MacBook Air 上執行),並沿用第一篇的「限制式評分」做法,讓每筆項目只需一次前向傳播即可完成分類。基準版本(逐筆迴圈)的做法很直接:每次只把一個 prompt 丟進 tokenizer,取最後一個位置的 logits,在三個標籤(billing、technical、account)對應的第一個 token 之間比較大小。文章刻意模擬了一個長尾分布的工單長度,搭配固定的填充句(filler)延伸文字,讓長度變化但分類訊號仍保留在句首。

針對批次化版本,文章的做法是把同一批資料跑兩次:一次維持任意順序,用來獨立衡量「單純分批」帶來的效益;另一次先依 token 長度排序再分批,藉此看出排序本身額外帶來的效益。兩次執行都會追蹤處理的 token 預算裡有多少比例是 padding,而排序的核心邏輯很單純:把長度相近的項目分到同一批,讓每一批只需要補齊到「自己這批」的最大長度,而不是整個資料集的最大長度。

📊 **基準數字:144 秒、4.2 筆/秒,padding 白算 3.7 倍**

以 600 筆模擬工單為例,prompt 長度最短 48 tokens、中位數 94 tokens、最長 449 tokens;如果每批都補齊到全域最大值,將處理 3.7 倍於實際所需的 token 量。逐筆推論的基準結果是 144.35 秒處理完 600 筆,平均每筆約 0.23–0.24 秒,換算約 4.2 筆/秒。文章釋出的內容目前尚未附上依長度排序分批後的具體秒數與加速倍率,因此本文僅呈現已公開的基準數據與 padding 浪費比例,不臆測分批後的實際效能提升。

⚠️ **本文未附完整分批結果**

素材中分批版本的程式碼已展示,但對應的實測輸出(耗時、items/sec、padding 比例)尚未在提供的內容中出現,因此無法據此估算依長度排序分批到底能帶來多少倍加速,只能確認 padding 浪費的量化依據(3.7 倍)與逐筆基準的成本。

🎯 **實務啟示**

如果你的應用場景是離線或近即時的批次分類、標記等窄域自動化任務,且輸入長度分布本身有長尾,先量測「padding 到全域最大值會浪費多少 token」是判斷是否值得改用依長度排序分批的第一步;搭配系列前兩篇提到的限制輸出空間與 KV cache 前綴重用,三者疊加起來才是把 SLM 部署成本壓低的完整思路。

🔗 **來源**
- 標題:Batching by Length Instead of Looping Item by Item for SLM Optimization
- 作者/機構:Matthew Mayo,KDnuggets
- 連結:https://www.kdnuggets.com/batching-by-length-instead-of-looping-item-by-item-for-slm-optimization

#SLM #LLMInference #Batching #HuggingFace #Transformers #EdgeAI #ModelOptimization #Qwen #PythonML #InferenceOptimization
