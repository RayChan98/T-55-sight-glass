# 05 · 上线前 SEO 检查清单 — Sight Glass（工业视镜）

> 阶段⑤产出 ｜ T-55 工业视镜 ｜ 2026-08-23 夜间预跑 ｜ 用途：建站完成后、上线前逐项检查（on-page + technical）

---

## 一、On-Page SEO（每页必查）

### 1.1 标题/描述/结构
- [ ] 每页唯一 Meta Title（≤60 字符，主词靠前，含品牌词）
- [ ] 每页唯一 Meta Description（≤155 字符，含主词 + CTA）
- [ ] H1 每页唯一且含主词（品类页=industrial sight glasses；安装页=tri clamp sight glass 等）
- [ ] H2-H4 层级正确（H1→H2→H3 不跳级）
- [ ] URL 结构：短、含主词、小写、连字符（/tri-clamp-sight-glass/ 而非 /product/12345/）
- [ ] 图片全部 alt 文本（含主词描述）

### 1.2 内容
- [ ] 每页 ≥800 词（品类/产品页），博客 ≥1500 词
- [ ] 参数表（玻璃/材质/温度/压力/尺寸/认证）每产品页必含
- [ ] 内部链接 ≥5/页（互链：品类↔安装方式↔行业↔配件↔B2B）
- [ ] 每页 1 个主 CTA（RFQ/询盘）+ 1 个次 CTA（手册/联系）

### 1.3 语义
- [ ] 全部 B2B 词带 sight glass / sight flow indicator / tri clamp 前缀（防 "sight" 词典污染）
- [ ] 同义覆盖：sight glass / sight glass window / sight port / inspection window
- [ ] 无 AI 翻译腔（全英文母语级，参考 LJ Star 表达）

## 二、Technical SEO（全站必查）

### 2.1 爬取/索引
- [ ] sitemap.xml 生成（全部 20-24 页收录）
- [ ] robots.txt 正确（放行 sitemap，禁爬 admin/thankyou）
- [ ] 全站无 404/软 404（构建后逐一 curl 验证，skill: deploy-verification-gates）
- [ ] canonical 每页唯一（防重复内容）
- [ ] 无重复/近似页面（tri-clamp vs clamp 不能双页抢一词）

### 2.2 性能/移动
- [ ] Core Web Vitals：LCP <2.5s / CLS <0.1 / INP <200ms（图片 WebP+懒加载）
- [ ] 移动端导航完整（汉堡菜单/折叠/搜索）
- [ ] 字体/图标本地化（禁 Google Fonts 外链拖慢）

### 2.3 结构化/信任
- [ ] Product/Organization JSON-LD（品类页+产品页）
- [ ] FAQ Schema（选型 6 问页）
- [ ] 全站 HTTPS + 证书有效
- [ ] 询盘表单可用（提交测试全流程，skill: b2b-site-inquiry-forms）
- [ ] Legal 页齐（Privacy Policy/Terms/Contact）

## 三、内容/外链

- [ ] 目录站收录：GlobalSpec / Metoree / IQS 提交（外链机会）
- [ ] 行业分页与品类页互链闭环（LJ Star 模式）
- [ ] 博客每篇内链 ≥3 个产品页
- [ ] 配件耗材页互链（复购线：gasket↔lens↔replacement）

## 四、部署前闸门（skill: deploy-verification-gates）

- [ ] 构建零报错（Astro 禁 TS 报错，GOVERNANCE 六）
- [ ] 从构建 HTML 提取全部内部 href 逐一 curl（禁死链）
- [ ] 无 WP/ACF 残留（纯静态）
- [ ] CF Pages 部署走代理（HTTPS_PROXY=127.0.0.1:7897）
- [ ] 域名/zone 状态验证（cf-pages-domain-diagnostics）

---

*本清单在 M2 建站完成后、上线前逐项执行*
