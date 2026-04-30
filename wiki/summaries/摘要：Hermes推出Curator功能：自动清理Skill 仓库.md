---
title: 摘要：Hermes推出Curator功能：自动清理Skill 仓库
type: summary
tags:
- Harness 工程
status: 已审核
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: https://www.notion.so/352701074b6881ffa532c43fa5d86498
notion_url: https://www.notion.so/Tizer/7c1733a1cf564b4797f6230534d00899
notion_id: 7c1733a1-cf56-4b47-97f6-230534d00899
---

## 一句话摘要

Hermes Agent 推出 Curator 后台维护功能，通过定期扫描和渐进式归档机制自动清理长期未使用的 Skill，解决自进化 Agent 的技能仓库膨胀问题。

## 关键洞察

- **Skill 膨胀是自进化 Agent 的必然副作用**：Hermes 自动沉淀经验为 Skill，长期使用后仓库规模快速增长，需要系统化治理

- **渐进式生命周期管理**：30 天未使用标记为 stale → 90 天未使用移入归档，平衡了自动化效率与安全性

- **安全边界设计精巧**：只处理 Agent 自创建的 Skill，不触碰系统预装或 Hub 安装的；最坏结果仅归档而非删除，可随时恢复

- **AI 辅助合并**：使用辅助模型建议功能相似 Skill 的合并方案，进一步压缩仓库体积

- **配置灵活可控**：扫描间隔、闲置阈值、归档阈值均可通过 YAML 配置自定义，`pin` 命令可保护关键 Skill

## 提取的概念

- [Hermes Curator](concepts/Hermes Curator.md)

- [Skill 生命周期管理](concepts/Skill 生命周期管理.md)

- [Hermes Agent](entities/Hermes Agent.md)

## 原始文章信息

- **作者**：AI工程化

- **来源**：微信公众号

- **发布时间**：2026-04-30

- **原文链接**：[Hermes推出Curator功能：自动清理Skill 仓库](https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ%3D%3D&mid=2461159595&idx=1&sn=118a32399db51abe9ca6ad54a390e59b&chksm=862d857db8f99a1e7421e0fba9162fba1aaf81ee3063a2ff913f7c6d41136ba6e6c215dc581c#rd)

- **详细文档**：[Hermes Curator 官方文档](https://hermes-agent.nousresearch.com/docs/user-guide/features/curator)

## 个人评注

Curator 解决的是自进化 Agent 的「技术债」问题——Skill 自动沉淀是 Hermes 的核心卖点，但沉淀过多又会拖累检索效率和上下文质量。这与 OpenClaw 的手动 Skill 管理形成有趣对比：OpenClaw 由人类主动编写和维护 Skill，天然不会膨胀；Hermes 则需要引入自动化清理机制来弥补自主学习的副作用。对于 Tizer 的知识管理流水线来说，这种「创建→使用→淘汰→合并」的生命周期模式值得借鉴——Wiki 条目同样面临规模膨胀问题，未来可以考虑类似的 lint + archive 机制。
