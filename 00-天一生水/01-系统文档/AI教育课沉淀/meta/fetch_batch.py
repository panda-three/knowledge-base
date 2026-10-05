#!/usr/bin/env python3
"""
飞书 wiki 叶子文档批量抓取脚本。
用法: python3 fetch_batch.py <batch_number>
读取 meta/batch_{n}.json，抓取正文存到 raw/ 目录。
"""
import json, subprocess, sys, time, os, re, hashlib

BASE = "/Users/panda/Desktop/knowledge-base/00-天一生水/01-系统文档/AI教育课沉淀"
META_DIR = os.path.join(BASE, "meta")
RAW_DIR = os.path.join(BASE, "raw")
ENV_PREFIX = ["env", "-u", "http_proxy", "-u", "https_proxy", "-u", "HTTP_PROXY", "-u", "HTTPS_PROXY"]

def clean_title(title):
    """清洗标题，去掉噪声后缀，用于文件名。"""
    t = title
    t = re.sub(r'[（(]截图[^）)]*[）)]', '', t)
    t = re.sub(r'-截图笔记$', '', t)
    t = re.sub(r'[（(]阅读优化版[）)]', '', t)
    t = re.sub(r'\s+逐字稿$', '', t)
    t = t.strip().rstrip('-').strip()
    # 文件名安全化
    t = re.sub(r'[\\/:*?"<>|]', '_', t)
    return t if t else "untitled"

def safe_filename(title, obj_token):
    """生成安全文件名，过长截断，加短 hash 防重名。"""
    clean = clean_title(title)
    short_hash = hashlib.md5(obj_token.encode()).hexdigest()[:6]
    # 限制长度
    if len(clean) > 80:
        clean = clean[:80]
    fname = f"{clean}__{short_hash}.md"
    return fname

def fetch_docx(obj_token):
    """抓取 docx 类型文档，返回 markdown 正文。"""
    cmd = ENV_PREFIX + ["lark-cli", "docs", "+fetch", "--doc", obj_token,
                        "--doc-format", "markdown", "--as", "user", "--format", "json"]
    for attempt in range(3):
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
            if r.returncode == 0:
                data = json.loads(r.stdout)
                if data.get("ok"):
                    content = data.get("data", {}).get("document", {}).get("content", "")
                    if content:
                        return content, None
                    else:
                        return "", "empty content"
                else:
                    err = data.get("msg", data.get("error", "unknown"))
                    if attempt < 2:
                        time.sleep(2 * (attempt + 1))
                        continue
                    return None, f"api error: {err}"
            else:
                if attempt < 2:
                    time.sleep(2 * (attempt + 1))
                    continue
                return None, f"exit {r.returncode}: {r.stderr[:200]}"
        except Exception as e:
            if attempt < 2:
                time.sleep(2)
                continue
            return None, f"exception: {e}"
    return None, "max retries"

def fetch_markdown_file(obj_token):
    """抓取原生 markdown 文件类型，返回正文。"""
    cmd = ENV_PREFIX + ["lark-cli", "markdown", "+fetch", "--file-token", obj_token,
                        "--as", "user", "--format", "json"]
    for attempt in range(3):
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
            if r.returncode == 0:
                data = json.loads(r.stdout)
                if data.get("ok"):
                    content = data.get("data", {}).get("content", "")
                    if content:
                        return content, None
                    else:
                        return "", "empty content"
                else:
                    err = data.get("msg", data.get("error", "unknown"))
                    if attempt < 2:
                        time.sleep(2 * (attempt + 1))
                        continue
                    return None, f"api error: {err}"
            else:
                if attempt < 2:
                    time.sleep(2 * (attempt + 1))
                    continue
                return None, f"exit {r.returncode}: {r.stderr[:200]}"
        except Exception as e:
            if attempt < 2:
                time.sleep(2)
                continue
            return None, f"exception: {e}"
    return None, "max retries"

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fetch_batch.py <batch_number>")
        sys.exit(1)
    
    batch_num = sys.argv[1]
    batch_file = os.path.join(META_DIR, f"batch_{batch_num}.json")
    
    with open(batch_file, encoding="utf-8") as f:
        docs = json.load(f)
    
    print(f"=== Batch {batch_num}: {len(docs)} docs ===")
    
    results = []
    success = 0
    failed = 0
    
    for i, doc in enumerate(docs):
        obj_token = doc["obj_token"]
        title = doc["title"]
        obj_type = doc["obj_type"]
        path = doc.get("path", title)
        
        fname = safe_filename(title, obj_token)
        fpath = os.path.join(RAW_DIR, fname)
        
        # 跳过已存在的文件（增量）
        if os.path.exists(fpath) and os.path.getsize(fpath) > 0:
            content_len = os.path.getsize(fpath)
            print(f"  [{i+1}/{len(docs)}] SKIP(exists): {title} ({content_len}B)")
            results.append({
                "obj_token": obj_token, "title": title, "path": path,
                "obj_type": obj_type, "filename": fname,
                "status": "skipped_exists", "content_length": content_len,
                "error": None
            })
            success += 1
            continue
        
        # 根据类型选择抓取方式
        if obj_type == "file" or title.endswith(".md"):
            content, err = fetch_markdown_file(obj_token)
            fetch_method = "markdown"
        else:
            content, err = fetch_docx(obj_token)
            fetch_method = "docx"
        
        if content is not None:
            # 写入文件，带 frontmatter 元信息
            frontmatter = f"---\nobj_token: {obj_token}\ntitle: {title}\nfeishu_path: {path}\nobj_type: {obj_type}\nfetch_method: {fetch_method}\n---\n\n"
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(frontmatter + content)
            content_len = len(content)
            print(f"  [{i+1}/{len(docs)}] OK: {title} ({content_len} chars, {fetch_method})")
            results.append({
                "obj_token": obj_token, "title": title, "path": path,
                "obj_type": obj_type, "filename": fname,
                "status": "ok", "content_length": content_len,
                "error": None
            })
            success += 1
        else:
            print(f"  [{i+1}/{len(docs)}] FAIL: {title} -> {err}")
            results.append({
                "obj_token": obj_token, "title": title, "path": path,
                "obj_type": obj_type, "filename": fname,
                "status": "failed", "content_length": 0,
                "error": err
            })
            failed += 1
        
        # 限流：间隔 ≥0.5s
        time.sleep(0.6)
    
    # 保存批次结果
    result_file = os.path.join(META_DIR, f"fetch_result_batch_{batch_num}.json")
    with open(result_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n=== Batch {batch_num} 完成: 成功/跳过={success}, 失败={failed} ===")
    print(f"结果保存: {result_file}")
    
    if failed > 0:
        print("\n失败列表:")
        for r in results:
            if r["status"] == "failed":
                print(f"  - {r['obj_token']} | {r['title']} | {r['error']}")

if __name__ == "__main__":
    main()
