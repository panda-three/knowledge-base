---
name: course-doc-to-local
description: 将「一堂创业课」（yitang.top/fs-doc/）等课程文档链接**完整转录为本地 Markdown**：全部图片下载到本地（相对路径引用，永久有效）、标题层级/加粗/引用/有序列表/代码块格式完整还原，按"总览+逐案例/章节"自动拆分为多篇，默认沉淀到 `/Users/panda/Desktop/knowledge-base/05-收件箱/<飞书文档标题>/`（交付目录仅 md + imgs/，不保留中间元数据）。当用户给出 yitang.top/fs-doc 链接并要求提取/转录/沉淀到本地（不进入飞书知识库、嫌飞书慢）时使用；支持单链接或批量多链接。与 course-doc-to-feishu 的分工：本技能输出本地 MD+图片（主路径，快、永久可控）；course-doc-to-feishu 输出飞书在线文档（按需才用，受逐张导入限流）。
---

# course-doc-to-local

课程文档链接 → **完整本地转录**（图片本地化 + 格式还原 + 拆分多篇）。

## 与 course-doc-to-feishu 的边界（先分清，避免方向性错误）

| 维度 | 本技能 course-doc-to-local | course-doc-to-feishu |
|---|---|---|
| 输出 | 本地目录：N 篇 .md + imgs/ 全部原图（相对路径） | 飞书在线文档（wiki 链接） |
| 图片 | 下载到本地，**永久有效** | 飞书导入（受逐张导入限流，慢） |
| 速度 | 分钟级（图片并行下载） | 小时级（523 张约 2-3 小时） |
| 格式 | 忠实原文（标题/加粗/引用/列表/代码块） | 同左 + 飞书兼容预处理（零宽/空格） |

**铁律：本地版不做飞书加粗兼容预处理**（开标签插零宽、闭标签插空格只用于飞书 markdown 导入，本地版会污染原文产生多余空格）。

## 前置环境（实测坑，必读）

- 本机代理 `http_proxy=http://127.0.0.1:7890` **不可用**（curl 000 / Errno 61）：
  - 下载图片：Python 用 `urllib.request.build_opener(urllib.request.ProxyHandler({}))` 直连
  - lark-cli（本技能一般不用）：需 `env -u http_proxy -u https_proxy -u HTTP_PROXY -u HTTPS_PROXY` 前缀
- 浏览器操作走 `mac_computer_use_tool`（plane="bu"，seed_browser_use）。先读 `browser-use-automation-mac` 技能。
- yitang 页面**无登录墙**（本项目源文档无需登录；若遇登录页调用 `interaction.request_action(browserControl)`）。
- 目标输出目录（默认）：`/Users/panda/Desktop/knowledge-base/05-收件箱/<飞书文档标题>/`（标题取页面 title，如「26 秋马：AI 十倍速成长 2/2」；用户另行指定目录时按用户指定）。**交付目录只含 N 篇 md + imgs/，不保留任何中间元数据**（datajson / imgs json / plan / 脚本副本一律不落盘到交付目录）。

## 工作流

### 1. 打开链接
`bu.navigate(url)` + `bu.wait_for_load()`。若跳登录 → `interaction.request_action(browserControl)` 请用户接管。
- 用 `bu.page_info()['title']` 取飞书文档标题 → 作为输出文件夹名 `<飞书文档标题>/`（用户另有指定时除外）。

### 2. dataJson 全量采集（核心，一次导出，零漏采零错位）

**不要用 DOM 滚动采集**（虚拟列表 DOM 节点复用会导致漏块/错位——历史"案例位置错乱"事故根因）。直接从页面 Vue 组件读取渲染数据源：

```javascript
(() => {
  const app = document.querySelector('#app');
  let vm = null; const seen = new Set();
  const walk = (el) => {
    if (!el || seen.has(el) || vm) return;
    seen.add(el);
    if (el.__vue__ && el.__vue__.$data && el.__vue__.$data.dataJson) { vm = el.__vue__; return; }
    for (const c of el.children || []) walk(c);
  };
  walk(app);
  const dj = vm.$data.dataJson;
  const out = [];
  const wb = (b) => {
    out.push({ t: Number(b.type), a: b.blockAttr, c: (b.childrens || []).length });
    (b.childrens || []).forEach(wb);
  };
  (dj.childrens || []).forEach(wb);
  window.__full = out;
  return JSON.stringify({ total: out.length });
})()
```

- `window.__full` 分批取回（每批 300 条，防返回截断）：`bu.js("JSON.stringify(window.__full.slice(a,b))")`，合并存 `course_<短名>_datajson.json`。
- 图片 URL 从 `vm.$data.previewSrcList` 取（顺序与 dataJson 图片块一致）→ `course_<短名>_imgs.json`。
- DFS 展平顺序 = 页面渲染顺序；`c` 为 childrens 数，容器子块紧跟其后。
- **中间文件存放**：以上中间文件（datajson / imgs / plan / md_url 等）一律写入系统临时目录（如 `$TMPDIR/course_<短名>/`），**不进入交付目录**；任务全部完成并验证通过后清理临时目录。用户明确不需要中间元数据，除非用户要求保留。

### 3. 结构识别与拆分（总览 + 逐案例/章节）

- 从 dataJson 提取全部标题块（t=3 h1 / t=4 h2 / t=5 h3）的 index 与文本 → 还原文档大纲。
- 默认切分规则：**总览（开篇/方法）+ 每个案例/章节各一篇**，切点 = 标题块在 dataJson 的原始 index。
- 生成拆分明细（每篇：名称、起止 index、含图数），**先给用户确认或按用户指示调整**；图片按"每篇含图数合计 == 总图数"校验全覆盖。

