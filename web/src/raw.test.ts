import { afterEach, beforeEach, describe, expect, test, vi } from 'vitest';

import { lookupRaw, type RawIndex, type RawItem } from './raw';

/**
 * raw.ts 的單元測試。
 *
 * 檔案系統策略：用 `vi.mock('node:fs')` 而非建臨時目錄 + spy `process.cwd()`。
 * 理由有三：
 *   1. loadRaw() 讀的是 `path.resolve(process.cwd(), '../data/raw')`——真實目錄路徑
 *      正好是本專案的 `data/raw`，任何「用真檔案」的做法都可能誤讀/誤寫真實資料。
 *   2. 「缺目錄」「單檔 JSON 壞掉」這兩個降級分支用 mock 一行就能製造，
 *      臨時目錄則要真的去 chmod / 寫壞檔。
 *   3. spy `process.cwd()` 會連帶影響 vite 的模組解析（動態 import 在同一進程），風險大於收益。
 *
 * 模組快取：loadRaw() 有模組級 `cache` 變數，跨測試必須 `vi.resetModules()` +
 * 動態 import 取新實例，否則第二個測試拿到第一個的快取而變成假綠。
 * 所有 loadRaw 測試一律走 setup() 這條路徑。
 */

interface FsMock {
  readdirSync: ReturnType<typeof vi.fn>;
  readFileSync: ReturnType<typeof vi.fn>;
}

vi.mock('node:fs', () => {
  const readdirSync = vi.fn();
  const readFileSync = vi.fn();
  return { default: { readdirSync, readFileSync }, readdirSync, readFileSync };
});

/** 固定「今天」，讓 RECENT_DAYS(30) 的 cutoff 可預測：cutoff = 2026-07-01。 */
const TODAY = '2026-07-31T12:00:00Z';

/** 一筆 data/raw JSON 的最小合法紀錄（欄位名用 snake_case，與 pipeline 寫出的一致）。 */
function rec(url: string, extra: Record<string, unknown> = {}) {
  return {
    title: '標題',
    abstract: '摘要',
    authors: ['作者甲'],
    organization: 'OpenAI',
    tags: ['llm'],
    source_name: 'arXiv',
    url,
    ...extra,
  };
}

/**
 * 準備一份假的 data/raw 並取得全新的 raw.ts 實例。
 * files 的 value 為陣列/物件時自動 JSON.stringify；為 string 時原樣回傳（用來製造壞 JSON）。
 */
async function setup(files: Record<string, unknown>) {
  vi.resetModules();
  const fs = (await import('node:fs')).default as unknown as FsMock;
  fs.readdirSync.mockReset();
  fs.readFileSync.mockReset();
  fs.readdirSync.mockReturnValue(Object.keys(files));
  fs.readFileSync.mockImplementation((p: string) => {
    const name = String(p).split('/').pop()!;
    const v = files[name];
    return typeof v === 'string' ? v : JSON.stringify(v);
  });
  const mod = await import('./raw');
  return { loadRaw: mod.loadRaw, lookupRaw: mod.lookupRaw, fs };
}

/** 手工組 RawIndex，讓 lookupRaw 的命中邏輯不必碰檔案系統。 */
function mkItem(overrides: Partial<RawItem> = {}): RawItem {
  return {
    title: '標題',
    abstract: '摘要',
    authors: [],
    organization: '',
    tags: [],
    sourceName: 'arXiv',
    url: 'https://example.com/a',
    collectedDate: '2026-07-20',
    signals: [],
    ...overrides,
  };
}

function mkIndex(
  byDayUrl: Record<string, RawItem> = {},
  byUrl: Record<string, RawItem> = {},
): RawIndex {
  return {
    byDayUrl: new Map(Object.entries(byDayUrl)),
    byUrl: new Map(Object.entries(byUrl)),
  };
}

// ---------------------------------------------------------------------------
// lookupRaw：純函式，直接手工組 index
// ---------------------------------------------------------------------------

