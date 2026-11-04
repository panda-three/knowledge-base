# -*- coding: utf-8 -*-
"""新版采集：签名请求 get-doc-blocks → AES 解密 → dataJson"""
import base64, hashlib, hmac, json, time, urllib.request, urllib.parse, sys
from Crypto.Cipher import AES

G = "BDFHJLNPRTVXZ\\^`"
M = "ether7sv6te7sv6he7sv6there7sv6r0"
TOKEN = "Pt6QrU0BdytQs6mn"

def aes_encrypt(p: bytes, k: bytes, iv: bytes) -> str:
    p += bytes([16 - len(p) % 16]) * (16 - len(p) % 16)
    return base64.b64encode(AES.new(k, AES.MODE_CBC, iv).encrypt(p)).decode()

def aes_decrypt(b64: str, k: bytes, iv: bytes) -> bytes:
    data = base64.b64decode(b64)
    return AES.new(k, AES.MODE_CBC, iv).decrypt(data)

def unpad(b: bytes) -> bytes:
    return b[:-b[-1]]

def get_auth_key(token: str) -> str:
    t = (G + "~" + token + "~" + str(int(time.time()))).encode("utf-8")
    key = hashlib.md5(G.encode("utf-8")).hexdigest().encode("ascii")
    return aes_encrypt(t, key, G.encode("utf-8"))

def get_uri_hash(us: str) -> str:
    return hmac.new(M.encode("utf-8"), us.encode("utf-8"), hashlib.sha1).hexdigest()

PARAMS = {"doc":"HhD1dAJT6obNFTxSr8jcRPtfn5e","mode":"0","fromAcl":"token","acl":"5e66343778305ee1540591dfff4e28f3",
          "utm_media":"web","utm_content":"mtvajp1rj83qdpk56y","utm_source":"","utm_medium":"","utm_activity":"","_uds":"hyyy_biu"}

def us_sorted():
    keys = sorted(PARAMS.keys())
    return "/api/feishu/get-doc-blocks?" + "&".join(f"{k}={PARAMS[k]}" for k in keys)

URL = "https://yitang.top/api/feishu/get-doc-blocks?" + urllib.parse.urlencode(PARAMS)

hd = {
    "X-token-1": get_auth_key(TOKEN),
    "X-token-2": get_uri_hash(us_sorted()),
    "X-token-er": us_sorted(),
    "X-request-by": "fe-31e8c42",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Referer": "https://yitang.top/fs-doc/5e66343778305ee1540591dfff4e28f3/HhD1dAJT6obNFTxSr8jcRPtfn5e",
}
req = urllib.request.Request(URL, headers=hd)
with urllib.request.build_opener(urllib.request.ProxyHandler({})).open(req, timeout=30) as r:
    body = json.loads(r.read().decode("utf-8"))
print("code:", body.get("code"), "| msg:", body.get("message"))
enc = body.get("data")
if isinstance(enc, str) and enc.startswith("{"):
    print("data 疑似已明文 JSON，前 200:", enc[:200])
    dj = json.loads(enc)
elif isinstance(enc, str):
    print("加密串长度:", len(enc))
    key = hashlib.md5(TOKEN.encode("utf-8")).hexdigest().encode("ascii")
    iv = TOKEN.encode("utf-8")
    plain = unpad(aes_decrypt(enc, key, iv))
    text = plain.decode("utf-8")
    print("解密后前 300:", text[:300])
    dj = json.loads(text)
elif isinstance(enc, (dict, list)):
    dj = enc
else:
    print("意外 data 类型:", type(enc)); sys.exit(1)

out = "/Users/panda/Desktop/knowledge-base/00-项目工作区/course-e2e/doc_datajson.json"
json.dump(dj, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("已保存:", out)
print("顶层结构:", type(dj).__name__)
if isinstance(dj, dict):
    print("keys:", list(dj.keys())[:20])
    kids = dj.get("childrens") or dj.get("blocks") or []
    print("childrens 数量:", len(kids) if hasattr(kids, '__len__') else 'n/a')
    if kids: print("首块:", json.dumps(kids[0], ensure_ascii=False)[:400])
