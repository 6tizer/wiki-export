---
title: 摘要：能用脚本就别用Agent。
type: summary
tags:
- 工作流
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, 经验分享
source_article_url: ''
notion_url: https://www.notion.so/653d99f7ef5342c1b3fcb23d9c935c6d
notion_id: 653d99f7-ef53-42c1-b3fc-b23d9c935c6d
---

**一句话摘要**：AI 任务分配应遵循「脚本优先 → Skill 次之 → Agent 最后」的金字塔原则，让 Agent 专注于无法提前规划的创造性任务，不断将已确定的逻辑下沉为 Skill 或脚本。

**关键洞察**

- 三层优先级：① 逻辑固定的可预见任务 → 脚本；② 需要泛化能力但不需要自主决策的 → Skill；③ 需要动态规划、根据中间结果调整策略的 → Agent

- 错误地将所有任务交给 Agent 会导致"慢、贵、不稳定"

- 最佳模式：Agent 创造工具，工具执行任务——形成能力下沉的正向循环

- Skill 的价值在于封装泛化能力：无法写死逻辑，但又不需要多步骤规划

- 真正的 Agent 使用场景：开发新脚本、做究极详细的竞品体验报告等"不知道中间步骤"的任务

**提取的概念**

- [Agent-Skill-Script 三层架构](concepts/Agent-Skill-Script 三层架构.md)（AI 任务分配金字塔模型）

**原始文章信息**

- 作者：数字生命卡兹克

- 来源：微信公众号

- 发布时间：2026-03-17

- 链接：[https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647680643&idx=1&sn=b717e3587060f26c2f13bd4d0a6725e1](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA%3D%3D&mid=2647680643&idx=1&sn=b717e3587060f26c2f13bd4d0a6725e1)

**个人评注**

这个框架与 Tizer 的 HITL 工作流设计高度一致。在设计 OpenClaw 工作流时，应优先问：这个任务能否先用脚本/Skill 解决？只有真正需要动态判断的部分才值得消耗 Agent Token。
