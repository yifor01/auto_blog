## [RSS] min_len 門檻須匹配實際 feed 長度
- **Date**: 2026-03-22
- **Problem**: The Verge AI RSS summary 穩定 ~683 chars，但 min_len=500 導致 fetch fallback 不觸發
- **Cause**: min_len 設太低，介於 RSS summary 原始長度之下，所以短摘要被誤判為「夠長」
- **Fix**: min_len 500 → 1000（rss_collector.py 預設值 + blog_collector.py 硬編碼）
- **Lesson**: 設定 min_len 門檻時，先調查各來源的典型 summary 長度，門檻應高於最長的「不夠好」摘要
