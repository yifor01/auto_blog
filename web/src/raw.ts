import fs from 'node:fs';
import path from 'node:path';
import { normalizeUrl } from './enrich';
import { RECENT_DAYS } from './utils';

// 從 data/raw/{date}.json 讀取來源原始資料，供詳情頁的「原始資料」box 使用。
// why 不共用 enrich.ts（data/scored）：pinned 文免評分、不在 scored 裡，
// 實測近 200 篇 posts 有 10 篇會查無資料；raw 則 200/200 全中。
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

let cache: Map<string, RawItem> | null = null;

export function loadRaw(): Map<string, RawItem> {
  // dev server 是長駐進程，快取會看不到 pipeline 新寫入的 raw JSON；只在 build 時快取
  if (import.meta.env?.DEV) cache = null;
  if (cache) return cache;

  const map = new Map<string, RawItem>();
  const dir = path.resolve(process.cwd(), '../data/raw');
  let files: string[] = [];
  try {
    // 排序：同一 url 可能出現在多天的 raw（跨日去重窗口外），後寫入者覆蓋前者。
    // readdirSync 不保證順序，不排序會讓 collectedDate / signals 每次 build 不一定相同。
    files = fs.readdirSync(dir).filter((f) => f.endsWith('.json')).sort();
  } catch {
    cache = map;
    return map; // 沒有 raw 資料時優雅降級
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
      map.set(url, {
        title: it.title ?? '',
        abstract: it.abstract ?? '',
        authors: Array.isArray(it.authors) ? it.authors : [],
        organization: it.organization ?? '',
        tags: Array.isArray(it.tags) ? it.tags.filter((t: unknown) => typeof t === 'string') : [],
        sourceName: it.source_name ?? '',
        url: it.url ?? '',
        collectedDate: day,
        signals: toSignals(it.raw_metadata),
      });
    }
  }

  cache = map;
  return map;
}
