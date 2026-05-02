---
title: TEE 可信执行环境
type: concept
tags:
- 加密资产
- Agent 安全
- 算力基础设施
status: 审核中
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c9c00c8eb00942a79f033dde2e6be35e
notion_id: c9c00c8e-b009-42a7-9f03-3dde2e6be35e
---

TEE（Trusted Execution Environment，可信执行环境）是处理器内部的硬件隔离安全区域，其中运行的代码和数据即使对宿主机操作系统和管理员也不可读取或篡改。

## 核心技术特性

- **硬件级隔离**：基于 Intel TDX（Trust Domain Extensions）、AMD SEV 等处理器技术实现

- **远程证明**：通过密码学方法对外证明代码确实在 TEE 中运行，实现可验证性

- **确定性密钥派生**：通过 KMS 实现，同一 Agent 实例重启后可恢复同一钱包

## Web3/AI Agent 应用

TEE 在链上 AI Agent 场景中解决了核心信任问题：如何证明 Agent 是真正自主运行的，没有后门？

**Phala Network dstack**（基于 Intel TDX）是目前最广泛使用的 Web3 TEE 实现：

- Agent 私钥在 TEE 内生成，连开发者也无法访问

- 代币发射/分发流程完全自主执行（aiPool 的实现方式）

- AI Agent 行为可验证（[Spore.fun](http://spore.fun/) 的信任保障）

- 支持 Docker 容器形式部署，对开发者友好

## 与其他隐私技术对比

- **TEE（硬件级）**：数据在安全硬件内集中处理，速度快但依赖硬件可信度

- **MPC（多方安全计算）**：多方协作计算，各方不暴露输入，无需特殊硬件

- **FHE（同态加密）**：对密文直接计算，计算开销大

- **ZKP（零知识证明）**：证明知道某事而不泄露内容，适合验证场景

## 来源引用

- 摘要：aiPool：用 TEE 打造无需信任的 AI Agent 代币发射台

- 摘要：ELIZA：从推特机器人到 AI Agent 操作系统

- 摘要：[Spore.fun](http://spore.fun/)：Adam 与 Eve 的双线进化

- 摘要：Nillion：为 AI Agent 个性化而生的「盲计算」基础设施

- 摘要：AI Agent 堆栈的终局：去中心化算力、分布式训练与链上 AI 预言机

- [Beginners' Guide to Privacy](https://defi0xjeff.substack.com/p/beginners-guide-to-privacy) — 源文章：Web3 隐私入门全景报告：从混币器到 Privacy 2.0，一文读懂链上隐私革命

- [摘要：用一个App统一管理所有AI的记忆和技能](summaries/摘要：用一个App统一管理所有AI的记忆和技能.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI5MTEwMDgyMA%3D%3D&mid=2247484252&idx=1&sn=170e13385d8b9279d9635415b3bd4c1e&chksm=ed55f24b6cf7d8cdcffcb566a0fea0d5c7099bfd12cda305d4304211ada2618d72fd82c575d7#rd)）

## 关联概念

- [Clawdi](entities/Clawdi.md)

- [BYOA 模式](concepts/BYOA 模式.md)

- [Privacy 2.0](concepts/Privacy 2.0.md)

- [选择性披露](concepts/选择性披露.md)

- [零知识证明](concepts/零知识证明.md)

- [多方计算](concepts/多方计算.md)

- [全同态加密](concepts/全同态加密.md)
