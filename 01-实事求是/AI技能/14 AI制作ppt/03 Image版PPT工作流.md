---
type: 课程笔记
status: 未标注
date: 2026-09-16
updated: 2026-09-16
tags: [AI技能, AI做PPT, GPT Image, Image Gen, Product Design, 风格设计]
source: https://feishu.cn/docx/OReld8OmJoSYFTxDLm5cuA8NnEf（飞书 AI教育课 · 03 Image版PPT工作流）
related: [课程：HTML版PPT·01, 课程：PPT实战八步·02, 课程：PPT收尾总结·04]
---

# 课程：Image版PPT·03

**一句话结论：** Image PPT = 先盘点资料出三份需求文档（清单/ASCII 线框/视觉规范），再定风格样板，最后批量生图；**先出 1-2 页样张定方向，别一次跑全量**，批量生图可改用 ChatGPT 网页提效。

---

## 一、核心交付

- HTML vs Image 选型对比表。
- 一套项目目录骨架。
- 三份需求文档：asset_inventory / ascii_layout / visual_style_guide。
- 一个效率判断：批量生图用 ChatGPT 网页比 Codex 内建快得多。

## 二、HTML vs Image PPT

| 对比 | HTML 版 | Image 版 |
|---|---|---|
| 产物 | index.html+assets，可调试 | 01.png 等页面图片 |
| 优势 | 结构可控、可交互、可演示 | 视觉质感强、风格快、海报级 |
| 改法 | 改代码/浏览器批注 | 小改文字，大改重生成该页 |
| 适合 | 课程型/方法论/动态图表 | 封面/流程图/对比图/金句页 |
| 风险 | 尺寸/导出/兼容 | **图片文字易错、编辑性有限** |

## 三、五步工作流

| 步 | 动作 | 产出 |
|---|---|---|
| 1 | 建项目目录 | 素材/需求/模板/输出 分开放 |
| 2 | Codex 盘点资料 | asset_inventory.md |
| 3 | Product Design 做风格 | ASCII 线框 + 3 套风格样板 + visual_style_guide.md |
| 4 | 先出 1-2 页样张 | 确认风格/字体/logo/密度/中文质量 |
| 5 | 批量生成 4-10 页 | ChatGPT 网页生图 |

## 四、关键做法

### 4.1 项目目录

```
HTML_Project/
├── 素材/        # 原始资料 + 视觉素材
├── 需求/        # 三份 .md
├── 模板/        # 提示词模板、风格样板图、输出图片
├── 输出PPT/
└── .agents/skills
```

### 4.2 盘点资料（边界提示词）

- 每份 Word 严格对应 1-2 页；**不使用 guizang-ppt-skill**；不生图、不改原文、不编造数据。
- 敏感信息红线：账号/IP/App Secret/Token/API Key 正式用前**逐张遮蔽**。
- 原则：UI/配置/价格优先用真实截图裁切，**不让模型重画可读界面或代码**。

### 4.3 三份需求文档

| 文档 | 内容 |
|---|---|
| asset_inventory.md | 页映射、素材策略、待补充清单 |
| ascii_content_layout.md | 每页：标题（一结论）+导语+主视觉/证据+页底一句+来源 |
| visual_style_guide.md | 色彩/字体/网格/版式组件/禁止项/质检清单 |

> 风格用 Product Design 出 3+3 套样板图选一套；选好后把样板图当附件，让 AI 写成规范文件。

## 五、生图与效率

### 5.1 先样张后批量

- 正式批量前先生 1-2 页样张；**方向错了一次跑全量最费额度**。
- 中文/代码容易失真 → 不让 Image Gen 直接整页生中文，用确定性排版+嵌入真实截图。

### 5.2 Codex vs ChatGPT 网页生图

| 维度 | Codex 内建 Image Gen | ChatGPT 网页 |
|---|---|---|
| 速度 | 慢（2 张≈22 分钟） | 快（3 张≈6 分钟，7 张≈8 分钟） |
| 额度 | 占 Codex 额度 | 不占 Codex 额度 |
| 效果 | 推理中 | 推理高级，效果更好 |
| 缺点 | 慢 | 需上传文件、手动下载、提炼 Skill 缺这步 |

> 项目来源文件上限：Free 5 / Plus·Go 25 / Pro·Edu·Business 40。

### 5.3 常见问题

| 问题 | 方案 |
|---|---|
| 截图易破损/被盖 | 改 ASCII 放弃截图；或推理调高（费额度）；或换 ChatGPT 网页；或后置处理（ROI 低） |

## 六、金句与判断

> 「不是让 AI 一次替你完成所有判断，而是把重复动作标准化、沉淀成专属 Skill。」
> 「先出 1-2 页样张定方向，别一次生成全部——方向错了最费额度。」

## 七、行动建议

| 层级 | 行动 |
|---|---|
| 基础 | 按目录骨架建一个空项目，先把三份 .md 跑通 |
| 进阶 | 用 Product Design 出 6 套风格样板，选定一套写进 visual guide |
| 高阶 | 批量生图迁到 ChatGPT 网页，沉淀成自己的 Image PPT Skill |

## 八、我的批注（双轨）

- 我的：「先样张后全量」和「三份 .md 解耦」对我做教学配图很实用。
- 待验证：生图速度/额度为 Lester 个人 Plus 账号实测，随版本与账号等级变化。

---
## 相关笔记
- [[01 课程前言与 HTML 版 PPT 入门]]
- [[02 HTML 版 PPT 实战八步：查看、换风格、改页、导出与沉淀]]
- [[04 收尾与总结]]
