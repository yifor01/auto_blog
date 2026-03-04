#!/usr/bin/env bash
# 一鍵啟動 Auto Post Blog 監控網頁
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 確認 .venv 存在
if [ ! -f ".venv/bin/activate" ]; then
  echo "❌ 找不到 .venv，請先執行："
  echo "   python3 -m venv .venv && source .venv/bin/activate && pip install -e ."
  exit 1
fi

# 確認 .env 存在
if [ ! -f ".env" ]; then
  echo "⚠️  找不到 .env，複製範本中..."
  cp .env.example .env
  echo "📝 請編輯 .env 填入 OPENROUTER_API_KEY，再重新執行此腳本。"
  exit 1
fi

source .venv/bin/activate

echo "🚀 啟動 Auto Post Blog 監控網頁..."
echo "   URL: http://127.0.0.1:8555"
echo "   按 Ctrl+C 停止"
echo ""

python -m src.cli web
