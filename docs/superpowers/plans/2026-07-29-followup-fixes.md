# 三項 follow-up 修正 — 實作計畫

> 承接 `2026-07-28-raw-data-box.md` 的最終 review follow-up 清單，使用者裁示三項全修。

**Goal:** 修掉最終 review 列出的三個殘留問題：`data/scored` 未納入修復、來源媒體標記外洩到 box、讀-改-寫路徑重複套用 s2twp。

**Architecture:** B 與前一支 branch 的 entity 解碼共用同一個收斂點（`ContentItem` validator，Layer A）；A 與 B 的歷史資料回補共用同一支 `repair-content`，最後只跑一次；C 改的是兩條寫回路徑，做法比照已驗證有效的 `repair.py`（保留原始 dict、只 patch 變動欄位）。

**Tech Stack:** Python 3 / Pydantic v2 / Typer / pytest

## Global Constraints

- 所有註解與使用者可見文字用**繁體中文**
- **只剝 `img` / `iframe` / `script` / `style` / `noscript` 五種標記**。實測 453 個含 tag 的欄位裡，`<version>` `<name>` `<string>` `<std>` `<id>` 是程式碼片段與泛型（`Vec<String>`），一律剝除會毀掉正常內容
- 剝除的正規表示式**必須容忍 `<` 後有空白**——實測 309 筆量子位的格式是 `< img id="wx_img" ...>`
- **只動 Layer A**（`src/models.py` 的 `ContentItem` validator），不得碰 Layer B（`save_blog_post` 的 `to_traditional_shape_only`）
- 資料寫回一律用 `src/utils.py` 的 `save_json()`
- 測試中不得發出真實 HTTP 請求；`repair-content` 的 fetcher 一律注入
- Commit message 格式 `<type>: <description>`
- 環境：先 `source .venv/bin/activate`
- `tests/` 與 `CHANGELOG.md` 被 `.gitignore` 排除，commit 不含它們（專案刻意設計），但仍要更新
  （**2026-07-31 部分已推翻**：`tests/` 已解除排除、納管進 repo 並接上 CI；`CHANGELOG.md` 仍維持排除。
  此條為本計畫執行當下的約束，保留不改）
- **時序約束**：背景有 pipeline 在寫 `data/`，Task 4 的 repair 實跑必須等它結束

## 實測數據（設計依據）

| 項目 | 數字 |
|---|---|
| `data/scored` entity 殘留 | 17 處 |
| `data/scored` HF 黏字殘留 | 49 筆 |
| 受影響 scored 檔數 | 29 |
| `data/raw` 含媒體標記的欄位 | 325（img 309 / script 10 / iframe 3） |
| 媒體標記來源分佈 | 量子位 309、GitHub Trending 8、Hacker News 6、Simon Willison 2 |
| 標記位置 | 開頭 309 / 中間 36 |
| 剝除後長度 < 50 字元的 | **0 / 325**（不會清空內容） |
| s2twp 二次套用漂移率 | 12 / 5064 = 0.24%（`卷→捲`、`了→瞭`、`檔→件`） |

---

### Task 1: 寫回路徑不再 round-trip ContentItem

**Files:**
- Modify: `src/backfill.py:51`、`src/backfill.py:79`
- Modify: `src/pipeline.py:243`、`src/pipeline.py:303`
- Test: `tests/test_backfill.py`、`tests/test_pipeline.py`

**根因**：`items = [ContentItem(**it) for it in raw_data]` → `save_json([it.model_dump() for it in items], raw_path)`。每次讀-改-寫都對已轉繁的存檔再套一次 Layer A 的 s2twp，而 s2twp 對繁體不冪等（`这个文档的参数` → `這個文件的參數` → `這個檔案的參數`，第 3 輪才穩定）。

**做法**：保留原始 dict，只 patch 真正變動的欄位。`backfill` 只動 `raw_metadata.upvotes`；`--supplement` 對既有項目寫回原 dict、只有新收的項目才用 `model_dump()`。

`build_day_lists()` 仍可吃 `ContentItem` 物件（它不寫回 raw），不用改。

- [ ] **Step 1: 寫失敗的測試（backfill 不漂移）**

```python
def test_backfill_does_not_reapply_opencc(tmp_path, monkeypatch):
    """讀-改-寫不得對已轉繁的存檔再套一次 s2twp（檔→件 那類漂移）。"""
    # s2twp 對這串繁體不冪等：這個文件的參數 → 這個檔案的參數
    drifting = "這個文件的參數設定"
    ...  # 造 raw JSON、mock fetch_upvotes 回傳有變動的票數、跑 backfill
    # 斷言：abstract 逐字不變，只有 raw_metadata.upvotes 變了
```

