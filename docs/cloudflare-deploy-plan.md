# Daily Blog → Cloudflare 自動部署 Plan

> 建立日期：2026-06-03 ｜ 狀態：**程式碼已實作（Step 1-4, 6 完成），Step 5 待手動設定**
> 目標：`daily-pipeline.yml` 跑完後，自動把 blog markdown 變成網站並部署到 Cloudflare，**遠端（手機/外網）私人查看**。

## 實作紀錄（2026-06-03）

已完成 `web/`（Astro 5）+ workflow deploy job。與原計劃的偏離與擴充：

- **Step 1**：`create-astro@5` 要求 Node 22，但本機/CI 是 Node 20（Astro 5 runtime 本身支援 ^20.3.0，只有 scaffolding CLI 卡 Node 22）→ 改**手動 scaffold** minimal 骨架，不升 Node。
- **Step 2**：blogs 有 2 篇缺 `date`、且多 `score`/`source` 欄位 → schema 的 `date` 改 `optional()`，頁面從檔名 `YYYY-MM-DD` 前綴 fallback（`utils.ts` 的 `idDate`/`postDate`）。
- **擴充：兩個 collection + tab 分頁**
  - `blogs`（人工策展，`output/blogs`）：tag + 月份 + 搜尋 sidebar 篩選。
  - `posts`（每日自動，`output/posts`，2345 篇）：source + 月份 + 搜尋篩選，**只 build 近 `RECENT_DAYS`（30）天**避免 2000+ 頁拖累部署；UI 標明「近 30 天（全部 N 篇）」。
  - 頂部 `⚡ 每日自動` / `★ 精選` tab 切換（`components/Nav.astro`）。**首頁 `/` default 顯示每日自動**，`/curated` 為精選；詳情頁 `/daily/<id>`、`/blogs/<id>`。
- **資料 bug 修復**：`output/blogs` 是**人工策展**、不由 pipeline 產；pipeline 每日產的是 `output/posts`。發現 `src/generators/blog_post.py` 用 f-string 組 frontmatter，標題含 `"` 時產生不合法 YAML（5 個既有檔受害，已修）→ 改用 `yaml.safe_dump`。
- **Step 4**：本機 build 814 頁通過、瀏覽器實測列表/內頁/篩選/tab 皆正常、零 console error。
- **Step 5**：Cloudflare dashboard 設定（建 Pages project、API token、Access）仍需手動，見下。
- **Step 5/6（改用 CF Git 整合）**：捨棄原計劃的 wrangler-action + Direct Upload，改用 **Cloudflare 連 GitHub 自動建置**——CF 偵測 push 自動 build + 部署，不需 API token/secrets、不需 workflow deploy job（已從 `daily-pipeline.yml` 移除）。每次 push 觸發重建（每日資料 commit ≈ 每日一次 build）。
  - ⚠️ 新版 CF「Connect to Git」預設建的是 **Worker**（非 Pages），介面是 `Build command` + `Deploy command: npx wrangler deploy`（沒有 Build output directory 欄位）。故採 **Workers Static Assets**：加 `web/wrangler.toml`（`name` + `compatibility_date` + `[assets] directory=./dist`），由 `wrangler deploy` 把 `dist/` 當靜態站部署。
  - CF build 設定：**Path/Root directory=`web`**（漏填會在 repo 根目錄跑 `pip install .` + `npm run build` 找不到 package.json 而失敗）、Build command=`npm run build`、Deploy command=`npx wrangler deploy`、Node 由 `web/.nvmrc`(=20) 控制。
  - `wrangler.toml` 的 `name` 必須與 CF 上建立的 Worker 同名。

> ⚠️ 未來新增 collection / 改 `RECENT_DAYS` 時記得：glob loader 會載入**全部** posts（日期篩選在 load 之後），所以任何一個壞 YAML 檔都會中斷 build。

## 已定案的架構決策

| 項目 | 選擇 | 理由 |
|---|---|---|
| SSG | **Astro 5** | blog 原生、build 快、Cloudflare 一等支援、content layer 可直接 glob 既有 markdown |
| 部署平台 | **Cloudflare Pages** | 純靜態、免費額度大、固定 `*.pages.dev` 網址 |
| 存取保護 | **Cloudflare Access**（Zero Trust，免費） | 綁定本人 email/Google，別人有連結也看不到 |
| 觸發方式 | 沿用 `daily-pipeline.yml`，跑完接一個 deploy job | 單一 workflow、零手動 |
| 後端 | **無 runtime**（同 taiwan-ai-prof） | FastAPI/pipeline 只在 CI 跑，不部署，零維運 |

