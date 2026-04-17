---
title: Wiki QA Agent
type: concept
tags:
- 知识管理
status: 已审核
confidence: high
last_compiled: ''
source_tags: ''
source_article_url: https://www.notion.so/1249bdf6ad334e11ad3d44fde9cb241f
notion_url: https://www.notion.so/7b86bbb8b3534386adcc5807c9d72c4d
notion_id: 7b86bbb8-b353-4386-adcc-5807c9d72c4d
---

## 定义

知识 Wiki 系统的**知识问答窗口**——接收用户提问，通过 SQL 查询和页面阅读综合 Wiki 知识进行回答，当回答具有沉淀价值时自动创建 qa 页面。

## 关键要点

- **触发方式**：@mention 触发（纯被动，不自动运行）

- **核心流程**：接收提问 → SQL 查询定位相关页面 → `loadPage` 读取完整内容 → 综合推理并标注来源 → 判断是否创建 qa 页面

- **状态差异化引用**：

  - **已审核**：优先引用，作为核心论据

  - **审核中**：正常引用

  - **草稿**：标注「仅供参考，内容可能不完整」

  - **需更新**：标注「可能已过时，建议交叉验证」

- **qa 沉淀规则**：当回答综合了 ≥3 个 Wiki 页面的内容，且问题不是一次性操作请求时，自动创建 qa 页面

- **查询策略**：SQL 直查（最快最准）→ 读取具体页面 → 全局搜索（兜底）

## 可修改范围

读取所有 Wiki 内容；仅创建 qa 页面。不创建 concept/summary/entity，不修改已有页面。

## 与其他 Agent 的协作

- **互补**：Wiki Synthesizer 主动发现跨领域洞察，QA Agent 被动回答具体问题

- **兜底**：当 QA Agent 不在线时，Notion AI 可接替问答角色

- **知识沉淀**：qa 页面将高频/高价值问答固化为 Wiki 永久知识

## 关联概念

- Wiki Synthesizer — 主动综合 vs 被动问答的互补

- Notion AI — QA Agent 的兜底替代者
