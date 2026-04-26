---
title: memory-persistence hook
type: concept
tags:
- 记忆系统
- Coding Agent
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/404298eeb85e4a5eb9104fab253160b3
notion_id: 404298ee-b85e-4a5e-b910-4fab253160b3
---

## 定义

memory-persistence hook 是一种在会话开始时自动加载上下文、会话结束时自动保存状态的钩子机制，用来让 Claude Code 在多轮、多次进入项目时保持连续记忆。

## 关键要点

- 它解决的是重复介绍项目背景的成本问题。

- 通过自动读写上下文，减少开发者管理对话元数据的负担。

- 这是把“记忆能力”从临时对话提升为工程化能力的典型例子。

- 适合与项目规范、任务状态、未解决问题跟踪一起使用。

## 来源引用

- [摘要：154K Star！Anthropic黑客松冠军的Claude Code配置大公开](summaries/摘要：154K Star！Anthropic黑客松冠军的Claude Code配置大公开.md)

  - 来源文章页面：154K Star！Anthropic黑客松冠军的Claude Code配置大公开

  - 外部链接：[原文链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw%3D%3D&mid=2247515422&idx=1&sn=6d3cca0b2702fd1b47b8a1771475441b&chksm=e9010047a94039c4cee3023882ada32b6ea1b4fbc65f29420b5c3c14de73f63686f7fec48b39#rd)
