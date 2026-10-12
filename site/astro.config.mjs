// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  // 10-13 补闸 t_f78872ba：站点正式地址声明（gate2/gate3 品牌域派生源；值不变）
  site: 'https://sightspec.pages.dev',
  vite: {
    plugins: [tailwindcss()]
  }
});