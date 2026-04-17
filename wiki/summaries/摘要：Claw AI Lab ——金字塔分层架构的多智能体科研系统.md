---
title: 摘要：Claw AI Lab ——金字塔分层架构的多智能体科研系统
type: summary
tags:
- 工作流
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/16fb2bfadcb743a6867af43f9fed67ce
notion_id: 16fb2bfa-dcb7-43a6-867a-f43f9fed67ce
---

**一句话摘要**：Claw AI Lab 通过金字塔分层架构和多智能体团队讨论，让单人也能跑出实验室级的科研效率，影响经由 HITL 闭环反馈持续演化。

**关键洞察**

- **金字塔层级**：研究方向设定 → 方法设计和实验规划 → 代码实现与结果分析，每层专属 Agent、动态调整

- **Claude Code Harness**：Experiment Harness 统一负责时间预算控制、指标上报、异常定义，生成标准化 results.json

- **三种模式**：Lab 讨论模式（跨方向议论达成共识）、独立研究模式（并行快路）、论文复现模式

- **讨论价值**：VLM/VLA/World Model 三方研究员议论，从分歧收敛出更优分层闭环方案，不只给出表面合理答案

- **底层结构**：GitHub: [github.com/Claw-AI-Lab/Claw-AI-Lab](http://github.com/Claw-AI-Lab/Claw-AI-Lab)

**提取的概念**

- Claw AI Lab

- Experiment Harness

**原始文章信息**

- 作者：量子位

- 来源：微信公众号

- 发布时间：2026-04-05

- 链接：[https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247880902](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247880902)

**个人评注**：展示了如何用 Claude Code Harness 实现重度科研流程自动化。Experiment Harness 的管控思路对 OpenClaw 中的流程标准化有参考价值。
