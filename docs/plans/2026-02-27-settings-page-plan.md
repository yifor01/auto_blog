# Settings Page Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 在 Web Monitor 側邊欄新增 ⚙️ Settings 連結，提供 `/settings` 專用頁面，讓使用者可透過 UI 修改 LLM 設定、評分參數與 Pipeline 參數，並即時寫回 `config.yaml` 與 `.env`。

**Architecture:** 新增 `src/web/config_manager.py` 維護 in-memory config；app 啟動時載入，`GET /settings` 讀取渲染，`POST /settings` 驗證後更新 memory 並寫回磁碟。由於 `llm_chat()` 每次呼叫都執行 `load_config()`，改寫 disk 後下次 pipeline 執行即生效。

**Tech Stack:** Python, FastAPI, Jinja2, PyYAML, python-dotenv, HTML form

**Known limitation:** `yaml.dump()` 在回寫 `config.yaml` 時會移除行內注釋（如 `# free tier = 8 req/min`）。這是 PyYAML 的已知限制，可接受。

---

## 欄位來源對應

| 表單欄位 | 讀/寫來源 | key |
|---------|-----------|-----|
| API Key | `.env` | `OPENROUTER_API_KEY` |
| API Base URL | `.env` | `OPENROUTER_API_URL` |
| Model | `config.yaml` | `llm.model` |
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

## Task 1: config_manager.py（核心模組）

**Files:**
- Create: `src/web/config_manager.py`
- Test: `tests/test_config_manager.py`

### Step 1: Write failing tests

建立 `tests/test_config_manager.py`：

```python
"""測試 config_manager 的讀寫功能。"""
from __future__ import annotations

import os
from pathlib import Path

import pytest
import yaml


@pytest.fixture
def tmp_env(tmp_path):
    """建立 .env 測試檔。"""
    env_file = tmp_path / ".env"
    env_file.write_text(
        "OPENROUTER_API_KEY=sk-test-123\n"
        "OPENROUTER_API_URL=https://openrouter.ai/api/v1\n"
        "# 這是注釋\n",
        encoding="utf-8",
    )
    return env_file


@pytest.fixture
def tmp_config(tmp_path):
    """建立 config.yaml 測試檔。"""
    cfg = {
        "llm": {
            "model": "test-model",
            "fallback_model": "fallback-model",
            "max_tokens": 4096,
            "request_delay_seconds": 0.5,
        },
        "scoring": {
            "rule_threshold": 25,
            "llm_top_k": 30,
            "final_top_k": 10,
            "hf_upvote_bonus_threshold": 10,
            "github_stars_high": 100,
            "github_stars_medium": 50,
        },
        "dedup": {"lookback_days": 7},
        "retention_days": 90,
    }
    config_file = tmp_path / "config.yaml"
    with open(config_file, "w") as f:
        yaml.dump(cfg, f, allow_unicode=True)
    return config_file


def test_init_config_loads_yaml(tmp_config, tmp_env, monkeypatch):
    """init_config 應將 config.yaml 載入 _config。"""
    import importlib
    import src.web.config_manager as cm
    monkeypatch.setattr(cm, "CONFIG_PATH", tmp_config)
    monkeypatch.setattr(cm, "ENV_PATH", tmp_env)
    cm.init_config()
    cfg = cm.get_config()
    assert cfg["llm"]["model"] == "test-model"
    assert cfg["scoring"]["rule_threshold"] == 25


def test_get_env_values(tmp_config, tmp_env, monkeypatch):
    """get_env_values 應讀取 .env 中的 API 設定。"""
    import src.web.config_manager as cm
    monkeypatch.setattr(cm, "CONFIG_PATH", tmp_config)
    monkeypatch.setattr(cm, "ENV_PATH", tmp_env)
    cm.init_config()
    env = cm.get_env_values()
    assert env["api_key"] == "sk-test-123"
    assert "openrouter.ai" in env["api_url"]


def test_write_env_updates_existing_key(tmp_env, monkeypatch):
    """_write_env 應替換現有 KEY=VALUE 行，並保留注釋行。"""
    import src.web.config_manager as cm
    monkeypatch.setattr(cm, "ENV_PATH", tmp_env)
    cm._write_env({"OPENROUTER_API_KEY": "sk-new-456"})
    content = tmp_env.read_text(encoding="utf-8")
    assert "sk-new-456" in content
    assert "sk-test-123" not in content
    assert "# 這是注釋" in content  # 注釋行保留


def test_write_env_appends_new_key(tmp_env, monkeypatch):
    """_write_env 當 key 不存在時應 append 到末尾。"""
    import src.web.config_manager as cm
    monkeypatch.setattr(cm, "ENV_PATH", tmp_env)
    cm._write_env({"NEW_KEY": "new-value"})
    content = tmp_env.read_text(encoding="utf-8")
    assert "NEW_KEY=new-value" in content


def test_update_and_save_writes_config(tmp_config, tmp_env, monkeypatch):
    """update_and_save 應更新 memory 並寫回 config.yaml。"""
    import src.web.config_manager as cm
    monkeypatch.setattr(cm, "CONFIG_PATH", tmp_config)
    monkeypatch.setattr(cm, "ENV_PATH", tmp_env)
    cm.init_config()
    cm.update_and_save({"scoring.rule_threshold": 30}, {})
    # memory 已更新
    assert cm.get_config()["scoring"]["rule_threshold"] == 30
    # 磁碟已更新
    with open(tmp_config) as f:
        disk = yaml.safe_load(f)
    assert disk["scoring"]["rule_threshold"] == 30
```

