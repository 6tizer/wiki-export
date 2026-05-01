---
title: 摘要：Anthropic 封杀 OpenClaw 订阅额度事件始末
type: summary
tags:
- 商业/生态
- OpenClaw
- Agent 安全
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: OpenClaw, Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c55aa53666ff4ac1942be1534a8be581
notion_id: c55aa536-66ff-4ac1-942b-e1534a8be581
---

**一句话摘要**：Anthropic 从 2026 年 4 月 4 日起正式封杀 OpenClaw 使用 Claude 订阅额度，强制按量计费，此举被解读为因 OpenClaw 创始人 Peter Steinberger 加入 OpenAI 而触发的商业竞争动作。

**关键洞察**

- **平台锁定策略**：Anthropic 经历四个阶段——悄悄封杀 OAuth token → 修改服务条款 → 大规模封号 → 正式邮件通知，最终将开发者引向自家 Claude Cowork

- **经济影响**：$200/月 Max 订阅用户的实际算力成本高达 $5000/月，订阅制被 Agent 持续跑满导致 Anthropic 严重亏损

- **导火索**：OpenClaw 创始人 Peter Steinberger 加入 OpenAI，Anthropic 随即将其从订阅白名单剔除

- **OpenAI 反向操作**：OpenAI 明确允许 Codex 订阅在 OpenClaw 等第三方使用，并向 OpenClaw 开源维护者免费提供 ChatGPT Pro

- **安全漏洞**：OpenClaw 存在 CVSS 8.8 高危漏洞（CVE-2026-25253），公网暴露实例超 3 万个

**提取的概念**

- OpenClaw

- AI 平台锁定策略

- Claude Cowork

**原始文章信息**

- 作者：新智元

- 来源：微信公众号

- 发布时间：2026-04-04

- 链接：[https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652689665](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652689665)

**个人评注**：这是直接影响 Tizer OpenClaw 工作流的重大事件。Anthropic 封杀 OpenClaw 意味着所有依赖 Claude 订阅的 OpenClaw Agent 需要迁移到按量计费或切换模型。需要关注 Claude Cowork 的功能演进，评估是否影响现有 pipeline。
