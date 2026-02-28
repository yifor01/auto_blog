# Pipeline Status Sync & Force Stop Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 修正 pipeline 狀態不同步（generate 執行中顯示 done）並加入 Force Stop 功能。

**Architecture:**
1. SSE stream 在 new-lines 迴圈中直接偵測 `=== Pipeline finished`，立即發 `event: done`（不等 30 秒 idle）
2. 前端 stage event handler：當 generate `action=end` 且所有 stage 都 done，直接更新 badge 為 done
3. 新增全域 `RUNNING_PROCS: dict[str, subprocess.Popen]`，並加 `/api/run/{date}/stop` endpoint 與前端 Stop 按鈕

**Tech Stack:** Python/FastAPI, JavaScript (vanilla), Jinja2 HTML template, subprocess (os.kill)

---

### Task 1：修正 SSE stream — 立即偵測 Pipeline finished

**Files:**
- Modify: `src/web/app.py:618-646`（event_generator 內 new-lines 處理迴圈）

**Background：為什麼有 30 秒延遲**

目前 `event: done` 只在 `consecutive_idle >= 30`（30 秒無新輸出）的 idle-check block 中發送。
當 pipeline 剛結束（"Pipeline finished" 寫入 log），SSE stream 在 new-lines 迴圈把該行當普通 data 輸出後，
`consecutive_idle` 被 reset 為 0，必須再等 30 秒 idle 才送 done。

**Step 1: 在 new-lines 迴圈內加入 `=== Pipeline finished` 偵測**

在 `src/web/app.py` 的 `event_generator` 函式，找到 new-lines 的 `for line in new_text.splitlines():` 迴圈，
在 `try/except` 之後、`yield f"data: {prefix}|{display}\n\n"` 之前加入：

```python
# 若偵測到 pipeline 結束行，立即送 done event
if "=== Pipeline finished" in line:
    yield f"data: pipeline|{display}\n\n"
    yield "event: done\ndata: done\n\n"
    return
```

完整修改後的迴圈結構（只展示相關位置）：

```python
for line in new_text.splitlines():
    if not line.strip():
        continue
    display = line
    try:
        parsed = _json.loads(line)
        if "pipeline_stage" in parsed:
            name = parsed["pipeline_stage"]
            action = parsed["stage_action"]
            current_stage = name if action == "start" else None
            stage_data = _json.dumps({
                "name": name,
                "action": action,
                "elapsed": parsed.get("elapsed"),
            })
            yield f"event: stage\ndata: {stage_data}\n\n"
            continue
        if "msg" in parsed:
            level = parsed.get("level", "INFO")
            msg = parsed["msg"]
            extras = {k: v for k, v in parsed.items()
                      if k not in ("ts", "level", "logger", "msg", "exc",
                                   "pipeline_stage", "stage_action", "elapsed")}
            display = f"[{level}] {msg}" + (f" {extras}" if extras else "")
    except Exception:
        pass
    # 若偵測到 pipeline 結束行，立即送 done event
    if "=== Pipeline finished" in line:
        yield f"data: pipeline|{display}\n\n"
        yield "event: done\ndata: done\n\n"
        return
    prefix = current_stage or "pipeline"
    yield f"data: {prefix}|{display}\n\n"
```

**Step 2: 驗證語法**

```bash
source .venv/bin/activate
python -c "import ast; ast.parse(open('src/web/app.py').read()); print('OK')"
```
Expected: `OK`

**Step 3: 跑現有測試確認無 regression**

```bash
pytest tests/ -x -q
```
Expected: 106 passed

**Step 4: Commit**

```bash
git add src/web/app.py
git commit -m "fix: SSE stream immediately emits done event on Pipeline finished"
```

---

### Task 2：修正前端 stage event handler — 所有 stage done 時更新 badge

**Files:**
- Modify: `src/web/templates/day_detail.html:543-556`（`_es.addEventListener('stage', ...)` handler）

**Background：badge 顯示問題**

目前 stage event handler 無論 `action` 為何，最後都呼叫 `updatePipelineBadge('running')`。
這表示當 generate "end" event 到達（最後一個 stage 完成）時，badge 仍留在 "running"，
要等到 SSE `event: done` 才更新為 "done"。加上 Task 1 修正後，這段時間應該很短，
但仍需修正以確保一致性。

**Step 1: 修改 stage event handler**

找到 `_es.addEventListener('stage', function(e) { ... });` 區塊，
將最後的 `updatePipelineBadge('running');` 改為：

