---
type: 研究
status: 初稿
date: 2026-09-17
version: V0.1
author: Panda + AI
audience: 课程开发（AI 辅助代码生成模块素材）
tags: [智能体构建课, Vibe Coding, 调研大纲, 最佳实践]
related: [双三角模型本体, 双三角模型十层解读, 研究：Claude Code训练AI员工实战指南]
source: https://code.claude.com/docs/en/best-practices
---

# Vibe Coding 最佳实践调研大纲（智能体构建课 · 模块素材）

> **用途**：支撑课程「AI辅助代码生成」模块的内容开发。本文是**大纲**，不是成稿；每条目标注来源与可信度，后续按此骨架补全。
> **来源标注图例**（对应反幻觉 Skill 的 L1-L5 来源定级）：
> - 【库】＝ 用户知识库内部素材（可信但须看 status）
> - 【外·L1】＝ 一手原始资料（官方文档 / 论文 / 原始推文）
> - 【外·L2】＝ 权威机构 / 权威媒体（学术、官方客户案例、央媒）
> - 【外·L3】＝ 专业媒体 / 社区（钛媒体、36氪、腾讯云社区、掘金）
> - 【外·L4】＝ 个人博客 / 自媒体（仅供参考，数字多为"一方称"）

---

## 0. 调研结论摘要（先行）

1. **Vibe Coding 已从"玩票"进化为工程实践**：2025 年 Karpathy 命名时是"忘记代码存在"的玩具玩法；到 2026 年，主流共识收敛为 **"意图 → 计划 → 生成 → 验证"闭环 + 人保留架构/安全/判断**。【外·L1-L3】
2. **最佳实践可归纳为 5 条**：Spec/测试先行、plan mode 分阶段、每次 diff review、可运行检查（pass/fail）、关键区域（auth/支付）人工。【外·L1-L3】
3. **案例证明力强但有水分**：从 $1M ARR 到 8000 万美元收购都有真实案例；但多数收入数字是创始人自述（一方称），教学须优先用官方客户案例（Ramp/Block）。【外·L1-L4】
4. **库内现状：直接素材极薄**——vibe coding 目录仅 2 个文件且 1 个为空模板；但**双三角体系可作"人机分工"的理论框架**（人搭系统，AI 跑系统），这是本模块区别于"工具课"的魂。【库】

---

## 1. Vibe Coding 的起源与定义

### 1.1 起源
- Karpathy 2025 年 2 月推文定义："fully give in to the vibes, embrace exponentials, and forget that the code even exists"（完全屈服于氛围，忘记代码存在）【外·L1：原始推文/权威转述】
- Collins Dictionary 2025 年度词汇（vibe coding 被词典收录）【外·L2】
- arXiv 论文《Vibe Coding: Toward an AI-Native Paradigm for Semantic and Intent-Driven Programming》——学术定义与范式讨论【外·L1】
- 钛媒体 2.5 万字《一部 AI 编程运动史（2020-2026）》——中文语境最完整的历史梳理【外·L3】

### 1.2 概念辨析（课程开场要讲清）
- vibe coding vs 传统 AI 辅助编程（Copilot 补全 vs 整功能生成）【外·L2-L3】
- vibe coding vs No-Code/低代码（Lovable 等，概念重叠但工具不同）【外·L3】
- **原始语境 vs 生产级应用**：Karpathy 最初指玩具/个人项目；用于生产软件是后来的扩展，也是争议焦点【外·L1-L2】

### 1.3 2026 年现状
- 已进入"工程化"阶段：企业客户案例（Ramp/Block）、YC 公司全栈用 Claude Code 建公司【外·L1】
- 中文社区讨论成熟度：从"工具安利"转向"工程纪律与代价"【外·L3】

---

## 2. 工具链全景（课程"选哪套工具演示"的依据）

