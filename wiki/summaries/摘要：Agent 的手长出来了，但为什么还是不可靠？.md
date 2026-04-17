---
title: 摘要：Agent 的"手"长出来了，但为什么还是不可靠？
type: summary
tags:
- Agent 技能
- 工作流
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b6881d281b7d9342d1005e6
notion_url: https://www.notion.so/81b0f9105e5044028108a56e3780c0a8
notion_id: 81b0f910-5e50-4402-8108-a56e3780c0a8
---

## 一句话摘要

Agent 真正的可靠性瓶颈，不在于是否接上了 MCP 或更多工具，而在于能否把复杂任务拆成可进化的 Skill 工作流，把确定性步骤硬化为程序逻辑，只把真正需要判断的部分留给 LLM。

## 关键洞察

- 行业的能力获取路径，正在从 Playwright、Selenium 这类“模拟人操作”，演进到 CDP、CLI、RPC 与 MCP 这类更轻量、更标准化的能力层封装。

- MCP 解决的是“能调工具”，并不自动解决“持续做对任务”。生产环境中的低成功率，暴露出验证、回滚、异常处理与经验沉淀仍然缺位。

- 公众号发布流水线案例说明，提升可靠性的关键不是给 Agent 更多自由，而是把大量确定性环节程序化，把少量高价值判断点显式保留给模型。

- CLI 与 MCP 只是能力载体，真正承载可靠性的是 Skill 工作流本身。[SKILL.md](http://skill.md/)、规则沉淀与错误回写，决定了流程是否能越跑越稳。

- 当 Skill 持续进化后，Agent 会从“什么都做”的通用执行者，收敛为关键决策点上的判断引擎。这种专业化不是退化，而是可靠性的起点。

## 提取的概念

- [MCP 协议](concepts/MCP 协议.md)

- [Tool Calling 2.0](concepts/Tool Calling 2.0.md)

- [CLI-Anything](entities/CLI-Anything.md)

- [AutoSkill](concepts/AutoSkill.md)

- [SKILL.md](concepts/SKILL.md.md)

## 原始文章信息

- 作者：Alphana和大船的AI工作区

- 来源：微信

- 发布时间：2026/04/16 09:03

- 原文链接：[点击查看原文](https://mp.weixin.qq.com/s?__biz=Mzg2NzQ4MTI5Nw%3D%3D&mid=2247484183&idx=1&sn=19d63da8469d8144bc75d9b5d96eb2a5&chksm=cf51bf7f2bbc808c4595a0b312c5385bc05ec91b701c72f7c3c5849e96e54a8581348a50997b#rd)

- 源文章页面：Agent 的"手"长出来了，但为什么还是不可靠？

## 个人评注

这篇文章和 Tizer 当前的 HITL 与内容流水线实践高度契合。它提供了一个很清晰的判断框架：底层接入层可以用 CLI、MCP 或 API，但真正决定交付质量的，是不是把规则、校验、失败经验和人工判断边界沉淀成可复用的 Skill 工作流。对 OpenClaw、内容工厂和后续自动化发布链路来说，这意味着要持续缩小“自由发挥区”，扩大“可验证执行区”。
