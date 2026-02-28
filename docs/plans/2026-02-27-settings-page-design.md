# Settings 頁面設計文件

**日期：** 2026-02-27
**狀態：** 已核准

## 目標

在 Web Monitor 側邊欄新增 ⚙️ Settings 連結，導向 `/settings` 專用頁面，讓使用者可透過 UI 直接修改 pipeline 的 LLM 設定、評分參數與 Pipeline 參數，不需手動編輯 `config.yaml` 或 `.env`。

---

## 架構

採用 **In-Memory Config + Persist** 方案：

1. App 啟動時呼叫 `init_config()` 將 `config.yaml` 載入全域記憶體（dict）
2. `GET /settings`：從 in-memory config + `.env`（`os.getenv`）讀取當前值，渲染表單
3. `POST /settings`：驗證輸入 → 更新 in-memory config → flush 回 `config.yaml` + `.env`
4. 下次 pipeline 執行時自動使用新設定（`load_config()` / `get_llm_client()` 都讀記憶體版本）

```
app startup → init_config() 載入 config.yaml 到全域記憶體
     │
GET /settings ──→ 讀 in-memory config + .env → 渲染表單
     │
POST /settings ─→ 驗證 → 更新記憶體 → flush config.yaml + .env
                 → redirect GET /settings?saved=1（PRG 模式）
```

---

## 新增檔案

### `src/web/config_manager.py`

全域 config 管理模組：

```python
_config: dict = {}  # in-memory config (從 config.yaml 載入)

def init_config() -> None:
    """App 啟動時呼叫，從 config.yaml 載入到記憶體。"""

def get_config() -> dict:
    """取得 in-memory config（deep copy）。"""

def update_and_save(config_updates: dict, env_updates: dict) -> None:
    """更新 in-memory config，並 flush 到 config.yaml + .env。"""

def _write_config_yaml(cfg: dict) -> None:
    """寫回 config.yaml，保留結構。"""

def _write_env(updates: dict) -> None:
    """逐行讀取 .env，替換對應 KEY= 行，找不到則 append。"""
```

### `src/web/templates/settings.html`

設定頁面（繼承 `base.html`），三個分組 section：
- LLM 設定、評分參數、Pipeline 參數

---

## 修改檔案

### `src/web/app.py`

1. import `config_manager as cm`
2. 在 `create_app()` 或 app 初始化時呼叫 `cm.init_config()`
3. 新增路由：
   - `GET /settings` → 讀 config + env，渲染 settings.html
   - `POST /settings` → 驗證 → `cm.update_and_save()` → redirect

### `src/web/templates/base.html`

側邊欄 nav 區塊加入 ⚙️ Settings 連結（位置：工具區塊之前）：

```html
<a href="/settings" class="nav-link {% if active_page == 'settings' %}active{% endif %}">
  <span>⚙️</span>
  Settings
</a>
```

---

## UI 設計

```
┌────────────────────────────────────────────────┐
│  ⚙️ Settings                                   │
├────────────────────────────────────────────────┤
│  [🤖 LLM 設定]                                  │
│   API Key:      [••••••••••••]  [👁 顯示]       │
│   API Base URL: [https://openrouter.ai/api/v1]  │
│   Model:        [deepseek/deepseek-chat-v3...]  │
│   Fallback:     [google/gemini-flash-1.5]       │
│   Max Tokens:   [4096]                          │
│   Request Delay:[0.5] 秒                        │
├────────────────────────────────────────────────┤
│  [📊 評分參數]                                   │
│   Rule 門檻:    [25]   LLM Top-K: [30]          │
│   Final Top-K:  [10]                            │
│   HF Upvote 門檻: [10]                          │
│   Stars 高: [100]   Stars 中: [50]              │
├────────────────────────────────────────────────┤
│  [🔧 Pipeline 參數]                             │
│   去重回看天數: [7]   資料保留天數: [90]          │
├────────────────────────────────────────────────┤
│                    [取消]  [💾 儲存設定]         │
│  ✅ 設定已儲存（儲存後顯示）                      │
└────────────────────────────────────────────────┘
```

---

## 設定欄位對應表

| UI 欄位 | 來源 | Key |
|---------|------|-----|
| API Key | `.env` | `OPENROUTER_API_KEY` |
| API Base URL | `.env` | `OPENROUTER_API_URL` |
| Model | `.env` | `OPENROUTER_MODEL` |
| Fallback Model | `config.yaml` | `llm.fallback_model` |
| Max Tokens | `config.yaml` | `llm.max_tokens` |
| Request Delay | `config.yaml` | `llm.request_delay_seconds` |
| Rule 門檻 | `config.yaml` | `scoring.rule_threshold` |
| LLM Top-K | `config.yaml` | `scoring.llm_top_k` |
| Final Top-K | `config.yaml` | `scoring.final_top_k` |
| HF Upvote 門檻 | `config.yaml` | `scoring.hf_upvote_bonus_threshold` |
| Stars 高 | `config.yaml` | `scoring.github_stars_high` |
| Stars 中 | `config.yaml` | `scoring.github_stars_medium` |
| 去重回看天數 | `config.yaml` | `dedup.lookback_days` |
| 資料保留天數 | `config.yaml` | `retention_days` |

---

## .env 更新策略

逐行讀取現有 `.env`，遇到 `KEY=...` 格式的行就替換對應 key 的值，其餘行（包括注釋）原樣保留。若 key 不存在則 append 到末尾。

```python
def _write_env(updates: dict) -> None:
    lines = env_path.read_text().splitlines() if env_path.exists() else []
    written = set()
    new_lines = []
    for line in lines:
        key = line.split("=", 1)[0].strip()
        if key in updates:
            new_lines.append(f"{key}={updates[key]}")
            written.add(key)
        else:
            new_lines.append(line)
    for key, val in updates.items():
        if key not in written:
            new_lines.append(f"{key}={val}")
    env_path.write_text("\n".join(new_lines) + "\n")
```

---

## 驗證計畫

1. 啟動服務 `python -m src.cli web`
2. 側邊欄出現 ⚙️ Settings 連結，點選進入 `/settings`
3. 表單顯示 config.yaml + .env 的當前值（API Key 遮罩）
4. 修改任意欄位後點「儲存設定」→ 頁面重整顯示綠色 toast
5. 確認 `config.yaml` 和 `.env` 已更新
6. 重啟服務後確認設定持久化
7. 邊界條件：空 API Key、非數字 threshold → 前端 required/type=number 攔截
