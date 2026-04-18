# CI/CD — GitHub Actions

Pipeline 可透過 GitHub Actions 每日自動執行，結果 commit 回 repo，本地 Dashboard `git pull` 後直接讀取。

## Workflows

| Workflow | 檔案 | 排程 | 說明 |
|----------|------|------|------|
| Daily Pipeline | `.github/workflows/daily-pipeline.yml` | UTC 18:00（台灣 02:00） | collect → score → generate，結果 commit 回 repo |
| Monthly Cleanup | `.github/workflows/monthly-cleanup.yml` | 每月 1 號 | `clean --keep-days 90 --auto`，清理舊資料 |

- 兩個 workflow 都支援 `workflow_dispatch` 手動觸發
- Daily Pipeline 可指定 `date` 和 `force` 參數
- Secrets 需在 GitHub Settings 設定：`AIHUBMIX_API_KEY_1`~`4`、`AIHUBMIX_API_URL`、`OPENROUTER_API_KEY`、`OPENROUTER_API_KEY_2`、`NEWSAPI_KEY`
- `data/` 和 `output/` 進 repo（排除 `data/health/`、`output/notes/`、`output/prompts/`）
- 本地 Dashboard：`git pull` → `python -m src.cli web`，checkpoint 機制自動跳過 Actions 已完成的 pipeline
- 注意：本地 `data/bookmarks.json` 若有變更，需先 commit/push 再 pull，避免 merge conflict

## 日常流程

```bash
# 1. 拉取 Actions 昨晚產出
git pull

# 2. 驗證結果正確性（每天必做）
python -m src.cli summary              # 檢查今日收集數量與評分分佈是否合理
python -m src.cli status               # 確認最近 7 天都有產出、無遺漏
ls -la data/scored/$(date +%Y-%m-%d).json   # 確認 scored 檔案存在且大小合理

# 3. 啟動 Dashboard 瀏覽
python -m src.cli web                  # 開啟 http://127.0.0.1:8555/dashboard
# → 檢查 Day Detail 頁：collector 來源數量、分數分佈是否正常
# → 抽查 2-3 篇 Blog 草稿品質（摘要完整性、LLM 評語合理性）

# 4. 若 Actions 失敗或結果異常 → 手動補跑
python -m src.cli run --date YYYY-MM-DD        # 補跑特定日期
# 或在 GitHub Actions 頁面 → Run workflow → 指定日期 + force=true
```

**異常排查重點**：
- 收集數量驟降 → 檢查 collector 來源是否掛掉（RSS URL 變更、API 限流）
- 評分全為 0 → 檢查 Actions log 中 LLM API 是否 429
- Blog 草稿品質差 → 檢查 `output/posts/` 內容，必要時 `--force` 重跑
