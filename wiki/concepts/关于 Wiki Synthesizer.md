---
title: 关于 Wiki Synthesizer
type: concept
tags:
- 知识管理
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/1249bdf6ad334e11ad3d44fde9cb241f
notion_url: https://www.notion.so/Tizer/ece328e209e243c789a55eb30a9c84b4
notion_id: ece328e2-09e2-43c7-89a5-5eb30a9c84b4
---

## 定义

知识 Wiki 系统的**知识进化者**角色——通过发现主题聚集，将零散的 concept/entity/summary 升华为跨资料的综合分析（synthesis），是 Wiki 从「信息库」走向「知识库」的关键角色。

## 关键要点

- **触发方式**：独立 recurrence 定时触发 + @mention 手动触发

- **核心流程**：扫描 concept 标签分布 → 发现主题聚集（≥10 个 concept 共享同一标签，或跨标签交叉分析）→ 三级去重检查 → 读取相关条目完整内容（按状态优先级）→ 生成 synthesis 综合分析页面

- **三级去重检查**：精确标题匹配 → 模糊主题匹配 → 标签覆盖检查（同标签下不超过 3 篇）

- **synthesis 页面结构**：研究问题 → 综合分析（对比表 + 演进路径）→ 关键发现（跨来源洞察）→ 来源列表 → 行动建议

- **深度优先**：每次最多处理 2 个主题

## 可修改范围

只创建 synthesis 页面，不修改其他任何页面。

## 与其他 Agent 的协作

- **上游**：依赖 Wiki Compiler 积累的 concept/entity/summary 作为原料

- **质量保障**：按状态优先级引用（已审核 > 审核中 > 草稿 > 需更新），确保 synthesis 的论据可靠性

- **互补**：Wiki QA Agent 回答具体问题，Synthesizer 主动发现并提炼跨领域洞察

## 关联概念

- Wiki Compiler — 提供 synthesis 的原料

- Wiki QA Agent — 被动回答 vs 主动综合的互补关系

- [关于 Gap Agent](concepts/关于 Gap Agent.md) — Gap Agent 发现缺什么，Synthesizer 发现能合成什么
