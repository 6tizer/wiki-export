---
title: 摘要：Claude强到不敢发的Mythos，被质疑用了字节Seed技术
type: summary
tags:
- 推理优化
- 链上协议
- 模型评测
status: 已审核
confidence: medium
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: https://www.notion.so/341701074b688191bdeef7c3aa860a74
notion_url: https://www.notion.so/Tizer/1f02778b434f47ab94561e940f3b019e
notion_id: 1f02778b-434f-47ab-9456-1e940f3b019e
---

## 一句话摘要

文章基于 GraphWalks BFS、token 使用效率与网络安全表现三条线索，推测 Claude Mythos 可能采用了类似字节 Seed 论文提出的 LoopLM 循环语言模型架构。

## 关键洞察

- Mythos 在 GraphWalks BFS 这类图遍历任务上的异常领先，被文章视为“架构创新”而非普通 Scaling Law 延伸的信号。

- 循环语言模型的关键不是输出更长推理，而是在潜空间内部进行多步迭代，并按题目难度动态分配计算。

- 文中借助 Ouro 实验结果说明，循环式预训练可能让较小参数模型在复杂推理任务上逼近更大传统模型。

- 文章区分了“知识存储”和“知识操作”，并认为循环架构真正放大的，是对已有知识做搜索、组合与多跳推理的能力。

- Mythos 在 CyberGym 与漏洞发现上的突出表现，也被作者拿来作为其可能具备循环式图遍历偏置的旁证。

## 提取的概念

- [Claude Mythos](entities/Claude Mythos.md)

- [LoopLM](concepts/LoopLM.md)

- [GraphWalks BFS](concepts/GraphWalks BFS.md)

- [RLVR](concepts/RLVR.md)

- [知识操作](concepts/知识操作.md)

- [Ouro](entities/Ouro.md)

## 原始文章信息

- 作者：量子位

- 来源：微信

- 发布时间：2026-04-13T12:24:00.000+08:00

- 原文链接：[查看原文](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247882749&idx=1&sn=2c5b489ce91054109b22b36188b08e7d&chksm=e912871f3bcec6edb33f9d3bbe2448cd2e302161209286bca16ddf778484c2f0d06c176fa3a7#rd)

## 个人评注

这篇文章对 Tizer 的价值，不在于立刻确认 Mythos 真实架构，而在于提供了一个可复用的判断框架：当模型在特定任务上出现“异常尖峰”时，可以优先从归纳偏置与架构变化，而不是只从参数规模或训练数据解释。对后续 HITL 选题、OpenClaw 架构观察和内容流水线中的“新模型机制卡片化”都很有参考意义。
