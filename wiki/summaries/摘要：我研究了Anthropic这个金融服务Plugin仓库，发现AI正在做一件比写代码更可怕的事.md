---
title: 摘要：我研究了Anthropic这个金融服务Plugin仓库，发现AI正在做一件比写代码更可怕的事
type: summary
tags:
- 开发工具
status: 已审核
confidence: medium
last_compiled: '2026-04-10'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/bda0ddc79ab84953aaaaedbfab234e7d
notion_id: bda0ddc7-9ab8-4953-aaaa-edbfab234e7d
---

## 一句话摘要

Anthropics 金融服务 Plugin 仓库揭示了 MCP → Skills → Plugin 的三层演进路线，正在将传统软件的竞争壁垒从「能不能做出来」变为「能不能比 Plugin 做得更好」。

## 关键洞察

- **MCP → Skills → Plugin 是三层递进关系**：MCP 解决连通性（AI 能连接什么）、Skills 解决能力（AI 会做什么）、Plugin 解决替代性（AI 替代什么）。三层叠加形成完整的 AI 工作伙伴。

- **Plugin = Skills + Connectors + Slash Commands + Sub-Agents**：每个 Plugin 是针对特定职能的完整方案，捆绑了方法论、数据接入、触发命令和多步骤自主执行。

- **Plugin 本质是一个市场（Marketplace）**：类比 App Store，Anthropic 开放第三方开发者贡献 Plugin，可能重塑软件行业分层结构。

- **Skills 的本质是将人的经验和工作流变为 AI 可读取的结构化知识**：从给人看的 SOP/文档，到给 AI 用的 Skills，这个转变比表面看起来影响深远。

- **Claude Sonnet 4.5 在金融任务上以 55.3% 准确率排名第一**：Citi、BCI、Coinbase、Visa 已在使用。

## 提取的概念

- MCP 协议

- Claude Cowork Skills

- [Knowledge Work Plugins](concepts/Knowledge Work Plugins.md)

- [Plugin Marketplace](concepts/Plugin Marketplace.md)

- 插件化架构（已有词条）

## 原始文章信息

- **作者**：老码小张

- **来源**：微信公众号

- **发布时间**：2026-02-28

- **链接**：[https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg==&mid=2247492719&idx=1&sn=c56204c0b610a7d054d98af6115cce1f](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247492719&idx=1&sn=c56204c0b610a7d054d98af6115cce1f)

## 个人评注

对 MCP → Skills → Plugin 演进路线的梳理清晰易懂。Plugin Marketplace 的概念对 Tizer 的 OpenClaw Skill 生态观察有启发——从 content pipeline 角度看，如果写作、内容分发等环节也能被 Plugin 化，效率会大幅提升。不过文章主要是观点论述，技术深度有限，金融 Plugin 的具体实现细节较少。
