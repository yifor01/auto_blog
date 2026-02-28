# Force Stop Pipeline Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 在 Pipeline Card 的每個 stage node 新增「Force Stop」按鈕（類似 GitLab CI/CD），讓使用者能中途取消正在執行的 pipeline，並即時同步 `cancelled` 狀態到 UI。

**Architecture:** 在後端新增 `RUNNING_PROCS: dict[str, subprocess.Popen]` 全域字典追蹤 process handle，新增 `POST /api/run/{date_str}/stop` API 發送 SIGTERM/SIGKILL。前端在每個 stage node 顯示小型停止按鈕（pipeline 執行中時可用），SSE stream 偵測 `"Pipeline cancelled"` 關鍵字後發 `event: cancelled`，前端收到後更新 badge 為橘色 `cancelled` 狀態。

**Tech Stack:** FastAPI (Python), Jinja2, vanilla JS, SSE, subprocess

---

### Task 1: 後端 — 全域 process dict + stop API

**Files:**
- Modify: `src/web/app.py:30`（新增 `RUNNING_PROCS`）
- Modify: `src/web/app.py:708-735`（`_run_pipeline` 儲存/清除 proc）
- Modify: `src/web/app.py:757`（stop API endpoint）

**Step 1: 在 `RUNNING_TASKS` 下方新增 `RUNNING_PROCS`**

在 `src/web/app.py` 第 30 行後：

```python
RUNNING_TASKS: set[str] = set()
RUNNING_PROCS: dict[str, subprocess.Popen] = {}
```

**Step 2: 修改 `_run_pipeline` 儲存 proc handle**

將 `_run_pipeline` 中的 Popen 區段改為：

```python
proc = subprocess.Popen(
    cmd,
    stdout=log_file,
    stderr=subprocess.STDOUT,
    text=True,
    encoding="utf-8",
    env=env,
)
RUNNING_PROCS[date_str] = proc
proc.wait()
exit_code = proc.returncode
```

cleanup 時（finally 區塊中）：

```python
finally:
    RUNNING_TASKS.discard(date_str)
    RUNNING_PROCS.pop(date_str, None)
```

**Step 3: 在 `_run_pipeline` 寫入 log 時加入取消判斷**

在 `proc.wait()` 後、寫 finished 行前：

```python
proc.wait()
exit_code = proc.returncode
if exit_code == -15 or exit_code == -9:  # SIGTERM / SIGKILL
    log_file.write(f"\n=== Pipeline cancelled by user: exit_code={exit_code} ===\n")
else:
    log_file.write(f"\n=== Pipeline finished: exit_code={exit_code} ===\n")
```

**Step 4: 新增 stop API endpoint（加在 `api_run_force` 之後）**

```python
@app.post("/api/run/{date_str}/stop")
async def api_run_stop(date_str: str):
    """中止正在執行的 pipeline。"""
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")

    proc = RUNNING_PROCS.get(date_str)
    if proc is None:
        raise HTTPException(status_code=404, detail="找不到執行中的 pipeline")

    # 嘗試優雅終止，3 秒後強制殺死
    proc.terminate()
    try:
        proc.wait(timeout=3)
    except subprocess.TimeoutExpired:
        proc.kill()

    return JSONResponse({"message": f"Pipeline 已中止（{date_str}）", "date": date_str})
```

**Step 5: 確認語法正確**

```bash
python3 -c "import ast; ast.parse(open('src/web/app.py').read()); print('Syntax OK')"
```

Expected: `Syntax OK`

**Step 6: 執行測試確認無 regression**

```bash
source .venv/bin/activate && pytest tests/ -x -q
```

Expected: `106 passed`

**Step 7: Commit**

```bash
git add src/web/app.py
git commit -m "feat: add RUNNING_PROCS tracking and /api/run/{date}/stop endpoint"
```

---

### Task 2: 後端 — SSE 偵測 `cancelled` 關鍵字

**Files:**
- Modify: `src/web/app.py`（SSE stream generator，`log_stream` 函數）

**Step 1: 找到 SSE done 偵測的位置**

目前程式碼（約 644 行）：
```python
if "Pipeline finished" in line or "=== Pipeline finished" in line:
    yield f"event: done\n..."
```

**Step 2: 在 done 偵測後加入 cancelled 偵測**

