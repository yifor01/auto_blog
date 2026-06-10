/**
 * Shared facet-filter + search logic for listing pages.
 *
 * facetKey: the secondary filter dimension
 *   - 'source' → index.astro (⚡ 每日自動)  — data-source="…"
 *   - 'tag'    → curated.astro (★ 精選)    — data-tags="a|b|c"
 *
 * The search input is debounced (150 ms) to avoid scanning the full
 * item list on every keystroke. Facet button clicks apply immediately.
 */

function debounce<T extends (...args: unknown[]) => void>(fn: T, ms: number): T {
  let timer: ReturnType<typeof setTimeout>;
  return ((...args: unknown[]) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), ms);
  }) as T;
}

export function initFilter(facetKey: 'source' | 'tag'): void {
  const searchEl = document.getElementById('search') as HTMLInputElement;
  const resetEl = document.getElementById('reset') as HTMLButtonElement;
  const resultCountEl = document.getElementById('result-count')!;
  const emptyEl = document.querySelector<HTMLElement>('.empty')!;
  const items = [...document.querySelectorAll<HTMLElement>('.post-item')];
  const facetBtns = [...document.querySelectorAll<HTMLButtonElement>('.facet-btn')];

  // State keys: q, month, and the page-specific facet dimension.
  const state: { [key: string]: string } = { q: '', month: '', [facetKey]: '' };

  function checkFacetItem(item: HTMLElement): boolean {
    const val = state[facetKey];
    if (!val) return true;
    if (facetKey === 'source') return item.dataset.source === val;
    // tag dimension: values stored as pipe-separated list in data-tags
    return (item.dataset.tags ?? '').split('|').includes(val);
  }

  function apply(): void {
    let visible = 0;
    for (const item of items) {
      // data-search is already lowercased at build time; query is lowercased on input.
      const okSearch = !state.q || (item.dataset.search ?? '').includes(state.q);
      const okMonth = !state.month || item.dataset.month === state.month;
      const okFacet = checkFacetItem(item);
      const show = okSearch && okMonth && okFacet;
      item.hidden = !show;
      if (show) visible++;
    }
    resultCountEl.textContent = String(visible);
    emptyEl.hidden = visible !== 0;
    resetEl.hidden = !(state.q || state[facetKey] || state.month);

    for (const btn of facetBtns) {
      const active =
        (btn.dataset.type === facetKey && btn.dataset.value === state[facetKey]) ||
        (btn.dataset.type === 'month' && btn.dataset.value === state.month);
      btn.classList.toggle('active', active);
    }
  }

  const debouncedApply = debounce(apply, 150);

  searchEl.addEventListener('input', () => {
    state.q = searchEl.value.trim().toLowerCase();
    debouncedApply();
  });

  for (const btn of facetBtns) {
    btn.addEventListener('click', () => {
      const type = btn.dataset.type as string;
      const value = btn.dataset.value ?? '';
      // Only handle known dimension types; toggle off on second click.
      if (type === 'month' || type === facetKey) {
        state[type] = state[type] === value ? '' : value;
        apply();
      }
    });
  }

  resetEl.addEventListener('click', () => {
    state.q = '';
    state.month = '';
    state[facetKey] = '';
    searchEl.value = '';
    apply();
  });
}
