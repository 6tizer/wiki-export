---
title: 摘要：mem9：让微信里的龙虾不再失忆
type: summary
tags:
- 记忆系统
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: RAG/Memory, 微信生态, OpenClaw
source_article_url: ''
notion_url: https://www.notion.so/bda9670ab68742a98fcb49050cf08ae0
notion_id: bda9670a-b687-42a9-8fcb-49050cf08ae0
---

**一句话摘衑**：mem9 是 TiDB 团队出品的开源 AI Agent 持久化记忆基础设施，通过将记忆从本地文件迁移到云端并采用两段式提取+混合搜索，实现记忆跟着人走而非跟着设备。

**关键洞察**

- 核心问题：当前 AI 工具的记忆存在本地文件里，换设备或 Agent 就丢失，不同 Agent 项目间各记各的

- 两段式提取：事实提取（只提取用户说的话）→ 记忆调和（ADD/UPDATE/DELETE/NOOP），如此最多 50 条/轮、异步处理

- 混合搜索：向量搜索+关键词搜索，底层用 TiDB Cloud 原生向量能力， jieba 分词支持中文

- 记忆脉指：按时间段检索某人/某件/某容时间发生了什么；记忆洞察：记忆间关联分析图谱

- 安装形式：发一射训指令给龙虾即可自动安装，内置 hooks 自动于 Agent 备起动/工作过程/结束时存取记忆

**提取的概念**

- mem9（云端 AI Agent 持久化记忆基础设施）

**原始文章信息**

- 作者：AGI Hunt | 来源：微信公众号 | 发布时间：2026-03-23

- 链接：[https://mp.weixin.qq.com/s?__biz=MzA4NzgzMjA4MQ==&mid=2453481812](https://mp.weixin.qq.com/s?__biz=MzA4NzgzMjA4MQ%3D%3D&mid=2453481812)

**个人评注**

与 Tizer 的 OpenClaw 项目高度相关。mem9 就是专门解决龙虾失忆问题的。安装方式非常优雅（一句话龙虾安装）且小山可以自部署，值得实际尝试。
