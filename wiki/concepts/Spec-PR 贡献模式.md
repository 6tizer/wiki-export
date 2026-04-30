---
title: Spec-PR 贡献模式
type: concept
tags:
- Agent 协作模式
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0f4d5c60edf04773ba7c96b1d8d08981
notion_id: 0f4d5c60-edf0-4773-ba7c-96b1d8d08981
---

## 定义

Spec-PR 贡献模式是 Warp 开源后引入的结构化贡献流程：在提交任何代码之前，贡献者必须先提交 `specs/GH<issue#>/product.md`（可测试的行为不变量）和 `specs/GH<issue#>/tech.md`（含文件引用的实现计划），经批准后才能开启代码 PR。

## 关键要点

- **分阶段贡献**：Bug 修复可直接进入 ready-to-implement；Feature 请求必须经过 ready-to-spec → spec PR 批准 → 代码 PR 三阶段

- **AI 审查优先**：代码 PR 自动分配给 Oz Agent 做第一轮 review，Oz 批准后才自动请求人工 SME 审查

- **零成本 Agent 实现**：贡献者可以 mention @oss-maintainers 让 Oz 云端 Agent 用免费额度实现 issue，无需本地 Agent harness

- **可重复审查**：贡献者可用 `/oz-review` 命令最多重新请求 3 次 AI review

- **人类定义、Agent 实现**：核心理念是人类负责规格定义和验证，Agent 负责实现和审查

## 关联概念

- Oz：执行 review 和 implementation 的 Agent 平台

- Open Agentic Development：Spec-PR 模式是该范式的具体制度化落地

## 来源引用

- [摘要：Warp Goes Open-Source, And Oz Becomes Your First-Line Code Reviewer](summaries/摘要：Warp Goes Open-Source, And Oz Becomes Your First-Line Code Reviewer.md)（[原文](https://x.com/AlphaSignalAI/status/2049534207412871477)）