### 2.1 主流工具（各附能力定位）
| 工具 | 定位 | 来源 |
|---|---|---|
| Cursor | IDE 内 AI 补全 + 对话编辑 | 【外·L2-L3】 |
| Claude Code | 终端 Agent，plan mode、subagents、CLAUDE.md | 【外·L1：官方文档】 |
| Windsurf | 编辑器 Agent + Codemaps 代码理解 | 【外·L3】 |
| Lovable / Replit | 自然语言直接生成全栈应用（No-Code 边界） | 【外·L3-L4】 |
| GitHub Copilot | 补全为主 | 【外·L2】 |

### 2.2 实测对比
- Convex 团队实测 Claude Code vs Cursor（从零搭含 API 抓取/解析/后端的完整项目）【外·L3】
- 腾讯云实测：Cursor+Claude Code 组合提效约 3 倍（接口层 2h vs 5h、跨包权限迁移 3h vs 8h）【外·L3】

### 2.3 课程选型建议（待定，见缺料清单）
- 课堂演示优先选**演示稳定 + 现场可控**的工具链；建议课前完整预演（质量门 D4 环节）

---

## 3. 最佳实践方法论（课程核心章节）

### 3.1 工作流框架（"怎么和 AI 一起写代码"）
- **Anthropic 官方 plan mode 四阶段**：Explore（读代码、问问题）→ Plan（出方案给人批）→ Implement → Verify（跑检查）【外·L1：Claude Code 官方 best practices】
- **Linh Truong 五步**：Frame Intent（目标/约束/验收标准）→ Load Context（文件/类型/约定）→ Plan → Generate & Run → Verify（读 diff、跑 app、测边界、安全审查）【外·L4】
- **Spec 先行**：每个功能先写 3-5 行 Spec 再让 AI 实现，避免"边想边说"返工【外·L2：上海图书馆培训材料】
- **测试先行**：先写测试用例定义期望行为，让 AI 按测试实现——"最强的约束手段"【外·L2】

### 3.2 提示词技术
- **Intent not Implementation**：描述结果与意图（"加一个可搜索的用户列表页"），不要微管理实现细节【外·L3：Developers Digest】
- **Scoped Prompts 模板**：Goal（做什么）+ Constraints（能碰/不能碰）+ Process（步骤）+ Verification（怎么验收）【外·L3：AI Wiki】
- **技术精确性**：把"make it faster"改成"优化数据库查询，响应从 2 秒降到 500ms 内"【外·L1：Anthropic】
- **引用真实文件**：prompt 里指具体文件（"match the pattern in src/routes/users.ts"），别口头描述风格【外·L3】
- **One feature, one session**：一次会话只做一个功能【外·L3】

### 3.3 工程化纪律（决定"能不能扛住生产"）
- **每次 commit 做 aggressive diff review**——不是扫一眼【外·L3-L4：Kunal Ganglani】
- **70/30 法则**：70% AI 辅助（样板/测试/文档/重构），30% 人工（架构/复杂逻辑/安全/评审）【外·L3：DEV Community】
- **可运行检查**：给 AI 能 pass/fail 的检查（测试/构建），让"看起来完成"变成"验证过完成"【外·L1：Anthropic】
- **CLAUDE.md / 版本控制指令文件**：把项目约定、常用命令、风格写进强制 README【外·L1】
- **subagents 分工**：专项子代理处理隔离任务（读大量文件/专项检查）【外·L1】
- 高级形态：**harness**（initializer agent + claude-progress.txt + git 提交）支持长时运行【外·L1：Anthropic 工程博客】

### 3.4 安全与质量（北大清华学生必问的）
- **四类风险**（Ankur Tyagi / freeCodeCamp）：context gaps（AI 不知道自己不知道）、integration blind spots（单测通过但冲突）、security、error handling【外·L3】
- 具体检查点：登录/鉴权是否真实安全、输入是否验证、API key 是否在环境变量、出错时会发生什么【外·L3-L4：TechRepublic / 10 best practices】
- **关键区域人工**：auth、支付等保留手工编码【外·L3：daily.dev】

