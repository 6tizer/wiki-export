---
title: 摘要：Recipes for serving LLMs locally on RTX 3090s.
type: summary
tags:
- 推理优化
- 模型部署
- 算力基础设施
status: 已审核
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: https://www.notion.so/351701074b688136946add933b67356e
notion_url: https://www.notion.so/Tizer/4cf7630daebb4f979639299aad21dca8
notion_id: 4cf7630d-aebb-4f97-9639-299aad21dca8
---

## 一句话摘要

Qwen 团队发布 FlashQLA 高性能线性注意力内核库，社区同步推出 club-3090 项目，为在消费级 RTX 3090 显卡上本地部署和高效运行大模型（如 Qwen3.6-27B）提供完整的内核优化与部署方案。

## 关键洞察

- **FlashQLA 实现 2-3 倍前向加速和 2 倍反向加速**：基于 TileLang 构建，通过 gate-driven 自动片内 CP、硬件友好的代数重构、融合 warp-specialized 内核三大技术实现显著提速

- **反向传播的 16 级 warp-specialized 流水线是核心技术突破**：在极其紧张的片上内存约束下，将数据搬运、Tensor Core 和 CUDA Core 计算重叠执行

- **club-3090 提供消费级 GPU 的完整 LLM serving 方案**：vLLM 双卡最高 127 TPS，llama.cpp 单卡支持 262K 上下文且无 prefill 悬崖，Docker Compose 一键部署

- **SM90+（Hopper）限制引发社区讨论**：FlashQLA 当前仅支持 H100 级 GPU，RTX 3090/4090 用户需要等待 Ampere/Ada 移植，club-3090 则填补了消费级硬件的空白

- **端侧 agentic 推理是关键应用场景**：线性注意力 + 智能 tiling 使 24GB 显卡也能在 32K+ 上下文下运行 agent 循环

## 提取的概念

- [FlashQLA](entities/FlashQLA.md)

- [club-3090](entities/club-3090.md)

- [TileLang](entities/TileLang.md)

- [GDN Chunked Prefill](concepts/GDN Chunked Prefill.md)

- [Warp Specialization](concepts/Warp Specialization.md)

- [线性注意力](concepts/线性注意力.md)

- [vLLM](entities/vLLM.md)

- [llama.cpp](entities/llama.cpp.md)

## 原始文章信息

- **作者**：@Alibaba_Qwen

- **来源**：X 书签

- **发布时间**：2026-04-29

- **原文链接**：[https://x.com/Alibaba_Qwen/status/2049462758211772663](https://x.com/Alibaba_Qwen/status/2049462758211772663)

- **相关仓库**：

  - [https://github.com/QwenLM/FlashQLA（235★，MIT）](https://github.com/QwenLM/FlashQLA（235★，MIT）)

  - [https://github.com/noonghunna/club-3090（77★，Apache-2.0）](https://github.com/noonghunna/club-3090（77★，Apache-2.0）)

## 个人评注

对 Tizer 的本地推理工作流有直接价值：club-3090 的 Docker Compose 方案可以快速为 OpenClaw 的本地 Agent 后端搭建 Qwen3.6-27B 推理服务；FlashQLA 的线性注意力优化思路在未来 Ampere 移植后也可用于降低本地 agent 循环的延迟。262K 上下文 + tool-use 稳定性的 llama.cpp 路径特别值得关注——这对需要长上下文 + 工具调用的 HITL agent 场景非常关键。
