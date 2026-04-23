---
title: Pipeline 模式
type: concept
tags:
- Agent 技能
- Coding Agent
status: 审核中
confidence: high
last_compiled: '2026-04-19'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/13604da362ff4044b8e2e1de49f7f892
notion_id: 13604da3-62ff-4044-b8e2-e1de49f7f892
---

## 定义

Pipeline 模式是把多步骤任务拆成必须按顺序完成的阶段，并为每个阶段设置输入、输出和检查点。

## 关键要点

- 解决大模型喜欢跳步、合并步骤的问题

- 适合需要审计性和阶段控制的任务

- 本质是把流程约束显式写进 Skill

## 来源引用

- [原文链接](https://x.com/KKaWSB/status/2034196862794961299)｜《Google 发布 5 个 Agent Skill 设计模式：告别乱写 [SKILL.md](http://skill.md/) 的时代》

- [原文链接](https://x.com/oragnes/status/2034221173970796776)｜《Google Cloud 的 5 种 [SKILL.md](http://skill.md/) 设计模式：让 AI 编程助手更听话的「抄作业」指南》

- [摘要：我翻了 Codex App的插件后，开始相信 skills pipeline 才是 AI 系统的主线](summaries/摘要：我翻了 Codex App的插件后，开始相信 skills pipeline 才是 AI 系统的主线.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI4MTIzNDE2NA%3D%3D&mid=2247484788&idx=1&sn=cba1aa9f29e886f730d0178eef8f1a03&chksm=ea5f4895b2405b442b52d72b68edbdd49a7375e2eb08bb943ca674778d50fd46582b0fd37b90#rd)）

## 关联概念

- [Skills Pipeline](concepts/Skills Pipeline.md)

- [Persona Pattern](concepts/Persona Pattern.md)

- [Agent Runtime](concepts/Agent Runtime.md)
