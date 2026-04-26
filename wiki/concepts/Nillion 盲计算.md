---
title: Nillion 盲计算
type: concept
tags:
- 安全/隐私
- Crypto/DeFi
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/78d28b9ab2eb441b9ffea03a67d69ac6
notion_id: 78d28b9a-b2eb-441b-9ffe-a03a67d69ac6
---

Nillion 是基于多方安全计算（MPC）的通用盲计算网络，通过"在不解密数据的前提下直接对加密数据计算"，解决 AI Agent 个性化与数据隐私的根本矛盾。

## 核心技术

- **盲计算（Blind Computation）**：对加密数据直接运算，任何一方都无法还原原始数据

- **Curl 协议**：Nillion 自研 MPC 协议，支持不解密条件下的复杂非线性计算

- **技术组合**：MPC（多方安全计算）+ FHE（同态加密）+ TEE（可信执行环境）+ ZKP（零知识证明）

## 双层架构

- **Nilchain（协调层）**：接收用户请求、处理交易费用，类似传统区块链

- **PETnet（隐私增强技术网络）**：多集群节点实际执行盲计算任务

## 三大产品模块

- **nilDB**：加密数据库，数据以密文形式存储

- **nilVM**：分布式计算引擎，在加密数据上执行计算

- **nilAI**：隐私 AI 推理，AI 模型在不见明文的情况下进行推理

## 应用场景

医疗数据联合训练、企业代码安全审计、个人 AI 助手隐私保护、DeFi 隐私补偿

## 来源引用

- [摘要：Nillion：为 AI Agent 个性化而生的「盲计算」基础设施](summaries/摘要：Nillion：为 AI Agent 个性化而生的「盲计算」基础设施.md)
