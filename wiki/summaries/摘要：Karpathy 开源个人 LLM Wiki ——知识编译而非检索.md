---
title: 摘要：Karpathy 开源个人 LLM Wiki ——知识编译而非检索
type: summary
tags:
- 知识管理
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: LLM, 自动化, Cursor, Agent, Karpathy, wiki
source_article_url: ''
notion_url: https://www.notion.so/91dec1d35de54bb6aaaf73086d9d6462
notion_id: 91dec1d3-5de5-4bb6-aaaf-73086d9d6462
---

**一句话摘要**：Karpathy 开源了一套用 LLM “编译”而非“检索”知识的三层架构（raw/层 + Wiki层 + Schema层），实现知识的持续保鲜而非每次查询重新推导。

**关键洞察**

- **与 RAG 的差异**：RAG 是每次查询重新发现知识，LLM Wiki 是挂载资料后一次编译、持续保鲜，查询带引用和回写 Wiki

- **三层架构**：raw/（只读原始资料）+ Wiki（LLM 生成的 Markdown）+ Schema（[AGENTS.md/CLAUDE.md——把](http://agents.md/CLAUDE.md——把) LLM 从聊天机器人变成 Wiki 维护者的关键）

- **日常操作**：灰入（一份资料可触发 10-15 个页面更新）、提问（好答案可被归档回 Wiki）、巡检（定期让 LLM 对 Wiki 做一次体检）

- **Farzapedia 实践**：Farza 用 2500 条日记 + Apple Notes 生成了 400 篇带反向链接的个人知识库，供 Agent 在设计能铺时参考个人奇好和履历

- **工具推荐**：Obsidian（IDE）+ LLM（程序员）+ Wiki（代码库）；Obsidian Web Clipper、qmd、Marp

**提取的概念**

- LLM Wiki（Karpathy 知识编译架构）

- [AGENTS.md](http://agents.md/) / [CLAUDE.md](http://claude.md/) Schema 层

- Farzapedia（个人 知识库模式）

**原始文章信息**

- 作者：AGI Hunt

- 来源：微信公众号

- 发布时间：2026-04-05

- 链接：[https://mp.weixin.qq.com/s?__biz=MzA4NzgzMjA4MQ==&mid=2453482392](https://mp.weixin.qq.com/s?__biz=MzA4NzgzMjA4MQ%3D%3D&mid=2453482392)

**个人评注**：这篇文章与 Tizer 的 Wiki Compiler Agent 直接相关——当前运行的 Wiki Compiler 就是这个架构的 Notion 实现。Karpathy 的 Schema 层概念、知识层级设计和 Farzapedia 模式都对优化现有流程有高度参考价值。
