# 转录规范与命令参考（transcription-guide）

本文件是 course-images-to-feishu 的细则，供转录与入库时参考。

## 一、XML 草稿结构

飞书文档 XML 草稿支持以下标签（按序使用）：

```xml
<title>子文档标题</title>
<h1>截图编号（如 截图01 为啥要学AI场景）</h1>
<h2>课件内板块（如 快速认识、互动、案例、敲黑板说重点）</h2>
<p>段落文本。忠实原文，保留口语化表达。</p>
<ul><li>无序列表项</li></ul>
<ol><li>有序列表项（自动编号，可省略 seq 属性）</li></ol>
<table>
  <thead><tr><th>表头1</th><th>表头2</th></tr></thead>
  <tbody><tr><td>单元格</td><td>单元格</td></tr></tbody>
</table>
<pre lang="bash"><code>代码块 / 提示词原文</code></pre>
<blockquote><p>引用</p></blockquote>
```

规则：
- `title` 必须且只能出现一次，在文件最顶部。
- `h1` 用于截图编号（截图01、截图02…），按读取顺序；`h2` 用于每张图内部的板块小节。
- 图片内的标题行转 `h1`/`h2`；正文内的加粗、原列表层级（ul 嵌套 ul）按原样保留。
- 界面截图用 `（界面：核心信息）` 一句话括注，不逐字转录 UI 文字。
- 数学公式/特殊符号按文本描述或原文录入；无法识别的 OCR 乱码修正后不加标注，明显的断行错误按语义合并。

## 二、拆分与命名

- 按课程叙事阶段拆 3-6 篇，示例：`01 开篇+预热（截图01-05）`、`02 框架（截图06-08）`、`03 个人篇（截图09-11）`、`04 组织篇（截图12-13）`、`05 总结（截图14）`。
- 父节点：`0X 课程名-截图笔记`，编号顺延；创建前先查根节点确认最新编号。

## 三、lark-cli 命令清单（全部加代理前缀）

```bash
export PREFIX="env -u http_proxy -u https_proxy -u HTTP_PROXY -u HTTPS_PROXY"

# 查知识库根节点（确认父节点编号）
$PREFIX lark-cli wiki +node-list --space-id 7669431379494440158 --as user --format json

# 建父节点
$PREFIX lark-cli wiki +node-create --space-id 7669431379494440158 --obj-type docx --title "08 XX-截图笔记" --as user --format json

# 初始化文档草稿
$PREFIX lark-cli docs +script --command init-draft --presentation-decision '{"presentation_mode":"normal"}' --format json

# 解析校验草稿（status 必须为 passed）
$PREFIX lark-cli docs +script --command parse --content "@./draft.xml" --format json

# 创建并直挂父节点
$PREFIX lark-cli docs +create --doc-format xml --content "@./draft.xml" --parent-token <父节点node_token> --format json

# 校验挂载
$PREFIX lark-cli wiki +node-list --space-id 7669431379494440158 --parent-node-token <父节点> --as user --format json

# 回读抽查
$PREFIX lark-cli docs +fetch --doc <document_id> --format json
```

## 四、踩坑速查

| 坑 | 解法 |
|---|---|
| lark-cli 连接被拒 | 所有命令加 `env -u http_proxy -u https_proxy -u HTTP_PROXY -u HTTPS_PROXY` 前缀 |
| 长图直接 Read 漏读/截断 | 先跑 `scripts/split_long_images.py` 分段，按分段清单逐段读 |
| 图片命名非纯数字 | 按文件名自然排序（01、02…）读取，不按系统随机顺序 |
| 文档类型选错 | 一律 `docs +create`（docx）；不要用 file/md 导入（无法 docs +fetch 回读） |
| 父节点编号冲突 | 创建前先 `wiki +node-list` 查根节点，取最新编号 +1 |
| 中间产物丢失 | /tmp 会被系统清理，分段/草稿丢失不影响飞书端产物，可重建 |
| parse 校验失败 | 检查 XML 标签闭合、title 唯一、h1/h2 层级是否合理，修正后重跑 |
| 子文档拆分过细/过粗 | 按 3-6 篇、单篇 3000-12000 字校准 |