---

## 4. 真实案例库（教学素材，按可信度分档）

### 4.1 高可信案例（官方客户案例，教学首选）
- **Ramp**：30 天落地 100 万行 AI 建议代码；事故调查时间最高降 80%；50% 工程师周活跃使用【外·L1：Claude 官方客户案例】
- **Block**：75% 工程师每周省 8-10 小时；内部工具 adoption 翻倍【外·L1：Anthropic 客户案例】
- **YC 公司全栈用 Claude Code 建公司**（HumanLayer / Ambral）【外·L1：Claude 官方博客】
- **Lazy AI**：代码需多次修复的比例降 51%、首次实现成功率 73%【外·L1：Anthropic 客户案例】
- **Emergent**：100+ 步工作流（此前 10-15 步）、自动生成 5000+ 行代码、自我纠错【外·L1】

### 4.2 独立开发者案例（社区报告，数字为"一方称"，须标注）
- **fly.pieter.com**（Pieter Levels）：Cursor 制作，$1M ARR run-rate，320K+ 玩家【外·L4：创始人自述】
- **Base44**：0 员工、$1M ARR、后被 Wix 以 8000 万美元收购【外·L4：媒体转述】
- **ShiftNex**：Lovable 制作，5 个月到 $1M ARR，5000+ 活跃用户【外·L4】
- **俯卧撑闹钟**（24 岁 Jake）：上线 4 个月月入 $5 万【外·L4：自媒体】

### 4.3 中文案例（贴近学员认知）
- **"手搓 App 赚 40 万"**：杭州产品经理 Shawn 做"阿布"AI 桌面搭子，82 个版本、B 端 5000 元购买【外·L2：中国新闻网/中国网】
- **Roi 小手机**：前字节员工 3 天做出爆款 Demo，成为融资起点【外·L3：钛媒体】
- **腾讯云 Cursor+Claude Code 提效实测**（真实开发任务时间对比）【外·L3】

### 4.4 案例使用注意（反幻觉红线）
- 4.2/4.3 的收入数字多为创始人自述或媒体转述 → 教学中标注"据创始人称"，不当作已验证事实
- 优先用 4.1 官方客户案例（有企业背书）；独立开发者案例用于"激励"而非"论证"

---

## 5. 批判与边界（防"只讲好话"，应对最挑剔学生）

- **《The Vibes Don't Scale》**（华盛顿大学 CSE331 课程材料）：前几个 PR 很好，200 次后 codebase 失控；**修复不是更好的 prompt，而是建一个能复利的机器**（规范、测试、架构纪律）【外·L1：学术课程材料】
- **"理解即负责"**：高效者基于对代码的理解"驾驭直觉"（surf the vibes）；生成超出理解能力的代码=灾难【外·L3：掘金】
- **Production Break**：AI-built apps 在生产环境出问题的常见模式【外·L4】
- **隐性代价**：开发者能力退化风险、调试成本转移【外·L3：36氪】
- **什么不该 vibe**：架构决策、安全、支付、复杂集成、不理解的代码【外·L3】

---

## 6. 对课程设计的启示（与双三角体系对接）

### 6.1 人机分工映射（用你库里的双三角框架讲）
| 双三角 | 在 Vibe Coding 中对应 |
|---|---|
| 人的创造力 | 提出产品意图、新假设（Intent） |
| 人的审美 | 验收标准、知道"什么叫好结果"（taste is the moat）【外·L4 印证】 |
| 人的体系 | 架构、Spec、CLAUDE.md、工程纪律 |
| AI 的场景 | 介入具体编码位置、生成实现 |
| AI 的基本功 | 按 Spec 执行、迭代、跑测试 |
| AI 的数据 | 上下文、样例、历史代码库 |

金句（库内双三角）：**"人搭系统，AI 跑系统"**——外网所有最佳实践本质上都在讲这句话。【库】

