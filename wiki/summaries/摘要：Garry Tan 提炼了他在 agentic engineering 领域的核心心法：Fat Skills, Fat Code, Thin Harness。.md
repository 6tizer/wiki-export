---
title: 摘要：Garry Tan 提炼了他在 agentic engineering 领域的核心心法：Fat Skills, Fat Code, Thin Harness。
type: summary
tags: []
status: 已审核
confidence: medium
last_compiled: '2026-04-15'
source_tags: Agent, LLM, 自动化, Prompt工程
source_article_url: https://www.notion.so/343701074b6881ddb6f2e7e20acfc38f
notion_url: https://www.notion.so/Tizer/8c8ef76171444df39453fe1ae39e5d10
notion_id: 8c8ef761-7144-4df3-9453-fe1ae39e5d10
---

## 一句话摘要

这篇文章把 Agentic Engineering 抽象为一套三层架构原则：将判断性知识沉淀到 Skills，将确定性执行下沉到 Code，而让 Harness 保持尽可能轻薄。

## 关键洞察

- **Fat Skills** 的核心不是提示词堆砌，而是把会反复发生的判断流程固化为 markdown 技能文件，持续复用与迭代。

- **Fat Code** 负责 API 调用、数据处理、校验与自动化执行等确定性逻辑，减少模型在关键路径上的随机性。

- **Thin Harness** 只承担最基础的连接职责，不在框架层堆积推理与业务编排，从而降低系统脆弱性。

- 这套方法强调 **“不做一次性工作”**：手动验证样本后再固化为技能，需要自动运行时再接入定时触发。

- 更强的新模型出现时，技能层可以直接受益，而底层确定性执行层无需大改，系统升级成本更低。

## 提取的概念

- [Agentic Engineering](concepts/Agentic Engineering.md)

- [Thin Harness, Fat Skills](concepts/Thin Harness, Fat Skills.md)

- [Fat Code](concepts/Fat Code.md)

## 原始文章信息

- **作者**：@chenchengpro

- **来源**：X书签

- **发布时间**：2026-04-13

- **原文链接**：[https://x.com/chenchengpro/status/2043697811993350611](https://x.com/chenchengpro/status/2043697811993350611)

## 个人评注

这套分层方式非常贴合 Tizer 当前的内容编译与 Agent 工作流。概念抽取、摘要生成、标签判断这类需要上下文判断的任务，适合沉淀为 Skills；而去重 SQL、属性写回、定时批处理与状态更新，则更适合保留在确定性流程层。这样可以同时提升可复用性、可维护性与后续模型升级收益。
