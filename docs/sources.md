# 資料來源清單

最後更新：2026-08-11。新增 collector 時同步更新本檔（endpoint 以程式碼為準，本檔只是索引）。

## Collector 總表

「走向」：**清單**＝退出評分、只排序成 `output/lists/{date}.json`；**評分**＝進規則預篩 → LLM 5D 評分 → top-K 生成；命中 `pinned_organizations` 者免評分直接生成。

| Collector | 走向 | Endpoint | 備註 |
|---|---|---|---|
| `rss` | 評分 | 26 個 feed（見下） | 收得最多的來源 |
| `arxiv` | 清單 | `arxiv` PyPI 套件（底層 `export.arxiv.org/api/query`） | cs.AI / cs.CL / cs.LG / cs.CV，max 50 |
| `semantic_scholar` | 清單 | `api.semanticscholar.org/graph/v1/paper/search/bulk` | 6 query、近 3 天、limit 30；無 key 也能用但限流嚴 |
| `github` | 清單 | `github.com/trending/{lang}?since=daily`（HTML） | python / typescript / rust |
| `hf_papers` | 清單 | `huggingface.co/papers?date=`（HTML）+ `export.arxiv.org/api/query` 補摘要 | 票數隔日才沉澱，`backfill.py` 每天回補前一天 |
| `newsapi` | 評分 | `newsapi.org/v2/everything` | 需 key；免費方案 ~24h 延遲，`lag_days: 2` |
| `hackernews` | 評分 | `hn.algolia.com/api/v1/search` | 12 query、≥50 points |
| `blogs` | 評分 | 10 個個人站首頁（先探 RSS，失敗才爬 HTML） | 見下 |
| `cn_labs` | 評分（多為 pinned） | 4 個 provider（見下） | 2026-08-11 新增 |
| `chatpaper` | 清單 | `chatpaper.com/api/v1/articles/list` | 回應為加密 binary，`parse_response()` 解密；2026-05-26～08-10 靜默斷線 78 天，已於 2026-08-11 修復 |
| `reddit` | 評分 | `old.reddit.com/r/{sub}/top/.json` | **GitHub Actions 上 403**（datacenter IP 被擋），只在本機有資料 |

## RSS feeds（26）

| 名稱 | URL |
|---|---|
| TechCrunch AI | `https://techcrunch.com/category/artificial-intelligence/feed/` |
| The Verge AI | `https://www.theverge.com/rss/ai-artificial-intelligence/index.xml` |
| OpenAI Blog | `https://openai.com/blog/rss.xml` |
| Google AI Blog | `https://blog.google/technology/ai/rss/` |
| HN AI | `https://hnrss.org/newest?q=AI+LLM+GPT+agent` |
| HuggingFace Blog | `https://huggingface.co/blog/feed.xml` |
| Google Research | `https://blog.research.google/feeds/posts/default` |
| MarkTechPost | `https://www.marktechpost.com/feed/` |
| VentureBeat AI | `https://venturebeat.com/category/ai/feed/` |
| KDnuggets | `https://www.kdnuggets.com/feed` |
| Anthropic Engineering | `https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_engineering.xml` |
| Anthropic Research | `https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_research.xml` |
| Anthropic News | `https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_news.xml` |
| Claude Blog | `https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_claude.xml` |
| Meta AI Research | `https://engineering.fb.com/category/ai-research/feed/` |
| Apple ML | `https://machinelearning.apple.com/rss.xml` |
| NVIDIA Developer | `https://developer.nvidia.com/blog/feed/` |
| AWS ML | `https://aws.amazon.com/blogs/machine-learning/feed/` |
| BAIR | `https://bair.berkeley.edu/blog/feed.xml` |
| Interconnects | `https://www.interconnects.ai/feed` |
| Import AI | `https://jack-clark.net/feed/` |
| The Gradient | `https://thegradient.pub/rss/` |
| Dwarkesh | `https://www.dwarkesh.com/feed` |
| Max Woolf | `https://minimaxir.com/index.xml` |
| 量子位 | `https://www.qbitai.com/feed` |
| Recode China AI | `https://recodechinaai.substack.com/feed` |

