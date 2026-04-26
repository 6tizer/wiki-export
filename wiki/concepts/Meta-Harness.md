---
title: Meta-Harness
type: concept
tags:
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/6863f6d87e3947b3b2291dc2bd3b8c50
notion_id: 6863f6d8-7e39-47b3-b229-1dc2bd3b8c50
---

## 定义

Meta-Harness 是斯坦福研究提出的自动化 Harness 设计方法：把 Harness 优化本身也变成一个 Harness，让 Coding Agent 通过访问完整历史记录自主搜索和改进 Harness 设计，替代人类工程师手工调参。

## 核心机制

三步循环迭代：

1. **翻档案**：Coding Agent（Claude Code + Opus 4.6）读取文件系统中所有历史记录（Harness 源码、评估分数、执行 trace）

1. **跑评估**：新 Harness 跑实际任务，收集成绩和 trace

1. **存档**：所有产物写回文件系统供下一轮查阅

**关键设计**：给 proposer 完整文件系统访问权限，而非压缩摘要

## 性能表现

- 文本分类：比人工最佳方案 ACE 高7.7个百分点，context 用量仅 ACE 四分之一

- 数学推理：自动发现的检索策略在5个未见过的模型上平均提升4.7个百分点

- TerminalBench-2：76.4% 通过率，超过人工精心调教的 Terminus-KIRA（74.7%）

## 完整历史的价值

消融实验：只给分数 34.6% → 分数+摘要 34.9% → 完整文件系统 **50.0%**

压缩信息不只是损失边角细节，而是丢掉了做出正确决策所需的关键线索。

## 两个边界

1. 模型能力天花板：Harness 优化无法创造权重中不存在的能力，只能释放未被利用的潜力

1. 泛化性：在9个未见过的数据集上测试，平均准确率73.1%，超过所有基线

## 关联概念

- [Harness Engineering](concepts/Harness Engineering.md)

- [长时程信用分配](concepts/长时程信用分配.md)

- [Terminal-Bench 2.0](entities/Terminal-Bench 2.0.md)

- [Agent 持续学习三层框架](concepts/Agent 持续学习三层框架.md)

- [Agent Traces](concepts/Agent Traces.md)

## 来源引用

- [摘要：Meta-Harness：斯坦福让 harness 实现自我改进](summaries/摘要：Meta-Harness：斯坦福让 harness 实现自我改进.md)

- [原文链接](https://x.com/yoonholeee/status/2044442372864700510)｜《Meta-Harness 代码开源：让 Agent 在新领域自主优化 Harness》｜来源条目：[摘要：Meta-Harness 代码开源：让 Agent 在新领域自主优化 Harness](summaries/摘要：Meta-Harness 代码开源：让 Agent 在新领域自主优化 Harness.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw%3D%3D&mid=2247523832&idx=1&sn=8a7013894ddc0668c0f1c9f935599450&chksm=c1b17f5bd2d0ca49ee848d1dc13c14fb122c8f551ba00b307b566dfa7edc4c20a52573051f79#rd)｜《字节最火的开源Agent项目，如何思考Agent的自我进化？》｜来源条目：[摘要：字节最火的开源Agent项目，如何思考Agent的自我进化？](summaries/摘要：字节最火的开源Agent项目，如何思考Agent的自我进化？.md)
