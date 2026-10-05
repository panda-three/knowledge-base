---
name: course-images-to-feishu
description: 将本地课程截图文件夹（用户给本地路径或上传文件夹）逐张 OCR 转录为最佳效果纯文字，结构化拆分为多篇后存入飞书「AI教育课」知识库（space_id=7669431379494440158）的「0X 课程名-截图笔记」父节点下。当用户给出图片文件夹路径/上传文件夹并要求转文字、转录、识别、存入知识库时使用。全程纯文字（不保留图片），交付 wiki/docx 链接。
---

# course-images-to-feishu

把本地课程截图文件夹 → 纯文字转录 → 结构化存入飞书「AI教育课」知识库。

与 `course-doc-to-feishu`（网页链接场景）互补：本技能只处理**本地图片文件夹**。

## 前置环境（必读）

- `lark-cli` 可用；**本机代理坑**：所有 lark-cli 命令必须加前缀 `env -u http_proxy -u https_proxy -u HTTP_PROXY -u HTTPS_PROXY`，否则连接被拒。
- 目标知识库：AI教育课，`space_id = 7669431379494440158`。
- 工作目录：临时目录（如 /tmp/xxx）会被系统清理，中间产物（分段图、草稿 XML）可重建，不影响飞书端产物。

## 工作流（按序执行）

### 第 0 步 · 预检文件夹
- 拿到用户给的文件夹路径（或上传的文件夹）后，列出全部文件：确认格式（png/jpg/webp…）、按文件名数字顺序排序（01、02…）、检查是否混入非截图文件。
- 确认知识库父节点编号：父节点按「0X 课程名-截图笔记」命名，编号顺延（当前到 07，下一篇为 08）。先 `wiki +node-list --space-id 7669431379494440158` 查根节点确认最新编号。

### 第 1 步 · 长图分段
- 逐张检查尺寸（PIL 读取）：高度 >4000px 的长图必须分段后再 Read，否则会漏读/截断。
- 跑分段脚本（放在本技能 scripts/ 下，勿在 /tmp 手写）：
  ```bash
  python3 <skill>/scripts/split_long_images.py "<文件夹路径>" --out <工作目录>/segments
  ```
- 脚本输出：短图原样复制、长图按 3800px 切段（`<名>_partNN.png`），并打印分段清单——按清单逐段读取，防漏读。

### 第 2 步 · 逐张读取转录
- 按文件名顺序逐张 Read（长图逐段读），每读完一张核对编号。
- 对每张图做**忠实转录**：标题、正文、列表、表格原文保留，不做概括改写；口语化表达与笔误保留原文，仅对明显 OCR 噪声（乱码、断行）修正。
- 界面截图（软件/网页 UI）不逐字转录，用一句话括注：`（界面：核心信息）`。

### 第 3 步 · 结构化转录
- 用 XML 草稿承载转录内容：`title`=子文档标题；`h1`=截图编号（截图01…）；`h2`=课件内板块（快速认识/互动/案例/敲黑板说重点 等）；段落、有序/无序列表、表格按原文转换。
- **纯文字，不插图片、不保留图片引用**（用户硬性偏好）。
- 详细 XML 结构与命令见 [references/transcription-guide.md](references/transcription-guide.md)。

### 第 4 步 · 拆分决策
- 按课程叙事阶段拆 **3-6 篇**（开篇/框架/个人篇/组织篇/总结 等），单篇 3000-12000 字；避免过碎（如 9 篇）或过粗（如单篇 2.7 万字）。
- 每篇一个独立 XML 草稿，子文档命名：`0N 内容主题（截图a-b）`（不带 .md 后缀）。

### 第 5 步 · 创建父节点
```bash
env -u http_proxy -u https_proxy -u HTTP_PROXY -u HTTPS_PROXY \
  lark-cli wiki +node-create --space-id 7669431379494440158 \
  --obj-type docx --title "08 课程名-截图笔记" --as user --format json   # 得 node_token
```

### 第 6 步 · 创建子文档（每篇重复）
```bash
# 1) 初始化草稿（得 workspace 与 draft_path）
lark-cli docs +script --command init-draft --presentation-decision '{"presentation_mode":"normal"}' --format json
# 2) 写 draft.xml（用 Write 工具，内容见 transcription-guide）
# 3) 解析校验（必须 passed）
lark-cli docs +script --command parse --content "@./draft.xml" --format json
# 4) 创建并直挂父节点（勿用 wiki +move，直接 --parent-token）
lark-cli docs +create --doc-format xml --content "@./draft.xml" --parent-token <父节点node_token> --format json
```

### 第 7 步 · 校验（不可跳过）
- `wiki +node-list --space-id 7669431379494440158 --parent-node-token <父节点>` 确认全部子文档挂载、标题正确。
- `docs +fetch --doc <document_id>` 抽查 1-2 篇：核对标题、章节、列表、表格正常渲染。

### 第 8 步 · 交付
- 用 `present_files` 交付父节点 wiki 链接 + 各子文档 docx 链接。
- 交付后向用户说明拆分结果（几篇、各覆盖哪些截图）。

## 关键规则（从历史任务复盘固化）

| 规则 | 说明 |
|---|---|
| 纯文字 | 不插图、不保留图片引用（用户偏好，03 早期带图已纠正） |
| 命名 | 父节点「0X 课程名-截图笔记」；子文档「0N 主题（截图a-b）」；不带 .md |
| 拆分 | 3-6 篇/课程，单篇 3000-12000 字 |
| 文档类型 | 一律 docx（docs +create），勿用 file/md 导入（06 的 file 型无法回读校验） |
| 长图 | >4000px 必须分段读取，按脚本清单核对防漏 |
| 代理 | lark-cli 前 env -u http_proxy -u https_proxy -u HTTP_PROXY -u HTTPS_PROXY |

## Resources

- `scripts/split_long_images.py`：长图分段脚本（确定性逻辑脚本化，勿每次重写）。
- `references/transcription-guide.md`：XML 结构细则、lark-cli 命令清单、踩坑速查。
