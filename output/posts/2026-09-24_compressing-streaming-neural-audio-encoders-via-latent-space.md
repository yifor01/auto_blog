---
title: Compressing Streaming Neural Audio Encoders via Latent-Space Distillation
source: Apple ML
url: https://machinelearning.apple.com/research/latent-space-distillation
model: claude-code/sonnet
generated_at: '2026-09-24T20:44:52.846834'
score: 88
---

📌 【Apple ML】端側語音壓縮 2.8 倍，WER 幾乎不掉

TL;DR：Apple 用「潛空間蒸餾」壓縮端側語音 tokenizer，2.8 倍壓縮下 WER 僅落後教師模型 1.9%。

Apple 裝置上的系統級聽寫（System-wide Dictation）完全在裝置端運行，語音要先經過一個 tokenizer——把短時間窗的波形映射成語言模型能讀懂的表示——才能進入基礎模型。這篇論文要解決的問題很直接：這個常駐的 tokenizer 該怎麼變小，又不明顯犧牲辨識準確率。

🤔 為什麼 tokenizer 的大小是個真問題

論文指出一個關鍵背景：Apple 的基礎模型採用稀疏啟動架構，並透過「Instruction-Following Pruning」機制，讓任何時刻只有一小部分 expert 被載入 DRAM。在這個前提下，始終在線的語音 tokenizer 必須和這些 expert 搶佔同一塊記憶體，它的參數量因此直接牽動裝置的功耗與延遲。換句話說，tokenizer 不是可以隨便放大的元件，它的每一個參數都在跟語言模型爭記憶體空間。

🧩 蒸餾目標：不學 token，不學輸出分布，學「量化前的潛在表示」

這篇論文的方法設計有一個明確的選擇：蒸餾的監督訊號既不是離散 token，也不是輸出機率分布，而是 pre-quantizer latent——也就是量化器（quantizer）處理之前、兩種 token 介面共享的最後一層表示。具體做法是：只訓練學生（student）encoder，讓它在平方誤差（squared-error）目標下去回歸教師（teacher）模型逐幀（per-frame）的這個潛在表示，並用一層仿射變換（affine layer）吸收教師與學生模型寬度不一致的問題。

因為監督目標發生在量化器與語言模型銜接層「之前」，同一套蒸餾配方可以同時覆蓋團隊支援的兩種 token 介面，並且分別套用在兩種情境上：單獨預訓練的 tokenizer，以及與語言模型聯合訓練的 tokenizer。

📊 2.8 倍壓縮，WER 只掉 1.9%

論文的核心結果：在 2.8 倍壓縮率下，蒸餾後的學生模型在六組教師—學生配對中的五組上，相對 WER（word error rate）僅比教師模型高出 1.9%，而且完全不需要額外微調。相較於一個獨立訓練、參數量相同的 tokenizer，蒸餾後的學生模型相對還能再改善 3.9%。

💡 一個值得注意的細節

論文作者名單中，Yongqiang Wang 標註目前任職於 NVIDIA、Yuan Liu 標註目前任職於 Anthropic，兩人都註明「這項工作是在 Apple 任職期間完成」，反映出這類端側語音基礎模型研究在業界人才流動下的延續性。

🎯 實務啟示

對於需要在裝置端常駐運行語音前端模型的團隊，這篇論文提供了一個具體可行的蒸餾配方：與其讓學生模型去模仿最終的離散 token 或輸出分布，不如直接瞄準「量化前」的連續潛在表示，用簡單的 MSE 加一層仿射對齊，就能在大幅壓縮參數量的同時把準確率損失壓到很小的範圍，而且這個配方對「獨立 tokenizer」與「聯合訓練 tokenizer」都適用，不需要為不同場景重新設計蒸餾目標。

🔗 來源
- 標題：Compressing Streaming Neural Audio Encoders via Latent-Space Distillation
- 作者／機構：Prasanth Yadla、Mohammad Samragh Razlighi 等，Apple（部分作者現任職 NVIDIA、Anthropic）
- 連結：https://machinelearning.apple.com/research/latent-space-distillation

#AppleML #SpeechRecognition #KnowledgeDistillation #OnDeviceAI #ModelCompression #ASR #EdgeAI #NeuralAudio #WER #MachineLearning
