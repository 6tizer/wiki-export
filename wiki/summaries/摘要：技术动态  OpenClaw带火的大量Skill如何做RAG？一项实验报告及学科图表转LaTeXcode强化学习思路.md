---
title: 摘要：技术动态 | OpenClaw带火的大量Skill如何做RAG？一项实验报告及学科图表转LaTeXcode强化学习思路
type: summary
tags: []
status: 已审核
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: https://www.notion.so/346701074b68817f81cfe3dc0a791209
notion_url: https://www.notion.so/Tizer/d9eaa1c410064549991f91e1c6c73889
notion_id: d9eaa1c4-1006-4549-991f-91e1c6c73889
---

## 一句话摘要

这篇文章用两个案例说明，面向 Agent 技能库与科学图表代码生成的关键突破都不在“更大模型”本身，而在于更完整的检索对象、更精细的数据构造，以及围绕任务目标设计的训练与奖励闭环。

## 关键洞察

- SkillRouter 证明，在大规模 Skill 检索里，真正决定路由精度的是技能实现体（body）中的执行逻辑、接口约束与处理流程，而不只是名称和描述。

- 面向技能路由的提升路径是“全文本检索 + 交叉重排 + Agent 注入”的工程闭环：先召回，再精排，最后只把必要的技能信息暴露给 Agent。

- 检索模型微调的核心不只是增加样本量，而是做好难负样本挖掘与假阴性过滤，避免模型被错误负样本带偏。

- SciTikZ 展示了“数据引擎先行”的路线：通过原始 TikZ 聚合、自动修复、质量裁判与课程筛选，把图表转代码任务做成可训练的问题。

- DSC-RL 说明，视觉一致性与代码一致性可以同时作为强化学习信号，把“图像是否画对”和“代码是否真正等价”绑定到一起优化。

## 提取的概念

- [SkillRouter](concepts/SkillRouter.md)

- [SkillsBench](concepts/SkillsBench.md)

- [难负样本挖掘](concepts/难负样本挖掘.md)

- [假阴性过滤](concepts/假阴性过滤.md)

- [SciTikZ](entities/SciTikZ.md)

- [DSC-RL](concepts/DSC-RL.md)

- [CrystalBLEU](concepts/CrystalBLEU.md)

## 原始文章信息

- 作者：开放知识图谱

- 来源：微信（转载公众号｜老刘说NLP）

- 发布时间：2026-04-18

- 原文链接：[查看原文](https://mp.weixin.qq.com/s?__biz=MzU2NjAxNDYwMg%3D%3D&mid=2247511178&idx=1&sn=c896eaafa5103282215bb5be4bba7cc3&chksm=fd9d22ba84f00affb289216b0bdc44ffeca8d246c470614a4977b0083697c66102dc2c006b52#rd)

## 个人评注

对 Tizer 当前的 OpenClaw / Skill 体系来说，这篇文章最大的启发是：当技能数量持续增长时，知识管理不应只沉淀“技能名录”，而要沉淀足够可检索的实现上下文，否则 Skill RAG 很容易停留在表层匹配。另一条线索则提醒我们，在内容流水线里，图表、示意图、结构化视觉表达也可以被纳入可编译、可回放、可强化的数据资产，这对后续文档自动化与知识再生产都很有参考价值。
