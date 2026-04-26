---
title: AX Tree
type: concept
tags:
- 知识管理
- 上下文管理
status: 草稿
confidence: medium
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/5d2d34489cf94f6cb2f56602f0af353d
notion_id: 5d2d3448-9cf9-4f6c-b2f5-6602f0af353d
---

## 定义

AX Tree 是 macOS 辅助功能系统暴露的一棵结构化界面树，能够直接提供当前应用、焦点控件、输入文本、按钮文案与网页 URL 等信息，为 Agent 的屏幕理解与记忆提取提供低成本的上下文输入。

## 关键要点

- 它最初服务于读屏等无障碍场景，但非常适合被 Agent 用来理解用户当前正在操作的界面状态。

- 相比“截图 + OCR”方案，AX Tree 的文本处理成本更低、语义噪声更少、结构化程度更高。

- 在 Word、飞书等绕开系统辅助通道的应用里，AX Tree 读取能力会受限，因此实际系统往往需要截图兜底。

- 在记忆系统里，AX Tree 更像一种高频、低成本的前台上下文采集接口。

## 来源引用

- [摘要：记忆，是 Agent 基建｜对话 Calvin@Vida](summaries/摘要：记忆，是 Agent 基建｜对话 Calvin@Vida.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ%3D%3D&mid=2247516299&idx=1&sn=c3233ab0dd43f620ef87eb82241b5952&chksm=c3c54e7f8cf382407deb18d014e716c88f39038aa16dbd580f95b730cfc1135ba9daccf127a8#rd)）

## 关联概念

- [OpenChronicle](entities/OpenChronicle.md)

- [Chronicle](concepts/Chronicle.md)

- [共享记忆层](concepts/共享记忆层.md)

- [Proactive Agents](concepts/Proactive Agents.md)
