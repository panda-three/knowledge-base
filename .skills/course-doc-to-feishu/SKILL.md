---
name: course-doc-to-feishu
description: 将「一堂创业课」（yitang.top/fs-doc/）等需要登录的课程文档链接**完整重转录**（保留全部图片+标题层级+高亮/加粗），结构化后存入飞书「AI教育课」知识库（space_id=7669431379494440158）。当用户给出 yitang.top/fs-doc 链接或同类课程文档站链接（支持**单链接或批量多链接**），并要求提取/转录/保存到 AI教育课 知识库时使用。默认保留图片和格式（高亮用加粗代替），交付 wiki 链接列表。支持以 yitang 原文档为标准，对已转录的飞书版做差异比对与重新对齐。
---

# course-doc-to-feishu

把课程文档链接 → **完整重转录（图片+格式）** → 存入飞书「AI教育课」知识库。

## ⚠️ 开工前必检：任务边界与图片策略（不可跳过）

**本技能与 course-images-to-feishu 的边界必须先分清，否则会犯方向性错误。**

| 维度 | 本技能 course-doc-to-feishu | course-images-to-feishu |
|---|---|---|
| 输入 | yitang.top/fs-doc/ 等课程文档**链接** | 本地课程**截图文件夹** |
| 图片策略 | **必须保留全部图片**（含第 6 步分批插入流程） | 纯文字转录，不保留图片 |
| 格式 | 保留标题层级 + 加粗 + 图片 | 纯文字 |
| 典型错误 | 把"图片太冗余"的截图偏好套用到文档链接，跳过全部图片 | — |

**开工前必须逐项确认：**
1. 输入是文档链接（http/https），不是本地截图文件夹 → 确认用本技能
2. 图片策略 = 保留全部图片 → 第 5 步必须生成 `![](url)`，第 6 步必须执行分批插入
3. 最终验证（第 9 步）必须检查图片数 > 0 且 = 预期数；**图片数为 0 时禁止交付，必须排查原因**

**用户偏好区分（不可混用）：**
- "课程截图转文字任务中，图片太冗余、纯文字即可" → 仅适用于 course-images-to-feishu
- "课程文档链接转录必须保留全部图片和加粗格式" → 适用于本技能

## 前置环境（必读）

- `lark-cli` 可用；**本机代理坑**：所有 lark-cli 命令必须加前缀 `env -u http_proxy -u https_proxy -u HTTP_PROXY -u HTTPS_PROXY`，否则连接被拒。本机 `http_proxy=http://127.0.0.1:7890` 代理不可用（curl 000 超时），unset 后直连正常。
- 目标知识库：AI教育课，`space_id = 7669431379494440158`。
- 浏览器操作走 `mac_computer_use_tool`（plane="bu"，seed_browser_use）。先读 `browser-use-automation-mac` 技能。
- **飞书 Markdown 导入限制**：支持网络图片 `![](url)`（自动下载）、支持 `**加粗**`；**不支持** `==高亮==` 语法和 HTML 内联样式 → 高亮统一用加粗代替。
- **大请求体限制（实测）**：`lark-cli docs +create` 对约 90KB 以上的内容请求体会**稳定超时**（约 11s）。超长文档必须分块（每块 ≤25KB）——chunk0 用于 create，其余 chunk 用 `+update --command append` 追加（见第 6 步）。

## 工作流

### 0. 任务类型判定（先做这一步，再开始采集）
- 输入是 yitang.top/fs-doc/ 或同类课程文档站链接 → 继续本技能
- 输入是本地截图文件夹/图片 → **停止本技能，改用 course-images-to-feishu**
- 确认图片策略：本技能必须保留全部图片，不接受"纯文字"处理；若用户明确要求纯文字，需先确认是否误用了技能
- **对齐任务判定**：若用户给出"以 yitang 原文档为标准，重新对齐/比对已有飞书版"，则本次为对齐任务——新增执行第 5.5 步（加粗预处理）与第 9 步的加粗 XML 验证，其余流程相同

### 1. 打开链接，处理登录墙
- `bu.navigate(url)` + `bu.wait_for_load`。
- 若跳转登录页/SSO → **立即**调用 `interaction_request_action(type="browserControl")` 请用户扫码/快捷登录，不绕行。

### 2. 滚到顶部，确认页面结构
- 强力滚到顶部：`bu.scroll(500,300,"up",amount=10)` 重复 15-20 次，确认 `page_info().sy == 0`。
- 探查一个含高亮的 text-block 内部结构，确认 class 命名（见下方 DOM 采集 JS）。
- 注意：yitang 页面是**虚拟列表**（DOM 节点复用），`window.scrollTo` 后内容可能不随视口更新；以 `bu.scroll`（视口坐标）逐步滚动为准，每次滚动后等待 0.5s+ 再提取。

### 3. DOM 滚动采集（核心，保留图片+格式）

