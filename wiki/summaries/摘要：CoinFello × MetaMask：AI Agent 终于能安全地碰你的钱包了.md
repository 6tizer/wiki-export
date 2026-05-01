---
title: 摘要：CoinFello × MetaMask：AI Agent 终于能安全地碰你的钱包了
type: summary
tags:
- 链上协议
- Agent 安全
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, OpenClaw, 自动化, LLM
source_article_url: https://www.notion.so/335701074b6881f49014fac2a94b3677
notion_url: https://www.notion.so/Tizer/45528ce3639c4c6589495ab8ffbe57e7
notion_id: 45528ce3-639c-4c65-8949-5ab8ffbe57e7
---

## 一句话摘要

CoinFello 与 MetaMask 结合智能账户和委托权限，把 AI Agent 的链上执行从“交出私钥”改造成“按边界授权”。

## 关键洞察

- 文章核心不是让 Agent 更会交易，而是先把钱包权限做成安全沙箱。

- ERC-4337 与 ERC-7710 的组合，让链上自动化可以精确限制操作类型和额度。

- CoinFello 把 DeFi 交互封装成可被 Agent 调用的 Skill，降低了自然语言发起链上动作的门槛。

- 这一方向的分歧在于“委托授权”与“链上执行拦截”谁更安全。

## 提取的概念

- [CoinFello](entities/CoinFello.md)

- [MetaMask](entities/MetaMask.md)

- [ERC-4337](concepts/ERC-4337.md)

- [ERC-7710](entities/ERC-7710.md)

## 原始文章信息

- 作者：xincctnnq

- 来源：X书签

- 发布时间：2026-03-11

- 链接：[原文](https://docs.coinfello.com/agent/skill)

## 个人评注

这篇内容对 Tizer 的启发不是“再接一个链上 Skill”，而是先把权限边界做成默认层。以后如果要做 HITL 的链上工作流，授权粒度会比模型能力更关键。
