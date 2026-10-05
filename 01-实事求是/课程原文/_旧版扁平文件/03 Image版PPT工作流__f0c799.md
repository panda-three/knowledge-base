---
obj_token: OReld8OmJoSYFTxDLm5cuA8NnEf
title: 03 Image版PPT工作流（截图04-06）
feishu_path: 14 AI制作ppt-截图笔记/03 Image版PPT工作流（截图04-06）
obj_type: docx
fetch_method: docx
source: 一堂创业课
---

<title>03 Image版PPT工作流（截图04-06）</title>

> 部分内容由豆包生成

# 截图04 Image 版 PPT 开篇与前三步

## Image 版 PPT：把课件变成视觉页面

- 用 Codex 调用 GPT Image 2 做 PPT，核心不是为了取代传统 PowerPoint，也不是为了把所有页面都变成不可编辑的图片。它真正解决的问题，是把「做 PPT 初稿」从手工排版，变成一条可以被拆解、批量执行、集中验收、持续沉淀的流程。
- GPT Image PPT 的本质：不是让 AI 一次替你完成所有判断，而是让 Codex 把「资料读取、页面规划、提示词组织、批量生图、版本管理、导出交付」这些重复动作标准化，创建专属 Skill。

### Image 版 PPT 优势（4 个）

| 优势 | 说明 |
|-|-|
| 视觉质感更强 | 可直接生成接近海报、发布会、信息图风格的 PPT 页面 |
| 复杂内容更好图像化 | 适合把流程、方法论、系统结构、对比关系做成视觉图解 |
| 批量生成效率高 | Codex 整理好内容与规则后，可批量调用 GPT Image 出图 |
| 适合个人 IP 内容 | 可融入 Q 版人物、课程主题、金句、书籍封面等个人品牌元素 |

### HTML PPT 与 Image PPT 的差异

| 对比项 | HTML 版 PPT | Image 版 PPT |
|-|-|-|
| 核心产物 | index.html + assets，可浏览可调试 | 01.png、02.png 等页面图片 |
| 优势 | 结构可控、可交互、适合调试与演示 | 视觉质感强、风格变化快、适合海报级页面 |
| 修改方式 | 改 HTML/CSS/JS 或用浏览器批注辅助 | 小改局部文字，大改重新生成该页 |
| 适合内容 | 课程型、方法论、网页演示、动态图表 | 视觉强、封面、流程图、对比图、金句页 |
| 风险 | 代码、尺寸、导出、浏览器兼容 | 图片文字可能错、编辑性有限 |

## 第一步：项目目录：把上下文放进文件夹

建议先建立一个项目文件夹，把原稿、图片、logo、参考图、规则文件、输出结果全部放进去。这样 Codex 才能从同一套资料中读取上下文，后续也方便复盘。补充说明：这方案也可以适用在 HTML PPT 中。

### 项目目录范例

```bash
HTML_Project/
├── 素材/                # 原始资料: Word、Markdown、PPT、PDF、Excel
│   ├── 视觉素材/         # (可选项) logo、人物图、产品图、截图、参考风格图
├── 需求/                # asset_inventory.md、ascii_content_layout.md、visual_style_guide.md
├── 模板/                # (可选项) 提示词模板、PPT 模版
│   ├── 风格样板图/       # 暂存 Product Design 生成风格样板图
│   ├── 输出图片/         # Codex 调用 Image Gen 生成的图片
│   ├── 输出 ChatGPT 图片/ # ChatGPT 生成的图片
├── 输出 PPT/             # (可选项) PPT / PDF 输出
└── .agents/skills        # (可选项) 项目专属 Skill
```

目录命名建议：对顺序有要求可在最前面追加数字 01、02、03；没有视觉素材或只有一个 Logo，都可以统一留一个素材目录。

## 第二步：让 Codex 盘点资料

这跟前面 HTML 版 PPT 操作流程相同。如果你 HTML 版 PPT 也在相关目录下且之前有运行过 guizang-ppt-skill，有一定几率会触发，建议追加"不使用 guizang-ppt-skill"的条件，反之无需补上。资料盘点 asset_inventory.md：资料量少时可以不需要，资料多时可统一记录，并可规定要显示哪些资料。