**不要用 `bu.get_page_text()`**（会丢失图片和格式）。用 `bu.js()` 提取结构化 block 数据。

采集 JS（每次视口提取，分段滚动增量保存到 `/tmp/collect_<name>.json`）：

```javascript
(() => {
  const blocks = Array.from(document.querySelectorAll('.block'));
  return blocks.map(b => {
    const cls = b.className.toString();
    const m = cls.match(/block-([A-Za-z0-9]+)/);
    const blockId = m ? m[1] : '';
    let type = 'text';
    if (cls.includes('docx-heading1-block')) type = 'h1';
    else if (cls.includes('docx-heading2-block')) type = 'h2';
    else if (cls.includes('docx-heading3-block')) type = 'h3';
    else if (cls.includes('docx-image-block')) type = 'image';
    else if (cls.includes('docx-bullet-block')) type = 'bullet';
    else if (cls.includes('docx-ordered-block')) type = 'ordered';
    else if (cls.includes('docx-quote-block')) type = 'quote';
    else if (cls.includes('docx-code-block')) type = 'code';

    let text = '', imgUrl = '';
    if (type === 'image') {
      const img = b.querySelector('img');
      imgUrl = img ? (img.getAttribute('src') || '') : '';
    } else {
      const editor = b.querySelector('.text-editor, .heading-content');
      if (editor) {
        const lines = Array.from(editor.querySelectorAll('.ace-line'));
        if (lines.length > 0) {
          text = lines.map(line => {
            let lineText = '';
            const walker = document.createTreeWalker(line, NodeFilter.SHOW_TEXT, null);
            let node;
            while (node = walker.nextNode()) {
              const t = node.textContent || '';
              if (!t) continue;
              // 检查父 span 是否加粗/高亮
              let parent = node.parentElement, isBold = false;
              while (parent && parent !== line) {
                const pCls = (parent.className || '').toString();
                if (pCls.includes('bold') || pCls.includes('text-highlight-background')) {
                  isBold = true; break;
                }
                parent = parent.parentElement;
              }
              lineText += isBold ? ('**' + t + '**') : t;
            }
            return lineText;
          }).join('\n');
        } else {
          text = (editor.innerText || '').trim();
        }
      }
      if (!text || text.trim() === '\u200b') text = (b.innerText || '').trim();
    }
    return {blockId, type, text, imgUrl};
  });
})()
```

采集循环（Python，分多段，每段 15-25 步，防 300s 超时）：
```python
for step in range(20):
    blocks = extract_blocks()  # 调用上面的 JS
    data.extend(blocks)
    bu.scroll(500, 400, "down", amount=3)
    time.sleep(0.35)
# 每段结束 json.dump(data, open('/tmp/collect_x.json','w'))
```
- 结束条件：`sy >= ph - h` 或连续 3 次 sy 不变。
- `bu.js()` 返回的已是 list，无需再 `json.loads()`。

### 3a. 结构化 dataJson 采集（推荐主路径，实测最可靠）

**DOM 滚动采集（第 3 步）是备选方案**：yitang 页面是虚拟列表，滚动采集会因 DOM 节点复用漏块、漏图或图片错位（实测：354 张的旧采集 vs 页面真实数据 355 张，存在 1 张遗漏导致后续全部错位风险）。**优先直接从页面 Vue 组件读取渲染数据源 `dataJson`**——它是页面渲染的完整权威数据（含文本、加粗、图片 URL、块顺序、嵌套结构），一次导出、零漏采。

```javascript
// 在页面上下文执行（bu.js），找到 fsdoc 组件的 $data.dataJson
(() => {
  const app = document.querySelector('#app');
  let vm = null;
  const seen = new Set();
  const walk = (el) => {
    if (!el || seen.has(el) || vm) return;
    seen.add(el);
    if (el.__vue__ && el.__vue__.$data && el.__vue__.$data.dataJson) { vm = el.__vue__; return; }
    for (const c of el.children || []) walk(c);
  };
  walk(app);
  // dataJson 结构：{blockId, type, sum, blockAttr, childrens, l1blockId}
  // 递归 DFS 导出每块：{t: 类型, a: blockAttr, c: childrens长度}
  const dj = vm.$data.dataJson;
  const out = [];
  const wb = (b) => {
    out.push({t: Number(b.type), a: b.blockAttr, c: (b.childrens||[]).length});
    (b.childrens || []).forEach(wb);
  };
  (dj.childrens || []).forEach(wb);
  window.__full = out;
  return JSON.stringify({total: out.length, bytes: JSON.stringify(out).length});
})()
```

**块类型映射（实测确认）**：