```python
# 偵測取消
if "Pipeline cancelled by user" in display:
    yield f"event: cancelled\ndata: {{}}\n\n"
    done = True
    break

# 原有的 done 偵測
if "Pipeline finished" in display or "exit_code=0" in display:
    yield f"event: done\ndata: {{}}\n\n"
    done = True
    break
```

> **注意：** 先偵測 `cancelled`（更具體），避免 `Pipeline finished` 也出現在同一行時誤判。

**Step 3: 語法確認 + 測試**

```bash
python3 -c "import ast; ast.parse(open('src/web/app.py').read()); print('Syntax OK')"
pytest tests/ -x -q
```

Expected: `Syntax OK`, `106 passed`

**Step 4: Commit**

```bash
git add src/web/app.py
git commit -m "feat: SSE emits 'cancelled' event when pipeline is force-stopped"
```

---

### Task 3: 前端 — `cancelled` CSS + stage node stop 按鈕

**Files:**
- Modify: `src/web/templates/day_detail.html`（`<style>` 區段 + stage node HTML）

**Step 1: 新增 CSS — cancelled 狀態樣式**

在 `day_detail.html` 的 `<style>` 區段，`badge-failed` 之後加：

```css
.pipeline-badge.badge-cancelled { background: rgba(249,115,22,0.15); color: #f97316; }
.stage-node.stage-cancelled { border-color: #f97316; background: rgba(249,115,22,0.08); }
.acc-badge.badge-cancelled { background: rgba(249,115,22,0.15); color: #f97316; }
```

**Step 2: 新增 CSS — stop button 樣式**

```css
.stage-stop-btn {
  display: none;
  margin-top: 4px;
  padding: 2px 8px;
  font-size: 0.68rem;
  background: rgba(239,68,68,0.15);
  color: #ef4444;
  border: 1px solid rgba(239,68,68,0.3);
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.15s;
}
.stage-stop-btn:hover { background: rgba(239,68,68,0.3); }
.pipeline-running .stage-stop-btn { display: inline-block; }
```

> `pipeline-running` class 加在 `.pipeline-card` 上，由 JS 控制。

**Step 3: 修改 stage node HTML — 加入 stop button**

將原本的 stage node 模板：

```html
<div class="stage-node stage-pending" id="snode-{{ stage_name }}">
  <div class="stage-icon" id="sicon-{{ stage_name }}">⬜</div>
  <div class="stage-label">{{ stage_label }}</div>
  <div class="stage-elapsed" id="selapsed-{{ stage_name }}">-</div>
</div>
```

改為：

```html
<div class="stage-node stage-pending" id="snode-{{ stage_name }}">
  <div class="stage-icon" id="sicon-{{ stage_name }}">⬜</div>
  <div class="stage-label">{{ stage_label }}</div>
  <div class="stage-elapsed" id="selapsed-{{ stage_name }}">-</div>
  <button class="stage-stop-btn" onclick="stopPipeline()">■ 停止</button>
</div>
```

**Step 4: 語法確認（Jinja2 template 不能直接 parse，改用目視確認）**

```bash
grep -n "stage-stop-btn" src/web/templates/day_detail.html
```

Expected: 至少 4 行（3 個 node + 1 CSS）

**Step 5: Commit**

```bash
git add src/web/templates/day_detail.html
git commit -m "feat: add cancelled CSS styles and stop button to stage nodes"
```

---

### Task 4: 前端 — JS 邏輯（stopPipeline + cancelled event handler）

**Files:**
- Modify: `src/web/templates/day_detail.html`（`<script>` 區段）

**Step 1: 新增 `cancelled` 到 `updateStageNode` icon mapping**

在 `updateStageNode` 函數中：

```javascript
icon.textContent = {
  pending: '⬜', running: '⟳', done: '✓', failed: '✗', cancelled: '⊘'
}[s.status] || '⬜';
```

**Step 2: 新增 `cancelled` 到 `updateAccordion` labels**

```javascript
const labels = {
  pending: '等待中', running: '執行中', done: '完成', failed: '失敗', cancelled: '已取消'
};
```

**Step 3: 新增 `updatePipelineBadge` labels**

```javascript
const labels = {
  done: '✓ 完成', running: '⟳ 執行中', failed: '✗ 失敗',
  idle: '尚未執行', collected: '已收集', scored: '評分完成',
  cancelled: '⊘ 已取消'
};
```

**Step 4: 新增 `stopPipeline()` 函數**

在 `triggerRun` 函數之後加入：

