---
title: 'Alibaba Releases Qwen4-Max: 2.4T MoE, 71B Active, 1M Context'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/16/alibaba-qwen4-max-release/
model: claude-code/sonnet
generated_at: '2026-11-17T00:56:40.902635'
score: 104
---

📌 Qwen4-Max 登場:2.4T MoE、71B 啟用、百萬上下文

TL;DR：阿里釋出 Qwen4-Max,稀疏 MoE 加原生多模態,單任務成本平均降 62%。

當大家還在比參數量,阿里巴巴的 Qwen 團隊直接把價格砍了近三成,還宣稱單次任務的平均成本降了 62%——這代表的不只是模型變強,更是整個推理成本結構的重新計算。

🤔 **Qwen4 世代的第一個模型**

Qwen4-Max 是 Qwen4 世代的首個模型,屬於封閉原始碼的稀疏 MoE 模型,總參數規模達 2.4T,每個 token 實際啟用 71B 參數。它支援文字、圖像與影片輸入,並具備百萬 token 的上下文長度。目前僅對 Token Plan 用戶開放預覽。

🧩 **架構調整:注意力、殘差連接與嵌入層同步升級**

Qwen4 在稀疏 MoE 設計上做了三處升級:attention、殘差連接(residual connections)與嵌入層(embeddings)。阿里表示,在 2.4T 規模的預訓練過程中沒有出現 loss 突增的情況。在內部測試中,Qwen4-Max-Base 相較 Qwen3.8-Max-Base,bits per byte 低了 5% 到 13%,而且是在啟用參數少了 25% 的前提下達成的。

📊 **16 項 benchmark 對比:4 項第一,程式設計與視覺仍落後**

阿里公開的比較圖涵蓋 16 項 benchmark,對手包括 Qwen3.8-Max-0902、Claude Opus 5.5、GPT-6.1 Sol、GPT-6 Astra 與 Kimi K3.1。部分分數引用自第三方排行榜,在發布時並未經過獨立重現驗證。Qwen4-Max 在 16 項中拿下 4 項第一,Claude Opus 5.5 則領先 7 項;Qwen4-Max 落後最明顯的領域是程式設計與視覺。值得一提的是,阿里圖表上標示的「Kimi K3.1」分數,與 Moonshot 官方卡片公布的 Terminal-Bench 4.0 分數(Kimi K3.1 Pro 為 65.7、Opus 5.5 為 66.4)存在差異,提醒讀者對照 benchmark 數字時仍需留意資料來源。

在阿里自建的 Work360 綜合評測(涵蓋 26 個頂層領域與 721 個細分專業)上,Qwen4-Max 拿下 52.69 分,高於 Qwen3.8-Max 的 47.74 分。更關鍵的是 token 用量:在 Work360 上,Xhigh 思考檔位用量降低約 24%、High 檔位降低約 35%;在 Terminal-Bench 4.0 上,兩個檔位的降幅分別約為 48% 與 49%。這使得 Work360 的平均單任務成本從 4.43 美元降到 1.67 美元,降幅達 62%。

💡 **定價也同步下調**

API 牌價同步調整:輸入價格從每百萬 token 2 美元降到 1.5 美元,輸出從 6 美元降到 4.5 美元,隱式快取讀取(implicit cache reads)從 0.25 美元大降 70% 到 0.075 美元。模型 ID 為 qwen4-max,部署在 QwenCloud 上,API 相容 OpenAI 與 Anthropic 的客戶端格式,支援 function calling、結構化輸出、context caching、批次處理、網路搜尋與 fine-tuning,預設速率限制為每分鐘 500 萬 token,思考模式可透過 enable_thinking 開關,訂閱制則透過 Token Plan 存取。

🎯 **實務啟示**

對於已經在用 Qwen 系列做生產應用的團隊,token 用量的大幅下降加上快取讀取價格砍 70%,意味著重度使用 context caching 的工作流(例如長文件問答、重複性 agent 任務)換模型後的實際帳單降幅,很可能比單純看輸入輸出單價更可觀。不過面對阿里自家公布的跨模型 benchmark 排名,在落地前仍建議用自己的任務實際測試,而非只看官方對照表。

🔗 **來源**
- 標題：Alibaba Releases Qwen4-Max: 2.4T MoE, 71B Active, 1M Context
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/11/16/alibaba-qwen4-max-release/

#Qwen4Max #Alibaba #MoE #LLMPricing #SparseAttention #MultimodalAI #LongContext #AIInference #ChinaAI #LLMBenchmark
