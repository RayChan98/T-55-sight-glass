#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T-55 阶段①补充：Bing SERP（走 7897 代理）— 核心词补全"""
import re, html, subprocess, urllib.parse, time, json, io
from urllib.parse import urlparse

PROXY = "http://127.0.0.1:7897"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

QUERIES = ["sight glass", "sanitary sight glass", "level sight glass", "boiler sight glass", "sight glass supplier"]

def fetch(q):
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(q) + "&setlang=en&cc=us&count=15"
    r = subprocess.run(["curl", "-x", PROXY, "-s", "-m", "20", "-A", UA,
                        "-H", "Accept-Language: en-US,en;q=0.9", url],
                       capture_output=True, text=True, timeout=30)
    return r.stdout

def parse_bing(raw):
    out = []
    for m in re.finditer(r'<li class="b_algo".*?</li>', raw, re.S):
        block = m.group(0)
        am = re.search(r'<a[^>]+href="(http[^\"]+)"[^>]*>(.*?)</a>', block, re.S)
        if not am:
            continue
        url = am.group(1)
        title = html.unescape(re.sub(r'<[^>]+>', '', am.group(2))).strip()
        sm = re.search(r'<p[^>]*>(.*?)</p>', block, re.S)
        snip = html.unescape(re.sub(r'<[^>]+>', '', sm.group(1))).strip() if sm else ""
        out.append((title, urlparse(url).netloc, snip, url))
    return out

results = {}
for q in QUERIES:
    time.sleep(5)
    raw = fetch(q)
    print("=" * 15, q, f"(len {len(raw)})", "=" * 15)
    if raw.count("b_algo") == 0:
        print("  [NO RESULTS / BLOCKED]")
        continue
    rows = parse_bing(raw)[:10]
    results[q] = [{"title": t, "domain": d, "snippet": s[:150], "url": u} for t, d, s, u in rows]
    for i, (t, d, s, u) in enumerate(rows, 1):
        print(f"{i}. {t}  [{d}]")
    print()

# 合并到 raw json
rawpath = r"D:\kravzik-work\T-55-sight-glass\preflight\01-competitor-domains-raw.json"
try:
    out = json.loads(io.open(rawpath, encoding="utf-8").read())
except Exception:
    out = {}
for q, rows in results.items():
    out[q] = rows
with io.open(rawpath, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print(f"\n合并完成，总词数: {len(out)}")
from collections import Counter
domains = Counter()
for q, res in out.items():
    for r in res:
        domains[r["domain"]] += 1
print("=== 域名频次 TOP 40 ===")
for d, c in domains.most_common(40):
    print(f"{c}\t{d}")
print(f"总唯一域名: {len(domains)}")