| type | 含义 | blockAttr 关键字段 |
|---|---|---|
| 2 | 文本 | `text.elements[].text_run.content`（`text_element_style.bold` 为加粗标记） |
| 3/4/5 | heading1/2/3 | `heading1/2/3.elements`（同 text） |
| 12 | bullet 无序列表 | `bullet.elements` |
| 13 | ordered 有序列表 | `ordered.style.sequence`（'1'/'2'/'auto'；'auto' 需按组内前项+1 连续编号） |
| 19 | callout 提示框 | `callout.emoji_id`（'sunflower'→渲染为 🌻） |
| 22 | 分割线 | 无 |
| 23 | 文件/视频 | `file.name`（飞书无法导入 file 块，转文本占位 `📹 名称`） |
| 24/25 | grid / grid_column（网格容器） | 容器本身跳过，子块按顺序输出（飞书 markdown 无网格） |
| 27 | 图片 | `cdnUrl`（真实图片 URL） |
| 33 | view 容器 | 跳过容器，子块正常输出 |
| 34 | quote_container 引用容器 | 子块内容流式输出（可加 `>` 前缀近似） |

**取回**：`window.__full` 分批 `bu.js("JSON.stringify(window.__full.slice(a,b))")`（每批 300 条，防止返回截断），本地存 JSON。**注意**：数据可能很大（2893 块约 1.2MB），分批必须做。

**其他可用数据源**：`vm.$data.dataTextSearchArray`（1413 项渲染文本索引，含 blockId+index+text，可交叉验证）、`vm.$data.previewSrcList`（图片 URL 列表，**仅供核对**，不要作为图片顺序来源——顺序以 dataJson 的 DFS 为准）。

**对齐/比对任务**：dataJson 即 yitang 当前页面权威标准；对比飞书版时用"文本流 diff"（两侧都去掉 `**` 与零宽后按块序列对比）精确定位图片/文本差异。

### 4. 清洗去重（跑脚本）

```python
import json, re
data = json.load(open('/tmp/collect_x.json'))

# 1. 按 (type, text, imgUrl) 内容去重（虚拟列表会重复渲染）
seen = set(); unique = []
for b in data:
    key = (b['type'], b['text'].strip(), b.get('imgUrl',''))
    if key not in seen:
        seen.add(key); unique.append(b)

# 2. 过滤空文本（零宽字符 \u200b 也算空）
# 3. 图片按出现位置顺序保留（！！！不要按 URL 去重——复用图会在多处出现，
#    去重会漏图；同一 URL 在第 N 处出现时要保留第 N 个位置）
# 4. 截断评论区：遇到 "全文评论" 或 "名字 2024-01-01 12:00:00" 格式行则截断
```

> ⚠️ **图片去重红线（实测踩坑）**：yitang 文档中同一图片 URL 常被复用多处（如 `fb73e086…` 在阳谋后/Partner 后/我先调研后等多处出现；354 个图片位置仅 339 个唯一 URL）。**必须按位置逐个保留**，任何形式的"按 URL 去重"都会漏图。

### 5. 生成 Markdown（含图片+加粗）

