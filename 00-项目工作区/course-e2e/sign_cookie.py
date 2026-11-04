# -*- coding: utf-8 -*-
import base64, hashlib, hmac, json, time, urllib.request, urllib.parse
from Crypto.Cipher import AES

G = "BDFHJLNPRTVXZ\\^`"
M = "ether7sv6te7sv6he7sv6there7sv6r0"
TOKEN = "Pt6QrU0BdytQs6mn"
COOKIE = "utm_content=mtvajp1rj83qdpk56y; _vway_sessid=8; yt_request_id=1793425682873300001603453330"

def aes_cbc_encrypt(plain: bytes, key: bytes, iv: bytes) -> str:
    pad = 16 - len(plain) % 16
    plain += bytes([pad]) * pad
    return base64.b64encode(AES.new(key, AES.MODE_CBC, iv).encrypt(plain)).decode()

def get_auth_key(token: str) -> str:
    t = (G + "~" + token + "~" + str(int(time.time()))).encode("utf-8")
    return aes_cbc_encrypt(t, hashlib.md5(G.encode("utf-8")).digest(), G.encode("utf-8"))

def uri_string(uri, params, order="orig"):
    keys = list(params.keys())
    if order == "sorted": keys = sorted(keys)
    return uri + "?" + "&".join(f"{k}={params[k]}" for k in keys)

def get_uri_hash(s): return hmac.new(M.encode(), s.encode(), hashlib.sha1).hexdigest()

PARAMS = {"doc":"HhD1dAJT6obNFTxSr8jcRPtfn5e","mode":"0","fromAcl":"token","acl":"5e66343778305ee1540591dfff4e28f3",
          "utm_media":"web","utm_content":"mtvajp1rj83qdpk56y","utm_source":"","utm_medium":"","utm_activity":"","_uds":"hyyy_biu"}
URL = "https://yitang.top/api/feishu/get-doc-blocks?" + urllib.parse.urlencode(PARAMS)

def call(sign, cookie, tok):
    hd = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
          "Referer": "https://yitang.top/fs-doc/5e66343778305ee1540591dfff4e28f3/HhD1dAJT6obNFTxSr8jcRPtfn5e"}
    if cookie: hd["Cookie"] = cookie
    if sign:
        us = uri_string("/api/feishu/get-doc-blocks", PARAMS)
        hd["X-token-1"] = get_auth_key(tok)
        hd["X-token-2"] = get_uri_hash(us)
        hd["X-token-er"] = us
        hd["X-request-by"] = "fe-31e8c42"
    try:
        with urllib.request.build_opener(urllib.request.ProxyHandler({})).open(urllib.request.Request(URL, headers=hd), timeout=20) as r:
            return r.status, r.read().decode("utf-8", "replace")[:250]
    except Exception as e:
        return None, repr(e)[:150]

for sign in (False, True):
    for ck in (None, COOKIE):
        st, body = call(sign, ck, TOKEN)
        code = ""
        try: code = json.loads(body).get("code")
        except Exception: pass
        print(f"sign={sign} cookie={'Y' if ck else 'N'} tok=short -> {st} code={code} :: {body[:120]}")
# TOKEN 完整 JSON 形态
for tok in ('{"$v":"Pt6QrU0BdytQs6mn","$ex":1805758440}', 'Pt6QrU0BdytQs6mn'):
    st, body = call(True, COOKIE, tok)
    code = ""
    try: code = json.loads(body).get("code")
    except Exception: pass
    print(f"sign=Y cookie=Y tok={tok[:20]}... -> {st} code={code} :: {body[:120]}")
