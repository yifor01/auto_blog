// @ts-check
import { defineConfig } from 'astro/config';

// 純靜態輸出，部署到 Cloudflare Pages（Direct Upload，無需 adapter）。
export default defineConfig({
  trailingSlash: 'ignore',
  // tab 切換走 ClientRouter 軟導航（見 layouts/Base.astro），再配 hover 預抓：
  // 滑到 tab 上就開始下載，點下去多半已在快取。首頁 index.html 約 2MB
  // （近 30 天全部內嵌供客戶端篩選），預抓收益最大。
  prefetch: {
    prefetchAll: true,
    defaultStrategy: 'hover',
  },
});
