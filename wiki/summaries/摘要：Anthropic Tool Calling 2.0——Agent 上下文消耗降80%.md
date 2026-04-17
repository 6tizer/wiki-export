---
title: 摘要：Anthropic Tool Calling 2.0——Agent 上下文消耗降80%
type: summary
tags:
- LLM
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-10'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/b4da784e00c74334868f9f9edc54d9fa
notion_id: b4da784e-00c7-4334-868f-9f9edc54d9fa
---

## 一句话摘要

Anthropic 发布 Tool Calling 2.0 四大特性：程序化工具调用、动态网页过滤、工具搜索和输入示例，将 Agent 从「LLM as Router」推向「LLM as Engine」，大幅降低 Token 消耗。

## 关键洞察

- **程序化工具调用**：模型直接输出可执行代码（而非 JSON），在沙箱中用 for 循环和条件分支批量处理，减少 30%-50% Token 消耗

- **动态网页过滤**：在 HTML 抓取和丢入上下文之间插入代码过滤层，精准提取相关信息，平均降低 24% Token 消耗

- **Tool Search 延迟加载**：只保留一个约 500 Token 的 tool_search_tool，其他工具按需动态加载，最高优化 80% 上下文窗口

- **输入示例**：工具定义中加入 Few-Shot 示范，复杂参数处理准确率从 72% 提升到 90%

- **安全挑战**：代码执行沙箱隔离级别成为关键，调试难度呈指数级上升

## 提取的概念

- Tool Calling 2.0

## 原始文章信息

- **作者**：[GoldenSpider.AI](http://goldenspider.ai/)

- **来源**：微信公众号

- **发布时间**：2026-02-27

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=MzU4MTkwMzkxOQ%3D%3D&mid=2247484798&idx=1&sn=aad5f855cce6ee6d0a5cf434b7532d56)

## 个人评注

Tool Search 的延迟加载机制是 MCP 生态扫尾的重要补丁——解决了工具多但 Token 爆炸的矛盾。程序化工具调用让大模型从路由器变成引擎，这一范式转变对 HITL 工作流中的工具编排有直接启发。
