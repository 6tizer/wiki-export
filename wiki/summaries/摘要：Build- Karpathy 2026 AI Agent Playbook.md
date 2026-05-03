---
title: '摘要：Build: Karpathy 2026 AI Agent Playbook'
type: summary
tags:
- Harness 工程
- Agent 协作模式
status: 已审核
confidence: medium
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: https://www.notion.so/355701074b6881ee99a9c46c107b52e2
notion_url: https://www.notion.so/Tizer/a52bc76229b14bc88f380d028e41e088
notion_id: a52bc762-29b1-4bc8-8f38-0d028e41e088
---

## 一句话摘要

Karpathy 警告 90% 的 AI 建议在 6 个月内过时，2026 年 AI Agent 的正确路径是构建 partial-autonomy 应用、采用 context engineering，并在 human-in-the-loop 监督下运行。

## 关键洞察

- **90% 的 AI 建议半年内失效**：大多数工具甚至活不过 90 天，框架每季度都在腐烂，选择技术栈时需关注持久模式而非短期热点

- **构建 partial-autonomy 应用**：不要追求全自主 Agent，而是提供 autonomy slider（自主度滑块），让用户在完全监督和高度自主之间自由调节

- **将 LLM 视为 1960s 操作系统**：通过 vibe coding、human-AI supervision loop 和 agent-friendly flow 来「编程」LLM，而非期待它独立完成一切

- **加速 generate-verify cycle**：Agent 的核心价值在于加速「生成-验证」循环，而非替代人类判断

- **生产环境中真正存活的是**：tight scoping（精准范围界定）、failure handling（故障处理）和 constraint architecture（约束架构），而非 GitHub Stars 或框架流行度

## 提取的概念

- [Context Engineering](concepts/Context Engineering.md)

- [Autonomy Slider](concepts/Autonomy Slider.md)

- [Vibe Coding](concepts/Vibe Coding.md)

- [Andrej Karpathy](entities/Andrej Karpathy.md)

## 原始文章信息

- **作者**: @DataChaz（转发 @rohit4verse 的帖子，引用 Karpathy YC AI Startup School 演讲）

- **来源**: X书签

- **发布时间**: 2026-05-01

- **链接**: [原文推文](https://x.com/DataChaz/status/2050114234973863975)

## 个人评注

Karpathy 强调的 partial-autonomy 和 autonomy slider 模式与 OpenClaw 的 HITL 架构高度一致——OpenClaw 本身就是在人类监督下运行的 Agent 系统，通过可配置的自主等级来平衡效率和安全。「框架每季度腐烂」的观察也印证了 Harness 工程的价值：将 Agent 的执行环境、验证机制和安全边界作为持久基础设施来构建，而非依赖短命的框架封装。
