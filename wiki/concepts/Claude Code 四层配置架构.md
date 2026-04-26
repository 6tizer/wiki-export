---
title: Claude Code 四层配置架构
type: concept
tags:
- Agent 协作模式
- 多Agent协作
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/8810ea41e9724fac8205c2cf268544db
notion_id: 8810ea41-e972-4fac-8205-c2cf268544db
---

## 定义

Claude Code 四层配置架构，指把 Claude Code 的工程化使用拆分为 Rules、Skills、Hooks、Agents 四层，各自负责规范、任务拆解、自动触发与任务委派。

## 关键要点

- Rules 定义项目规范与约束。

- Skills 封装常见任务的处理方式。

- Hooks 负责事件触发后的自动动作。

- Agents 负责将特定任务委托给更合适的子代理。

- 四层组合后，Claude Code 从终端里的对话框升级为可协调、可记忆、可迭代的代理系统。

## 来源引用

- [摘要：154K Star！Anthropic黑客松冠军的Claude Code配置大公开](summaries/摘要：154K Star！Anthropic黑客松冠军的Claude Code配置大公开.md)

  - 来源文章页面：154K Star！Anthropic黑客松冠军的Claude Code配置大公开

  - 外部链接：[原文链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw%3D%3D&mid=2247515422&idx=1&sn=6d3cca0b2702fd1b47b8a1771475441b&chksm=e9010047a94039c4cee3023882ada32b6ea1b4fbc65f29420b5c3c14de73f63686f7fec48b39#rd)
