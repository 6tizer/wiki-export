---
title: 摘要：Anthropic 最新博客：MCP 没死，它又来了
type: summary
tags:
- Agent 技能
- Agent 编排
status: 已审核
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b68817785a5ceda6489a48f
notion_url: https://www.notion.so/3b340ea96daa41548d7c720a4bda72fe
notion_id: 3b340ea9-6daa-4154-8d7c-720a4bda72fe
---

## 一句话摘要

Anthropic 这篇实践博客的核心不是简单为 MCP 翻案，而是重新给 MCP 划定边界：在本地开发场景里 CLI + Skills 仍然更优，但在云端生产环境中，MCP 可以借助按需找工具、把中间结果留在执行层等新做法，把成本与组合性问题压到可接受范围，成为标准化接入层。

## 关键洞察

- Anthropic 将 Agent 连接外部系统分成 API、CLI、MCP 三条路径，强调适用场景取决于运行环境，而不是谁“一统天下”。

- 针对 MCP 最受诟病的 token 与 schema 膨胀问题，博客提出 **Tool Search**：按任务意图动态检索相关工具，而不是把全部工具定义一次性塞进上下文。

- 博客提出 **程序化工具调用**：把工具返回结果留在代码沙箱中循环、过滤、聚合，只把最终结果返回给模型，从而减少多步工作流的上下文消耗。

- Cloudflare 的案例说明，好的 MCP 服务可以借鉴 CLI 的思路，只暴露少量通用接口，再通过脚本执行复杂操作，这就是一种 **代码编排**。

- Anthropic 把 **Skills** 明确放到编排层：MCP 负责连接能力，Skills 负责告诉 Agent 如何用这些连接完成具体任务。

## 提取的概念

- [MCP 协议](concepts/MCP 协议.md)

- [Tool Search](concepts/Tool Search.md)

- [程序化工具调用](concepts/程序化工具调用.md)

- [代码编排](concepts/代码编排.md)

- [Agent Skills](concepts/Agent Skills.md)

- [Anthropic](entities/Anthropic.md)

- [Claude Cowork](entities/Claude Cowork.md)

## 原始文章信息

- 作者：AGI Hunt

- 来源：微信

- 发布时间：2026-04-23 15:10（Asia/Shanghai）

- 原文链接：[Anthropic 博客解读文章](https://mp.weixin.qq.com/s?__biz=MzA4NzgzMjA4MQ%3D%3D&mid=2453483055&idx=1&sn=aca9f531006d4ae5c50feb6d4cc5229e&chksm=86732b338b1b484418b20621dcb0a955f7260a88990b6194acc039e8dc4969bb5bf99c3b9f8e#rd)

- 源文章页面：Anthropic 最新博客：MCP 没死，它又来了

## 个人评注

这篇文章对 Tizer 当前工作流的启发很直接：本地开发与研究阶段，仍然应该优先使用 CLI + Skills 这类轻量方案；但一旦进入云端、多客户端、需要统一认证与远程接入的场景，就需要一个像 MCP 这样的标准协议层。更重要的是，编排设计要坚持三个原则：**按需暴露工具、把中间状态留在执行层、让能力接口尽量薄且可组合**。
