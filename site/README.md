# SIGHTSPEC — Industrial Sight Glass & Flow Indicator (T-55)

> T-55 工业视镜测品站 ｜ 2026-08 建站 ｜ 26 页 ｜ Astro 7 + Tailwind v4

## 站点

- **线上**：https://sightspec.pages.dev （Cloudflare Pages）
- **定位**：卫生级快装视镜旗舰 + 流量指示器 + 配件复购线（M1 选品结论）
- **表单**：全站询盘（Footer + popup modal），CF Function `/api/contact` → 发信（ok:true 实测）

## 页面结构（26）

- 首页 / 关于 / 联系方式 / FAQ / 感谢页 / Privacy / Terms
- 产品分类页 + 4 详情页：flanged / tri-clamp / threaded / sight-flow-indicators
- 应用分类页 + 4 详情页：chemical-processing / food-beverage / oil-gas / pharmaceutical
- 服务分类页 + 3 详情页：OEM-ODM / technical-support / wholesale-distribution
- 博客 3 篇 + 作者页：what-is-a-sight-glass / how-to-choose-a-sight-glass / sight-glass-glass-types

## 常用命令

```sh
npm install        # 首次
npm run build      # 构建 → dist/
npx wrangler pages deploy dist --project-name=<project>   # 部署
npm run dev        # 本地预览
```

## 上游文档

- 选品报告：`F:/kravzik建站信息/Hermes全自动网站运营/选品研究/候选产品池/T-55-工业视镜/01-选品报告-SightGlass-M1.md`
- 预跑分析：本仓 `preflight/`（竞对深拆/内容骨架/范本/SEO 清单）
- 交接 README：`00-README-任务背景与交接.md`（同目录）

## 待办

- [ ] 主人验收（线上渲染版）
- [ ] 广告测（赛马机制）
- [ ] Semrush 词表来了做内容增量
- [ ] 记录表「核心词/字数/配图数」字段回填（收录后）
