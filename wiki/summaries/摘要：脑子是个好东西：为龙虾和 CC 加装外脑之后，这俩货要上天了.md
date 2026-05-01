---
title: 摘要：脑子是个好东西：为龙虾和 CC 加装外脑之后，这俩货要上天了
type: summary
tags:
- OpenClaw
- RAG/检索
- 上下文管理
- 长期记忆
- CLI 工具
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: Agent, LLM, OpenClaw, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/3e89900528b249209a3e73079da33c52
notion_id: 3e899005-28b2-4920-9a3e-73079da33c52
---

## 一句话摘要

claude-mem 是一套 RAG+Hook 工程，通过生命周期 Hook 收集 OpenClaw 和 Claude Code 的对话与工具调用，存入 SQLite FTS5+Chroma 向量库，以语义检索方式在新会话中注入相关记忆。

## 关键洞察

- **OpenClaw 失忆的根本原因**：会话上下文（短期）和长期记忆混在一起，多通道切换时每段会话互不知情

- **claude-mem 的技术栈**：RAG + Hook，SQLite FTS5 + Chroma 向量库，embedding 语义检索

- **老问题仍存在**：记忆库越大，检索容易错抓相似但不相关内容，可能出现幻觉；省 token、方便追溯

- **安装极简**：OpenClaw 一行 curl 命令安装，Claude Code 参考官方文档

- **与 mem9 的区别**：claude-mem 更轻量本地化，mem9 更系统有云端存储和两段式提取

## 提取的概念

- claude-mem

## 原始文章信息

- **作者**: MacTalk

- **来源**: 微信公众号

- **发布时间**: 2026-03-29

- **GitHub**: [https://github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)

## 个人评注

直接解决 Tizer OpenClaw 多通道失忆问题，claude-mem 和 mem9 是两个可选方案，前者更轻量，后者更完整。
