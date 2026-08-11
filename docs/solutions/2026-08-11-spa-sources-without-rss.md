# 官網是 SPA 又沒有 RSS 時，怎麼把它變成 collector

2026-08-11。接中國 AI 實驗室官方 blog（Qwen / MiniMax / DeepSeek / Kimi）時整理出的流程。

## 問題

要新增的四個來源官網都是 CSR SPA：`rss.xml` / `feed.xml` / `atom.xml` 全部 404，
既有的 `blog_collector`（先探 RSS、失敗才爬 HTML）對它們一律回 0 筆。
表面結論是「這些來源接不了」——但實際上四家有三種不同的可用路徑。

## 探測順序（由便宜到貴）

1. **`curl` 常見 feed 路徑**：`/rss.xml`、`/feed`、`/index.xml`、`/atom.xml`。
   命中就結束——但**要看最新一篇的日期，不是看 HTTP 狀態**。
   `qwenlm.github.io/blog/index.xml` 回 200 且有 44 篇，看起來完全正常，
   實際上 2025-09-23 之後就停更了，比官方 API 少 8 篇。
2. **`curl` 首頁 HTML，grep 資料痕跡**：`__NEXT_DATA__`、`self.__next_f`、
   `__NUXT__`、`window.__INITIAL_STATE__`、`"title"`。
   有 `__NEXT_DATA__` 或 `__NUXT__` → 資料是完整 JSON，好解；
   只有 `self.__next_f`（Next.js App Router 的 RSC flight payload）→ 資料被切成
   字串片段，解析很脆，通常不值得（智譜 `zhipuai.cn` 就卡在這裡）。
3. **playwright 開頁面看 network requests**：這一步才是真正找 API 的地方。
   MiniMax 的 `minimax.io/api/news?page=1&locale=en` 就是這樣抓到的。
   看不到任何內容請求、只有埋點（`mcs.zijieapi.com`）→ 資料是 SSR 或 RSC 塞在
   HTML 裡，回第 2 步；兩步都落空就放棄（ByteDance Seed）。
4. **playwright snapshot 比對原始 HTML**：頁面上「看得到但 grep 不到」的欄位，
   多半是格式沒對上而不是真的不存在。Kimi 的日期就是這樣——先前搜
   `20\d{2}-\d{2}-\d{2}` 全落空，以為要靠瀏覽器才拿得到，實際上原始 HTML 裡
   有 39 個 `2026/07/16`，只是分隔符是斜線。

## 拿到端點之後必查的三件事

**① 連結欄位一律實打一次 HTTP。** Qwen 每篇的 `canonical` 指向
`qwenlm.github.io/blog/{path}`，看起來最正統，實測全部 404（那個站已停更，
CMS 樣板沒改）。要組 `qwen.ai/blog?id={path}`。照抄 canonical 等於整批死連結。

**② 掃整份回應的欄位型別，不要只看第一筆。** MiniMax 的 `publishDate` 在同一頁
回應裡，新文章是毫秒 epoch 整數、2026-05 以前是 ISO 8601 字串。只寫 int 版本
會在跑進舊文時整個 provider 拋例外。

```python
for e in data["data"]:
    print(type(e["publishDate"]).__name__, repr(e["publishDate"]))
```

**③ 日期字串要看上下文再採信。** Kimi 文章頁裡的 `2026-07-17` 全部出自圖片 CDN
路徑（`kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/2/2026-07-17/...`），那是素材
上傳日。真正的發布日只在索引頁卡片上，而且是另一天（`2026/07/16`）。
判斷方法是把 match 前後 90 字元印出來看，不要只看 regex 命中。

## DOM 配對：只上溯一層

Kimi 的卡片結構是 `div > [a.absolute（覆蓋整片的連結）, div.card-body > h4 + p]`
——連結與標題是**兄弟**不是父子。從 `.card-body` 往上找 `a` 時只能看一層：
再往上就會跨到別張卡片，把 2024 年那些連到 arXiv 的舊卡片配上隔壁的 `/blog/`
連結（實測 19 張卡片中有 11 張被錯配到同一個 href）。

## 收尾：新 SourceType 的白名單掃描

新增 `SourceType.CN_LABS` 後四家都收得到、organization 也推得出來，但一篇都沒進
pinned——`src/pinned.py` 的 `select_pinned()` 用白名單過濾
`it.source in (SourceType.RSS, SourceType.BLOG)`，新值不在裡面就靜默落空，
沒有例外、沒有 log，看起來只像「今天剛好沒有官方文」。

加新 enum 值時 `grep -rn 'SourceType.BLOG'` 掃一遍所有列舉處。白名單式過濾對
新值的預設是「排除」，而排除不會報錯。
