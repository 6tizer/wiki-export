---
title: Qwen2.5-1.5B-Instruct
type: entity
tags:
- LLM
status: 草稿
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/83cc6d3a7a064546ac86495860de1fb2
notion_id: 83cc6d3a-7a06-4546-ac86-495860de1fb2
---

## 定义

Qwen2.5-1.5B-Instruct 是阿里通义千问系列的一款 1.5B 指令模型，在本文中作为 wenyan_poetry 的微调底座，承担了专属中文模型构建的基础能力。

## 关键要点

- 它在这篇文章中的角色不是最终产品，而是 OpenClaw 进行专属模型训练时所依赖的底座模型。

- 选择较小参数规模的模型，意味着本地微调与部署的门槛更低，更适合形成可复制的 Agent 训练流程。

- 文章借它说明：Agent 的能力边界可以通过训练自己的模型底座而被重新定义。

## 来源引用

- [摘要：首次实现龙虾自己微调大脑：OpenClaw 微调大模型，并把新大脑装回自己](summaries/摘要：首次实现龙虾自己微调大脑：OpenClaw 微调大模型，并把新大脑装回自己.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkyMDU4ODUwMw%3D%3D&mid=2247492103&idx=1&sn=ddf43f45906b135a3844606e253da259&chksm=c0206a2f58c916240e5ef5f394c40772c765aab1a6e66946b5134b62947d9c9e8a917bd559e5#rd)）

## 关联概念

- [OpenClaw](entities/OpenClaw.md)

- [Ollama](entities/Ollama.md)

- [wenyan_poetry](entities/wenyan_poetry.md)

- [训练—部署—替换闭环](concepts/训练—部署—替换闭环.md)
