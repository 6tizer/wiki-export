---
title: Hermes Curator
type: concept
tags:
- Harness 工程
status: 草稿
confidence: high
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/6ea4f0a7869d40f6a9b512df878bf6c9
notion_id: 6ea4f0a7-869d-40f6-a9b5-12df878bf6c9
---

## 定义

Hermes Curator 是 Hermes Agent 平台内置的后台维护子系统，负责定期扫描 Agent 自动创建的 Skill，根据使用频率和闲置时间将其标记为「陈旧」(stale) 或移入归档目录，防止 Skill 仓库无限膨胀。

## 核心要点

- **定期自动扫描**：默认每 7 天运行一次（`interval_hours: 168`），检查 Skill 使用频率与最后更新时间

- **渐进式清理**：30 天未使用 → stale 标记；90 天未使用 → 移入归档目录

- **安全边界**：只处理 Agent 自创建的 Skill，不触碰系统预装或 Hub 安装的 Skill；最坏结果仅归档而非删除

- **可恢复**：`hermes curator restore` 可随时恢复归档 Skill

- **Skill 保护**：`hermes curator pin` 可锁定重要 Skill 不被自动处理

- **AI 辅助合并**：使用辅助 AI 模型为功能相似的 Skill 建议合并方案

## 配置示例

```yaml
curator:
  enabled: true
  interval_hours: 168  # 7天
  min_idle_hours: 2
  stale_after_days: 30
  archive_after_days: 90
```

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

## 来源引用

- [摘要：Hermes推出Curator功能：自动清理Skill 仓库](summaries/摘要：Hermes推出Curator功能：自动清理Skill 仓库.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ%3D%3D&mid=2461159595&idx=1&sn=118a32399db51abe9ca6ad54a390e59b&chksm=862d857db8f99a1e7421e0fba9162fba1aaf81ee3063a2ff913f7c6d41136ba6e6c215dc581c#rd)）

- [摘要：Hermes Just Built Garbage Collection for AI Agent Skills](summaries/摘要：Hermes Just Built Garbage Collection for AI Agent Skills.md)（[原文](https://x.com/AlphaSignalAI/status/2050269010735018074)）

- [摘要：How Hermes Agent Solves Skill Drift and Context Rot as a Self-Improving Agent](summaries/摘要：How Hermes Agent Solves Skill Drift and Context Rot as a Self-Improving Agent.md)（[原文](https://x.com/mem0ai/status/2050351798142288050)）