- h1 → `## `、h2 → `### `、h3 → `#### `
- image → `![](imgUrl)`（网络URL，飞书会自动下载）
- bullet → `- `、ordered → 数字列表、quote → `> `、code → ``` 包裹
- text → 原样输出（已含 `**加粗**` 标记）
- 后处理加粗：合并相邻 `**a****b**` → `**ab**`，清理空加粗 `****`
- 标题缺失补全：DOM 采集可能因虚拟列表边界遗漏个别 h1/h2，用纯文本版（`bu.get_page_text()` 采集的版本）对比补全缺失标题和内容
- 文首/文末细节核对：若 yitang 页面文首有 🌻 行、文末有重复段/「真诚点赞，手留余香」/「（点击跳转）」等，必须逐字保留（采集易漏）
- 保存为 `<项目目录>/course_<短名>_v2.md`

### 5.5 加粗标记飞书兼容性预处理（对齐任务/含紧贴加粗的文档必做，实测规则）

**飞书 Markdown 导入对 `**` 的解析与 yitang 页面不同，以下三种写法会出问题（全部经最小测试文档 + XML fetch 实测确认）：**

| 模式 | 示例 | 飞书导入结果 | 修复方案（实测有效） |
|---|---|---|---|
| A. 开标签 `**` 后紧跟全角标点 | `概念**：OPT（One Person Team）**` | 该对加粗转义为 `\*\*`（字面显示） | 开标签后插零宽空格：`概念**\u200b：OPT…**` → 渲染 `<b>：OPT…</b>`，加粗范围与 yitang 一致（含标点） |
| B. 开标签 `**` 后紧跟空格 | `** AI 落地**` | 连锁错乱：字面 `**` 残留 + 相邻文本被错误加粗 | 开标签后插零宽空格：`**\u200b AI 落地**` → `<b> AI 落地</b>` |
| C. 相邻独立加粗被合并 | `**AI 负责**收集、读取、归档、分析和预审；**人负责**定义标准。` | 整段合并成一个粗体：`<b>AI 负责收集、读取、归档、分析和预审；人负责</b>` | 第一对闭标签后插普通空格：`**AI 负责** 收集、读取…**人负责**定义…` → 两段独立加粗（代价：1 个可见空格） |
| D. 闭标签前有空格 | `**动作5 **接着…` | 闭标签失效 → 与下一对合并 | 去掉尾随空格 + 闭标签后插空格：`**动作5** 接着…` |
| E. 仅空格分隔的相邻加粗对 | `**有** **50T**`、`**：** **OPT…**` | 合并成一个粗体 `**有 50T**`（或 `**\u200b：OPT…**`） | **无需修复**：中间无其他内容，合并后区域全部加粗，视觉与源等价（内容级一致） |
| F. 单独加粗的标点对 | `…修正**。**` | 句号并入前一个加粗对（`**…修正。**`） | **无需修复**：标点加粗视觉无差异，内容等价 |

**实现建议（状态机，实测验证）**：不要用正则一次性替换（无法区分开/闭标签）。用状态机从左到右扫描：
- 开标签（当前不在加粗内）`**` 后跟全角标点或空格 → 输出 `**\u200b`（模式 A/B）
- 闭标签（当前在加粗内）`**` → 若前一个字符是空格先去掉（模式 D），输出 `**`；若后面紧跟 `**`（相邻对）插普通空格（模式 C 相邻变体）
- 行内完整加粗对 ≥2 且闭标签后紧跟普通字符（非 `**`、非空格、非零宽）→ 闭标签后插普通空格（模式 C 一般情况）
- 生成后自检：全文 `**` 数量为偶数；已知危险写法清零

**检测脚本**（对生成的 Markdown 全量扫描，输出需修复位置）：

```python
import re
md = open('course_x_v2.md').read()
PUNCT = set('：，。；！？、""''（）【】《》<>"\'(),.;:!?')
for ln_no, line in enumerate(md.split('\n'), 1):
    stars = [m.start() for m in re.finditer(r'\*\*', line)]
    # 成对扫描（奇数位开、偶数位闭）
    for i in range(0, len(stars)-1, 2):
        s, e = stars[i], stars[i+1]
        content = line[s+2:e]
        if '*' in content or not content.strip(): continue
        nxt = line[s+2] if s+2 < len(line) else ''
        if nxt.isspace() or nxt in PUNCT:  # 模式 A/B
            print(f'L{ln_no} 开标签后危险字符: {line[max(0,s-10):e+10]}')
    # 相邻加粗对（模式 C/D）：闭标签后紧跟文字且两对间含标点
    spans = [(m.start(), m.end()) for m in re.finditer(r'\*\*[^*]+\*\*', line)]
    for i in range(len(spans)-1):
        s1, e1 = spans[i]; s2, e2 = spans[i+1]
        mid = line[e1:s2]
        if not mid or '**' in mid: continue
        if mid[0].isspace() or mid[0] in PUNCT: continue
        if any(ch in PUNCT for ch in mid):
            print(f'L{ln_no} 相邻加粗合并风险: {line[s1:e2][:60]}')
```

**修复实现要点**：
- 零宽空格 `\u200b` 插入**开标签后**有效（阻止 A/B 类失效）；插入**闭标签后无效**（飞书忽略，不用于修复合并）。
- 模式 C/D 只能用**普通空格**修复（闭标签后）。引入的可见空格是飞书解析限制下的最小干预，视觉无感；加粗范围与 yitang 一致优先于空格级差异。
- 修复后必须自检：全文 `**` 数量为偶数；已知危险写法（`**：`、`** 文字`、`**"`、`X **`）清零。
- 特殊案例：yitang 页面可能存在"加粗逗号"等意外格式（如 `AI读论文**，**确实…`——逗号真实加粗），以页面采集结果为准，用模式 A 修复（`**\u200b，**`），不要擅自改写加粗范围。

### 6. 写入飞书（关键：分块创建 + 分批插入图片）

**两个独立的超时/限流坑，必须分开处理：**
- **坑1 创建超时**：含大量占位符的 noimg.md 若超过约 25KB/块，`docs +create` 会 timeout。**必须分块**（每块 ≤25KB，在 `[IMAGE_PLACEHOLDER_N]` 行后断开）。
- **坑2 图片插入限流**：一次性导入含 50+ 张图片的 Markdown 会服务端超时，且连续快速 `str_replace` >50 次会触发 `invalid_` 限流。**必须逐张插入 + 间隔 ≥2s**。

#### 6a. 创建无图片版（分块 create + append）

