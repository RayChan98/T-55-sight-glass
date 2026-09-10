#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T-55 SIGHTSPEC 全站 SEO meta 修复：title<=65 + desc<=160（seo-meta-ctr-rules 公式）"""
import io, os, re

BASE = r"D:\kravzik-work\T-55-sight-glass\site\src\pages"

# url_key -> (new_title, new_desc)
META = {
    "index": (
        "Industrial Sight Glass Manufacturer | SIGHTSPEC",
        "Factory-direct sight glasses: tri-clamp, threaded, flanged and sight flow indicators. DIN 7080 borosilicate, USP Class VI, MOQ 10 pcs for OEM buyers.",
    ),
    "about": (
        "About SIGHTSPEC — Precision Sight Glass Factory",
        "SIGHTSPEC is a sight glass manufacturer: DIN 7080 borosilicate windows, 100% pressure-tested assemblies, USP Class VI and FDA compliance for OEM buyers.",
    ),
    "contact": (
        "Contact SIGHTSPEC | Sight Glass Quotes in 24 Hours",
        "Request a sight glass quote: send size, connection, pressure and temperature. Engineering replies within 24 hours with CAD drawings and pricing.",
    ),
    "faq": (
        "Sight Glass FAQ: MOQ, Lead Time, Glass Types",
        "15 sight glass buying answers: MOQ 10 pcs, 7-25 day lead time, DIN 7080 borosilicate vs quartz, gasket materials, certifications and spare parts.",
    ),
    "privacy": (
        "Privacy Policy | SIGHTSPEC",
        "How SIGHTSPEC collects, uses and protects your inquiry data. No third-party sale of contact details.",
    ),
    "terms": (
        "Terms of Service | SIGHTSPEC",
        "SIGHTSPEC terms of service: quotation validity, warranty scope, shipping terms and intellectual property for sight glass orders.",
    ),
    "thank-you": (
        "Thank You | SIGHTSPEC",
        "Your sight glass inquiry was received. Our engineering team replies within 24 hours.",
    ),
    # ---- applications ----
    "applications/index": (
        "Sight Glass Applications by Industry | SIGHTSPEC",
        "Sight glasses by industry: pharmaceutical, food and beverage, brewery, chemical, oil and gas, steam and boiler. Material and glass selection per duty.",
    ),
    "applications/pharmaceutical": (
        "Pharmaceutical Sight Glass | USP Class VI",
        "Sanitary sight glasses for pharma: USP Class VI, ASME BPE, Ra 0.4-0.8 um finish, dead-leg-free tri-clamp design for CIP/SIP and sterile process lines.",
    ),
    "applications/food-beverage": (
        "Food & Beverage Sight Glass | FDA Compliant",
        "Hygienic sight glasses for food and beverage: FDA 21 CFR compliant, tri-clamp connection, EPDM or PTFE gaskets, CIP/SIP rated to 300C for dairy and juice.",
    ),
    "applications/brewery": (
        "Brewery Sight Glass | Sanitary Tri-Clamp",
        "Brewery sight glasses: sanitary tri-clamp windows for fermenters, bright tanks and brewhouse piping. 1/2-12 inch, DIN 7080 borosilicate, CIP rated.",
    ),
    "applications/chemical-processing": (
        "Chemical Process Sight Glass | Borosilicate",
        "Sight glasses for chemical processing: DIN 7080 borosilicate windows, 316L or Hastelloy bodies, ANSI Class 150/300 flanges for corrosive media duty.",
    ),
    "applications/oil-gas": (
        "Oil & Gas Sight Glass | High Pressure Windows",
        "High pressure sight glasses for oil and gas: carbon steel bodies, ANSI Class 300 flanges, quartz windows, rated to 100 bar for pipelines and separators.",
    ),
    "applications/steam": (
        "Steam & Boiler Sight Glass | High Temperature",
        "High temperature sight glasses for steam and boiler duty: quartz or borosilicate windows, carbon steel bodies, graphite gaskets for boiler drums and mains.",
    ),
    # ---- products ----
    "products/index": (
        "Sight Glass Products | SG Series Catalog",
        "Sight glass catalog: tri-clamp SG-100, flow indicator SG-200, threaded SG-300, flanged SG-400, plus hinged, bolt-on, weld-in, gaskets and windows.",
    ),
    "products/tri-clamp-sight-glasses": (
        "Tri-Clamp Sight Glass SG-100 | Sanitary",
        "Sanitary tri-clamp sight glass SG-100: 1/2-12 inch, DIN 7080 borosilicate, 316L body, 572F and 230 psi, USP Class VI for pharma, food and brewery lines.",
    ),
    "products/threaded-sight-glasses": (
        "Threaded Sight Glass SG-300 | NPT/BSP",
        "Threaded sight glass SG-300: male NPT or BSP 1/4-3 inch, rated to 100 bar (1450 psi), 316L or carbon steel for compact high-pressure instrument lines.",
    ),
    "products/flanged-sight-glasses": (
        "Flanged Sight Glass SG-400 | ANSI & DIN",
        "Flanged sight glass SG-400: ANSI Class 150/300 or DIN PN10-PN40, 2-8 inch large windows, borosilicate or quartz for chemical and oil and gas piping.",
    ),
    "products/sight-flow-indicators": (
        "Sight Flow Indicator SG-200 | Visual Flow",
        "Sight flow indicator SG-200: flapper, rotary, ball or drip tube visual flow confirmation. Tri-clamp, threaded or flanged, 500F and 300 psi rated.",
    ),
    "products/hinged-sight-glasses": (
        "Hinged Sight Glass | Quick-Opening Windows",
        "Hinged sight glasses: quick-opening windows for fast vessel access and cleaning. Bolt-on or weld-neck mounting, borosilicate DIN 7080 windows.",
    ),
    "products/bolt-on-sight-glasses": (
        "Bolt-On Sight Glass | ANSI B16.5 Windows",
        "Bolt-on sight glasses to ANSI B16.5: replaceable windows on existing vessel nozzles, no welding required. Carbon or stainless steel frames.",
    ),
    "products/weld-in-sight-glasses": (
        "Weld-In Sight Glass | Butt-Weld Windows",
        "Weld-in sight glasses: butt-weld or socket-weld bodies for vessels, reactors and piping. 316L, Hastelloy or carbon steel with DIN 7080 windows.",
    ),
    "products/sight-glass-gaskets": (
        "Sight Glass Gaskets | EPDM, FKM, PTFE",
        "Replacement sight glass gaskets: EPDM, silicone, FKM (Viton) and PTFE in DIN 7080 and tri-clamp sizes. Temperature and chemical compatibility table.",
    ),
    "products/sight-glass-replacement-windows": (
        "Sight Glass Replacement Windows | DIN 7080",
        "Replacement sight glass windows: DIN 7080 borosilicate, soda lime and quartz discs in standard diameters. Factory-direct spare parts for SG series.",
    ),
    # ---- services ----
    "services/index": (
        "Sight Glass Services | OEM, Wholesale, Support",
        "SIGHTSPEC services: OEM/ODM custom sight glasses, wholesale distribution from MOQ 10 pcs, and engineering support with CAD drawings and sizing help.",
    ),
    "services/oem-odm": (
        "OEM / ODM Sight Glass Manufacturing",
        "Custom sight glass OEM/ODM: your sizes, connections, glass type and private label. MOQ 100 pcs, 15-25 day lead time, CAD drawings before production.",
    ),
    "services/wholesale-distribution": (
        "Sight Glass Wholesale | Distributor Pricing",
        "Sight glass wholesale and distribution: tiered factory pricing from MOQ 10 pcs, private label, regional exclusivity and stocked spare parts programs.",
    ),
    "services/technical-support": (
        "Sight Glass Technical Support | Sizing & CAD",
        "Sight glass engineering support: model selection, CAD drawings (DWG/PDF), installation guides, gasket sizing and spare parts for broken windows.",
    ),
    # ---- blog ----
    "blog/index": (
        "Sight Glass Blog | Technical Guides 2026",
        "Sight glass engineering guides: definitions, selection checklists, glass type comparisons, sanitary standards and flow indicator differences for B2B buyers.",
    ),
    "blog/what-is-a-sight-glass": (
        "What Is a Sight Glass? Types & Working Principle",
        "What is a sight glass explained: working principle, soda lime vs borosilicate vs quartz comparison table, 4 main types and selection checklist.",
    ),
    "blog/how-to-choose-a-sight-glass": (
        "How to Choose a Sight Glass: 6-Question Guide",
        "How to choose a sight glass in 6 questions: pressure, temperature, body metal, glass type, gasket material and mounting style, with decision table.",
    ),
    "blog/sight-glass-glass-types": (
        "Sight Glass Glass Types: Borosilicate vs Quartz",
        "Sight glass glass types compared: borosilicate vs soda lime vs quartz. Temperature limits, thermal shock, chemical resistance and cost tables for engineers.",
    ),
    "blog/sight-glass-vs-sight-flow-indicator": (
        "Sight Glass vs Sight Flow Indicator: Compared",
        "Sight glass vs sight flow indicator: 8-row comparison of function, indication method, mounting, price and maintenance, plus a buying decision checklist.",
    ),
    "blog/sanitary-sight-glass-guide": (
        "Sanitary Sight Glass Guide 2026: Tri-Clamp Specs",
        "Sanitary sight glass guide: 3A, ASME BPE, USP Class VI and FDA standards, tri-clamp size table 1/2-12 inch, gasket materials and CIP/SIP selection.",
    ),
    "blog/authors/ray-chan": (
        "Ray Chan | Sight Glass Technical Writer",
        "Ray Chan writes sight glass selection guides for SIGHTSPEC: glass types, sanitary standards, tri-clamp sizing and flow indicator comparisons.",
    ),
}

