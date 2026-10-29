---
title: 研究：如何让 AI 生成 ppt
type: problem
status: open
date: 2026-04-15
updated: 2026-04-15
priority: 未定
source: https://musk-online.fbcontent.cn/pub-musk-ai-studio/workflow/file/document/7nFHHgQyM3PmL9FJcmUeEP.html
---
# 研究：如何让 AI 生成 ppt

## 核心问题
- 核心卡点：AI 生成 PPT 的稳定性不足，产出不可控
- 目标状态：找到一条可复用的稳定生成流程


## 方案一：逐字稿 → LLM 直出
- 适用场景：内容已明确，只需快速产出 PPT
- 步骤：
  1. 输出逐字稿（豆包，修改方便）
  2. 逐字稿 → 豆包/通义/其他 LLM → PPT 初稿
  3. 手动整合，调整结构与重点
  4. 发给豆包做样式完善（⚠️ 高峰期需多次刷新）

## 方案二：多源输入 → NotebookLM
- 适用场景：素材分散，需要 AI 辅助整合理解
- 输入源：
  - 视频素材
  - 同步辅导材料
  - 单招大方案文档
- 步骤：
  1. 上传全部素材到 NotebookLM
  2. 利用 AI 总结与提炼内容
  3. 基于提炼结果生成 PPT

## 方案三：PPT 大纲->codex+open-slide

1. open-slide安装+启动：cd my-slide  ，pnpm dev
2. 人工大纲结构->AI 修改+人工润色->清单体笔记
3. 给大纲->出初稿（手搓大纲）->codex移动版修改
4. ppt 提示词：[[ppt提示词]]


## 方案四：html --->pptx

飞象老师的 html: https://musk-online.fbcontent.cn/pub-musk-ai-studio/workflow/file/document/7nFHHgQyM3PmL9FJcmUeEP.html
1. 豆包：通过对比豆包、智谱清言、以及 Kimi，最好用的就是豆包，给链接让其提取内容，再重新生成 ppt
2. html->pdf->pptx: 通过在浏览器中点击打印，然后选择另存为 PDF 然后再通过 PDF 转 PPTX 的这个网站来实现。

## 方案五：采用skill



## 待决事项
- 输出类型：网页 PPT vs 实体 PPT（各有优劣，未决定）
- 工具对比：豆包 / 智谱 / NotebookLM 的最佳分工待验证




