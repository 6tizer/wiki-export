---
title: NemoClaw
type: entity
tags:
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/21b78950c2674a46b5989d028f1a4441
notion_id: 21b78950-c267-4a46-b598-9d028f1a4441
---

## 定义

NemoClaw是NVIDIA于2026年推出的实时Agent行为拦截治理工具，将监督移到行动发生的瞬间，而非事后审查。

## 核心要点

- **实时拦截**：Agent尝试连接一个不在预批准列表里的网络端点时，请求被阻止并实时展示给人类操作员批准或拒绝

- **商业策略**：默认路由到Nemotron 3 Super 120B，将NVIDIA变成所有受治理OpenClaw部署的默认推理提供商

- **局限**：规模化后（几百个Agent、每小时几千个连接请求），审批要么退化成橡皮图章，要么变成瓶颈

- **治理创新**：前七个系统的监督都是事后的，NemoClaw把监督移到了行动的瞬间

## 在可进化性阶梯的位置

治理工具，不在阶梯内，而是阶梯的外部约束框架

## 来源引用

- [摘要：循环即实验室：八个 AI 自主研究系统横评](summaries/摘要：循环即实验室：八个 AI 自主研究系统横评.md)（赛博禅心，微信，2026-04-10，NVIDIA官方文档）

- [摘要：OpenClaw：Jensen Huang 口中「下一个 Linux」，Agent 时代的操作系统](summaries/摘要：OpenClaw：Jensen Huang 口中「下一个 Linux」，Agent 时代的操作系统.md)（[原文](https://x.com/Voxyz_ai/status/2034334016711626766)，X书签）
