---
title: 摘要：The Self-Healing Agent Harness
type: summary
tags:
- Harness 工程
- 模型评测
status: 已审核
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: https://www.notion.so/351701074b688194917aeefacc6a1bea
notion_url: https://www.notion.so/Tizer/cadcfb30f077400e90dfb9f3dde5038b
notion_id: cadcfb30-f077-400e-90df-b9f3dde5038b
---

## 一句话摘要

CREAO 创始人 Peter Pang 提出将 Agent 评测与 QA 融合为同一自愈闭环（评分→分诊→修复→验证→发布门控），取代传统人工 QA、staging 环境和手动发布审批，实现每日 3-8 次生产部署。

## 关键洞察

- **Eval 和 QA 是同一个问题**：对 AI Agent 平台而言，模型回答质量差和产品 Bug 对用户来说无法区分，应在同一流水线中处理

- **评分结果而非路径**（Grade the outcome, not the trajectory）：Agent 常走非线性路径但仍产出正确结果，惩罚路径是低效的评估方式

- **评分无工单等于无效仪表盘**：Grader 没有 Engineering Pipeline 支撑就只是一个没人看的 dashboard；反之亦然。两者必须同时构建

- **Tri-Judge Panel 消除自评偏差**：使用 Anthropic/OpenAI/Google 三个模型家族并行评分，取均值而非投票，将粗糙四级量表转换为可追踪趋势的连续指标

- **AI-Gated Grey Rollout 替代 staging**：将真实流量切片路由到新版本，评分系统实时对比决策是否晋升，失败自动回滚并开工单进入修复流水线

- **按模型差异化采样**：主力模型 10%、少数模型 100%，确保小流量模型也能快速达到统计显著性

## 提取的概念

- [Self-Healing Agent Harness](concepts/Self-Healing Agent Harness.md)

- [Tri-Judge Panel](concepts/Tri-Judge Panel.md)

- [AI-Gated Grey Rollout](concepts/AI-Gated Grey Rollout.md)

- [Agent Harness](concepts/Agent Harness.md)（已有概念，追加引用）

- [CREAO](entities/CREAO.md)（已有实体，追加引用）

## 原始文章信息

- **作者**：Peter Pang (@intuitiveml)

- **来源**：X书签

- **发布时间**：2026-04-27

- **原文链接**：[X 推文](https://x.com/intuitiveml/status/2048912026018484317)

## 个人评注

本文提出的 Self-Healing Agent Harness 是 Harness Engineering 理念的一个高水准生产实践案例。其中「评分即 Bug 报告」的思路与 OpenClaw 内容管道中的质量回路设计思路一致——任何自动化流水线都需要一个闭环反馈机制来持续自我修正。Tri-Judge Panel 的跨家族评分方法可借鉴到 HITL 工作流中用于多视角审核，AI-Gated Grey Rollout 则为 Agent 平台的持续部署提供了一个可操作的模板。
