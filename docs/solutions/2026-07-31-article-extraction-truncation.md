# 外部文章正文抓取被系統性截斷（2026-07-31）

## 問題

使用者回報某篇 TechCrunch 貼文的「原始文章」被截斷。實際查下去不是個案：
**當日 18 個 RSS 來源的 abstract 全部恰好 2000 字元且斷在句中**。

```
…I am not reporting you to HQ — what you did is competitive, not
                                                                 ^ 就這樣沒了
```

## Root cause

三個獨立缺陷疊在同一條路徑上，只修任何一個症狀都會復發。

### ① 容器選擇踩了 `select_one` 的文件順序（最不顯而易見）

原本的寫法把一整串 selector 丟給 `select_one`，並在註解裡表達「由精確到泛用」的優先序：

```python
body = soup.select_one(
    "article, .post-content, .entry-content, main, .content, "
    "[role='main'], .article-body, …"
)
```

但 **CSS `select_one` 回傳的是文件順序第一個 match，不是 selector 列表順序第一個**。
而外層容器在 DOM 中必然排在內層之前——`main` 是 `.entry-content` 的祖先，
祖先永遠先出現。於是：

- selector 列表的順序**完全沒有作用**
- 每個站都選到最外層容器，把推薦區、Topics、Most Popular 一起吃進正文
- **沒有任何 log、沒有 exception**，只是內容悄悄變髒

實測（同一頁、同一支提取函式）：

| 站 | 選到的（`main`） | 應該選的 | 差額＝雜訊 |
|---|---|---|---|
| TechCrunch | 7646 | `.entry-content` 6388 | 1258 |
| The Verge | 10331 | `article` 9027 | 1304 |

**修法**：按列表順序**逐一** `select_one`，取第一個內容夠長（≥200 字元）的。

### ② `text[:max_chars]` 硬切

純字元切片，不看句界，必然切在單字或引號中間。

**修法**：`truncate_at_boundary()`，句界（含中文 `。！？`）→ 詞界回退。
關鍵細節是**回退幅度要有下限**（`_BOUNDARY_MIN_RATIO = 0.6`）：整段沒有標點的
文本若無腦退到最近句界，會被砍到只剩開頭一句，比硬切更糟。

### ③ 上限寫死在函式預設參數

`max_len: int = 2000` 寫死，`config.yaml` 完全碰不到。改由
`collectors.abstract_max_chars` 控制，預設 8000（一般新聞全文約 3000-9000 字元）。

放寬前先確認成本：`scorer.py` 本來就自帶 `[:1500]`，評分 prompt 不受影響；
真正受益的是 `blog_post.py` 的生成 prompt，它用完整 abstract。

## 雜訊剝除要兩層（單靠 class 關鍵字不夠）

第一層是 class/id 語意關鍵字（`[class*='related']`、`newsletter`、`share`…）。

但這對 **CSS-module / Next.js 的雜湊類名完全無效**：

```html
<div class="LinkGrid-module-scss-module__wTN57W__intro"><h2>Related content</h2>
```

Anthropic、The Verge 都是這樣。所以第二層改用**尾段標題啟發式**：h1-h4 的文字
命中「Related content / Most popular / …」且**位於全文 60% 之後**才剝除——
位置門檻是為了不誤殺正文中段真的在討論熱門模型的同名小標。

### 這裡踩了一次自傷，值得單獨記

剝除時要決定「移除哪個節點」。第一版無腦上溯到容器的直接子節點：

```python
node = heading
while node.parent is not None and node.parent is not container:
    node = node.parent          # ← 一路上溯到頂
```

The Verge 的 `h2 "Most Popular"` 距容器 **8 層**，上溯後那個直接子節點正是
`entry-body-container`——**整篇 8131 字元的正文**。結果正文只剩 506 字元。

修法是上溯時檢查祖先文字量，一旦大到裝得下 heading 之前的正文就停手：

```python
tail_budget = (len(full_text) - position) * 1.2 + 50
while node.parent is not None and node.parent is not container:
    if len(node.parent.get_text(" ", strip=True)) > tail_budget:
        break               # 這個祖先已經含正文，不是推薦區
    node = node.parent
```

## 可複用 pattern

### 「長度聚集在單一值」是硬切的指紋

修完 rss 之後要確認其他 source 有沒有同樣問題。與其逐個讀程式碼，更快的是
**對 `data/raw` 全量統計每個 source 的 abstract 長度分佈，看有沒有異常聚集**：

```python
c = collections.Counter(lengths)
top, cnt = c.most_common(1)[0]
if cnt / len(lengths) > 0.10:
    print(f"{cnt/len(lengths)*100:.1f}% 卡在 {top}")   # ← 硬切嫌疑
```

結果：

| source | 撞頂比例 | 判定 |
|---|---|---|
| rss | 69.9% @ 2000 | 本次修復 |
| **github** | **91.6% @ 1500** | `readme_text[:1500]`，補修 |
| **reddit** | **36.6% @ 500** | `selftext[:500]`，補修 |
| hackernews | 24.6% @ 1542 | ＝1500 + engagement 後綴 |
| arxiv / chatpaper / hf_papers / semantic_scholar | 無聚集 | API 直供完整摘要，乾淨 |

反證也靠這份資料：arxiv `max=2438 > 2000` 直接證明它沒有 2000 上限；
chatpaper 最常見長度只佔 0.3%，分佈自然。

### 分佈同時能區分「我方截斷」與「上游就短」

`newsapi` median 258 / max 260，**遠低於程式裡的 `[:500]`**——代表那個 slice
從未生效，短的原因是上游 NewsAPI 免費方案的 `description` 本身就是摘要。
同樣是「內容不完整」，但**不是同一類 bug**，修法完全不同（要補抓文章 URL，
屬功能增強）。沒有這份分佈就會誤修。

### 同一個 bug 常有多份複製

`blog_collector._scrape_html` 藏著第三份：自帶 `select_one("article, .post-content,
.entry-content, main")`（同樣的祖先優先坑）、只取前 3 個 `<p>`、再 `[:1000]` 硬切。
找到 root cause 後要 grep 整個 `src/` 確認沒有平行實作，而不是只修呼叫鏈上那一處。

## 驗證

- **897 passed**，新增 20 個離線測試（`tests/test_collectors/test_article_extraction.py`）
- 真實網頁對照四種 CMS：TechCrunch 2000→6388、The Verge→7992、Anthropic→3223、
  KDnuggets→7978，四站零雜訊殘留且都在句界收尾
- **實跑 collector 打真實 feed** 收 40 篇：median 3881，**36 篇（90%）在舊制會被腰斬**

## 未做

歷史資料未回填（使用者裁示「既往不究」）。`data/raw` 裡既有的 abstract 仍是
被截斷的版本，新邏輯只影響往後的收集。