### Step 2: Run test to verify it fails

```bash
cd /home/yifor/auto_post_blog
pytest tests/test_config_manager.py -v
```
Expected: FAIL with `ModuleNotFoundError: No module named 'src.web.config_manager'`

### Step 3: Implement config_manager.py

建立 `src/web/config_manager.py`：

```python
"""In-memory config manager — 供 Settings 頁面讀寫 config.yaml 與 .env。"""
from __future__ import annotations

import copy
import os
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
CONFIG_PATH = PROJECT_ROOT / "config.yaml"
ENV_PATH = PROJECT_ROOT / ".env"

_config: dict = {}


def init_config() -> None:
    """App 啟動時呼叫一次，將 config.yaml 載入 memory。"""
    global _config
    load_dotenv(ENV_PATH)
    with open(CONFIG_PATH, encoding="utf-8") as f:
        _config = yaml.safe_load(f) or {}


def get_config() -> dict:
    """回傳 in-memory config 的 deep copy。"""
    return copy.deepcopy(_config)


def get_env_values() -> dict[str, str]:
    """讀取 .env 中的 API 相關設定。"""
    return {
        "api_key": os.getenv("OPENROUTER_API_KEY", ""),
        "api_url": os.getenv("OPENROUTER_API_URL", ""),
    }


def update_and_save(config_updates: dict[str, Any], env_updates: dict[str, str]) -> None:
    """更新 in-memory config，並 flush 到 config.yaml + .env。"""
    _apply_nested(config_updates)
    _write_config_yaml()
    if env_updates:
        _write_env(env_updates)
    load_dotenv(ENV_PATH, override=True)


def _apply_nested(updates: dict[str, Any]) -> None:
    """將 "a.b.c": value 格式的更新寫入 _config。"""
    for dotted_key, value in updates.items():
        keys = dotted_key.split(".")
        d = _config
        for k in keys[:-1]:
            d = d.setdefault(k, {})
        d[keys[-1]] = value


def _write_config_yaml() -> None:
    """將 _config 寫回 config.yaml（注意：注釋會被移除）。"""
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        yaml.dump(_config, f, allow_unicode=True, default_flow_style=False, sort_keys=False)


def _write_env(updates: dict[str, str]) -> None:
    """逐行更新 .env：替換現有 KEY=VALUE，找不到則 append；注釋行原樣保留。"""
    if ENV_PATH.exists():
        lines = ENV_PATH.read_text(encoding="utf-8").splitlines()
    else:
        lines = []

    written: set[str] = set()
    new_lines: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and "=" in stripped:
            key = stripped.split("=", 1)[0].strip()
            if key in updates:
                new_lines.append(f"{key}={updates[key]}")
                written.add(key)
                continue
        new_lines.append(line)

    for key, val in updates.items():
        if key not in written:
            new_lines.append(f"{key}={val}")

    ENV_PATH.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
```

