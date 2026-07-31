# 兩種靜默失敗，以及為什麼「加強 error handling」對它們都沒用

Date: 2026-07-31
Commits: `3e027c4`（newsapi）、`7b0c741`（blog collector）
相關：`docs/solutions/2026-07-31-article-extraction-truncation.md`（同一週的第三個靜默失敗）

本專案栽在「靜默失敗」的形狀已經第四次了（HN Algolia 改規則歸零、HF collector 三個預設值、
外部正文截斷、本次兩個）。這次的兩個剛好是**兩種不同的靜默機制**，值得一起記。

## 形狀 A：合法的空回應（newsapi）

`data/raw` 裡 newsapi **118 天中 116 天為 0 筆**，log 只寫 `count: 0`，無 error、CI 全綠。

表面症狀完美吻合「錯誤被吞掉」——程式碼裡確實有個 `except Exception` 把錯誤寫成 log。
順手的修法是加強 error handling。**那完全沒用。**

```
GET /v2/everything?from=<今天>&to=<明天>  →  HTTP 200
{"status": "ok", "totalResults": 0, "articles": []}
```

免費 Developer 方案的文章有 ~24 小時延遲。回應是**完全合法的空結果**，
`raise_for_status()` 不會叫、`except` 抓不到、schema 驗證也會過。

### 診斷的決定性一步：掃日期分佈，不是讀程式碼

```
T-0 = 0    T-1 = 15    T-2 = 82    T-3 = 85
```

一眼看出是時間軸問題而非邏輯問題。**打 API 掃參數空間比讀 collector 原始碼快一個數量級**，
因為要證偽的是「我方程式碼有 bug」這個預設。

### 第二個決定性線索：例外指出根因

118 天裡唯二有資料的 07-08（28 筆）、07-10（4 筆）。`git log` 顯示這兩個檔案都是
`chore: pipeline 2026-07-11` 寫入的——**07-11 那次 catchup 補跑「過去日期」**。

查過去日期就有、查當天就沒有。異常樣本比正常樣本資訊量大得多。

## 形狀 B：錯誤位置誤導（blog collector）

Chip Huyen 的 abstract 全是 13–82 字元的 `"Title: {title}"` 佔位字串。

症狀寫著「正文抽取回空」，而 `extract_full_text_from_html()` **上週才剛因為 selector 問題被修過**
（見同目錄的截斷修復文件）。先入為主去查 selector 是最自然的動作。

實際跑一次：**HTTP 404**。抽取函式從頭到尾沒問題，它收到的是一個 GitHub Pages 的 404 頁面。

### 一個根因，三個症狀

```python
if href.startswith("/"):
    href = url.rstrip("/") + href       # url = "https://huyenchip.com/blog/"
```

`href` 是**根相對路徑**（`/2025/01/07/agents.html`），依 RFC 3986 必須接在 **origin** 上。
程式接的是索引頁 URL **含 `/blog` 路徑** → `https://huyenchip.com/blog/2025/...` → 404。

同一個錯法（`blog_collector.py:78` 的 RSS 探測也用它）串出三個表面不相關的症狀：

| # | 症狀 | 機制 |
|---|---|---|
| ① | 走了 HTML 抓取而非 RSS | 6 條 feed 路徑全拼成 `/blog/feed` → 全 404 |
| ② | abstract 是佔位字串，**且存檔的 url 是死連結** | 文章連結 404 → `content_abstract = ""` → `or f"Title: {title}"` |
| ③ | 2023–2025 舊文標成當天 | `_scrape_html` 寫 `published_date=target_date`，無日期過濾 |

改用 `urljoin` 後 `https://huyenchip.com/feed` 是 HTTP 200 的合法 feed，走 RSS 路徑就有
`parse_entry_date` 給的真實日期——**症狀 ③ 不必單獨修，跟著消失**。

## 可複用 pattern

1. **「0 筆」不等於「出錯」。** 外部 API 的空結果可能完全合法。要區分「我方沒收到」與
   「對方沒給」，唯一可靠的方式是打 API 掃參數空間，不是讀自己的程式碼。
2. **error handling 攔不到合法回應。** 症狀像「錯誤被吞掉」時，先確認錯誤真的存在。
   本例中就算把 `except Exception` 改成完美的錯誤處理，行為一模一樣。
3. **異常樣本比正常樣本值錢。** 116 天為 0 之中的那 2 天，直接指出「過去日期 vs 當天」的差異。
   查靜默歸零時先問「有沒有哪天不是 0，那天有什麼不同」。
4. **抽取類 bug 先印 `status_code`。** 「抽不到內容」有兩種：抽取邏輯錯、或根本沒抓到頁面。
   後者更常見也更便宜驗證。上週剛修過抽取邏輯這件事本身就是誤導源。
5. **修對之後數量變少也可能是對的。** huyenchip 修好後貢獻 0 筆——因為它停更 18 個月，
   7 天過濾正確擋掉。用「數量有沒有增加」當驗收標準會把正確結果判成失敗。
6. **URL 拼接一律 `urljoin`。** 手寫 `rstrip("/") + href` 在索引頁帶路徑時必錯，
   而多數來源的索引頁在網站根，所以這個 bug 會潛伏到某天新增一個帶路徑的來源。

## 修法上的一個取捨

RSS 探測**沒有**直接改成 origin-only，而是「每條路徑先試索引相對、再試 origin 相對並去重」。
理由：索引頁在網站根時兩種拼法相同，去重後探測次數與網址**完全不變**，10 個既有來源零行為改變
（由 `test_rss_probe_unchanged_for_root_level_blogs` 釘住）。只有帶路徑的來源會多打幾次。

修 bug 時能讓「沒中招的路徑」保持位元級不變，就不需要為它們重新建立信心。