資料流：
```
daily-pipeline.yml (cron 每天 UTC18:00)
  ├─ Python pipeline → output/blogs/*.md  (現況已有)
  ├─ Commit results                        (現況已有)
  └─ [新增] deploy job:
        Astro build (glob 讀 output/blogs) → web/dist/
        wrangler pages deploy → Cloudflare Pages
```

## 現有素材（已確認）

- blog markdown：`output/blogs/2026-03-04_saarthi-agi.md`（檔名 `YYYY-MM-DD_slug.md`）
- frontmatter 欄位：
  ```yaml
  title: "..."          # 必填
  date: "2026-03-02"    # 字串，schema 要 coerce.date()
  paper_url: "..."      # optional
  paper_title: "..."    # optional
  tags: [Agent, ...]    # array, optional
  tldr: "..."           # optional
  ```
- 其他可上站的內容：`output/digests/`（每日 digest）、`output/posts/`、`output/notes/`（第二期再加）
- workflow：`.github/workflows/daily-pipeline.yml`（已有 `permissions: contents: write`、commit step）

## 實作步驟

### 1. 建立 Astro 專案（`web/`）
```bash
cd ~/projects/auto_post_blog
npm create astro@latest web -- --template minimal --no-install --no-git --typescript strict
cd web && npm install
```

### 2. Content collection schema（`web/src/content.config.ts`）
用 Astro 5 content layer glob loader **直接指向既有 markdown，免 copy**：
```ts
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blogs = defineCollection({
  loader: glob({ pattern: '*.md', base: '../output/blogs' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    paper_url: z.string().optional(),
    paper_title: z.string().optional(),
    tags: z.array(z.string()).default([]),
    tldr: z.string().optional(),
  }),
});

export const collections = { blogs };
```
> ⚠️ slug 來自檔名 `YYYY-MM-DD_slug`，含底線 ok；如要乾淨 URL 可在 page 做 `id.split('_').slice(1).join('-')`。

### 3. 頁面
- `web/src/pages/index.astro`：依 `date` 降序列出全部 blog（title + date + tldr + tags），連到內頁。
- `web/src/pages/blogs/[...slug].astro`：`getStaticPaths()` 渲染 `<Content />`（markdown body）。
- 樣式：暗色、單欄、可讀寬度即可（第一版不用花俏）。

### 4. 本機驗證
```bash
cd web && npm run build && npm run preview
# 確認列表有文章、內頁 markdown 正常渲染、tags 顯示
```

### 5. Cloudflare 一次性設定（手動，只做一次）
1. **建 Pages project**：Cloudflare dashboard → Workers & Pages → Create → Pages → 取名 `auto-post-blog`（先 Direct Upload，不接 Git）。
2. **API Token**：My Profile → API Tokens → Create → 用 "Cloudflare Pages: Edit" 模板 → 複製 token。
3. **Account ID**：dashboard 右側欄複製。
4. **GitHub Secrets**（repo Settings → Secrets → Actions）新增：
   - `CLOUDFLARE_API_TOKEN`
   - `CLOUDFLARE_ACCOUNT_ID`
5. **Cloudflare Access（私人保護）**：Zero Trust → Access → Applications → Add → Self-hosted → domain 填 `auto-post-blog.pages.dev` → Policy：Action=Allow, Include=Emails=你的 email。儲存後訪問該站需登入。

### 6. 接上 workflow（改 `daily-pipeline.yml`）
在現有 `pipeline` job 之後新增 deploy job（checkout 會抓到剛 commit 的最新 md）：
```yaml
  deploy:
    needs: pipeline
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
          cache-dependency-path: web/package-lock.json
      - name: Build site
        run: cd web && npm ci && npm run build
      - name: Deploy to Cloudflare Pages
        uses: cloudflare/wrangler-action@v3
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          accountId: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
          command: pages deploy web/dist --project-name=auto-post-blog
```
> 也加進 `workflow_dispatch` 手動觸發測試（已有），或 deploy job 加 `on: workflow_dispatch` 單獨測。

### 7. 驗證
- 手動觸發 workflow（`workflow_dispatch`）→ 看 deploy job 綠燈 → 開 `https://auto-post-blog.pages.dev` → 應跳 Cloudflare Access 登入 → 登入後看到 blog 列表。

## 後續可擴充（非第一版）
- [ ] digests / posts 各自 collection + 分頁
- [ ] RSS（`@astrojs/rss`）
- [ ] tag 篩選頁
- [ ] 自訂網域（CF Pages → Custom domains）
- [ ] 列表分頁 / 搜尋

## 注意事項
- `web/` 要進 git；`web/node_modules`、`web/dist` 加進 `.gitignore`。
- Astro content layer 的 `base: '../output/blogs'` 是相對 `web/`，CI checkout 後路徑成立。
- FastAPI 完全不部署，沿用 taiwan-ai-prof「Python 只在 CI/本機跑」模式。