### Step 4: Run test to verify it passes

```bash
pytest tests/test_config_manager.py -v
```
Expected: 全部 PASS (5 tests)

### Step 5: Commit

```bash
git add src/web/config_manager.py tests/test_config_manager.py
git commit -m "feat: add config_manager for in-memory config read/write"
```

---

## Task 2: app.py — 新增 Settings 路由

**Files:**
- Modify: `src/web/app.py`

### Step 1: 加入 import 與 init 呼叫

在 `src/web/app.py` 頂部 import 區加入（緊接 `from src.web import data_service as ds` 之後）：

```python
from src.web import config_manager as cm
from fastapi import Form
```

在 `app = FastAPI(...)` 建立之後（第 19 行之後）加入：

```python
cm.init_config()
```

### Step 2: 新增 GET /settings 路由

在 `/notes` 路由之後、`/api/status` 之前加入：

```python
@app.get("/settings", response_class=HTMLResponse)
async def settings_page(request: Request, saved: str = ""):
    cfg = cm.get_config()
    env = cm.get_env_values()
    return templates.TemplateResponse(
        "settings.html",
        {
            "request": request,
            "cfg": cfg,
            "env": env,
            "saved": saved == "1",
            "sidebar_stats": ds.get_sidebar_stats(),
        },
    )
```

### Step 3: 新增 POST /settings 路由

緊接 GET /settings 之後加入：

```python
@app.post("/settings")
async def settings_save(
    request: Request,
    api_key: str = Form(""),
    api_url: str = Form(""),
    llm_model: str = Form(""),
    fallback_model: str = Form(""),
    max_tokens: int = Form(8192),
    request_delay: float = Form(0.5),
    rule_threshold: int = Form(25),
    llm_top_k: int = Form(30),
    final_top_k: int = Form(10),
    hf_upvote_threshold: int = Form(10),
    github_stars_high: int = Form(100),
    github_stars_medium: int = Form(50),
    dedup_lookback: int = Form(7),
    retention_days: int = Form(90),
):
    env_updates: dict[str, str] = {}
    if api_key.strip():
        env_updates["OPENROUTER_API_KEY"] = api_key.strip()
    if api_url.strip():
        env_updates["OPENROUTER_API_URL"] = api_url.strip()

    config_updates: dict = {
        "llm.model": llm_model.strip() or cm.get_config().get("llm", {}).get("model", ""),
        "llm.fallback_model": fallback_model.strip(),
        "llm.max_tokens": max_tokens,
        "llm.request_delay_seconds": request_delay,
        "scoring.rule_threshold": rule_threshold,
        "scoring.llm_top_k": llm_top_k,
        "scoring.final_top_k": final_top_k,
        "scoring.hf_upvote_bonus_threshold": hf_upvote_threshold,
        "scoring.github_stars_high": github_stars_high,
        "scoring.github_stars_medium": github_stars_medium,
        "dedup.lookback_days": dedup_lookback,
        "retention_days": retention_days,
    }
    cm.update_and_save(config_updates, env_updates)
    return RedirectResponse(url="/settings?saved=1", status_code=303)
```

### Step 4: 手動驗證 app.py 可 import

```bash
python3 -c "from src.web.app import app; print('app.py OK')"
```
Expected: `app.py OK`

### Step 5: Commit

