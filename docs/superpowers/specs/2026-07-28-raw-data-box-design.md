# 摘要頁面「原始資料」展開 box — 設計

日期：2026-07-28

## 目標

在每篇自動生成的摘要文詳情頁加一個可展開的「原始資料」box，讓讀者能把 LLM 生成的成品與來源原文並排核對。用途是**單純查看**，不做 diff 對照。

涵蓋兩個前端：

- Astro 靜態站 `/daily/<id>`（`web/src/pages/daily/[slug].astro`）
- Web Monitor `/post/<date>/<slug>`（`src/web/templates/post_view.html`）

同時修復兩批會直接在 box 裡露出來的髒資料：HuggingFace 論文摘要的空白遺失（第 4 節）、跨來源的 HTML entity 未解碼（第 5 節）。

## 非目標

- 不做「LLM 生成 vs 原始摘要」的差異標示（YAGNI，肉眼比對已足夠）
- 不改 `/papers/<slug>`、`/trending/<slug>`——它們本來就直接攤平顯示原文
- 不改 HF 抓取解析邏輯（已於 commit `2c7cd40` 修正並實測通過，見 §4）

## 1. 資料層

### 1.1 為何以 `data/raw` 為唯一來源

`web/src/enrich.ts` 目前從 `data/scored` 讀進 `abstract` / `authors` / `organization`，但詳情頁只用了 `tags` 和 `organization`。直接接上去看似最省，但 **scored 有覆蓋缺口**：

抽查近 200 篇 `output/posts`，**10 篇 pinned 文不在 `data/scored`**（命中 `pinned_organizations` 免評分直接生成），而 **200/200 都在 `data/raw`**。

因此新增獨立模組讀 raw，`loadEnrichment()` 維持原樣不動。兩個 map 職責分離，box 的資料不會被 `enrich.ts` 的 `TAG_STOPLIST` 過濾掉。

### 1.2 `web/src/raw.ts`（新檔）

```
export interface RawItem { ... }
export interface RawIndex { byDayUrl: Map<string, RawItem>; byUrl: Map<string, RawItem> }
export function loadRaw(): RawIndex
export function lookupRaw(index: RawIndex, url?: string, postDay?: string): RawItem | null
```

- **雙索引**：主 key 為複合的 `` `${day}|${normalizeUrl(item.url)}` ``（`day` 取自 raw 檔名），另建 url-only 的 `byUrl` 作 fallback，同一 URL 保留**最早收集**的那筆
- `lookupRaw()` 的命中順序：先用 post 日期精準命中當天那筆，落空才退回 url-only
- **why 不能只用 url-only key**（原設計如此，實作階段改掉）：同一篇文章常橫跨多天被收集，url-only key 會被最後寫入的那天覆蓋，實測 **575 篇中有 69 篇**在 box 裡顯示到「別天」的原始資料（訊號值如 stars_today 也跟著失真）。複合 key 讓「post 當天」成為第一順位；退回 url-only 是為了 post 日期與收集日不同、或該天 raw 已被 `clean` 清掉的情形，此時取最早那筆離 post 日期最近、失真最小
- fallback 命中（`collectedDate !== post 日期`）時 UI 標示「非當日」並說明實際收集日，不讓讀者誤以為是當天資料
- URL 正規化直接 import `enrich.ts` 既有的 `normalizeUrl`；Python 端對應 `src/utils.py` 的 `normalize_url_light()`，**兩邊比對規則必須一致**（分歧的症狀是 box 靜默不顯示，見該函式 docstring）
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

- **不重用 `get_day_raw_items(d)`**——那支丟掉了 `organization` 與 `raw_metadata`，而 box 需要機構與 `upvotes` / `stars_today` 等天然訊號。直接讀當日 raw JSON
- URL 正規化用 `src/utils.py` 的 `normalize_url_light()`（去尾斜線、`http:` → `https:`），行為須與 Astro 端 `normalizeUrl` 一致。**不要用同檔的 `normalize_url()`**——那支為去重設計，會排序 query、去 `www.`，兩端來源相同時只會徒增不一致風險。兩支函式的用途差異表寫在 `normalize_url_light()` 的 docstring
- post 的日期即 raw 的日期，只查當日；查無回 `None`
- **兩端命中策略刻意分歧**：Astro 有 url-only fallback + 「非當日」標示（§1.2），Monitor 只查當日、查無就不渲染 box。理由是 Monitor 是本機工具，資料就在同一台機器上、缺 box 不痛；Astro 是對外的唯一入口，寧可退一步顯示鄰近日期的資料並標示清楚。改動任一端前先確認這個分歧仍成立
- **刻意不走 `ContentItem`**：`get_day_raw_items()` 用 `ContentItem(**raw)` 重建，等於讀取時再套一次 Layer A 的 s2twp 轉換（對繁體不冪等），而 box 承諾顯示的是磁碟上那份原始資料，故直接讀 dict。實測兩條路徑對同一批資料的文字漂移率 0.24%（5064 筆中 12 筆，如 `檔`→`件`）
- `_RAW_SIGNAL_LABELS` 與 `web/src/raw.ts` 的 `SIGNAL_LABELS` 必須逐字一致（key + emoji 標籤）；已知型別契約差異（TS `Number()` 接受字串、Python `isinstance` 不接受）記在 `data_service.py` 該常數上方，實測全量資料零影響

