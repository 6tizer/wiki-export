---
title: rOS
type: concept
tags:
- 知识管理
status: 草稿
confidence: medium
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/c2dfa991fb4a4469861aa178a27115ee
notion_id: c2dfa991-fb4a-4469-861a-a178a27115ee
---

**定义**

rOS 是 remio 公司（前网易副总裁汪源创办）发布的 Agent 原生操作系统，让软件的第一服务对象从人变为 Agent，为 aApp 提供完整的运行底座和个人数字记忆体系。

**核心设计哲学**

- 传统软件：以人为核心，设计 GUI 降低人的使用门槛

- rOS：以 Agent 为核心，软件只需提供语义清晰的接口，无需复杂图形界面

- 结果：软件不再需要"大而全"的套件，Agent 可自由组合不同厂商的最优 aApp

**关键能力**

- **个人上下文工程**：整合网页、文档、会议录音、聊天消息等多源信息，构建结构化的个人数字记忆体，供 aApp 直接调用

- **数据主权**：所有数据在用户本地完成处理，只有调用云端 LLM API 的必要内容会离开本地

- **文件操作安全**：实时拦截 Agent 的所有文件读写/修改/删除，支持历史版本一键回滚

- **实时订阅**：aApp 能第一时间响应用户工作内容变化

**商业模式**

- 运营商式 Token 结算：平台统一和用户结算消耗，开发者无需承担 Token 成本

- aApp 生态：内置著作权管理和签名鉴权，解决 Skill 盗版问题，行业专家可直接商业化 know-how

- 分级会员体系

**竞争定位**

- 对标 OpenClaw：rOS 目标是"iPhone/Mac"式开箱即用，OpenClaw 是"Linux"式需要技术门槛的搭建框架

**来源引用**

- [摘要：从知识库到 Agent 原生 OS，汪源想为 Agent 造一个操作系统](summaries/摘要：从知识库到 Agent 原生 OS，汪源想为 Agent 造一个操作系统.md)（极客公园，2026-04-02）
