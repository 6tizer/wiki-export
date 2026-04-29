---
title: Self-Healing Agent Harness
type: concept
tags:
- Harness 工程
- 模型评测
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/21e67201645e4eec8d9599eb9bf8727a
notion_id: 21e67201-645e-4eec-8d95-99eb9bf8727a
---

## 定义

Self-Healing Agent Harness 是一种将模型评测（Evaluation）与质量保证（QA）融合为同一闭环的工程方法论。其核心思想是：对 AI Agent 平台而言，模型回答质量差和产品 Bug 是同一个问题，因此评分系统和工程修复流水线必须串联运行，形成「评分 → 分诊 → 修复 → 验证 → 发布门控」的自愈循环。

该方法论由 CREAO 平台创始人 Peter Pang 提出并在生产环境实践，取代了传统的人工 QA 审核、staging 环境和手动发布审批。

## 关键要点

- 将 Eval 和 QA 视为同一循环：低分即 Bug Report，Bug 修复后重新评分验证

- 三大组件：Grader（三评委面板）、Engineering Pipeline（六步自动修复流水线）、Bridge（AI 门控灰度发布）

- 评分基于结果而非路径（Grade the outcome, not the trajectory）——Agent 的非线性执行路径不应被惩罚

- 评分无工单等于无效仪表盘——评分必须直接驱动工程修复

- 替代了传统的 staging 环境、人工 QA 和手动发布审批流程

- 在 CREAO 平台实现每日 3-8 次生产部署

## 三大组件

### 1. Grader（评分器）

- 异步评分端点，不影响用户延迟

- 使用 Tri-Judge Panel（三模型家族并行评分）

- 按模型差异化采样：主力模型 10%，少数模型 100%

- 12 个领域分类条件化评分标准

### 2. Engineering Pipeline（工程流水线）

六个顺序执行的每日任务：

1. **Detect & Triage**：聚类低分评价，9 维严重性评分

1. **Investigate**：遍历堆栈、日志、最近部署，指派根因

1. **Auto-Fix**：高置信问题自动分支、修复、提交 PR（每轮最多 3 个）

1. **Verify**：查询 CloudWatch 验证修复效果，零出现则关闭工单

1. **Re-grade**：已关闭集群 24 小时内 100% 采样，回归则回滚

1. **Report**：每日摘要推送到 Linear 和团队频道

### 3. Bridge（发布桥）

- 将真实流量的小切片（10%）路由到新版本

- Grader 实时对比基线评分

- 晋升阶梯：5% → 20% → 50% → 100%，每步统计门控

- 评分下降 ≥0.15（p<0.05，≥200 次交互窗口）→ 自动回滚

## 关联概念

- [Tri-Judge Panel](concepts/Tri-Judge Panel.md)

- [AI-Gated Grey Rollout](concepts/AI-Gated Grey Rollout.md)

- [Agent Harness](concepts/Agent Harness.md)

- [CREAO](entities/CREAO.md)

- [Harness Engineering](concepts/Harness Engineering.md)

## 来源引用

- [摘要：The Self-Healing Agent Harness](summaries/摘要：The Self-Healing Agent Harness.md)（[原文](https://x.com/intuitiveml/status/2048912026018484317)）