describe('lookupRaw 命中順序', () => {
  const URL = 'https://example.com/a';

  test('postDay 有對應那天時，回傳「當天」那筆而非 byUrl fallback', () => {
    const sameDay = mkItem({ collectedDate: '2026-06-28', signals: [{ label: '⭐ stars today', value: 141 }] });
    const otherDay = mkItem({ collectedDate: '2026-07-22', signals: [{ label: '⭐ stars today', value: 2040 }] });
    const index = mkIndex({ [`2026-06-28|${URL}`]: sameDay, [`2026-07-22|${URL}`]: otherDay }, { [URL]: otherDay });

    // 這正是實測 69/575 篇踩到的症狀：一篇 2026-06-28 的文章顯示「收集於 2026-07-22」、⭐ 2040。
    const hit = lookupRaw(index, URL, '2026-06-28');
    expect(hit).toBe(sameDay);
    expect(hit?.collectedDate).toBe('2026-06-28');
    expect(hit?.signals[0].value).toBe(141);
  });

  test('postDay 那天不存在時退回 byUrl fallback', () => {
    const fallback = mkItem({ collectedDate: '2026-07-22' });
    const index = mkIndex({ [`2026-07-22|${URL}`]: fallback }, { [URL]: fallback });

    expect(lookupRaw(index, URL, '2026-06-28')).toBe(fallback);
  });

  test('postDay 未提供時直接走 byUrl', () => {
    const item = mkItem();
    const index = mkIndex({ [`2026-07-20|${URL}`]: mkItem({ title: '不該被選中' }) }, { [URL]: item });

    expect(lookupRaw(index, URL, undefined)).toBe(item);
  });

  test('postDay 為空字串時視同未提供，走 byUrl 且不 throw', () => {
    const item = mkItem();
    const index = mkIndex({ [`|${URL}`]: mkItem({ title: '不該被空字串 key 命中' }) }, { [URL]: item });

    expect(lookupRaw(index, URL, '')).toBe(item);
  });

  test('byDayUrl 落空且 byUrl 也沒有時回 null', () => {
    const index = mkIndex({}, {});
    expect(lookupRaw(index, URL, '2026-07-20')).toBeNull();
  });
});

describe('lookupRaw 邊界輸入', () => {
  const URL = 'https://example.com/a';
  const index = mkIndex({ [`2026-07-20|${URL}`]: mkItem() }, { [URL]: mkItem() });

  test('url 為 undefined 回 null', () => {
    expect(lookupRaw(index, undefined, '2026-07-20')).toBeNull();
  });

  test('url 為空字串回 null', () => {
    expect(lookupRaw(index, '', '2026-07-20')).toBeNull();
  });

  test('url 為純空白回 null（normalizeUrl trim 後為空）', () => {
    expect(lookupRaw(index, '   ', '2026-07-20')).toBeNull();
  });

  test('未知 url 回 null', () => {
    expect(lookupRaw(index, 'https://example.com/nope', '2026-07-20')).toBeNull();
  });

  test('空 index 一律回 null 且不 throw', () => {
    const empty = mkIndex();
    expect(() => lookupRaw(empty, URL, '2026-07-20')).not.toThrow();
    expect(lookupRaw(empty, URL, '2026-07-20')).toBeNull();
    expect(lookupRaw(empty, undefined, undefined)).toBeNull();
  });

  test('url 與 postDay 皆未提供回 null', () => {
    expect(lookupRaw(index, undefined, undefined)).toBeNull();
  });
});

describe('lookupRaw 的 url 正規化與 index 端對齊', () => {
  // 計畫裡點名的第一嫌疑：「若 build 通過但 box 沒出現，先查 normalizeUrl 兩端是否對得上」。
  // index 的 key 是 normalizeUrl 後的字串，查詢端必須套用同一套正規化。
  const KEY = 'https://example.com/a';
  const item = mkItem();
  const index = mkIndex({ [`2026-07-20|${KEY}`]: item }, { [KEY]: item });

  test.each([
    ['尾斜線', 'https://example.com/a/'],
    ['多個尾斜線', 'https://example.com/a///'],
    ['http 協定', 'http://example.com/a'],
    ['前後空白', '  https://example.com/a  '],
  ])('%s 的 url 仍能精確命中', (_label, url) => {
    expect(lookupRaw(index, url, '2026-07-20')).toBe(item);
  });
});

