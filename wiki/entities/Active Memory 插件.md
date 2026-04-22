---
title: Active Memory 插件
type: entity
tags:
- OpenClaw
- 记忆系统
status: 审核中
confidence: high
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/3ed9eaefb9954f5fbfb3886fd6fe9466
notion_id: 3ed9eaef-b995-4f5f-bfb3-886fd6fe9466
---

## 定义

Active Memory 插件是 OpenClaw 在主回复前插入的可选记忆子代理，用于自动检索 ongoing 对话相关的偏好、上下文和历史细节，让记忆能力在回答前就参与推理。

## 核心机制

- 在主回复前运行专用记忆子代理

- 自动拉取与当前对话最相关的偏好、上下文与历史细节

- 支持 `message`、`recent`、`full` 三种上下文模式

- 支持 `/verbose` 实时检查，以及自定义 prompt 和 thinking 参数

## 关键要点

- 把“记忆检索”从事后整理前移到回复前阶段

- 降低用户手动说“记住这个”的频率

- 让长期记忆系统与当前会话形成更紧密闭环

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651027177&idx=1&sn=f3ece19977485e25725110b5dc3e1bb7&chksm=855a263b95874ae0288e165b327a35db0538c226bade72c984a4ff4f99ff14efe7e074c527ab#rd)｜《Openclaw 龙虾五天五连，24小时两更，火力全开！到底更新了些什么？》｜源文章：Openclaw 龙虾五天五连，24小时两更，火力全开！到底更新了些什么？

## 关联概念

- [OpenClaw](entities/OpenClaw.md)

- [Dreaming 记忆机制](concepts/Dreaming 记忆机制.md)
