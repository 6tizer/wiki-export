---
title: Book Mirror
type: concept
tags:
- 知识管理
- 提示工程
- OpenClaw
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/121b0a26fc064d79b194882429ff3705
notion_id: 121b0a26-fc06-4d79-b194-882429ff3705
---

## 定义

Book Mirror 是一种个性化阅读分析技术（OpenClaw/Hermes Skill），通过将书籍内容与读者的个人上下文（对话记录、人际关系、情感模式、工作风格等）进行交叉映射，生成逐章双栏分析：左栏保留原书核心内容，右栏映射到读者的真实生活情境。

别名：书籍镜像、个性化阅读分析

## 关键要点

- **双栏结构**：左栏（作者原意）+ 右栏（个人映射），左栏详尽到可以替代原书，右栏具体到使用读者自己的话

- **上下文驱动**：右栏的质量完全取决于 AI 对读者的了解程度；对陌生人执行 Book Mirror 只是普通书摘

- **Pipeline**：获取书籍 → 按章拆分 → 构建 Context Pack（读者档案）→ 逐章双栏分析 → 事实核查 → 输出 PDF

- **质量标准**：禁止泛化建议（如"consider reflecting on..."），只允许基于具体记忆的精确映射；无关章节直接标注不适用

- **依赖长期记忆**：需要 Agent 拥有长时间积累的用户对话、治疗笔记、关系模式等上下文才能发挥真正价值

## 来源引用

- [摘要：Here's a fun skill you can teach your OpenClaw/Hermes — Book Mirror](summaries/摘要：Here's a fun skill you can teach your OpenClaw-Hermes — Book Mirror.md)（[原文](https://x.com/garrytan/status/2049059060427952164)）

## 关联概念

- [OpenClaw](entities/OpenClaw.md)

- [Hermes Agent](entities/Hermes Agent.md)
