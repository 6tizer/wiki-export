---
title: OpenClaw 安全实践指南
type: concept
tags:
- Agent 安全
- OpenClaw
status: 审核中
confidence: high
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/62eca4423ff7427fa3b71dbbbe5f983f
notion_id: 62eca442-3ff7-427f-a3b7-1dbbbe5f983f
---

## 定义

OpenClaw 安全实践指南是慢雾安全团队（SlowMist）于 2026 年 3 月在 GitHub 开源的安全指南，层小指南本身就是发给 Agent 执行的，公开仓库：[https://github.com/slowmist/openclaw-security-practice-guide](https://github.com/slowmist/openclaw-security-practice-guide)

## 四条核心原则

1. **零摩擦操作**：安全机制不干手正常工作，只在触碑红线时介入

1. **高风险必须确认**：不可逆或敏感操作必须暂停，等待人工批准

1. **显式夜间审计**：所有核心指标每晚上报，不允许静默通过

1. **默认零信任**：始终假设提示词注入、供应链投毒和业务逻辑滥用都有可能发生

## 三层防御矩阵

- **行动前（Pre-action）**：行为黑名单 + 严格的 Skill 安装审计协议，防止供应链投毒

- **行动中（In-action）**：权限收窄 + 跨 Skill 预检查，控制高风险业务逻辑执行

- **行动后（Post-action）**：13 项核心指标的夜间自动化审计 + Brain Git 灾难恢复

## 注意事项

- 指南基于 Linux Root 环境编写，Mac/Windows 需让 Agent 自行推导适配

- 模型能力直接影响安全效果：弱模型可能误判红线

- 夜间审计是事后检测，已发生的破坏无法回滚

## 来源引用

- [摘要：OpenClaw 极简安全实践指南：慢雾为高权限 AI Agent 打造的三层防御体系](summaries/摘要：OpenClaw 极简安全实践指南：慢雾为高权限 AI Agent 打造的三层防御体系.md)

- [摘要：OpenClaw 安全实践指南：SlowMist 给高权限 AI Agent 的「思想钢印」](summaries/摘要：OpenClaw 安全实践指南：SlowMist 给高权限 AI Agent 的「思想钢印」.md)（Cos / SlowMist_Team，X书签）— 从"把安全策略直接注入 Agent 认知层"的角度补充这份指南的设计意义