### 6.2 课程模块教学设想（初步，待大纲定稿深化）
- 现场 demo：Spec → 生成 → 验证 闭环现场演示（工具链待定）
- 学员练习：每人写 3 行 Spec，让 AI 实现，再互相 diff review
- 案例教学：从"独立开发者神话"到"工程化纪律"的对照（4.1 vs 4.2 的差距就是"能不能 scale"）
- 批判环节：用《The Vibes Don't Scale》做课堂辩论（"vibe coding 会杀死程序员吗"）

### 6.3 教学红线
- 案例数字必须标注来源与可信度（反幻觉 Skill 强制）
- 工具现场演示必须课前预演（质量门 D4）
- 不吹"AI 取代程序员"，讲清"人机分工"（双三角立场）

---

## 7. 缺料清单（待补）

- [ ] **库内「主题 AI 小程序」空模板**待填——可改造为学员作业模板（现场项目任务书）【库】
- [ ] **工具链选型定案**：课堂演示用 Cursor 还是 Claude Code（稳定性/网络/账号）——需实际预演
- [ ] **精读并转讲义**：Anthropic《Claude Code: Best practices for agentic coding》全文【外·L1】
- [ ] **精读**：《The Vibes Don't Scale》全文（作为课堂批判素材）【外·L1】
- [ ] **中文案例一手信源核验**：阿布/40 万收入、Roi 小手机融资——找到原始报道交叉验证【外·L2→需核验】
- [ ] **库内补充沉淀**：调研结论转成知识库笔记（01-实事求是/AI技能 或 03-素材），挂双三角 related

---

## 附：主要来源清单（可追溯）

**官方一手（L1）**：
- Claude Code 官方 Best Practices：https://code.claude.com/docs/en/best-practices
- Anthropic 工程博客：https://www.anthropic.com/engineering/claude-code-best-practices
- Anthropic《Effective harnesses》：https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Anthropic《Scaling Agentic Coding》：https://resources.anthropic.com/hubfs/Scaling%20agentic%20coding%20across%20your%20organization.pdf
- Claude 客户案例（Ramp/Block/YC）：https://claude.com/customers/ramp 等
- arXiv 论文：https://arxiv.org/pdf/2510.17842v1
- UW《The Vibes Don't Scale》：https://courses.cs.washington.edu/courses/cse331/26sp/readings/the-vibes-dont-scale.pdf

**权威/专业媒体（L2-L3）**：
- 钛媒体运动史：https://www.tmtpost.com/7964511.html
- 中国新闻网《手搓 App 我赚了 40 万》：http://news.china.com.cn/2026-05/23/content_118510478.shtml
- 腾讯云 Vibe Coding 深度解析：https://cloud.tencent.com/developer/article/2731295
- 腾讯云 Cursor+Claude Code 提效实测：https://cloud.tencent.com/developer/article/2689887
- 36氪《coding 的中场战事》：https://m.36kr.com/p/3815446937820932
- 上海图书馆培训材料（PDF）：https://opendata.library.sh.cn/download/docs/2026/...
- 掘金《Windsurf Codemaps 深度解析》：https://juejin.cn/post/7571285984089243700

**社区/个人（L4）**：
- Kunal Ganglani：https://www.kunalganglani.com/blog/vibe-coding-best-practices-2026
- Linh Truong：https://linhtruong.com/research/Vibe_Coding_Strategy.html
- CodingWithVibe 案例：https://codingwithvibe.com/vibe-coded-apps/
- DEV Community 70/30：https://dev.to/pockit_tools/vibe-coding-in-2026-the-complete-guide-to-ai-pair-programming-that-actually-works-42de

---

## 变更记录
- V0.1（2026-09-17）：初版。调研覆盖库内检索（vibe coding 目录+Claude Code 研究）+ 外网 3 轮检索（定义/官方最佳实践/案例/批判）；来源按 L1-L4 标注。
