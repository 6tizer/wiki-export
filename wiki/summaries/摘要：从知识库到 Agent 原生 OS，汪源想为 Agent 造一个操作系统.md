---
title: 摘要：从知识库到 Agent 原生 OS，汪源想为 Agent 造一个操作系统
type: summary
tags:
- MCP 协议
- 上下文管理
- 长期记忆
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e9729e9342f341dd93c2161ea3c56df8
notion_id: e9729e93-42f3-41dd-93c2-161ea3c56df8
---

**一句话摘要**

remio 发布 Agent 原生操作系统 rOS 和新应用形态 aApp，将软件的第一服务对象从人变为 Agent，颠覆了延续数十年的"以人为核心"的 GUI 设计逻辑，为普通知识工作者提供开箱即用的 Agent 能力。

**关键洞察**

- 核心判断：当下的 Computer Use、MCP、Skill 都是过渡性方案（类比 WAP 时代），本质是让 Agent 适配为人设计的旧软件

- aApp 三大差异：① 后台持续运行+事件触发（vs Skill 用完即走）② 直接访问用户完整工作上下文（vs 手动投喂）③ 自然语言配置（vs 复杂 Prompt 工程）

- 软件设计颠覆：不再需要 GUI，软件只需提供语义清晰的接口；Agent 可自由组合不同厂商 aApp，无需被单一套件（飞书/钉钉）绑定

- 护城河：时间积累的"数字记忆"——用户上下文工程，用得越久迁移成本越高

- 数据主权：所有处理在本地完成，云端只传必要的 LLM API 请求；实时备份 Agent 所有文件操作，支持一键回滚

**提取的概念**

- rOS

- [aApp](concepts/aApp.md)

- Agent 原生操作系统

**原始文章信息**

- 作者：极客公园（连冉）

- 来源：微信公众号

- 发布时间：2026-04-02

- 链接：[https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653102659](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ%3D%3D&mid=2653102659)

**个人评注**

rOS/aApp 的设计哲学与 Tizer 的知识管理体系有交叉——两者都强调数据主权和本地上下文积累。aApp 的"围绕业务模型设计、把调度权交给 Agent"原则可以为 OpenClaw 的 Skill 设计提供参考。
