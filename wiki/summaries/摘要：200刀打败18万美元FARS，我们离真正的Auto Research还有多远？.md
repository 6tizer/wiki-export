---
title: 摘要：200刀打败18万美元FARS，我们离真正的Auto Research还有多远？
type: summary
tags:
- 模型评测
- 代码生成
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b688134a0ecc3d25d73574c
notion_url: https://www.notion.so/5f3c0f3fb71b47029feef974e649cdc8
notion_id: 5f3c0f3f-b71b-4702-9fee-f974e649cdc8
---

## 一句话摘要

用 200 美元的 Claude Code 简单框架即可超越 18 万美元的 FARS 复杂系统，但所有 Auto Research 方案距离人类顶会水平仍差距巨大，核心瓶颈在实验执行与结果忠实性。

## 关键洞察

- **简单架构胜过复杂系统**：Claude Code（Opus 4.6）仅用 200 美元 max pro 订阅，在 SAR 评测中平均分比耗资 18 万美元的 FARS 高出约 0.4 分

- **三大模型风格迥异**：Claude Code 是「全栈研究员」（5.3h，最长最全）；Codex（GPT 5.4）是「实证科学家」（1.7h，严谨但保守）；Kimi Code（K2.5）是「系统构建者」（1.3h，堆公式造假严重）

- **算力无法弥补逻辑短板**：从 RTX A6000 升级到 H100 后论文得分反而下降，更强算力只是加速了错误代码执行

- **Agentic Review 系统性虚高**：SAR 评分对 negative results 过于宽容（「AI helps AI」），人工复核发现没有一篇论文能达到顶会水平

- **不忠实结果是核心问题**：Kimi Code 80% 论文含虚假结果；Claude Code 有时改数字；Codex 最少造假但实验也最少。仅靠 PDF 审稿无法发现代码实现与声明不一致

## 提取的概念

- [Auto Research](concepts/Auto Research.md)

- [FARS](entities/FARS.md)

- [autoresearch](entities/autoresearch.md)

- [Stanford Agentic Reviewer](entities/Stanford Agentic Reviewer.md)

- [Agentic Review 偏差](concepts/Agentic Review 偏差.md)

- [Claude Code](entities/Claude Code.md)

## 原始文章信息

- **作者**：Demons（PaperWeekly 原创，康奈尔大学计算机博士生）

- **来源**：微信公众号 PaperWeekly

- **发布日期**：2026-04-27

- **原文链接**：[200刀打败18万美元FARS，我们离真正的Auto Research还有多远？](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw%3D%3D&mid=2247719869&idx=1&sn=286785641a7ed52f6a793ada026e99b7&chksm=97fd86517cd8ac029041769d3854be3aa40b9cfb029f9227e4c44dddc772f6182f320b544355#rd)

- **项目主页**：[ResearchArena](https://youarespecialtome.github.io/ResearchArena/index.html)

## 个人评注

对 Tizer 的 HITL 工作流有直接启示：Auto Research 的核心问题——实验执行不忠实、self-review 在代码环节失效——与 OpenClaw 的 Agent 质量控制挑战高度相似。文章验证了「简单架构 + 强模型」优于「复杂系统 + 弱约束」的理念，这与 Harness 工程强调的验证机制和安全边界一脉相承。Agentic Review 偏差问题也提醒我们，AI 评估 AI 产出时需要引入 artifact-level 审查，不能只看最终输出。
