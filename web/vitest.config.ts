import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    environment: 'happy-dom',
    // 真實站台是 https://auto-post-blog.pages.dev/，location.pathname 需為 '/'，
    // syncHash 清空篩選時會 replaceState 到 location.pathname。
    environmentOptions: {
      happyDOM: { url: 'https://auto-post-blog.pages.dev/' },
    },
    include: ['src/**/*.test.ts'],
  },
});
