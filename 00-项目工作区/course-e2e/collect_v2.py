# -*- coding: utf-8 -*-
"""新版 yitang 采集：签名请求 → AES 解密 → DFS 展平 dataJson → 图片 URL 列表
输出: data.json(展平 [{t,a,c}]) + imgs.json(全局顺序 cdnUrl) + 大纲预览
"""
import base64, hashlib, hmac, json, sys, time, urllib.request, urllib.parse
from Crypto.Cipher import AES

G = "BDFHJLNPRTVXZ\\^`"
M = "ether7sv6te7sv6he7sv6there7sv6r0"

def aes_encrypt(p, k, iv):
    p += bytes([16 - len(p) % 16]) * (16 - len(p) % 16)
    return base64.b64encode(AES.new(k, AES.MODE_CBC, iv).encrypt(p)).decode()

def aes_decrypt(b64, k, iv):
    return AES.new(k, AES.MODE_CBC, iv).decrypt(base64.b64decode(b64))

def unpad(b): return b[:-b[-1]]

def sign_headers(token, uri, params):
    ts = str(int(time.time()))
    t1 = (G + "~" + token + "~" + ts).encode("utf-8")
    key1 = hashlib.md5(G.encode("utf-8")).hexdigest().encode("ascii")
    h1 = aes_encrypt(t1, key1, G.encode("utf-8"))
    us = uri + "?" + "&".join(f"{k}={params[k]}" for k in sorted(params.keys()))
    h2 = hmac.new(M.encode("utf-8"), us.encode("utf-8"), hashlib.sha1).hexdigest()
    return {"X-token-1": h1, "X-token-2": h2, "X-token-er": us, "X-request-by": "fe-31e8c42"}, us

def decrypt_data(enc, token):
    key = hashlib.md5(token.encode("utf-8")).hexdigest().encode("ascii")
    iv = token.encode("utf-8")
    return unpad(aes_decrypt(enc, key, iv)).decode("utf-8")

def fetch_blocks(doc_id, acl, token):
    params = {"doc": doc_id, "mode": "0", "fromAcl": "token", "acl": acl,
              "utm_media": "web", "utm_content": "mtvajp1rj83qdpk56y",
              "utm_source": "", "utm_medium": "", "utm_activity": "", "_uds": "hyyy_biu"}
    uri = "/api/feishu/get-doc-blocks"
    hd, _ = sign_headers(token, uri, params)
    hd.update({"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
               "Referer": f"https://yitang.top/fs-doc/{acl}/{doc_id}"})
    url = "https://yitang.top" + uri + "?" + urllib.parse.urlencode(params)
    with urllib.request.build_opener(urllib.request.ProxyHandler({})).open(urllib.request.Request(url, headers=hd), timeout=30) as r:
        body = json.loads(r.read().decode("utf-8"))
    if body.get("code") != 0:
        raise SystemExit(f"请求失败 code={body.get('code')} msg={body.get('message')}")
    enc = body["data"]
    if isinstance(enc, str) and not enc.startswith("{"):
        return json.loads(decrypt_data(enc, token))
    return enc

def flatten(blocks):
    out = []
    def wb(b):
        out.append({"t": b["type"], "a": b.get("blockAttr") or {}, "c": len(b.get("childrens") or [])})
        for c in (b.get("childrens") or []): wb(c)
    for c in (blocks.get("childrens") or []): wb(c)
    return out

def img_urls(blocks):
    urls = []
    def wb(b):
        if b["type"] == 27:
            u = (b.get("blockAttr") or {}).get("cdnUrl")
            if u: urls.append(u)
        for c in (b.get("childrens") or []): wb(c)
    for c in (blocks.get("childrens") or []): wb(c)
    return urls

if __name__ == "__main__":
    doc_id, acl, token = sys.argv[1], sys.argv[2], sys.argv[3]
    dj = fetch_blocks(doc_id, acl, token)
    data = flatten(dj["blocks"])
    imgs = img_urls(dj["blocks"])
    json.dump(data, open("data.json", "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(imgs, open("imgs.json", "w", encoding="utf-8"), ensure_ascii=False)
    print(f"展平块数: {len(data)} | 图片块: {len(imgs)}")
    # 大纲
    print("\n== 大纲 (t=3/4/5 标题块) ==")
    for i, blk in enumerate(data):
        if blk["t"] in (3, 4, 5):
            key = {3: "heading1", 4: "heading2", 5: "heading3"}[blk["t"]]
            txt = "".join(r.get("text_run", {}).get("content", "") for r in (blk["a"].get(key) or {}).get("elements", []))
            print(f"  idx={i} t={blk['t']} {txt[:40]}")
