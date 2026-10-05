---
obj_token: PyACdT53ToQCLqxVhuNcrX5AnLf
title: 01 课程前言与 HTML 版 PPT 入门（截图00-01）
feishu_path: 14 AI制作ppt-截图笔记/01 课程前言与 HTML 版 PPT 入门（截图00-01）
obj_type: docx
fetch_method: docx
source: https://github.com/op7418/guizang-ppt-skill
---

<title>01 课程前言与 HTML 版 PPT 入门（截图00-01）</title>

> 部分内容由豆包生成

# 截图00 课程前言：自我介绍与两条做 PPT 的路线

## 自我介绍

一堂八年级，学分 2246（截止到 2026/7/9）。

个人简介：AI × SaaS × 企业培训 × 项目管理。姓名方振义，昵称 Lester。10+ 年技术人，曾服务 +8 年四大企业担任 SalesForce 架构师，完整培训系统搭建与 SalesForce 技术讲课经验；新人 SalesForce 培训负责人、SalesForce 考证负责人、SalesForce Einstein AI 培训负责人；熟悉 AI、SaaS 技术；10 门三节课 AI 应用课程主理人；"IT/AI+项目管理+金融"赛道，40+ 资格认证，包含 30+ 相关 SalesForce 证书、PMP、TOGAF、敏捷项目管理、量化分析师 AQF、财务分析师 FVA、私募基金从业资格；AI 领域书《万山无阻》联合作者。

【互动】商业突破大航海的 AI 一页纸，有看过的同学可以评论区扣个 1。

作者往期分享文章清单：Codex 系列（Codex 电脑控制 Computer Use、Codex 高级用法 Subagents 子代理/子智能体、Codex 追求目标 Goal mode、Codex 介绍基础功能基础操作与设置、Codex 编程工具推荐 2 个官方免费视频插件、OpenAI Codex 编程工具无缝整合 GPT Image 2 生图模型）；GPT Image 2 简介；Claude Code 国内适配版 2 个方案搞定安装与环境配置；OpenClaw 系列（阿里云+OpenClaw 不到 20 元尝鲜、集成飞书、挑选官方 ClawHub 中 Skills、入门应用方向选择、数字员工入门设置关键档案、数字员工隐私保密能力）；AI 编程（大 Markdown 文件不好读？顺手追加一个 HTML）。

## 课程前言

由于这次航海，也分享蛮多 Codex 的文章，因此收到一堂的邀请，是否可以针对 Codex 来做 PPT 分享，毕竟接下来将会有商业突破大航海汇报，或是平日上班也是高频的需求：PPT 汇报。

【互动】你做 PPT 的时候，最花时间的是哪一步？你可以在评论区打对应的数字：

1. 整理内容
2. 找风格、做排版
3. 反复修改
4. 上面三个都有

今天分享用 Codex 做 PPT，有两种做法：

- HTML PPT：内容、文字、布局、交互都写在网页里，适合快速修改、现场演示和视觉表达。
- Image PPT：每一页主要由 GPT Image 生成，视觉冲击力更强，适合发布、传播和需要完整画面感的场景。

这两条路线不是谁取代谁。它们解决的是不同问题。HTML 的优势是可修改、可验证、可继续迭代；Image 的优势是把构图、材质、配图和画面气质一次性压进一张图里。HTML 像一个可以调试的工程，Image 像一张设计的海报。

## HTML 版 PPT：把课件变成可调试的网页

- 用 HTML 版 PPT 做初稿，核心不是为了取代 PowerPoint，而是为了把「做 PPT 初稿」从手工排版，变成可快速生成、可快速修改、可复用的结构化流程。
- 用 HTML 版 PPT 不是一张扁平图片，而是一份可以持续调试的中间稿。

### HTML 版 PPT 优势（6 个）

| 优势 | 说明 |
|-|-|
| 生成速度快 | Codex 可以直接生成 HTML/CSS，一次做出多页初稿 |
| 修改成本低 | 改颜色、字体、布局、间距，只需要改 CSS 或组件 |
| 结构更清楚 | 每一页都是模块化内容，适合先输入逻辑 |
| 适合批量生成 | 金句页、课程页、数据看板页、产品介绍页都能套模板 |
| 图表与数据更方便 | 可以直接接 CSV、Excel、JSON，生成动态图表 |
| 可预览、可部署 | 浏览器打开即可预览，也能一键部署成网页演示版 |

小贴士：HTML 版 PPT 特别适合需要反复修改、批量生成与网页展示的内容。

如果我们从零开始做 HTML PPT，也会马上遇到另一组问题：画布怎么固定成比例？怎么控制字体？怎么打印成 PDF？

# 截图01 guizang-ppt-skill 简介与前四步

## guizang-ppt-skill 简介

所以这次我采用了歸藏老师分享的一个 HTML PPT Skill，guizang-ppt-skill。下载来源：https://github.com/op7418/guizang-ppt-skill

这个 Skill 适用于制作杂志风、分享型或汇报类的 HTML 版 PPT。它能按照固定的主题和版式体系，自动生成网页演示文稿，并内置了自检清单。不过，生成内容是否准确、所用资料是否有据可查，仍然需要由自行核实与判断。guizang-ppt-skill 支持 Claude Code、Codex、Cursor。

（界面：GitHub 仓库 README 截图——Guizang PPT Skill · 网页 PPT / 配图 / 封面，stars 2060，AGPL-3.0，内置两套视觉系统：Style A 电子杂志 × 电子墨水（像 Monocle 贴上了代码，适合叙事、观点、分享、个人风格表达）；Style B 瑞士国际主义（网格至上、单一高饱和锚点色、直角、发丝线、极致字号对比，适合事实、产品、分析、方法论表达）。常见使用场景表与平台支持表。）

