import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// 直接 glob 既有的 output/blogs/*.md（相對 web/），免 copy。
// 注意：部分舊文 frontmatter 缺 date、且多了 score/source 欄位，
// 故 date 設 optional（頁面端從檔名 YYYY-MM-DD 前綴 fallback），
// 未知欄位由 z.object 自動忽略。
const blogs = defineCollection({
  loader: glob({ pattern: '*.md', base: '../output/blogs' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date().optional(),
    paper_url: z.string().optional(),
    paper_title: z.string().optional(),
    tags: z.array(z.string()).default([]),
    tldr: z.string().optional(),
  }),
});

// 每日自動生成的 pipeline 貼文（output/posts），frontmatter 與 blogs 不同：
// title / url / source / score / model / generated_at，無 tags、無 tldr。
const posts = defineCollection({
  loader: glob({ pattern: '*.md', base: '../output/posts' }),
  schema: z.object({
    title: z.string(),
    url: z.string().optional(),
    source: z.string().optional(),
    score: z.coerce.number().optional(),
    model: z.string().optional(),
    // YAML 會把未加引號的 ISO timestamp 解析成 date，故用 coerce 容錯
    generated_at: z.coerce.date().optional(),
  }),
});

export const collections = { blogs, posts };
