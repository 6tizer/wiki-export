---
title: AI-Gated Grey Rollout
type: concept
tags:
- Harness 工程
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/bb272d4be5f94f81af609c57fb474e26
notion_id: bb272d4b-e5f9-4f81-af60-9c57fb474e26
---

## 定义

AI-Gated Grey Rollout 是一种以 AI 评分系统作为发布门控的灰度部署策略。当 Agent 系统发生重大变更（如模型替换、系统提示重写、工具权限扩展）时，将少量真实流量路由到新版本，由 Grader 实时对比评分决定是否逐步扩大流量，无需 staging 环境或人工审批。

该方法作为 Self-Healing Agent Harness 的第三个组件（The Bridge），在 CREAO 平台生产环境运行。

## 关键要点

- 初始切片通常为 10% 真实流量，路由到新变体

- Grader 对新旧版本进行实时 head-to-head 评分对比

- 晋升阶梯自动运行：5% → 20% → 50% → 100%，每步都有统计门控

- 失败条件：面板平均分下降 ≥0.15（p<0.05，最少 200 次交互窗口），或确定性 Bug 检测器发现新错误集群尖峰

- 失败后自动回滚流量到稳定版本，并开 Linear 工单进入工程流水线

- 用真实用户流量验证安全性，爆炸半径由队列大小封顶

- 替代了传统的 staging 环境和 "looks good to me" 式的 PR 审批

## 与传统灰度的区别

- 传统灰度（canary/blue-green）依赖人工观察指标和手动晋升

- AI-Gated 版本由 Agent 自身的评分系统自动决策，形成闭环

- 失败的发布直接变成 Engineering Pipeline 的输入，关闭了「即将发布的 Bug」这一缺口

## 关联概念

- [Self-Healing Agent Harness](concepts/Self-Healing Agent Harness.md)

- [Tri-Judge Panel](concepts/Tri-Judge Panel.md)

- [Agent Harness](concepts/Agent Harness.md)

- [CREAO](entities/CREAO.md)

## 来源引用

- [摘要：The Self-Healing Agent Harness](summaries/摘要：The Self-Healing Agent Harness.md)（[原文](https://x.com/intuitiveml/status/2048912026018484317)）