Anthropic 那四條走 `Olshansk/rss-feeds` 鏡像（官方站無 RSS）。因為 netloc 是
`raw.githubusercontent.com`，`infer_organization()` 的網域比對必然落空，只能靠
feed name 命中 `_NAME_TO_ORG`——名稱改了就推不出 organization、不會進 pinned。

Import AI 用原始發布站 `jack-clark.net`，不是 substack 鏡像：後者在 Cloudflare
挑戰後面，會對 Python client 的 TLS 指紋回 403（換 UA / 開 HTTP2 都無效）。

## 個人 blog（10）

先依序探測 RSS，全部落空才退回爬 HTML。

| 名稱 | 索引頁 |
|---|---|
| Naval Ravikant | `https://nav.al/` |
| Andrej Karpathy | `https://karpathy.github.io/` |
| 寶玉 baoyu.io | `https://baoyu.io/` |
| Lilian Weng (OpenAI) | `https://lilianweng.github.io/` |
| Jay Alammar | `https://jalammar.github.io/` |
| Sebastian Raschka | `https://magazine.sebastianraschka.com/` |
| Simon Willison | `https://simonwillison.net/` |
| Eugene Yan | `https://eugeneyan.com/` |
| Hamel Husain | `https://hamel.dev/` |
| Latent Space | `https://www.latent.space/` |

## cn_labs — 中國 AI 實驗室官方 blog（4）

四家官網都是 CSR SPA，既無 RSS 也爬不到 HTML，只能打前端自用的端點。
四家的 organization 都在 `pinned_organizations` 裡，命中即免評分置頂生成。

| Provider | 端點 | organization | 日期怎麼來 |
|---|---|---|---|
| `qwen` | `https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=zh-CN` | Alibaba | content 那頁 HTML 的 `article:published_time` meta |
| `minimax` | `https://www.minimax.io/api/news?page=1&locale=en` | MiniMax | `publishDate`，**同欄位混用 ms epoch int 與 ISO 字串** |
| `deepseek` | `https://api-docs.deepseek.com/news/` | DeepSeek | slug 內嵌（`news260424` = 2026-04-24） |
| `kimi` | `https://www.kimi.com/blog/` | Moonshot AI | 索引頁卡片的 `.card-date`（`2026/07/16`） |

三個一定要記得的地雷：

- **Qwen 的文章 URL 不可用 content 裡的 canonical**。canonical 指向
  `qwenlm.github.io`，那個 Hugo 靜態站 2025-09-23 之後停更，新文章一律 404
  （RSS 仍回 200 且有 44 篇舊文，看起來完全正常）。要組 `https://qwen.ai/blog?id={path}`。
- **Kimi 文章頁裡的日期字串全是圖片 CDN 的上傳日**
  （`kimi-file.moonshot.cn/.../2026-07-17/`），拿去當發布日會系統性偏移。
- **DeepSeek 2024 年的公告是四碼 `newsMMDD`**，年份不在 slug 也不在頁面上，一律跳過。

## 評估過但未採用

避免重複踩同一輪。實測日期 2026-08-11。

| 來源 | 為什麼不用 |
|---|---|
| `deepseek.ai/blog` | **不是官方**。自己的 meta 寫「Independent DeepSeek AI blog」，掛 Vercel，5 篇 SEO 科普文。官方是 `api-docs.deepseek.com/news/` |
| 智譜（`zhipuai.cn/news`） | 內容埋在 Next.js RSC flight payload，無乾淨端點。`z.ai/blog` 是 404，`z.ai` 導向 chat 產品頁 |
| ByteDance Seed | 前端只有埋點請求（`mcs.zijieapi.com`），HTML 也不含資料 |
| `qwenlm.github.io/blog/index.xml` | RSS 仍回 44 items 但**已停更**，最新 2025-09-23。API 有 8 篇它沒有 |
| ChinAI（`chinai.substack.com/feed`） | 回 200 但 0 item，與 Import AI 同一個 Cloudflare 坑 |
| 騰訊混元 / Moonshot 舊網域 / StepFun / InternLM / OpenBMB / BAAI / 機器之心 | `rss.xml` 皆 404，或回 HTML 而非 feed |