// ---------------------------------------------------------------------------
// loadRaw：需要 mock fs
// ---------------------------------------------------------------------------

describe('loadRaw 索引建立', () => {
  beforeEach(() => {
    vi.useFakeTimers({ toFake: ['Date'] });
    vi.setSystemTime(new Date(TODAY));
  });

  afterEach(() => {
    vi.useRealTimers();
    vi.unstubAllEnvs();
  });

  test('byDayUrl 用 day+url 複合 key，同一 url 跨多天各自獨立成筆', async () => {
    const URL = 'https://github.com/foo/bar';
    const { loadRaw } = await setup({
      '2026-07-20.json': [rec(URL, { raw_metadata: { stars_today: 141 } })],
      '2026-07-22.json': [rec(URL, { raw_metadata: { stars_today: 2040 } })],
    });

    const index = loadRaw();

    // 若 key 退化成 url-only，兩天會互相覆寫成 1 筆——這正是 69/575 篇顯示到別天資料的成因。
    expect(index.byDayUrl.size).toBe(2);
    expect(index.byDayUrl.get(`2026-07-20|${URL}`)?.signals).toEqual([{ label: '⭐ stars today', value: 141 }]);
    expect(index.byDayUrl.get(`2026-07-22|${URL}`)?.signals).toEqual([{ label: '⭐ stars today', value: 2040 }]);
  });

  test('byDayUrl 的 key 使用正規化後的 url', async () => {
    const { loadRaw } = await setup({
      '2026-07-20.json': [rec('http://example.com/a/')],
    });

    const index = loadRaw();

    expect([...index.byDayUrl.keys()]).toEqual(['2026-07-20|https://example.com/a']);
    // 原始 url 原樣保留在 item.url，只有 key 被正規化。
    expect(index.byDayUrl.get('2026-07-20|https://example.com/a')?.url).toBe('http://example.com/a/');
  });

  test('collectedDate 取自檔名而非紀錄內容', async () => {
    const { loadRaw } = await setup({
      '2026-07-20.json': [rec('https://example.com/a', { published_date: '2020-01-01' })],
    });

    expect(loadRaw().byUrl.get('https://example.com/a')?.collectedDate).toBe('2026-07-20');
  });

  test('缺漏欄位有安全預設值，tags 過濾掉非字串', async () => {
    const { loadRaw } = await setup({
      '2026-07-20.json': [{ url: 'https://example.com/a', tags: ['llm', 42, null, 'agent'], authors: 'not-an-array' }],
    });

    const item = loadRaw().byUrl.get('https://example.com/a')!;
    expect(item).toMatchObject({
      title: '',
      abstract: '',
      authors: [],
      organization: '',
      tags: ['llm', 'agent'],
      sourceName: '',
      signals: [],
    });
  });

  test('沒有 url 的紀錄整筆跳過，不 throw', async () => {
    const { loadRaw } = await setup({
      '2026-07-20.json': [{ title: '無 url' }, null, { url: '   ' }, rec('https://example.com/ok')],
    });

    const index = loadRaw();
    expect(index.byUrl.size).toBe(1);
    expect([...index.byUrl.keys()]).toEqual(['https://example.com/ok']);
  });
});