```bash
请先分析此目录 GPT Image PPT 的所有资料，目标是产生 10 页 Image PPT，
每份 Word 严格对应 1-2 页 Image PPT，预计调用内建 Image Gen Skill 生图

# 输出
- 新增一份 asset_inventory.md，放在 F:\一堂 AI Live\PPT 内容\GPT Image PPT\需求 的目录下

# 限制条件
- 不使用 guizang-ppt-skill
- 不要生成图片，也不要修改原始文件
- 如果发现缺少关键素材，请在最后列出"待补充清单"
- 请不要编造没有提供的数据与内容
```

（界面：执行结果——已盘点全部 7 份 Word，每份 Word 对应 1-2 页；已列明 Image Gen 使用策略及待补充清单；未生成图片、未修改原始 Word；未使用 guizang-ppt-skill。）

### asset_inventory.md 要点

任务边界：基于素材中 7 份 Word 制作 10 页 Image PPT，每份 Word 严格对应 1-2 页；本轮仅做素材分析，不生成图片、不制作 PPT、不修改 Word；不使用 guizang-ppt-skill；内容只取自现有 Word，价格优惠版本数量平台状态等均视为源文档陈述，未做外部核验，正式出稿前应人工确认；各 Word 后半段重复的自我介绍/课程清单/书籍预售/一堂经历等不纳入主体。

目录与素材：素材\Claude Code\ 1 份；素材\OpenClaw\ 6 份；共 153 个媒体文件，核心教程部分关联 120 张图片。素材质量：操作类截图充足且多有红框箭头标注，可作事实依据或局部裁切；局限是尺寸明暗不统一、部分文字密集，直接整图放入 16:9 会难读；风险是可能含账号头像、实例名、IP、App Secret、Token、API Key 等敏感信息，正式使用前必须逐张遮蔽；原则是涉及 UI、配置字段、价格、具体数值时优先复用真实截图，不让 Image Gen 重画界面或生成可读配置文字。

Word 逐份盘点：A Claude Code 国内安装与环境配置（40 图，2 页）；B 阿里云低成本尝鲜（16 图，1 页）；C 集成飞书（33 图，2 页）；D 入门应用方向选择（0 图，1 页）；E 数字员工关键文件（0 图，2 页）；F 数字员工隐私保密能力（25 图，1 页）；G 挑选 ClawHub Skills（6 图，1 页）。10 页严格映射：1=A-1/2、2=A-2/2、3=B-1/1、4=C-1/2、5=C-2/2、6=D-1/1、7=E-1/2、8=E-2/2、9=F-1/1、10=G-1/1。

后续 Image Gen 素材策略：建议生成 4 类无文字概念视觉（第 6 页三入口汇聚工作台、第 7 页项目管理数字员工协作、第 8 页身份价值观用户三层结构、第 9 页资料分级审计公私隔离三层防护）；统一约束：16:9 横向、主体不贴边留安全区、不要求可读中文/代码/价格/平台按钮/产品 UI、不生成品牌 Logo、不增加人物身份客户案例效果数据；若需品牌或界面证据，用 Word 真实截图裁切遮蔽而非让模型重画。可直接复用：安装验证截图、CC Switch/智谱/Kimi 配置入口（需复核版本与敏感字段）、阿里云套餐服务器部署图（价格标注待核验）、飞书开放平台创建应用权限长连接事件订阅版本发布截图、ClawHub Security Scan 作者页下载量星标截图。不建议直接复用：后半段自我介绍课程宣传图、过长权限 JSON/settings.json 整页截图、未遮蔽的 App Secret/Token/API Key/IP/头像/实例标识截图、未人工确认的时效性价格优惠版本数量。待补充清单：统一视觉方向、正式标题副标题署名及 Logo、第 6-8 页正文视觉素材、所有拟用截图脱敏标准、时效性信息人工确认结果、第三方 Logo 与真实界面截图是否允许、最终交付格式。

# 截图05 Product Design 做风格设计

## 第三步：用 Product Design 做风格设计

Codex 的 Product Design 插件，可以用来先探索视觉方向、封面风格、关键页样式，帮助你决定这套 PPT 应该走哪种视觉路线。

### Step 1：Product Design 设计 ASCII 内容线框

