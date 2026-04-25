---
title: 摘要：凌晨3点，硅谷炸锅！Anthropic源码意外泄露，51万行代码揭露Claude惊天野心
type: summary
tags:
- Agent 框架
- 商业/生态
status: 已审核
confidence: medium
last_compiled: '2026-04-25'
source_tags: ''
source_article_url: https://www.notion.so/34d701074b6881158387c2233b144e50
notion_url: https://www.notion.so/77fcf7be8b00490f9da944a7bdd64dc3
notion_id: 77fcf7be-8b00-490f-9da9-44a7bdd64dc3
---

## 一句话摘要

Anthropic 因 source map 泄露意外暴露了 Conway 等内部项目，显示 Claude 正从对话式助手演进为具备后台常驻、事件唤醒、扩展机制与跨设备延续能力的长期运行智能体平台。

## 关键洞察

- 泄露的 51.2 万行 TypeScript 代码揭示，Anthropic 关注点不再是“更会聊天”，而是“持续替人完成任务”。

- Conway 体现的是常驻智能体范式：关闭窗口后仍可在后台运行，由外部事件触发执行并通过系统通知回报结果。

- 代码中的 Extensions 区域与 `.cnw.zip` 格式表明 Anthropic 正尝试把 Claude 做成可安装、可扩展的 Agent 平台，而非单一助手。

- 从 Claude Code、[Claude Cowork](entities/Claude Cowork.md)、Claude Dispatch 到 [Claude Managed Agents](entities/Claude Managed Agents.md)，Anthropic 的产品路线逐步补齐本地执行、持久线程、托管运行与平台化能力。

- 这类 [Agent 操作系统层](concepts/Agent 操作系统层.md) 一旦落到用户设备和工作流层，价值与风险会同时放大：效率提升与权限/安全暴露并存。

## 提取的概念

- [Conway](entities/Conway.md)

- [常驻智能体](concepts/常驻智能体.md)

- [Agent 扩展生态](concepts/Agent 扩展生态.md)

- [Claude Dispatch](entities/Claude Dispatch.md)

- [Claude Cowork](entities/Claude Cowork.md)

- [Claude Managed Agents](entities/Claude Managed Agents.md)

- [Agent 操作系统层](concepts/Agent 操作系统层.md)

## 原始文章信息

- 作者：新智元

- 来源：微信

- 发布时间：2026-04-25 08:18

- 原文链接：[查看原文](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652695027&idx=2&sn=95c7c69c2170bdfcc5acec870d14cd59&chksm=f0e3f5d6d7d4b599e156421a54e77bfae306b7fb7b21299b37c7ddcf43d8de24ef5723b0a15c#rd)

- 源文章页：凌晨3点，硅谷炸锅！Anthropic源码意外泄露，51万行代码揭露Claude惊天野心

## 个人评注

这篇文章对 Tizer 的启发不在“Claude 又更新了什么”，而在于 Agent 产品竞争已经从 prompt 体验转向运行时设计：谁能把触发器、长期状态、工具权限和回执机制串成稳定工作流，谁就更接近真正的内容流水线与 HITL 操作系统。对 OpenClaw / 内容编译链路而言，后台常驻、事件唤醒、扩展生态与安全边界会是下一阶段必须同步思考的四个维度。
