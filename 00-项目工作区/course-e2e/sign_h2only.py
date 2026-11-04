# -*- coding: utf-8 -*-
import base64, hashlib, hmac, json, time, urllib.request, urllib.parse
from Crypto.Cipher import AES
G = "BDFHJLNPRTVXZ\\^`"; M = "ether7sv6te7sv6he7sv6there7sv6r0"; TOKEN = "Pt6QrU0BdytQs6mn"
def aes(p: bytes, k: bytes, iv: bytes):
    p += bytes([16-len(p)%16])*(16-len(p)%16)
    return base64.b64encode(AES.new(k, AES.MODE_CBC, iv).encrypt(p)).decode()
def h1():
    t = (G+"~"+TOKEN+"~"+str(int(time.time()))).encode()
    return aes(t, hashlib.md5(G.encode()).digest(), G.encode())
def h2(us): return hmac.new(M.encode(), us.encode(), hashlib.sha1).hexdigest()
PARAMS = {"doc":"HhD1dAJT6obNFTxSr8jcRPtfn5e","mode":"0","fromAcl":"token","acl":"5e66343778305ee1540591dfff4e28f3",
          "utm_media":"web","utm_content":"mtvajp1rj83qdpk56y","utm_source":"","utm_medium":"","utm_activity":"","_uds":"hyyy_biu"}
def us_of(order):
    keys = list(PARAMS.keys())
    if order=="sorted": keys=sorted(keys)
    return "/api/feishu/get-doc-blocks?" + "&".join(f"{k}={PARAMS[k]}" for k in keys)
URL = "https://yitang.top/api/feishu/get-doc-blocks?" + urllib.parse.urlencode(PARAMS)
def call(hd):
    base = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)","Referer":"https://yitang.top/fs-doc/5e66343778305ee1540591dfff4e28f3/HhD1dAJT6obNFTxSr8jcRPtfn5e"}
    base.update(hd)
    try:
        with urllib.request.build_opener(urllib.request.ProxyHandler({})).open(urllib.request.Request(URL, headers=base), timeout=20) as r:
            return r.status, r.read().decode("utf-8","replace")[:150]
    except Exception as e: return None, repr(e)[:120]
# 只带 1，不带 2/er
st, body = call({"X-token-1": h1(), "X-request-by": "fe-31e8c42"})
print("only h1 ->", st, body[:120])
# 1 + 2（两种顺序）+ er 对应
for order in ("orig","sorted"):
    us = us_of(order)
    st, body = call({"X-token-1": h1(), "X-token-2": h2(us), "X-token-er": us, "X-request-by": "fe-31e8c42"})
    print(f"h1+h2({order}) ->", st, body[:120])