```javascript
_es.addEventListener('stage', function(e) {
  const payload = JSON.parse(e.data);
  const name = payload.name, action = payload.action, elapsed = payload.elapsed;
  if (action === 'start') {
    stageState[name].status = 'running';
    expandAccordion(name);
  } else if (action === 'end') {
    stageState[name].status = 'done';
    stageState[name].elapsed = elapsed;
  }
  updateStageNode(name);
  updateAccordion(name);
  // 若所有 stage 都已完成，badge 改為 done；否則維持 running
  const allDone = STAGES.every(function(s) { return stageState[s].status === 'done'; });
  updatePipelineBadge(allDone ? 'done' : 'running');
});
```

**Step 2: 驗證 HTML 語法（grep 確認 JS 結構完整）**

```bash
grep -n "updatePipelineBadge" src/web/templates/day_detail.html
```
Expected: 看到 4 行，分別在 `updatePipelineBadge` 函式定義與各呼叫點，
確認 `addEventListener('stage'` 內的呼叫已改為使用三元運算式。

**Step 3: 跑測試**

```bash
pytest tests/ -x -q
```
Expected: 106 passed

**Step 4: Commit**

```bash
git add src/web/templates/day_detail.html
git commit -m "fix: update pipeline badge to done when all stages complete"
```

---

### Task 3：修正 stage-info — RUNNING_TASKS 中的日期不應從 data_state 標 generate done

**Files:**
- Modify: `src/web/app.py:534-541`（stage-info Step 1 邏輯）

**Background：data_state 誤導**

`get_pipeline_state()` 只要看到 `output/posts/{date}*.md` 存在就回傳 `"done"`。
generate 階段寫第一篇文章後，此函式就回傳 `"done"`，Stage 1 於是把 generate 標為 done。
雖然 Step 2（RUNNING_TASKS check）和 Step 3（log parsing）通常能修正，
但為了明確防止誤判，當日期在 RUNNING_TASKS 中時，不應讓 data_state 影響 generate 的狀態。

**Step 1: 修改 Step 1 判斷邏輯**

將原本：
```python
# Step 1：用資料檔推算基礎狀態（最可靠的 fallback）
data_state = ds.get_pipeline_state(d)
if data_state in ("collected", "scored", "done"):
    stages["collect"]["status"] = "done"
if data_state in ("scored", "done"):
    stages["score"]["status"] = "done"
if data_state == "done":
    stages["generate"]["status"] = "done"

pipeline_status = data_state if data_state != "none" else "idle"
```

改為：
```python
# Step 1：用資料檔推算基礎狀態（最可靠的 fallback）
data_state = ds.get_pipeline_state(d)
if data_state in ("collected", "scored", "done"):
    stages["collect"]["status"] = "done"
if data_state in ("scored", "done"):
    stages["score"]["status"] = "done"
# generate 只有在確認 pipeline 已結束（不在 RUNNING_TASKS）才從 data_state 推算
if data_state == "done" and date_str not in RUNNING_TASKS:
    stages["generate"]["status"] = "done"

pipeline_status = data_state if data_state != "none" else "idle"
```

**Step 2: 驗證語法**

```bash
python -c "import ast; ast.parse(open('src/web/app.py').read()); print('OK')"
```
Expected: `OK`

**Step 3: 跑測試**

```bash
pytest tests/ -x -q
```
Expected: 106 passed

**Step 4: Commit**

```bash
git add src/web/app.py
git commit -m "fix: skip generate=done inference from data_state while pipeline is running"
```

---

### Task 4：後端 — 加入 RUNNING_PROCS 追蹤與 Stop endpoint

**Files:**
- Modify: `src/web/app.py:30`（新增全域 RUNNING_PROCS dict）
- Modify: `src/web/app.py:703-730`（`_run_pipeline` 函式，把 proc 存入 RUNNING_PROCS）
- Modify: `src/web/app.py:751`（在 `api_run_force` 之後新增 stop endpoint）

**Step 1: 新增全域 RUNNING_PROCS dict**

在 `RUNNING_TASKS: set[str] = set()` 那行（約 L30）後加一行：

```python
RUNNING_PROCS: dict[str, subprocess.Popen] = {}
```

**Step 2: 修改 `_run_pipeline` — 存入 proc 並在結束後刪除**

修改 `_run_pipeline` 函式：

