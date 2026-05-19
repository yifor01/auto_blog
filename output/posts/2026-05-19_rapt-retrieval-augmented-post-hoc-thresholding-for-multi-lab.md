---
title: "RAPT: Retrieval-Augmented Post-hoc Thresholding for Multi-Label Classification"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.16535
score: 104
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:56:03.132904
---

📌 **RAPT：檢索增強的後處理閾值**  

🎣 在工業文件理解管線中，全局閾值常因 OCR 噪聲與標籤不平衡而失效。RAPT 提出一種無需重訓的檢索增強方法，讓每份文件都能自動找到最適閾值。  

🤔 **多標籤分類的閾值問題難以靜態解決**  
工業多標籤文件理解流程會先對候選標籤評分，再透過全局或逐標籤的靜態閾值產生最終標籤集。這一步驟直接影響後續資訊抽取的正確度與後驗工作量。然而，OCR 噪聲、標籤不平衡、實例依賴的標籤基數以及非對稱錯誤成本，讓單一全局閾值在文件格式演變過程中變得脆弱且難以維護。  

🧪 **模型不可知的檢索增強後處理包裝器**  
RAPT 被設計為一個模型不可知的包裝器：任何能提供文件向量（用於相似度搜尋）與每標籤信心分數的預測器都可以作為基礎，包括度量學習編碼器與微調的 Transformer 分類器。對於每個查詢文件，RAPT 先取得基礎分類器的分數向量，然後從歷史文件中檢索出相似的「閾值情境」（cases），根據這些鄰居的實際結果（例如鄰居平均標籤數、閾值校正）來局部調整查詢文件的選擇閾值，最終透過鄰居解決方案的聚合（如平均標籤數或校正閾值）產出標籤集。  

🔑 **在工業資料與六個公開基準上，RAPT 持續優於靜態閾值與少樣本 LLM**  
實驗將度量學習編碼器與微調的 Transformer 分別與 RAPT 組合，與全局閾值、逐標籤閾值以及 K=5 的少樣本 LLM 基線進行比較。結果顯示，RAPT 在所有資料集上都優於靜態閾值基線。在工業資料集中，搭配度量學習編碼器時，RAPT 達到最高的 0.87 Macro‑F1；而微調 Transformer 版本平均獲得 0.775 Macro‑F1，這比少樣本 LLM 基線高出約 2 個。此外，RAPT 的推論時間至少減少 115 倍，GPU 記憶體使用量減少 13.5 倍。  

💡 **局部適配的關鍵在於利用相似文件的歷史決策**  
RAPT 的優勢來自於它不試圖學習一個全局的最適閾值，而是透過檢索過去已知的「閾值情境」來捕捉文件特有的標籤分佈與噪聲特徵。這種基於案例的後處理方式讓模型能在不改變底層權重的情況下，依據每份文件的局上下文做出更精細的標籤選擇，從而在標籤不平衡與實例依賴的場景中獲得更穩定的 Macro‑F1 提升。  

⚠️ **僅針對後處理階段進行評估，底層模型的品質仍是上限**  
實驗聚焦於將 RAPT 加在已訓練好的分類器上，未探討若基礎模型本身表現較差時，RAPT 能帶來多少絕對提升。此外，雖然報告了在六個公開基準與一個工業資料集上的表現，但未具體說明每個基準的名稱或資料大小，這限制了對結果在不同領域的直接推廣。  

🎯 **工業管線可直接採用，無需重訓即可獲得分數提升**  
- 若現有系統已經產出文件向量與標籤分數（例如透過度量學習或 Transformer），只需將 RAPT 作為後處理層插入，即可獲得顯著的 Macro‑F1 改善。  
- 由於不需要重新訓練底層模型，更新成本低，特別適合文件格式頻繁變動的場景。  
- 在資源受限的邊緣或伺服器環境中，RAPT 大幅降低推論時間與記憶體需求，適合高吞吐的文件處理管線。  

🔗 **論文連結**  
📝 RAPT: Retrieval-Augmented Post-hoc Thresholding for Multi-Label Classification  
👤 Lasal Jayawardena, Nirmalie Wiratunga, Ikechukwu Nkisi-Orji, Darren Nicol (Robert Gordon University; William Nicol (Aberdeen) Limited)  
🔗 https://arxiv.org/abs/2605.16535  

你的多標籤分類管線是否仍在為全局閾值而苦惱？歡迎在留言區分享你的經驗或對後處理方法的看法 👇  

#AI #MultiLabelClassification #InformationRetrieval #RAPT #MachineLearning #工業應用 #Transformer #度量學習 #arXiv #技術分享
