---
title: 'Jet-Long: Efficient Long-Context Extension with Dynamic Bifocal RoPE'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.07740
score: 93
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T08:16:37.095415'
---

📌 Jet-Long：透過動態雙焦 RoPE 實現高效的長文本擴充套件

TL;DR：一種 zero-shot 方法，利用動態縮放因子與雙焦 attention 機制，讓 LLM 在不同序列長度下維持高效能。

當前的 LLM 在處理長文本時，往往面臨效能下降或需要昂貴的微調成本。如何在不經過額外訓練的情況下，讓模型在面對不同長度的輸入時都能保持精準的注意力，成為長文本處理的核心挑戰。

🤔 **解決長文本擴充套件的效能衰減**

Jet-Long 提出了一種名為「動態雙焦 RoPE (Dynamic Bifocal RoPE)」的新方法，旨在讓大型語言模型能以 zero-shot 的方式擴充套件上下文長度。其核心目標是在不重新訓練模型的前提下，讓模型能高效處理長序列，並在不同長度的輸入之間維持穩定的效能。

🧩 **動態縮放與雙焦 Attention 機制**

該方法主要透過以下兩個技術路徑實現：
- **動態調整縮放因子 (Dynamic Rescaling Factors)**：根據輸入的序列長度動態調整縮放引數，而非使用固定的縮放比例。
- **雙焦 Attention 機制 (Bifocal Attention Mechanism)**：利用雙焦設計來最佳化注意力分配，確保模型在處理不同長度序列時，都能維持高品質的表現。

🎯 **實務啟示**

對於需要處理長文本但缺乏微調資源的工程師來說，Jet-Long 提供的 zero-shot 擴充套件能力具有高度實作價值。這種動態調整的機制意味著模型能更靈活地適應不同長度的上下文，而不需要為每種長度預先設定不同的配置。

🔗 **來源**
- 標題：Jet-Long: Efficient Long-Context Extension with Dynamic Bifocal RoPE
- 連結：https://huggingface.co/papers/2607.07740

#LLM #LongContext #RoPE #Attention #ZeroShot #NLP #MachineLearning #Efficiency #JetLong #DeepLearning
