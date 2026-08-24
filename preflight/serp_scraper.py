#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T-55 阶段①：竞对主域名清单 — Sight Glass 核心词 SERP 批量抓取（DDG HTML，走 7897 代理）"""
import subprocess, re, json, time, urllib.parse

PROXY = "http://127.0.0.1:7897"
KEYWORDS = [
    "sight glass",
    "sight glass manufacturer",
    "sight glass supplier",
    "sanitary sight glass",
    "tri clamp sight glass",
    "sight flow indicator",
    "sight flow indicator manufacturer",
    "level sight glass",
    "boiler sight glass",
    "flanged sight glass",
    "sight glass for chemical industry",
    "borosilicate sight glass",
    "reactor sight glass",
    "sight glass with light",
    "sight glass price",
]

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
        # 跳过广告
        if "y.js?" in href or "ad_domain" in href:
            continue
        results.append((href, title))
    return results

def hostname(url):
    m = re.match(r'https?://([^/]+)', url)
    return m.group(1).lower() if m else url

out = {}
for q in KEYWORDS:
    for attempt in range(3):
        try:
            html = fetch_serp(q)
            res = parse_results(html)
            if len(res) == 0:
                print(f"[{q}] 0 results (attempt {attempt+1}) - 限流")
                time.sleep(12)
                continue
            out[q] = [{"url": u, "title": t, "domain": hostname(u)} for u, t in res]
            print(f"[{q}] {len(res)} results")
            break
        except Exception as e:
            print(f"[{q}] retry {attempt+1}: {e}")
            time.sleep(10)
    time.sleep(3)

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
