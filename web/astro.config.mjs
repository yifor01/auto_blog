// @ts-check
import { defineConfig } from 'astro/config';

// 純靜態輸出，部署到 Cloudflare Pages（Direct Upload，無需 adapter）。
export default defineConfig({
  trailingSlash: 'ignore',
});
