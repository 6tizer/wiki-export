---
title: 摘要：OpenClaw 极简安全实践指南：慢雾为高权限 AI Agent 打造的三层防御体系
type: summary
tags:
- OpenClaw
- Agent 安全
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: OpenClaw, Agent, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/30525cb470994ca2942c1d74a0e63e42
notion_id: 30525cb4-7099-4ca2-942c-1d74a0e63e42
---

## 一句话摘要

慢雾开源的 OpenClaw 安全指南采用「把安全意识直接植入 Agent 认知」的思路，构建零外部依赖的三层防御矩阵。

## 关键洞察

- 核心创新：指南本身就是发给 Agent 执行的 Markdown 文件，不是人工 checklist

- **三层防御**：Pre-action（行为黑名单+供应链审计）→ In-action（权限收窄+预检查）→ Post-action（13 项夜间审计+灾难恢复）

- **v2.8 Beta 新增**：Agent 辅助 5 步部署、`--light-context` Cron 保护、持久化报告路径、增强代码审查

- 明确承认的局限：弱模型可能误判红线；夜间审计是事后检测；指南本身也可能被提示注入篡改

- GitHub 发布不到一个月已积累 2,601 Stars，持续活跃维护

## 提取的概念

[OpenClaw](entities/OpenClaw.md) · [OpenClaw 安全实践指南](concepts/OpenClaw 安全实践指南.md)

## 原始文章信息

- **作者**：evilcos, SlowMist_Team（慢雾）

- **来源**：X书签

- **发布时间**：2026-03-02

- **链接**：[https://github.com/slowmist/openclaw-security-practice-guide](https://github.com/slowmist/openclaw-security-practice-guide)

## 个人评注

「安全意识植入 Agent 认知」的思路与 Tizer 的 HITL 理念一致——让 Agent 在关键节点主动暂停等待人工确认。这份指南对任何在本地部署高权限 OpenClaw 的场景都是必读材料。