- 使用 ASCII 内容线框的好处是，预先知道文字排版的大致位置，到时候追加风格之后心理也有一个底。
- 如果 ASCII 内有说要 [真实截图]，可以考虑追加限制条件排除真实截图，不然就需要模型提高或后置处理，这会提高后来调整图片难度。

```bash
@Product Design 根据 asset_inventory.md，帮我产生 ASCII 内容排版的 10 页 Image PPT 内容

# 输出
- 新增一份 ascii_content_layout.md，放在 F:\一堂 AI Live\Image PPT Demo\需求 的目录下
```

（界面：执行结果——设计简报回放：10 页 16:9 静态 Image PPT 内容线框，严格沿用现有页码映射不新增事实，每页含标题、核心文案、ASCII 区块、素材位置与来源；建议采用「杂志式图文叙事」：截图页强调证据，概念页突出主视觉，整体比纯卡片网格更有节奏；备选统一卡片网格或全流程图风格。用户确认"采用「杂志式图文叙事」"。已完成 10 页杂志式 ASCII 内容排版，校验页数、Word 映射、素材槽位与敏感信息提示，下一步可据此编写逐页 Image Gen 提示词。）

ascii_content_layout.md 要点：每页统一结构——主标题（每页只表达一个结论，1-2 行）、导语（一句话交代为什么看这一页）、主视觉/真实截图证据/结构化内容、页底结论（一句可带走的话）、来源（对应 Word）。示例第 2 页：眉题 CLAUDE CODE / 两种接法；主标题"多供应商切换，还是直接接入国内模型？"；路径 A CC Switch 适合多供应商统一切换；路径 B 国内模型厂商（智谱 GLM / Kimi K2.5）；共同配置 ANTHROPIC_BASE_URL + ANTHROPIC_AUTH_TOKEN；可选参数超时/非核心通信/Git 署名/默认语言；页底"选择路径不等于锁死模型；版本与优惠均需发布前核验"；素材说明左右各选一张代表性截图裁切到配置动作，不展示完整密钥，API Key/Token/个人账号信息必须遮蔽。

## Step 2：Product Design 风格设计

提示词可根据自己要求调整，比如追加限制或放 Logo。用 @ 可以指定档名，如有重名请确认来源是哪个目录位置。

```bash
@product-design 帮我设计 3 套风格方案，同时分别生成 3 张独立的 16:9 风格样板图让我参考，
根据 @asset_inventory.md 与 @ascii_content_layout.md 内容，
用来制作 Image PPT，同时之后采用内建 Image Gen Skill 生图

# 注意
- 文字部分不要被风格遮蔽到

# 输出
- 生成风格样板图，放在 F:\一堂 AI Live\Image PPT Demo\风格样板图 的目录下
```

（界面：执行结果——3 张 16:9 风格样板图：1.杂志式证据页；2.深色命令中心；3.玻璃低感教学页。校验：三张均 16:9，实际 1672×941，已保留文字安全区，原始 Word 与两份 md 未修改。我个人推荐第 1 套作为主风格：最适合"真实截图证据 + 教程讲解"的 Image PPT，你要继续选 1/2/3 其中一套，我就可以按该风格推进正式 10 页视觉生成。）

重新刷 Product Design 风格设计提示词，再追加额外新的 3 套风格方案：

```bash
再追加额外新的 3 套风格方案，依然使用 @Product Design
```

（界面：新增 3 张：4.Swiss Technical Blueprint；5.Warm Notebook Lab；6.Neon Ink Editorial。快速判断：第 4 套最合适课程教程和流程页；第 5 套最有人味适合教学感；第 6 套最有视觉冲击，但正式做 10 页时要克制霓虹装饰避免抢文字。你可以从 1-6 里选一套作为主风格，我再继续推进正式 10 页 Image PPT。）

## Step 3：生成视觉风格文件 visual_style_guide.md

挑选一张适合的风格样板图，把视觉风格存下来，后续提供参考资料使用。提示词需把风格样板图当做附件搭配使用；visual_style_guide.md 会包含色彩、字体、排版等，有需要可迭代优化。Tips：可直接拖拉图片到对话框中自动变成附件。

