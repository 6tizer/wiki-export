---
title: Sandbox 抽象
type: concept
tags:
- Agent 编排
- 安全/隐私
status: 草稿
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/b88c0320883647f596f92433ed9184ff
notion_id: b88c0320-8836-47f5-96f9-2433ed9184ff
---

## 定义

Sandbox 抽象是把 Agent 的执行环境视为可替换的“手”，与负责推理和调度的“大脑”解耦，从而让工具环境独立部署、隔离和恢复。

## 关键要点

- 它强调 brain 与 hands 的分离

- 价值在于安全隔离、容错恢复和多环境接入

- 是托管式 Agent 基础设施里非常关键的一层系统设计

## 来源引用

- [原文链接](https://x.com/blackanger/status/2041951380836147479)｜《Anthropic 的 Agent OS 野心：从 Managed Agents 看未来 Agent 基础设施》｜源文章：Anthropic 的 Agent OS 野心：从 Managed Agents 看未来 Agent 基础设施

- [原文链接](https://x.com/dotey/status/2043904844608532640)｜《Vercel 开源了 Open Agents，一个用来搭建企业自有编程 Agent 平台的参考实现。》｜来源条目：[摘要：Vercel 开源了 Open Agents，一个用来搭建企业自有编程 Agent 平台的参考实现。](summaries/摘要：Vercel 开源了 Open Agents，一个用来搭建企业自有编程 Agent 平台的参考实现。.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652692712&idx=1&sn=608b9832517125a701a13bfd13a99cb6&chksm=f01e31dc247eca9744e9d6e321351659ba0974b8ddea7e9b635d9eb34363255c700453927790#rd)｜《OpenAI祭出GPT-5.4神装！Codex同款Harness全面开放》｜源文章：OpenAI祭出GPT-5.4神装！Codex同款Harness全面开放

- [原文链接](https://x.com/jxnlco/status/2044469127696556153)｜《Sandboxes are coming to the Agents SDK》｜源文章：OpenAI Agents SDK 沙盒：让 AI Agent 真正「留下工作成果」

## 关联概念

- [OpenAI Agents SDK](entities/OpenAI Agents SDK.md)

- [Sandbox Agents](concepts/Sandbox Agents.md)

- [编排与计算分离](concepts/编排与计算分离.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [快照与状态恢复](concepts/快照与状态恢复.md)

- [多沙盒并行](concepts/多沙盒并行.md)
