/**
 * Shared facet-filter + search + reading-state logic for listing pages.
 *
 * Dimensions are data-driven by the buttons present on the page:
 *   - month  → data-month="YYYY-MM"
 *   - source → data-source="…"        (index.astro)
 *   - tag    → data-tags="a|b|c"      (index.astro + curated.astro)
 *
 * Extra features (all optional — elements absent on a page are skipped):
 *   - sort buttons   `.sort-btn[data-sort=date|score]` — score sort uses
 *     flex `order` so DOM stays put; day headers hide in score mode
 *   - toggle buttons `.toggle-btn[data-toggle=unread|bm]`
 *   - bookmark stars `.bm-btn[data-id]`  (localStorage `apb-bm`)
 *   - read state     localStorage `apb-read` (detail pages mark on visit)
 *   - density toggle `#density` — body.compact hides summaries
 *   - keyboard: `/` focus search, j/k move, Enter open, b bookmark
 *   - filter state mirrored into location.hash (shareable)
 *
 * The search input is debounced (150 ms); facet clicks apply immediately.
 */

type Dim = 'month' | 'source' | 'tag';
const DIMS: Dim[] = ['month', 'source', 'tag'];

const LS_READ = 'apb-read';
const LS_BM = 'apb-bm';
const LS_COMPACT = 'apb-compact';

function loadSet(key: string): Set<string> {
  try {
    const raw = JSON.parse(localStorage.getItem(key) ?? '[]');
    return new Set(Array.isArray(raw) ? raw : []);
  } catch {
    return new Set();
  }
}

function saveSet(key: string, set: Set<string>): void {
  localStorage.setItem(key, JSON.stringify([...set]));
}

function debounce<T extends (...args: unknown[]) => void>(fn: T, ms: number): T {
  let timer: ReturnType<typeof setTimeout>;
  return ((...args: unknown[]) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), ms);
  }) as T;
}

