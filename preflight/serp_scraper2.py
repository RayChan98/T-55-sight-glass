#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T-55 阶段①补充：少量关键词 SERP 抓取（夜间反爬缓解版：长间隔+小批量）"""
import subprocess, re, json, time, urllib.parse

PROXY = "http://127.0.0.1:7897"
KEYWORDS = ["sight glass", "sanitary sight glass", "level sight glass", "boiler sight glass"]

def fetch_serp(q):
    url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(q)
    r = subprocess.run(["curl", "-x", PROXY, "-s", "-m", "25", "-A",
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0", url],
                       capture_output=True, text=True, timeout=35)
    return r.stdout

def parse_results(html):
    results = []
    for m in re.finditer(r'class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', html, re.S):
        href, title = m.group(1), re.sub(r'<[^>]+>', '', m.group(2)).strip()
        if "y.js?" in href or "ad_domain" in href:
            continue
        results.append((href, title))
    return results

def hostname(url):
    m = re.match(r'https?://([^/]+)', url)
    return m.group(1).lower() if m else url

out = {}
for q in KEYWORDS:
    ok = False
    for attempt in range(4):
        try:
            html = fetch_serp(q)
            res = parse_results(html)
            if len(res) == 0:
                print(f"[{q}] 0 results (attempt {attempt+1}) - 限流")
                time.sleep(20 + attempt * 15)
                continue
            out[q] = [{"url": u, "title": t, "domain": hostname(u)} for u, t in res]
            print(f"[{q}] {len(res)} results")
            ok = True
            break
        except Exception as e:
            print(f"[{q}] retry {attempt+1}: {e}")
            time.sleep(15)
    if not ok:
        print(f"[{q}] FAILED 全部重试")
    time.sleep(15)

# 合并白天已有数据（从日志恢复）
daytime = {
    "sight glass manufacturer": [
        ("https://www.sightglasswindows.com/", "PPC Sight Glass Windows", "sightglasswindows.com"),
        ("https://www.cyclopswv.com/", "Cyclops Industries", "cyclopswv.com"),
        ("https://lumiglas.ltd/", "Lumiglas", "lumiglas.ltd"),
        ("https://archonind.com/products/sight-glass/", "ARCHON Industries", "archonind.com"),
        ("https://www.ljstar.com/", "LJ Star", "ljstar.com"),
        ("https://us.metoree.com/categories/2474/", "Metoree 目录", "us.metoree.com"),
        ("https://www.iqsdirectory.com/sight-glass/", "IQS Directory", "iqsdirectory.com"),
    ],
    "sight flow indicator manufacturer": [
        ("https://archonind.com/products/sight-flow-indicator/", "ARCHON Sight Flow Indicators", "archonind.com"),
        ("https://www.opwglobal.com/products/us/chemical-industrial-products/process-products/visi-flo-sight-flow-indicators", "OPW VISI-FLO", "opwglobal.com"),
        ("https://www.globalspec.com/suppliers/1820/sight_flow_indicators", "GlobalSpec 187 suppliers", "globalspec.com"),
        ("https://ernstinstruments.com/sight-flow-indicators-sight-glass/", "Ernst Instruments", "ernstinstruments.com"),
        ("https://sightglasswindows.com/sight-flow-indicators/", "PPC Sight Flow Indicators", "sightglasswindows.com"),
        ("https://www.clarkreliance.com/sight-flow-indicators", "Clark-Reliance Jacoby-Tarbox", "clarkreliance.com"),
        ("https://www.ljstar.com/product-lines/sight-flow-indicators/", "LJ Star Sight Flow Indicators", "ljstar.com"),
    ],
    "tri clamp sight glass": [
        ("https://sanitaryfittings.us/product-category/fittings/clamp-fittings/sight-glasses", "Sanitary Fittings", "sanitaryfittings.us"),
        ("https://tcfittings.com/collections/sight-glass", "TC Fittings", "tcfittings.com"),
        ("https://www.brewershardware.com/tri-clamp-compatible-fittings/tri-clamp-compatible-sight-glasses/", "Brewers Hardware", "brewershardware.com"),
        ("https://www.amazon.com/DERNORD-Line-Sanitary-Straight-SUS316/dp/B075JBJQ1Y", "Amazon DERNORD", "amazon.com"),
        ("https://www.gormansmith.com/collections/tri-clamp-sight-glasses", "Gorman & Smith", "gormansmith.com"),
        ("https://oakstills.com/products/tri-clamp-in-line-sight-glass", "OakStills", "oakstills.com"),
        ("https://www.brewerygaskets.com/tri-clamp-sight-glass/", "Brewery Gaskets", "brewerygaskets.com"),
        ("https://www.stouttanks.com/small-parts-and-accessories/tri-clamp-sight-glasses", "Stout Tanks", "stouttanks.com"),
    ],
}
for q, rows in daytime.items():
    if q not in out:
        out[q] = [{"url": u, "title": t, "domain": d} for u, t, d in rows]
        print(f"[{q}] (白天数据合并) {len(rows)}条")

with open(r"D:\kravzik-work\T-55-sight-glass\preflight\01-competitor-domains-raw.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

from collections import Counter
domains = Counter()
for q, res in out.items():
    for r in res:
        domains[r["domain"]] += 1
print("\n=== 域名出现频次 TOP 50 ===")
for d, c in domains.most_common(50):
    print(f"{c}\t{d}")
print(f"\n总唯一域名: {len(domains)}")
