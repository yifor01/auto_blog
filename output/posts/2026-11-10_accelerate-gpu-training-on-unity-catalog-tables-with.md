---
title: Accelerate GPU training on Unity Catalog tables with UCDataset
source: Databricks
url: https://www.databricks.com/blog/accelerate-gpu-training-unity-catalog-tables-ucdataset
model: claude-code/sonnet
generated_at: '2026-11-10T01:06:18.464680'
score: 81
---

📌 GPU訓練卡在等資料？UCDataset直接讀Unity Catalog

TL;DR：Databricks推出UCDataset,讓PyTorch直接串流讀取Unity Catalog資料表,實測訓練時間加速10倍。

GPU通常是訓練任務裡最貴的資源,但多數團隊根本餵不飽它們。真正的瓶頸往往不是模型本身,而是資料能不能夠快地送到GPU手上,每一秒晶片空等,燒掉的都是時間與金錢。

🤔 資料搬運才是真正的瓶頸

Databricks指出,多數訓練資料本來就存放在Unity Catalog的資料表裡,要把它送進分散式訓練任務,團隊得在幾種變通方法裡挑一個,每一種都要付出額外的時間與金錢成本。除了搬資料,loader本身也是負擔:每張GPU、每個worker都需要拿到均衡的一份資料切片,團隊得自己手刻這段邏輯,一個不小心的bug就可能讓模型在沒人發現的情況下,吃進重複或漏掉的資料列。結果就是昂貴的GPU閒置、訓練時間拉長,ML工程師忙著維護資料管線,而不是改善模型。

🧩 描述要讀什麼,剩下交給它

UCDataset是一款原生的PyTorch data loader,把Unity Catalog的資料表直接串流進訓練任務裡的每一張GPU,不用匯出、不用複製、也不用自己寫loader程式碼。使用方式是,你只需要描述要讀的資料表、需要的欄位,以及row filter;篩選條件會在讀取資料表檔案的當下就套用,不符合條件的資料列根本不會進到訓練程式碼裡。UCDataset會直接吐出完整的batch,只要用batch_size=None把它包進標準PyTorch DataLoader即可,不需要額外寫sampler或sharding程式碼,因為每張GPU會自動拿到屬於自己的那份資料。

Databricks舉了一個範例情境:團隊把使用者與商品特徵、加上點擊標籤存在main.recsys.ctr_features這張表裡,每天都有新的曝光資料寫入。他們想在兩個節點、共16張GPU上,直接從這張表訓練一個CTR（click-through-rate）模型。做法是在train.py裡選定這張表、篩出已標記的訓練資料列、挑出模型需要的欄位,搭配標準PyTorch DDP訓練迴圈;再用workload.yaml描述這個任務,讓它在每個節點上用torchrun啟動train.py,透過AI Runtime CLI執行。要擴大到更多GPU,只需要調整workload.yaml裡的num_accelerators,訓練程式碼本身不用改。安裝方式也很單純,在notebook裡執行%pip install databricks-uc-dataset,或直接從PyPI安裝同名套件即可。

📊 實測:300GB資料表、8張H100,加速10倍

Databricks在模擬的生產環境工作負載上做了測試,用8張NVIDIA H100 GPU串流一張300GB的特徵表來訓練推薦系統模型,平均訓練時間比直接讀取匯出的Parquet副本快了10倍。

💡 權限與一致性是順帶解決的紅利

UCDataset讀的是Unity Catalog裡的即時表,沒有匯出步驟,自然也沒有第二份副本需要額外同步;每次執行讀取時都會套用filter與該表的deletion vectors,所以每一輪訓練都能自動吃到上一次執行後新增的資料列。在AI Runtime上,訓練任務是以執行者的身分讀取資料,Unity Catalog原有的權限設定會直接套用在訓練任務上;因為讀的是受治理的原表,也就不存在另一份需要單獨上鎖的匯出副本。資料治理與GPU訓練效能這兩件事,不再是互相拉扯的取捨。

⚠️ 目前仍是Beta,限制也很明確

目前UCDataset只能讀取Unity Catalog裡登記的Delta表（包含有deletion vectors的表）,但在Beta階段還無法讀取設有row filter或column mask的資料表。此外UCDataset目前主要處理結構化表格資料;針對Unity Catalog volumes裡的非結構化檔案,官方另外提供UCVolumeDataset做本地快取串流,支援images、audio、documents等多模態訓練（透過FILE型別直接從表裡讀取）的能力則仍在擴充中。

🎯 實務啟示

如果你的訓練資料已經在Unity Catalog裡,而目前還在手刻sharding邏輯,或靠匯出Parquet再讀取,UCDataset值得評估,尤其適合對GPU閒置時間敏感、又需要資料持續更新的場景,像是天天有新曝光紀錄的推薦系統。但要留意Beta階段對row filter與column mask資料表的限制,上線前先確認你的表結構是否相容。

🔗 來源
- 標題：Accelerate GPU training on Unity Catalog tables with UCDataset
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/accelerate-gpu-training-unity-catalog-tables-ucdataset

#Databricks #UnityCatalog #PyTorch #GPU #DistributedTraining #MLOps #DataEngineering #DeepLearning #MachineLearning #AIInfrastructure
