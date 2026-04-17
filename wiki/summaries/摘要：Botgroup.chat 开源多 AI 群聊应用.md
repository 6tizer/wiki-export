---
title: 摘要：Botgroup.chat 开源多 AI 群聊应用
type: summary
tags:
- LLM
status: 已审核
confidence: medium
last_compiled: '2026-04-10'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/5d5b2a5c4172410abd6676cd7babb971
notion_id: 5d5b2a5c-4172-410a-bd66-76cd7babb971
---

## 一句话摘要

[Botgroup.chat](http://botgroup.chat/) 是一款基于 React + Cloudflare Pages 的开源多 AI 群聊应用，支持多个自定义 AI 角色在同一对话中实时互动。

## 关键洞察

- **Multi-Agent 群聊模式**：多个 AI 角色同时参与对话，模拟真实群聊场景，可用于多视角评估和辩论

- **角色自定义**：用户可定义每个 AI 的名称、性格、使用模型和头像，打造个性化智能体

- **多模型支持**：兼容千问、混元、豆包等多种国产模型，通过环境变量管理 API Key

- **向量数据库上下文记忆**：基于 Pinecone + OpenAI 嵌入实现跨对话的上下文检索，保持对话连贯性

- **Cloudflare Pages 一键部署**：Fork 仓库后通过 Cloudflare Dashboard 快速配置和部署

## 提取的概念

- Multi-Agent 群聊

- 向量数据库上下文记忆

## 原始文章信息

- **作者**：蚝油菜花

- **来源**：微信公众号

- **发布时间**：2025-03-14

- **链接**：[原文链接](http://mp.weixin.qq.com/s?__biz=MzkyMzc2MDY1OA%3D%3D&mid=2247494074&idx=1&sn=6d9da93f572cea2580bf590540ad67b8)

## 个人评注

多 AI 角色群聊的方案对 Tizer 的内容管道有启发——可以让多个 Agent 分别从不同角度（技术、产品、用户体验）评审内容，形成更全面的反馈。向量数据库的上下文记忆方案也是 Agent 记忆系统的一个轻量级参考实现。
