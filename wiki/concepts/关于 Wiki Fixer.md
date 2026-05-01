---
title: 关于 Wiki Fixer
type: concept
tags:
- 知识管理
status: 已审核
confidence: high
last_compiled: ''
source_tags: ''
source_article_url: https://www.notion.so/1249bdf6ad334e11ad3d44fde9cb241f
notion_url: https://www.notion.so/Tizer/60be26ada85b4d0594c644285458aa97
notion_id: 60be26ad-a85b-4d05-94c6-44285458aa97
---

## 定义

知识 Wiki 系统的**治疗师**角色——根据 Lint Report 的诊断结果执行自动修复，同时支持用户通过 @mention 下达指令模式的手动修复任务。

## 关键要点

- **触发方式**：Lint Agent 在报告中 @mention 触发（自动模式）+ 用户或 Notion AI @mention 触发（指令模式）

- **自动模式（7 类修复）**：

  - A. 状态修复：补空状态、草稿→审核中（7天+完整）、→已审核（≥2篇引用）、→需更新（>30天）

  - B. 标签修复：空标签补全、废弃标签重映射、分类校验

  - C. 类型分类修正：concept↔entity 迁移

  - D. 完全同名重复合并：保留状态更高/类型更准/编辑更新的

  - E. 引用链修复：E1 孤岛修复（追加引用）+ E2 纯文本引用升级为 `<mention-page>`

  - F. 规范化近似重复合并

  - G. 报告不自动处理的项目

- **指令模式**：合并近似重复、删除条目、补充内容、类型迁移、批量状态更新

- **安全边界**：不创建 summary/concept/entity，不修改 Schema 等系统页面

## 可修改范围

状态/标签/类型修复、同名重复合并、引用链修复（孤岛 + 纯文本升级）。近似重复合并和删除需要人类指示。

## 与其他 Agent 的协作

- **上游**：接收 Wiki Lint Agent 的 lint-report 作为修复清单

- **指挥者**：Notion AI 或 Tizer 可通过 @mention 下达指令

- **不越权**：修复范围严格限定，建设性工作（创建新条目）交给 Wiki Compiler

## 关联概念

- Wiki Lint Agent — 诊断问题，提供修复清单

- Wiki Compiler — 建设者，Fixer 不越界做建设工作