```python
def _run_pipeline(date_str: str, force: bool) -> None:
    """在背景執行 pipeline，並將 stdout/stderr 寫入 logs/{date_str}.log。"""
    RUNNING_TASKS.add(date_str)
    log_path = LOGS_DIR / f"{date_str}.log"
    try:
        cmd = [sys.executable, "-m", "src.cli", "run", "--date", date_str]
        if force:
            cmd.append("--force")
        with open(log_path, "w", encoding="utf-8") as log_file:
            log_file.write(f"=== Pipeline started: {date_str} (force={force}) ===\n")
            log_file.flush()
            env = {**os.environ, "AUTOPB_LOG_FORMAT": "json"}
            proc = subprocess.Popen(
                cmd,
                stdout=log_file,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                env=env,
            )
            RUNNING_PROCS[date_str] = proc   # ← 新增
            proc.wait()
            exit_code = proc.returncode
            log_file.write(f"\n=== Pipeline finished: exit_code={exit_code} ===\n")
    except Exception as e:
        log_path.write_text(f"Pipeline failed to start: {e}\n", encoding="utf-8")
    finally:
        RUNNING_TASKS.discard(date_str)
        RUNNING_PROCS.pop(date_str, None)   # ← 新增
```

**Step 3: 新增 `/api/run/{date_str}/stop` endpoint**

在 `api_run_force` endpoint 之後新增：

```python
@app.post("/api/run/{date_str}/stop")
async def api_run_stop(date_str: str):
    """終止指定日期正在執行的 pipeline。"""
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")
    proc = RUNNING_PROCS.get(date_str)
    if proc is None:
        raise HTTPException(status_code=404, detail="該日期沒有正在執行的 pipeline")
    proc.terminate()   # SIGTERM，讓 pipeline 有機會做 cleanup
    return JSONResponse({"message": f"已發送終止信號（{date_str}）"})
```

**Step 4: 驗證語法**

```bash
python -c "import ast; ast.parse(open('src/web/app.py').read()); print('OK')"
```
Expected: `OK`

**Step 5: 跑測試**

```bash
pytest tests/ -x -q
```
Expected: 106 passed

**Step 6: Commit**

```bash
git add src/web/app.py
git commit -m "feat: add RUNNING_PROCS tracking and /api/run/{date}/stop endpoint"
```

---

### Task 5：前端 — 加入 Stop 按鈕與相關 JS/CSS

**Files:**
- Modify: `src/web/templates/day_detail.html:36-45`（pipeline-header 按鈕區）
- Modify: `src/web/templates/day_detail.html:126-134`（CSS）
- Modify: `src/web/templates/day_detail.html:569-598`（JS：`triggerRun`, `triggerStop`）

**Step 1: 在 pipeline-header 加入 Stop 按鈕**

找到 `<div class="split-btn-wrap">` 區塊，在其之後、`</div>` 結束前加入 Stop 按鈕。
修改後的 pipeline-header 右側：

```html
<div class="pipeline-header-actions">
  <!-- Stop 按鈕（只在 running 時顯示） -->
  <button class="btn-stop" id="btn-stop"
          onclick="triggerStop(dateStr)"
          style="display:none;">■ 停止</button>
  <!-- 重跑按鈕（split button） -->
  <div class="split-btn-wrap">
    <button class="btn-run-main" id="btn-run-main"
            onclick="triggerRun(dateStr, true)">↻ 重跑</button>
    <button class="btn-run-caret" id="btn-run-caret"
            onclick="toggleRunDropdown(event)">▾</button>
    <div class="run-dropdown" id="run-dropdown" style="display:none;">
      <button onclick="triggerRun(dateStr, true); closeRunDropdown()">強制重跑（清除快取）</button>
      <button onclick="triggerRun(dateStr, false); closeRunDropdown()">續跑（保留已有進度）</button>
    </div>
  </div>
</div>
```

注意：原本的 `<div class="split-btn-wrap">` 外層要改為 `<div class="pipeline-header-actions">` 包住兩個按鈕。

**Step 2: 加入 Stop 按鈕 CSS**

在 `/* Split Button */` 區塊後加：

```css
/* Pipeline header actions */
.pipeline-header-actions { display: flex; align-items: center; gap: 0.5rem; }
/* Stop Button */
.btn-stop { padding: 6px 14px; background: rgba(239,68,68,0.15); color: #ef4444;
            border: 1px solid rgba(239,68,68,0.3); border-radius: 6px; cursor: pointer;
            font-size: 0.85rem; font-weight: 600; transition: background 0.15s; }
.btn-stop:hover { background: rgba(239,68,68,0.28); }
.btn-stop:disabled { opacity: 0.45; cursor: not-allowed; }
```

**Step 3: 新增 `triggerStop` 函式與修改 `triggerRun`/`openLogStream`/`event done` 以控制 Stop 按鈕顯示**

在 `// ---- Trigger Run ----` 區塊新增 helper：

