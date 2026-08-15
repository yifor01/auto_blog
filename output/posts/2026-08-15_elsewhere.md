---
title: Elsewhere
source: Simon Willison
url: https://simonwillison.net/elsewhere/
model: nvidia/nemotron-3-ultra-550b-a55b:free
generated_at: '2026-08-15T06:32:42.541025'
score: 38
---

📌 Simon Willison 近期開源動態：sqlite-utils 修錯、alchemy-utils 多資料庫原型、修訂歷史壓縮實驗

TL;DR：Simon Willison 釋出 sqlite-utils 4.2.1 修正崩潰錯誤、推出 alchemy-utils 以 SQLAlchemy 支援多資料庫、並實驗用 zstd 壓縮 JSON 陣列儲存文件修訂歷史。

Simon Willison 的個人站點 "Elsewhere" 近期密集更新，涵蓋多個開源專案的新版本與實驗性原型。對於關注 Python 資料工具鏈、LLM 整合與資料庫工程的開發者，這幾項更新各自解決了實際痛點：依賴管理陷阱、跨資料庫 API 統一、生產環境資料庫原子替換，以及長文件版本控制的儲存效率。

🐛 **sqlite-utils 4.2.1：修正 `uvx` 執行時缺少 `typing-extensions` 的崩潰錯誤**

sqlite-utils 4.2 引入了需要 `typing-extensions` 的程式碼，但該套件未列入正式依賴，僅存在於開發依賴群組。當使用者直接執行 `uvx sqlite-utils` 時，開發依賴不會被安裝，導致 CLI 工具崩潰。4.2.1 修正此問題，並新增煙霧測試確保 CLI 在缺少開發依賴時仍能運作：

```bash
uv run --no-default-groups --isolated sqlite-utils --help
```

`--no-default-groups` 阻止安裝預設開發群組，`--isolated` 忽略現有 `.venv` 中的額外依賴，確保測試環境乾淨。

🧩 **sqlite-utils 4.2.1：`table.transform()` 大幅擴充 Schema 保留能力**

`transform()` 透過建立新表、複製資料、刪除舊表再重命名來實現複雜 `ALTER TABLE`。新版本現在能保留：
- Check constraints
- Unique constraints
- 欄位註解

並新增檢查約束的內省屬性，方便程式化讀取 schema 定義。

🤖 **llm-gemini：支援 Gemini 3.7 Flash、推理追蹤與伺服器端工具**

最新版本相容 LLM 0.32，新增：
- Gemini 3.7 Flash、3.6 Flash、3.5 Flash-Lite
- 兩個嵌入模型：`gemini-embedding-2`、`gemini-embedding-001`
- 推理軌跡可視化
- 伺服器端工具啟用模式

作者以三種思考努力程度生成「騎自行車的鵜鶘」 SVG 測試輸出（註：早期版本渲染異常屬作者工具 Bug，已修復）。

🗄️ **alchemy-utils：以 SQLAlchemy 實現 sqlite-utils 多資料庫 API 原型**

作者嘗試打造「資料庫無關」版 sqlite-utils，核心 API 包含 `insert`、`upsert`、`insert_all`、`upsert_all`、`create`、`update` 及表內省功能，底層改用 SQLAlchemy 支援 PostgreSQL、SQLite、DuckDB。專案採用 `uv init`、紅綠燈 TDD 與 pytest 開發，針對 PostgreSQL 測試參考 `django-sql-dashboard` 模式。

使用範例：
```bash
# 列出 PostgreSQL 表資料
uvx --with 'alchemy-utils[postgresql]' alchemy-utils rows 'postgresql+psycopg://simon@localhost:5432/simonwillisonblog' redirects_redirect

# 匯入 CSV 到 DuckDB 自動建立 schema
curl 'https://raw.githubusercontent.com/simonw/sf-tree-history/refs/heads/main/Street_Tree_List.csv' | uvx --with 'alchemy-utils[duckdb]' alchemy-utils insert 'duckdb:////tmp/trees.db' trees - --csv
```

首次匯入近百萬筆樹木資料耗時近一小時，經最佳化後降至約 35 秒。

🔄 **datasette-upload-database：正式化 API 實現生產環境資料庫原子替換**

該外掛允許上傳 SQLite 資料庫至託管 Datasette 實例並自動服務。新版提供正式 API，支援在 GitHub Actions 等 CI 環境建構資料庫，完成後以原子方式替換生產環境資料庫，避免服務中斷。

🗜️ **修訂歷史壓縮實驗：zstd 壓縮 JSON 陣列儲存版本**

作者嘗試將文件所有歷史版本存為 JSON 字串陣列，再以 zlib 或 zstd 壓縮整體存入單一 BLOB 欄位，時間戳另存為整數陣列（無需壓縮）。GPT-5.6 Sol Pro 實作原型測試：1,000 次模擬修訂產生 20.4 MB 原始文本，壓縮後僅 80.3 KB（壓縮率約 99.6%）。為避免每次編輯都需解壓縮整個陣列，建議將歷史拆分為多列，每列最多 128 版本或 3 MB 未壓縮 JSON。

🎯 **實務啟示**

- **依賴管理**：CLI 工具若以 `uvx` 發布，務必將執行時真正需要的套件列入 `dependencies` 而非 `dev-dependencies`，並加入無開發依賴的煙霧測試。
- **跨資料庫抽象**：SQLAlchemy 雖引入效能開銷，但對需同時支援 PostgreSQL、SQLite、DuckDB 的工具而言，統一 API 能大幅降低維護成本；alchemy-utils 仍屬 alpha，生產環境採用前需自行效能基準測試。
- **資料庫部署**：datasette-upload-database 的原子替換模式適合「建構一次、部署多次」的 CI/CD 流程，消除遷移腳本失敗風險。
- **版本儲存策略**：對頻繁編輯的長文件，整體壓縮 JSON 陣列在儲存空間上極具優勢，但讀寫需解壓縮整份歷史；分塊策略（固定版本數或大小上限）可平衡空間與存取延遲。

🔗 **來源**
- 標題：Elsewhere
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/elsewhere/

#SimonWillison #sqliteutils #alchemyutils #Datasette #LLM #Gemini #SQLAlchemy #DatabaseEngineering #VersionControl #Compression
