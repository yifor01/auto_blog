---
title: Reverse-engineered Jev-like model
source: Hacker News
url: https://github.com/vinnylarouge/jevlike
model: claude-code/sonnet
generated_at: '2026-09-17T20:37:37.660189'
score: 83
---

📌 逆向工程 Jev:一次前向傳播,選出正確選項

TL;DR:開源複刻商用選項評分模型 Jev,單次前向傳播比逐字生成快約 100 倍。

多數 LLM 應用在做選擇題時,還是讓模型一個字一個字寫出答案,再解析成選項。TypeSafe 的商用模型 Jev 反其道而行:輸入一段文字與一份選項清單,直接為每個選項輸出一個機率,一次前向傳播就搞定。TypeSafe 沒有公開設計細節,Hacker News 上一個名為 jevlike 的專案,獨立做出了輸入輸出形狀相同的起始模型。

🤔 為什麼不用生成式方式做選擇題

Jev 這類模型要解決的問題是:給一段 context 文字,以及一份會不斷變動的選項清單,為每個選項算出一個機率,而不是像自迴歸解碼器那樣逐字生成答案。作者明確強調,jevlike 是獨立的研究起始模型,不是 Jev 的複製品,也沒有證明與 Jev 效能相當,或重現 TypeSafe 的私有訓練方法。

🧩 核心架構:query 向量、attention、共享點積、softmax

每個選項會先被轉成一個 query 向量(代表該選項文字的一組短數字)。這個 query 向量對 context tokens 做 attention,算出對應的權重,產生該選項專屬的 context 向量。接著用一個共享的點積運算,把「選項向量」與「context 向量」這對組合轉換成一個分數,最後所有選項的分數一起做 softmax,轉成總和為一的機率分布。

encoder(把文字轉成向量的部分)有兩種選擇:預設是從頭學習 byte embedding,成本低但對語意理解較弱;另一個選項是接上凍結的 Hugging Face 預訓練 encoder,只訓練小型的 scorer head,`--rank` 參數控制這個 head 的寬度。資料格式是每行一個 JSON,包含 context、options 清單(每行選項數可不同,最少兩個)與 zero-based 的 label 索引。

專案還展示了同一個 option-attention head 不只能處理文字,也能替影像 patch 打分:demo 影片串接了兩段五秒畫面,一段是用七個按鍵操作的 Doom 戰鬥畫面,一段是用五個按鍵下棋的畫面,兩個範例都是呼叫 `jevlike.vision` 這同一個視覺 scorer,沒有另外複製一份模型。

📊 準確率與速度數據

- 在合成選單資料上,單次前向傳播的 scorer 達到約 98% 準確率。
- 在 target-disjoint 的 Wikispeedia 下一步點擊資料上,搭配凍結的 Qwen2.5-0.5B encoder,準確率為 26%,而 shuffled 與 random-encoder 對照組僅約 8%;一個從頭訓練、只用 4 萬筆點擊資料的小模型則達到 29%。
- 在八個選項的情境下,單次前向傳播的速度比被迫寫出 400 個 token 的小型解碼器快約 100 倍。
- Demo 用的 Doom 聯合訓練 checkpoint,在 10 場紀錄中平均擊殺 0.60、reward -97.50;純棋類 checkpoint 在對隨機對手的 50 局中取得 4 勝 46 和 0 敗,但對戰 Stockfish level 0 時僅 0 勝 2 和 48 敗——作者特別說明這些片段是挑選出來展示活動性,不代表典型表現或棋力宣稱。

⚠️ 作者列出的明確限制

這是研究性質的起始模型,而非 Jev 的複製品;準確率高度依賴資料品質、切分品質與 encoder 選擇;預設的 byte encoder 雖然便宜,但對語言意義的掌握較弱;接上預訓練模型的路徑可能需要下載大型模型、佔用更多記憶體;單次評分需要在預測前就拿到完整的選項清單;速度比較用的是小型本地解碼器,而非大型商用模型。

🎯 實務啟示

如果你的應用場景是「從一份會變動的選項清單裡挑一個」,例如意圖路由、選單分類這類任務,jevlike 提供了一個比自迴歸生成快得多的推論路徑,程式碼採 MIT 授權。專案也提醒使用自有資料時,要把相關紀錄(例如同一位客戶或同一個目標頁面)切在同一個資料切分裡,避免近似重複樣本洩漏到測試集,這點在自建 held-out 測試集時值得留意。

🔗 來源
- 標題:Reverse-engineered Jev-like model
- 連結:https://github.com/vinnylarouge/jevlike

#ReverseEngineering #MachineLearning #Attention #OpenSource #TextClassification #NeuralNetworks #Softmax #ModelArchitecture #GitHub #AIResearch