def fix_file(path, key):
    if key not in META:
        return None
    new_title, new_desc = META[key]
    c = io.open(path, encoding='utf-8').read()
    orig = c
    changed = []

    # title 变量模式
    for var in ['metaTitle', 'title']:
        pat = rf"(const {var} = )(['\"])(.*?)\2"
        m = re.search(pat, c)
        if m:
            c = c[:m.start()] + f"{m.group(1)}'{new_title}'" + c[m.end():]
            changed.append(f"{var}->title")
            break

    # description 变量模式
    for var in ['description', 'desc']:
        pat = rf"(const {var} = )(['\"])(.*?)\2"
        m = re.search(pat, c)
        if m:
            c = c[:m.start()] + f"{m.group(1)}'{new_desc}'" + c[m.end():]
            changed.append(f"{var}->desc")
            break

    # Layout title= / description= 属性（多行或单行）
    m = re.search(r'<Layout\s+title=\{?["`]([^"`]+)["`]?\}?', c)
    if m and 'title' not in ' '.join(changed):
        c = c[:m.start()] + c[m.start():].replace(m.group(0), f'<Layout title="{new_title}"', 1)
        changed.append("Layout title")
    m = re.search(r'description=\{?["`]([^"`]+)["`]?\}?', c)
    if m and 'desc' not in ' '.join(changed):
        c = c[:m.start()] + c[m.start():].replace(m.group(0), f'description="{new_desc}"', 1)
        changed.append("Layout desc")

    if c != orig:
        io.open(path, 'w', encoding='utf-8').write(c)
        return changed
    return None

count = 0
for root, dirs, files in os.walk(BASE):
    for fn in sorted(files):
        if not fn.endswith('.astro'): continue
        p = os.path.join(root, fn)
        rel = os.path.relpath(p, BASE).replace(os.sep, '/').replace('.astro', '')
        if rel.endswith('/index'): rel = rel[:-6]
        res = fix_file(p, rel)
        if res:
            count += 1
            print(f"  ✓ {rel}: {res}")

print(f"\n修复 {count} 个文件")
# 校验长度
bad = []
for k, (t, d) in META.items():
    if len(t) > 65: bad.append(f"TITLE({len(t)}) {k}: {t}")
    if len(d) > 160: bad.append(f"DESC({len(d)}) {k}")
print("新 meta 超长检查:", bad if bad else "✅ 全部合规 (title<=65, desc<=160)")
