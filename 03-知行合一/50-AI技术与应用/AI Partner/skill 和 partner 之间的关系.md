---
type: AI应用产物
status: 未标注
tags: [AI应用, AI partner]
updated: 2026-06-28
auto_filled: 2026-09-15
source: 自创/实践产物
---
## 一句话关系

**Partner 是包装格式。Skill 是运行形态。**

或者更精确：
> **Partner = 系统提示词 + 数据资产包，是「最小 AI 交付原子单元」**
> **Skill = Partner 部署到执行环境后的运行实例，是「能干活的能力插件」**

---

## 从 Truman 的 8 步流程看转化节点

这是最清晰的证据链：

```
第一步到第五步：建最佳实践教程
        ↓
第六步：转化成 Partner
        「我让AI把这个教程转化成Partner：
          一个系统提示词 + 一个数据资产包」
        ↓
第七步：封装到 YAI Partner，发布
        「Partner 自动生成一个个 MD 文档」
        ↓
第八步：下载本地 → 丢给 OpenClaw → 开始干活
         ↑ 
      到这里，它变成了一个 Skill
```

**转化节点就在第八步**——同样的系统提示词 + 数据资产包，在 YAI 平台叫 Partner，丢进 OpenClaw / Claude Code 运行起来就叫 Skill。

---

## 用 TCPR 框架理解

一堂后来用 TCPR 框架重构了 AI 角色定位：

| 角色 | 定位 | 本质上是什么 |
|---|---|---|
| T Partner | 教学伙伴 | 一个特定用途的 Partner |
| C Partner | 咨询伙伴 | 一个特定用途的 Partner |
| P Partner | 实践伙伴 | 一个特定用途的 Partner |
| R Partner | 研究伙伴 | 一个特定用途的 Partner |

这里的「Partner」是统称——每个角色都是「一个系统提示词 + 一个数据资产包」的封装。但当它们部署到具体环境（OpenClaw、Claude Code、Coze）里跑起来时，它们就是一个个 Skill。

---

## 从平台视角看

知识库里有一段关键材料：

> 「一堂提供最小【逻辑单位】和【数据单位】，大家可以自行封装和使用；包含：系统提示词、Coze、Skill、Agent（ReACT）甚至最近火热的 OpenClaw。」

这里列出的五种都是**部署目标形态**：

| 部署形态 | 运行环境 |
|---|---|
| 系统提示词 | 直接粘贴到 LLM 对话窗口 |
| Coze | Coze 平台的 Bot |
| Skill | OpenClaw / Claude Code 的能力插件 |
| Agent（ReACT） | 支持 ReACT 模式的 Agent 框架 |
| OpenClaw | OpenClaw 的 Agent 实例 |

**同一个 Partner（系统提示词 + 数据资产包），可以部署成上面任何一种形态。** 部署成 OpenClaw 能跑的，就叫 Skill。

---
---

## 一张图总结

```
最佳实践教程（你的审美和判断力的沉淀）
        ↓ 第六步：工业化转译
   ┌────────────────────┐
   │  Partner            │
   │  = 系统提示词       │  ← 一堂的「最小 AI 交付原子单元」
   │  + 数据资产包       │    平台无关，可跨平台迁移
   └────────────────────┘
        ↓ 第七步：发布到 YAI Partner
        ↓ 第八步：下载 MD 文档，部署到执行环境
   ┌────────┬────────┬──────────┬──────────┐
   │ Skill  │ Agent  │  Coze    │ 系统提示词 │  ← 运行形态
   │(OpenClaw)│(ReACT)│(Coze平台)│(直接粘贴) │
   └────────┴────────┴──────────┴──────────┘
```

---

## 所以回到你的问题

**Skill 封装和 Partner 封装是什么关系？**

它们是同一件事的两个阶段：
- **Partner 封装**是标准化包装阶段——把能力变成「系统提示词 + 数据资产包」的原子单元，平台无关，可跨平台迁移
- **Skill 封装**是部署运行阶段——把这个原子单元部署到 OpenClaw / Claude Code 里，让它变成一个能实际干活的执行单元


##  partner与 skill 之间的转换

把你手里的 Partner MD 文档（系统提示词 + 数据资产包）丢给codex，对它说：「**这是我设计的一个 Partner，包含角色定义、工作流程、约束条件和参考案例。请你按照 Claude Code 原生的 Skill 格式，帮我生成一个完整的 skill.md 及相关参考文件。**」——大概率它能自己搞定。