```bash
git add src/web/app.py
git commit -m "feat: add GET/POST /settings routes with config_manager"
```

---

## Task 3: settings.html — 設定頁面模板

**Files:**
- Create: `src/web/templates/settings.html`

### Step 1: 建立 settings.html

建立 `src/web/templates/settings.html`，完整內容如下：

```html
{% extends "base.html" %}
{% block title %}Settings — Auto Post Blog Monitor{% endblock %}

{% block page_title %}
<nav style="display:flex; align-items:center; gap:8px; font-size:13.5px;">
  <a href="/dashboard" class="link-muted">Dashboard</a>
  <span style="color:var(--t6);">/</span>
  <span style="color:var(--t1); font-weight:600;">⚙️ Settings</span>
</nav>
{% endblock %}

{% block content %}
<style>
.settings-section {
  background: var(--bg-c); border: 1px solid var(--br);
  border-radius: 12px; padding: 20px 24px; margin-bottom: 20px;
}
.settings-section-title {
  font-size: 13px; font-weight: 600; color: var(--t2);
  margin: 0 0 16px; padding-bottom: 10px; border-bottom: 1px solid var(--br3);
}
.form-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 14px;
}
.form-field { display: flex; flex-direction: column; gap: 5px; }
.form-label {
  font-size: 11.5px; color: var(--t4); font-weight: 500;
}
.form-input {
  padding: 8px 12px; background: var(--bg-in);
  border: 1px solid var(--br2); border-radius: 8px;
  font-size: 13px; color: var(--t1); outline: none;
  transition: border-color 0.13s;
}
.form-input:focus { border-color: var(--av); }
.form-input[type="number"] { -moz-appearance: textfield; }
.form-hint { font-size: 10.5px; color: var(--t5); }
.pw-wrap { position: relative; display: flex; }
.pw-wrap .form-input { flex: 1; }
.pw-toggle {
  position: absolute; right: 8px; top: 50%; transform: translateY(-50%);
  background: none; border: none; cursor: pointer; color: var(--t4);
  font-size: 14px; padding: 2px 4px;
}
.form-actions {
  display: flex; gap: 10px; justify-content: flex-end;
  padding-top: 6px;
}
.btn-save {
  padding: 9px 20px; border-radius: 9px; border: none; cursor: pointer;
  font-size: 13px; font-weight: 600;
  background: var(--av); color: #fff; transition: opacity 0.13s;
}
.btn-save:hover { opacity: 0.88; }
.btn-cancel {
  padding: 9px 16px; border-radius: 9px; border: 1px solid var(--br2);
  background: none; cursor: pointer; font-size: 13px; color: var(--t3);
  transition: background 0.13s; text-decoration: none; display: inline-flex;
  align-items: center;
}
.btn-cancel:hover { background: var(--bg-hv); }
.toast-ok {
  display: flex; align-items: center; gap: 8px;
  background: rgba(52,211,153,0.1); border: 1px solid rgba(52,211,153,0.3);
  color: var(--ag); border-radius: 9px; padding: 10px 16px;
  font-size: 13px; margin-bottom: 16px;
}
</style>

<div style="margin-bottom:18px;">
  <h2 style="font-size:20px; font-weight:700; color:var(--av); margin:0 0 4px;">⚙️ Settings</h2>
  <p style="font-size:13px; color:var(--t4); margin:0;">調整 pipeline 參數，儲存後下次執行即生效</p>
</div>

{% if saved %}
<div class="toast-ok">✅ 設定已儲存成功</div>
{% endif %}

<form method="post" action="/settings">

  <!-- Section 1: LLM 設定 -->
  <div class="settings-section">
    <div class="settings-section-title">🤖 LLM 設定</div>
    <div class="form-grid">

      <div class="form-field" style="grid-column: 1/-1;">
        <label class="form-label">API Key</label>
        <div class="pw-wrap">
          <input type="password" name="api_key" id="api-key-input"
            class="form-input" placeholder="留空則不修改"
            autocomplete="off" />
          <button type="button" class="pw-toggle" onclick="togglePw('api-key-input', this)" title="顯示/隱藏">👁</button>
        </div>
        <span class="form-hint">目前已設定：{{ '✅ 已設定' if env.api_key else '❌ 未設定' }}。留空不修改。</span>
      </div>

      <div class="form-field">
        <label class="form-label">API Base URL</label>
        <input type="url" name="api_url" class="form-input"
          value="{{ env.api_url or 'https://openrouter.ai/api/v1' }}" required />
      </div>

      <div class="form-field">
        <label class="form-label">Model（主力）</label>
        <input type="text" name="llm_model" class="form-input"
          value="{{ cfg.llm.model }}" required />
      </div>

      <div class="form-field">
        <label class="form-label">Fallback Model</label>
        <input type="text" name="fallback_model" class="form-input"
          value="{{ cfg.llm.fallback_model or '' }}" />
      </div>

      <div class="form-field">
        <label class="form-label">Max Tokens</label>
        <input type="number" name="max_tokens" class="form-input"
          value="{{ cfg.llm.max_tokens or 8192 }}" min="256" max="65536" required />
      </div>

      <div class="form-field">
        <label class="form-label">Request Delay（秒）</label>
        <input type="number" name="request_delay" class="form-input"
          value="{{ cfg.llm.request_delay_seconds or 0.5 }}"
          min="0" max="60" step="0.5" required />
        <span class="form-hint">Free tier 建議 ≥ 7.5 秒（8 req/min）</span>
      </div>

    </div>
  </div>

  <!-- Section 2: 評分參數 -->
  <div class="settings-section">
    <div class="settings-section-title">📊 評分參數</div>
    <div class="form-grid">

      <div class="form-field">
        <label class="form-label">Rule Score 門檻</label>
        <input type="number" name="rule_threshold" class="form-input"
          value="{{ cfg.scoring.rule_threshold or 25 }}" min="0" max="200" required />
        <span class="form-hint">低於此分數直接排除，不進 LLM 評分</span>
      </div>

      <div class="form-field">
        <label class="form-label">LLM 評分候選數（llm_top_k）</label>
        <input type="number" name="llm_top_k" class="form-input"
          value="{{ cfg.scoring.llm_top_k or 30 }}" min="1" max="200" required />
        <span class="form-hint">Rule 篩選後，送 LLM 評分的上限數量</span>
      </div>

      <div class="form-field">
        <label class="form-label">最終產出數（final_top_k）</label>
        <input type="number" name="final_top_k" class="form-input"
          value="{{ cfg.scoring.final_top_k or 10 }}" min="1" max="100" required />
        <span class="form-hint">每天最多生成幾篇文章</span>
      </div>

      <div class="form-field">
        <label class="form-label">HF Upvote 加分門檻</label>
        <input type="number" name="hf_upvote_threshold" class="form-input"
          value="{{ cfg.scoring.hf_upvote_bonus_threshold or 10 }}" min="0" max="10000" required />
      </div>

      <div class="form-field">
        <label class="form-label">GitHub Stars 高門檻</label>
        <input type="number" name="github_stars_high" class="form-input"
          value="{{ cfg.scoring.github_stars_high or 100 }}" min="0" required />
      </div>

      <div class="form-field">
        <label class="form-label">GitHub Stars 中門檻</label>
        <input type="number" name="github_stars_medium" class="form-input"
          value="{{ cfg.scoring.github_stars_medium or 50 }}" min="0" required />
      </div>

    </div>
  </div>

  <!-- Section 3: Pipeline 參數 -->
  <div class="settings-section">
    <div class="settings-section-title">🔧 Pipeline 參數</div>
    <div class="form-grid">

      <div class="form-field">
        <label class="form-label">去重回看天數</label>
        <input type="number" name="dedup_lookback" class="form-input"
          value="{{ cfg.dedup.lookback_days if cfg.dedup else 7 }}" min="0" max="90" required />
        <span class="form-hint">0 = 停用跨日去重</span>
      </div>

      <div class="form-field">
        <label class="form-label">資料保留天數</label>
        <input type="number" name="retention_days" class="form-input"
          value="{{ cfg.retention_days or 90 }}" min="1" max="3650" required />
        <span class="form-hint">超過此天數的舊資料可清理</span>
      </div>

    </div>
  </div>

  <!-- Actions -->
  <div class="form-actions">
    <a href="/dashboard" class="btn-cancel">取消</a>
    <button type="submit" class="btn-save">💾 儲存設定</button>
  </div>

</form>
{% endblock %}

{% block scripts %}
<script>
function togglePw(inputId, btn) {
  var input = document.getElementById(inputId);
  if (input.type === 'password') {
    input.type = 'text';
    btn.textContent = '🙈';
  } else {
    input.type = 'password';
    btn.textContent = '👁';
  }
}
</script>
{% endblock %}
```

