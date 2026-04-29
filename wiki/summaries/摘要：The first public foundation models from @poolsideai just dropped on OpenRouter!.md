---
title: 摘要：The first public foundation models from @poolsideai just dropped on OpenRouter!
type: summary
tags:
- 代码生成
- 模型部署
- 商业/生态
status: 已审核
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: https://www.notion.so/351701074b6881c7abc6f15f57187679
notion_url: https://www.notion.so/Tizer/44a22cc12b9649159bb433b5139a957c
notion_id: 44a22cc1-2b96-4915-9bb4-33b5139a957c
---

## 一句话摘要

Poolside 首批公开基础模型 Laguna M.1 和 Laguna XS.2 登陆 OpenRouter，限时免费提供，引发社区关于开源编码模型定价杠杆与闭源模型竞争力的讨论。

## 关键洞察

- **双模型首发**：Laguna M.1（225B MoE / 23B 激活）为旗舰编码 Agent 模型，Laguna XS.2（33B MoE / 3B 激活）为轻量高效版，均专注 agentic coding 和长时域任务

- **限时免费策略**：OpenRouter 提供限时免费访问，被社区解读为在企业客户签约前通过开放分发抢占开发者采纳率的市场策略

- **开源定价杠杆**：社区热议 225B MoE（23B 激活）免费开源模型在编码基准上击败 Claude Sonnet 4.6，可能动摇闭源编码模型的定价优势

- **实际落地质疑**：社区指出 128K 上下文 / 8K 输出的规格已不算前沿，且 agentic coding 评测在多文件仓库场景下仍易失真，需关注工具调用可靠性和重试成本

- **Apache 2.0 + 单 GPU 对 SMB 的价值**：XS.2 的开源许可和单 GPU 运行能力为中小企业提供了 API 成本上限可控的自托管选项

## 提取的概念

- [Laguna M.1](entities/Laguna M.1.md)

- [Laguna XS.2](entities/Laguna XS.2.md)

- [Poolside](entities/Poolside.md)

- [OpenRouter](entities/OpenRouter.md)

- [Agentic Coding](concepts/Agentic Coding.md)

## 原始文章信息

- **作者**：@OpenRouter

- **来源**：X 书签

- **发布时间**：2026-04-28

- **原文链接**：[https://x.com/OpenRouter/status/2049145538373947541](https://x.com/OpenRouter/status/2049145538373947541)

## 个人评注

- **分发即采纳**：OpenRouter 限时免费的打法是典型的开发者生态增长策略——先让开发者在工作流中跑通模型，再转化为付费用户。这对 OpenClaw 的分发思路有参考意义

- **基准 vs 实战**：社区讨论揭示了一个关键矛盾——编码基准分数可能不代表真实 Agent 工作流的可靠性。128K/8K 的规格限制和多文件场景下的 eval 失真问题值得在 HITL 管线选型时警惕

- **开源编码模型格局**：继 DeepSeek 之后，Poolside 再次证明 MoE 架构在编码任务上的竞争力，闭源模型的护城河正在被侵蚀
