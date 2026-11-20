#!/usr/bin/env python3
"""扫描 dist/ 生成 files.json。

网页版靠这份清单取文件名与大小，Vercel、GitHub Pages 这类不返回目录列表的托管
只有靠它才能列文件。用法：在本文件所在目录执行 python3 生成清单.py
"""
import io
import json
import os
import sys

base = os.path.dirname(os.path.abspath(__file__))
dist = os.path.join(base, 'dist')

if not os.path.isdir(dist):
    sys.exit('没找到 dist 目录：' + dist)

items = []
for name in sorted(os.listdir(dist), key=lambda s: s.lower()):
    if name.startswith('.'):
        continue
    path = os.path.join(dist, name)
    if not os.path.isfile(path):
        continue
    items.append({'name': name, 'size': os.path.getsize(path)})

out = os.path.join(base, 'files.json')
with io.open(out, 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)
    f.write('\n')

print('已写入 files.json：%d 个文件' % len(items))
