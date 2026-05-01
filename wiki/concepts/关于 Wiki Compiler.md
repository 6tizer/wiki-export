---
title: 关于 Wiki Compiler
type: concept
tags:
- 知识管理
status: 已审核
confidence: high
last_compiled: ''
source_tags: ''
source_article_url: https://www.notion.so/22dabdd5d3a349d9a15bf6a0e86fda2f
notion_url: https://www.notion.so/Tizer/441a6ce2e903449dabdf7b3258a3b66a
notion_id: 441a6ce2-e903-449d-abdf-7b3258a3b66a
---

## 定义

知识 Wiki 系统的**编译器**角色——负责将原始资料（微信文章、X 书签）转化为结构化的 Wiki 条目，是整个知识流水线的入口和建设者。

## 关键要点

- **触发方式**：新文章入库时自动触发（page.created，60s 防抖）+ 独立 recurrence 每小时检查存量未编译文章 + @mention 手动触发

- **核心流程**：读取源文章 → Summary 去重检查 → 创建 summary（状态=已审核）→ 提取 3-7 个核心概念 → 强制查重（名称归一化）→ 已有则追加引用 / 没有则创建 concept 或 entity（状态=草稿）→ `<mention-page>` 回填 → 设置标签 + 置信度 + 编译时间 → 标记源文章已编译

- **concept vs entity 判断**：有版本历史、GitHub Stars、融资信息等「档案属性」→ entity；否则 → concept

- **来源标签透传**：从源文章的标签属性复制到 summary 的「来源标签」text 属性，保留原始细粒度信息

- **批量编译能力**：每次最多 30 篇，实测可达 ~60 篇/小时

## 可修改范围

创建新 summary / concept / entity，追加引用。不修改已有页面的核心内容。

## 与其他 Agent 的协作

- **上游**：微信文章数据库、X 书签文章数据库提供原始资料

- **下游**：产出的 concept / entity 供 [关于 Gap Agent](concepts/关于 Gap Agent.md) 做覆盖缺口对比；产出的 summary 供 Wiki Synthesizer 做跨资料综合分析

- **质量保障**：Wiki Lint Agent 定期检查 Compiler 产出的条目质量，Wiki Fixer 执行修复

## 关联概念

- Wiki Lint Agent — 诊断编译产出的质量问题

- Wiki Fixer — 修复编译产出中的标签/状态/重复等问题

- Wiki Synthesizer — 在编译产出的基础上做知识进化
