---
title: 摘要：56% → 92%：Karpathy autoresearch 让 skill 成功率直接起飞
type: summary
tags:
- Agent 协作模式
- 训练/微调
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Skill 开发, Agent, 开源项目
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1b66b96fa0444d6fa10de49a27149189
notion_id: 1b66b96f-a044-4d6f-a10d-e49a27149189
---

**一句话摘要**

Karpathy 开源的 autoresearch 让 AI Agent 在固定时间预算内自主循环实验，通过将模糊目标转化为可量化的二元 Eval，将 Skill 成功率从 56% 提升至 92%。

**关键洞察**

- 核心方法论：将模糊需求（"写得自然一点"）转化为 yes/no 二元 Eval，避免主观量表带来的不稳定性——Eval 黄金法则：每条必须是是非题

- 自主研究循环：[program.md](http://program.md/)（人类写策略）→ AI 修改 [train.py](http://train.py/) → 固定 5 分钟训练 → 评估指标 → 保留/丢弃 → 循环；约 12 次/小时，100 次/夜

- 可迁移性：同样方法论应用于代码性能优化，页面加载从 1100ms 降至 67ms（67 轮迭代）

- Changelog 即资产：进化历史记录是模型升级或平台迁移时最有价值的参考

- 本质是强化学习：评分规则 = reward signal，让 AI 自主找到最优解

**提取的概念**

- autoresearch

- Eval 设计方法论

- Skill 优化循环

**原始文章信息**

- 作者：字节前端

- 来源：微信公众号

- 发布时间：2026-03-27

- 链接：[https://mp.weixin.qq.com/s?__biz=MzA3MDkzNjM3MA==&mid=2455675564&idx=1&sn=70889bda6cc3e1b9466a0e0f2dca74fe](https://mp.weixin.qq.com/s?__biz=MzA3MDkzNjM3MA%3D%3D&mid=2455675564&idx=1&sn=70889bda6cc3e1b9466a0e0f2dca74fe)

**个人评注**

autoresearch 的方法论对 Tizer 的工作流有直接价值——Skill 优化的 Eval 框架可直接应用于 OpenClaw Skill 调优。"把模糊感觉变成可测试的是非题"是提升 Agent 稳定性的核心思路，与 Wiki Compiler 的编译质量控制方向高度一致。
