---
title: Skill Drift
type: concept
tags:
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/2f8116f816cc4c18bca82d811ec29b89
notion_id: 2f8116f8-16cc-4c18-bca8-2d811ec29b89
---

## 定义

**Skill Drift**（技能漂移）是指 Agent 系统中已固化的 Skill 随时间悄悄失效的现象——通常由底层 API 合约变更、外部依赖更新或模型行为变化导致。Skill 表面上仍存在且可被路由器调用，但其输出已不再正确或可靠。

## 关键要点

- Skill Drift 最常见的触发因素是**API 合约变更**：当某个项目的 API 接口签名或返回格式改变时，依赖该 API 的 Skill 会静默失败

- 这种失效是**无声的**——不会抛出显式错误，只是输出质量悄然下降，难以通过常规监控发现

- 解决方案是在 Skill 创建时自动附带测试（auto-test on skill creation），在 Skill 被调用前主动验证其有效性

- 在多项目 Agent 系统中，一个项目的 Skill Drift 可能扩散影响其他项目（cross-project contamination）

## 关联概念

- [Skillify](concepts/Skillify.md)

- [GBrain](entities/GBrain.md)

- [Harness Engineering](concepts/Harness Engineering.md)

## 来源引用

- [摘要：Big drop for GBrain v0.19.](summaries/摘要：Big drop for GBrain v0.19.md)（[原文](https://x.com/garrytan/status/2047504667127799974)）

- [摘要：How Hermes Agent Solves Skill Drift and Context Rot as a Self-Improving Agent](summaries/摘要：How Hermes Agent Solves Skill Drift and Context Rot as a Self-Improving Agent.md)（[原文](https://x.com/mem0ai/status/2050351798142288050)）