```javascript
function setRunningUI(isRunning) {
  const stopBtn  = document.getElementById('btn-stop');
  const mainBtn  = document.getElementById('btn-run-main');
  const caretBtn = document.getElementById('btn-run-caret');
  if (stopBtn)  stopBtn.style.display  = isRunning ? 'block' : 'none';
  if (mainBtn)  mainBtn.disabled  = isRunning;
  if (caretBtn) caretBtn.disabled = isRunning;
}
```

修改 `triggerRun`：將原本的 `mainBtn.disabled = true; caretBtn.disabled = true;` 改為呼叫 `setRunningUI(true)`，
並移除末尾的 `setTimeout(...disabled = false..., 5000)`（改由 done event 控制）：

```javascript
async function triggerRun(dateStr, force) {
  setRunningUI(true);
  closeRunDropdown();

  STAGES.forEach(function(s) {
    stageState[s] = { status: 'pending', elapsed: null };
    updateStageNode(s);
    updateAccordion(s);
    const pre = document.getElementById('slog-' + s);
    if (pre) pre.textContent = '';
    collapseAccordion(s);
  });
  updatePipelineBadge('running');

  try {
    const url = force ? '/api/run/' + dateStr + '/force' : '/api/run/' + dateStr;
    const res  = await fetch(url, { method: 'POST' });
    const data = await res.json();
    showToast(data.message || 'Pipeline 已啟動', '🚀');
    setTimeout(function() { openLogStream(); }, 800);
  } catch(e) {
    showToast('啟動失敗，請確認 server 狀態', '❌');
    updatePipelineBadge('failed');
    setRunningUI(false);
  }
}
```

新增 `triggerStop`：

```javascript
async function triggerStop(dateStr) {
  const stopBtn = document.getElementById('btn-stop');
  if (stopBtn) { stopBtn.disabled = true; stopBtn.textContent = '停止中...'; }
  try {
    const res  = await fetch('/api/run/' + dateStr + '/stop', { method: 'POST' });
    const data = await res.json();
    showToast(data.message || 'Pipeline 已終止', '⛔');
  } catch(e) {
    showToast('終止失敗', '❌');
    if (stopBtn) { stopBtn.disabled = false; stopBtn.textContent = '■ 停止'; }
  }
}
```

修改 `_es.addEventListener('done', ...)` handler，在更新 badge 後加入 `setRunningUI(false)`：

```javascript
_es.addEventListener('done', function() {
  _es.close(); _es = null;
  updatePipelineBadge('done');
  setRunningUI(false);
  setTimeout(function() { location.reload(); }, 1500);
});
```

修改 `openLogStream` 的 `_es.onerror`，在關閉時也重置 UI：

```javascript
_es.onerror = function() {
  if (_es) { _es.close(); _es = null; }
  setRunningUI(false);
};
```

最後，修改 `initStageInfo`：若 `pipeline_status === 'running'` 則呼叫 `setRunningUI(true)`：

```javascript
async function initStageInfo() {
  try {
    const r = await fetch('/api/logs/' + dateStr + '/stage-info');
    if (!r.ok) return;
    const data = await r.json();
    data.stages.forEach(function(s) {
      stageState[s.name] = { status: s.status, elapsed: s.elapsed };
      updateStageNode(s.name);
      updateAccordion(s.name);
      if (s.status === 'done') expandAccordion(s.name);
    });
    updatePipelineBadge(data.pipeline_status);
    if (data.pipeline_status === 'running') {
      setRunningUI(true);
      openLogStream();
    }
  } catch(e) { /* 靜默失敗 */ }
}
```

**Step 4: 驗證 grep**

```bash
grep -n "btn-stop\|triggerStop\|setRunningUI" src/web/templates/day_detail.html
```
Expected: 看到 stop 按鈕定義、CSS、`setRunningUI` 函式、`triggerStop` 函式各出現在正確位置。

**Step 5: 跑測試**

```bash
pytest tests/ -x -q
```
Expected: 106 passed

**Step 6: Commit**

```bash
git add src/web/templates/day_detail.html
git commit -m "feat: add Stop button to pipeline card with GitLab CI/CD style UX"
```

---

## 快速驗收 Checklist

- [ ] `pytest tests/ -x -q` → 106 passed（無 regression）
- [ ] 啟動 web server：`python -m src.cli web`
- [ ] 觸發 pipeline → 確認 Stop 按鈕出現（紅色）
- [ ] 在 generate 階段觀察 badge → 確認顯示 "⟳ 執行中"（不再顯示 "✓ 完成"）
- [ ] 按 Stop → 確認 toast 出現、pipeline 終止、Stop 按鈕消失
- [ ] Pipeline 正常完成時 → 確認 badge 立即更新為 "✓ 完成"（不再等 30 秒）
