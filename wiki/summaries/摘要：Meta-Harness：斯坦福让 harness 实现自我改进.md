---
title: 摘要：Meta-Harness：斯坦福让 harness 实现自我改进
type: summary
tags:
- Harness 工程
- OpenClaw
- Agent 协作模式
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Harness, Research, Agent
source_article_url: ''
notion_url: https://www.notion.so/Tizer/7fe93720ca734f3abae4cfe34a14bdbb
notion_id: 7fe93720-ca73-4f3a-bae4-cfe34a14bdbb
---

## 一句话摘要

斯坦福研究提出 Meta-Harness，通过让 Coding Agent 访问完整历史记录自主迭代改进 Harness，在文本分类上超过人工最佳方案7.7个百分点，开启了「让 AI 自己设计 Harness」的新篇章。

## 关键洞察

- **三步循环**：翻档案（读完整历史）→ 跑评估（收集成绩和 trace）→ 存档（写回文件系统）

- **完整历史至关重要**：只给分数 34.6% → 分数+摘要 34.9% → 完整文件系统 50.0%

- **多个基准超越人工方案**：TerminalBench-2 达76.4%，超过 Terminus-KIRA（74.7%），搜索平均读历史文件量82个

- **至关重要的诺言**：Harness 优化无法创造权重中不存在的能力，只能释放未被利用的潜力

- **人类仔然不可替代**：proposer 仍需要人类定义的搜索技能、评估指标和文件系统组织方式

## 提取的概念

- Meta-Harness

## 原始文章信息

- **作者**: AGI Hunt

- **来源**: 微信公众号

- **发布时间**: 2026-03-31

- **论文**: [https://yoonholee.com/meta-harness/paper.pdf](https://yoonholee.com/meta-harness/paper.pdf)

## 个人评注

Meta-Harness 对 Tizer 的工作流设计有重要启示：可以在 OpenClaw 工作流中尝试让 Agent 自主迭代优化 Harness，而不是靠人工一读调参。
