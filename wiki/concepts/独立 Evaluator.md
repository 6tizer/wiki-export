---
title: 独立 Evaluator
type: concept
tags:
- Harness 工程
- Agent 协作模式
status: 审核中
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/ea71a5fd37044d94819b6d20594d7772
notion_id: ea71a5fd-3704-4d94-819b-6d20594d7772
---

## 定义

独立 Evaluator 是与主执行模型分离的验收器，只根据产物和可执行结果判断任务是否达标，而不信任模型自评。

## 关键要点

- 主执行模型负责生成，Evaluator 负责验收

- 最好基于可执行检查，例如测试、编译、页面打开结果或 Schema 校验

- 适合放在关键节点做 gatekeeping，并与失败重试配合

## 关联概念

- [Harness Engineering](concepts/Harness Engineering.md)

- [生成者+验证者](concepts/生成者+验证者.md)

- [验证闭环](concepts/验证闭环.md)

## 来源引用

- [原文链接](https://blog.ltbase.dev/posts/agents/harness-engineering.html)｜《模型不是笨，是 Harness 没配好》｜来源条目：[摘要：模型不是笨，是 Harness 没配好](summaries/摘要：模型不是笨，是 Harness 没配好.md)
