---
title: 子 Agent 生成陷阱
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/312fde64ece142caa09865a74c17a9fa
notion_id: 312fde64-ece1-42ca-a098-65a74c17a9fa
---

## 定义

子 Agent 生成陷阱是指攻击者诱导父 Agent 在编排流程中实例化一个带有恶意系统提示、恶意目标或不受信任配置的子 Agent，使后者在继承上层信任与权限后为攻击者执行任务。

## 关键要点

- 攻击面出现在多 Agent 编排与任务委派链路，而不是单一模型回答阶段

- 恶意子 Agent 往往伪装成审查器、助手、执行器等“合理角色”进入控制流

- 一旦父 Agent 默认信任子 Agent 输出，攻击者就能借系统内部协作链放大权限

## 来源引用

- [摘要：Google Deepmind论文解读：如何给AI Agent 投毒](summaries/摘要：Google Deepmind论文解读：如何给AI Agent 投毒.md)（[原文](https://x.com/vista8/status/2046038788582088830)）
