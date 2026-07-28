# 摘要頁面「原始資料」展開 box — 設計

日期：2026-07-28

## 目標

在每篇自動生成的摘要文詳情頁加一個可展開的「原始資料」box，讓讀者能把 LLM 生成的成品與來源原文並排核對。用途是**單純查看**，不做 diff 對照。

涵蓋兩個前端：

- Astro 靜態站 `/daily/<id>`（`web/src/pages/daily/[slug].astro`）
- Web Monitor `/post/<date>/<slug>`（`src/web/templates/post_view.html`）

同時修復 HuggingFace 論文摘要的歷史破損資料（見第 4 節）。

## 非目標

- 不做「LLM 生成 vs 原始摘要」的差異標示（YAGNI，肉眼比對已足夠）
- 不改 `/papers/<slug>`、`/trending/<slug>`——它們本來就直接攤平顯示原文
- 不改 collector 抓取邏輯（HF 解析已於 commit `2c7cd40` 修正並實測通過）

## 1. 資料層

### 1.1 為何以 `data/raw` 為唯一來源

`web/src/enrich.ts` 目前從 `data/scored` 讀進 `abstract` / `authors` / `organization`，但詳情頁只用了 `tags` 和 `organization`。直接接上去看似最省，但 **scored 有覆蓋缺口**：

抽查近 200 篇 `output/posts`，**10 篇 pinned 文不在 `data/scored`**（命中 `pinned_organizations` 免評分直接生成），而 **200/200 都在 `data/raw`**。

因此新增獨立模組讀 raw，`loadEnrichment()` 維持原樣不動。兩個 map 職責分離，box 的資料不會被 `enrich.ts` 的 `TAG_STOPLIST` 過濾掉。

### 1.2 `web/src/raw.ts`（新檔）

```
export interface RawItem { ... }
export function loadRaw(): Map<string, RawItem>
```

- key：`normalizeUrl(item.url)`，直接 import `enrich.ts` 既有的 `normalizeUrl`，兩邊比對規則必須一致
- 只讀近 `RECENT_DAYS`(30) 天的 `data/raw/*.json`，與 `recentCutoff()` 同基準——詳情頁本來就只 build 近 30 天
- 快取策略沿用 `enrich.ts`：`import.meta.env?.DEV` 時不快取（dev server 長駐會看不到 pipeline 新寫入的檔）
- 讀檔/parse 失敗一律 `continue`，缺 `data/raw` 目錄時回傳空 map（優雅降級，與 `loadEnrichment()` 一致）

Build 成本：30 個檔約 8.2MB JSON parse，一次性，可接受。

### 1.3 Box 欄位（Astro / Monitor 共用定義）

| 欄位 | 來源 | 缺漏處理 |
|------|------|----------|
| 來源原標題 | `item.title` | 必有 |
| 摘要原文 | `item.abstract` | 缺 → 顯示「（來源未提供摘要）」 |
| 作者 | `item.authors` | 空陣列 → 不顯示該列 |
| 機構 | `item.organization` | 空字串 → 不顯示該列 |
| 原始 tags | `item.tags` | **不套 stoplist**，空 → 不顯示 |
| 來源名稱 | `item.source_name` | 必有 |
| 原始 URL | `item.url` | 必有 |
| 收集日期 | raw 檔名的 `YYYY-MM-DD` | 必有 |
| 來源訊號 | `upvotes` / `stars_today` / `points` / `citation_count` | 有值才顯示，`0`/`null` 不顯示 |

「來源原標題」與 post frontmatter 的 `title` 通常相同，但仍獨立顯示——LLM 有改寫標題的情況，這正是要核對的重點之一。

## 2. Astro `/daily/<id>`

### 位置

`<Content />` **之後**、`.model-note` 之前。讀者先讀成品，要核對再展開。

### 實作

原生 `<details class="raw-box">` + `<summary>`，**零 JavaScript**：

- SSG 純靜態，不增加 client bundle
- Chrome 的 Ctrl+F 會自動展開 `<details>` 內的命中結果
- 不會像閱讀進度條那樣有 `ClientRouter` 軟導航的 listener 洩漏問題（見 `[slug].astro` 現有註解）

細節：

- `abstract` 用 `white-space: pre-wrap` 保留原始換行
- 樣式沿用既有 CSS 變數（`--surface` / `--border` / `--mono` / `--faint`），與 `.score-card` 視覺一致
- **`loadRaw()` 查無此 URL 時整個 `<details>` 不渲染**，不留空殼
- `getStaticPaths()` 內把 `RawItem` 一併放進 `props`，與現有 `enrich` 的傳法一致

## 3. Web Monitor `/post/<date>/<slug>`

### `data_service.py`

新增 `get_raw_by_url(date_str: str, url: str) -> dict | None`：