describe('loadRaw 的 byUrl fallback 保留最早收集日', () => {
  const URL = 'https://example.com/a';

  beforeEach(() => {
    vi.useFakeTimers({ toFake: ['Date'] });
    vi.setSystemTime(new Date(TODAY));
  });

  afterEach(() => {
    vi.useRealTimers();
    vi.unstubAllEnvs();
  });

  test('同一 url 出現在多天時，byUrl 留最早那天', async () => {
    const { loadRaw } = await setup({
      '2026-07-10.json': [rec(URL, { title: '最早' })],
      '2026-07-20.json': [rec(URL, { title: '中間' })],
      '2026-07-28.json': [rec(URL, { title: '最新' })],
    });

    const item = loadRaw().byUrl.get(URL)!;
    expect(item.collectedDate).toBe('2026-07-10');
    expect(item.title).toBe('最早');
  });

  test('readdirSync 回傳亂序時仍留最早那天（靠 loadRaw 內部 sort）', async () => {
    // Node 不保證 readdirSync 的順序，這裡刻意給日期遞減的順序。
    const { loadRaw } = await setup({
      '2026-07-28.json': [rec(URL, { title: '最新' })],
      '2026-07-10.json': [rec(URL, { title: '最早' })],
      '2026-07-20.json': [rec(URL, { title: '中間' })],
    });

    expect(loadRaw().byUrl.get(URL)?.collectedDate).toBe('2026-07-10');
  });

  test('byUrl 留最早的同時，byDayUrl 每天仍各自完整', async () => {
    const { loadRaw } = await setup({
      '2026-07-10.json': [rec(URL, { raw_metadata: { upvotes: 3 } })],
      '2026-07-28.json': [rec(URL, { raw_metadata: { upvotes: 99 } })],
    });

    const index = loadRaw();
    expect(index.byUrl.get(URL)?.signals).toEqual([{ label: '👍 upvotes', value: 3 }]);
    expect(index.byDayUrl.get(`2026-07-28|${URL}`)?.signals).toEqual([{ label: '👍 upvotes', value: 99 }]);
  });
});

describe('loadRaw 的 signals 擷取', () => {
  beforeEach(() => {
    vi.useFakeTimers({ toFake: ['Date'] });
    vi.setSystemTime(new Date(TODAY));
  });

  afterEach(() => {
    vi.useRealTimers();
    vi.unstubAllEnvs();
  });

  async function signalsOf(raw_metadata: unknown) {
    const { loadRaw } = await setup({
      '2026-07-20.json': [rec('https://example.com/a', { raw_metadata })],
    });
    return loadRaw().byUrl.get('https://example.com/a')!.signals;
  }

  test('五種訊號齊備時，標籤與順序符合 SIGNAL_LABELS', async () => {
    expect(
      await signalsOf({ points: 120, upvotes: 8, citation_count: 5, stars_today: 30, num_comments: 42 }),
    ).toEqual([
      { label: '👍 upvotes', value: 8 },
      { label: '⭐ stars today', value: 30 },
      { label: 'HN points', value: 120 },
      { label: 'HN 留言', value: 42 },
      { label: '📖 citations', value: 5 },
    ]);
  });

  test('值為 0 的訊號不入列', async () => {
    expect(await signalsOf({ upvotes: 0, stars_today: 7 })).toEqual([{ label: '⭐ stars today', value: 7 }]);
  });

  test('負數不入列', async () => {
    expect(await signalsOf({ upvotes: -5, stars_today: 7 })).toEqual([{ label: '⭐ stars today', value: 7 }]);
  });

  test('非數值（字串 / null / 物件 / NaN）不入列', async () => {
    expect(await signalsOf({ upvotes: 'many', points: null, num_comments: {}, citation_count: NaN, stars_today: 7 }))
      .toEqual([{ label: '⭐ stars today', value: 7 }]);
  });

  test('raw_metadata 缺漏或非物件時 signals 為空陣列', async () => {
    expect(await signalsOf(undefined)).toEqual([]);
    expect(await signalsOf(null)).toEqual([]);
    expect(await signalsOf('not-an-object')).toEqual([]);
  });

  test('raw_metadata 只帶不在白名單的欄位時 signals 為空', async () => {
    expect(await signalsOf({ score: 88, rank: 1 })).toEqual([]);
  });
});

