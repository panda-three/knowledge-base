---
作者: Panda
来源: 合并《如何设计一个 Skill》+《Skill 最佳实践》
用途: 下次建 Skill 前扫一眼，3 分钟做完边界判断
使用者: 我自己
版本: v1
日期: 2025-06-17
标签:
  - Skill
  - Codex
  - 工作流
source: https://github.com/suyuan2022/ai-dev-pipeline
---
# 建 Skill 的执行清单

---

## 一、核心姿势（先刻进骨头）

- **Skill 是写给 AI 看的**：把经验提前沉淀成 AI 能执行的协议，下次直接让 AI 按协议干活
- **先简单做出来，快速迭代**：第一版只跑通核心流程，用真实场景试跑后再补细节
- **边界公式**：一个 Skill = 一段稳定的用户意图 + 一段稳定的工作流 + 一组相对稳定的产物

---

## 二、建不建？6 问决策

| #   | 问题               | 答"是" → 倾向建 Skill |
| --- | ---------------- | ---------------- |
| 1   | 用户会不会反复直接提这类需求？  | ✓                |
| 2   | 有没有相对稳定的工作流？     | ✓                |
| 3   | 是否需要专门判断，而非临场发挥？ | ✓                |
| 4   | 产物是否相对固定？        | ✓                |
| 5   | **提示词有没有用三到五次**  | ✓                |



---

## 三、目录结构：按需生长

**唯一必需的**：`SKILL.md`

| 目录 | 什么时候加 |
|---|---|
| `scripts/` | 确定性执行逻辑，临场生成容易漂移（如 `md→html`） |
| `references/` | 长规则、详细资料，不必每次都加载进上下文 |
| `assets/` | 模板、样式、图标等生成资源 |
| `agents/` | UI 元数据、平台集成信息（本地协作通常不需要） |

**姿势**：先用只有 `SKILL.md` 的最小版本跑，哪层内容反复出现再拆出去。让目录跟着职责长，别跟着模板长。

---

## 四、如何管理 skill

1. 统一位置：/Users/panda/Desktop/best-practice
2. 用软连接：
+ skill 文件夹：for d in skills/*/; do ln -sf "$(pwd)/$d" ~/.codex/skills/$(basename "$d"); done
+ 单skill 文件：ln -s "$PWD/llm_wiki_skill" ~/.codex/skills/llm_wiki_skill
---

> **记住两句**：Skill 是用出来的，不是设计出来的。完整不在目录多，在边界清。


## 五.最佳实践池子
1. coding:https://github.com/suyuan2022/ai-dev-pipeline
2. card:https://github.com/lijigang/ljg-skills/tree/master/ljg-card
3. picture:https://github.com/quzhi-ai/tufte-xiaohei-fusion
4. ppt:https://github.com/op7418/guizang-ppt-skill
5. dbs:https://github.com/dontbesilent2025/dbskill#
6. ppt:https://github.com/zarazhangrui/frontend-slides
7. ppt:https://open-slide.dev/docs/getting-started  安装在`/Users/panda/my-slide`
8. UI 设计 skill:https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
9. 大神 skill:https://github.com/mattpocock/skills/tree/main/skills/productivity/teach