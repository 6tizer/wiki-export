---
title: 摘要：从千问点奶茶说起——Generative UI 协议架构实践
type: summary
tags:
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-26'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/7bbfbab3987142a5a79f1e4aca811fb3
notion_id: 7bbfbab3-9871-42a5-a79f-1e4aca811fb3
---

## 一句话摘要

通过 DivKit（SDUI）+ A2UI 双协议架构在 Android 上实现 Generative UI，让 AI 助手能根据对话上下文实时生成可交互界面。

## 关键洞察

- **双协议分工**：DivKit 处理确定性展示型 UI（天气、相册），A2UI 处理生成式交互型 UI（表单、问卷），各取所长

- **组件越少越好**：从 15 种组件砍到 6 种后，LLM 格式错误率从 ~20% 降到接近 0

- **Zod discriminatedUnion**：给 LLM 明确的分支路径约束，比 z.union 好得多

- **交互闭环设计**：按钮的 action label 作为新消息注入聊天流，触发下一轮 AI 响应，表单成为对话的一部分而非终点

- **为 LLM 设计数据结构**：扁平优于嵌套、枚举优于自由文本、少字段优于多字段

## 提取的概念

- Generative UI

- [A2UI 协议](concepts/A2UI 协议.md)

- Server-Driven UI

## 原始文章信息

- **作者**：老码小张

- **来源**：微信公众号

- **发布时间**：2026-02-28

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247492699&idx=1&sn=86f5750ed425288bc57c149db9c919df)

## 个人评注

Generative UI 是 Agent 交互的重要趋势——对话不再只是文字来回，而是承载任意交互的容器。「组件越少 LLM 错误率越低」的经验对设计任何 LLM 友好的 Schema 都有借鉴意义。双协议架构的思路也可应用于 Notion 的 Agent 工作流设计。