describe('loadRaw 只讀近 RECENT_DAYS(30) 天', () => {
  beforeEach(() => {
    vi.useFakeTimers({ toFake: ['Date'] });
    vi.setSystemTime(new Date(TODAY)); // cutoff = 2026-07-01
  });

  afterEach(() => {
    vi.useRealTimers();
    vi.unstubAllEnvs();
  });

  test('cutoff 之前的檔案完全不讀（連 readFileSync 都不呼叫）', async () => {
    const { loadRaw, fs } = await setup({
      '2026-05-01.json': [rec('https://example.com/ancient')],
      '2026-06-30.json': [rec('https://example.com/old')],
      '2026-07-01.json': [rec('https://example.com/edge')],
      '2026-07-30.json': [rec('https://example.com/fresh')],
    });

    const index = loadRaw();

    expect([...index.byUrl.keys()].sort()).toEqual(['https://example.com/edge', 'https://example.com/fresh']);
    expect(fs.readFileSync).toHaveBeenCalledTimes(2);
  });

  test('非 .json 檔案被忽略', async () => {
    const { loadRaw, fs } = await setup({
      '2026-07-20.json': [rec('https://example.com/a')],
      '2026-07-21.txt': 'not json',
      'README.md': '# hi',
    });

    expect(loadRaw().byUrl.size).toBe(1);
    expect(fs.readFileSync).toHaveBeenCalledTimes(1);
  });
});

describe('loadRaw 的優雅降級', () => {
  beforeEach(() => {
    vi.useFakeTimers({ toFake: ['Date'] });
    vi.setSystemTime(new Date(TODAY));
  });

  afterEach(() => {
    vi.useRealTimers();
    vi.unstubAllEnvs();
  });

  test('缺 data/raw 目錄時回空 index 且不 throw', async () => {
    vi.resetModules();
    const fs = (await import('node:fs')).default as unknown as FsMock;
    fs.readdirSync.mockReset();
    fs.readFileSync.mockReset();
    fs.readdirSync.mockImplementation(() => {
      throw Object.assign(new Error('ENOENT: no such file or directory'), { code: 'ENOENT' });
    });
    const { loadRaw } = await import('./raw');

    let index!: RawIndex;
    expect(() => {
      index = loadRaw();
    }).not.toThrow();
    expect(index.byDayUrl.size).toBe(0);
    expect(index.byUrl.size).toBe(0);
    // 空 index 也要能安全查詢
    expect(lookupRaw(index, 'https://example.com/a', '2026-07-20')).toBeNull();
  });

  test('單一檔案 JSON 壞掉時跳過該檔，其餘正常', async () => {
    const { loadRaw } = await setup({
      '2026-07-20.json': '{ 這不是合法 JSON',
      '2026-07-21.json': [rec('https://example.com/ok')],
    });

    const index = loadRaw();
    expect([...index.byUrl.keys()]).toEqual(['https://example.com/ok']);
  });

  test('單一檔案 readFileSync 拋錯時跳過該檔，其餘正常', async () => {
    vi.resetModules();
    const fs = (await import('node:fs')).default as unknown as FsMock;
    fs.readdirSync.mockReset();
    fs.readFileSync.mockReset();
    fs.readdirSync.mockReturnValue(['2026-07-20.json', '2026-07-21.json']);
    fs.readFileSync.mockImplementation((p: string) => {
      if (String(p).includes('2026-07-20')) throw new Error('EACCES');
      return JSON.stringify([rec('https://example.com/ok')]);
    });
    const { loadRaw } = await import('./raw');

    expect([...loadRaw().byUrl.keys()]).toEqual(['https://example.com/ok']);
  });

  test('JSON 不是陣列時跳過該檔', async () => {
    const { loadRaw } = await setup({
      '2026-07-20.json': { items: [rec('https://example.com/a')] },
      '2026-07-21.json': [rec('https://example.com/ok')],
    });

    expect([...loadRaw().byUrl.keys()]).toEqual(['https://example.com/ok']);
  });

  test('全部檔案都壞掉時回空 index', async () => {
    const { loadRaw } = await setup({
      '2026-07-20.json': 'broken',
      '2026-07-21.json': 'also broken',
    });

    const index = loadRaw();
    expect(index.byDayUrl.size).toBe(0);
    expect(index.byUrl.size).toBe(0);
  });
});

