---
title: "Tokenization with Split Trees"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.22705
score: 116
model: tencent/hy3-preview:free
generated_at: 2026-05-22T20:28:22.498618
---

📌 【Kensho+MIT】分詞樹優化：詞元減11%
你以為 BPE 已經是詞元壓縮的極限？
在相同 40,960 詞彙規模下，ToaST 讓詞元數量比 BPE、WordPiece、UnigramLM 少超過 11%。
這意味著模型在同等運算預算下能看到更長的文字。

🤔 **現有詞元方法未直接最佳化壓縮**
傳統 subword 演算法（BPE、WordPiece、UnigramLM）是先建立詞彙表，再根據詞彙表切分文字。這兩個步驟是分開進行的，詞彙表的選擇並未直接考慮最終的 token 數量或推論效率。

🧪 **以 byte n-gram 先建全二元樹再透過 IP 選詞彙**
ToaST 首先對每個預先切分的字串（pretoken）使用預計算的 byte n-gram 計數，貪婪地將其切分成一棵完整的二元樹，這一步與詞彙表無關。給定一個詞彙表後，推論會遞迴下降這棵樹，每條路徑上第一個在詞彙表中的節點會被輸出為 token。詞彙表的選擇則被形式化為一個整數規劃問題（IP），目標是在此推論程序下使所有 split tree 的總 token 數最小。該 IP 的線性規劃鬆弛在實務上近似整數，因而能得到可證明的近似最佳詞彙表，且訓練時間隨 split tree 數量的平方增長。

 **詞元減少 11%+，Renyi 效率提升，CORE 分數最高**
在英文語料上，使用 40,960 或更大的詞彙表時，ToaST 的 token 數比 BPE、WordPiece、UnigramLM 少超過 11%。這直接減少了模型推論所需的 token 數，從而延長了有效上下文長度。此外，ToaST 較少使用常見的單位元組（single-byte tokens），這帶來了顯著的 Renyi 效率提升。在訓練 1.5B 參數語言模型的實驗中，ToaST 獲得最高的 CORE 分數，比基線高出 2.6%~7.6%（其中兩項達顯著水準），並在 22 個獨任務中有 13 項表現最佳。

💡 **詞樹結構讓推論更貼近詞彙邊界，減少單位元濫用**
因為每個 pretoken 先被切成完整的二元樹，推論時會沿著樹尋找最近的詞彙節點，這使得切分點更可能落在真實的詞彙邊界上，而不是被迫切入高頻單位元。因此，單位元 token 的使用頻率下降，進一步提升了編碼效率。

⚠️ **實驗僅限英文、詞彙規模≥40k，訓練時間平方增長**
目前的結果僅在英文文字上驗證，且詞彙表大小需達到 40,960 以上才能觀察到顯著改善。此外，ToaST 的訓練時間會隨 split tree 數量的平方增長，在非常大的語料上可能需要更多計算資源。

🎯 **工程師可直接換用 ToaST 獲得更長有效上下文與更佳模型表現**
如果你正在使用 BPE 或 WordPiece 進行語言模型訓練，切換到 ToaST 只需替換 tokenizer，即可在不增大模型或計算預算的情況下獲得更少的 token 數、更長的有效上下文以及更好的 Renyi 效率。在 1.5B 規模的實驗中，這轉化為 CORE 分數的明顯提升。

🔗 **論文連結**
📝 Tokenization with Split Trees (ToaST)
👤 Craig W. Schmidt, Michael Krumdick, Adam Wiemerslage, Seth Ebner, Varshini Reddy (Kensho Technologies; Ben-Gurion University; MIT)
🔗 https://arxiv.org/abs/2605.22705

你有試過在訓練中更換 tokenizer 來提升效能嗎？歡迎在留言區分享經驗 👇

#AI #NLP #Tokenization #Kensho #MIT #LanguageModel #MachineLearning
