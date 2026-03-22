## [2026-03-22]
### Added
- GitHub Actions daily pipeline workflow（UTC 18:00 = 台灣 02:00 自動執行 collect → score → generate，結果 commit 回 repo）
- GitHub Actions monthly cleanup workflow（每月 1 號自動清理 90 天前資料）
- 支援 `workflow_dispatch` 手動觸發，可指定日期與 `--force` 重跑

### Changed
- `.gitignore`: `data/` 和 `output/` 改為追蹤（排除 `health/`、`notes/`、`prompts/`），讓 Actions 產出可 commit 回 repo
### Fixed
- RSS/Blog collector `min_len` 500 → 1000，修復 The Verge AI 等 ~683 字元摘要不觸發 fetch fallback 的問題

### Changed
- `src/utils.py`: `import time` 移至檔案頂部；`_get_openrouter_client()` 改接收 `or_cfg` 參數，去除重複 `load_config()` 呼叫