describe('loadRaw 的模組級快取', () => {
  beforeEach(() => {
    vi.useFakeTimers({ toFake: ['Date'] });
    vi.setSystemTime(new Date(TODAY));
  });

  afterEach(() => {
    vi.useRealTimers();
    vi.unstubAllEnvs();
  });

  test('build 模式（DEV=false）快取結果，第二次呼叫不再讀目錄', async () => {
    vi.stubEnv('DEV', false);
    const { loadRaw, fs } = await setup({ '2026-07-20.json': [rec('https://example.com/a')] });

    const first = loadRaw();
    const second = loadRaw();

    expect(second).toBe(first);
    expect(fs.readdirSync).toHaveBeenCalledTimes(1);
  });

  test('dev 模式（DEV=true）不快取，每次都重讀（才看得到 pipeline 新寫入的檔）', async () => {
    vi.stubEnv('DEV', true);
    const { loadRaw, fs } = await setup({ '2026-07-20.json': [rec('https://example.com/a')] });

    loadRaw();
    // 模擬 pipeline 在 dev server 運行期間寫入新的一天
    fs.readdirSync.mockReturnValue(['2026-07-20.json', '2026-07-21.json']);
    fs.readFileSync.mockImplementation((p: string) =>
      JSON.stringify([rec(String(p).includes('2026-07-21') ? 'https://example.com/new' : 'https://example.com/a')]),
    );
    const second = loadRaw();

    expect(fs.readdirSync).toHaveBeenCalledTimes(2);
    expect(second.byUrl.has('https://example.com/new')).toBe(true);
  });

  test('缺目錄的空 index 同樣進快取（DEV=false 時不重複探測）', async () => {
    vi.stubEnv('DEV', false);
    vi.resetModules();
    const fs = (await import('node:fs')).default as unknown as FsMock;
    fs.readdirSync.mockReset();
    fs.readFileSync.mockReset();
    fs.readdirSync.mockImplementation(() => {
      throw new Error('ENOENT');
    });
    const { loadRaw } = await import('./raw');

    loadRaw();
    loadRaw();

    expect(fs.readdirSync).toHaveBeenCalledTimes(1);
  });
});

// ---------------------------------------------------------------------------
// loadRaw + lookupRaw 串起來：還原實際踩過的 bug 情境
// ---------------------------------------------------------------------------

describe('loadRaw + lookupRaw 整合', () => {
  beforeEach(() => {
    vi.useFakeTimers({ toFake: ['Date'] });
    vi.setSystemTime(new Date(TODAY));
  });

  afterEach(() => {
    vi.useRealTimers();
    vi.unstubAllEnvs();
  });

  test('跨多天收集的同一 url，post 拿到自己那天的資料', async () => {
    const URL = 'https://github.com/foo/bar';
    const { loadRaw, lookupRaw: lookup } = await setup({
      '2026-07-10.json': [rec(URL, { raw_metadata: { stars_today: 141 } })],
      '2026-07-22.json': [rec(URL, { raw_metadata: { stars_today: 2040 } })],
    });
    const index = loadRaw();

    const early = lookup(index, URL, '2026-07-10');
    expect(early?.collectedDate).toBe('2026-07-10');
    expect(early?.signals).toEqual([{ label: '⭐ stars today', value: 141 }]);

    const late = lookup(index, URL, '2026-07-22');
    expect(late?.collectedDate).toBe('2026-07-22');
    expect(late?.signals).toEqual([{ label: '⭐ stars today', value: 2040 }]);
  });

  test('post 日期與所有收集日都不同時，退回最早那筆', async () => {
    const URL = 'https://github.com/foo/bar';
    const { loadRaw, lookupRaw: lookup } = await setup({
      '2026-07-10.json': [rec(URL, { title: '最早' })],
      '2026-07-22.json': [rec(URL, { title: '最新' })],
    });

    // raw 該天已被 clean 清掉（或 post 日期本就與收集日不同）
    expect(lookup(loadRaw(), URL, '2026-07-15')?.title).toBe('最早');
  });
});
