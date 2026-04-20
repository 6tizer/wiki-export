---
title: 摘要：Google Deepmind论文解读：如何给AI Agent 投毒
type: summary
tags:
- 安全/隐私
- Agent 编排
status: 已审核
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: https://www.notion.so/348701074b68811c964bcf4acd27149e
notion_url: https://www.notion.so/ce548a09318c4f098821b023148c3ea7
notion_id: ce548a09-318c-4f09-8821-b023148c3ea7
---

## 一句话摘要

这篇文章系统梳理了 AI Agent 在感知、推理、记忆、行动、多 Agent 协作与人在回路六个层面的安全陷阱，指出攻击者无需破解模型本身，只要操纵 Agent 所处环境，就可能把 Agent 变成攻击用户的工具。

## 关键洞察

- Agent 的核心脆弱性来自“感知鸿沟”：人类看到的是界面，Agent 读取的是 HTML、元数据、像素与结构化上下文，因此隐藏指令更容易绕过人的直觉判断。

- 论文把攻击面总结为六类陷阱：内容注入、语义操控、认知状态、行为控制、系统性陷阱与人在回路陷阱，覆盖从单次干扰到长期投毒、从单 Agent 到多 Agent 生态的完整链路。

- 真正危险的不只是单点攻击，而是链式组合：隐藏指令可先解除对齐，再诱发越权操作、数据外发，最后通过记忆或知识库投毒把影响长期化。

- 多 Agent 生态的同质性会把局部攻击放大为系统性风险，例如拥塞、级联反应、感染性越狱与群体共谋。

- 防御不能只靠模型对齐，还需要训练期对抗强化、运行时内容扫描与行为监控，以及内容可信度、责任归属等生态层治理。

## 提取的概念

- [间接提示注入](concepts/间接提示注入.md)

- [动态伪装](concepts/动态伪装.md)

- [知识库投毒](concepts/知识库投毒.md)

- [潜伏记忆投毒](concepts/潜伏记忆投毒.md)

- [数据窃取陷阱](concepts/数据窃取陷阱.md)

- [子 Agent 生成陷阱](concepts/子 Agent 生成陷阱.md)

- [人格超信念](concepts/人格超信念.md)

## 原始文章信息

- 作者：@vista8

- 来源：X书签

- 发布时间：2026-04-20

- 原文链接：[https://x.com/vista8/status/2046038788582088830](https://x.com/vista8/status/2046038788582088830)

- 源文章页面：Google DeepMind「AI Agent 陷阱」论文解读：六类攻击，让你的 AI 助手反咬你一口

## 个人评注

这篇材料对 Tizer 当前的 Agent 工作流很有参考价值：一方面，任何带浏览、检索、记忆、外发能力的 Agent 都要把“环境即攻击面”当成默认前提；另一方面，在 OpenClaw、HITL 审批和内容流水线场景中，应优先建立输入分级、动作确认、来源隔离和异常暂停机制，避免把高权限自动化直接暴露在不可信上下文里。
