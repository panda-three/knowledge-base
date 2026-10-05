# -*- coding: utf-8 -*-
"""
本地沉淀：下载 523 张 CDN 图片到本地 + 13 篇 MD 改相对路径引用
输出：course_p1_local/ (13 个 md + imgs/ 图片)
"""
import json, os, re, time, urllib.request, concurrent.futures

BASE = "/Users/panda/DoubaoWork/chats/2026-09-17/new-chat"
imgs_by_doc = json.load(open(os.path.join(BASE, "imgs_by_doc.json"), encoding="utf-8"))
OUT = os.path.join(BASE, "course_p1_local")
IMGDIR = os.path.join(OUT, "imgs")
os.makedirs(IMGDIR, exist_ok=True)

# 篇序号映射（01-13）
doc_no = {
    "01-总览：开篇与飞轮": "01", "02-总览：训练方法与立Flag": "02", "03-案例：温童凯": "03",
    "04-案例：张伟强": "04", "05-案例：蒋之之": "05", "06-案例：叶文彬": "06",
    "07-案例：廖廖": "07", "08-第一赛段收尾": "08", "09-案例：砻沣": "09",
    "10-案例：郁金星": "10", "11-案例：劉衛": "11", "12-更多：大量同学都在练": "12",
    "13-第二赛段收尾": "13",
}

def ext_of(url):
    base = url.rsplit('/', 1)[-1]
    if '.' in base:
        e = base.rsplit('.', 1)[-1].split('?')[0].lower()
        if e in ("png", "jpg", "jpeg", "gif", "webp", "bmp"):
            return "jpg" if e == "jpeg" else e
    return "jpg"

jobs = []  # (doc_name, pos, url, local_rel)
for name, urls in imgs_by_doc.items():
    no = doc_no[name]
    for pos, url in enumerate(urls, 1):
        local = f"imgs/p{no}_{pos:03d}.{ext_of(url)}"
        jobs.append((name, pos, url, local))

print("总任务:", len(jobs))

# 禁用代理直连（本机 7890 代理不可用）
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

def download(job):
    name, pos, url, local = job
    path = os.path.join(OUT, local)
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return (local, True, "cached")
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Referer": "https://yitang.top/",
    })
    for attempt in range(3):
        try:
            with opener.open(req, timeout=40) as r, open(path, "wb") as f:
                f.write(r.read())
            if os.path.getsize(path) > 0:
                return (local, True, "ok")
        except Exception as e:
            last = str(e)[:100]
            time.sleep(2)
    return (local, False, last)

ok, fail = [], []
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:
    for local, succ, info in ex.map(download, jobs):
        if succ:
            ok.append(local)
        else:
            fail.append((local, info))
        if (len(ok) + len(fail)) % 50 == 0:
            print(f"进度 {len(ok)+len(fail)}/{len(jobs)}", flush=True)

print()
print(f"下载成功 {len(ok)} / {len(jobs)}")
if fail:
    print(f"失败 {len(fail)}:")
    for local, info in fail[:20]:
        print("  ", local, info)

json.dump({"ok": ok, "fail": [[f[0], f[1]] for f in fail]},
          open(os.path.join(BASE, "download_result.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
