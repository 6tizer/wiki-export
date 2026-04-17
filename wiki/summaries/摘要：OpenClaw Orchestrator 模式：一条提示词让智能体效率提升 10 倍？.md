---
title: 摘要：OpenClaw Orchestrator 模式：一条提示词让智能体效率提升 10 倍？
type: summary
tags:
- Agent 编排
- OpenClaw
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: Agent, OpenClaw, 自动化, LLM
source_article_url: ''
notion_url: https://www.notion.so/bb4744b7f2b94501aaac1a3fa4bc47c1
notion_id: bb4744b7-f2b9-4501-aaac-1a3fa4bc47c1
---

### 一句话摘要

Orchestrator 模式强调让主 Agent 专注规划与调度、把执行交给子智能体，但其收益只在特定复杂任务中成立，不能被当作通用默认策略。

### 关键洞察

- 多智能体带来的主要红利是并行和角色隔离，而不是“数量越多越强”。

- 把调度规则写入身份或行为文件，会直接影响主 Agent 与子智能体的边界分工。

- 在共享上下文要求高、任务简单或资源有限时，单智能体通常更稳妥。

### 提取的概念

- [Orchestrator 模式](concepts/Orchestrator 模式.md)

- [子智能体](concepts/子智能体.md)

- [SOUL.md](concepts/SOUL.md.md)

- [AGENTS.md](concepts/AGENTS.md.md)

### 原始文章信息

- 作者：@shao__meng \(meng shao\)

- 来源：X书签

- 发布时间：未明确给出

- 链接：[原文](https://x.com/shao__meng/status/2030818206882103640)

### 个人评注

- 这对 Tizer 的启发是：多 Agent 应该成为“复杂任务升级档”，而不是默认开关，尤其在 HITL 场景里更要谨慎控制调度深度。
