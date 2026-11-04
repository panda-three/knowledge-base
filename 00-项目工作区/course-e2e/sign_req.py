# -*- coding: utf-8 -*-
"""复刻 yitang get-doc-blocks 签名（X-token-1/2/er）并请求，黑盒验证签名参数组合"""
import base64, hashlib, hmac, json, time, urllib.request, urllib.parse
from Crypto.Cipher import AES

G = "BDFHJLNPRTVXZ\\^`"          # 16 字节常量
M = "ether7sv6te7sv6he7sv6there7sv6r0"   # 混淆常量（页面实测）
TOKEN = "Pt6QrU0BdytQs6mn"

def aes_cbc_encrypt(plain: bytes, key: bytes, iv: bytes) -> str:
    pad = 16 - len(plain) % 16
    plain += bytes([pad]) * pad
    return base64.b64encode(AES.new(key, AES.MODE_CBC, iv).encrypt(plain)).decode()

def get_auth_key(token: str) -> str:
    t = (G + "~" + token + "~" + str(int(time.time()))).encode("utf-8")
    key = hashlib.md5(G.encode("utf-8")).digest()
    iv = G.encode("utf-8")
    return aes_cbc_encrypt(t, key, iv)

def uri_string(method: str, uri: str, params: dict, data=None, order: str = "orig") -> str:
    keys = list(params.keys())
    if order == "sorted":
        keys = sorted(keys)
    n = uri + "?"
    n += "&".join(f"{k}={params[k]}" for k in keys)
    if method.upper() == "POST" and data is not None:
        n += "\n\n" + json.dumps(data)
    return n

def get_uri_hash(s: str) -> str:
    return hmac.new(M.encode("utf-8"), s.encode("utf-8"), hashlib.sha1).hexdigest()

PARAMS = {
    "doc": "HhD1dAJT6obNFTxSr8jcRPtfn5e",
    "mode": "0",
    "fromAcl": "token",
    "acl": "5e66343778305ee1540591dfff4e28f3",
    "utm_media": "web",
    "utm_content": "mtvajp1rj83qdpk56y",
    "utm_source": "",
    "utm_medium": "",
    "utm_activity": "",
    "_uds": "hyyy_biu",
}

def request(uri, order):
    us = uri_string("GET", uri, PARAMS, order=order)
    h1 = get_auth_key(TOKEN)
    h2 = get_uri_hash(us)
    url = "https://yitang.top" + uri + "?" + urllib.parse.urlencode(PARAMS)
    req = urllib.request.Request(url, headers={
        "X-token-1": h1,
        "X-token-2": h2,
        "X-token-er": us,
        "X-request-by": "fe-31e8c42",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Referer": "https://yitang.top/fs-doc/5e66343778305ee1540591dfff4e28f3/HhD1dAJT6obNFTxSr8jcRPtfn5e",
    })
    try:
        with urllib.request.build_opener(urllib.request.ProxyHandler({})).open(req, timeout=30) as r:
            body = r.read().decode("utf-8", "replace")
            return r.status, body[:600]
    except Exception as e:
        return None, repr(e)[:300]

if __name__ == "__main__":
    for uri in ["/api/feishu/get-doc-blocks", "/feishu/get-doc-blocks"]:
        for order in ["orig", "sorted"]:
            st, body = request(uri, order)
            print(f"uri={uri} order={order} -> status={st}")
            print("   ", body.replace("\n", " ")[:400])
