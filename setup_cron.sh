#!/usr/bin/env bash
# Auto Post Blog — Cron 設定腳本
# 功能:
#   1. 建立每日執行腳本 (含 catch-up 補跑)
#   2. 設定 cron job
#   3. 設定開機自動補跑 (@reboot)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV="$SCRIPT_DIR/.venv"
LOG_DIR="$SCRIPT_DIR/logs"

mkdir -p "$LOG_DIR"

# 建立每日執行腳本
cat > "$SCRIPT_DIR/run_daily.sh" << 'RUNNER'
#!/usr/bin/env bash
set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/.venv/bin/activate"
cd "$SCRIPT_DIR"

DATE=$(date +%Y-%m-%d)
LOG="$SCRIPT_DIR/logs/$DATE.log"

echo "=== Auto Post Blog — $DATE ($(date)) ===" >> "$LOG"

# 先補跑缺失的日期 (最近 7 天)
echo "--- Catch-up check ---" >> "$LOG"
python -m src.cli catchup --days 7 2>&1 | tee -a "$LOG"

# 再跑今天
echo "--- Today's run ---" >> "$LOG"
python -m src.cli run 2>&1 | tee -a "$LOG"

# 自動清理過期資料
echo "--- Auto Clean ---" >> "$LOG"
python -m src.cli clean --auto 2>&1 | tee -a "$LOG"

echo "=== Done at $(date) ===" >> "$LOG"
RUNNER
chmod +x "$SCRIPT_DIR/run_daily.sh"

# 建立開機補跑腳本
cat > "$SCRIPT_DIR/run_catchup.sh" << 'CATCHUP'
#!/usr/bin/env bash
# 開機後等待 60 秒 (確保網路就緒) 再補跑
sleep 60
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/.venv/bin/activate"
cd "$SCRIPT_DIR"

DATE=$(date +%Y-%m-%d)
LOG="$SCRIPT_DIR/logs/${DATE}_reboot.log"

echo "=== Reboot Catch-up — $(date) ===" >> "$LOG"
python -m src.cli catchup --days 7 2>&1 | tee -a "$LOG"
echo "=== Done at $(date) ===" >> "$LOG"
CATCHUP
chmod +x "$SCRIPT_DIR/run_catchup.sh"

# 設定 cron jobs
# 1. 每天 10:00 AM 執行 (HF Papers 9 AM 後才更新)
# 2. 開機時補跑 (@reboot)
CRON_DAILY="0 10 * * * $SCRIPT_DIR/run_daily.sh"
CRON_REBOOT="@reboot $SCRIPT_DIR/run_catchup.sh"

# 移除舊的 auto_post_blog cron, 加入新的
(crontab -l 2>/dev/null | grep -v "auto_post_blog" ; echo "$CRON_DAILY" ; echo "$CRON_REBOOT") | crontab -

echo "✅ Cron 設定完成！"
echo ""
echo "📅 排程:"
echo "   每天 10:00 AM — 完整 pipeline (含自動補跑)"
echo "   開機時         — 自動補跑最近 7 天缺失"
echo ""
echo "📄 腳本:"
echo "   $SCRIPT_DIR/run_daily.sh     (每日執行)"
echo "   $SCRIPT_DIR/run_catchup.sh   (開機補跑)"
echo ""
echo "📁 日誌: $LOG_DIR/"
echo ""
echo "🔍 目前 cron 設定:"
crontab -l 2>/dev/null | grep auto_post_blog || echo "  (無)"
echo ""
echo "💡 手動執行:"
echo "   $SCRIPT_DIR/run_daily.sh           # 完整跑"
echo "   source .venv/bin/activate"
echo "   python -m src.cli catchup --days 7 # 只補跑"
echo "   python -m src.cli status           # 查看狀態"
