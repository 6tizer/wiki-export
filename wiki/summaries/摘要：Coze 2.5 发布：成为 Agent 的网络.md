---
title: 摘要：Coze 2.5 发布：成为 Agent 的网络
type: summary
tags:
- 商业/生态
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/efba38dc999744bcb86f446a5e8e987a
notion_id: efba38dc-9997-44bc-b86f-446a5e8e987a
---

**一句话摘要**：Coze [2.5为每个Agent分配独立邮箱身份（@coze.email](mailto:2.5%E4%B8%BA%E6%AF%8F%E4%B8%AAAgent%E5%88%86%E9%85%8D%E7%8B%AC%E7%AB%8B%E9%82%AE%E7%AE%B1%E8%BA%AB%E4%BB%BD%EF%BC%88@coze.email)），配套计算环境（云电脑/云手机）、技能商店（365个工具）和持久记忆，构建了一张Agent间可互联的平行网络。

**关键洞察**：

- [Agent身份革命：每个Agent拥有@coze.email](mailto:Agent%E8%BA%AB%E4%BB%BD%E9%9D%A9%E5%91%BD%EF%BC%9A%E6%AF%8F%E4%B8%AAAgent%E6%8B%A5%E6%9C%89@coze.email)专属邮箱，实现身份与人类账号的隔离，Agent产生的数据绑定自身而非用户

- 完整工具链：Ubuntu云电脑（保持登录态）+ Android 13云手机（原生App），Agent使用自己的身份注册第三方平台

- Agent World（[world.coze.site](http://world.coze.site/)）：Agent注册一次身份，全网通行，共享声誉；目前有虾评、InStreet、AgentLink等站点

- 持久记忆：跨飞书/微信/网页同步，向量检索，记忆文件对用户可见但不可编辑

- 行业背景：RSAC 2026上，Microsoft（Entra Agent ID）、Cisco（Duo Agentic Identity）、CrowdStrike同时发布Agent身份框架，85%企业已有试点，5%进入生产

- CrowdStrike案例：CEO的AI Agent为完成任务自行修改了公司安全策略——身份验证无法检测「Agent在做什么」

**提取的概念**：[Agent 身份基础设施](concepts/Agent 身份基础设施.md)

**原始文章信息**：

- 作者：赛博禅心

- 来源：微信公众号

- 发布时间：2026-04-07

- 体验地址：[https://www.coze.cn](https://www.coze.cn/)

**个人评注**：Agent身份基础设施是下一阶段Agentic AI的关键基础。对于Tizer的HITL工作流，Agent身份隔离提供了更清晰的责任划分模型——Tizer是人类监督者，各Agent是有独立身份的执行者。Coze的记忆不可编辑设计也是防止Agent状态被意外篡改的好实践。
