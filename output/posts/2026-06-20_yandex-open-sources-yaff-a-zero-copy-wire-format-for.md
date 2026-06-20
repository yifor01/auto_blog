---
title: 'Yandex Open-Sources YaFF: A Zero-Copy Wire Format for Protobuf With Near-Struct
  Read Speed'
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/20/yandex-open-sources-yaff-a-zero-copy-wire-format-for-protobuf-with-near-struct-read-speed/
score: 80
model: google/gemma-4-31b-it:free
generated_at: '2026-06-20T19:40:58.693923'
---

📌 【Yandex 開源 YaFF：讓 Protobuf 獲得零拷貝的讀取速度

TL;DR：Yandex 推出 YaFF，在保留 Protobuf 的 .proto 模式的同時，實現零拷貝 (zero-copy) 的讀取效能。

對於高負載的後端伺服器，CPU 消耗過多在解析 (parsing) Protobuf 訊息，在規模化後可能地消耗數千個物理核心。

🤔 **Protobuf 的效能痛點：解析成本太高**

在許多高負-載的後端系統中，Protobuf 的解析過程會佔用雙位數百分比的 CPU 資源。雖然 Google 的 FlatBuffers 能提供零拷貝讀取，但它與 Protobuf 的語義不相容，意味著工程師必須維護兩套 schema，並手寫轉換層，這讓許多團隊覺得遷移成本過高，決定放棄。

🧩 **YaFF 的設計：保留 .proto 模式的零拷別方案**

Yandex 推出的 YaFF (Yet another Flat Format) 並非要取代 Protobuf，而是一種替代的線路格式 (wire format)。它的核心邏輯是：

- **維持單一事實來源**：繼續使用原有的 .proto 檔案，無需額外維護另一套 schema。
- **改變記憶體佈局**：僅改變資料在記憶體中的儲存方式，讓讀取時無需解析步驟，直接從 buffer 中讀取欄位。
- **漸進式採納**：由於支持雙向轉換，開發者可以在效能最關鍵的熱路徑 (hot path) 引入 YaFF，其餘部分則維持原有的 Protobuf，降低遷移門檻。

🧩 **四種記憶體佈局 (Layouts) 靈活切換**

YaFF 根據不同場景提供四種儲存選項：
- **Fixed**：純粹的 packed struct，無標頭 (header)，適用於固定不變的 schema。
- **Flat**：增加 2-byte 標頭，支援 schema 演進 (evolution)。
- **Sparse**：透過元數據表 (meta table) 定址，適用於稀疏的 schema。
- **Dynamic**：預設選項，會根據 schema 狀態在 Flat 與 Sparse 之間自動切換。

📊 **效能驗證與實作**

Yandex 隨專案提供了基於 `google/benchmark` 的可重複基準測試套件（於 Release build 執行），用以驗證其讀取速度與效能表現。

🎯 **實務啟示**

對於需要極高吞吐量且不想放棄 Protobuf 生態系的後端工程師，YaFF 提供了一個平衡點：你不需要為了效能而被迫維護兩套 schema (如 FlatBuffers)，就能在關鍵路徑上消除解析成本，降低 CPU 負載。

🔗 **來源**
- 標題：Yandex Open-Sources YaFF: A Zero-Copy Wire Format for Protobuf With Near-Struct Read Speed
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/06/20/yandex-open-sources-yaff-a-zero-copy-wire-format-for-protobuf-with-near-struct-read-speed/

#Yandex #Protobuf #YaFF #ZeroCopy #Cpp #Serialization #BackendPerformance #OpenSource #Apache2 #SoftwareArchitecture
