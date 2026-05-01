---
title: 摘要：Nillion：为 AI Agent 个性化而生的「盲计算」基础设施
type: summary
tags:
- Agent 协作模式
- 算力基础设施
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM
source_article_url: ''
notion_url: https://www.notion.so/Tizer/fc3bf39fc49d45a8a874b1d02a2d0e4b
notion_id: fc3bf39f-c49d-45a8-a874-b1d02a2d0e4b
---

**一句话摘要**：Nillion 是基于 MPC（多方安全计算）的通用盲计算网络，通过"在不解密数据的前提下直接对加密数据计算"解决 AI Agent 个性化与数据隐私的根本矛盾。

## 关键洞察

- 盲计算核心：MPC + FHE + TEE 三种技术组合，自研 Curl 协议支持不解密条件下的复杂非线性计算

- 三大模块：nilDB（加密数据库）、nilVM（分布式计算引擎）、nilAI（隐私 AI 推理）

- 双层架构：Nilchain（协调层）+ PETnet（隐私增强技术网络，实际执行盲计算）

- 不绑定单一链：可插拔"隐私中间件"，已与 NEAR 协议集成，支持以太坊/Solana 等

- 团队：Hedera/Reserve Protocol 联合创始人 + 高盛/Uber 创始工程师 + 皇家霧洛威密码学教授

## 提取的概念

- **Nillion 盲计算** — MPC + FHE + TEE 的通用隐私计算基础设施

- **TEE 可信执行环境** — Nillion 技术栈之一

## 原始文章信息

- **作者**：@FourPillarsFP（Four Pillars，@Steve_4P 撰稿）

- **来源**：X书签

- **发布时间**：2025-01-07

- **链接**：[https://4pillars.io/en/articles/nillion-private-computation](https://4pillars.io/en/articles/nillion-private-computation)

## 个人评注

Nillion 的盲计算技术为 OpenClaw 的 HITL 数据隐私问题提供了技术解：用户个人数据可以加密方式参与 Agent 训练，而不暴露给任何服务方。这是隐私保护 AI Agent 个性化的关键基础设施方向。