```python
# 把所有 ![](url) 行替换为占位符 [IMAGE_PLACEHOLDER_N]（按出现顺序编号）
# 保存为 course_x_v2_noimg.md；校验占位符总数 == 图片总数
import re
def ph(m):
    n = len(re.findall(r'!\[[^\]]*\]\([^)]+\)', md[:m.start()])) + 1
    return f'[IMAGE_PLACEHOLDER_{n}]'
noimg = re.sub(r'!\[[^\]]*\]\([^)]+\)', ph, md)
assert noimg.count('[IMAGE_PLACEHOLDER_') == len(imgs)

# 分块：按行切，每块 ≤25KB（在图片占位符行后断开）
lines = noimg.split('\n'); chunks, cur, curlen = [], [], 0
for ln in lines:
    cur.append(ln); curlen += len(ln) + 1
    if curlen > 22000 and ln.startswith('[IMAGE_PLACEHOLDER_'):
        chunks.append('\n'.join(cur)); cur, curlen = [], 0
if cur: chunks.append('\n'.join(cur))
```

```bash
# chunk0 用于 create
env -u http_proxy ... lark-cli docs +create --doc-format markdown \
  --title "<原标题>" --content "@./chunk0.md" --as user --format json
# 得 document_id；其余 chunk 逐个 append
env -u http_proxy ... lark-cli docs +update --doc "<document_id>" \
  --command append --content "@./chunk1.md" --doc-format markdown --as user --format json
# chunk2、chunk3... 依此类推
```

> 飞书自动行为：create 后文档会在标题下自动插入 `> 部分内容由豆包生成` blockquote，属正常现象，无需处理。

#### 6b. 逐张 str_replace 插入图片（后台脚本）

**限流规律（本轮多次实测，比旧经验更严）**：连续约 20-50 次 `str_replace` 写调用（无论间隔 3s 还是 8s）会触发服务端临时拒绝（响应非 JSON，报 parse 错误），**停止请求 2-3 分钟后自动恢复**（手动单张总是成功）。**多脚本并发会显著加剧限流**（3 个脚本并发时 20 张就失败）——**续跑前必须 `ps aux | grep insert` 确认无其他插入脚本在跑**。

**稳跑策略（实测可靠，355 张约 60-70 分钟）**：
- 每张间隔 10s；每成功 12 张暂停 150s（重置限流窗口）
- 单张失败 → 退避 300s 后重试同一张（不跳过、不立即重试）
- 进度实时写入日志（`序号 OK/RETRY` 行），可从断点续跑（脚本启动时 fetch 文档，找残留最小占位符序号作为起点）

```python
# 核心循环骨架（完整脚本见实测案例：/tmp/insert_v2.py）
for i in range(START, TOTAL+1):
    if consec > 0 and consec % 12 == 0:
        time.sleep(150)   # 限流窗口重置
    out = call(["lark-cli","docs","+update","--doc",DOC,"--command","str_replace",
                "--pattern",f"[IMAGE_PLACEHOLDER_{i}]","--content",f"![]({url})",
                "--doc-format","markdown","--as","user","--format","json"])
    if ok: consec += 1
    else: time.sleep(300)  # 退避后重试同一张
    time.sleep(10)
```

> ⚠️ **系统重启会清空 /tmp**（实测踩坑）：`imgs.json`、markdown 等中间产物放 /tmp 会因重启丢失。**关键产物同时放项目目录**，且保留"从页面 dataJson 重新导出"的脚本（数据源在页面，可随时重建中间文件）。

#### 6c. 图片插入的块级风险与修复（实测铁律，必读）

**str_replace 匹配范围限制（决定性实测）**：`str_replace` 的 pattern **只能匹配占位符标记文本**（`[IMAGE_PLACEHOLDER_N]`）；**任何普通文本（中文/英文/标题）做 pattern 都会 1013 not found**（即使该文本明确存在于文档中，append 后也不行）。**原因**：lark-cli 的 str_replace 只对"create 时生成的占位符标记"生效。**需要按内容定位/修复时**：用 `docs +fetch --detail with-ids` 拿到块 ID，再用 `block_replace`（整块替换）/`block_insert_after`（块后插入）。

**图片插入吞块风险（本次最大事故）**：**若占位符与文本在同一块**（create 时 markdown 单换行合并，XML 里表现为 `[PH]<br/>文本…`），str_replace 把占位符换成 `![](url)` 后，**飞书把整块解析为图片块，块内其余文本全部丢失**（实测：编号 40 插入后，40 图后的 40 行文本 + 41-46 六个占位符全部消失；编号 70 插入后，71-77 占位符及 56 行文本全被吞）。**纯占位符块**（`[PH]<br/>[PH]`，无文本）插入**安全**（实测 61 插入后 62/63 保留）。**占位符与文本同块是普遍现象而非个例**：create 时 markdown 单换行合并，一个 `<p>` 内可含「文本<br/>占位符<br/>文本」，**实测 355 张图中有 45 个危险块、约 200+ 占位符与此同块**——**凡占位符与文本同块必须 block_replace，str_replace 只能用于纯占位符块**。

