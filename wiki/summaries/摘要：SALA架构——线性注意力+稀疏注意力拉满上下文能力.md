---
title: 摘要：SALA架构——线性注意力+稀疏注意力拉满上下文能力
type: summary
tags:
- 推理优化
- 上下文管理
- Agent 协作模式
status: 已审核
confidence: high
last_compiled: '2026-04-10'
source_tags: LLM, Agent
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a01399ec08dc410d82e73c004d14ba97
notion_id: a01399ec-08dc-410d-82e7-3c004d14ba97
---

## 一句话摘要

面壁提出 SALA 架构，75% 线性注意力层（快）+ 25% 稀疏注意力层（准），在端侧显卡上首次跑通百万级长文本推理，速度是同规模全注意力模型的 3.5 倍。

## 关键洞察

- **SALA 混合架构**：75% Lightning Attention（线性，负责局部精细计算）+ 25% InfLLM v2（稀疏，负责全局高效计算）

- **上下文扩展至 2048K**：无需 YaRN 等额外技术

- **HALO 训练范式**：从全注意力模型架构转换而非从零训练，成本降低 ~75%

- **256K 时速度 3.5 倍**：RTX 5090 上 Qwen3-8B 在 128K 时崩溃，MiniCPM-SALA 可跑到 1M

- **HyPE 混合位置编码**：线性层保留 RoPE，稀疏层去掉位置编码避免长距离衰减

## 提取的概念

- 线性注意力（已有概念，追加引用）

## 原始文章信息

- **作者**：卡尔的AI沃茨

- **发布时间**：2026-02-14

- **链接**：[原文](https://mp.weixin.qq.com/s?__biz=Mzg3MTk3NzYzNw%3D%3D&mid=2247504911&idx=1&sn=2e13b6399acc5e6834e706c2c588ecc2)

## 个人评注

SALA 架构对 Agent 长对话场景有重要意义——百万级上下文能力可以让 Agent 不再受上下文窗口限制。与记忆分层架构的‌「热/温/冷‌」分层理念在模型层面形成对应。
