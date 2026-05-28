---
title: "Perplexity AI Open-Sources Unigram Tokenizer That Achieves 5x Lower p50 Latency Than Hugging Face tokenizers Crate"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/28/perplexity-ai-open-sources-unigram-tokenizer-that-achieves-5x-lower-p50-latency-than-hugging-face-tokenizers-crate/
score: 98
model: tencent/hy3-preview:free
generated_at: 2026-05-28T21:17:48.533134
---

📌 **Perplexity 開源 Unigram 分詞器 提速 5 倍**

你以為 LLM 的瓶頸都在 GPU 算力？其實在大批次請求中，CPU 端的 tokenization 也會吃掉不少延遲。

🤔 **CPU 端 tokenization 成為推論瓶頸**  
Perplexity 指出，即使模型很小（如嵌入、重排序器），每筆請求仍必須先經過 CPU 端的分詞。當 batch size 大時，這個步驟會佔據總延遲的顯著比例，成為提升整體吞吐量的關鍵點。

🧪 **從零重寫 Rust 版 Unigram tokenizer**  
研究團隊在 pplx-garden 儲存庫中，用 Rust 從頭實作 Unigram 演算法。該實作在產線輸入長度下，使 p50 延遲比 Hugging Face tokenizers crate 低約 5 倍、比 SentencePiece（C++）低約 2 倍、比 IREE 的 tokenizer（C）低約 1.5 倍，且在穩定狀態下不產生任何 heap 配置。

🔥 **實際效益：CPU 使用率下降 5‑6×、重排序延遲縮減雙位數毫秒**  
在 Perplexity 的推論堆疊中，這個 tokenizer 讓 CPU 佔用率減少 5‑6 倍，並為重排序器節省了十毫秒以上的延遲。這些改善對於嵌入模型、分類器以及重排序器等小型模型尤為顯著，因為它們的 GPU 計算往往只需個位數毫秒，而 tokenization 卻可能成為主導因素。

💡 **演算法本質未變，實現帶來工程價值**  
Unigram 分詞本身並非新創意：它由 Kudo 在 2018 年提出，透過 SentencePiece 實作，將分詞視為最可能路徑問題，使用 Viterbi 動態規劃尋找最高分數的字元切割路徑。Perplexity 的貢獻在於以 Rust 實現零分配的版本，提供可直接插入的高效能替代方案。

⚠️ **限制：僅報告延遲與 CPU 效益，未涉及精度影響**  
文章著重於效能提升，未詳細探討 tokenization 精度是否與原始 SentencePiece 完全等價，亦未說明在極端較長序列或特殊語系上的表現。

🎯 **對基礎設施工程師的啟示**  
- 在 CPU 受限的推論管線中，優化 tokenization 可帶來可觀的延遲與成本下降。  
- 零分配的 Rust 實作適合高併發、低延遲的服務。  
- 若使用 XLM‑RoBERTa 或其他基於 SentencePiece 的 250k‑token Unigram 模型，可直接考慮採用此開源 tokenizer。

🔗 **論文連結**  
📝 Perplexity AI Open‑Sources Unigram Tokenizer That Achieves 5x Lower p50 Latency Than Hugging Face tokenizers Crate  
👤 Asif Razzaq (MarkTechPost)  
🔗 https://www.marktechpost.com/2026/05/28/perplexity-ai-open-sources-unigram-tokenizer-that-achieves-5x-lower-p50-latency-than-hugging-face-tokenizers-crate/  
💻 開源倉儲：pplx-garden（Perplexity AI 的推論技術儲存庫）

你在生產環境中是否也遇到過 tokenization 成為瓶頸？歡迎在留言區分享你的經驗與優化技巧 👇

#Perplexity #Unigram #Tokenizer #Rust #LLM #AI基礎設施 #MarkTechPost #開源 #推論優化