```bash
帮我把附件的这一个设计规范写入 visual_style_guide.md，放在 F:\一堂 AI Live\Image PPT Demo\需求 的目录下
```

（界面：执行结果——内容已根据附件 Swiss Technical Blueprint 风格整理成设计规范，包含风格定位、16:9 画布与网格、色彩、字体、版式组件、截图与 Image Gen 使用规则、10 页应用建议、禁止项与质量检查清单。校验：文件约 288 行；没有改动 asset_inventory.md 与 ascii_content_layout.md。）

visual_style_guide.md 要点：风格定位为 Swiss grid 瑞士网格 / Technical blueprint 技术蓝图 / Evidence-first 证据优先 / Clean instructional layout 清晰教学版式 / Screenshot-friendly 适合承载真实截图，整体气质"干净、理性、精确、可信"，像高级系统架构课程视觉资料而非营销海报。使用边界：16:9 横向；正文信息只来自两份 md 不新增事实；涉及 UI/配置/价格/版本/平台状态优先用 Word 真实截图，不得用 Image Gen 重画可读 UI；Image Gen 仅用于无文字概念背景、抽象结构、流程氛围；图片内不得生成可读中文英文代码价格 Logo 产品名按钮配置字段；正式文字数字文件名代码由 PPT 后期叠加。画布网格：16:9，设计基准 1920×1080，安全区四边至少 64px，正文不低于 960px；12 或 16 栏模块化网格，分割线细轻克制，元素沿网格对齐；可用淡蓝网格底纹但透明度低不影响正文。色彩：背景白 #F7F9FC；主深蓝 #001B3F/#002B5C；蓝色强调 #0057FF/#1E6BFF；浅蓝辅助 #DCEBFF/#EEF5FF；中性灰 #B8C0CC/#D8DDE5；警示红 #E6262E 每页最多 1-2 小面积点缀；页面 70% 以上浅色留白，深蓝不铺满。字体：中文思源黑体/Noto Sans CJK/微软雅黑，英文代码 Inter/IBM Plex Sans/JetBrains Mono；页眉 24-30px、主标题 64-88px、副标题 30-38px、正文 28-34px、标签 20-24px、代码 26-32px；文字必须放在纯白浅灰深蓝纯色区，不叠复杂结构图截图发光线条，长句拆短行每行不超 22 中文字。版式组件：顶部标尺 40-60px 细线刻度小蓝条工程制图感；深色标题块用于首页章节页问题页关键结论；中性界面轮廓只放抽象灰条或后期准确文字，不生成真实按钮菜单输入框；步骤圆点用 1/2/3/4 蓝色，未处理用浅灰，风险待核验用少量红，无源数据不伪造统计图表。

# 截图06 Image Gen 生成图片与 ChatGPT 网页替代

## 第四步：用 Image Gen 生成图片

- 使用 Codex 内建的 Image Gen Skill 来生图，正式批量生图前建议先生成 1-2 页样张，目的是确认风格、字体、logo、页面密度和中文文字质量。不要一开始就让 Codex 一次生成全部内容，否则方向错了会浪费 Codex 额度得更快。
- 如果怕大量图片导致额度不足，可以考虑 ChatGPT 网页上生成。

```bash
@imagegen 请根据 asset_inventory.md ascii_content_layout.md visual_style_guide.md，
先产生 1 ~ 2 页 PPT 图片

# 要求：
1. 输出 16:9 PPT 页面图片
2. 文件命名为 01.png、02.png
3. 保存到 F:\一堂 AI Live\Image PPT Demo\输出图片
4. 如果某页文字过多，优先做信息层级压缩，不要缩到不可读
```

（界面：执行结果——已处理 22m44s，生成前 2 页；校验：两张均 1920×1080、16:9、文件名 01.png/02.png、文字已层级压缩未缩到不可读、原始 Word 与三份需求文档未修改。我没有让 Image Gen 直接生成整页中文，因为中文与代码容易失真；这两页采用 Swiss Technical Blueprint 风格做确定性排版，并嵌入/裁切 Word 内真实截图。）

### 问题与解决方案

可以发现如果是放 Word 中截图中的图片，容易图片破损或盖到图片。

