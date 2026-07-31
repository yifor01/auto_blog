# 讀取端無損 / 清洗歸資料層 — 分層原則與四類歷史髒資料修復

日期：2026-07-31
相關 commit：`0bb411a`..`3431163`（35 個），branch `feat/raw-data-box` 已 merge 進 main

## 起點

需求只是「在摘要詳情頁加一個可展開的原始資料 box」。實作前掃了一次要顯示的資料，發現攤開來會露出四批髒東西，於是變成一次資料層整理。

## 四個問題與根因

### 1. HF 摘要空白全失（192 筆）

HF 論文頁把 abstract 拆成大量 text node 並夾雜 Svelte hydration 註解。`get_text(strip=True)` 逐節點 strip 後無縫串接 → `LLMtrainingisshiftingfrom...`。

抓取邏輯已於 `2c7cd40` 修好（`" ".join(p.get_text().split())`），但歷史資料還壞著。而 arXiv fallback 的觸發條件是 `len(abstract) < 100`——破損字串很長，**永遠繞過補救而靜默通過**。

### 2. HTML entity 未解碼（340 處）

多個 collector 把來源 HTML 原文直接塞進 `ContentItem`。`rss.title` 那批已洩漏到成品，線上直接顯示 `Sam Altman&#8217;s orb`。

### 3. 來源媒體標記外洩（319 欄位）

`< img id="wx_img" src="...">`（注意 `<` 後有空格）殘留在 abstract 開頭，量子位佔 309 筆。

### 4. 讀取端重複套用 s2twp 造成漂移（實測一輪 731 欄位 / 3.00%）

**這個是最隱蔽的。** `ContentItem` 的 Layer A validator 用 `to_traditional()`（OpenCC s2twp，含台灣詞庫），而 s2twp **對繁體不冪等**：

```
这个文档的参数 → 這個文件的參數 → 這個檔案的參數   （第 3 輪才穩定）
```

有 22 個地方在做「讀 JSON → 建 `ContentItem`/`ScoredItem` → 用它的文字」。每讀一次就多套一輪。其中兩處是讀-改-寫同一路徑（`backfill.py` 每天跑、`pipeline.py --supplement`），會把漂移**寫回存檔**。

## 核心設計原則：讀取端無損，清洗歸資料層

一開始只想修 `backfill.py` 的寫回。但同一缺陷散在 7 個讀 raw + 15 個讀 scored 的呼叫點，於是收斂成兩個 helper：

```python
# src/models.py
_LAYER_A_FIELDS = ("title", "abstract", "tags")

def item_from_raw(raw: dict) -> ContentItem      # 完整建構後把 Layer A 欄位從原始 dict 還原
def scored_from_raw(raw: dict) -> ScoredItem     # 同上，處理內嵌的 item
```

**為何不用 `model_construct()`**：實測否決——它跳過所有驗證含型別轉換，`published_date` 會停在 `str`，下游 `.isoformat()` 當場 AttributeError。改用「完整建構後還原文字欄位」，前提是 `validate_assignment` 為 `False`（Pydantic v2 預設）。

**分工因此明確**：
- **讀取端**（`item_from_raw` / `scored_from_raw`）：無損還原，不做任何清洗
- **寫入端**（collector → Layer A validator）：新資料在建構時清洗
- **資料層**（`repair-content`）：修歷史髒資料

`repair.py` 之所以能在 Task 7 全量改寫 98 個 raw 檔而零漂移，正是因為它從頭就走原始 dict、不經 `ContentItem`。

## 可複用 pattern

### A. 「守門 + 轉換 + 修正表」三段式

簡→繁修復不能對全量跑 s2twp（會漂）。做法：

1. **欄位層級守門**：欄位需含明確簡體字才進轉換器
2. **收斂到不動點**：s2tw 轉一次不穩定（`互不干扰`→`互不干擾`→`互不幹擾`）
3. **變體修正表**（41 條）：迴圈後套，修 OpenCC 的消歧錯誤

**守門的已知失效模式**：守門是欄位層級、每輪重新評估。第一輪轉完後欄位已幾乎全繁體，只剩一個殘留字（如 `佣`）就把整個欄位重新放進詞組轉換器——**守門在第二輪失效開放**。

### B. 有守門的表是一次性機會，無守門的不是

`_VARIANT_FIXES` 只套在「真的轉過」的欄位（`if out == text: return text` 早退）。**實跑寫入後欄位變純繁體 → 守門再也不放行 → 日後補條目對已修過的資料完全無效**，只能 `git revert`。實測約 87% 的欄位修完後不再留簡體證據字元。

因此後來另建一張**無守門的 `_TYPO_FIXES`**（60 條）處理守門碰不到的錯字。代價是安全標準高得多——它會套到全部 88000 個欄位而非 800 個，每條都要對全語料驗傷。

### C. 一簡對多繁的條目必須帶脈絡錨定

