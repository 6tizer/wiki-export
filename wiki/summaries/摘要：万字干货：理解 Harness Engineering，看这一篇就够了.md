---
title: 摘要：万字干货：理解 Harness Engineering，看这一篇就够了
type: summary
tags:
- Agent 编排
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/011ab480963044c38f16b0f29de6f7b5
notion_id: 011ab480-9630-44c3-8f16-b0f29de6f7b5
---

**一句话摘要**：Harness Engineering是“AI工程化的驾驭体系”，本文从Claude Code实践中提炼，系统性总结Harness包含什么、为什么需要、如何设计和如何实现。

**关键洞察**：

- 核心隐喻：AI Agent = SOTA模型（野马）+ Harness（驾驭系统）= 千里马

- Harness是除LLM本身之外让Agent真正能干活的一切基础设施

- PPAF闭环：感知→规划→行动→反思

- R.E.S.T模型：可靠性、效率、安全性、可观测性

- Harness为带边界控制的REPL容器：Read→ Eval→ Print→ Loop

- 六大设计原则：为失败而设计、契约优先、默认安全、决策与执行分离、万物皆可度量、数据驱动进化

- 核心靡证：3人小组在五个月内构建了百万行代码级别产品，合并了1500个 Pull Request

**提取的概念**：Harness 工程（已有Wiki条目，需追加引用）

**原始文章信息**：

- 作者：[TRAE.ai](http://trae.ai/) 和咊鱼用户

- 来源：微信公众号

- 发布时间：2026-04-10

**个人评注**：目前中文圈对Harness Engineering最系统全面的介绍。PPAF闭环和R.E.S.T模型对设计Wiki Compiler等多层次Agent系统有直接指导价值。
