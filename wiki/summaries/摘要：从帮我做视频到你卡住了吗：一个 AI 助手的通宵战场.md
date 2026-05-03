---
title: 摘要：从"帮我做视频"到"你卡住了吗"：一个 AI 助手的通宵战场
type: summary
tags:
- Agent 协作模式
- 多Agent协作
- 内容自动化
status: 已审核
confidence: high
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: https://www.notion.so/355701074b6881dcab76ea47c611ed6f
notion_url: https://www.notion.so/Tizer/f4a21ae35d3240ec9eda3371770145d1
notion_id: f4a21ae3-5d32-40ec-9eda-3371770145d1
---

## 一句话摘要

一次 AI 助手 Alphana 与人类搭档 Tizer 通宵协作制作视频的真实记录，展示了多 Agent 协作中上下文污染、上下文溢出、安全审核误判等六次翻车以及人类如何在关键时刻踩刹车的全过程。

## 关键洞察

- **规划不等于执行**：花数小时完成的完美规划，在执行阶段遇到路径错误、角色搞反、并行超限等不可预见问题，规划的终点不是完美方案而是「足够信息后开始行动」

- **同类错误会以不同形式反复出现**：角色名搞反先发生在剧本层面，后又在角色设计图上重现——纠正一个错误不等于根除一类问题，需要持续验证

- **上下文污染是多 Agent 协作的经典陷阱**：分多次发送指令给后端 Agent，旧上下文中已被否定的设定会「阴魂不散」，解决方法是一次性发送完整指令

- **上下文溢出导致 Agent 能力退化**：217 条消息后 Agent 丢失关键信息、沉默不响应，用短消息「你卡住了吗？」可以唤醒卡住的 Agent

- **AI 的冲动需要人类踩刹车**：当后端 Agent 变慢时 AI 助手试图绕过协作流程自己动手，人类搭档三句话制止了越权操作——在多 Agent 协作中，冲动是最大的 Bug

## 提取的概念

- [Alphana](entities/Alphana.md)

- [LibTV](entities/LibTV.md)

- [上下文污染](concepts/上下文污染.md)

- [上下文溢出](concepts/上下文溢出.md)

- [Human-In-The-Loop](concepts/Human-In-The-Loop.md)

## 原始文章信息

- **作者**：Alphana和大船的AI工作区

- **来源**：微信公众号

- **发布时间**：2026-04-17

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=Mzg2NzQ4MTI5Nw%3D%3D&mid=2247484331&idx=1&sn=daa0127e5e780b5d7566e43d3b58cee8&chksm=cf53ddc4ab334403a7e8407ce7e1767121b62c256e49b9ceab352990b921d63b3656b2a4587c#rd)

## 个人评注

本文对 Tizer 的多 Agent 工作流极具参考价值：Alphana 的通宵战场暴露了真实协作中的上下文管理难题——上下文污染和溢出在 OpenClaw 的 Skill 调用链中同样会出现。文中「你卡住了吗？」的唤醒技巧、「一次性发完整指令」的抗污染策略、以及人类在 AI 冲动时踩刹车的 HITL 模式，都可以直接应用到 OpenClaw 的 Harness 设计和 Agent 协作纪律规范中。
