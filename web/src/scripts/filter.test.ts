import { beforeEach, describe, expect, test, vi } from 'vitest';

import { initFilter } from './filter';

/**
 * 列表頁最小骨架，屬性名稱與 index.astro 的 .post-item 一致。
 * initFilter() 沒有 #search 也沒有 .post-item 時會早退，fixture 兩者都給。
 */
const LISTING_FIXTURE = `
  <input id="search" type="search" />
  <button id="reset" class="reset" hidden>✕ 清除篩選</button>
  <button class="facet-btn" data-type="source" data-value="arxiv">arXiv</button>
  <button class="facet-btn" data-type="source" data-value="hackernews">HN</button>
  <span id="result-count">2</span>
  <ul>
    <li class="day-header" data-day="2026-07-30"></li>
    <li class="post-item" data-id="a" data-day="2026-07-30" data-month="2026-07"
        data-source="arxiv" data-tags="llm|agent" data-score="72" data-search="alpha"></li>
    <li class="post-item" data-id="b" data-day="2026-07-30" data-month="2026-07"
        data-source="hackernews" data-tags="tooling" data-score="55" data-search="beta"></li>
  </ul>
  <p class="empty" hidden>沒有符合條件的文章。</p>
`;

/** Astro ClientRouter 在每次導航時寫進 history 的 state。 */
const ROUTER_STATE = { index: 3, scrollX: 0, scrollY: 120 };

beforeEach(() => {
  localStorage.clear();
  history.replaceState(ROUTER_STATE, '', '/');
  document.body.innerHTML = LISTING_FIXTURE;
});

describe('syncHash 與 ClientRouter 的 history.state 共存', () => {
  test('光載入列表頁不會清掉 ClientRouter 的 history.state', () => {
    initFilter();

    // state 被蓋成 null，ClientRouter 的 popstate handler 就不接手，
    // 症狀是按上一頁 URL 退回去了但畫面不變。
    expect(history.state).not.toBeNull();
    expect(history.state).toEqual(ROUTER_STATE);
  });

  test('點篩選鈕更新 hash 之後仍保留 history.state', () => {
    initFilter();

    const btn = document.querySelector<HTMLButtonElement>('.facet-btn[data-value="arxiv"]')!;
    btn.click();

    expect(location.hash).toBe('#source=arxiv');
    expect(history.state).toEqual(ROUTER_STATE);
  });

  test('清空篩選回到 pathname 時仍保留 history.state', () => {
    initFilter();

    const btn = document.querySelector<HTMLButtonElement>('.facet-btn[data-value="arxiv"]')!;
    btn.click();
    btn.click(); // 再點一次取消

    expect(location.hash).toBe('');
    expect(location.pathname).toBe('/');
    expect(history.state).toEqual(ROUTER_STATE);
  });
});

/**
 * 每日收合：同一天第 6 篇起帶 data-extra，預設藏起來，由 .day-more 的按鈕展開。
 * 只有「日期排序 + 沒有任何篩選」時收合；一旦有篩選就全部顯示符合的。
 */
function collapseFixture(): string {
  const day = '2026-10-31';
  const posts = Array.from({ length: 7 }, (_, i) => {
    const extra = i >= 5 ? ' data-extra' : '';
    const src = i === 6 ? 'arxiv' : 'hackernews';
    return `<li class="post-item" data-id="p${i}" data-day="${day}" data-month="2026-10"
        data-source="${src}" data-tags="" data-score="${90 - i}" data-search="post${i}"${extra}>
        <a class="post-link" href="/daily/p${i}"></a></li>`;
  }).join('');
  return `
    <input id="search" type="search" />
    <button id="reset" class="reset" hidden></button>
    <button class="sort-btn" data-sort="date">最新</button>
    <button class="sort-btn" data-sort="score">分數</button>
    <button class="facet-btn" data-type="source" data-value="arxiv">arXiv</button>
    <button class="day-cell" data-jump="${day}">31</button>
    <button class="day-cell" data-jump="2026-10-30">30</button>
    <span id="result-count"></span>
    <ul>
      <li class="day-header" data-day="${day}"></li>
      ${posts}
      <li class="day-more" data-day="${day}">
        <button class="more-btn"><span class="more-label"></span></button>
      </li>
      <li class="day-header" data-day="2026-10-30"></li>
      <li class="post-item" data-id="q0" data-day="2026-10-30" data-month="2026-10"
          data-source="hackernews" data-tags="" data-score="50" data-search="other"></li>
    </ul>
    <p class="empty" hidden></p>
  `;
}