## 第一步：安装 guizang-ppt-skill

如果不想要全局级 Skill，可以在指定的目录下，把下面提示词改成"项目级 Skill"，这样 Skill 只会在此项目生效。

安装提示词：

```bash
安装 guizang-ppt-skill 且是全局级 Skill，来源 https://github.com/op7418/guizang-ppt-skill
```

注意事项：Codex 提示安装 Skill 需要重启，就建议重启 Codex。

（界面：Codex 安装成功返回——路径 C:\Users\Administrator.codex\skills\guizang-ppt-skill，来源 op7418/guizang-ppt-skill，SKILL.md、README.md、资源与校验脚本均完整，已适配 Codex、Windows 和中文环境；如界面尚未识别，请重启 Codex。）

## 验证 Skill

方式一：\$ Skill 名称 或 @Skill 名称。\$ 只会列出 Skill 清单；/ 不只包含 Skills，也包含其他 Codex 能力。

方式二：到 Codex 技能确认。在插件中选技能，如果在插件中寻找找不到此 Skill。（界面：Codex 左侧栏 @插件 → 技能列表，找到 "Guizang Ppt Skill 生成横向翻页网页 PPT / HTML dec..."）

## 第二步：让 AI 读取项目资料

- 把相关的资料放在同一个目录中，让 Codex 去读取此目录，在 [项目] 中选 [使用现有文件夹]，来指定你的目录。
- 关于项目目录设置，可以参考 Image 版 PPT 中第一步：项目目录，把上下文放进文件夹，有相关建议做参考。

（界面：Codex 创建项目弹窗 → 项目类型 → 本地 → 使用现有文件夹）

建议：不建议一开始就让 Codex 凭空设计，建议作法是先让它看当前文件夹，讲清楚准备使用哪些文件，你要使用当成 HTML PPT 的素材，同时可以包含限制要求。

## 分析提示词与执行结果

提示词的边界：盘点资料；请不要编造没有提供的数据与内容。

Guizang PPT Skill 内置提供两种视觉方向：电子杂志风和瑞士国际主义。电子杂志风适合叙事、观点、分享、个人风格表达；瑞士国际主义适合事实、产品、分析、方法论表达。这次选择瑞士国际主义，因为内容主要是我自己一堂的 AI 一页纸内容当做素材，包含 Codex 功能介绍和 GPT Image，属于科技、工程和方法论主题。

分析提示词：

```bash
请先分析此目录 HTML PPT，这是打算采用 Guizang Ppt Skill 且风格是 瑞士国际主义， 目标是产生限定 10 页
```

（界面：Codex 执行结果——已完成只读分析，HTML PPT 目前包含：7 份 Word、Codex 6 份、GPT Image 2 份、209 页内容图片、暂无 HTML；已建议 10 页映射表（封面、Codex 基础功能与基础操作与设置、Computer Use、Goal mode、Subagents、两个官方免费视频插件、Remotion 与 Hyperframes 对比、Instant 与 Thinking、Codex 整合 GPT Image 2），S01-S10 页码；内容控制原则：只压缩重组 Word 已有内容、不补充外部事实或虚构数字、不使用需要强行编造数据的版式、版本号套餐价格等时效性信息必须标注原文日期或"个人实测"、Word 内本机路径预售信息重复课程广告默认不纳入、图片优先复用 Word 内已有截图、主题色建议使用适合 AI 科技内容的克莱因蓝 IKB。）

## 第三步：生成大纲 & 调试

这时候可以生成大纲第一版看内容，目的是减少后面大改的概率。

大纲提示词，建议同时开启计划模式。建议：当启动计划模式，推理可以调整到 高 或 超高，可以根据你文件数量与上下文决定，这样的实施方案效果会更好。

（界面：Codex 输入框左下角 + → 智能体 → 计划模式 开启计划模式；推理档位 5.5 高）

大纲提示词：

```bash
根据上面的内容，帮我设计10 页的大纲内容，采用 Guizang Ppt Skill 生成 HTML PPT
```

## 计划模式相关的提问内容

提问 1：这份 10 页瑞士风 HTML PPT 应如何处理 Word 内嵌图片？选项：①纯信息设计（Recommended）不抽取截图，仅用网格、文字和几何结构，事实边界最稳且适合；②少量关键截图，筛选 2-3 张现有截图作为证据页，视觉更具体但需要裁切和适配；③截图优先，大量复用 Word 内嵌截图，接近教程课件但信息密度和制作复杂度更高。

提问 2：这份 PPT 主要面向哪类听众？选项：①AI/Codex 初学者（Recommended）强调概念、差异和使用路径，减少技术细节与长提示词；②已有 Codex 用户，突出 Goal、Subagents、插件和工作流等进阶用法；③课程宣传受众，更强调能力全景与吸引力，但会弱化操作细节。

（界面：10 页瑞士风 HTML PPT 实施方案 Summary——标题《Codex：从对话到执行》，副标题"从基础操作到视频与图像生成"，风格应用 AI 科技蓝色系 IKB，902FA7 一个强调色；每页页码与主题映射 S01-S10；Implementation Changes 从 template-swiss.html 构建、删除模板示例页、使用隐藏 HTML 注释记录每页 Word 来源、正文文字不低于 18px/16px、复制本地 assets/motion.min.js 作为动画蓝图、不改或覆盖 7 份 Word 原文件；Test Plan 运行 validate-swiss-deck.mjs、浏览器逐页检查 1920×1080；Assumptions 省略重复的个人介绍课程推广；实施此计划？是，实施此计划。）

这边就是开始调整自己大纲内容，甚至可以考虑下面资料追加：Logo；Style & font 调整；主题 & 内容的文字调整；版式规则。