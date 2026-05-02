---
title: 摘要：这套题，GPT-5.5、Opus 4.7加起来没考到「1分」，人类却拿了满分100？
type: summary
tags:
- 模型评测
status: 已审核
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: https://www.notion.so/354701074b6881109a07dea84b4ab3b8
notion_url: https://www.notion.so/Tizer/5e6d9e55c8254cd698496abcaf5a60d9
notion_id: 5e6d9e55-c825-4cd6-9849-6abcaf5a60d9
---

## 一句话摘要

ARC Prize 发布的 ARC-AGI-3 基准测试显示，GPT-5.5 和 Claude Opus 4.7 在面对全新交互式逻辑环境时得分均低于 1%，而人类首次接触即可满分通过，揭示了当前顶尖模型在抽象推理能力上与人类智能之间的巨大鸿沟。

## 关键洞察

- **人机差距悬殊**：人类 100% vs GPT-5.5 的 0.43% / Claude Opus 4.7 的 0.18%，千亿参数模型在「全新逻辑环境」中的表现不如 6 岁儿童

- **三大失败模式**：研究团队从 160 组运行轨迹中提炼出核心失败原因——局部反馈无法构建全局世界模型、训练数据锚定导致误判、通关不等于理解

- **两种不同的「翻车姿势」**：Claude Opus 4.7 像「过度自信的直觉主义者」，将观察压缩为自信但错误的理论；GPT-5.5 像「思维发散的理论家」，无法完成压缩，始终停留在分散的可能性中

- **ARC-AGI-3 的设计哲学**：135 个交互式环境，刻意剥离文化知识，只保留探索、假设验证、持续学习等核心智能维度

- **「压缩」能力是关键区分**：Opus 压缩错了（false compression），GPT-5.5 压缩不了（no compression），两者都未达到人类水平的正确压缩

## 提取的概念

- [ARC-AGI-3](concepts/ARC-AGI-3.md)：第三代抽象推理基准，交互式环境设计，人类满分而所有前沿模型低于 1%

- [ARC Prize](entities/ARC Prize.md)：由 François Chollet 创立的研究组织，发布 ARC-AGI 系列基准

- [ARC-AGI-2](concepts/ARC-AGI-2.md)：前代基准，静态网格推理，本文用于对比说明 ARC-AGI-3 的架构升级

## 原始文章信息

- **作者**：机器之心编辑部

- **来源**：微信公众号

- **发布时间**：2026-05-02

- **原文链接**：[机器之心](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651031297&idx=1&sn=41368039c5bd521303caf995c14d0d01&chksm=8594815c5485420133d6dd0824d6f62510d0b99d6e342f45d94bb16a5fa61c1407b536f9b580#rd)

- **参考来源**：[ARC Prize 官方博客](https://arcprize.org/blog/arc-agi-3-gpt-5-5-opus-4-7-analysis)、[François Chollet 推文](https://x.com/fchollet/status/2050328852107612559)

## 个人评注

ARC-AGI-3 的结果对 Tizer 的工作有两层启示：（1）当前 AI Agent 在面对真正「未知」的任务时仍然脆弱，OpenClaw 的 Harness 设计需要考虑模型在新环境中的「虚假世界模型」问题——Agent 可能看起来在执行正确操作，实际上只是在用错误的抽象模型碰运气；（2）「训练数据锚定效应」提醒我们，在内容自动化管线中，LLM 对已知模式的过度依赖可能导致对新类型内容的误分类。这也印证了 HITL（Human-in-the-Loop）在 Agent 系统中不可或缺的地位。