通用寫法會誤傷，而且誤傷對象往往就在自己的語料裡：

| 通用條目 | 誤傷 |
|---|---|
| `託盤→托盤` | `委託盤與信託盤`（股市工具 README） |
| `遊標→游標` | `旅遊標籤` |
| `幹擾→干擾` | `骨幹擾動`（ML backbone + perturbation） |
| `復雜→複雜` | `修復雜湊表`（雜湊 = hash，台灣術語） |
| `隻會→只會` | `一隻會飛的鳥` |
| `·庫裡安→·庫里安` | 通用寫法會壞 `資料庫裡安放著索引` |

**每條都要有 guard 測試**，而且要用 mutation 驗證錨定是必要的（把條目還原成通用寫法，guard 必須 FAIL）。

### D. 跨語言平行實作只能靠註解與 mutation 守

`web/src/raw.ts` 與 `src/web/data_service.py` 是同功能的兩份實作。TS 側沒有測試框架、Python 側的測試被 `.gitignore` 排除（CI 跑不到），所以一致性**只由人的注意力維持**。做法：

> **（2026-07-31 已解決，上段為當時實況，保留不改）**
> 這個缺口已補上，兩端都由 `.github/workflows/ci.yml` 守：
> - TS 側引入 vitest（`e77f802`，使用者追認），`web/src/raw.test.ts` 41 個測試含 13 個 mutation 驗證
> - Python `tests/` 解除 `.gitignore` 排除、844 個測試納管並接上 `python-test` job
> - 契約期望值收斂成單一來源 `web/src/__fixtures__/cross-lang-contract.json`（`e0fb178`、`2d99733`），
>   `web/src/cross-lang-contract.test.ts` 與 `tests/test_cross_lang_contract.py` 共讀
> - CI 的 paths 是兩個 job 的聯集，改 `web/**` 也會跑 pytest ——
>   否則只同步 TS 端仍會漏掉另一半，正是本段擔心的失效模式
>
> 「只由人的注意力維持」現在改由 CI 維持；下列三條做法仍然成立、且仍是必要條件。

- 同語言內的重複一律消除（`_norm_raw_url` / `_norm_url` → `utils.normalize_url_light()`）
- 跨語言的在兩邊互相 cross-reference 註解，寫明已知差異與實測數據
- 加 AST meta-test 擋「新增第 N+1 個呼叫點」——逐一守住現況的測試對此完全無感

## 驗證方法論（這輪最貴的教訓）

簡→繁修正表歷經 **6 種量測法**，前 5 種每一種都宣告過「新造錯字 0」：

| 量測法 | 宣告 | 被下一種找到 |
|---|---|---|
| 從自己修正表導出黑名單 | 0 | 11 處 |
| target-side 掃 60 個變體字 | 11 | — |
| 字元多重集差 + `s2tw(t2s(T))!=T` 收斂 | 0 | 5 處 |
| 位置級 difflib 對齊 + 三層分類 | 5 | — |
| 變體家族 + 參考語料詞頻 | 0 | 自陳只獨立抓到 3/5 |
| **provenance 分區 + 逐句人工判讀** | **0** | ✅ 站住 |

每種在自己的假設之內都嚴謹，盲點都在假設之外。最後站住的那種**放棄「先篩哪些字可疑」**，改成先用位置級對齊分辨「哪些輸出位置是本 pass 產生的」，再不篩字元、全部讀過去，並用未變更語料當裁判集。

三條衍生教訓已入 `lessons.md`：驗收標準不可從自己的修法導出、mutation 前後必清 `__pycache__`、`git diff --name-only` 對非 ASCII 檔名的假綠燈。

## 數字

| 項目 | 前 | 後 |
|---|---|---|
| HF 摘要黏字 | 192 | 0 |
| HTML entity | 340 | 0 |
| 媒體標記 | 319 | 0 |
| `data/scored` ↔ `data/raw` 一致率 | 97.46% | **100.00%** |
| 讀取一輪 round-trip 漂移 | 731 欄位 (3.00%) | 0 |
| 歧義字 `譭齣穀俬孃衚衕剋閤几后` | 各有殘留 | **全歸零** |
| 測試 | 495 | 841 |

## 未解決

- **根因還在 Layer A**：`to_traditional`（s2twp，所有新資料的生產路徑）每天仍在產 `更复杂→更復雜`、`死胡同→死衚衕`、`克制→剋制`。變體表放在修復層只能補歷史。使用者已裁示把安全子集搬到 `utils` 與 `_TERM_FIXES` 並排無條件套用，另開一輪執行
- **`併發布` 是 `_TYPO_FIXES` 唯一有已知碰撞面的條目**（`高併發布局`），刻意保留且刻意沒加 guard 測試（會 FAIL），是全表唯一靠文件而非測試守住的例外
- 約 32 處既有錯字落在純繁體欄位，守門永遠碰不到（無守門表已處理其中一部分）
