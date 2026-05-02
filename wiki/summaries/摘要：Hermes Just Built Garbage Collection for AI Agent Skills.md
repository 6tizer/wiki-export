---
title: 摘要：Hermes Just Built Garbage Collection for AI Agent Skills
type: summary
tags:
- Harness 工程
- Agent 安全
status: 已审核
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: https://www.notion.so/354701074b688190ada2cffbc1bca4a9
notion_url: https://www.notion.so/Tizer/9035f3b0df82401db6fee6a2aa6dd83d
notion_id: 9035f3b0-df82-401d-b6fe-e6a2aa6dd83d
---

## 一句话摘要

Hermes Agent v0.12.0 推出自治式 Curator 子系统，以两阶段垃圾回收（确定性状态转移 + LLM 辅助合并）管理 Skill 仓库生命周期，首次在开源 Agent 框架中补齐「创建→使用→退役」闭环。

## 关键洞察

- **首个完整 create-use-retire 闭环**：Curator 补齐了自进化 Agent 长期缺失的 Skill 退役环节，目前没有其他开源框架内置等效功能

- **双阶段 GC 架构**：Phase 1 为纯确定性状态转移（30 天 stale → 90 天 archive），Phase 2 由辅助 LLM 执行 umbrella-building 合并，将功能近似 Skill 整合为伞型 Skill 或降级为 references/templates/scripts 支撑文件

- **纵深防御设计**：bundled manifest 保护系统 Skill、hub lock.json 保护市场 Skill、pin 命令硬锁定关键 Skill、fork 进程仅获 memory+skills 工具集——最坏结果仅为可恢复的归档

- **辅助模型分离**：Curator 审查可路由到比主模型更廉价的辅助模型（auxiliary.curator），降低维护开销

- **已知缺陷需注意**：v0.12.0 首版无 dry-run 模式，use-counter 曾因零调用点而失效（PR #17932 修复），patch 活跃度尚未纳入生命周期信号

## 提取的概念

- [Hermes Curator](concepts/Hermes Curator.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [Skill 生命周期管理](concepts/Skill 生命周期管理.md)

- [自进化智能体](concepts/自进化智能体.md)

## 原始文章信息

- **作者**：@AlphaSignalAI

- **来源**：X（Twitter）

- **发布时间**：2026-05-01

- **原文链接**：[Hermes Just Built Garbage Collection for AI Agent Skills](https://x.com/AlphaSignalAI/status/2050269010735018074)

## 个人评注

这篇文章是目前对 Hermes Curator 最详尽的技术分析，比之前的微信文章深入得多。双阶段 GC 架构（确定性转移 + LLM 合并）的设计思路对 Tizer 的知识管理流水线有直接参考价值——Wiki 条目同样面临「只增不减」的膨胀问题，可以借鉴类似的时间维度自动标记 + AI 辅助合并策略。文中提到的 umbrella-building 合并策略（将近似 Skill 合并为一个伞型 Skill + 支撑文件）与 Wiki 的 concept 合并机制异曲同工。值得关注的是 bump_use() 的零调用点 bug——任何基于使用计数的生命周期系统都需要确保计数器真正被触发。