### Step 2: 啟動並手動驗證

```bash
python -m src.cli web
```
開啟 `http://127.0.0.1:8080/settings`，確認：
- 頁面正常載入，各欄位顯示 config.yaml 的當前值
- API Key 欄位為 password 型，👁 按鈕可切換顯示
- 點「取消」跳回 Dashboard

### Step 3: Commit

```bash
git add src/web/templates/settings.html
git commit -m "feat: add settings.html template with LLM/scoring/pipeline sections"
```

---

## Task 4: base.html — 側邊欄加入 Settings 連結

**Files:**
- Modify: `src/web/templates/base.html`

### Step 1: 找到插入位置

在 `base.html` 中找到「工具」section（約第 961 行）：

```html
<div class="nav-section" style="margin-top: 6px">工具</div>
<a href="/api/status" class="nav-link">
```

### Step 2: 在「工具」區塊之前插入 Settings 連結

在 `<div class="nav-section" style="margin-top: 6px">工具</div>` 這一行的**前面**插入：

```html
          <a
            href="/settings"
            class="nav-link {% if request.url.path == '/settings' %}active{% endif %}"
          >
            <span style="font-size:15px; margin-right:4px;">⚙️</span>
            Settings
          </a>
```

### Step 3: 驗證 template 語法

```bash
python3 -c "
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('src/web/templates'))
tmpl = env.get_template('base.html')
print('base.html OK')
"
```
Expected: `base.html OK`