**危险块识别与处理**：
1. `docs +fetch --doc <id> --doc-format xml --detail with-ids` → 找含 `IMAGE_PLACEHOLDER` 的块，**块内除占位符外还有其他文本** → 危险（**注意：块边界解析必须向左找最近的块级开始标签（`<p id=`/`<li id=`/`<h` 等），跳过 `<br/>`/`<b>` 等内联标签；用 `rfind('<')` 会被 `<br/>` 误导，导致漏检——这是 70 号事故的根因**）
2. 危险块处理：**block_replace 整块**——把 XML 块转 markdown（`<b>`→`**`、`<br/>`→`\n`），占位符替换为图片 URL，**图片与文本之间必须用空行分隔**（`![](url)` 前后各加空行，确保图片成为独立块；不加空行会再次吞块）——`block_replace --block-id <id> --content @file`
3. 替换后必须 fetch 验证：占位符消失 + 块内文本保留（**用 XML fetch 验证，markdown fetch 会把图片聚合显示，造成"图片堆叠/文本缺失"的假象**）

**block 操作常见失败**：
- `block_replace` 内容过大（>5KB 含多图）→ 服务器超时（"server time out error"）——**但操作可能已成功**！重试前先 fetch 检查实际状态；仍失败则**拆分**（先只插图，文本用 `block_insert_after` 补回）
- **限流：block_replace 连续约 20 次触发 `internal` 错误**（`"ok": false, "type": "internal"`）——**且 FAIL 的调用可能实际生效**（以 fetch 实际状态为准，不要盲目重试）——**稳跑参数：间隔 45s、每 10 次成功暂停 300s、失败退避 300s**
- `degrade_code=1011 no changes`：**该块已被其他调用成功处理**（重试冗余）——fetch 确认后跳过
- 图片块带 `caption="[]"`（XML 格式插入残留）→ markdown 显示 `![\[\]](url)` 链接样式 → `block_replace` 用纯 `![](url)` 重写该图块
- 文本缺失补回：`block_insert_after --block-id <图块或前文块id> --content @<纯文本文件>`；若插入内容含图+文本，**图与文本空行分隔**，且插入后立刻 fetch XML 验证（markdown 显示可能误导）

**顺序建议**：create 后先做危险块分析 → 危险块用 block_replace → 其余用 str_replace 稳跑（6b）。

### 7. 移入知识库
```bash
env -u http_proxy ... lark-cli wiki +move --obj-type docx \
  --obj-token <document_id> --target-space-id 7669431379494440158 \
  --as user --format json
# 得 node_token，wiki 链接 = https://my.feishu.cn/wiki/<node_token>
```

### 8. 替换旧版（如用户要求"重转录/替换"）
- 删除旧 wiki 节点：`lark-cli wiki +node-delete --node-token <旧node_token> --obj-type wiki --space-id 7669431379494440158 --yes --as user`
- 注意：`--obj-type` 必须是 `wiki`（传 node_token 时），传 docx 会报 not found。

### 9. 验证与交付（硬门槛，不通过禁止交付）
- `lark-cli docs +fetch --doc <document_id> --doc-format markdown` 回读，逐项检查：
  - **图片数 = 预期数**（`content.count('![')`）；若图片数为 0，立即停止交付，排查是否跳过了第 6 步图片插入
  - 占位符残留 = 0（`content.count('IMAGE_PLACEHOLDER')`）；若 > 0，说明有图片插入失败，需重试
  - 标题层级齐全（h1/h2/h3 数量与采集数据一致）、无评论区残留
  - 加粗标记数量 > 0（确认格式未丢失）
- **加粗对齐验证（对齐任务必做）**：`docs +fetch --doc-format xml` 回读，用正则提取所有 `<b>…</b>` 片段，核对第 5.5 步修复过的位置渲染正确（如 `<b>：OPT…</b>`、`<b> AI 落地</b>`、两段独立 `<b>AI 负责</b>…<b>人负责</b>`）；若发现整段被合并成单 `<b>`，回到第 5.5 步修复后重建文档
- **文本流 diff 验证（对齐任务）**：将飞书 fetch 内容与 dataJson 生成稿分别转成"文本流 + 图片标记"（两侧都去掉 `**`、零宽、标题 `#`），用 difflib 对比——任何非加粗的文本差异都必须修复；**加粗被合并（模式 E/F）属内容等价，不算差异**
- **重建决策**：当发现旧转录与权威数据存在**结构性不一致**（图片数不同、`\*\*` 字面残留、文本差异 >30 处）时，**不要修补旧文档**——直接用 dataJson 完整重建（分块 create+append + 重新插图），修补的纠错成本高于重建
- 全部通过后，用 `present_files` 交付 wiki 链接。

## 踩坑速查

