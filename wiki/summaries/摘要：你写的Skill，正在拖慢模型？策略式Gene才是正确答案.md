---
title: 摘要：你写的Skill，正在拖慢模型？策略式Gene才是正确答案
type: summary
tags:
- Agent 编排
- Coding Agent
status: 已审核
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b6881cba7a5da6e308f3bad
notion_url: https://www.notion.so/373acddf6cc0489787858eb89f290682
notion_id: 373acddf-6cc0-4897-8785-8eb89f290682
---

## 一句话摘要

EvoMap 团队提出的 **Gene** 证明：让 Agent 变强的关键，不是把经验写成更长的 Skill 文档，而是把经验压缩成高控制密度、可匹配、可进化的策略对象。

## 关键洞察

- 同一份底层经验被分别做成约 2,500 token 的 Skill 与约 230 token 的 Gene 时，**Gene 在受控实验中稳定优于完整 Skill，且完整 Skill 甚至可能低于无指导基线**。

- 真正对模型执行有效的，不是给人看的完整说明，而是能直接约束下一步行为的 **strategy** 与 **AVOID 警告**。

- Gene 不是单纯的“短 Prompt”，而是可被匹配、变异、验证与继承的对象；GEP 协议把它进一步升格为可持续进化的协议层载荷。

- CritPt 的端到端结果说明：即使不更新模型参数，只靠 Gene 池与进化引擎，也能把同一基模的表现显著抬升。

- 这套思路对 Tizer 的工作流很有启发：与其不断堆更长的 Skill/说明文档，不如沉淀成更短、更强约束、更易复用的策略资产。

## 提取的概念

- [Gene](concepts/Gene.md)

- [GEP 协议](concepts/GEP 协议.md)

- [Evolver](entities/Evolver.md)

- [Procedural Skill](concepts/Procedural Skill.md)

- [AVOID 警告](concepts/AVOID 警告.md)

- [CritPt](entities/CritPt.md)

## 原始文章信息

- 作者：机器之心

- 来源：微信

- 发布时间：2026-04-21 18:14（Asia/Shanghai）

- 原文链接：[https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2651029194&idx=1&sn=74444aa55fa4caff4666f024133d1896&chksm=8556a7658823460534cdb2c17157b616b7b4dc1061276c088fe77b3338d30db85b2e60109ba7#rd](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651029194&idx=1&sn=74444aa55fa4caff4666f024133d1896&chksm=8556a7658823460534cdb2c17157b616b7b4dc1061276c088fe77b3338d30db85b2e60109ba7#rd)

## 个人评注

这篇文章实际上是在重新定义“经验资产”的最小有效形态。对 Tizer 当前围绕 OpenClaw、内容工厂、HITL 与多 Agent 编排的实践来说，最值得吸收的不是某个单点技巧，而是把可复用经验沉淀成 **策略对象** 而非 **长文档**：让模型在执行瞬间拿到最关键的触发信号、步骤约束与禁止项，才能真正提升稳定性与复用效率。