### 4. 生成 Markdown（格式还原）

用 `scripts/gen_split.py`（参数：datajson.json + 拆分方案）。**类型映射（实测确认）**：

| t | 含义 | 处理 |
|---|---|---|
| 2 | 文本 | 原样；`text.elements[].text_run.content`，bold/background_color 转 `**`（相邻同状态 run 合并） |
| 3/4/5 | h1/h2/h3 | `## / ### / #### ` + 文本 |
| 12 | bullet | `- ` |
| 13 | ordered | 按 `ordered.style.sequence` 编号（'1' 开新组、'auto' 续号） |
| **14** | **code 代码块** | **```` ``` ```` 包裹；内容在 `a.code.elements`（不在 a.text！漏了会丢提示词/代码）** |
| 19/24/25/33 | callout/grid/grid_column/view 容器 | 跳过容器，子块按顺序输出 |
| 22 | 分割线 | `---` |
| 23 | file | `📹 名称` |
| 27 | image | `![](url)` 独立成块（前后空行） |
| 34 | quote_container | 子块加 `> ` 前缀（嵌套累加） |

### 5. 图片本地化（并行下载 + 相对路径）

- `scripts/download_imgs.py`：从 imgs.json 并行下载全部图片到 `<输出>/imgs/`，命名 `pNN_MMM.ext`（NN=篇号，MMM=篇内序号），**禁用代理直连 + 重试 3 次 + 校验非空**。
- `scripts/localize.py`：把 MD 中 `![](url)` 按出现顺序替换为 `![](imgs/pNN_MMM.ext)`（相对路径）。
- **图片按位置保留，禁止按 URL 去重**（同 URL 复用多处时必须保留第 N 个位置）。

### 6. 验证（硬门槛，不通过禁止交付）

`scripts/verify.py` 执行：
- **文本流 diff**：从 dataJson 重建权威文本流（所有块类型的文本；列表去编号、去 `**`、去 `>`、图片→`[IMG]`），与生成 MD 提取的文本流对比 → **相似度必须 = 1.0**（逐篇）
- **图片数** = dataJson 图片块数（t=27 计数），本地文件全部存在
- **无 CDN 残留**：grep `cdn.yitang.top` 应为 0
- 加粗 `**` 数量为偶数

### 7. 交付

- 交付目录：`/Users/panda/Desktop/knowledge-base/05-收件箱/<飞书文档标题>/`（N 篇 md + imgs/），用 `present_files` 交付 md 文件，说明图片在同目录 `imgs/`。
- 交付目录只含 md + imgs/：中间元数据（datajson / imgs json / plan / 脚本副本）用完即清理，不留存。
- 用户另行指定输出目录时按用户指定；用户要求不进收件箱时（如仅临时转录）可输出到临时目录。

## 踩坑速查

| 坑 | 解法 |
|---|---|
| 下载 Errno 61 / 000 | 本机 7890 代理不可用；Python `ProxyHandler({})` 直连；lark-cli 加 `env -u http_proxy...` |
| DOM 滚动采集漏块/错位 | 用 dataJson 一次全量导出（第 2 步） |
| t=14 被当 h3 | **t=14 是 code 代码块**（内容在 a.code.elements），t=5 才是 h3 |
| 提示词/代码块内容丢失 | code 块必须从 `a.code.elements` 提取，不在 `a.text` |
| 本地版加粗出现多余空格/零宽 | 本地版**不要**做飞书兼容预处理（零宽/空格只为飞书导入设计） |
| 图片按 URL 去重漏图 | 按位置逐个保留（同一 URL 复用多处） |
| 图片与文本同块（飞书导入场景） | 本技能本地输出无此问题；若转飞书走 course-doc-to-feishu |
| 虚拟列表滚动不更新 | 不用滚动采集，直接读 dataJson |
| 有序列表编号错乱 | sequence='auto' 组内续号，数字='1' 开新组 |
| 引用内容混入正文 | t=34 子块加 `> ` 前缀 |
| 文本以 `#` 开头被误判标题 | verify.py md_flow 标题正则须为 `^(#{1,6})\s+`（# 后必须有空格；gen_split 生成的标题都带空格，正文标签如 `#个人成长` 不带空格，P3 实测踩坑，本地副本已修正） |

## 批量处理（多链接）

- 登录态共享：一次登录，后续链接 `bu.new_tab(url)` + `bu.switch_tab()` 逐个采集（采集串行）。
- 每链接独立保存中间文件到临时目录（datajson/imgs/md），各阶段失败可断点续跑；全部完成并验证后清理临时目录。
- 每链接独立输出到 `05-收件箱/<各自飞书文档标题>/`，不混放。
- 图片下载可多链接并行（本地无 API 限流问题）。

## 参考实现

- P1《26 秋马：AI 十倍速成长 1/2》完整链路（3567 块 / 523 图 / 13 篇 / 全部验证通过）：`/Users/panda/DoubaoWork/chats/2026-09-17/new-chat/course_p1_local/`
- P2《26 秋马：AI 十倍速成长 2/2》（2889 块 / 353 图 / 13 篇 / 全部验证通过，新规范首例）：`/Users/panda/Desktop/knowledge-base/05-收件箱/26 秋马：AI 十倍速成长 2/2/`（交付目录仅 md + imgs/，中间元数据已清理）
- 验证脚本注意：verify.py 权威文本流需补 t=22 分割线（`---`），否则含分割线的篇会误报文本流不一致（P2 实测踩坑，本地副本已修正）。
