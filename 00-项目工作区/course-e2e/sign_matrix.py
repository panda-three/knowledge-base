# -*- coding: utf-8 -*-
import base64, hashlib, hmac, json, time, urllib.request, urllib.parse
from Crypto.Cipher import AES

G = "BDFHJLNPRTVXZ\\^`"
M = "ether7sv6te7sv6he7sv6there7sv6r0"
TOKEN = "Pt6QrU0BdytQs6mn"

def aes_cbc_encrypt(plain: bytes, key: bytes, iv: bytes) -> str:
    pad = 16 - len(plain) % 16
    plain += bytes([pad]) * pad
    return base64.b64encode(AES.new(key, AES.MODE_CBC, iv).encrypt(plain)).decode()

def get_auth_key(token: str) -> str:
    t = (G + "~" + token + "~" + str(int(time.time()))).encode("utf-8")
    return aes_cbc_encrypt(t, hashlib.md5(G.encode("utf-8")).digest(), G.encode("utf-8"))

def uri_string(uri: str, params: dict, order: str) -> str:
    keys = list(params.keys())
    if order == "sorted": keys = sorted(keys)
    elif order == "reversed": keys = list(reversed(keys))
    return uri + "?" + "&".join(f"{k}={params[k]}" for k in keys)

def get_uri_hash(s: str) -> str:
    return hmac.new(M.encode("utf-8"), s.encode("utf-8"), hashlib.sha1).hexdigest()

PARAMS = {"doc":"HhD1dAJT6obNFTxSr8jcRPtfn5e","mode":"0","fromAcl":"token","acl":"5e66343778305ee1540591dfff4e28f3",
          "utm_media":"web","utm_content":"mtvajp1rj83qdpk56y","utm_source":"","utm_medium":"","utm_activity":"","_uds":"hyyy_biu"}

def request(uri, order, er_mode, ctxid):
    us = uri_string(uri, PARAMS, order)
    h1, h2 = get_auth_key(TOKEN), get_uri_hash(us)
    er = None
    if er_mode == "raw": er = us
    elif er_mode == "json": er = json.dumps(us)
    hd = {"X-token-1": h1, "X-token-2": h2, "X-request-by": "fe-31e8c42",
          "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
          "Referer": "https://yitang.top/fs-doc/5e66343778305ee1540591dfff4e28f3/HhD1dAJT6obNFTxSr8jcRPtfn5e"}
    if er: hd["X-token-er"] = er
    if ctxid: hd["X-Ctxid"] = ctxid
    url = "https://yitang.top" + (uri if uri.startswith("/") else uri.replace("https://yitang.top", "")) + "?" + urllib.parse.urlencode(PARAMS)
    try:
        with urllib.request.build_opener(urllib.request.ProxyHandler({})).open(urllib.request.Request(url, headers=hd), timeout=20) as r:
            return r.status, r.read().decode("utf-8", "replace")[:200]
    except Exception as e:
        return None, repr(e)[:150]

cases = [
    ("/api/feishu/get-doc-blocks", "orig", "raw", None),
    ("/api/feishu/get-doc-blocks", "sorted", "raw", None),
    ("/api/feishu/get-doc-blocks", "reversed", "raw", None),
    ("https://yitang.top/api/feishu/get-doc-blocks", "orig", "raw", None),
    ("/api/feishu/get-doc-blocks", "orig", None, None),
    ("/api/feishu/get-doc-blocks", "orig", "raw", "8"),
    ("/api/feishu/get-doc-blocks", "orig", "json", None),
    ("/api/feishu/get-doc-blocks", "sorted", None, "8"),
]
for uri, order, er, ctxid in cases:
    st, body = request(uri, order, er, ctxid)
    code = ""
    try: code = json.loads(body).get("code")
    except Exception: pass
    print(f"uri={uri[:40]} order={order} er={er} ctx={ctxid} -> {st} code={code}")
    if code == 0:
        print("SUCCESS body head:", body[:400])
