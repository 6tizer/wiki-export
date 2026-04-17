---
title: LoopLM
type: concept
tags:
- LLM
status: 草稿
confidence: high
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/05ef444677d3480bb2f18165ade9a4fe
notion_id: 05ef4446-77d3-480b-b2f1-8165ade9a4fe
---

## 定义

LoopLM 是文中提到的循环语言模型架构名称，核心是在潜空间对同一组表示进行多步迭代，而不是只依赖一次前向传播完成推理。

## 关键要点

- 它把“思考”更多放在潜空间内部完成，不需要额外输出更长的推理 token

- 模型可以按任务难度动态调整循环步数，简单题少迭代，难题多迭代

- 文中认为它尤其适合图搜索、多跳推理、程序执行这类需要反复操作已有知识的任务

- 文章将其视为解释 Claude Mythos 异常性能峰值的关键候选架构

## 关联概念

- [Claude Mythos](entities/Claude Mythos.md)

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247882749&idx=1&sn=2c5b489ce91054109b22b36188b08e7d&chksm=e912871f3bcec6edb33f9d3bbe2448cd2e302161209286bca16ddf778484c2f0d06c176fa3a7#rd)｜《Claude强到不敢发的Mythos，被质疑用了字节Seed技术》｜源文章：Claude强到不敢发的Mythos，被质疑用了字节Seed技术
