import fs from 'node:fs';
import path from 'node:path';

// 從 data/scored/{date}.json 讀取 5D 評分與 metadata，
// 以 normalized URL 比對 posts frontmatter 的 url，於 build 時增強卡片/詳情頁。
// scored JSON 不在 web/ 內，故用 fs 直讀（cwd = web/，與 content.config.ts 的 glob base 同基準）。

export interface Enrichment {
  novelty: number;
  impact: number;
  trending: number;
  practicality: number;
  blogWorthiness: number;
  llmScore: number;
  ruleScore: number;
  llmReason: string;
  ruleReasons: string[];
  tags: string[];
  organization: string;
  authors: string[];
  abstract: string;
}

// 來源性質的雜訊 tag，不值得當 facet
const TAG_STOPLIST = new Set([
  'github', 'trending', 'rss', 'news', 'reddit', 'hackernews', 'hn',
  'blog', 'paper', 'papers', 'huggingface', 'arxiv', 'newsapi',
  'hf_daily', 'semantic_scholar', 'chatpaper', 'ai_blogs',
  'editors pick', 'staff', 'technology', 'tech news', 'new releases',
  'ai shorts', 'applications', 'ai', 'artificial intelligence',
]);

export function normalizeUrl(url: string | undefined): string {
  if (!url) return '';
  return url.trim().replace(/\/+$/, '').replace(/^http:/, 'https:');
}

function cleanTags(tags: unknown): string[] {
  if (!Array.isArray(tags)) return [];
  const seen = new Set<string>();
  const out: string[] = [];
  for (const t of tags) {
    if (typeof t !== 'string') continue;
    const key = t.trim().toLowerCase();
    if (!key || TAG_STOPLIST.has(key) || seen.has(key)) continue;
    seen.add(key);
    out.push(t.trim());
  }
  return out;
}

let cache: Map<string, Enrichment> | null = null;

export function loadEnrichment(): Map<string, Enrichment> {
  // dev server 是長駐進程，快取會看不到 pipeline 新寫入的 scored JSON；只在 build 時快取
  if (import.meta.env?.DEV) cache = null;
  if (cache) return cache;
  const map = new Map<string, Enrichment>();
  const dir = path.resolve(process.cwd(), '../data/scored');
  let files: string[] = [];
  try {
    files = fs.readdirSync(dir).filter((f) => f.endsWith('.json'));
  } catch {
    cache = map;
    return map; // 沒有 scored 資料時優雅降級
  }
  for (const file of files) {
    let parsed: unknown;
    try {
      parsed = JSON.parse(fs.readFileSync(path.join(dir, file), 'utf-8'));
    } catch {
      continue;
    }
    if (!Array.isArray(parsed)) continue;
    for (const row of parsed) {
      const item = row?.item;
      const url = normalizeUrl(item?.url);
      if (!url) continue;
      map.set(url, {
        novelty: row.novelty ?? 0,
        impact: row.impact ?? 0,
        trending: row.trending ?? row.relevance ?? 0,
        practicality: row.practicality ?? 0,
        blogWorthiness: row.blog_worthiness ?? 0,
        llmScore: row.llm_score ?? 0,
        ruleScore: row.rule_score ?? 0,
        llmReason: row.llm_reason ?? '',
        ruleReasons: Array.isArray(row.rule_reasons) ? row.rule_reasons : [],
        tags: cleanTags(item?.tags),
        organization: item?.organization ?? '',
        authors: Array.isArray(item?.authors) ? item.authors.slice(0, 5) : [],
        abstract: item?.abstract ?? '',
      });
    }
  }
  cache = map;
  return map;
}

export const DIM_LABELS: [keyof Enrichment, string][] = [
  ['novelty', '新穎性'],
  ['impact', '影響力'],
  ['trending', '話題性'],
  ['practicality', '實用性'],
  ['blogWorthiness', '適合度'],
];
