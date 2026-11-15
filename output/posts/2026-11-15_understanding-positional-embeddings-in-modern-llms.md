---
title: Understanding Positional Embeddings in Modern LLMs
source: Sebastian Raschka
url: https://magazine.sebastianraschka.com/p/understanding-positional-embeddings
model: claude-code/sonnet
generated_at: '2026-11-15T21:51:32.288219'
score: 82
---

📌 從GPT-2到RoPE：LLM怎麼「記住」token位置

TL;DR：Sebastian Raschka 系統梳理 LLM 位置編碼的演進，從學習式絕對位置到 RoPE，是理解現代 LLM 架構的必備基礎。

把「The red fox jumps over the gray fox.」和「The gray fox jumps over the red fox.」兩句話丟進一個完全沒有位置資訊的 self-attention 機制，模型會發現兩句話其實長得一模一樣。這就是 Raschka 這篇長文想解決的問題：LLM 到底是怎麼知道「誰在前、誰在後」的？

🤔 為什麼 attention 本身「看不見」順序

Raschka 從架構全貌切入：tokenizer 把輸入文字轉成 token ID，token embedding 層把每個 ID 映射成一個向量（也就是「特徵」），接著 transformer block 用 attention 與 feedforward 修改這些向量，最後輸出層產生下一個 token 的機率分佈。問題在於，若用一般、沒有因果遮罩（causal mask）的 self-attention，交換句子裡任意兩個字的位置，得到的 embedding 與 attention 分數完全不會變,因為同一個 token ID 永遠對應同一個 embedding 向量,與它出現在第幾個位置無關。

有趣的是，GPT 系列使用的因果遮罩（只能看自己與更早的 token）其實已經隱含了部分順序資訊,在前面「紅狐狸／灰狐狸」的例子中,"jumps" 在第一句只能看到 "red",在第二句只能看到 "gray",理論上已經能分辨兩句不同。但因果遮罩分辨不出「相隔 1 個位置」和「相隔 10 個位置」的差異,這也是為什麼 GPT-2 與多數新 LLM 仍然需要額外、明確的位置資訊。

🧩 GPT-2 的做法：學一張位置向量表,加一次就好

文章用 GPT-2 示範最直接（但不是最「省資源」）的做法,也就是學習式絕對位置編碼。整個流程可以拆成幾步：

1. Tokenizer 將輸入文字轉成 token ID。
2. Token embedding 層把每個 ID 映射成向量。
3. GPT-2 另外學一張「位置向量表」,依照 token 在序列中的位置 m,取出對應的位置向量 P_m。這張表的實作方式跟 token embedding 層完全一樣,輸出維度也相同,才能相加。
4. 把 token embedding 向量跟 P_m 逐元素相加,得到的 h_m 才是真正送進第一個 transformer block 的輸入。
5. 之後所有 transformer block 的 attention 與 feedforward 都在這個已經融合位置資訊的向量上運算。

與 GPT-2 相對的是文中提到的 MiniMax-M3（作為 2026 年多數新 LLM 的代表）,它不是在輸入階段把位置向量加一次就結束,而是用 RoPE,在「每一個」transformer block 的 attention 內部注入位置資訊。這是新舊架構在「何時、如何加入位置資訊」上的根本差異。摘要內容在深入 RoPE 具體運算之前就結束,因此本篇暫時只能點出這個宏觀差異,原文後段才會展開 RoPE 的數學推導,以及後面提到會討論的「NoPE」概念,也就是完全不加明確位置編碼,只靠因果遮罩提供的隱含順序資訊。

💡 這不是「過時的小細節」

Raschka 特別說明,他原本是在準備一篇關於 2026 年 LLM 架構趨勢的文章時,才發現自己從沒單獨寫過位置編碼這個主題,於是把它獨立成一篇基礎教材,方便之後的架構分析文章引用,也回應了許多讀者長期想要一篇 RoPE（相對位置編碼）教學的需求。

🎯 實務啟示

看懂「位置資訊是在輸入層加一次,還是在每層 attention 內動態注入」,是讀懂新架構差異的關鍵切入點。遇到像 MiniMax-M3 這類在 attention 內用 RoPE 處理位置的模型時,不能再用 GPT-2 式「embedding 加位置向量」的直覺去類推,這會直接影響你對模型長序列外推、位置泛化能力的判斷。

🔗 來源
- 標題：Understanding Positional Embeddings in Modern LLMs
- 作者／機構：Sebastian Raschka
- 連結：https://magazine.sebastianraschka.com/p/understanding-positional-embeddings

#LLM #PositionalEmbeddings #RoPE #TransformerArchitecture #DeepLearning #GPT2 #MiniMax #MachineLearning #AttentionMechanism #NeuralNetworks
