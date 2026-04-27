---
title: 摘要：40 Claude Cowork Commands, Workflows & Automations Most Users Don't Know
  — The Complete List
type: summary
tags:
- 内容自动化
- AI 产品
status: 已审核
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b688127bdb1e81908c22471
notion_url: https://www.notion.so/Tizer/a592c4f767494671b7383ec5636ccfb8
notion_id: a592c4f7-6749-4671-b738-3ec5636ccfb8
---

## 一句话摘要

本文列举了 40 个 Claude Cowork 的 slash 命令、文件操作工作流、多服务连接器链和定时自动化方案，试图展示 Cowork 作为「自主操作系统」而非简单聊天助手的全部能力。

## 关键洞察

- **Slash 命令体系**：/schedule（定时任务）、/compact（上下文压缩）、/plan（强制规划模式）、/memory（调试上下文加载）、/cost（Token 预估）等命令构成 Cowork 的核心交互层，多数用户仅使用自然语言而忽略了命令行能力

- **文件系统智能操作**：Cowork 可实现批量智能重命名（根据文件内容生成描述）、近似去重、混乱文件夹自动整理、过期归档等，超越简单文件管理

- **Connector 多源工作流**：通过连接 Gmail、Google Drive、Slack、Calendar 等服务，可构建「Gmail → 摘要 → Drive」「Calendar → 会议准备简报」「Slack → Action Items」等跨平台自动化链

- **文档内容再加工**：支持语音转录 → 成稿、会议录音 → 结构化笔记、多篇研究 → 高管摘要、合同 → 白话解读等文档处理流水线

- **定时自动化模式**：支持每日收件箱清零、每周文件清理、周一计划简报、月度财务整理、竞品扫描等周期性任务，需保持电脑开启和 Claude Desktop 运行

> ⚠️ 可信度说明：回复线程中有用户指出，部分命令（/compact、/clear、/plan、/memory、/cost）实际属于 Claude Code 而非 Cowork，/undo 命令未经证实，"Product Management plugin" 不存在，slash command 系统尚在开发中。文章实用建议有价值，但具体命令可用性需独立验证。

## 提取的概念

- [Claude Cowork](entities/Claude Cowork.md)（本文核心产品）

- [Claude Cowork Skills](concepts/Claude Cowork Skills.md)（slash 命令即 skill 的扩展形态）

- [Connector 上下文接入](concepts/Connector 上下文接入.md)（多服务连接器工作流）

- [Scheduled Run](concepts/Scheduled Run.md)（定时自动化任务模式）

## 原始文章信息

- **作者**：@eng_khairallah1 (Khairallah AL-Awady)

- **来源**：X 书签

- **发布时间**：2026-04-24

- **原文链接**：[X 推文](https://x.com/eng_khairallah1/status/2047609433489035739)

## 个人评注

Cowork 的 Connector 多源工作流思路（Gmail→摘要→Drive、Slack→Action Items）与 Tizer 的内容自动化管线有共鸣——当前 Wiki Compiler 本质上也是一个「源数据库 → 结构化知识」的自动化链。文章中「Content Repurposing Pipeline」（一篇内容 → 8 条推文 + 2 条 LinkedIn + newsletter）的模式可借鉴到 OpenClaw 的内容分发流程。不过文章准确性存疑（部分命令混淆了 Claude Code 和 Cowork），引用时需注意区分。
