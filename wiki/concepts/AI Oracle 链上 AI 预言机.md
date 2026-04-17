---
title: AI Oracle 链上 AI 预言机
type: concept
tags:
- Crypto/DeFi
status: 审核中
confidence: medium
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/09768a34fd69443f99a1cea9d3588ffa
notion_id: 09768a34-fd69-443f-99a1-cea9d3588ffa
---

## 定义

AI Oracle（链上 AI 预言机）是将 AI 模型推理能力嵌入区块链执行层的基础设施，使智能合约能够以可验证方式直接“调用” AI 模型，而非盲目信任外部 API 的返回値。

## 关键要点

- **核心问题**：AI 的输出是概率性的，区块链的输出是确定性的；智能合约需要对 AI 输出的可信性保证

- **Ritual 的方案**：将 AI 推理嵌入区块链执行层作为操作码（opcode），AI 模型推理附带 ZKP 或 TEE 的验证

- **运作方式**：将取烟内容发送到 AI 预言机网络，返回附带密码学证明的推理结果

- **连接两个世界**：AI 预言机可以让 DeFi 协议基于 AI 判断（而非盲目信任）执行自动化首务、滠清算等

## 典型项目

- **Ritual**：将 AI 推理嵌入层 opcode，支持 ZKP 庒验证

- **Phala Network TEE**：通过 TEE 保证 Agent 输出不可篡改

## 来源引用

- [AI Agent 堆栈的终局：去中心化算力、分布式训练与链上 AI 预言机](https://www.notion.so/d4673e86715f4c08accb8ca28fe4a248)

- 《LeviX：用五个 AI Agent 帮你读懂预测市场，电竞+AI 的大胆组合》｜X书签文章｜原文链接：[https://x.com/roger73005305/status/2039296213766520970](https://x.com/roger73005305/status/2039296213766520970)｜来源条目：[摘要：LeviX：用五个 AI Agent 帮你读懂预测市场，电竞+AI 的大胆组合](summaries/摘要：LeviX：用五个 AI Agent 帮你读懂预测市场，电竞+AI 的大胆组合.md)
