---
title: 摘要：Google 发布 5 个 Agent Skill 设计模式：告别乱写 SKILL.md 的时代
type: summary
tags:
- Agent 技能
- Coding Agent
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, Cursor, LLM, 自动化
source_article_url: https://www.notion.so/335701074b6881518480fa64a1be5b2d
notion_url: https://www.notion.so/a5b3725cef7c43efa240e13ac153ad74
notion_id: a5b3725c-ef7c-43ef-a240-e13ac153ad74
---

### 一句话摘要

Google 这篇指南的价值，不是发明了新技术，而是把 Agent Skill 设计里常见但混乱的做法系统化成五种可复用模式。

### 关键洞察

- Tool Wrapper、Generator、Reviewer、Inversion、Pipeline 五种模式分别对应专家知识、模板生成、结构化审查、需求澄清和分步执行。

- 它把“怎么写 [SKILL.md](http://skill.md/)”从经验活变成可交流的共同语言。

- 这些模式最大的作用是约束模型边界，而不是给模型更多自由。

- 组合使用不同模式，往往比单一大 prompt 更稳定。

### 提取的概念

- [SKILL.md](concepts/SKILL.md.md)

- [Tool Wrapper 模式](concepts/Tool Wrapper 模式.md)

- [Generator 模式](concepts/Generator 模式.md)

- [Reviewer 模式](concepts/Reviewer 模式.md)

- [Inversion 模式](concepts/Inversion 模式.md)

- [Pipeline 模式](concepts/Pipeline 模式.md)

### 原始文章信息

- 作者：KKaWSB

- 来源：X书签

- 发布时间：未明确披露

- 链接：[原文链接](https://x.com/KKaWSB/status/2034196862794961299)

### 个人评注

这套模式特别适合 Tizer 的知识编译体系，因为它提供了“结构化操作知识”的命名方式。以后遇到工作流文章，可以更稳定地归纳成模式，而不只是碎片技巧。 
