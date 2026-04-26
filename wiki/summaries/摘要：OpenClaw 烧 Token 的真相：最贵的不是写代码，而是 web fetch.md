---
title: 摘要：OpenClaw 烧 Token 的真相：最贵的不是写代码，而是 web fetch
type: summary
tags:
- OpenClaw
- 上下文管理
- 内容自动化
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: OpenClaw, Agent, 自动化, LLM
source_article_url: ''
notion_url: https://www.notion.so/f5408faec45a48c78c275b663b2a5a39
notion_id: f5408fae-c45a-48c7-8c27-5b663b2a5a39
---

## 一句话摘要

这篇文章指出 Agent 成本飙升的主因不是“生成太多”，而是重复读取庞大上下文，尤其是 web fetch 会迅速吞掉 token 预算。

## 关键洞察

- 每轮对话都重复发送系统提示、历史记录和记忆文件，是隐性成本黑洞。

- web fetch 往往比代码生成贵得多，尤其在长网页和 PDF 场景下更明显。

- 降本的关键是 Context Compaction、模型路由和结构化记忆持久化。

## 提取的概念

- [WebFetch](concepts/WebFetch.md)

- [Context Compaction](concepts/Context Compaction.md)

- [模型路由](concepts/模型路由.md)

## 原始文章信息

- 作者：Marvin Tong (@marvin_tong)

- 来源：X书签

- 发布时间：2026-03-11

- 链接：[原文](https://x.com/marvin_tong/status/2031557670826815705)

## 个人评注

- 对 Tizer 的 Agent 体系非常实用，意味着内容抓取和网页读取要优先做摘要化与分层缓存，而不是直接整页塞进 prompt。
