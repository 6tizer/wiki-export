---
title: 摘要：方舟Coding Plan——国产模型一键调用按请求计费
type: summary
tags:
- LLM
- OpenClaw
status: 已审核
confidence: medium
last_compiled: '2026-04-10'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/d6dd0891fff54b64a3baed777cef0a61
notion_id: d6dd0891-fff5-4b64-a3ba-ed777cef0a61
---

## 一句话摘要

火山引擎「方舟Coding Plan」提供一个 API Key 调用多款国产模型（Doubao、Kimi、GLM、DeepSeek），改为按请求次数计费而非按 Token，解决 Agent 类工具高 Token 消耗的成本问题。

## 关键洞察

- **按请求计费解决 Agent 费用痛点**：Agent 算力消耗是 Chatbot 的 100-1000 倍，按 Token 计费普通人扰不住

- **多模型一个 Key**：支持 doubao-seed-2.0-code、kimi-k2.5、glm-4.7、deepseek-v3.2 等

- **双协议兼容**：同时支持 Anthropic 协议和 OpenAI 协议接入

- **字节算力保障**：背靠字节跳动算力资源，稳定性和速度有保障

## 提取的概念

- Agent 成本控制（已有概念，追加引用）

## 原始文章信息

- **作者**：沃垠AI

- **来源**：微信公众号

- **发布时间**：2026-03-02

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=MzIwMTU5OTQ1Nw%3D%3D&mid=2653725180&idx=1&sn=b2d0eb04cfe929f141fad40844293ed9)

## 个人评注

带有较强推广性质，但按请求计费模式对 Agent 生态确实是重要创新。双协议接入设计对 OpenClaw 等工具的兼容性友好。