```javascript
async function stopPipeline() {
  if (!confirm('確定要中止此 Pipeline 嗎？')) return;
  try {
    const res = await fetch('/api/run/' + dateStr + '/stop', { method: 'POST' });
    const data = await res.json();
    showToast(data.message || 'Pipeline 已中止', '⊘');
  } catch(e) {
    showToast('中止失敗，請確認 server 狀態', '❌');
  }
}
```

**Step 5: 新增 `pipeline-running` class 控制**

在 `openLogStream()` 開頭加：

```javascript
document.getElementById('pipeline-card').classList.add('pipeline-running');
```

在 SSE `done` 和 `error` handler 中移除：

```javascript
document.getElementById('pipeline-card').classList.remove('pipeline-running');
```

**Step 6: 新增 SSE `cancelled` event handler**

在 `_es.addEventListener('done', ...)` 之後：

```javascript
_es.addEventListener('cancelled', function() {
  _es.close(); _es = null;
  document.getElementById('pipeline-card').classList.remove('pipeline-running');
  // 正在 running 的 stage → cancelled
  STAGES.forEach(function(s) {
    if (stageState[s].status === 'running') {
      stageState[s].status = 'cancelled';
      updateStageNode(s);
      updateAccordion(s);
    }
  });
  updatePipelineBadge('cancelled');
  showToast('Pipeline 已取消', '⊘');
});
```

**Step 7: 在 `triggerRun` 開頭加 `pipeline-running` class**

```javascript
document.getElementById('pipeline-card').classList.add('pipeline-running');
```

在 `triggerRun` 的 catch/finally 中移除：

```javascript
document.getElementById('pipeline-card').classList.remove('pipeline-running');
```

**Step 8: 在 `_es.onerror` 中移除 `pipeline-running`**

```javascript
_es.onerror = function() {
  if (_es) { _es.close(); _es = null; }
  document.getElementById('pipeline-card').classList.remove('pipeline-running');
};
```

**Step 9: 確認 JS 結構完整**

```bash
grep -n "stopPipeline\|cancelled\|pipeline-running" src/web/templates/day_detail.html
```

Expected: 至少 8 行匹配

**Step 10: Commit**

```bash
git add src/web/templates/day_detail.html
git commit -m "feat: add stopPipeline() JS + SSE cancelled handler + pipeline-running class"
```

---

### Task 5: 文件同步

**Files:**
- Modify: `CLAUDE.md`（Web API Endpoints 表格）
- Modify: `README.md`（Web Monitor 說明）
- Modify: `memory/MEMORY.md`（已完成 Phase 記錄）

**Step 1: 更新 `CLAUDE.md` — 新增 stop API**

在 `Web API Endpoints` 表格的 `/api/run/{date}/force` 之後加：

```markdown
| POST | `/api/run/{date_str}/stop` | 中止執行中的 pipeline |
```

**Step 2: 更新 `README.md`**

在 Web monitor 的 API 說明（若有）加入 stop endpoint 說明。若 README 無此段落則略過。

**Step 3: 更新 `memory/MEMORY.md`**

將 Phase 9 的已完成記錄後新增：

```markdown
- **Phase 10**: Pipeline Force Stop（106 tests passed）
  - `app.py`：`RUNNING_PROCS: dict[str, Popen]` 全域追蹤 process handle
  - `POST /api/run/{date_str}/stop`：terminate + kill fallback
  - SSE：偵測 `"Pipeline cancelled"` → `event: cancelled`
  - `day_detail.html`：stage node 加 stop button，`pipeline-running` class 控制顯示，`cancelled` badge/CSS
```

**Step 4: Commit**

```bash
git add CLAUDE.md README.md memory/MEMORY.md
git commit -m "docs: sync Force Stop Pipeline changes to CLAUDE.md, README, MEMORY"
```

---

## 驗證 Checklist

- [ ] `pytest tests/ -x -q` 全部通過（106 passed）
- [ ] `python3 -c "import ast; ast.parse(open('src/web/app.py').read()); print('OK')"` 通過
- [ ] `GET /api/health` → `running_pipelines` 欄位存在
- [ ] pipeline 執行中時：三個 stage node 顯示「■ 停止」按鈕
- [ ] pipeline 未執行時：停止按鈕隱藏
- [ ] 點擊停止後：badge 變橘色「⊘ 已取消」，running stage 變 `⊘`
- [ ] SSE 在取消後正確關閉（不再輪詢 log）
- [ ] 強制重跑後可正常啟動（cancelled 狀態後仍可執行）
