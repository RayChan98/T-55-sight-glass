# SIGHTSPEC 站点参数真源（子 agent 写页必读）

## 品牌定位
- 品牌：SIGHTSPEC — Industrial Sight Glass Manufacturer（工业视镜制造商）
- 定位：工厂直销 B2B（OEM/ODM 定制 + 标准品），对标 LJ Star / ARCHON 但走工厂直销
- 邮箱：cj226144@gmail.com ｜ WhatsApp：+86 137 1086 0663
- 站点 URL：https://sightspec.pages.dev（正式域名后绑）

## 色板（已定，改动只动 global.css @theme）
- navy-950: #0B1F33（深空蓝黑主色） / navy-900: #102A45 / navy-800: #17395C
- brand-blue: #2563EB（品牌辅色） / cta-orange: #F97316（CTA） / brand-green: #10B981（质量点缀）

## 产品型号与参数（抄竞对公开值，禁编造）
旗舰产品族（抄 LJ Star METAGLAS 参数模式，自家型号）：

1. **SG-100 Tri-Clamp Sight Glass**（卫生级快装视镜，旗舰）
   - Mounting: Sanitary tri-clamp (1/2"–12" / DN15–DN300)
   - Glass: Borosilicate to DIN 7080（可选 soda lime）
   - Metal: 304 / 316L SS（可选 Hastelloy / Duplex）
   - 温度压力: up to 572°F (300°C)；FV to 230 psi (1.6 MPa)
   - Approvals: USP Class VI / BPE Compliant / FDA
   - 卖点：无缝死角设计、防雾可选加热、OEM 定制

2. **SG-200 Sight Flow Indicator**（视镜流量指示器，次旗舰）
   - Mounting: Tri-clamp / threaded / flanged / weld
   - Glass: Borosilicate（高温）/ soda lime（低温）
   - Metal: 304 / 316L SS / carbon steel
   - 类型: flapper(挡板)/rotary(转子)/drip tube(滴管)/ball(浮球)
   - 温度: up to 500°F；压力: up to 300 psi
   - 卖点：卫生级与工业双线、可视流量验证

3. **SG-300 Threaded Sight Glass**（螺纹视镜）
   - Mounting: Male NPT / BSP（1/4"–3"）
   - Glass: Borosilicate to DIN 7080
   - Metal: 316 SS / Hastelloy / carbon steel
   - 压力: up to 100 bar (1450 psi)
   - 卖点：紧凑、高压、罐体/管道小口径观察

4. **SG-400 Flanged Sight Glass**（法兰视镜）
   - Mounting: ANSI B16.5 Class 150/300 / DIN PN10-PN40
   - Glass: Borosilicate / soda lime / quartz（高温）
   - Metal: Carbon steel / 316 SS
   - 尺寸: 2"–8" (DN50–DN200)
   - 卖点：大视窗、化工/油气管道主流连接

## 页面地图（URL 固定，内链只指这些）
- / : 首页
- /products/ : 品类总览
- /products/tri-clamp-sight-glasses/ : 旗舰
- /products/sight-flow-indicators/ : 次旗舰
- /products/threaded-sight-glasses/
- /products/flanged-sight-glasses/
- /applications/ : 应用总览
- /applications/pharmaceutical/
- /applications/food-beverage/
- /applications/chemical-processing/
- /applications/oil-gas/
- /services/oem-odm/ /services/wholesale-distribution/ /services/technical-support/（已存在，保留）
- /blog/ + 博客文章
- /about/ /contact/ /faq/ /privacy/ /terms/ /thank-you/（已存在）

## 写作规范（硬性）
- 页面正文 ≥600 词；博客 ≥1200 词
- 每页 1 个 H1；H2 分段；关键处用表格（参数表/对比表）
- FAQ 用 <details>/<summary>
- 内链只指向页面地图内真实 URL，禁止指不存在页
- CTA 用 CtaBand 组件 + data-quote-open 属性
- 卖点禁绝对化（禁"永不损坏/完全防堵"——视镜玻璃是耗材）
- 专业事实来自竞对公开参数（LJ Star/ARCHON/Steriflow），禁编造认证
