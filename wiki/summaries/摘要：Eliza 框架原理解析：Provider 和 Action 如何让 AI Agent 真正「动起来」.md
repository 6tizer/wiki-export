---
title: 摘要：Eliza 框架原理解析：Provider 和 Action 如何让 AI Agent 真正「动起来」
type: summary
tags:
- Agent 协作模式
- 长期记忆
- 上下文管理
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/bf42cf85950148998e348fd4859dab85
notion_id: bf42cf85-9501-4899-8e34-8fd4859dab85
---

**一句话摘要**：Eliza 框架的 Provider/Action/Evaluator 三件套构建了可插拔的感知-执行-反思循环：Provider 解决 AI 看不到实时信息的问题，Action 解决 AI 只能说不能做的问题。

**关键洞察**

- ElizaOS 三层架构：Provider（感知）+ Action（执行）+ Evaluator（思考）+ Memory（跨会话记忆）

- Provider 模式：每次处理消息时自动调用所有已注册 Provider，返回文本片段拼接为 State 对象注入 Prompt

- Action 模式：每个 Action 包含 validate（是否触发）、handler（执行逻辑）、examples（少量样本）三个核心字段

- Memory 层：将 Provider 和 Action 产生的信息压缩后写入，让 Agent 跨多次对话保持连贯上下文

- 社区反馈：ElizaOS 是「加密项目优先」，文档质量参差不齐，v2 正针对这些问题做系统性改进

**提取的概念**：ElizaOS、Provider 模式、Action 模式、Agent 记忆系统

**原始文章信息**

- 作者：hhhx402

- 来源：X书签

- 链接：[https://x.com/hhhx402/status/1873309705768198645](https://x.com/hhhx402/status/1873309705768198645)

**个人评注**：Eliza 的 Provider/Action/Evaluator 框架设计与 OpenClaw 的 Agent 技能模块设计极具参考价値。
