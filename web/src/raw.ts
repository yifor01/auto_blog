import fs from 'node:fs';
import path from 'node:path';
import { normalizeUrl } from './enrich';
import { RECENT_DAYS } from './utils';

// 從 data/raw/{date}.json 讀取來源原始資料，供詳情頁的「原始資料」box 使用。
// why 不共用 enrich.ts（data/scored）：pinned 文免評分、不在 scored 裡。
// 實測近 30 天 575 篇 posts：用 scored 查只命中 565（miss 的 10 篇正好全是 pinned），
// 用 raw 查則 575/575 全中。
// raw JSON 不在 web/ 內，故用 fs 直讀（cwd = web/，與 content.config.ts 的 glob base 同基準）。

export interface RawItem {
  title: string;
  abstract: string;
  authors: string[];
  organization: string;
  tags: string[];
  sourceName: string;
  url: string;
  collectedDate: string; // YYYY-MM-DD
  signals: { label: string; value: number }[];
}

// 同一 url 可能被多天收集到（跨日去重窗口之外），每天的 signals（stars_today 等）都不同。
// box 掛在特定 post 上，要顯示的是「該 post 當天」那一筆，因此主索引用 day+url 複合 key；
// byUrl 只是查不到精確日期時的保底。
export interface RawIndex {
  byDayUrl: Map<string, RawItem>; // key = `${day}|${normalizeUrl(url)}`
  byUrl: Map<string, RawItem>; // key = normalizeUrl(url)，保留最早收集的那一天（見 loadRaw 註解）
}

// raw_metadata 中值得展示的天然訊號；沒有或為 0 的不顯示
const SIGNAL_LABELS: [string, string][] = [
  ['upvotes', '👍 upvotes'],
  ['stars_today', '⭐ stars today'],
  ['points', 'HN points'],
  ['num_comments', 'HN 留言'],
  ['citation_count', '📖 citations'],
];

function toSignals(meta: unknown): { label: string; value: number }[] {
  if (!meta || typeof meta !== 'object') return [];
  const m = meta as Record<string, unknown>;
  const out: { label: string; value: number }[] = [];
  for (const [key, label] of SIGNAL_LABELS) {
    const v = Number(m[key]);
    if (Number.isFinite(v) && v > 0) out.push({ label, value: v });
  }
  return out;
}

let cache: RawIndex | null = null;

export function loadRaw(): RawIndex {
  // dev server 是長駐進程，快取會看不到 pipeline 新寫入的 raw JSON；只在 build 時快取
  if (import.meta.env?.DEV) cache = null;
  if (cache) return cache;

  const index: RawIndex = { byDayUrl: new Map(), byUrl: new Map() };
  const dir = path.resolve(process.cwd(), '../data/raw');
  let files: string[] = [];
  try {
    // 排序成日期遞增，讓 byUrl 的「先寫入者保留」= 保留最早收集日，結果與 readdirSync
    // 的 OS/filesystem 順序無關（Node 不保證該順序），確保每次 build 產出相同。
    files = fs.readdirSync(dir).filter((f) => f.endsWith('.json')).sort();
  } catch {
    cache = index;
    return index; // 沒有 raw 資料時優雅降級
  }

  // 詳情頁只 build 近 RECENT_DAYS 天，多讀的檔案純屬浪費 build 時間
  const cutoff = new Date(Date.now() - RECENT_DAYS * 86400_000).toISOString().slice(0, 10);

  for (const file of files) {
    const day = file.slice(0, 10);
    if (day < cutoff) continue;
    let parsed: unknown;
    try {
      parsed = JSON.parse(fs.readFileSync(path.join(dir, file), 'utf-8'));
    } catch {
      continue;
    }
    if (!Array.isArray(parsed)) continue;
    for (const it of parsed) {
      const url = normalizeUrl(it?.url);
      if (!url) continue;
      const item: RawItem = {
        title: it.title ?? '',
        abstract: it.abstract ?? '',
        authors: Array.isArray(it.authors) ? it.authors : [],
        organization: it.organization ?? '',
        tags: Array.isArray(it.tags) ? it.tags.filter((t: unknown) => typeof t === 'string') : [],
        sourceName: it.source_name ?? '',
        url: it.url ?? '',
        collectedDate: day,
        signals: toSignals(it.raw_metadata),
      };
      index.byDayUrl.set(`${day}|${url}`, item);
      // fallback 保留「最早」收集日而非最新：post 幾乎都在該項目首次被收集的那天生成
      // （實測 575 篇中最舊日與 post 日期相符 521 篇、最新日只有 506 篇），
      // 精確 key 落空時，最早那筆離 post 日期最近、stars_today 之類的訊號也最不失真。
      if (!index.byUrl.has(url)) index.byUrl.set(url, item);
    }
  }

  cache = index;
  return index;
}

// 查某篇 post 對應的原始資料：先用 post 日期精準命中當天那筆，
// 落空才退回 url-only（例如 post 日期與收集日不同，或 raw 已被 clean 清掉該天）。
export function lookupRaw(
  index: RawIndex,
  url: string | undefined,
  postDay: string | undefined,
): RawItem | null {
  const key = normalizeUrl(url);
  if (!key) return null;
  if (postDay) {
    const exact = index.byDayUrl.get(`${postDay}|${key}`);
    if (exact) return exact;
  }
  return index.byUrl.get(key) ?? null;
}
