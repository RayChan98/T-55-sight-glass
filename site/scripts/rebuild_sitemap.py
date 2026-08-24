#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SIGHTSPEC - 从 dist 重建 sitemap.xml + robots.txt（loop-engineering 坑#4 已验证方案）"""
import os, io, datetime

BASE_URL = "https://sightspec.pages.dev"
DIST = r"D:\kravzik-work\T-55-sight-glass\site\dist"
PUBLIC = r"D:\kravzik-work\T-55-sight-glass\site\public"
TODAY = datetime.date.today().isoformat()

urls = []
for root, dirs, files in os.walk(DIST):
    for fn in files:
        if fn != "index.html":
            continue
        d = os.path.relpath(root, DIST)
        d = d.strip("/")
        if d in (".", ""):
            urls.append(f"{BASE_URL}/")
        else:
            urls.append(f"{BASE_URL}/{d}/")

urls.sort()
print(f"共 {len(urls)} 个 URL:")
for u in urls:
    print(" ", u)

xml = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    xml.append(f'  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>')
xml.append('</urlset>')

with io.open(os.path.join(PUBLIC, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write("\n".join(xml) + "\n")
print("sitemap.xml 已重建")

# robots.txt
robots = f"""User-agent: *
Allow: /
Disallow: /thank-you/

Sitemap: {BASE_URL}/sitemap.xml
"""
with io.open(os.path.join(PUBLIC, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots)
print("robots.txt 已重建")
