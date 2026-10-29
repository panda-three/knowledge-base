---
type: 研究
status: 待验证
date: 2026-09-18
source: 公众号「极客之家」2026-08-27《23万Star、被安装超1800万次，这套顶级的Skills有多强？》；仓库 mattpocock/skills（MIT）。已联网核验：来源真实、仓库存在、23.8万 Star。
audience: 自己
tags: [AI, Skills, 提示词工程, 软件工程, 外部研究]
related: [[研究：AI Skills与Agent万字长文观点]]
---
# 研究：Matt Pocock 的 AI 工程 Skills 库

> 原件归档：99-归档/收件箱原文/2026-09/20260918-0633-公众号链接.md

## 是什么
- Matt Pocock（Total TypeScript 作者，前 Vercel/Stately 工程师）把自己 `.agents` 目录里日常在用的 skill 文件原样开源。
- 一个 skill = 一个文件夹 + 一份流程说明文档；触发时（如 `/tdd`）才加载，平时不占上下文，区别于每次都加载的 CLAUDE.md。
- 53 个 skill、累计安装 1800 万+；定位**小而专、只干一件事**，用不用、何时用由人决定（区别于 Spec Kit / BMAD 这类"流程接管一切"）。

## 高频 skill 四组
1. **动手前问清需求**：`/grill-me`、`/grill-with-docs`（让 AI 反向盘问需求，一次只问一个，问清为止；后者把术语写进 CONTEXT.md、把不可撤销决策写成 ADR）；`/ask-matt`（帮你挑 skill）。
2. **写码/排错有规矩**：`/tdd`（先写必然失败的测试再写最小实现，防"假 TDD"）；`/diagnosing-bugs`（必须先跑出稳定复现命令才允许猜原因）；`/code-review`（规范符合与需求实现分开查）。
3. **管住代码库**：`/improve-codebase-architecture`（扫仓库找"浅模块"，生成 HTML 报告供人挑，不自作主张重构）。
4. **串流程**：`/to-spec`（对话整理成规格）、`/to-tickets`（拆工单+依赖）、`/implement`（走 tdd+code-review）、`/triage`（issue 分诊）、`/handoff`（长会话压缩成交接文档）、`/prototype`（一次性原型看完即弃）。

## 我的判断
- 核心不是新东西：盘问需求 / 测试先行 / 统一语言 / ADR / 原型验证，都是软件工程二三十年的老规矩，只是被写成 AI 能执行的纯文本。
- 价值：AI 写得快把老问题放大（需求没说清、代码越堆越乱），这些"老规矩"正好对冲；且流程不做黑盒，可 fork 自改，把判断权留给人。
- 对我：`/grill-with-docs` 的"先被盘问、建 CONTEXT.md / 统一术语"最值得先试；一次性 demo / 脚本用不上。
