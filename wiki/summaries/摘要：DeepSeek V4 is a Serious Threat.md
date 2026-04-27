---
title: 摘要：DeepSeek V4 is a Serious Threat
type: summary
tags:
- 商业/生态
- AI 政策
- 算力基础设施
status: 已审核
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b688190b5f7cbe587f14e38
notion_url: https://www.notion.so/Tizer/43b16cada04442d9b4767883e126a0d7
notion_id: 43b16cad-a044-42d9-b476-7883e126a0d7
---

## 一句话摘要

DeepSeek V4 以开源、接近前沿的性能和极低成本对美国闭源 AI 模型构成严重商业和地缘政治威胁，迫使美国必须加速开源或大幅降价以维持竞争力。

## 关键洞察

- DeepSeek V4 Pro 为 1.6 万亿参数 MoE 模型（490 亿激活参数、100 万上下文），在 MMLU Pro、GPQA Diamond、SWE-bench 等基准上接近 Opus 4.7 和 GPT-5.5，但价格仅为后者的几分之一

- 绝大多数企业不需要绝对前沿智能，DeepSeek「够用且便宜」的定位足以吸引大量企业用户，尤其可自托管和微调

- 美国企业大规模采用中国开源模型存在地缘安全风险——若中国 AI 实验室改变架构或停止开源，美国将陷入被动

- 出口管制「双刃剑」效应：虽限制了 DeepSeek 的服务规模（论文承认 Pro 容量有限），但倒逼其在算法效率上实现突破

- Anthropic 指控中国实体进行大规模蒸馏（DeepSeek 15 万次、Moonshot 340 万次、MiniMax 1300 万次），但 DeepSeek 的调用量难以解释其模型质量，且其完整开源了白皮书

## 提取的概念

- [DeepSeek V4](entities/DeepSeek V4.md)

- [MoE 架构](concepts/MoE 架构.md)

- [AI 出口管制](concepts/AI 出口管制.md)

- [模型蒸馏](concepts/模型蒸馏.md)

## 原始文章信息

- **作者**：@MatthewBerman

- **来源**：X 书签

- **发布时间**：2026-04-25

- **链接**：[原文](https://x.com/MatthewBerman/status/2047843625510609373)

## 个人评注

本文从美国视角分析 DeepSeek V4 的冲击，核心论点是「够用+免费」对闭源商业模型的威胁。对 Tizer 的启示：

- **OpenClaw 选型参考**：DeepSeek V4 Flash（284B/13B 激活）在成本-性能比上极具竞争力，适合作为 Agent 推理后端

- **Harness 工程价值凸显**：多位评论者（Matt Teufel、AIPropManager 等）指出「harness 比模型更重要」，与 OpenClaw 的工程哲学一致

- **开源模型战略**：作为依赖开源模型的 Agent 开发者，模型的可获取性和部署自由度是核心利益，DeepSeek 的开源策略直接利好

- **蒸馏争议的启示**：蒸馏指控凸显了数据来源的法律模糊地带，OpenClaw 在训练数据方面应保持合规透明
