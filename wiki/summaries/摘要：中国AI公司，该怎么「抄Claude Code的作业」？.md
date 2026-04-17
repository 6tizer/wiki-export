---
title: 摘要：中国AI公司，该怎么「抄Claude Code的作业」？
type: summary
tags:
- Coding Agent
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化, Claude
source_article_url: ''
notion_url: https://www.notion.so/d5616e1973f648f8b49fa0aa7f011f9d
notion_id: d5616e19-73f6-48f8-b49f-a0aa7f011f9d
---

**一句话摘要**：极客公园深度分析 Claude Code 泳露源码的四大可学点（工具描述精细化、记忆分层、情绪感知工程化、KAIROS 守护进程模式），并指出真正的学习姿态应是理解设计决策背后的 tradeoff 而非直接 fork 代码。

---

## 关键洞察

- **工具描述就是产品力**：每个工具的 prompt 描述进行了极其精细的调优（什么时候用、什么时候不用、用完怎处理结果），光工具描述层就有 2.9 万行 TypeScript

- **记忆分层**：热数据始终在线，温数据按需加载，冷数据只做索引；不能把所有历史对话塞进去

- **情绪感知工程化**：用正则表达式检测用户是否在骡所，比用模型推理要快得多且便宜；所有问题不需丢给大模型

- **KAIROS 尴听进程方向**：不是“更快地回答问题”，而是“在你没有问问题的时候，已经在工作”

- **抗警示**：学习您的不能直接 fork 51 万行，而要针对自己的模型特点重新实现

## 原始文章信息

- **作者**：极客公园

- **来源**：微信公众号

- **发布日期**：2026-04-01

- **链接**：[https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653102545](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ%3D%3D&mid=2653102545)

## 个人评注

极客公园的分析角度对 Tizer 最有实用价值，尤其是工具描述精细化和记忆分层设计思路可直接应用于自建的 OpenClaw 局。
