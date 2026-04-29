---
title: Environment Engineering
type: concept
tags:
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/677cc687d3b04a2f8e968eb9da7fb9ef
notion_id: 677cc687-d3b0-4a2f-8e96-8eb9da7fb9ef
---

## 定义

Environment Engineering（环境工程）是由 holaOS 团队提出的系统设计方法论，与 Harness Engineering 形成互补。其核心论点是：Harness Engineering 让单次 run 可运维，而 Environment Engineering 让工作本身变得持久（durable）、可检查（inspectable）、可移植（portable）、跨 run 一致（coherent）。

简言之：**环境定义系统**——Agent 的能力上限不由 harness 决定，而由它所处的工作环境决定。

## 关键要点

- **持久性优先**：工作状态不应随 session 结束而消失，环境必须跨 run 保持连续性

- **文件 ≠ 附件，App ≠ API 调用，Memory ≠ Prompt Stuffing**：这些都是环境表面（environment surfaces），不是临时注入

- **委托而非自动化**（Delegation > Automation）：人类负责意图、判断和审查，模型负责执行工作

- **与 Harness Engineering 的关系**：Harness 管理单次执行的运维边界，Environment 管理跨执行的工作连续性

## 与 Harness Engineering 的区别

- Harness Engineering：聚焦 run 级别——执行环境、验证机制、安全边界

- Environment Engineering：聚焦 workspace 级别——持久状态、共享上下文、长周期连续性

## 关联概念

- Harness Engineering

- Agent OS

- holaOS

## 来源引用

- [摘要：holaOS — 开源 Agent Computer](summaries/摘要：holaOS — 开源 Agent Computer.md)（[原文](https://x.com/JeliPenguin/status/2049147344315388281)）
