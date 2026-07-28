# 抽取失敗回退預設值：HF collector 的三個靜默 bug

日期：2026-07-28
相關 commit：`2c7cd40`
前情：[2026-07-27 三個靜默內容品質 bug](2026-07-27-silent-content-quality-bugs.md)（同樣是靜默失效，但機制不同——那次是「單側正確」，這次是「回退預設值」）

## 問題

使用者的原始回報只有一句話：**「Papers tab 的每一篇 paper box 比其他分頁來的長」**。

從這個純視覺症狀往下挖，挖出三個互不相關、都不會報錯的 collector bug。

## 三個 root cause

### 1. `get_text(strip=True)` 吃掉節點間空白

HF 論文頁的 abstract `<p>` 被拆成 **1797 個逐字元 text node**（前端逐字渲染）。BeautifulSoup 的 `get_text(strip=True)` 會對每個 node 各自 strip 再**無縫串接**：

```
strip=True      : 'WeintroduceSANA-Video2.0,ahybridvideodiffusiontransformer...'
get_text(" ")   : 'W e i n t r o d u c e S A N A ...'        ← 反向踩雷
" ".join(split) : 'We introduce SANA-Video 2.0, a hybrid ...'  ← 正解
```

這個 160 字元的不可斷字長 token 讓 grid `1fr` 欄從 952px 被撐到 1292px，整頁橫向溢出（`scrollWidth 1692 > viewport 1440`）——就是使用者看到的「box 比較長」。

判斷是否踩到這個坑：`len(list(el.strings))` 遠大於單字數，就代表節點被逐字/逐字元拆過。

### 2. selector 失配 + 預設值 = 永久靜默

```python
upvote_el = article.select_one("[class*='upvote'], button")   # 改版後永遠 None
upvotes = 0                                                    # ← 就這樣沿用了
if upvote_el:
    ...
```

HF 改版後票數移進 `[role="checkbox"] .leading-none`，卡片裡既無 `button` 也無帶 `upvote` 的 class。selector 落空 → `upvotes` 固定 0，**沒有 log、沒有例外、CI 全綠**。而 hf 清單正是依 upvotes 排序，等於該排序長期完全失效。

### 3. status 200 不代表拿到你要的那一頁

HF 在沒有當日論文時（週末）**不回 404**，而是 302 到最近有資料的日期並回 200：

```
?date=2026-07-25 → 302 → /papers/date/2026-07-24, articles=22
?date=2026-07-26 → 302 → /papers/date/2026-07-24, articles=22   ← 同一批
```

collector 只檢查 `status_code`，於是 07-24 的論文被標成 07-25、07-26 的內容。`follow_redirects=True` 讓轉址完全隱形——httpx 要看 `resp.url` 或 `resp.history` 才知道被轉過。

（順帶一提：未來日期其實是回 **400**，原本就擋掉了。這點與最初的推測相反，實測才確認。）

## 可複用規則

1. **抽取 HTML 文字一律用 `" ".join(el.get_text().split())`**——不要用 `strip=True`，也不要用 separator。前者吃空白、後者在逐字元 DOM 上插滿空白
2. **有 fallback 預設值的欄位，走 fallback 時必須記 log**——否則來源站改版時整個欄位歸零，pipeline 照跑照 commit。稽核方式：對已存檔資料做 sanity check（某欄位是否 100% 等於預設值），比讀程式碼快得多
3. **帶日期/分頁參數的抓取要驗證「拿回來的真的是我要的那一頁」**——status 200 只代表伺服器有回應，不代表內容對
4. **時間敏感的訊號要在正確的時間點抓**——HF 票數在論文發布當下幾乎是 0（pipeline 跑凌晨 2 點），拿當下的數字排序等於用雜訊排序。解法是隔日回補（`src/backfill.py`），不是在收集當下重試

## 附帶教訓：自動化的副作用會打到真實資料

第一版把自動補票掛在 `run_collect()`，結果 `pytest tests/` 走到那條路徑，**打了真實 HF 並改寫真實的 `data/raw/2026-07-20.json`**。

任何「會發網路請求 + 會寫檔」的邏輯掛進被測試覆蓋的函式前，先想清楚測試會不會走到。這裡的雙層防護：

- 掛在 `run_pipeline` 而非 `run_collect`（測試碰不到）
- `backfill_hf_upvotes()` 在 `PYTEST_CURRENT_TEST` 下直接 no-op，需 `AUTOPB_ALLOW_BACKFILL_IN_TESTS=1` 才解除

## 驗證方式

三個 bug 全部用**真實 HF 頁面**實跑驗證，不靠 fixture：

- 四個日期的轉址行為（`?date=` 07-24/25/26/27/28/30）
- 新舊 selector 並排跑同一頁面：`old=0 new=48 / old=0 new=32 / ...`，新值嚴格遞減且與頁面排序一致
- 修正後的 abstract：`len=1797, 空白數=246`
- 版面用 Playwright 開**真實 build 產物**量 `scrollWidth` / 欄寬 / 卡片高度，並往 DOM 塞 300 字元無空白 token 做壓力測試
