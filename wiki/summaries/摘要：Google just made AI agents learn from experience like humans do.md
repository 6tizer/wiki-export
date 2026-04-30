---
title: 摘要：Google just made AI agents learn from experience like humans do.
type: summary
tags:
- 长期记忆
- 推理优化
status: 已审核
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: https://www.notion.so/352701074b688179b747ff41bdec1b8b
notion_url: https://www.notion.so/Tizer/dff60a8a0f1f4ff2abd3bc8fdfdad7ca
notion_id: dff60a8a-0f1f-4ff2-abd3-bc8fdfdad7ca
---

## 一句话摘要

Google 提出 ReasoningBank 框架，让 AI Agent 通过外挂记忆层从每次任务的成功与失败中持续学习，无需重新训练即可逐周期提升表现。

## 关键洞察

- ReasoningBank 将每次任务执行蒸馏为「策略卡片」，成功变剧本、失败变陷阱，下次任务前检索最相关卡片指导行动

- 工作流极简：执行任务 → 标注结果 → 提取经验 → 存入记忆库 → 下次匹配检索

- 在 WebArena 上成功率提升 8.3%，在 SWE-Bench Verified 上提升 4.6%，执行步骤减少约 3 步

- 搭配 MaTTS（Memory-aware Test-Time Scaling）后收益进一步复合增长

- 无需标注数据、无需微调，模型权重不变，仅靠记忆层即可让行为逐周期优化

## 提取的概念

- [ReasoningBank](concepts/ReasoningBank.md)

- [MaTTS](concepts/MaTTS.md)

- [SWE-Bench Verified](entities/SWE-Bench Verified.md)

## 原始文章信息

- 作者：@AlphaSignalAI

- 来源：X书签

- 发布时间：2026-04-30

- 原文链接：[https://x.com/AlphaSignalAI/status/2049821506515968132](https://x.com/AlphaSignalAI/status/2049821506515968132)

- 论文链接：[arXiv:2509.25140](https://arxiv.org/abs/2509.25140)

- 源文章页面：ReasoningBank：让 AI Agent 像人类一样从经验中学习

## 个人评注

- 「失败也入库」的记忆思路与 OpenClaw 的经验沉淀方向高度契合：不只记住成功路径，更要把踩坑记录编译为可检索的规避策略

- 策略卡片模式可以启发 HITL 流水线的迭代机制——每一轮人工审核反馈都可以蒸馏为下一轮自动编译的改进规则

- MaTTS 的「多花算力产出更多元经验→更好记忆→更好推理」正反馈循环，是 test-time compute scaling 的又一个实证
