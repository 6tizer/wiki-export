---
title: Skill 生命周期管理
type: concept
tags:
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/3f3c5675b2274bda904d5542099efbb1
notion_id: 3f3c5675-b227-4bda-904d-5542099efbb1
---

## 定义

Skill 生命周期管理是指对 AI Agent 自动创建的 Skill（技能脚本/解决方案）进行从创建、使用、陈旧标记到归档或合并的全流程治理。随着 Agent 长期运行，Skill 仓库会持续膨胀，导致检索效率下降和上下文污染，因此需要系统化的生命周期管理策略。

## 核心要点

- **膨胀问题**：自进化型 Agent（如 Hermes）会自动沉淀解决方案为 Skill，长期运行后仓库规模快速增长

- **生命周期阶段**：活跃 → 陈旧(stale) → 归档(archived)，每个阶段有明确的时间阈值和触发条件

- **治理手段**：定期扫描使用频率、自动归档低频 Skill、AI 辅助合并相似 Skill、手动 pin 保护关键 Skill

- **安全原则**：归档而非删除，确保可恢复性；区分自创建 Skill 与系统预装 Skill

- **实现案例**：Hermes Curator 是目前该概念的典型实现

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

## 来源引用

- [摘要：Hermes推出Curator功能：自动清理Skill 仓库](summaries/摘要：Hermes推出Curator功能：自动清理Skill 仓库.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ%3D%3D&mid=2461159595&idx=1&sn=118a32399db51abe9ca6ad54a390e59b&chksm=862d857db8f99a1e7421e0fba9162fba1aaf81ee3063a2ff913f7c6d41136ba6e6c215dc581c#rd)）

- [摘要：Hermes Just Built Garbage Collection for AI Agent Skills](summaries/摘要：Hermes Just Built Garbage Collection for AI Agent Skills.md)（[原文](https://x.com/AlphaSignalAI/status/2050269010735018074)）