export function initFilter(): void {
  const searchEl = document.getElementById('search') as HTMLInputElement | null;
  const resetEl = document.getElementById('reset') as HTMLButtonElement | null;
  const resultCountEl = document.getElementById('result-count');
  const emptyEl = document.querySelector<HTMLElement>('.empty');
  const items = [...document.querySelectorAll<HTMLElement>('.post-item')];
  const facetBtns = [...document.querySelectorAll<HTMLButtonElement>('.facet-btn')];
  const sortBtns = [...document.querySelectorAll<HTMLButtonElement>('.sort-btn')];
  const toggleBtns = [...document.querySelectorAll<HTMLButtonElement>('.toggle-btn')];
  const dayHeaders = [...document.querySelectorAll<HTMLElement>('.day-header')];
  const densityBtn = document.getElementById('density');

  const read = loadSet(LS_READ);
  const bm = loadSet(LS_BM);

  const state: Record<string, string> = {
    q: '',
    month: '',
    source: '',
    tag: '',
    sort: 'date',
    unread: '',
    bm: '',
  };

  // --- 已讀 / 收藏狀態渲染 ---
  for (const item of items) {
    const id = item.dataset.id ?? '';
    item.classList.toggle('is-read', read.has(id));
    item.classList.toggle('is-bm', bm.has(id));
  }

  // --- 「今天 / 昨天」相對標籤（client 端判定，避免 build 時間誤差）---
  const todayStr = new Date().toISOString().slice(0, 10);
  const yesterdayStr = new Date(Date.now() - 86400_000).toISOString().slice(0, 10);
  for (const h of dayHeaders) {
    const rel = h.querySelector<HTMLElement>('.day-rel');
    if (!rel) continue;
    if (h.dataset.day === todayStr) rel.textContent = '今天';
    else if (h.dataset.day === yesterdayStr) rel.textContent = '昨天';
  }

  function checkDim(item: HTMLElement, dim: Dim): boolean {
    const val = state[dim];
    if (!val) return true;
    if (dim === 'tag') return (item.dataset.tags ?? '').split('|').includes(val);
    return item.dataset[dim] === val;
  }

  function apply(): void {
    let visible = 0;
    const dayVisible = new Map<string, number>();
    for (const item of items) {
      const okSearch = !state.q || (item.dataset.search ?? '').includes(state.q);
      const okDims = DIMS.every((d) => checkDim(item, d));
      const okUnread = !state.unread || !read.has(item.dataset.id ?? '');
      const okBm = !state.bm || bm.has(item.dataset.id ?? '');
      const show = okSearch && okDims && okUnread && okBm;
      item.hidden = !show;
      if (show) {
        visible++;
        const day = item.dataset.day ?? '';
        dayVisible.set(day, (dayVisible.get(day) ?? 0) + 1);
      }
      // score 排序：用 flex order 重排，免動 DOM
      item.style.order =
        state.sort === 'score' ? String(-Math.round(Number(item.dataset.score ?? 0))) : '';
    }

    // 日期標頭：score 模式全部隱藏；date 模式隱藏該日 0 篇的
    for (const h of dayHeaders) {
      h.hidden = state.sort === 'score' || !(dayVisible.get(h.dataset.day ?? '') ?? 0);
    }

    if (resultCountEl) resultCountEl.textContent = String(visible);
    if (emptyEl) emptyEl.hidden = visible !== 0;
    if (resetEl)
      resetEl.hidden = !(
        state.q || state.month || state.source || state.tag || state.unread || state.bm
      );

    for (const btn of facetBtns) {
      const t = btn.dataset.type ?? '';
      btn.classList.toggle('active', state[t] === btn.dataset.value);
    }
    for (const btn of sortBtns) {
      btn.classList.toggle('active', btn.dataset.sort === state.sort);
    }
    for (const btn of toggleBtns) {
      btn.classList.toggle('active', !!state[btn.dataset.toggle ?? '']);
    }
    syncHash();
  }

  // --- URL hash 同步（可分享篩選狀態）---
  function syncHash(): void {
    const p = new URLSearchParams();
    for (const k of ['q', 'month', 'source', 'tag', 'unread', 'bm']) {
      if (state[k]) p.set(k, state[k]);
    }
    if (state.sort !== 'date') p.set('sort', state.sort);
    const s = p.toString();
    history.replaceState(null, '', s ? `#${s}` : location.pathname);
  }

  function readHash(): void {
    const p = new URLSearchParams(location.hash.slice(1));
    for (const k of ['q', 'month', 'source', 'tag', 'unread', 'bm']) {
      state[k] = p.get(k) ?? '';
    }
    state.sort = p.get('sort') ?? 'date';
    if (searchEl) searchEl.value = state.q;
  }

  // 同頁 hash 導航（如詳情頁 tag 連結回列表）不會 reload，需監聽重新套用
  window.addEventListener('hashchange', () => {
    readHash();
    apply();
  });

  const debouncedApply = debounce(apply, 150);

  searchEl?.addEventListener('input', () => {
    state.q = searchEl.value.trim().toLowerCase();
    debouncedApply();
  });

  for (const btn of facetBtns) {
    btn.addEventListener('click', () => {
      const type = btn.dataset.type as Dim;
      if (!DIMS.includes(type)) return;
      const value = btn.dataset.value ?? '';
      state[type] = state[type] === value ? '' : value;
      apply();
    });
  }

  for (const btn of sortBtns) {
    btn.addEventListener('click', () => {
      state.sort = btn.dataset.sort ?? 'date';
      apply();
    });
  }

  for (const btn of toggleBtns) {
    btn.addEventListener('click', () => {
      const key = btn.dataset.toggle ?? '';
      state[key] = state[key] ? '' : '1';
      apply();
    });
  }

  resetEl?.addEventListener('click', () => {
    for (const k of ['q', 'month', 'source', 'tag', 'unread', 'bm']) state[k] = '';
    if (searchEl) searchEl.value = '';
    apply();
  });

  // --- 收藏星號 ---
  function toggleBm(item: HTMLElement): void {
    const id = item.dataset.id ?? '';
    if (!id) return;
    if (bm.has(id)) bm.delete(id);
    else bm.add(id);
    saveSet(LS_BM, bm);
    item.classList.toggle('is-bm', bm.has(id));
    if (state.bm) apply(); // 收藏篩選中取消收藏 → 即時消失
  }

  for (const btn of document.querySelectorAll<HTMLButtonElement>('.bm-btn')) {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      const item = btn.closest<HTMLElement>('.post-item');
      if (item) toggleBm(item);
    });
  }

  // --- 精簡模式 ---
  if (localStorage.getItem(LS_COMPACT) === '1') document.body.classList.add('compact');
  densityBtn?.addEventListener('click', () => {
    const on = document.body.classList.toggle('compact');
    localStorage.setItem(LS_COMPACT, on ? '1' : '0');
  });

  // --- 鍵盤操作 ---
  let cursor = -1;
  function visibleItems(): HTMLElement[] {
    return items.filter((i) => !i.hidden);
  }
  function moveCursor(delta: number): void {
    const vis = visibleItems();
    if (!vis.length) return;
    const current = vis.findIndex((i) => i.classList.contains('kbd-focus'));
    const next = Math.min(vis.length - 1, Math.max(0, (current === -1 ? -1 : current) + delta));
    for (const i of items) i.classList.remove('kbd-focus');
    vis[next].classList.add('kbd-focus');
    vis[next].scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    cursor = next;
  }

  document.addEventListener('keydown', (e) => {
    const target = e.target as HTMLElement;
    if (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA') {
      if (e.key === 'Escape') (target as HTMLInputElement).blur();
      return;
    }
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    if (e.key === '/') {
      e.preventDefault();
      searchEl?.focus();
    } else if (e.key === 'j') {
      moveCursor(1);
    } else if (e.key === 'k') {
      moveCursor(-1);
    } else if (e.key === 'Enter' && cursor >= 0) {
      const focused = document.querySelector<HTMLElement>('.post-item.kbd-focus a.post-link');
      focused?.click();
    } else if (e.key === 'b' && cursor >= 0) {
      const focused = document.querySelector<HTMLElement>('.post-item.kbd-focus');
      if (focused) toggleBm(focused);
    }
  });

  readHash();
  apply();
}

// 詳情頁呼叫：標記已讀
export function markRead(id: string): void {
  const read = loadSet(LS_READ);
  if (read.has(id)) return;
  read.add(id);
  saveSet(LS_READ, read);
}