- 方案一：调整 ascii_content_layout.md，放弃关于截图内容，重新生成无截图内容的 ascii_content_layout.md。
- 方案二：推理模型调到 高 或 超高，缺点加速额度消耗。个人经验：plus 会员每次都把推理模型调到高，当下只要 2 天就会把一周的额度耗完。
- 方案三：使用 ChatGPT 网页上生成图片且智能（推理）设置 高级。
- 方案四：每张截图都需要后置处理，然而 Image PPT 就是为了快速出图，因此这方案 ROI 偏低。

## 替代方案：直接在 ChatGPT 网页上生成图片

优点：不占用 Codex 的额度；个人实测 ChatGPT 网页生图效率比 Codex 在批量生图速度快；当 Codex 本地网络不佳时也可快速替代；支持线上改图。

缺点：需要上传相关文件到 ChatGPT 项目中当做来源；还需要下载生成图片到本地对应目录；本地资料有更新可能忘记手动上传做更新；如果要提炼成专属 Skill 将会缺少生图这部分的提炼。

注意事项：项目的来源数量有文件上限，根据 GPT 账号等级：Free 5；Go、Plus 25；Edu、Pro、Business、Enterprise 40。

### Step 1：创建项目

（界面：ChatGPT 左侧栏 → 项目 → + → 创建项目，项目名称"Image PPT Demo"）

### Step 2：上传相关设计文件

项目 → 来源 → 上传文件：需求目录（必须）asset_inventory.md、ascii_content_layout.md、visual_style_guide.md；素材资料（可选）如需要上传相关资料素材。

（界面：Image PPT Demo 项目来源标签页上传 9 份文件：三份 md 及 6 份 Word 素材）

### Step 3：生成样张

这边建议将 智能（推理）设置 高级。对话框 + → 创建图片 可视化呈现任何内容。文件命名为 01.png、02.png、03.png 在 ChatGPT 上没效果。

```bash
@创建图片 根据来源的三个 .md 资料，先产生 1 ~ 3 页 PPT 图片

# 要求：
1. 输出 16:9 PPT 页面图片
2. 文件命名为 01.png、02.png、03.png
3. 如果某页文字过多，优先做信息层级压缩，不要缩到不可读
4. 截图内容可以参考对应来源的 word 内容
```

（界面：执行结果——在 ChatGPT 生 3 张图只要花 6 分钟；反观透过 Codex 调用 Image Gen 只有 2 张图就花 22 分钟；对比图的效果来说 ChatGPT 生图效果还比 Codex 调用 Image Gen Skill 好。ChatGPT 生图：高级（推理）；Codex：中（推理）。Thought for 6m 3s。产物 01/02/03 三张瑞士技术蓝图风格页面。）

## 第五步：批量生成 Image PPT

后续生图我将改到 ChatGPT 网页上生成图片来处理。如果是调整 ascii_content_layout.md 也可以考虑全部图片生成在 ChatGPT 网页上，处理效率上还是可以。

```bash
继续，根据来源的三个 .md 资料，产生 4 ~ 10 页 PPT 图片

# 要求：
1. 输出 16:9 PPT 页面图片
2. 如果某页文字过多，优先做信息层级压缩，不要缩到不可读
3. 截图内容可以参考对应来源的 word 内容
```

（界面：执行结果——生 7 张图也只花 8 分钟，这效率上是比 Codex 中透过 Image Gen 的 2 张图花费 22 分钟高出太多。Thought for 8m 6s。产物 04-10：先建飞书应用再把权限一次配齐；把消息通道接上再完成发布与测试；别从"能做什么"开始从每天重复的事开始；数字员工要主动工作先写清"怎么运行"；数字员工是谁相信什么服务谁；真正的保密不只是一条"不要泄露"；下载之前先做六次检查。）

Codex 批量生图提示词（这边就没有执行，主要是效率出图效率低）：

```bash
@imagegen 继续，根据 asset_inventory.md ascii_content_layout.md visual_style_guide.md，产生

# 要求：
1. 输出 16:9 PPT 页面图片
2. 文件命名为 03.png、04.png ... 10.png
3. 保存到 F:\一堂 AI Live\Image PPT Demo\输出图片
4. 如果某页文字过多，优先做信息层级压缩，不要缩到不可读
```