| 坑 | 解法 |
|---|---|
| lark-cli 连接被拒 | `env -u http_proxy -u https_proxy -u HTTP_PROXY -u HTTPS_PROXY` 前缀（本机 7890 代理不可用） |
| `docs +create` 大请求体（约 90KB）超时 | 分块：chunk0 create（≤25KB），其余 chunk append |
| 登录墙 | `interaction_request_action(browserControl)` 请用户接管 |
| 用 get_page_text() 丢图片格式 | 用 bu.js() 提取 .block 结构化数据 |
| 虚拟列表重复渲染 | 按 (type,text,imgUrl) 内容去重 |
| 虚拟列表滚动不更新内容 | window.scrollTo 可能无效（DOM 节点复用），用 bu.scroll 视口滚动 + 等待 |
| 图片按 URL 去重漏图 | **禁止**按 URL 去重：同一 URL 复用多处必须按位置逐个保留（354 位置/339 唯一） |
| 一次性导入 50+ 图超时 | 先建无图片版（占位符），再逐张 str_replace 插入 |
| 批量插入图片触发限流 | 间隔 ≥2 秒，失败重试间隔 ≥8 秒，重试 3 次 |
| 限流新规律（2026-09 实测） | 连续 20-50 次写调用必触发（parse 错误）；停止 2-3 分钟自动恢复；**稳跑策略：每 12 张暂停 150s + 失败退避 300s + 间隔 10s** |
| 多插入脚本并发 | **禁止**：3 脚本并发时 20 张就触发限流；续跑前 `ps aux \| grep insert` 确认无并发 |
| 系统重启清空 /tmp | 关键中间产物（imgs.json、md）同时存项目目录；保留 dataJson 再导出脚本 |
| DOM 滚动采集漏图/错位 | 改用 3a 的 dataJson 结构化采集（页面渲染数据源，一次导出零漏采） |
| 仅空格分隔相邻加粗（`**a** **b**`）被飞书合并 | 模式 E：无需修复，合并后区域全加粗，视觉等价 |
| 单独标点加粗（`**。**`）被并入前对 | 模式 F：无需修复，视觉等价 |
| str_replace 对普通文本 pattern 全部 1013 | str_replace 只匹配占位符标记；定位/修复用 `fetch --detail with-ids` + block_replace/block_insert_after |
| 占位符与文本同块时插入图片吞文本 | 先 fetch with-ids 分析危险块（块边界跳过 `<br/>`/`<b>`），block_replace 整块（占位符→图，**图与文本空行分隔**） |
| 危险块分析漏检（用 rfind('<') 找块边界） | 被 `<br/>` 误导；改为向左找最近的块级开始标签（`<p id=`/`<li id=` 等） |
| block_replace 连续 ~20 次触发 internal 错误 | 间隔 45s、每 10 次成功暂停 300s、失败退避 300s；FAIL 可能实际生效，以 fetch 为准 |
| fetch markdown 显示图片聚合/文本缺失 | 假象；用 `--doc-format xml` 验证真实结构 |
| block_replace 大内容服务器超时 | 可能已成功：先 fetch 确认；仍失败则拆成"先插图 + block_insert_after 补文本" |
| block_replace 返回 1011 no changes | 该块已被处理（重试冗余），fetch 确认后跳过 |
| 图片块带 caption="[]"（XML 插入残留） | block_replace 用纯 `![](url)` 重写图块 |
| 开标签 `**` 后紧跟全角标点（`**：`） | 开标签后插零宽空格 `\u200b`（`**\u200b：X**`） |
| 开标签 `**` 后紧跟空格（`** X**`） | 开标签后插零宽空格 `\u200b`（`**\u200b X**`） |
| 相邻独立加粗被合并（`**A**文字，**B**`） | 第一对闭标签后插普通空格（`**A** 文字，**B**`） |
| 闭标签前有空格（`**动作5 **`） | 去尾随空格 + 闭标签后插空格（`**动作5** `） |
| 零宽空格插入位置 | 只能插**开标签后**（阻止失效）；插闭标签后被飞书忽略，不修复合并 |
| 飞书不支持 ==高亮== | 高亮统一用 **加粗** 代替 |
| 标题因虚拟列表边界遗漏 | 用 get_page_text() 纯文本版对比补全缺失标题 |
| 评论区混入正文图片 | 遇到 "全文评论" 或评论者时间戳行截断 |
| `bu.js()` 返回值 | 已是 list，不要再 json.loads() |
| 删除旧 wiki 节点 | --obj-type 必须是 wiki（传 node_token 时） |
| 工具 300s 超时 | 采集分多段，每段增量 json.dump 到 /tmp |
| 加粗标记碎片化 | 后处理合并相邻 **a****b** → **ab**，清理空加粗 **** |
| 飞书自动插入「> 部分内容由豆包生成」blockquote | 属飞书自动行为，正常现象 |
| 把截图任务的"图片太冗余/纯文字"偏好套用到文档链接，跳过全部图片 | 开工前必检（本文件顶部）：文档链接必须保留全部图片；第 9 步图片数=0 禁止交付 |

## 批量处理（多链接）

当用户一次给出多个链接时，按以下流程批量处理，避免重复登录和 API 限流。

### 批量策略总览

