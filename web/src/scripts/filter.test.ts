import { beforeEach, describe, expect, test } from 'vitest';

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
