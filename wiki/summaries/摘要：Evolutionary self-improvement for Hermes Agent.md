---
title: 摘要：Evolutionary self-improvement for Hermes Agent
type: summary
tags:
- 提示工程
- 推理优化
- Harness 工程
status: 已审核
confidence: high
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: https://www.notion.so/341701074b6881c6a791fb6dc3573211
notion_url: https://www.notion.so/Tizer/0f542a8cbed04494b1b6bbfa81491a78
notion_id: 0f542a8c-bed0-4494-b1b6-bbfa81491a78
---

## 一句话摘要

Hermes Agent Self-Evolution 是 Nous Research 基于 DSPy + GEPA 构建的自进化优化管线，它让 Hermes Agent 能围绕 skill、工具描述、system prompt 乃至代码，通过执行轨迹驱动的演化搜索持续改进表现。

## 关键洞察

- GEPA 不是纯黑箱强化学习，而是读取执行轨迹来做更有针对性的 prompt 与 skill 变异，因此在数据效率上明显更高。

- 当前已实现 Phase 1 的技能文件优化，后续规划扩展到工具描述、system prompt、代码实现与持续改进闭环。

- 优化流程强调 guardrails，包括测试通过、体积限制、语义不漂移与人工 PR 审核，避免自我改写失控。

- 项目不依赖 GPU 训练，主要通过 API 调用完成变异、评估与筛选，单次优化成本约为 2–10 美元。

- 对 Coding Agent 而言，prompt 工程的重心正在从“手工微调”转向“设计评估数据、反馈回路与约束机制”。

## 提取的概念

- [Hermes Agent Self-Evolution](entities/Hermes Agent Self-Evolution.md)

- [GEPA](concepts/GEPA.md)

- [DSPy](entities/DSPy.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [技能自我进化](concepts/技能自我进化.md)

- [System Prompt 工程](concepts/System Prompt 工程.md)

## 原始文章信息

- 作者：@KKaWSB

- 来源：X书签

- 发布时间：2026/04/12

- 原文链接：[https://x.com/KKaWSB/status/2043119101028274268](https://x.com/KKaWSB/status/2043119101028274268)

- 相关仓库：[https://github.com/NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution)

## 个人评注

- 对 Tizer 的工作流最有启发的，不是“自动改 prompt”本身，而是把 **生成 → 评估 → 约束 → 回写** 做成可复用的编译流水线。

- 如果未来要把 OpenClaw / 内容管线里的 Skill、提示词模板、审核规则做成持续优化系统，这类由执行轨迹驱动的演化框架很值得对照吸收。