| 阶段 | 并行度 | 原因 |
|------|--------|------|
| 登录 | 1 次 | 同站登录态共享，一次登录全链接免登录 |
| DOM 采集 | 串行 | 浏览器一次只能操作一个页面 |
| 清洗+生成MD | 串行/并行均可 | 本地 Python 操作，秒级完成 |
| 创建无图文档 | 并行 ≤3（每文档内部分块 create+append） | API 调用轻量，但并发过高触发限流 |
| 逐张插入图片 | 每文档内部串行，文档间并行 ≤2 | 图片插入是 API 密集操作，总并发控制在 2-3 |
| 移入知识库 | 并行 ≤3 | 轻量 API |
| 删除旧版 | 并行 ≤3 | 轻量 API |

### 批量执行流程

#### 1. 预处理链接列表
```python
# 解析用户给的所有链接，去重，提取短名
urls = [...]  # 用户给的链接列表
for url in urls:
    short_name = extract_short_name(url)  # 从URL路径或页面标题提取
    # 每个链接独立保存中间结果：
    # /tmp/collect_<short_name>.json  — DOM采集原始数据
    # /tmp/imgs_<short_name>.json     — 图片URL列表（按位置，含重复）
    # <项目目录>/course_<short_name>_v2.md      — 含图Markdown（已做 5.5 加粗预处理）
    # <项目目录>/course_<short_name>_v2_noimg.md — 无图Markdown（占位符版）
```

#### 2. 一次登录，批量采集（串行）
- 打开第一个链接，处理登录墙（`interaction_request_action`）。
- 登录态在浏览器会话内保持，同站后续链接**无需重新登录**。
- 用 `bu.new_tab(url)` 打开后续链接，`bu.switch_tab()` 切换。
- 每个链接按单链接流程完成 DOM 采集（滚到顶部→分段滚动→bu.js提取→增量保存）。
- **采集完一个再切下一个**，不要同时滚动多个标签页（bu 只附着一个 tab）。

#### 3. 批量清洗+生成Markdown（本地，快速）
- 对每个链接的采集数据独立跑清洗脚本（去重、截断评论区、生成MD、提取图片URL列表、**执行第 5.5 步加粗预处理**）。
- 这步是本地 Python 操作，几秒完成一个，可以串行也可以写一个循环批量处理。

#### 4. 批量创建无图文档（并行 ≤3，每文档内分块）
```bash
# 对每个文档：先分块（≤25KB），chunk0 create，其余 append
env -u http_proxy ... lark-cli docs +create --doc-format markdown \
  --title "<标题>" --content "@./course_x_v2_noimg_chunk0.md" --as user --format json
# 然后逐个 append chunk1..n
```
- 最多同时 3 个文档并发，避免触发 API 限流。
- 记录每个文档的 `document_id`。

#### 5. 批量插入图片（每文档串行，文档间并行 ≤2）
- 每个文档内部：逐张 `str_replace` 插入图片（间隔 ≥2 秒，失败重试 3 次）。
- 文档之间：最多同时跑 2 个文档的图片插入（总 API 并发控制在 2-3）。
- **关键**：所有文档的图片插入共享同一个限流预算，不要每个文档都全速跑。
- 可以写一个后台脚本，用 `xargs -P 2` 或 Python `concurrent.futures` 控制并发。

#### 6. 批量移入知识库（并行 ≤3）
```bash
env -u http_proxy ... lark-cli wiki +move --obj-type docx \
  --obj-token <doc_id> --target-space-id 7669431379494440158 --as user --format json
```

#### 7. 批量替换旧版（如需要）
- 对每个旧文档执行 `wiki +node-delete`（--obj-type wiki --yes）。
- 并行 ≤3。

#### 8. 批量验证+交付
- 对每个新文档 `docs +fetch --doc-format markdown` 回读：
  - 图片数 = 预期数
  - 占位符残留 = 0
  - 标题层级齐全
  - 第 5.5 步修复点渲染正确（加粗对齐，XML fetch 核对）
- 用 `present_files` 一次性交付所有 wiki 链接（非媒体文件可共享一次调用）。

### 批量失败处理

- **单个链接采集失败**：不影响其他链接，记录失败列表，最后单独重试。
- **单个文档图片插入部分失败**：记录失败的图片序号，最后统一用长间隔（5秒）重试。
- **API 限流（批量 invalid_ 错误）**：立即停止所有并发，等待 30 秒后从断点续跑，并发降为 1。
- **中间结果持久化**：每个链接的采集数据、图片URL列表、Markdown都保存到本地文件，任何阶段失败都可以从断点续跑，不需要重新采集。

### 批量预估时间参考

| 文档数 | 每文档图片数 | 预估总时间 |
|--------|-------------|-----------|
| 2 | 50-150 | 10-15 分钟 |
| 5 | 50-150 | 25-40 分钟 |
| 10 | 50-150 | 50-80 分钟 |

主要时间花在图片插入（API 密集），采集和清洗很快。建议 5 个以上链接时告知用户预估时间。
