---
title: "Introducing Storage Buckets on the Hugging Face Hub"
source: HuggingFace Blog
url: https://huggingface.co/blog/storage-buckets
score: 103
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-11T18:40:39.908346
---

📌 **Hugging Face 推出 Storage Buckets：AI 訓練資料的新家**

你是否曾經為了管理 AI 訓練產生的海量中間檔而頭痛？Hugging Face 剛剛推出 Storage Buckets，專門解決這個長期困擾 ML 工程師的問題。

🤔 **為什麼 AI 訓練資料不適合放 Git 裡？**

當你開始大規模訓練模型時，會產生大量不斷變化的檔案：檢查點、優化器狀態、處理過的數據分片、日誌、追蹤等等。這些檔案有三個特徵：

- 頻繁變更（每幾分鐘就更新一次）
- 來自多個任務的同時寫入
- 不需要版本控制

用 Git 來管理這些檔案就像用鐵鎚敲核桃——太重了，而且效率低下。

🧪 **Storage Buckets 的核心設計**

Hugging Face 的解決方案是：一個基於 S3 協議的物件儲存系統，但與眾不同的是：

1. **非版本控制設計**：專為頻繁寫入和覆蓋而優化
2. **Xet 技術加持**：對共享內容的檔案特別高效（訓練資料的典型特徵）
3. **完整的 Hub 整合**：可以在瀏覽器中瀏覽、透過 Python 腳本操作、或使用 hf CLI 管理
4. **標準權限管理**：支援私人或公開的 Bucket，整合 Hugging Face 的權限系統

🎣 **真正的問題是：為什麼現在才有？**

AI 訓練的生態系統已經成熟到需要這樣的基礎設施。當訓練集群、數據管道和智能體變得無處不在時，我們需要一個專門為它們設計的儲存抽象層。

💡 **Storage Buckets 的四大使用場景**

1. **訓練集群**：寫檢查點和優化器狀態，需要快速且頻繁
2. **數據管道**：迭代處理原始數據集，產生臨時檔案
3. **智能體系統**：儲存追蹤、記憶和共享知識圖譜
4. **實驗管理**：快速切換不同的實驗配置和結果

🎯 **從開發者角度的實用價值**

- **Python 整合**：可以直接從程式碼操作 hf://buckets
- **檔案系統整合**：支援標準的檔案系統操作介面
- **版本化儲存庫**：可以從 Bucket 升級到版本控制的儲存庫
- **預熱功能**：能將資料預先載入到計算節點附近，減少延遲

⚠️ **這不是萬能的，但解決了真正的痛點**

Storage Buckets 專注於一個明確的問題領域：ML 生產環境中的中間檔案管理。它不是為了取代 Git 儲存庫，而是作為一個互補的工具。

🔗 **論文連結**
📝 Introducing Storage Buckets on the Hugging Face Hub
👤 Hugging Face Team
🔗 部落格：huggingface.co/blog/storage-buckets
🔗 GitHub：github.com/huggingface/huggingface_hub

你現在用什麼方式管理 AI 訓練產生的中間檔案？有沒有遇到類似的困擾？歡迎分享你的經驗！

#AI #MachineLearning #HuggingFace #Storage #MLInfrastructure #DataEngineering
