import { RECENT_DAYS, recentCutoff } from './utils';

export interface GithubEntry {
  title: string;
  slug: string;
  url: string;
  abstract: string;
  stars_today: number;
  language: string;
}

export interface HfEntry {
  title: string;
  slug: string;
  url: string;
  abstract: string;
  upvotes: number;
  arxiv_id: string;
  authors: string[];
}

export interface OtherEntry {
  title: string;
  slug: string;
  url: string;
  abstract: string;
  source: string;
  source_name: string;
  citation_count: number;
  published_date: string;
  authors: string[];
}

export interface DayLists {
  date: string;
  github: GithubEntry[];
  papers: { hf: HfEntry[]; others: OtherEntry[] };
}

// build 時直讀 pipeline 產出的 lists JSON（與 posts 同策略：近 N 天）
const modules = import.meta.glob<DayLists>('../../output/lists/*.json', {
  eager: true,
  import: 'default',
});

export function loadLists(days = RECENT_DAYS): DayLists[] {
  const cutoff = recentCutoff(days);
  return Object.values(modules)
    .filter((d) => new Date(`${d.date}T00:00:00Z`) >= cutoff)
    .sort((a, b) => b.date.localeCompare(a.date));
}