### `app.py`

`post_view` route 從 `post["frontmatter"]["url"]` 取 URL 查 raw，結果以 `raw_item` 傳入 template。

**注意**：`post_view.html` 同時被 `note_view` route 使用。`note_view` 不傳 `raw_item`，template 端以 `{% if raw_item %}` 包住即可，AI 筆記頁自然不會出現這個 box。

### `post_view.html`

同款 `<details>`，欄位與第 1.3 節一致。樣式跟隨 monitor 既有的 inline style 慣例，**不共用 Astro 的 CSS**——兩個前端本來就沒有共用樣式層，硬抽反而增加耦合。

## 4. HF 摘要空白遺失（黏字）

### 問題

`data/raw` 中 `source == hf_papers` 的項目有一批 `abstract` 空白全被吃掉（`LLMtrainingisshiftingfrom...`）。

**成因與現況**：HF 論文頁把 abstract 拆成大量 text node 並夾雜 Svelte hydration 註解，舊版解析用 `get_text(strip=True)` 導致節點間空白全失。`hf_papers.py:195` 已於 commit `2c7cd40`（2026-07-28）改為 `" ".join(p.get_text().split())`，以現行程式碼實跑破損 URL 實測 `space_ratio` 0.13、輸出正常。

**因此 collector 無需再改，這是純歷史資料修復。**

實測破損範圍：

- `data/raw` 全期 **192 筆**（最早 2026-04-16）
- `output/lists` 近 30 天 `papers.hf` **46/46 全破** ← 線上 `/papers/<slug>` 目前顯示的就是這批

### 修復判定式

```
source == "hf_papers"
  and len(abstract) > 100
  and ascii 比例 > 0.9              # 擋掉中文摘要（天生幾乎沒有空白）
  and abstract.count(" ") / len(abstract) < 0.05
```

實測命中 **hf_papers 192/192**，與人工清點的破損數完全吻合。

**必須限定 `source == hf_papers`**。全來源掃描時這條式子在 `hackernews`（26 筆）和 `reddit`（8 筆）會誤判——那些內容本來就是整串 URL 與 markdown 連結，空白天生就少。

**但不可改用「含 `/` 或 `http` 就排除」當防呆**：真實破損樣本 **59/192 含 `/`**（`and/or`、`Hand-Object`），這樣寫會漏掉 31% 的修復目標。唯一正確的防線是呼叫端的 source 限定。

修復動作見 §6 的 `repair-content` CLI。

### 順手補的防呆

`hf_papers.py:216` 的 arXiv fallback 觸發條件目前是 `len(abstract.strip()) < 100`。破損字串很長，會直接繞過補救而靜默通過。改為：

```
if (len(abstract.strip()) < 100 or looks_unspaced(abstract)) and arxiv_id:
```

`looks_unspaced()` 放在 `hf_papers.py` 匯出，與 `repair-content` 共用同一個判定函式。

## 5. HTML entity 未解碼

### 問題

多個 collector 把來源的 HTML 原文直接塞進 `ContentItem`，entity 沒解碼。實測分佈：

| 來源.欄位 | 未解碼 / 總數 | 範例 |
|---|---|---|
| `hackernews.abstract` | 269 / 1780 | `&#x27;`、`https:&#x2F;&#x2F;x.com` |
| `rss.title` | 58 / 2919 | `Spotify&#8217;s Prompted Playlists` |
| `reddit.abstract` | 6 / 101 | `&gt;` |
| `semantic_scholar.abstract` | 1 / 970 | `&amp;` |
| `newsapi.abstract` | 1 / 32 | `&nbsp;` |

`rss.title` 這批**已經洩漏到成品**：`output/posts` 有 4 篇的 frontmatter `title:` 帶著 `&#8217;`，線上直接可見。

與本功能的關聯：box 一攤開，`hackernews` 那 269 筆的 `&#x2F;&#x2F;` 會整片露出來。

### 修法：收斂到 `ContentItem` validator

