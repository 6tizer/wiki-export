---
title: Context Hub
type: entity
tags:
- Coding Agent
status: 草稿
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/30f873c8916544ae8e0fe14ed4e6b2d4
notion_id: 30f873c8-9165-44ae-8e0f-e14ed4e6b2d4
---

## 定义

Context Hub 是一个面向 Coding Agent 的运行时文档获取工具，通过 CLI 在生成代码前拉取最新 API 文档，减少模型使用过时接口的情况。

## 关键要点

- 让 Agent 在运行时读取最新文档而不是依赖训练快照

- 支持搜索、按语言过滤和文档获取

- 适合 Cursor、Claude Code 等编程助手接入

## 来源引用

- 《Context Hub：吴恩达开源的 Coding Agent「文档新鲜度」解决方案》｜文章链接：[https://x.com/AndrewYNg/status/2031051809499054099](https://x.com/AndrewYNg/status/2031051809499054099)

- 《Context Hub：吴恩达为 AI 编程 Agent 打造的「Stack Overflow」》（Andrew Y. Ng，X书签，2026-03）— 补充其“最新 API 文档 + Agent 反馈闭环”的定位。

- 《Context Hub：Andrew Ng 为 AI 编程 Agent 打造的「Stack Overflow」》（@berryxia，X书签，2026-03）— 补充注释层、共享学习与文档投毒风险视角。

- 《Context Hub：吴恩达为 AI 编程 Agent 打造的「Stack Overflow」》— X书签，2026-03：强调运行时获取最新 API 文档

- 《Context Hub：Andrew Ng 为 AI 编程 Agent 打造的「Stack Overflow」》— X书签，2026-03：补充 annotation、共享反馈与风险讨论