### Step 4: Commit

```bash
git add src/web/templates/base.html
git commit -m "feat: add Settings link to sidebar"
```

---

## Task 5: 整合驗證

### Step 1: 啟動服務

```bash
python -m src.cli web
```

### Step 2: 驗證所有功能

1. 訪問 `http://127.0.0.1:8080/dashboard` → sidebar 顯示 ⚙️ Settings 連結
2. 點擊 Settings → 進入 `/settings` 頁面，連結高亮 active
3. 各欄位顯示 `config.yaml` 與 `.env` 的當前值
4. **修改 Rule 門檻** 為 `28`，點「儲存設定」
5. 頁面重整後顯示綠色「✅ 設定已儲存成功」toast
6. 確認 `config.yaml` 的 `scoring.rule_threshold` 值已更新為 `28`
7. **API Key 測試**：保留空白提交 → `.env` 中 API Key 不變
8. **API Key 更新**：填入假值 `sk-test-0000` 提交 → `.env` 更新成功
9. 重新把 API Key 改回原值並儲存

### Step 3: 邊界條件確認

- 表單欄位有 `required` + `min/max` 限制，非數字輸入由瀏覽器攔截
- Model 欄位留空時保留原值（POST handler 的 `or cm.get_config()...` 邏輯）

### Step 4: Final commit

```bash
git add -p  # 確認無多餘檔案
git commit -m "feat: complete settings page integration"
```