const $ = <T extends HTMLElement = HTMLElement>(sel: string) => document.querySelector<T>(sel)!;
const extras = () => [...document.querySelectorAll<HTMLElement>('.post-item[data-extra]')];
const moreRow = () => $('.day-more[data-day="2026-10-31"]');

describe('每日收合', () => {
  beforeEach(() => {
    document.body.innerHTML = collapseFixture();
  });

  test('預設只顯示每天前 5 篇，展開列寫出被藏的篇數', () => {
    initFilter();

    expect(extras().every((el) => el.hidden)).toBe(true);
    expect(moreRow().hidden).toBe(false);
    expect($('.more-label').textContent).toContain('2');
  });

  test('結果數算的是符合條件的篇數，不扣掉收合的', () => {
    initFilter();

    expect($('#result-count').textContent).toBe('8');
  });

  test('點展開顯示該日全部文章，再點一次收回', () => {
    initFilter();

    $('.more-btn').click();
    expect(extras().every((el) => !el.hidden)).toBe(true);
    expect(moreRow().hidden).toBe(false);
    expect($('.more-label').textContent).toContain('收合');

    $('.more-btn').click();
    expect(extras().every((el) => el.hidden)).toBe(true);
  });

  test('搜尋時不收合：符合的第 6 篇以後也要出現', async () => {
    // 先排空前面測試留下的非同步事件。不排空時，整批跑會有一筆晚到的事件
    // 觸發 readHash() 把搜尋框清空（單獨跑這個測試則會過）。推測是 happy-dom
    // 排進佇列的 hashchange；沒有直接證實。
    await new Promise((r) => setTimeout(r, 0));
    initFilter();

    const search = $<HTMLInputElement>('#search');
    search.value = 'post6';
    search.dispatchEvent(new Event('input'));
    await new Promise((r) => setTimeout(r, 200)); // 搜尋有 150ms debounce

    expect($('.post-item[data-id="p6"]').hidden).toBe(false);
    expect(moreRow().hidden).toBe(true);
  });

  test('篩選來源時不收合', () => {
    initFilter();

    $('.facet-btn[data-value="arxiv"]').click();

    expect($('.post-item[data-id="p6"]').hidden).toBe(false);
    expect(moreRow().hidden).toBe(true);
  });

  test('分數排序時不收合', () => {
    initFilter();

    $('.sort-btn[data-sort="score"]').click();

    expect(extras().every((el) => !el.hidden)).toBe(true);
    expect(moreRow().hidden).toBe(true);
  });

  test('j 鍵跳過收合中的文章，直接進到下一天', () => {
    Element.prototype.scrollIntoView = vi.fn();
    initFilter();

    for (let i = 0; i < 6; i++) {
      document.dispatchEvent(new KeyboardEvent('keydown', { key: 'j' }));
    }

    expect($('.kbd-focus').dataset.id).toBe('q0');
  });
});

describe('日期跳轉月曆', () => {
  beforeEach(() => {
    document.body.innerHTML = collapseFixture();
  });

  test('點日期格捲到該日第一篇', () => {
    const spy = vi.fn();
    Element.prototype.scrollIntoView = spy;
    initFilter();

    $('.day-cell[data-jump="2026-10-30"]').click();

    expect(spy).toHaveBeenCalledTimes(1);
    expect(spy.mock.contexts[0]).toBe($('.post-item[data-id="q0"]'));
  });

  test('篩選後沒有文章的日子，日期格變成不能點', () => {
    initFilter();

    $('.facet-btn[data-value="arxiv"]').click();

    expect($<HTMLButtonElement>('.day-cell[data-jump="2026-10-30"]').disabled).toBe(true);
    expect($<HTMLButtonElement>('.day-cell[data-jump="2026-10-31"]').disabled).toBe(false);
  });
});
