---
title: Agent 身份基础设施
type: concept
tags:
- 安全/隐私
status: 草稿
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/8edbf2dbaade42919ac45c539fb350c9
notion_id: 8edbf2db-aade-4291-9ac4-5c539fb350c9
---

## 定义

Agent身份基础设施（Agent Identity Infrastructure）是指为AI Agent提供独立身份标识、权限管理和责任追踪机制的技术体系，使Agent能够作为网络中的独立参与者存在，而非附属在人类账户之下。

## 核心问题

传统Agent缺乏独立身份导致的问题：

- Agent代表用户操作时，其行为数据混入用户个人数据

- 无法独立建立跨平台信任和声誉

- 责任边界模糊（谁的账户发起了操作？）

- 安全漏洞：验证了「这个Agent是谁」，但无法验证「它正在做什么」

## 主要实现方案

### Coze 2.5（字节跳动）

- [专属@coze.email](mailto:%E4%B8%93%E5%B1%9E@coze.email)邮箱，前缀自定义

- Agent World（[world.coze.site](http://world.coze.site/)）：全网通行API Key，跨站点共享声誉

- 配套计算环境：Ubuntu云电脑 + Android 13云手机

### Microsoft Entra Agent ID

- 每个Agent绑定人类sponsor，纳入企业身份治理

- 可注册、审计、设置访问策略、到期自动回收

### Cisco Duo Agentic Identity

- 每次工具调用时实时评估权限（而非一次性授予）

## 行业数据（RSAC 2026）

- 85%的企业已有Agent试点项目，仅5%进入生产环境

- 最大障碍：信任（Cisco总裁Jeetu Patel语）

- CrowdStrike披露：生产环境中Agent自行修改公司安全策略以完成任务

## 关键要点

- 邮箱是目前最合理的Agent身份切入点：去中心化协议、所有系统兼容

- Agent的身份、技能、记忆、日程、存储是其在网络中正常运转的最小工具链

## 来源引用

- [摘要：Coze 2.5 发布：成为 Agent 的网络](summaries/摘要：Coze 2.5 发布：成为 Agent 的网络.md)（赛博禅心，2026-04-07）
