---
title: 摘要：How to really stop your agents from making the same mistakes
type: summary
tags:
- 知识管理
- Agent 协作模式
- 模型评测
- 长期记忆
- Harness 工程
status: 已审核
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b688149a139c7653dcb5080
notion_url: https://www.notion.so/ec026288fbce439693ce09c3601f55d2
notion_id: ec026288-fbce-4396-93ce-09c3601f55d2
---

## 一句话摘要

Skillify 的核心主张是：把 Agent 的每一次失败都沉淀成可路由、可测试、可长期执行的 Skill，让错误通过结构化约束而不是提示词承诺被永久消除。

## 关键洞察

- LangChain / LangSmith 提供了测试与观测组件，但没有给出“先修什么、按什么顺序修、何时算修完”的工程闭环。

- 作者把 Agent 工作分成需要判断的 latent work 与应当脚本化的 deterministic work，像历史日历检索、时区换算这类任务都应尽量下沉到确定性脚本。

- Skillify 不是单次补丁，而是一套 10 步质量闸门：`SKILL.md`、确定性代码、单元测试、集成测试、LLM eval、resolver trigger、resolver eval、check-resolvable / DRY audit、E2E smoke test、brain filing rules。

- 真正的可靠性来自“让旧错误在结构上不可再发生”，而不是继续依赖更长的 system prompt 或更强的模型临场发挥。

- GBrain 被定位为负责记忆、评测与质量闸门的底座，而 Hermes Agent 提供技能自生成能力，二者结合才接近作者想要的长期演化式 Agent 系统。

## 提取的概念

- [Skillify](concepts/Skillify.md)

- [Thin Harness, Fat Skills](concepts/Thin Harness, Fat Skills.md)

- [Latent vs. Deterministic](concepts/Latent vs. Deterministic.md)

- [Resolver](concepts/Resolver.md)

- [check-resolvable](concepts/check-resolvable.md)

- [GBrain](entities/GBrain.md)

- [Hermes Agent](entities/Hermes Agent.md)

## 原始文章信息

- 作者：@garrytan

- 来源：X书签

- 发布时间：2026-04-22

- 原文链接：[https://x.com/garrytan/status/2046876981711769720](https://x.com/garrytan/status/2046876981711769720)

## 个人评注

这篇文章对 Tizer 当前的知识编译工作流有两个直接启发：第一，像漏编、误分类、重复入库这类问题，不应继续靠提示词临场修补，而应被沉淀成可复用、可测试的处理规则；第二，去重、路由、增量更新与质量检查应该前置为结构化流程，这样知识库才能随着错误积累而变得更稳，而不是越来越脆。
