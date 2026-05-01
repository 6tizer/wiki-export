---
title: 摘要：EdgeClaw：把 Claude Code 体验带到 OpenClaw
type: summary
tags:
- OpenClaw
- 长期记忆
- 推理优化
- 多Agent协作
- Agent 协作模式
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: OpenClaw, Agent, LLM, 自动化, Claude, 记忆
source_article_url: ''
notion_url: https://www.notion.so/Tizer/12bb594d2d3d425b8e80b3f5afbe7796
notion_id: 12bb594d-2d3d-425b-8e80-b3f5afbe7796
---

**一句话摘要**：EdgeClaw（清华/人大/面壁智能）为OpenClaw增加了Claude Code级别的长期记忆（ClawXMemory三层架构）、成本感知路由器（ClawXRouter，节省58%费用）和三层隐私保护。

**关键洞察**：

- ClawXMemory三层架构：L2项目记忆（高级汇聚）→L1记忆片段（结构化摘要）→L0原始对话，沿记忆树主动推理，优于传统向量检索

- ClawXRouter：本地小模型（MiniCPM/Qwen3.5）作为Judge，自动将60-80%简单请求路由到便宜模型，PinchBench实测节省58%成本且分数提升6.3%

- 三层隐私保护：S1（安全/云端）→S2（敏感/脱敏后发送）→S3（私密/仅本地），双引擎检测（规则+本地LLM）

- ClawXKairos：Tick调度的自驱动Agent循环，支持后台命令自动化和异步子代理

- ClawXGovernor：三层Hook中间件，30轮调用节省85% Token

- ClawXSandbox：基于系统沙盒（bwrap/sandbox-exec），零Docker开销

**提取的概念**：EdgeClaw（已有Wiki条目，需追加引用）

**原始文章信息**：

- 作者：小华同学ai

- 来源：微信公众号

- 发布时间：2026-04-07

- GitHub：[https://github.com/OpenBMB/EdgeClaw](https://github.com/OpenBMB/EdgeClaw)

**个人评注**：EdgeClaw的ClawXRouter成本优化策略对Tizer的工作流有直接价值——Wiki Compiler Agent可以借鉴「根据任务复杂度路由到不同模型」的思路，为简单摘要任务使用更便宜的模型。ClawXMemory的三层架构也是构建长期记忆系统的参考实现。
