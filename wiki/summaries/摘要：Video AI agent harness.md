---
title: 摘要：Video AI agent harness
type: summary
tags:
- 视频/3D
- Harness 工程
- 多Agent协作
status: 已审核
confidence: medium
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b6880488db6efa3ef9614ad
notion_url: https://www.notion.so/Tizer/044093db2aeb4d47864e843356c405ad
notion_id: 044093db-2aeb-4d47-864e-843356c405ad
---

## 一句话摘要

这篇文章系统梳理了 8 个开源视频 Agent 框架，指出视频 AI 正从单点生成工具，走向由 harness、工作流编排与多 Agent 协作驱动的完整生产系统。

## 关键洞察

- 当前开源视频 Agent 大致可分为三类：端到端导演型、通用工作流底座型，以及视频理解/编辑型

- 真正的差异化不只在模型能力，更在 harness、工具编排、记忆与流程控制层

- Dify 与 [ComfyUI](entities/ComfyUI.md) 代表“上层编排 + 下层生成引擎”的组合思路，适合搭建可扩展视频流水线

- [UniVA](entities/UniVA.md)、[ViMax](entities/ViMax.md) 等项目说明，多 Agent 分工已成为复杂视频生成的重要方向

- [VideoAgent](entities/VideoAgent.md) 与 [FireRed-OpenStoryline](entities/FireRed-OpenStoryline.md) 则更强调围绕编辑意图的人机协作与后期处理

## 提取的概念

- [Agent Harness](concepts/Agent Harness.md)

- [多 Agent 协作工作流](concepts/多 Agent 协作工作流.md)

- [节点式工作流](concepts/节点式工作流.md)

- [意图驱动编辑](concepts/意图驱动编辑.md)

- [OpenMontage](entities/OpenMontage.md)

- [UniVA](entities/UniVA.md)

- [Dify](entities/Dify.md)

- [ComfyUI](entities/ComfyUI.md)

- [VideoAgent](entities/VideoAgent.md)

- [Director](entities/Director.md)

- [ViMax](entities/ViMax.md)

- [FireRed-OpenStoryline](entities/FireRed-OpenStoryline.md)

## 原始文章信息

- 作者：未填写

- 来源：X书签

- 发布时间：未填写

- 外部链接：未填写

- 源条目：开源视频 Agent 框架全景扫描：八个项目，哪个适合你？

## 个人评注

这类视频 Agent 框架对 Tizer 的启发，不在于马上替换现有内容生产工具，而在于明确了未来视频内容流水线的分层结构：上层用 Agent 负责任务拆解与质量控制，中层用工作流负责编排，下层由具体模型和节点式工具执行。对于需要 HITL 审核的内容工厂，这种结构尤其适合逐步落地。