`src/models.py` 的 `_normalize_to_traditional`（title / abstract）與 `_normalize_tags_to_traditional`（tags）已經是 Layer A 的唯一收斂點。在同一處、**`to_traditional()` 之前**加 `html.unescape()`：

```python
return to_traditional(html.unescape(v))
```

一改覆蓋所有來源與所有欄位，不必逐個 collector 修。

順序理由：先解碼再轉繁。`&#8217;` 解碼後是 `'`（ASCII 標點），OpenCC 不動它；反過來則是把 entity 字面餵給 OpenCC，雖然目前不會出錯，但語意上是拿未解碼的髒字串當輸入。

**已知取捨**：`html.unescape()` 只做一輪，`&amp;amp;` 會變成 `&amp;` 而非 `&`。來源若真的雙重轉義，這裡不處理——實測資料中沒有這種案例，不預先加複雜度。

## 6. 歷史資料修復 CLI `repair-content`

一支 CLI 同時處理 §4 的 HF 黏字與 §5 的 entity，避免把同一批檔案改兩遍。

### 修復範圍

| 目標 | 動作 |
|---|---|
| `data/raw/*.json` | HF 黏字 → 重抓；所有來源 title/abstract/tags → `html.unescape()` |
| `output/lists/*.json` | `papers.hf[].abstract` 以 URL 比對同步覆寫；title/abstract 解碼 |
| `output/posts/*.md` | **只改 frontmatter 的 `title:` 行**，body 不動 |

HF 黏字的重抓流程：重抓論文頁（現行 `hf_papers.py` 解析）→ 失敗或結果仍判定為破損則走 arXiv fallback → 兩者皆失敗則保留原值、記 warning，不中斷整批。

### 刻意不做的事

- **不改檔名**。`sam-altman8217s-orb` 這種被污染的 slug 就是 Astro 的頁面 id，改名等於改 URL、打斷既有連結與 `apb-read` localStorage 記錄。只修 frontmatter 的顯示標題。
- **不解碼 post body**。body 是 LLM 生成的 markdown，可能含程式碼區塊，裡面的 `&amp;` 有可能是字面意義。實測 4 篇受影響檔案的 entity 全部只出現在 `title:` 行，沒有動 body 的必要。

### 參數與慣例

`--days N`（預設全期）、`--dry-run`。無任何項目變更則不寫檔，與 `src/backfill.py` 既有慣例一致。

## 7. 錯誤處理總表

| 情境 | 行為 |
|------|------|
| `data/raw` 目錄不存在 | `loadRaw()` 回空 map，所有頁面不渲染 box |
| 單一 raw 檔 parse 失敗 | 跳過該檔，其餘正常 |
| post URL 在 raw 查無 | 該頁不渲染 box |
| `abstract` 為空 | 渲染 box，該欄顯示「（來源未提供摘要）」 |
| Monitor：`note_view` 走同一 template | 不傳 `raw_item`，box 不渲染 |
| `repair-content` HF 重抓失敗 | 保留原值 + warning，不中斷整批 |

## 8. 測試

- `loadRaw()`：URL 正規化比對、缺目錄降級、只讀近 30 天
- `get_raw_by_url()`：命中 / 查無 / URL 尾斜線差異
- `looks_unspaced()`：破損字串、**含 `/` 的破損字串**（真實樣本 59/192 含 `and/or`、`Hand-Object`，早期版本用「含 `/` 就排除」當防呆會誤殺這批）、正常英文摘要、中文摘要
- **URL 堆疊的 HN 留言不由 `looks_unspaced()` 擋**，改由呼叫端的 `source == hf_papers` 限定擋掉——測在 `repair_all()` 層級（給一筆 unspaced 的 hackernews 項目，斷言不觸發重抓）
- `ContentItem` entity 解碼：`&#8217;` / `&#x2F;` / `&amp;` / `&nbsp;` 各一例；已解碼字串冪等；**簡體 + entity 混合**（驗證解碼與 OpenCC 轉繁的順序正確）
- `repair-content --dry-run`：不寫檔
- 端對端：`npm run build` 後開實際頁面確認 box 展開正常，含一篇 pinned 文（驗證 scored 缺口確實由 raw 補上）、一篇 hackernews 來源（驗證 entity 已解碼）

## 9. Commit 切分

1. **feat**：`raw.ts` + Astro box + monitor box + `get_raw_by_url` + 測試
2. **fix**：`ContentItem` entity 解碼 + `hf_papers.py` 防呆 + `repair-content` CLI + 測試
3. **chore**：`repair-content` 產生的 `data/` / `output/` 資料修正（**獨立 commit**，diff 量大，不與程式碼混在一起）
