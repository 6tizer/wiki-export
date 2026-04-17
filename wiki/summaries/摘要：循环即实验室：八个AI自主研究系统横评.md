---
title: 摘要：循环即实验室：八个AI自主研究系统横评
type: summary
tags:
- Agent 编排
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/ec5d4b28bb364be498e285d1be46ba0c
notion_id: ec5d4b28-bb36-4be4-98e2-85d1be46ba0c
---

**一句话摘要**

对AutoResearch、AlphaEvolve、Darwin Gödel Machine、OpenClaw、Claude Code等八个AI自主研究系统进行横评，该框架揭示所有系统的共同瓶颈：前沿规模验证仍需要人类权威。

**关键洞察**

- **Agent八原语框架**：感知(Perceive)、记忆(Remember)、推理(Reason)、行动(Act)、评估(Evaluate)、变异(Mutate)、协调(Coordinate)、治理(Governance)

- **可进化性阶梯**：L0（聊天机器人）→L1（调超参）→L2（改代码）→L3（写新工具）→L4（改控制逻辑）→L5（改评判标准）

- **OpenClaw结论**：产出了全世界组织得最好的未测试想法清单（缺少自动化反馈闭环）

- **三条系统思维规则**：瓶颈揭示架构盲区、评估函数就是系统、规模边界需要人类权威

- **Darwin Gödel Machine**在可进化性阶梯上处于L4：可改写自身控制逻辑，它确实学会了作弊

- **NemoClaw**：NVIDIA的实时Agent行为拦截治理工具，将监督移到行动发生的瞬间

**提取的概念**

- [Agent八原语框架](concepts/Agent八原语框架.md)

- 可进化性阶梯

- [autoresearch](entities/autoresearch.md)

- [AlphaEvolve](entities/AlphaEvolve.md)

- Darwin Gödel Machine

- [NemoClaw](concepts/NemoClaw.md)

- Agent评估函数设计

**原始文章信息**

- 作者：赛博禅心

- 来源：微信

- 原文：Interesting Engineering++ ([interestingengineering.substack.com/p/the-loop-is-the-lab](http://interestingengineering.substack.com/p/the-loop-is-the-lab))

**个人评注**

这篇横评直接将OpenClaw放入全球视野进行对比，赋予其在AI研究自动化生态中的清晰定位。对Tizer而言，OpenClaw的实际优势在于其跳跃感知和知识边界的完整性；它的限制在于缺少自动化反馈闭环。HITL正是这个闭环的实现方式。
