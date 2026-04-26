---
title: TuriX Parallelum
type: concept
tags:
- Agent 协作模式
- 多Agent协作
status: 草稿
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/6114e2d8a71d44c69537c9b613aefa30
notion_id: 6114e2d8-a71d-44c6-9537-c9b613aefa30
---

## 定义

TuriX Parallelum 是 TuriX-CUA 的四角色协同架构，通过 Planner、Brain、Evaluator、Executor 的分工，把桌面 GUI 任务拆成规划、决策、评估、执行四个环节，并让相邻步骤并行推进。

## 关键要点

- 用角色拆分来降低长链路 GUI 操作中的上下文混乱

- Evaluator 检查上一步时，Executor 可以继续执行下一步，在成功率与速度之间取得平衡

- 这种并行流水线尤其适合需要持续观察屏幕反馈的桌面自动化任务

## 来源引用

- [摘要：让 AI 接管你的电脑！这个 Agent 凭什么 2.3K Stars 还在涨](summaries/摘要：让 AI 接管你的电脑！这个 Agent 凭什么 2.3K Stars 还在涨.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzk2NDMzMDY3OA%3D%3D&mid=2247484301&idx=1&sn=4d6110b4360d9b2b2b928651b476655a&chksm=c5575f8328dc1444d94c8af751859872f63422f37f65fed3f718380ab623bbed58f684d915f2#rd)）

## 关联概念

- [Turix CUA](entities/Turix CUA.md)

- [Computer Use](concepts/Computer Use.md)

- [Agent Skills](concepts/Agent Skills.md)
