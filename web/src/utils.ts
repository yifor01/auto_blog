import type { CollectionEntry } from 'astro:content';

// 從 id（= 檔名去副檔名，格式 YYYY-MM-DD_slug）解析日期。
export function idDate(id: string): Date {
  const m = id.match(/^(\d{4}-\d{2}-\d{2})/);
  return m ? new Date(`${m[1]}T00:00:00Z`) : new Date(0);
}

// blogs 的 frontmatter 可能帶 date，缺漏時 fallback 到檔名。
export function postDate(post: CollectionEntry<'blogs'>): Date {
  if (post.data.date) return post.data.date;
  return idDate(post.id);
}

const fmt = new Intl.DateTimeFormat('zh-TW', {
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
  timeZone: 'UTC',
});

export function formatDate(d: Date): string {
  return fmt.format(d);
}

// posts/ 沒有 tldr，從 markdown body 抽第一段 prose 當摘要。
// 跳過標題（# 開頭）、frontmatter（--- 行）、引用/清單/表格/程式碼/圖片，
// 去掉行內 markdown 標記後截斷。
// emoji 開頭的正文行視為有效摘要，不跳過。
export function excerpt(body: string | undefined, max = 150): string {
  if (!body) return '';
  for (const raw of body.split('\n')) {
    const line = raw.trim();
    if (!line) continue;
    // Skip headings, frontmatter delimiters, block-level markdown syntax.
    if (/^(---|[#>*\-+|`]|!\[|\d+\.)/.test(line)) continue;
    const t = line
      .replace(/!\[[^\]]*\]\([^)]*\)/g, '')
      .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')
      .replace(/[*_`~]/g, '')
      .trim();
    if (t.length < 15) continue;
    return t.length > max ? `${t.slice(0, max).trimEnd()}…` : t;
  }
  return '';
}

// 中文閱讀速度約 400-500 字/分，粗估閱讀時間（分鐘，至少 1）。
export function readingMinutes(body: string | undefined): number {
  if (!body) return 1;
  const chars = body.replace(/\s/g, '').length;
  return Math.max(1, Math.round(chars / 450));
}

// 「每日自動」分頁只 build 近 N 天，避免 2000+ 頁拖累部署。
export const RECENT_DAYS = 30;

export function recentCutoff(days = RECENT_DAYS): Date {
  const now = new Date();
  return new Date(now.getTime() - days * 86400_000);
}