- 沿用既有的 `get_day_raw_items(d)` 讀當日 raw
- URL 正規化須與 Astro 端 `normalizeUrl` 行為一致（去尾斜線、`http:` → `https:`）
- post 的日期即 raw 的日期，只查當日；查無回 `None`

### `app.py`

`post_view` route 從 `post["frontmatter"]["url"]` 取 URL 查 raw，結果以 `raw_item` 傳入 template。

**注意**：`post_view.html` 同時被 `note_view` route 使用。`note_view` 不傳 `raw_item`，template 端以 `{% if raw_item %}` 包住即可，AI 筆記頁自然不會出現這個 box。

### `post_view.html`

同款 `<details>`，欄位與第 1.3 節一致。樣式跟隨 monitor 既有的 inline style 慣例，**不共用 Astro 的 CSS**——兩個前端本來就沒有共用樣式層，硬抽反而增加耦合。

## 4. HF 摘要歷史資料修復

### 問題

`data/raw` 中 `source == hf_papers` 的項目有一批 `abstract` 空白全被吃掉（`LLMtrainingisshiftingfrom...`）。

**成因與現況**：HF 論文頁把 abstract 拆成大量 text node 並夾雜 Svelte hydration 註解，舊版解析用 `get_text(strip=True)` 導致節點間空白全失。`hf_papers.py:195` 已於 commit `2c7cd40`（2026-07-28）改為 `" ".join(p.get_text().split())`，以現行程式碼實跑破損 URL 實測 `space_ratio` 0.13、輸出正常。

**因此 collector 無需再改，這是純歷史資料修復。**

實測破損範圍：

- `data/raw` 全期 **192 筆**（最早 2026-04-16）
- `output/lists` 近 30 天 `papers.hf` **46/46 全破** ← 線上 `/papers/<slug>` 目前顯示的就是這批

### 新增 CLI `repair-abstracts`

判定式（同時作為修復目標的篩選條件）：

```
source == "hf_papers" and len(abstract) > 100 and abstract.count(" ") / len(abstract) < 0.05
```

行為：

1. 掃 `data/raw/*.json` 找出破損項目
2. 重抓論文頁解析（現行 `hf_papers.py` 邏輯）
3. 抓取失敗或結果仍判定為破損 → 走 arXiv fallback
4. 兩者皆失敗 → 保留原值、記 warning，不寫入
5. 同步覆寫 `output/lists/*.json` 的 `papers.hf[].abstract`（以 URL 比對）
6. 無任何項目變更則不寫檔（與 `src/backfill.py` 的既有慣例一致）

參數：`--days N`（預設全期，192 筆量體不大）、`--dry-run`。

### 順手補的防呆

`hf_papers.py:216` 的 arXiv fallback 觸發條件目前是 `len(abstract.strip()) < 100`。破損字串很長，會直接繞過補救而靜默通過。改為：

```
if (len(abstract.strip()) < 100 or _looks_unspaced(abstract)) and arxiv_id:
```

`_looks_unspaced()` 與 `repair-abstracts` 共用同一個判定函式，放在 `hf_papers.py` 匯出。

## 5. 錯誤處理總表

| 情境 | 行為 |
|------|------|
| `data/raw` 目錄不存在 | `loadRaw()` 回空 map，所有頁面不渲染 box |
| 單一 raw 檔 parse 失敗 | 跳過該檔，其餘正常 |
| post URL 在 raw 查無 | 該頁不渲染 box |
| `abstract` 為空 | 渲染 box，該欄顯示「（來源未提供摘要）」 |
| Monitor：`note_view` 走同一 template | 不傳 `raw_item`，box 不渲染 |
| `repair-abstracts` 重抓失敗 | 保留原值 + warning，不中斷整批 |

## 6. 測試

- `loadRaw()`：URL 正規化比對、缺目錄降級、只讀近 30 天
- `get_raw_by_url()`：命中 / 查無 / URL 尾斜線差異
- `_looks_unspaced()`：破損字串、正常英文摘要、中文摘要（**中文摘要幾乎沒有空白，必須不被誤判**——判定式須限定 `source == hf_papers`，而 HF abstract 一律為英文）
- `repair-abstracts --dry-run`：不寫檔
- 端對端：`npm run build` 後開實際頁面確認 box 展開正常，含一篇 pinned 文（驗證 scored 缺口確實由 raw 補上）

## 7. Commit 切分

1. **feat**：`raw.ts` + Astro box + monitor box + `get_raw_by_url` + 測試
2. **fix**：`hf_papers.py` 防呆 + `repair-abstracts` CLI + 測試
3. **chore**：`repair-abstracts` 產生的 `data/` / `output/` 資料修正（**獨立 commit**，diff 量大，不與程式碼混在一起）
