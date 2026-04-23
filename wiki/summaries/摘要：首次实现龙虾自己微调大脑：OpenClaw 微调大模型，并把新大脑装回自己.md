---
title: 摘要：首次实现龙虾自己微调大脑：OpenClaw 微调大模型，并把新大脑装回自己
type: summary
tags:
- OpenClaw
- LLM
status: 已审核
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b68816e965ac2a34f9f561e
notion_url: https://www.notion.so/225259c0f5d4488cb720fc939ab07065
notion_id: 225259c0-f5d4-488c-b720-fc939ab07065
---

## 一句话摘要

OpenClaw 首次跑通了“微调基础模型 → 本地部署 → 替换自身默认大脑”的完整链路，用基于 Qwen2.5-1.5B-Instruct 微调得到的 wenyan_poetry 证明 Agent 不再只是调用模型，而开始具备塑造和替换专属模型的能力。

## 关键洞察

- 这次实验经过约 16 小时单机运行，完成了从模型微调到本地接入再到替换运行大脑的全流程。

- 新模型 **wenyan_poetry** 以 **Qwen2.5-1.5B-Instruct** 为底座，重点面向中文聊天、文言文交流与古诗词创作。

- 通过封装成 **Ollama** 可接入模型，OpenClaw 可以把微调结果直接变成自己的运行时“大脑”。

- 文章的重点不只是“又微调了一个模型”，而是 Agent 与模型的关系从“调用通用脑”走向“训练并拥有专属脑”。

- 这更像一个明确的工程拐点：从使用外部智能，走向塑造可部署、可替换的专属智能。

## 提取的概念

- [OpenClaw](entities/OpenClaw.md)

- [Ollama](entities/Ollama.md)

- [wenyan_poetry](entities/wenyan_poetry.md)

- [Qwen2.5-1.5B-Instruct](entities/Qwen2.5-1.5B-Instruct.md)

- [训练—部署—替换闭环](concepts/训练—部署—替换闭环.md)

## 原始文章信息

- 作者：清新研究

- 来源：微信

- 发布时间：2026-04-22 20:55

- 原文链接：[链接](https://mp.weixin.qq.com/s?__biz=MzkyMDU4ODUwMw%3D%3D&mid=2247492103&idx=1&sn=ddf43f45906b135a3844606e253da259&chksm=c0206a2f58c916240e5ef5f394c40772c765aab1a6e66946b5134b62947d9c9e8a917bd559e5#rd)

- 源文章页面：首次实现龙虾自己微调大脑：OpenClaw 微调大模型，并把新大脑装回自己

## 个人评注

- 这条案例对 Tizer 的启发不是“又一个模型发布”，而是把 Agent 能力链条往前推进了一步：当内容生产或自动化系统需要针对特定任务塑造专属模型时，训练数据、模型部署层与执行层可以形成可复用的闭环。

- 对 OpenClaw 生态而言，这也说明知识沉淀、评测反馈、部署回注和工具调用可以被逐步串成更稳固的工作流，而不再只是一次性的模型调用实验。