- [ ] **Step 2: 跑測試確認失敗**
- [ ] **Step 3: 改 `backfill.py`**——用原始 dict 寫回，只 patch upvotes
- [ ] **Step 4: 跑測試確認通過**
- [ ] **Step 5: 同樣處理 `pipeline.py` 的 `--supplement`**（既有項目寫回原 dict）
- [ ] **Step 6: 全套 `pytest tests/ -q`**
- [ ] **Step 7: Commit** `fix: 寫回 raw 時保留原始 dict，避免重複套用 s2twp`

---

### Task 2: `ContentItem` 剝除來源媒體標記

**Files:**
- Modify: `src/models.py`
- Test: `tests/test_models.py`

**做法**：在 Layer A validator 內、`html.unescape()` 之後、`to_traditional()` 之前剝除媒體標記，並正規化剝除後留下的多餘空白。

**只剝五種**：`img` / `iframe` / `script` / `style` / `noscript`。`script` 與 `style` 若成對出現，連同標記之間的內容一起剝除（那是 JS/CSS 不是正文）；其餘只剝標記本身。

- [ ] **Step 1: 寫失敗的測試**——涵蓋：量子位的 `< img id="wx_img" ...>` 開頭（注意 `<` 後有空格）、中間出現的 `<iframe>`、成對 `<script>...</script>` 連內容剝除、**`Vec<String>` 與 `<version>` 必須完好無損**、剝除後空白正規化、對無標記文字冪等
- [ ] **Step 2: 跑測試確認失敗**
- [ ] **Step 3: 實作**
- [ ] **Step 4: 跑測試確認通過**
- [ ] **Step 5: 全套回歸**（這個改動影響整條 pipeline 下游）
- [ ] **Step 6: Commit** `fix: ContentItem 剝除來源殘留的 img/iframe/script 標記`

---

### Task 3: `repair-content` 擴充 `data/scored` 與媒體標記

**Files:**
- Modify: `src/repair.py`
- Test: `tests/test_repair.py`

**做法**：

1. 新增 `data/scored/*.json` 段。結構與 raw 不同：是 `list[dict]`，每個 row 的來源欄位在 `row["item"]` 底下（`title` / `abstract` / `tags` / `source`）。entity 解碼與 HF 黏字重抓的判定式沿用既有的
2. 既有的 raw / lists / posts 三段加上媒體標記剝除，與 Task 2 共用同一個剝除函式（從 `src/models.py` 匯出，不要複製一份）
3. 統計欄位增加 `tags_stripped`（或等價命名），CLI 輸出一併顯示

**注意**：scored 的 HF 黏字重抓要沿用同一個 `fetcher` 與節流；若同一個 url 在 raw 已經重抓過，直接沿用結果不要重打。

- [ ] **Step 1: 寫失敗的測試**——scored 段的 entity / 黏字 / 媒體標記各一；`--dry-run` 對 scored 不寫檔；無變更不寫檔
- [ ] **Step 2: 跑測試確認失敗**
- [ ] **Step 3: 實作**
- [ ] **Step 4: 跑測試確認通過（含 mutation 驗證新的寫入 call site）**
- [ ] **Step 5: `--dry-run` 對真實資料實跑**，確認候選數與實測數據表相符
- [ ] **Step 6: Commit** `fix: repair-content 擴充 data/scored 與媒體標記剝除`

---

### Task 4: 執行修復並驗證

**前置**：確認背景 pipeline 已結束（`pgrep -af "src.cli run"` 無輸出）。

- [ ] **Step 1: 全期 `--dry-run`**，確認候選數
- [ ] **Step 2: 小批 `--days 3`（非 dry-run）**，檢視 diff
- [ ] **Step 3: 全期實跑**
- [ ] **Step 4: 殘留驗證**——`data/scored` entity 0 / 黏字 0；`data/raw` 媒體標記 0；`data/raw` 與 `output/lists` 既有的 0 殘留維持 0
- [ ] **Step 5: 確認沒有把好資料改壞**——剝除後無內容被清空；`Vec<String>` 那類泛型完好；比對 commit 前後每個檔的項目數與欄位集合
- [ ] **Step 6: 獨立 `chore:` commit**
- [ ] **Step 7: 重 build Astro 站，抽驗原本受影響的 21 篇之一**，確認 box 內不再有 `< img id="wx_img"`
- [ ] **Step 8: 更新 CHANGELOG**
